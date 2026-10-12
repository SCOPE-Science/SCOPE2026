from collections import defaultdict
from itertools import product

WITNESSES={
'01010001110101': ('01001101', 144, 136),
'01110101010001': ('01101001', 147, 144),
}

def occurrences(word):
    d={'':1}
    for c in word:
        ext={s+c:count for s,count in d.items()}
        for s,count in ext.items():
            d[s]=d.get(s,0)+count
    return d

def classify(w):
    c=occurrences(w)
    bound=(len(w)+1)//2
    full=max(c.values())
    short=max(count for s,count in c.items() if len(s)<=bound)
    return full,short,sorted(s for s,count in c.items() if count==full)

def check():
    failures=[]
    at14=[]
    for n in range(2,15):
        for bits in product('01',repeat=n):
            w=''.join(bits)
            full,short,peak=classify(w)
            if full>short:
                failures.append((w,full,short,peak))
                if n==14:at14.append(w)
                else:raise AssertionError(('earlier', n,w,full,short,peak))
    expected=['01010001110101','01110101010001','10001010101110','10101110001010']
    assert sorted(at14)==expected,(at14,expected)
    for w,(u,number,short_number) in WITNESSES.items():
        full,short,peak=classify(w)
        assert(full,short,peak)==(number,short_number,[u]),(w,full,short,peak)
        counts=defaultdict(int)
        for mask in range(1<<len(w)):
            v=''.join(w[i] for i in range(len(w)) if mask>>i&1)
            counts[v]+=1
        assert counts==occurrences(w)
        bylen=[max(c for key,c in counts.items() if len(key)==r) for r in range(len(w)+1)]
        profiles={
          '01010001110101':[1,7,31,67,111,123,136,130,144,72,36,18,9,3,1],
          '01110101010001':[1,7,30,64,114,129,144,144,147,86,63,27,11,3,1],
        }
        assert bylen==profiles[w], (w,bylen)
    print('VERIFY_OK all_binary_words_n=2..14 failures_before14=0 failures_at14=4 unique_maximizers=2 independent_mask_checks=32768')
if __name__=='__main__':check()
