"""Exact-rational verification for balanced complete multipartite edge-flow projections.
Run: python balanced_multipartite_checker.py
Only finite supplementary checks; the unrestricted proof is analytical.
"""
from fractions import Fraction as Q

def check(r,q):
    n=r*q
    E=[(u,v) for u in range(n) for v in range(u+1,n) if u//q!=v//q]
    m=len(E)
    den=r*q*q*(r-1)
    a=Q(r*q-1,den)
    b=Q(1,den)
    # Potential for input oriented edge u->v (and D column delta_u-delta_v).
    def potential(u,v,w):
        if w==u:return a
        if w==v:return -a
        if w//q == u//q:return -b
        if w//q == v//q:return b
        return Q(0)
    # Build P using potentials: P[f,e] = potential(head_f)-potential(tail_f).
    P=[[potential(*E[e],*E[f][:1]) - potential(*E[e],E[f][1]) for e in range(m)] for f in range(m)]
    # sign convention: P[f,e]=(delta_head-delta_tail) dot L^+ (delta_u-delta_v); using u-v. chosen P difference(u_f)-difference(v_f).
    assert all(P[i][j]==P[j][i] for i in range(m) for j in range(m))
    # direct consistency of incidence: P D^T x = D^T x using random integer vertex potentials.
    for s in range(3):
        x=[Q((j*j+3*s*j+7*j*s*s)%17-8) for j in range(n)]
        y=[x[u]-x[v] for u,v in E]
        assert [sum(P[i][j]*y[j] for j in range(m)) for i in range(m)]==y
    # full exact idempotence finite check
    for i in range(m):
        for j in range(m):
            assert sum(P[i][k]*P[k][j] for k in range(m)) == P[i][j]
    # verify all column l1 norms and stated formula
    C=Q(2*(q*q*r*r-q*q-2*q*r+2),q*q*r*(r-1))
    Z=Q(3*q*q*r*r-q*q*r-2*q*q-8*q*r+8,q*q*r*(r-1))
    for j in range(m):
        assert sum(abs(P[i][j]) for i in range(m))==C
        assert sum(abs((Q(i==j)-P[i][j])) for i in range(m))==Z
    return m,C,Z

if __name__=='__main__':
    for r,q in [(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(4,3),(5,2),(5,3)]:
        m,c,z=check(r,q)
        print(r,q,m,str(c),str(z))
    print('CHECK_OK')
