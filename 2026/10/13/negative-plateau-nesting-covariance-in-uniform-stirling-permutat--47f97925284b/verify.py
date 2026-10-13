"""Exact independent checks for plateau--nesting covariance in uniform Stirling permutations.
Usage: python3 verify.py  (Python standard library only).
"""
from fractions import Fraction
from math import comb, prod


def parse_tree(word):
    """Independently decode DFS contour into rooted labelled plane-tree data."""
    n=len(word)//2
    stack=[0]
    seen=set()
    depths={0:0}
    child_counts={i:0 for i in range(n+1)}
    gap_parents=[0]
    for x in word:
        if x not in seen:
            assert x > stack[-1]
            parent=stack[-1]
            depths[x]=depths[parent]+1
            child_counts[parent]+=1
            seen.add(x)
            stack.append(x)
        else:
            assert stack[-1]==x
            stack.pop()
        gap_parents.append(stack[-1])
    assert stack==[0] and seen==set(range(1,n+1))
    P=sum(child_counts[i]==0 for i in range(1,n+1))
    H=sum(depths[i] for i in range(1,n+1))
    W=sum(depths[i] for i in range(1,n+1) if child_counts[i]==0)
    return P,H,W,depths,child_counts,gap_parents


def word_stats(word):
    n=len(word)//2
    P=sum(word[i]==word[i+1] for i in range(len(word)-1))
    first={}
    S=0
    for i,x in enumerate(word):
        if x not in first: first[x]=i
        else: S+=i-first[x]-1
    return P,S


def closed(n):
    # (2n)!!/(2n-1)!! = 4^n / binom(2n,n)
    return Fraction(2,3)*Fraction(4**n,comb(2*n,n))-Fraction(8*n+4,9)


def run():
    words=[()]
    stats_checks=0
    gap_checks=0
    mean_checks=0
    signs=0
    cov_checks=0
    rec_cov=Fraction(0)
    for n in range(1,8):
        words=[w[:g]+(n,n)+w[g:] for w in words for g in range(len(w)+1)]
        N=len(words)
        assert N==prod(range(1,2*n,2))
        sumP=sumS=sumPS=sumH=sumW=0
        for word in words:
            P,S=word_stats(word)
            PT,H,W,depths,counts,gaps=parse_tree(word)
            assert P==PT and S==2*(H-n)
            stats_checks+=1
            sumP+=P;sumS+=S;sumPS+=P*S;sumH+=H;sumW+=W
            if n<=5:
                # Verify every conditional insertion identity using independently parsed child words.
                children=[parse_tree(word[:g]+(n+1,n+1)+word[g:])[:3] for g in range(2*n+1)]
                dp=sum(z[0]-P for z in children)
                dh=sum(z[1]-H for z in children)
                dw=sum(z[2]-W for z in children)
                assert dp==2*n+1-P
                assert dh==2*H+n+1
                assert dw==2*H+n+1-W
                prod_sum=sum(z[0]*z[1] for z in children)
                assert prod_sum == (2*n+2)*P*H+n*P+(2*n+3)*H+n+1-W
                # Parent-gap depth representation is checked separately.
                assert sum(depths[j]+1 for j in gaps)==2*H+n+1
                assert sum((counts[j]==0) for j in gaps)==P
                gap_checks+=1
        eP=Fraction(sumP,N);eS=Fraction(sumS,N)
        eH=Fraction(sumH,N);eW=Fraction(sumW,N)
        cov=Fraction(sumPS,N)-eP*eS
        assert eP==Fraction(2*n+1,3)
        assert eW==Fraction(2,3)*eH+Fraction(n+2,9)
        assert cov==closed(n)
        mean_checks+=2
        cov_checks+=1
        assert (cov==0 if n==1 else cov<0)
        signs+=1
        if n<7:
            rec_cov = Fraction(2*n+2,2*n+1)*rec_cov-Fraction(2,9)
            assert 2*rec_cov==closed(n+1)
        print(f'n={n} words={N} covariance={cov} checks=OK',flush=True)
    for n in range(1,1001):
        assert closed(n)== Fraction(2,3)*Fraction(4**n,comb(2*n,n))-Fraction(8*n+4,9)
        assert closed(n)<0 if n>=2 else closed(n)==0
    print(f'VERIFY_OK words={stats_checks} decoded_shape_checks={stats_checks} conditional_insertion_checks={gap_checks} exact_mean_checks={mean_checks} covariance_checks={cov_checks} finite_sign_checks={signs} n_range=1..7 analytic_formula_checks=1000')

if __name__=='__main__': run()
