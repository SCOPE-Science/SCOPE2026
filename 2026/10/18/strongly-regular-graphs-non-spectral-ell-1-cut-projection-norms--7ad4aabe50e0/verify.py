#!/usr/bin/env python3
"""Exact arithmetic checks for canonical cut/cycle edge projections on strongly regular graphs."""
from fractions import Fraction
from itertools import combinations, product


def graph_rook(q=4):
    V=list(product(range(q), repeat=2))
    E=[(i,j) for i,j in combinations(range(len(V)),2) if V[i][0]==V[j][0] or V[i][1]==V[j][1]]
    return V,E


def graph_shrikhande():
    V=list(product(range(4),repeat=2)); S={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    E=[(i,j) for i,j in combinations(range(len(V)),2) if ((V[i][0]-V[j][0])%4,(V[i][1]-V[j][1])%4) in S]
    return V,E


def graph_cycle(n):
    V=list(range(n));E=[(i,j) for i,j in combinations(V,2) if min((j-i)%n,(i-j)%n)==1]
    return V,E


def graph_petersen():
    V=list(combinations(range(5),2));E=[(i,j) for i,j in combinations(range(10),2) if not (set(V[i]) & set(V[j]))]
    return V,E


def graph_triangular(n):
    V=list(combinations(range(n),2));E=[(i,j) for i,j in combinations(range(len(V)),2) if (set(V[i]) & set(V[j]))]
    return V,E


def graph_complete_bipartite(n):
    V=list(range(2*n));E=[(i,j) for i in range(n) for j in range(n,2*n)]
    return V,E


def verify(name,graph,display=False):
    V,E=graph;n=len(V);m=len(E)
    N=[set() for _ in range(n)]
    for u,v in E:
        N[u].add(v);N[v].add(u)
    k=len(N[0]);assert 2<=k<n-1 and all(len(N[u])==k for u in range(n))
    lam={len(N[u]&N[v]) for u,v in combinations(range(n),2) if v in N[u]}
    mu={len(N[u]&N[v]) for u,v in combinations(range(n),2) if v not in N[u]}
    assert len(lam)==len(mu)==1,(name,lam,mu)
    lam=lam.pop();mu=mu.pop();assert mu>0
    h=k-lam+mu-1;D=k*h+mu
    assert h>=1 and D>2*h
    wing_sums=[];cut_nums=[];cyc_nums=[];diags=[]
    for x,y in E:
        X=N[x]-N[y]-{y};Y=N[y]-N[x]-{x}
        assert len(X)==len(Y)==k-lam-1
        eX=sum(u in X and v in X for u,v in E)
        eY=sum(u in Y and v in Y for u,v in E)
        vnum=[(h+1)*((v==x)-(v==y))+(x in N[v])-(y in N[v]) for v in range(n)]
        # (kI-A) v = D (delta_x-delta_y) exact integer check
        Lv=[k*vnum[v]-sum(vnum[u] for u in N[v]) for v in range(n)]
        assert Lv==[D*((v==x)-(v==y)) for v in range(n)]
        qnums=[vnum[u]-vnum[v] for u,v in E]
        diag=qnums[E.index((x,y))]
        assert diag==2*h
        qnum=sum(abs(z) for z in qnums)
        cnum=sum(abs(D*(i==E.index((x,y)))-z) for i,z in enumerate(qnums))
        pred=2*k*(h-1)+2*(k-2)*(k-lam)+4-2*(eX+eY)
        assert qnum==pred,(name,(x,y),qnum,pred)
        assert cnum==D+qnum-4*h
        wing_sums.append(eX+eY);cut_nums.append(qnum);cyc_nums.append(cnum);diags.append(diag)
    assert min(cut_nums)==(2*k*(h-1)+2*(k-2)*(k-lam)+4-2*max(wing_sums))
    assert max(cut_nums)==(2*k*(h-1)+2*(k-2)*(k-lam)+4-2*min(wing_sums))
    Q=Fraction(max(cut_nums),D);C=Fraction(max(cyc_nums),D)
    if display:print('%s: SRG %s, edges=%s, wing_sums=%s, cut_norm=%s, cycle_norm=%s, diagonal=%s, all_columns_verified=%d'%(name,(n,k,lam,mu),m,sorted(set(wing_sums)),Q,C,Fraction(diags[0],D),m))
    return Q,C,sorted(set(wing_sums))


def main():
    tests=[('C5',graph_cycle(5)),('Petersen',graph_petersen()),('triangular T5',graph_triangular(5)),('K3,3',graph_complete_bipartite(3)),('rook 4x4',graph_rook()),('Shrikhande',graph_shrikhande())]
    out={name:verify(name,g,True) for name,g in tests}
    assert out['rook 4x4']==(Fraction(9,4),Fraction(21,8),[6])
    assert out['Shrikhande']==(Fraction(19,8),Fraction(11,4),[4])
    assert out['Shrikhande'][0]-out['rook 4x4'][0]==Fraction(1,8)
    assert out['Shrikhande'][1]-out['rook 4x4'][1]==Fraction(1,8)
    print('ALL_EXACT_CHECKS_PASS')


if __name__=='__main__':main()
