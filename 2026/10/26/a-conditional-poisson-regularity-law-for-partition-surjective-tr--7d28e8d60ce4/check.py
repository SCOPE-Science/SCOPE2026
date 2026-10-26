"""Finite witness enumeration and independent regularity checks for block-surjective transformations."""
from itertools import product
from collections import Counter
from math import factorial, exp, comb
from fractions import Fraction


def blocks_of_sizes(sizes):
    blocks=[]
    offset=0
    for a in sizes:
        blocks.append(tuple(range(offset,offset+a)))
        offset += a
    return blocks


def all_surjective_options(blocks,i):
    src=blocks[i]
    options=[]
    for j,dest in enumerate(blocks):
        if len(dest)>len(src):
            continue
        for images in product(dest,repeat=len(src)):
            if set(images)==set(dest):
                options.append((j,images))
    return options


def all_maps(sizes):
    blocks=blocks_of_sizes(sizes)
    opts=[all_surjective_options(blocks,i) for i in range(len(blocks))]
    for choice in product(*opts):
        f=[None]*sum(sizes)
        for src,(_,images) in zip(blocks,choice):
            for x,y in zip(src,images):f[x]=y
        yield tuple(f),tuple(j for j,_ in choice)


def criterion(sizes,targets):
    return all(any(t==j and sizes[i]==sizes[j] for i,t in enumerate(targets)) for j in set(targets))


def compose(f,g):
    return tuple(g[f[x]] for x in range(len(f)))


def onto_count(a,b):
    return sum((-1)**(b-j)*comb(b,j)*j**a for j in range(b+1))


def exact_predict(sizes):
    b=max(sizes)
    m=sum(1 for a in sizes if a==b)
    assert all(a<b for a in sizes[:-m])
    base=sizes[:-m]
    w=[onto_count(b,a) for a in base]
    d=factorial(b)
    C=sum(w)
    pred=0
    lower_count=0
    for f0,targ in all_maps(base):
        lower_count+=1
        witnessed={j for i,j in enumerate(targ) if base[i]==base[j]}
        if not set(targ).issubset(witnessed):continue
        pred+=(m*d+sum(w[j] for j in witnessed))**m
    denom=lower_count*(m*d+C)**m
    assert 0<=pred<=denom
    return pred,denom,lower_count,C,d


def check_case(sizes,brute=False):
    dct=Counter()
    maps=[]
    for f,targ in all_maps(sizes):
        dct['all']+=1
        if criterion(sizes,targ): dct['regular']+=1
        maps.append((f,targ))
    num,denom,lower_count,C,d=exact_predict(sizes)
    assert (dct['regular'],dct['all'])==(num,denom),(sizes,dct,num,denom)
    if brute:
        gs=[f for f,_ in maps]
        for f,targ in maps:
            actual=any(compose(compose(f,g),f)==f for g in gs)
            assert actual==criterion(sizes,targ),(sizes,f,targ)
    print('size_profile',sizes,'maps',dct['all'],'regular',dct['regular'],'exact_regular_fraction',str(Fraction(num,denom)),'C',C,'d',d,'brute',brute)
    return dct['all']


def test_poisson_bound(base,b,max_M=9):
    assert all(a<b for a in base)
    w=[onto_count(b,a) for a in base];C=sum(w);d=factorial(b)
    f0_maps=list(all_maps(base))
    limit=0.
    for f,t in f0_maps:
        witnessed={j for i,j in enumerate(t) if base[i]==base[j]}
        if set(t).issubset(witnessed):
            missing=C-sum(w[j] for j in witnessed)
            limit+=exp(-missing/d)
    limit/=len(f0_maps)
    for M in range(1,max_M+1):
        numer,denom,_,c,dd=exact_predict(base+[b]*M)
        finite=numer/denom
        assert abs(finite-limit)<=min(1,2*C*C/(M*d*d))+1e-12,(base,b,M,finite,limit)
    print('poisson_limit',base,b,'limit',repr(limit),'checked_M',max_M,'tv_rate_bound_verified')


def check_joint_law(sizes):
    """Direct map enumeration versus the full multivariate rare-target multinomial law."""
    b=max(sizes)
    M=sum(a==b for a in sizes)
    base=sizes[:-M]
    lower_count=sum(1 for _ in all_maps(base))
    w=[onto_count(b,a) for a in base]
    d=factorial(b)
    observed=Counter()
    for f,targs in all_maps(sizes):
        hits=tuple(targs[len(base):].count(i) for i in range(len(base)))
        observed[hits]+=1
    for hits,observed_count in observed.items():
        s=sum(hits)
        ways=factorial(M)
        for k in hits:ways//=factorial(k)
        ways//=factorial(M-s)
        predict=lower_count*ways*(M*d)**(M-s)
        for k,weight in zip(hits,w):predict*=weight**k
        assert observed_count==predict,(sizes,hits,observed_count,predict)
    assert len(observed)==comb(M+len(base),len(base))
    print('multinomial_joint_law',sizes,'outcomes',len(observed),'checked')

if __name__=='__main__':
    n=0
    for sizes,brute in [
        ([1,1,2],True),([1,1,2,2],True),([1,1,2,2,2],False),
        ([1,2,3],True),([1,2,3,3],False),([1,1,2,3],True),
        ([1,1,2,3,3],False),([2,2,3,3],False),([1,1,3,3],False)]:
        n+=check_case(sizes,brute)
    check_joint_law([1,1,2,3,3])
    check_joint_law([2,2,3,3])
    test_poisson_bound([1,1,2],3,12)
    test_poisson_bound([2,2],3,12)
    test_poisson_bound([1,1],2,12)
    print('ALL_PARTITION_SURJECTION_POISSON_CHECKS_PASSED enumerated_maps='+str(n))
