"""Exact finite-graph checks for a regular territorial-occupancy replacement law.

No external dependencies. The theorem for all degrees is analytic; these are
independent exact-arithmetic consistency tests, not a finite proof of it.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def graphs():
    def cycle(n):
        return [set(((i-1) % n, (i+1) % n)) for i in range(n)]
    def biclique(d):
        return [set(range(d, 2*d)) for _ in range(d)] + [set(range(d)) for _ in range(d)]
    def cube():
        return [{i ^ (1 << k) for k in range(3)} for i in range(8)]
    def prism():
        return [set(((i//3)*3+(i%3+1)%3, (i//3)*3+(i%3+2)%3, (1-i//3)*3+i%3)) for i in range(6)]
    return [('cycle5', cycle(5)), ('cycle6',cycle(6)),
            ('biclique3', biclique(3)),('cube',cube()),
            ('triangular_prism',prism()), ('biclique4', biclique(4))]


def occupant_probs(adj, h):
    n=len(adj); d=len(adj[0]); denominator=h+d
    return [[(h if i == m else F(1)) / denominator if (i==m or m in adj[i])
             else F(0) for m in range(n)] for i in range(n)]


def direct_weights(adj, h):
    n=len(adj); pp=occupant_probs(adj,h)
    w=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for m in range(n):
            other=[k for k in range(n) if k!=i and pp[k][m]]
            w[i][i]+=pp[i][m]*__import__('functools').reduce(lambda x,k:x*(1-pp[k][m]),other,F(1))
        for j in range(i+1,n):
            for m in range(n):
                if not pp[i][m] or not pp[j][m]: continue
                others=[k for k in range(n) if k!=i and k!=j and pp[k][m]]
                e=F(0)
                for mask in range(1<<len(others)):
                    term=F(1)
                    for k,key in enumerate(others):
                        term*=pp[key][m] if mask&(1<<k) else (1-pp[key][m])
                    e+=term/F(1+mask.bit_count())
                w[i][j]+=pp[i][m]*pp[j][m]*e
            w[j][i]=w[i][j]
    return w


def coefficients(d,h):
    p=F(1,h+d); q=h*p
    A=F(2)*h/(d*(h+d))*(1-(1-p)**d)
    E=sum((F(comb(d-2,k))*p**k*(1-p)**(d-2-k)
            * ((1-q)/F(k+1)+q/F(k+2))) for k in range(d-1))
    B=p*p*E
    S=q*(1-p)**d + F(d*d)*p*p*(1-p)**(d-1)
    return A,B,S


def predicted(adj,h):
    n=len(adj);d=len(adj[0]); a,b,s=coefficients(d,h)
    out=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j: out[i][j]=s
            else: out[i][j]=(a if j in adj[i] else 0)+b*len(adj[i]&adj[j])
    return out


def main():
    count=0
    for name,adj in graphs():
        d=len(adj[0]);assert d>=2 and all(len(s)==d for s in adj)
        assert all(i not in adj[i] and all(i in adj[j] for j in adj[i]) for i in range(len(adj)))
        for h in [F(1,4),F(1),F(2),F(13,4)]:
            w=direct_weights(adj,h); predicted_w=predicted(adj,h)
            assert w == predicted_w, (name,h)
            assert all(sum(row)==1 for row in w), (name,h)
            assert all(w[i][j]==w[j][i] for i in range(len(adj)) for j in range(len(adj)))
            a,b,s=coefficients(d,h)
            assert s+d*a+d*(d-1)*b==1
            count+=len(adj)**2
    a,b,s=coefficients(3,F(2)); assert a==F(244,1875)
    assert b==F(109,3750)
    assert s==F(272,625)
    print('EXACT_REPLAY_OK matrix_entries=',count)
    print('triangular_prism_d3_h2: A=',a,'B=',b,'S=',s,'triangle_edge=',a+b,
          'other_edge=',a,'temperature=',1-s)

if __name__=='__main__':main()
