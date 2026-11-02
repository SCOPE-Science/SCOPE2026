"""Independent, unpruned exact enumeration at palindromic-subsequence lengths 1..10."""
from itertools import combinations, product
from collections import Counter

EXPECTED = {
 1:{1:2},2:{1:2,2:4},3:{2:6,3:8},4:{3:24,4:16},
 5:{3:2,4:60,5:32},6:{4:22,5:180,6:64},
 7:{5:52,6:420,7:128},8:{5:2,6:316,7:1116,8:256},
 9:{7:712,8:2508,9:512},10:{7:46,8:3076,9:6228,10:1024},
}
def embedded(host,target):
    j=0
    for ch in host:
        if ch==target[j]:
            j+=1
            if j==len(target):return True
    return False

def index(host):
    count=0; seen=set()
    for ch in host:
        seen.add(ch)
        if len(seen)==2:count+=1;seen=set()
    return count

for k in range(1,11):
    palindromes=[''.join(p+(p[::-1] if k%2==0 else p[-2::-1])) for p in product('01',repeat=(k+1)//2)]
    tally=Counter()
    for zeros in combinations(range(2*k),k):
        zs=set(zeros)
        host=''.join('0' if j in zs else '1' for j in range(2*k))
        if all(embedded(host,pal) for pal in palindromes):
            tally[index(host)]+=1
    assert dict(tally)==EXPECTED[k], (k,tally,EXPECTED[k])
print('VERIFY_INDEPENDENT_OK unpruned_complete_length_k=1..10 palindrome_index_distributions=true')
