"""Exact finite-size checks for leaf-count / search-path covariance in uniform random BSTs."""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial


def pair_from_permutation(order):
    # Insert keys into a binary search tree; child pointers are 0-based indices.
    nodes=[]
    for key in order:
        if not nodes:
            nodes.append([key, -1, -1, 0])
            continue
        p=0
        while True:
            branch=1 if key<nodes[p][0] else 2
            c=nodes[p][branch]
            if c<0:
                nodes[p][branch]=len(nodes)
                nodes.append([key,-1,-1,nodes[p][3]+1])
                break
            p=c
    leaves=sum(left<0 and right<0 for _,left,right,depth in nodes)
    path=sum(depth for _,left,right,depth in nodes)
    return leaves,path


def moment_recurrence(N=100):
    leaf=[Q(0)]*(N+1)
    path=[Q(0)]*(N+1)
    mixed=[Q(0)]*(N+1)
    leaf[1]=Q(1)
    for n in range(2,N+1):
        a=b=c=Q(0)
        for k in range(n):
            l=n-1-k
            a+=leaf[k]+leaf[l]
            b+=path[k]+path[l]+(n-1)
            c+=(mixed[k]+mixed[l]+leaf[k]*path[l]+leaf[l]*path[k]
                +(n-1)*(leaf[k]+leaf[l]))
        leaf[n]=a/n
        path[n]=b/n
        mixed[n]=c/n
        cov=mixed[n]-leaf[n]*path[n]
        target= -Q((n+3)*(n-2),9*n)
        assert cov==target,('recursive',n,cov,target)
        assert leaf[n]==Q(n+1,3), ('leaf_mean',n,leaf[n])
    return leaf,path,mixed


def exhaustive(N=8):
    leaf,path,mixed=moment_recurrence(N)
    count=0
    for n in range(1,N+1):
        sl=sp=slp=0
        for order in permutations(range(n)):
            l,p=pair_from_permutation(order)
            sl+=l;sp+=p;slp+=l*p
            count+=1
        m=factorial(n)
        assert Q(sl,m)==leaf[n],('exhaustive-leaf',n)
        assert Q(sp,m)==path[n],('exhaustive-path',n)
        assert Q(slp,m)==mixed[n],('exhaustive-mixed',n)
    return count

if __name__=='__main__':
    moment_recurrence(100)
    n=exhaustive(8)
    print(f'PASS: all exact moment/covariance recurrences through n=100; {n} exhaustive BST permutations through n=8.')
