#!/usr/bin/env python3
"""Direct geometric radical-point check of the smooth-base criterion.
For a quadratic pencil over Fq (q even) with irreducible polar Pfaffian,
the two conjugate singular polar members lie over K=F_(q^2). If the square radical restriction is nonzero, any singular base point on
that radical line is K-rational. If it vanishes identically, a root of the
other binary quadratic exists over the algebraic closure (special case).
"""
from itertools import product


def field(q):
    Q=q*q
    m=Q.bit_length()-1
    poly={4:7,16:19}[Q]
    def mul(a,b):
        z=0
        while b:
            if b&1:z^=a
            b>>=1;a<<=1
            if a&Q:a^=poly
        return z
    M=[[mul(a,b) for b in range(Q)]for a in range(Q)]
    return Q,M


def main():
    for q in (2,4):
        Q,M=field(q)
        sq=[M[x][x] for x in range(Q)]
        conj=[pow_field(x,q,M) for x in range(Q)]
        pts=[(1,t) for t in range(Q)]+[(0,1)]
        invalid=0
        for a,b,c,d in product(range(Q),repeat=4):
            # A singular base point is exactly a common zero on a
            # radical line of the two conjugate singular members.
            singular=(b==0 and d==0)
            for x,y in ([] if singular else pts):
                xx,yy=sq[x],sq[y]
                if (M[b][xx]^M[d][yy])==0 and (M[x][y]^M[a][xx]^M[c][yy])==0:
                    singular=True;break
            if not singular:
                A,B,C,D=conj[a],conj[b],conj[c],conj[d]
                for x,y in pts:
                    xx,yy=sq[x],sq[y]
                    if (M[B][xx]^M[D][yy])==0 and (M[x][y]^M[A][xx]^M[C][yy])==0:
                        singular=True;break
            if singular:invalid+=1
            disc=M[b][d]^sq[M[a][d]]^sq[M[c][b]]
            assert singular==(disc==0),(q,a,b,c,d,singular,disc)
        expected=Q**4-Q*(Q-1)**2*(Q+1)
        assert invalid==expected,(q,invalid,expected)
        print('q=%d direct_geometric_singular_lifts=%d direct_geometric_smooth_lifts=%d' % (q,invalid,Q**4-invalid))
    print('GEOMETRIC_BASE_CRITERION_OK')

def pow_field(a,n,M):
    z=1
    while n:
        if n&1:z=M[z][a]
        a=M[a][a];n>>=1
    return z

if __name__=='__main__':main()
