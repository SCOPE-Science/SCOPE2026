"""Separate finite-dimensional checks for the complete-bipartite two-particle Grover walk.

Requires Python 3 and numpy; no network or external data.
"""
import math
import numpy as np


def build_walk(m, n):
    vertices = list(range(m+n))
    neighbors = {v:([m+j for j in range(n)] if v<m else list(range(m))) for v in vertices}
    arcs = [(v,w) for v in vertices for w in neighbors[v]]
    idx={a:i for i,a in enumerate(arcs)}
    incoming={v:[idx[(w,v)] for w in neighbors[v]] for v in vertices}
    # Full two-particle amplitudes in the ordered directed-arc basis.
    def step(P):
        sums=np.zeros((m+n,m+n),dtype=P.dtype)
        for v in vertices:
            for w in vertices:
                sums[v,w]=sum(P[i,j] for i in incoming[v] for j in incoming[w])
        Q=np.empty_like(P)
        for r,(v,w) in enumerate(arcs):
            for s,(x,y) in enumerate(arcs):
                Q[r,s]=2*sums[v,x]/(len(neighbors[v])*len(neighbors[x]))-P[idx[(w,v)],idx[(y,x)]]
        return Q
    return arcs,idx,step


def spectrum(m,n,t):
    N=m*n
    q=2*math.sqrt((m-1)*(n-1))/N
    a=(1+math.sqrt(max(0,1-4*q*q)))/2
    b=1-a
    if t%4==0:
        result=[.5,.5]
    elif t%2:
        result=[a/2,a/2,b/2,b/2]
    else:
        result=[a*a/2,a*a/2,b*b/2,b*b/2]+[q*q/2]*4
    return np.array(sorted((x for x in result if x>1e-13),reverse=True))


def main():
    checks=0
    for m,n in [(1,1),(1,2),(2,1),(2,2),(2,3),(3,2),(2,4),(3,3),(3,4),(4,3),(4,4)]:
        arcs,ix,step=build_walk(m,n)
        A=len(arcs)
        N=m*n
        ra=[ix[(i,m+j)] for i in range(m) for j in range(n)]
        rb=[ix[(m+j,i)] for i in range(m) for j in range(n)]
        uu=np.ones(N)
        pp=np.array([float(i==0) for i in range(m) for j in range(n)])
        vv=np.array([float(j==0) for i in range(m) for j in range(n)])
        ee=np.zeros(N);ee[0]=1
        E=np.outer(ee,ee)
        B2=(E+4/N**2*np.outer(uu,uu)-2/N*(np.outer(pp,vv)+np.outer(vv,pp)))/math.sqrt(2)
        e=ix[(0,m)]
        rev=ix[(m,0)]
        for sign in (1,-1):
            P=np.zeros((A,A),dtype=float)
            P[e,rev]=1/math.sqrt(2)
            P[rev,e]=sign/math.sqrt(2)
            for t in range(5):
                if t%4==0: B=E/math.sqrt(2)
                elif t%4==1: B=sign*(2/N*np.outer(pp,vv)-E)/math.sqrt(2)
                elif t%4==2: B=B2
                else: B=sign*(2/N*np.outer(vv,pp)-E)/math.sqrt(2)
                assert np.max(abs(P[np.ix_(ra,rb)]-B))<1e-10,(m,n,t,sign,'explicit block')
                checks+=1
                eig=np.linalg.eigvalsh(P@P.T)
                eig=np.sort(eig)[::-1]
                expect=spectrum(m,n,t)
                assert np.max(np.abs(eig[:len(expect)]-expect))<1e-10,(m,n,t,sign,eig,expect)
                assert (len(eig)==len(expect) or np.max(abs(eig[len(expect):]))<1e-10),(m,n,t,sign,eig)
                assert abs(np.linalg.norm(P)**2-1)<1e-10
                assert np.max(abs(P-sign*P.T))<1e-10
                checks+=4
                if t<4: P=step(P)
            P0=np.zeros((A,A));P0[e,rev]=1/math.sqrt(2);P0[rev,e]=sign/math.sqrt(2)
            assert np.max(abs(P-P0))<1e-10,(m,n,sign,np.max(abs(P-P0)))
            checks+=1
    print('VERIFY_OK',checks,'matrix identities',len([(1,1),(1,2),(2,1),(2,2),(2,3),(3,2),(2,4),(3,3),(3,4),(4,3),(4,4)]),'graph sizes')

if __name__=='__main__': main()
