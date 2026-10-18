from collections import Counter,defaultdict

def period(f):
    state=0; seen=set(); s=[]
    for _ in range(32):
        if state in seen:return None
        seen.add(state)
        s.append((state>>4)&1)
        state=((state<<1)&31)|((state>>4)^((f>>(state&15))&1))
    if state!=0:return None
    return s

def lc(w):
    p=sum(bit<<i for i,bit in enumerate(w)); v=0
    while (p.bit_count()&1)==0 and p:
        q=0;r=0
        for i in range(p.bit_length()-1,-1,-1):
            r^=(p>>i)&1
            if i:q |=r<<(i-1)
        assert r==0
        p=q;v+=1
    return 32-v

def discrepancy(w):
    s=0;v=[0]
    for x in w:s+=2*x-1;v.append(s)
    assert s==0
    return max(v)-min(v)

def main():
    d=Counter();lc_hist=Counter(); disc_hist=Counter();examples={}
    for f in range(65536):
        w=period(f)
        if w is None:continue
        c=lc(w); e=discrepancy(w)
        d[c,e]+=1;lc_hist[c]+=1;disc_hist[e]+=1;examples.setdefault((c,e), f)
    print('total',sum(d.values()),'lc',sorted(lc_hist.items()),'disc',sorted(disc_hist.items()))
    print('joint',sorted(d.items()))
    print('examples',examples)
if __name__=='__main__':main()
