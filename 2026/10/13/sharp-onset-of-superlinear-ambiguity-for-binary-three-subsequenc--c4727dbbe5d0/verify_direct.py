"""Independent direct triple-index census, no subsequence dynamic programming."""
from collections import Counter
from itertools import combinations

H={1:22448,2:7331,3:2952,4:2081,5:746,6:624,7:246,8:83,9:66,10:44,11:14,12:4,13:2,14:6,20:2}
M=(1,1,1,1,2,2,3,3,4,4,6,10,14,20)

def census(n):
    positions=list(combinations(range(n),3))
    classes=Counter()
    for word in range(1<<n):
        bits=tuple((word>>j)&1 for j in range(n-1,-1,-1))
        spectrum=[0]*8
        for i,j,k in positions:
            spectrum[4*bits[i]+2*bits[j]+bits[k]]+=1
        classes[tuple(spectrum)]+=1
    return classes

def verify():
    for n in range(3,17):
        classes=census(n)
        assert max(classes.values())==M[n-3]
        if n==16:
            assert Counter(classes.values())==H
            assert {p for p,k in classes.items() if k==20}=={
                (56,85,82,85,57,82,57,56),(56,57,82,57,85,82,85,56)}
        print(n, len(classes), max(classes.values()))
    print('VERIFY_DIRECT_OK')
if __name__=='__main__':verify()
