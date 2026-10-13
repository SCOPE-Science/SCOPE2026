"""Independent finite-field count of labeled perfect, idempotent-free
commutative binary algebras. Python 3 stdlib only; finite checks do not
replace the proof for arbitrary odd prime powers.
"""
from itertools import product
from math import comb


def prove_small_prime(p):
    pts=[(1,t) for t in range(p)]+[(0,1)]
    triples=set()
    for r,s in pts:
        for scale in range(1,p):
            triples.add(tuple((scale*comb(3,j)*pow(r,3-j,p)*pow(s,j,p))%p for j in range(4)))
    data={'irreducible_cubic':0, 'linear_times_irreducible_quadratic':0, 'triple_root':0}
    perfect=0
    for a,b,c,d,e,f in product(range(p),repeat=6):
        images=((a,b),(c,d),(e,f))
        if not any((x[0]*y[1]-x[1]*y[0])%p for i,x in enumerate(images) for y in images[i+1:]):
            continue
        perfect+=1
        no_idem=True
        for x,y in pts:
            sx=(a*x*x+2*c*x*y+e*y*y)%p
            sy=(b*x*x+2*d*x*y+f*y*y)%p
            if (x*sy-y*sx)%p==0 and (sx or sy):
                no_idem=False
                break
        if not no_idem:continue
        cubic=(b%p,(2*d-a)%p,(f-2*c)%p,(-e)%p)
        roots=sum(1 for x,y in pts if sum(cubic[j]*pow(x,3-j,p)*pow(y,j,p) for j in range(4))%p==0)
        if roots==0: data['irreducible_cubic']+=1
        elif roots==1 and cubic in triples: data['triple_root']+=1
        elif roots==1: data['linear_times_irreducible_quadratic']+=1
        else:raise AssertionError(('unpredicted',p,(a,b,c,d,e,f),roots))
    expected={
        'irreducible_cubic':p*p*(p-1)*(p**3-p)//3,
        'linear_times_irreducible_quadratic':p*(p*p-1)*(p*p-p)//2,
        'triple_root':(p-1)*(p*p-1),
    }
    assert data==expected,(p,data,expected)
    assert perfect==(p**3-1)*(p**3-p)
    print('F_%d perfect=%d, idempotent-free strata=%s; formula=%d'%(
        p,perfect,data,sum(expected.values())))

if __name__=='__main__':
    for p in (3,5):prove_small_prime(p)
    print('VERIFY_OK')
