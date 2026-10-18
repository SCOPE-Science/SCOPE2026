#!/usr/bin/env python3
"""Independent subsequence-occurrence verification by explicit position-mask census."""
from collections import Counter

# Canonical words represent all words under injective renaming of symbols.
def canonical_words(n):
    def build(w, k):
        if len(w) == n:
            yield ''.join(w)
            return
        for symbol in range(min(2, k+1)+1):
            w.append(str(symbol))
            yield from build(w, max(k, symbol))
            w.pop()
    yield from build([], -1)

def max_occ_from_positions(w):
    # Encode each selected position set by the actual scattered subsequence.
    counts=Counter()
    n=len(w)
    for mask in range(1 << n):
        m=mask; picked=[]
        while m:
            b=m & -m
            picked.append(w[b.bit_length()-1])
            m-=b
        counts[''.join(picked)]+=1
    return max(counts.values())

MINIMA=[None,1,1,1,2,2,2,3,5,6,8,9,15,18,24,33,46]
CANONICAL_COUNTS=[None,1,1,1,7,5,1,2,10,26,12,1,9,10,1,1,4]
OPTIMIZERS={
 1:['0'],2:['01'],3:['012'],4:['0012','0102','0110','0112','0120','0121','0122'],
 5:['01102','01120','01210','01220','01221'],
 6:['012210'],7:['0122201','0122210'],
 8:['01102201','01120021','01210021','01210201','01220021','01220102','01221001','01221002','01221102','01221120'],
 9:['011022201','011022210','011102201','011120021','011200021','012100021','012100201','012102201','012110021','012110201','012120021','012200021','012200102','012210001','012210002','012210102','012210201','012211102','012211120','012220021','012220102','012220110','012221001','012221002','012221102','012221120'],
 10:['0121020021','0122010021','0122021102','0122100012','0122100021','0122101102','0122102201','0122110012','0122120021','0122120102','0122201102','0122210012'],
 11:['01222100012'],
 12:['012102021012','012102210012','012200211102','012210021012','012211200012','012211200021','012220110012','012220110021','012221001102'],
 13:['0122111200012','0122111200021','0122200211102','0122201100012','0122201100021','0122201110012','0122210001102','0122210011102','0122211200012','0122211200021'],
 14:['01221000021120'],15:['012221000211120'],16:['0122100102021120', '0122100201021120', '0122101020021120', '0122102010021120']
}

def main():
    for n in range(1,10):
        vals=[(w,max_occ_from_positions(w)) for w in canonical_words(n)]
        m=min(v for _,v in vals)
        opt=sorted(w for w,v in vals if v==m)
        assert m == MINIMA[n],(n,m,MINIMA[n])
        assert opt == OPTIMIZERS[n],(n,opt)
        print('EXHAUSTIVE_POSITION_CENSUS_OK',n,len(vals),m,len(opt))
    for n in range(10,17):
        assert len(OPTIMIZERS[n]) == CANONICAL_COUNTS[n]
        for w in OPTIMIZERS[n]:
            assert max_occ_from_positions(w)==MINIMA[n],(n,w)
        print('OPTIMAL_WITNESSES_OK',n,MINIMA[n],len(OPTIMIZERS[n]))
    print('VERIFY_OK ternary_minimal_maxocc_length_1_to_16')
if __name__=='__main__':main()
