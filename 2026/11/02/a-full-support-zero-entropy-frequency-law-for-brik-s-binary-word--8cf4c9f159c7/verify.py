"""Independent finite checks for the Brik-word cylinder theorem.
Pure standard library. Finite checks do not certify limiting assertions.
"""
from collections import Counter
from math import log2

def block_counts(s,m):
    return Counter(s[t:t+m] for t in range(len(s)-m+1))

def entropy(counts):
    tot=sum(counts.values())
    return -sum(v/tot*log2(v/tot) for v in counts.values())

def run():
    B='101'
    words=['0','1','01','10','11','101','111','1111','10101']
    rows=[]
    for i in range(1,22):
        assert len(B)==2**(i-1)+i+1
        assert '00' not in B
        if i>=5:
            for w in words:
                m=len(w)
                if 2**(i-1)+1>=m:
                    N=sum(B[z:z+m]==w for z in range(len(B)-m+1))
                    Bnext=B+B[i:]
                    Nnext=sum(Bnext[z:z+m]==w for z in range(len(Bnext)-m+1))
                    assert -i <= Nnext-2*N <= m-1, (i,w,N,Nnext)
        if i in (7,10,13,16,19,21):
            cnt=block_counts(B,4)
            rows.append([i,len(B),cnt.get('1111',0),round(cnt.get('1111',0)/len(B),9),round(entropy(block_counts(B,8))/8,6)])
        B=B+B[i:]
    print('LENGTH AND COUNT RECURRENCE: PASS (levels 1..21, 9 patterns)')
    print('No forbidden 00: PASS')
    print('i,length,count(1111),fraction(1111), H_8/8')
    for row in rows:print(*row,sep=',')
    # reconstruct exact deletion embeddings for small levels
    for j in range(2,8):
        orig='101'
        seq=[None,orig]
        for i in range(1,j+5):
            orig=orig+orig[i:]
            seq.append(orig)
        base=seq[j]
        for I in range(j+1,j+5):
            target=seq[I]
            template=base*2**(I-j)
            it=iter(template)
            assert all(any(ch==v for v in it) for ch in target)
            L=len(template)-len(target)
            assert L==2**(I-j)*(j+1)-I-1,(j,I,L)
    print('DELETION EMBEDDING AND LENGTH DEFECT: PASS (j=2..7, I=j+1..j+4)')
    print('All finite checks PASS')

if __name__=='__main__':run()
