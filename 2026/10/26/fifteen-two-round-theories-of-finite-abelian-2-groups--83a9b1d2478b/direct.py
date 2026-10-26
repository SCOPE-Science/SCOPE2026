"""Independent exhaustive rank-two model signatures in the entire ternary language.
Run: python3 direct.py
No use of the reduced atomic mask or its algebraic formulas.
"""
from itertools import product
REPS=[(),(2,),(2,2),(4,),(2,4),(4,4),(2,4,4),
      (8,),(2,8),(4,8),(8,8),(16,),(2,16),(4,16),(8,16)]

def full_type(mod):
    Z=(0,)*len(mod)
    es=list(product(*(range(m) for m in mod)))
    def add(a,b):return tuple((aa+bb)%m for aa,bb,m in zip(a,b,mod))
    res=set()
    for x in es:
        s=set()
        for y in es:
            p=(Z,x,y)
            eq=tuple(int(p[i]==p[j]) for i in range(3) for j in range(i,3))
            rel=tuple(int(add(p[i],p[j])==p[k]) for i in range(3) for j in range(3) for k in range(3))
            s.add(eq+rel)
        res.add(frozenset(s))
    return frozenset(res)

def run():
    profiles={p:full_type(p) for p in REPS}
    assert len(set(profiles.values()))==15
    assert full_type((32,))==profiles[(16,)]
    assert full_type((2,2,2,4))==profiles[(2,4)]
    print('FULL_ATOMIC_LANGUAGE_OK representatives=15 all_distinct')
    print('NONISOMORPHIC_EQUALITIES_OK C16=C32 and C2xC4=C2xC2xC2xC4')
    print('DIRECT_VERIFY_OK')
if __name__=='__main__':run()
