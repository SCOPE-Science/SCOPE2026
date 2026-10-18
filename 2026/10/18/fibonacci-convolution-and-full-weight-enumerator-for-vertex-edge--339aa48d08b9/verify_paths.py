"""Independent finite checks for path vertex-edge perfect Roman weight counts.

The enumerator uses the original edge condition, not the zero-run transfer.
The separate recurrence is extracted from the claimed rational identity.
"""
from collections import defaultdict
from itertools import product

SHIFTS=((1,1),(1,2),(2,1),(2,2),(3,2),(4,2),(4,3))


def count_bruteforce(n):
    ans=defaultdict(int)
    for a in product((0,1,2),repeat=n):
        okay=True
        for i in range(n-1):
            if a[i]==a[i+1]==0:
                count_left=int(i>0 and a[i-1]==2)
                count_right=int(i+2<n and a[i+2]==2)
                if count_left!=1 and count_right!=1:
                    okay=False
                    break
        if okay:
            ans[sum(a)]+=1
    return dict(ans)


def rational_coefficients(nmax):
    result=[]
    for n in range(nmax+1):
        p=defaultdict(int)
        if n in (0,1):p[0]+=1
        if n==3:p[2]+=1
        for dn,dw in SHIFTS:
            if n>=dn:
                for w,v in result[n-dn].items():p[w+dw]+=v
        result.append(dict(p))
    return result


def fibonacci(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a


def verify():
    C=rational_coefficients(160)
    checked=0
    for n in range(13):
        B=count_bruteforce(n)
        assert C[n]==B, (n,C[n],B)
        checked+=3**n
    for n in range(1,161):
        p=C[n]
        k=n//2
        assert min(p)==k,(n,'min',min(p),k)
        if n%2:
            expected=fibonacci(k+1)
        else:
            expected=sum(fibonacci(i+1)*fibonacci(k-i+1) for i in range(k+1))
        assert p[k]==expected,(n,p[k],expected)
    # Directly test the empty word and the first nonempty cases.
    assert C[0]=={0:1}
    assert C[1]=={0:1,1:1,2:1}
    assert C[2]=={1:2,2:3,3:2,4:1}
    print(f'VERIFICATION_OK brute_lengths=0..12 checked_words={checked} rational_lengths=0..160 optimum_lengths=1..160')

if __name__=='__main__':verify()
