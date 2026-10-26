"""Exhaustive two-round first-order types in relational group language.
Standalone stdlib verifier for small abelian and Heisenberg groups.
The infinite classification is supplied by the proof, not this finite experiment.
"""
from itertools import product

def cyclic_power(p,d):
    elements=list(product(range(p),repeat=d)); identity=(0,)*d
    def mul(x,y):return tuple((a+b)%p for a,b in zip(x,y))
    return elements,identity,mul

def heisenberg(p):
    elements=list(product(range(p),repeat=3)); identity=(0,0,0)
    def mul(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p,(x[2]+y[2]+x[0]*y[1])%p)
    return elements,identity,mul

def atom(e,x,y,mul):
    a=(e,x,y)
    equal=tuple(a[i]==a[j] for i in range(3) for j in range(3))
    rel=tuple(mul(a[i],a[j])==a[k] for i in range(3) for j in range(3) for k in range(3))
    return equal+rel

def rank_two_type(group):
    elements,e,mul=group
    pointed=set()
    for x in elements:
        pointed.add(frozenset(atom(e,x,y,mul) for y in elements))
    return frozenset(pointed)

def simplified_signature(group):
    elements,e,mul=group
    pointed=set()
    for x in elements:
        px=mul(x,x)
        pointed.add(frozenset((x==e,y==e,x==y,px==e,mul(y,y)==e,px==y,mul(y,y)==x,mul(x,y)==e)
                              for y in elements))
    return frozenset(pointed)

def power(x,k,e,mul):
    r=e
    for _ in range(k): r=mul(r,x)
    return r

def main():
    groups={
        'C2':cyclic_power(2,1),'C2xC2':cyclic_power(2,2),
        'C3':cyclic_power(3,1),'C3xC3':cyclic_power(3,2),
        'C5':cyclic_power(5,1),'C5xC5':cyclic_power(5,2),
        'C7':cyclic_power(7,1),'C11':cyclic_power(11,1),
        'H3':heisenberg(3),'H5':heisenberg(5)
    }
    types={}
    for name,g in groups.items():
        a=rank_two_type(g); b=simplified_signature(g)
        assert len(a)==len(b)
        types[name]=a
        print('GROUP_OK',name,'size',len(g[0]),'pointed',len(a),'full_signature_types',sorted(map(len,a)))
    expected_classes=[{'C2'},{'C2xC2'},{'C3'},{'C3xC3','H3'},{'C5'},{'C5xC5','C7','C11','H5'}]
    for block in expected_classes:
        assert len({types[g] for g in block})==1,block
    for i,b1 in enumerate(expected_classes):
        for b2 in expected_classes[i+1:]:
            assert types[next(iter(b1))]!=types[next(iter(b2))],(b1,b2)
    print('SIX_CLASS_CALIBRATION_OK classes=6 all_pairs_distinct')
    for name,g in groups.items():
        p=2 if name.startswith('C2') else (3 if name.startswith(('C3','H3')) else (5 if name.startswith(('C5','H5')) else (7 if name=='C7' else 11)))
        elems,e,mul=g
        assert all((lambda x:(lambda y:mul(x,y)==e)(tuple((-a)%p for a in x)))(x) for x in elems) if name.startswith('C') else True
        assert all(mul(power(x,(p+1)//2,e,mul),power(x,(p+1)//2,e,mul)) == x for x in elems) if p%2 else True
    print('PRIME_EXPONENT_POWER_MAP_OK')
    print('VERIFY_OK')
if __name__=='__main__': main()
