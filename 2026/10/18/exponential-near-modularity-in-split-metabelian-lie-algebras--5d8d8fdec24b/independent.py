"""Independent explicit invariant-subspace pair-sum verification for three spectral blocks."""
from itertools import product
from verify import all_spaces,rref,ga,H,exact_counts

def direct(blocks,q):
    loc=[list(all_spaces(a,q)) for a in blocks]
    idx=list(product(*loc))
    n=sum(blocks)
    p11=p01=n1=0
    for X in idx:
        x=sum(map(len,X));n1+=q**(n-x)
        zs=[list(all_spaces(a-len(s),q)) for a,s in zip(blocks,X)]
        p01+=q**(n-x)*sum(H(x,sum(map(len,Z)),q) for Z in product(*zs))
    for X in idx:
        for Y in idx:
            ints=[len(A)+len(B)-len(rref(A+B,q)) for A,B in zip(X,Y)]
            quot=[a-len(rref(A+B,q)) for a,A,B in zip(blocks,X,Y)]
            p11+=q**(n-sum(ints))*(1+sum(q**m-1 for m in quot))
    got=exact_counts(blocks,q)
    assert (n1,p01,p11)==got[1:]
    print('INDEPENDENT_SPECTRAL_SUBSPACES_OK',blocks,q,'invariant_subspaces',len(idx),'p11',p11)

if __name__=='__main__':
    direct((2,2,2),3)
    direct((2,2),2)
