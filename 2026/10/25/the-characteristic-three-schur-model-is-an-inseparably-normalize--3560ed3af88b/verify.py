#!/usr/bin/env python3
"""Exact finite-field checks for the characteristic-three Schur model.

Projective coordinates are (a,b,x,w), with equation x*a^3-w*b^3=0.
The code tests genuine line containment by the polynomial restriction,
not merely vanishing at all rational points of a line.
"""
from itertools import combinations, product


class F3ext:
    # Basis 1,z,...; reductions z^2=2 (degree 2), z^3=z+1 (degree 3).
    def __init__(self, degree):
        assert degree in (1, 2, 3)
        self.degree = degree
        self.q = 3 ** degree
        self.coeffs = {1: [0], 2: [1, 0], 3: [2, 2, 0]}[degree]
        self.mul_table = [[self._mul_slow(a,b) for b in range(self.q)] for a in range(self.q)]
        self.inv_table = [None] * self.q
        for a in range(1, self.q):
            self.inv_table[a] = next(b for b in range(1,self.q) if self.mul_table[a][b] == 1)
        self.add_table = [[self._from_vec([(u+v)%3 for u,v in zip(self._vec(a),self._vec(b))]) for b in range(self.q)] for a in range(self.q)]
        self.neg_table = [self._from_vec([(-v)%3 for v in self._vec(a)]) for a in range(self.q)]
        self.cube = [self.mul_table[self.mul_table[a][a]][a] for a in range(self.q)]

    def _vec(self, a):
        out=[]
        for _ in range(self.degree):
            out.append(a%3)
            a//=3
        return out
    def _from_vec(self, v):
        return sum(c*3**i for i,c in enumerate(v))
    def _mul_slow(self,a,b):
        m=self.degree
        av,bv=self._vec(a),self._vec(b)
        v=[0]*(2*m-1)
        for i in range(m):
            for j in range(m):
                v[i+j]=(v[i+j]+av[i]*bv[j])%3
        for i in range(2*m-2,m-1,-1):
            c=v[i]
            # monic polynomial z^m+sum(coeffs[j]*z^j)
            for j in range(m):
                v[i-m+j]=(v[i-m+j]-c*self.coeffs[j])%3
        return self._from_vec(v[:m])
    def add(self,a,b):return self.add_table[a][b]
    def sub(self,a,b):return self.add_table[a][self.neg_table[b]]
    def mul(self,a,b):return self.mul_table[a][b]
    def inv(self,a):return self.inv_table[a]
    def normalize(self, vec):
        p=next(x for x in vec if x)
        return tuple(self.mul(x,self.inv(p)) for x in vec)


def projective_points(field):
    # RREF rank-one, avoid q^4 exhaustive tuples for degree-three case.
    q=field.q
    for pivot in range(4):
        for tail in product(range(q),repeat=3-pivot):
            yield (0,)*pivot+(1,)+tuple(tail)


def on_surface(v,F):
    a,b,x,w=v
    return F.mul(x,F.cube[a])==F.mul(w,F.cube[b])


def true_line(v0,v1,F):
    a0,b0,x0,w0=v0
    a1,b1,x1,w1=v1
    m=F.mul; sub=F.sub; cube=F.cube
    return all(c == 0 for c in (
        sub(m(x0,cube[a0]),m(w0,cube[b0])),
        sub(m(x1,cube[a0]),m(w1,cube[b0])),
        sub(m(x0,cube[a1]),m(w0,cube[b1])),
        sub(m(x1,cube[a1]),m(w1,cube[b1])),
    ))


def rref_lines(F):
    q=F.q
    for i,j in combinations(range(4),2):
        free0=[k for k in range(i+1,4) if k!=j]
        free1=list(range(j+1,4))
        for vals in product(range(q),repeat=len(free0)+len(free1)):
            row0=[0]*4; row1=[0]*4
            row0[i]=row1[j]=1
            for k,v in zip(free0,vals):row0[k]=v
            for k,v in zip(free1,vals[len(free0):]):row1[k]=v
            yield tuple(row0),tuple(row1)


def main():
    for m in (1,2,3):
        F=F3ext(m);q=F.q
        pts=sum(on_surface(v,F) for v in projective_points(F))
        singular=sum(on_surface(v,F) and v[0]==v[1]==0 for v in projective_points(F))
        assert pts==(q+1)**2,(q,pts)
        assert singular==q+1,(q,singular)
        print('points',q,pts,'singular-line-points',singular)
        if m<3:
            line_rows=list(rref_lines(F))
            actual=sum(true_line(u,v,F) for u,v in line_rows)
            expected_total=(q*q+1)*(q*q+q+1)
            assert len(line_rows)==expected_total,(q,len(line_rows),expected_total)
            assert actual==q+3,(q,actual)
            print('lines',q,actual,'rref-subspaces-examined',len(line_rows))
    # Over F3 the rational point test is NOT an adequate line certificate.
    F=F3ext(1)
    all_rows=list(rref_lines(F))
    false_positives=0
    for u,v in all_rows:
        rational_points = [F.normalize(tuple(F.add(F.mul(s,a),F.mul(t,b)) for a,b in zip(u,v)))
                           for s,t in product(range(3),repeat=2) if s or t]
        if all(on_surface(pt,F) for pt in rational_points) and not true_line(u,v,F):
            false_positives+=1
    assert false_positives==2,false_positives
    print('F3-pointwise-false-line-positives',false_positives)
    print('VERIFY_OK')


if __name__=='__main__':main()
