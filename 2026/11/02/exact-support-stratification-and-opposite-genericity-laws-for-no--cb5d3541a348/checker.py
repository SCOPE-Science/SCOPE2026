"""Independent finite-instance checker for supported-predicate census."""
from itertools import product, permutations
from math import comb


def bell(n):
    vals=[1]
    for m in range(n): vals.append(sum(comb(m,j)*vals[j] for j in range(m+1)))
    return vals[n]


def nr(k,r):
    return sum(comb(r,j)*bell(j)*k**(r-j) for j in range(r+1))


def eq_partition_codes(n):
    def gen(prefix,upper):
        if len(prefix)==n:
            yield tuple(prefix)
        else:
            for i in range(upper+2):
                yield from gen(prefix+[i],max(upper,i))
    yield from gen([0],0)


def preserves_partition(part, p):
    n=len(part)
    return all((part[i]==part[j])==(part[p[i]]==part[p[j]]) for i in range(n) for j in range(i))


def transposition(n,i,j):
    p=list(range(n));p[i],p[j]=p[j],p[i];return p


def full_support_eq(k):
    n=k+3
    all_parts=0; full=0; hist=[0]*(k+1)
    fresh_swaps=[transposition(n,k,j) for j in range(k+1,n)]
    anchor_swaps=[transposition(n,a,k) for a in range(k)]
    for p in eq_partition_codes(n):
        if any(not preserves_partition(p,t) for t in fresh_swaps):continue
        all_parts+=1
        d=sum(preserves_partition(p,t) for t in anchor_swaps)
        hist[d]+=1
        if d==0:full+=1
    return all_parts,full,hist


def orbit_labels(k,r):
    n=k+r+2
    coords=list(product(range(n), repeat=r))
    labels={}
    for x in coords:
        which={}
        pat=[];next_label=0
        for a in x:
            if a<k:pat.append(('a',a))
            else:
                if a not in which:which[a]=next_label;next_label+=1
                pat.append(('f',which[a]))
        labels[tuple(pat)]=None
    return len(labels)


def full_support_binary(k):
    # For every S-orbit on A^2, choose a bit. Each a outside least support
    # imposes equality between bits of cells exchanged by (a, fresh).
    n=k+3
    def signature(a,b):
        def classify(z):return ('a',z) if z<k else ('f',None)
        if a>=k and b>=k:return ('fresh_equal',) if a==b else ('fresh_distinct',)
        return classify(a),classify(b)
    sigs=sorted({signature(a,b) for a in range(n) for b in range(n)},key=repr)
    index={t:i for i,t in enumerate(sigs)}
    edges=[]
    for a in range(k):
        swap=transposition(n,a,k)
        equalities=set()
        for x,y in product(range(n), repeat=2):
            aa=index[signature(x,y)];bb=index[signature(swap[x],swap[y])]
            if aa!=bb:equalities.add(tuple(sorted((aa,bb))))
        edges.append(equalities)
    total=1<<len(sigs)
    exact=0
    for bits in range(total):
        if all(any(bool((bits>>u)&1)!=bool((bits>>v)&1) for (u,v) in edge) for edge in edges):exact+=1
    return total,exact


def main():
    for k in range(6):
        total,full,hist=full_support_eq(k)
        no_singletons=sum((-1)**j*comb(k,j)*bell(k-j) for j in range(k+1))
        expected=(bell(k+1)+bell(k), bell(k)+no_singletons)
        pred_hist=[comb(k,d)*(bell(k-d)+sum((-1)**j*comb(k-d,j)*bell(k-d-j) for j in range(k-d+1))) for d in range(k+1)]
        assert hist==pred_hist,(k,hist,pred_hist)
        assert (total,full)==expected,(k,(total,full),expected)
        print('EQ',k,total,full,hist)
    for k in range(4):
        for r in range(1,4):
            assert orbit_labels(k,r)==nr(k,r),(k,r,orbit_labels(k,r),nr(k,r))
        predicted=sum((-1)**(k-j)*comb(k,j)*2**nr(j,2) for j in range(k+1))
        actual=full_support_binary(k)
        assert actual==(2**nr(k,2),predicted),(k,actual,predicted)
        print('BIN',k,*actual)
    print('ALL_CHECKS_OK')

if __name__=='__main__':main()
