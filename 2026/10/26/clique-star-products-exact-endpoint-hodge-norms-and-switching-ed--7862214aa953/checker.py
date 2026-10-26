"""Exact checks for cut/cycle edge-projection norms on clique--star products.
Requires Python 3 and sympy. No external inputs or network calls.
"""
import sympy as S
from itertools import combinations

def claimed(m,k):
    m,k=S.sympify(m),S.sympify(k)
    hc=2*(2*k*m-k+m*m-1)/(m*(k+m+1))
    hl=2*(k*m*m+2*k*m-k+m**3+2*m*m-2*m-1)/(m*(m+1)*(k+m+1))
    v=(5*k*m-3*k+3*m*m-2*m+3)/((m+1)*(k+m+1))
    phc=(5*k*m-2*k+3*m*m-3*m-6)/(m*(k+m+1))
    phl=(3*k*m-2*k+3*m*m-m-6)/(m*(k+m+1))
    pv=2*(m-1)*(3*k+2*m-1)/((m+1)*(k+m+1))
    return {'hub':(hc,phc),'leaf':(hl,phl),'spoke':(v,pv)}

def graph_check(m,k):
    vertices=[(i,t) for i in range(m) for t in range(k+1)]
    p={v:i for i,v in enumerate(vertices)}
    edges=[]
    for t in range(k+1):
        for i,j in combinations(range(m),2):edges.append((p[i,t],p[j,t], 'hub' if t==0 else 'leaf'))
    for i in range(m):
        for t in range(1,k+1):edges.append((p[i,0],p[i,t], 'spoke'))
    N=len(vertices)
    # Ground the last vertex. This yields exactly the same edge-current
    # projector as the Moore--Penrose Laplacian pseudoinverse.
    D=S.zeros(N-1,len(edges))
    for a,(u,v,typ) in enumerate(edges):
        if u<N-1:D[u,a]=1
        if v<N-1:D[v,a]=-1
    L=D*D.T
    Q=D.T*L.inv()*D
    typvals={}
    for j,(_,_,typ) in enumerate(edges):
        x=sum(abs(Q[i,j]) for i in range(len(edges)))
        y=1+x-2*Q[j,j]
        if typ in typvals:assert typvals[typ]==(x,y),(m,k,typ,typvals[typ],x,y)
        else:typvals[typ]=(x,y)
    exp=claimed(m,k)
    assert set(typvals)==set(exp)
    for typ in exp:assert typvals[typ]==exp[typ],(m,k,typ,typvals[typ],exp[typ])
    assert Q*Q==Q
    return len(edges)

def symbolic_check():
    m,k=S.symbols('m k',integer=True,positive=True)
    c=claimed(m,k)
    D=m*(m+1)*(m+k+1)
    aq=k*(m*m-5*m+2)+m**3-4*m*m+5*m+2
    ap=k*(m*m-9*m+2)+m**3-6*m*m+11*m+6
    identities=[
        c['hub'][0]-c['spoke'][0]+aq/D,
        c['hub'][1]-c['spoke'][1]+ap/D,
        c['hub'][0]-c['leaf'][0]-2*(k-1)*(m-1)/((m+1)*(m+k+1)),
        c['hub'][1]-c['leaf'][1]-2*(k-1)/(m+k+1),
    ]
    assert all(S.cancel(x)==0 for x in identities)
    for M in range(2,30):
        for K in range(3,100):
            aqv=aq.subs({m:M,k:K})
            apv=ap.subs({m:M,k:K})
            q=sorted(((v[0],typ) for typ,v in claimed(M,K).items()),reverse=True)[0][0]
            p=sorted(((v[1],typ) for typ,v in claimed(M,K).items()),reverse=True)[0][0]
            assert q == max(c['hub'][0].subs({m:M,k:K}),c['spoke'][0].subs({m:M,k:K}))
            assert p == max(c['hub'][1].subs({m:M,k:K}),c['spoke'][1].subs({m:M,k:K}))
            assert S.sign(aqv)==S.sign((c['spoke'][0]-c['hub'][0]).subs({m:M,k:K}))
            assert S.sign(apv)==S.sign((c['spoke'][1]-c['hub'][1]).subs({m:M,k:K}))
    print('SYMBOLIC_IDENTITIES_OK')

def main():
    symbolic_check()
    total=0
    configs=[(2,3),(2,4),(3,3),(3,4),(4,3),(4,4),(5,3),(6,3),(6,5)]
    for m,k in configs:
        total+=graph_check(m,k)
    print(f'CLIQUE_STAR_CERTIFICATE_OK configurations={len(configs)} exact_columns={total}')

if __name__=='__main__':main()
