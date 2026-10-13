"""Exact exhaustive enumeration of binary length-3 subsequence spectra."""
from collections import Counter

EXPECTED_MAX = (1,1,1,1,2,2,3,3,4,4,6,10,14,20)
EXPECTED_D = (8,16,32,64,126,247,480,926,1764,3337,6208,11408,20608,36649)
EXPECTED_HIST_16 = {1:22448,2:7331,3:2952,4:2081,5:746,6:624,7:246,8:83,9:66,10:44,11:14,12:4,13:2,14:6,20:2}
EXPECT_TOP = {(56,85,82,85,57,82,57,56),(56,57,82,57,85,82,85,56)}

def deck(n, w):
    one=[0,0]; two=[0]*4; three=[0]*8
    for shift in range(n-1,-1,-1):
        b=(w>>shift)&1
        for i in range(4): three[2*i+b]+=two[i]
        for i in range(2): two[2*i+b]+=one[i]
        one[b]+=1
    return tuple(three)

def verify():
    for n in range(3,17):
        sizes=Counter()
        for w in range(1<<n):sizes[deck(n,w)]+=1
        hist=Counter(sizes.values())
        assert sum(k*v for k,v in hist.items())==1<<n
        assert len(sizes)==EXPECTED_D[n-3], (n,'profiles')
        assert max(hist)==EXPECTED_MAX[n-3], (n,'maximum')
        if n==16:
            assert hist==EXPECTED_HIST_16, hist
            assert {p for p,c in sizes.items() if c==20}==EXPECT_TOP
        print(n,len(sizes),max(hist),hist[max(hist)])
    print('VERIFY_DP_OK')

if __name__=='__main__':verify()
