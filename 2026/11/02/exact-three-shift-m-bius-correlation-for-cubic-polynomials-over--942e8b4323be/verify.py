#!/usr/bin/env python3
"""Independent finite tests for the three-shift cubic polynomial Mobius identity."""
from itertools import combinations


def mobius_monic_cubic(a, b, c, p):
    """Factor-pattern test using roots and derivative, not discriminants."""
    roots = [t for t in range(p) if (t**3 + a*t*t + b*t + c) % p == 0]
    if len(roots) == 0:
        return -1
    if len(roots) == 2:
        return 0
    if len(roots) == 3:
        return -1
    t = roots[0]
    return 0 if (3*t*t + 2*a*t + b) % p == 0 else 1


def direct_mobius(p, triples):
    table = [[[mobius_monic_cubic(a, b, c, p) for c in range(p)]
              for b in range(p)] for a in range(p)]
    cases = 0
    for shifts in triples:
        total = sum(table[a][b][(c+shifts[0])%p]
                    * table[a][b][(c+shifts[1])%p]
                    * table[a][b][(c+shifts[2])%p]
                    for a in range(p) for b in range(p) for c in range(p))
        assert total == p*p, (p, shifts, total)
        cases += 1
    return cases


def small_character_identity(p):
    ch = [0] * p
    for x in range(1,p):
        ch[x] = 1 if pow(x,(p-1)//2,p) == 1 else -1
    cases = 0
    for shifts in combinations(range(p),3):
        total=0
        for v in range(p):
            for u in range(p):
                prod=1
                for c in shifts:
                    prod=prod*(u-(v+c)**2)%p
                total+=ch[prod]
        assert total == p*ch[p-1],(p,shifts,total)
        cases+=1
    return cases


class F125:
    """F_5[z]/(z^3+z+1), with base-5 coordinate encoding."""
    def __init__(self):
        self.terms=[(n%5,(n//5)%5,n//25) for n in range(125)]
        self.add=[[sum(((a[i]+b[i])%5)*5**i for i in range(3)) for b in self.terms]
                  for a in self.terms]
        self.neg=[sum(((-a[i])%5)*5**i for i in range(3)) for a in self.terms]
        self.mul=[]
        for a in self.terms:
            row=[]
            for b in self.terms:
                p=[0]*5
                for i in range(3):
                    for j in range(3):
                        p[i+j]+=a[i]*b[j]
                for i in (4,3):
                    p[i-2]-=p[i]
                    p[i-3]-=p[i]
                row.append(sum((p[i]%5)*5**i for i in range(3)))
            self.mul.append(row)
        squares={self.mul[i][i] for i in range(1,125)}
        self.ch=[0]+[1 if j in squares else -1 for j in range(1,125)]
        assert len(squares)==62
        assert self.mul[5][5] != 0
        self.one=1

    def sub(self,x,y):
        return self.add[x][self.neg[y]]

    def square(self,x):
        return self.mul[x][x]


def extension_character_identity():
    F=F125()
    # The cubic modulus is irreducible because z^3+z+1 has no F_5 root.
    assert all((i**3+i+1)%5 for i in range(5))
    triples=[(0,1,5),(0,1,25),(0,5,25),(0,1,31),
             (1,5,25),(2,7,61),(5,17,83),(4,57,124),
             (0,11,101),(32,47,105),(3,50,62),(14,77,89)]
    for shifts in triples:
        assert len(set(shifts))==3
        total=0
        for v in range(125):
            roots=[F.square(F.add[v][c]) for c in shifts]
            for u in range(125):
                p=F.one
                for r in roots:
                    p=F.mul[p][F.sub(u,r)]
                total+=F.ch[p]
        assert total==125*F.ch[F.neg[1]],(shifts,total)
    return len(triples)


def main():
    small=sum(small_character_identity(p) for p in (5,7,11,13))
    direct=0
    for p in (5,11):
        direct+=direct_mobius(p,list(combinations(range(p),3)))
    for p in (17,23):
        ts=list(combinations(range(p),3))
        selections=ts[::max(1,len(ts)//20)][:21]
        direct+=direct_mobius(p,selections)
    ext=extension_character_identity()
    print(f'VERIFY_OK direct_mobius_triples={direct} prime_character_triples={small} extension_triples={ext} field_order=125')

if __name__=='__main__':
    main()
