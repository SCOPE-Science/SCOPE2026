#!/usr/bin/env python3
"""Second, integer-only exhaustive check of binary overlap-free nine-square cutoff."""
state=[(0,(0,))]
by_length=[];witnesses=[]
for length in range(1,49):
    nxt=[]
    for old,best in state:
        for bit in (0,1):
            x=old*2+bit
            if any((x^(x>>p))&((1<<(p+1))-1)==0 for p in range(1,(length-1)//2+1)):
                continue
            m=-10**9
            for h in range(1,length//2+1):
                mask=(1<<h)-1
                if (x&mask)==((x>>h)&mask):
                    m=max(m,best[length-2*h]+1)
            nxt.append((x,best+(m,)))
    nine=sorted(f'{x:0{length}b}' for x,dp in nxt if dp[-1]>=9)
    if length<48:assert not nine
    if length==48:
        assert len(nxt)==416 and len(nine)==2
        witnesses=nine
    by_length.append((length,len(nxt),len(nine)))
    state=nxt
assert witnesses==['001001101001011010011001011001101001011010011011','110110010110100101100110100110010110100101100100']
print('Lengths checked:',len(by_length))
print('Length 47:',by_length[46])
print('Length 48:',by_length[47])
print('Unique words:',witnesses)
print('INDEPENDENT_INTEGER_OVERLAP_CHECK_OK')
