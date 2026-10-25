"""Independent dynamic-programming census and character-sum replay.
Graph is the edge-once subdivision of K_{2,q}.
"""
from collections import defaultdict
from itertools import product

def page_types(a0,a1):
    return [(b,x,y) for b,x,y in product(range(4),repeat=3)
            if b!=a0 and b!=a1 and x!=a0 and x!=b
            and y!=a1 and y!=b and x!=y]

def dynamic(a0,a1,q):
    colors0=[c for c in range(4) if c!=a0]
    colors1=[c for c in range(4) if c!=a1]
    # Parity of occurrences and support are tracked separately: a positive
    # even multiplicity invalidates strong oddness despite parity zero.
    states={(0,0,0,0):1}
    for _ in range(q):
        nxt=defaultdict(int)
        for (par0,used0,par1,used1),ways in states.items():
            for b,x,y in page_types(a0,a1):
                bit0=1<<colors0.index(x)
                bit1=1<<colors1.index(y)
                nxt[par0^bit0,used0|bit0,par1^bit1,used1|bit1]+=ways
        states=nxt
    return sum(ways for (p0,u0,p1,u1),ways in states.items()
               if p0==u0 and p1==u1)

def formula(q):
    assert q>=2 and q%2==0
    return 12*4**q+6*3**q-18*2**q-6

def character_sum(a0,a1,q):
    assert q>=2 and q%2==0
    C=set(range(4)); pages=page_types(a0,a1)
    total=0
    for z0 in sorted(C-{a0}):
        for z1 in sorted(C-{a1}):
            c0=min(C-{a0,z0});c1=min(C-{a1,z1})
            admissible=[(b,x,y) for b,x,y in pages if x!=z0 and y!=z1]
            for e in (1,-1):
                for f in (1,-1):
                    lam=sum((e if x==c0 else 1)*(f if y==c1 else 1)
                            for b,x,y in admissible)
                    total+=e*f*lam**q
    assert total%4==0
    return total//4

def main():
    for q in [2,4,6,8]:
        same=dynamic(0,0,q); different=dynamic(0,1,q)
        assert same==character_sum(0,0,q)==3*(3**q+2**q-1)//2
        assert different==character_sum(0,1,q)==4**q-2**(q+1)
        total=4*same+12*different
        assert total==formula(q)
        print(f'q={q}: same={same}, different={different}, total={total}')
    print('THETA_VERIFICATION_OK')
if __name__=='__main__':main()
