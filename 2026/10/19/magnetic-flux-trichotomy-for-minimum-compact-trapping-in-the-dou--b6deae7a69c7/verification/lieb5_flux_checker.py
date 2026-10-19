"""Reproduce compact-state support tests for a flux-threaded Lieb-5 lattice.

Infinite lattice is represented on a finite open rectangle large enough to
contain the test pattern. No finite-size spectral claim is inferred.
"""
import itertools
import cmath
import numpy as np


def edges_grid(nx=5, ny=4):
    verts=[(x,y) for y in range(ny) for x in range(nx)]
    ed=[]
    for x,y in verts:
        if x+1<nx: ed.append(((x,y),(x+1,y),'x'))
        if y+1<ny: ed.append(((x,y),(x,y+1),'y'))
    return verts,ed


def edge_phase(u,direction,phi):
    return 0.0 if direction=='x' else u[0]*phi


def incidence(edge_set,phi,sign=-1):
    vs=sorted(set(v for u,w,d in edge_set for v in (u,w)))
    idx={v:i for i,v in enumerate(vs)}
    C=np.zeros((len(vs),len(edge_set)),dtype=complex)
    for j,(u,w,d) in enumerate(edge_set):
        C[idx[u],j]=1
        C[idx[w],j]=sign*cmath.exp(1j*edge_phase(u,d,phi))
    return C


def theta_edges():
    e=[]
    for y in (0,1):
        for x in (0,1): e.append(((x,y),(x+1,y),'x'))
    for x in (0,1,2):e.append(((x,0),(x,1),'y'))
    return e


def rectangle_edges():
    e=[]
    for y in (0,1):
        for x in (0,1):e.append(((x,y),(x+1,y),'x'))
    for x in (0,2):e.append(((x,0),(x,1),'y'))
    return e


def square_edges():
    return [((0,0),(1,0),'x'),((0,1),(1,1),'x'),
            ((0,0),(0,1),'y'),((1,0),(1,1),'y')]


def full_matrix_and_state(embedded_edges,phisign,phi,nx=5,ny=4):
    v_all,e_all=edges_grid(nx,ny)
    vi={v:i for i,v in enumerate(v_all)}
    ei={e:i for i,e in enumerate(e_all)}
    H=np.zeros((len(v_all)+2*len(e_all),)*2,dtype=complex)
    for j,(u,w,d) in enumerate(e_all):
        a=len(v_all)+2*j;b=a+1
        links=[(vi[u],a,1),(a,b,1),(vi[w],b,cmath.exp(1j*edge_phase(u,d,phi)))]
        for c,k,wgt in links:
            H[c,k]=wgt;H[k,c]=wgt.conjugate()
    C=incidence(embedded_edges,phi,sign=phisign)
    _,S,vh=np.linalg.svd(C,full_matrices=True)
    rank=int(sum(S>1e-9)); null=vh.conj().T[:,rank:]
    if not null.shape[1]: return None
    x=null[:,0]
    vec=np.zeros(H.shape[0],dtype=complex)
    # E=+1: inner amplitudes equal, C sign +1; E=-1: opposite, C sign -1.
    for j,e in enumerate(embedded_edges):
        p=len(v_all)+2*ei[e]
        vec[p]=x[j]
        vec[p+1]=phisign*x[j]
    return (np.linalg.norm(H@vec-phisign*vec),len([z for z in vec if abs(z)>1e-8]),null.shape[1],np.min(np.abs(x)))


if __name__=='__main__':
    for ph, pat, n in [(0,square_edges(),8), (np.pi,rectangle_edges(),12),
                      (np.pi/2,theta_edges(),14),(2*np.pi/3,theta_edges(),14),
                      (np.sqrt(2),theta_edges(),14)]:
        for s in (-1,1):
            res=full_matrix_and_state(pat,s,ph)
            assert res is not None,(ph,s)
            err,k,d,lo=res
            assert err<1e-12 and k==n and d>=1 and lo>1e-9,(ph,s,res)
            print('phi=',round(ph,8),'sign=',s,'error=',round(err,14),
                  'occupied=',k,'kernel_dimension=',d,'minimum_edge_coefficient=',round(float(lo),9))
    # All small subgraphs with minimum degree >=2 in a finite square window.
    # Necessary condition for a nonzero divergence-free vector on its support.
    verts,edges=edges_grid(4,4)
    valid={j:0 for j in range(1,7)}
    cyclic={j:set() for j in range(1,7)}
    for k in range(1,7):
        for ix in itertools.combinations(range(len(edges)),k):
            deg={}
            for i in ix:
                u,v,_=edges[i];deg[u]=deg.get(u,0)+1;deg[v]=deg.get(v,0)+1
            if any(d<2 for d in deg.values()):continue
            valid[k]+=1
            cyclic[k].add((len(deg),len(ix)))
    print('candidate support graph counts',valid,'(vertices,edges)',cyclic)
    assert valid[1]==valid[2]==valid[3]==valid[5]==0
    assert cyclic[4]=={(4,4)} and cyclic[6]=={(6,6)}
