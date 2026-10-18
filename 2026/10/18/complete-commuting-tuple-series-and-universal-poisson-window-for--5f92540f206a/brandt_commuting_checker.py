"""Reproducible small-instance tests for commuting-tuples in Brandt semigroups.
Requires only Python 3's standard library. Run: python brandt_commuting_checker.py
"""
from itertools import permutations
from math import comb, factorial


def groups():
    one = ((0,),)
    c2 = ((0,), (1,))
    s3 = tuple(permutations(range(3)))
    return [('trivial', one, lambda a,b:(0,)),
            ('C2', c2, lambda a,b:((a[0]+b[0])%2,)),
            ('S3', s3, lambda a,b:tuple(a[b[i]] for i in range(3)))]


def counting_commuting_tuples(elements, commutes, K):
    count = [1]
    states = [()]
    for k in range(1, K+1):
        nxt = []
        for p in states:
            for x in elements:
                if all(commutes(x,y) for y in p):
                    nxt.append(p+(x,))
        states = nxt
        count.append(len(states))
    return count


def egf_mul(A,B):
    K=min(len(A),len(B))-1
    return [sum(comb(k,j)*A[j]*B[k-j] for j in range(k+1)) for k in range(K+1)]


def egf_power(A,k):
    R=[1]+[0]*(len(A)-1)
    for _ in range(k): R=egf_mul(R,A)
    return R


def predicted(n,group_size,group_commuting,K):
    C=group_commuting
    total=egf_power(C,n)
    for a in range(1,n):
        for b in range(1,n-a+1):
            coefficient=factorial(n)//(factorial(a)*factorial(b)*factorial(n-a-b))
            E=[group_size**k*sum((-1)**(i+j)*comb(a,i)*comb(b,j)*((a-i)*(b-j))**k
                 for i in range(a+1) for j in range(b+1)) for k in range(K+1)]
            P=egf_mul(E,egf_power(C,n-a-b))
            total=[x+coefficient*y for x,y in zip(total,P)]
    return egf_mul([1]*(K+1),total)


def run():
    tests=0
    for name,G,mul in groups():
        q=len(G)
        eq=lambda a,b:mul(a,b)==mul(b,a)
        cg=counting_commuting_tuples(G,eq,4)
        for n in range(1,5):
            K=4 if q<=2 and n<=3 else 3 if n<=3 else 2
            el=(None,)+tuple((i,a,j) for i in range(n) for j in range(n) for a in G)
            def prod(x,y):
                if x is None or y is None or x[2]!=y[0]:return None
                return (x[0],mul(x[1],y[1]),y[2])
            eqB=lambda x,y:prod(x,y)==prod(y,x)
            actual=counting_commuting_tuples(el,eqB,K)
            theoretical=predicted(n,q,cg,K)
            assert actual==theoretical,(name,n,actual,theoretical)
            print(name, n, actual)
            tests+=1
    print('ALL_BRANDT_COMMUTING_COUNTS_PASSED',tests)


if __name__=='__main__':run()
