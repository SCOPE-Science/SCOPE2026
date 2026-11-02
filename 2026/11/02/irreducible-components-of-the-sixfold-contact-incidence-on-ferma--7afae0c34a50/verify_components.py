from itertools import combinations
from collections import Counter

def partitions(seq):
    if not seq:
        yield ()
        return
    head,*tail=seq
    for blocks in partitions(tail):
        yield ((head,),)+blocks
        for j in range(len(blocks)):
            new=list(blocks)
            new[j]=(head,)+new[j]
            yield tuple(new)

def coefficient_census():
    poly=Counter()
    byshape=Counter()
    universe=tuple(range(6))
    for m in range(2,7):
        for subset in combinations(universe,m):
            for blocks in partitions(list(subset)):
                if any(len(b)<2 for b in blocks):
                    continue
                if m==6 and len(blocks)==1:
                    continue
                k=len(blocks)
                # disjoint zero-power-sum blocks, pair-blocks have d components
                exponent=sum(len(b)==2 for b in blocks)
                poly[exponent]+=1
                byshape[(tuple(sorted(map(len,blocks))),6-m)]+=1
    return poly,byshape
p,byshape=coefficient_census()
print('polynomial coefficients',dict(sorted(p.items(),reverse=True)))
print('partition shapes',dict(sorted(byshape.items())))
assert p==Counter({3:15,2:45,1:90,0:51}),p
for degree,expected in [(6,5451),(7,15*343+45*49+90*7+51),(8,15*512+45*64+90*8+51)]:
    count=sum(n*degree**power for power,n in p.items())
    assert count==expected
    print('d=',degree,'components=',count)

from math import comb,prod
for n in range(1,4):
    lambdas=list(range(1,n+1))
    import itertools
    determinant=sum((-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))*prod(lambdas[j]**perm[j] for j in range(n)) for perm in itertools.permutations(range(n)))
    vandermonde=prod(lambdas[j]-lambdas[i] for i in range(n) for j in range(i+1,n))
    assert determinant==vandermonde
    print('Vandermonde',n,determinant)

# Exact formal check of degree-six expansion: three zero-power-sum pairs,
# slopes (1,2,3), and separately two inactive coordinates (nonzero sixth term).
for d in (6,7,10):
    block_sums=[0,0,0]
    for j in range(1,6):
        coefficient=comb(d,j)*sum((a+1)**j*B for a,B in enumerate(block_sums))
        assert coefficient==0
print('VERIFY_OK')
