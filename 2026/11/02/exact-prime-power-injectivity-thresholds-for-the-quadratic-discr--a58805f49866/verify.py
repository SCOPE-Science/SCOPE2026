#!/usr/bin/env python3
"""Independent exact checks of a prime-power quadratic-residue collision theorem.
No external packages are required. Exhaustive only for the listed finite cases.
"""

def isprime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))

def predicted(p, a):
    if p == 2:
        return 2 if a == 1 else 2**(a-2) + 1
    k = a // 2
    return (3*p**k + 1)//2 if a % 2 == 0 else ((p+2)*p**k + 1)//2

def predicted_pair(p,a):
    if p==2:
        return (1,2) if a==1 else (2**(a-2),2**(a-2)+1)
    k=a//2
    return ((p**k+1)//2,(3*p**k+1)//2) if a%2==0 else (((p-2)*p**k+1)//2,((p+2)*p**k+1)//2)

def independent_check(p, a):
    m=p**a
    target=predicted(p,a)
    if target > 15000: return False
    before={}
    for j in range(1,target+1):
        residue=(2*j*(j-1))%m
        assert (residue in before)==(j==target), (p,a,j)
        if j==target:
            assert (before[residue],j)==predicted_pair(p,a),(p,a,j)
        else:
            before[residue]=j
    # Separate all-pair integer divisibility at the boundary, to check uniqueness.
    i_target, j_target=predicted_pair(p,a)
    count=0
    for i in range(1,target):
        if (2*(target-i)*(target+i-1))%m==0:
            count+=1
            assert i==i_target
    assert count==1
    return True

if __name__=='__main__':
    fields=0; residues=0
    for p in range(2,50):
        if not isprime(p):continue
        for a in range(1,11):
            t=predicted(p,a)
            if t>15000:break
            assert independent_check(p,a)
            fields+=1;residues+=t
    print(f'VERIFY_OK prime_powers={fields} residues_checked={residues} unique_first_pairs={fields}')
