"""Finite, standalone checks of the three-block BST path identity.

No external packages or source files are required.
"""
from itertools import permutations, product
from fractions import Fraction
from math import factorial


def tree_metrics(seq):
    seq=list(seq)
    if not seq:
        return -1, -1, -1
    keys=[seq[0]]
    left=[-1]
    right=[-1]
    maxdepth=0
    for value in seq[1:]:
        i=0
        dep=0
        while True:
            child=left if value<keys[i] else right
            if child[i]==-1:
                child[i]=len(keys)
                keys.append(value)
                left.append(-1)
                right.append(-1)
                maxdepth=max(maxdepth, dep+1)
                break
            i=child[i]
            dep+=1
    def extreme(arr):
        k=0
        dep=0
        while arr[k]!=-1:
            k=arr[k]
            dep+=1
        return dep
    return maxdepth, extreme(left), extreme(right)


def external_paths(rho):
    parents={rho[0]:None}
    for val in rho[1:]:
        current=rho[0]
        while True:
            bigger=val>current
            descendant=[j for j,p in parents.items() if p==current and (j>current)==bigger]
            if descendant:
                current=descendant[0]
            else:
                parents[val]=current
                break
    paths={}
    for val in rho:
        x=val
        path=[]
        while parents[x] is not None:
            path.append((parents[x],x))
            x=parents[x]
        paths[val]=list(reversed(path))
    return paths


def composite_height_formula(rho, locals_at_labels):
    paths=external_paths(rho)
    metrics={j:tree_metrics(locals_at_labels[j]) for j in rho}
    return max(metrics[j][0]+sum(1+metrics[u][1 if v<u else 2] for u,v in paths[j]) for j in rho)


def run():
    nchecks=0
    samples=0
    outer=list(permutations((1,2,3)))
    for n in range(1,5):
        locals=list(permutations(range(1,n+1)))
        for rho in outer:
            for ps in product(locals,repeat=3):
                locals_at_labels={rho[i]:ps[i] for i in range(3)}
                full=[(rho[i]-1)*n+x for i in range(3) for x in ps[i]]
                observed=tree_metrics(full)[0]
                formula=composite_height_formula(rho,locals_at_labels)
                assert observed==formula,(n,rho,ps,observed,formula)
                nchecks+=1
                samples+=1
        print('n',n,'all six outer shapes passed')

    # Exhaustive unequal-block tests (including a four-block outer structure).
    uneven_tests=0
    for sizes in ((1,2,3),(2,1,3),(1,2,2,3)):
        k=len(sizes)
        for rho in permutations(range(1,k+1)):
            ranges=[list(permutations(range(1,sizes[i]+1))) for i in range(k)]
            for ps in product(*ranges):
                blocks={rho[i]:ps[i] for i in range(k)}
                value_order=sorted(range(k),key=lambda j:rho[j])
                starts={}
                acc=0
                for i in value_order:
                    starts[rho[i]]=acc
                    acc+=sizes[i]
                full=[starts[rho[i]]+x for i in range(k) for x in ps[i]]
                assert tree_metrics(full)[0]==composite_height_formula(rho,blocks)
                uneven_tests+=1
                nchecks+=1
    # Direct first and second moments of both record extremes for small n,
    # compared with the sums derived from the independent relative-rank encoding.
    for n in range(2,9):
        R=[]; L=[]
        for p in permutations(range(1,n+1)):
            maxv=0; minv=n+1; r=l=0
            for x in p:
                if x>maxv:
                    maxv=x; r+=1
                if x<minv:
                    minv=x; l+=1
            R.append(r); L.append(l)
        f=factorial(n)
        mean=Fraction(sum(R),f)
        cov=Fraction(sum(a*b for a,b in zip(R,L)),f)-mean**2
        theo_mean=sum((Fraction(1,j) for j in range(1,n+1)),Fraction(0))
        theo_cov=-sum((Fraction(1,j*j) for j in range(2,n+1)),Fraction(0))
        assert mean==theo_mean,(n,mean,theo_mean)
        assert cov==theo_cov,(n,cov,theo_cov)
        nchecks+=2
    print('EXACT_CHECKS',nchecks,'BLOCK_CASES',samples,'RECORD_COV_CHECKS',14,'UNEQUAL_BLOCK_CASES',uneven_tests)

if __name__=='__main__':
    run()
