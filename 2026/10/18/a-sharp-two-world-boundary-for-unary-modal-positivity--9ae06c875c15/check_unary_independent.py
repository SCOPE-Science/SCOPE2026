#!/usr/bin/env python3
"""Independent 8-bit truth-table closure using all 256 possible unary operations."""
EXPECTED = {
 0:(3,4,3,0),1:(9,16,9,0),2:(18,64,18,0),3:(18,64,18,0),
 4:(18,64,18,0),5:(6,16,6,0),6:(6,16,6,0),7:(10,64,18,8),
 8:(9,16,9,0),9:(3,4,3,0),10:(6,16,6,0),11:(6,16,6,0),
 12:(18,64,18,0),13:(6,16,6,0),14:(10,64,18,8),15:(5,16,6,1),
}

def at(signature,valuation):
    return (signature >> (2 * valuation)) & 3

def lift(source, fn):
    return sum(fn(at(source,k)) << (2*k) for k in range(4))

def lattice(a,b,meet):
    op=(lambda x,y: x&y) if meet else (lambda x,y:x|y)
    return sum(op(at(a,k),at(b,k)) << (2*k) for k in range(4))

def op_mask(m,box):
    def apply(x):
        r=0
        for w in range(2):
            successors=[v for v in range(2) if m&(1<<(2*w+v))]
            q=all(x&(1<<v) for v in successors) if box else any(x&(1<<v) for v in successors)
            if q:r|=(1<<w)
        return r
    return apply

def generate(mask,with_complement):
    operations={0,255, (0<<0)|(1<<2)|(2<<4)|(3<<6)}
    while True:
        old=operations.copy()
        for sig in old:
            operations.add(lift(sig,op_mask(mask,True)))
            operations.add(lift(sig,op_mask(mask,False)))
            if with_complement:operations.add(sig ^ 255)
        for a in old:
            for b in old:
                operations.add(lattice(a,b,True));operations.add(lattice(a,b,False))
        if operations==old:break
        assert len(operations)<=256
    return operations

def monotone(sig):
    return all((a&b)!=a or ((at(sig,a)&at(sig,b))==at(sig,a)) for a in range(4) for b in range(4))

def main():
    for mask in range(16):
        pos=generate(mask,False)
        full=generate(mask,True)
        mono={sig for sig in full if monotone(sig)}
        found=(len(pos),len(full),len(mono),len(mono-pos))
        assert found==EXPECTED[mask],(mask,found)
        print(mask,found)
    print('PASS independent all-frames exhaustive 8-bit full-algebra saturation')

if __name__=='__main__':main()
