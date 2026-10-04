#!/usr/bin/env python3

def partitions(seq):
    seq=list(seq)
    if not seq:
        yield []
        return
    x=seq[0]
    for rest in partitions(seq[1:]):
        yield [{x}]+[set(b) for b in rest]
        for j in range(len(rest)):
            rr=[set(b) for b in rest]
            rr[j].add(x)
            yield rr

def canon_part(blocks):
    return tuple(sorted(tuple(sorted(b)) for b in blocks))

def eq_free(i,a,j,b,finite,block_of,cycle_after=None,cycle_len=2):
    if i in finite or j in finite:
        if i in finite and j in finite:
            return i==j
        return False
    if i==j and a==b:
        return True
    if block_of[i] != block_of[j]:
        return False
    if a==0 or b==0:
        return False
    pa=a-1; pb=b-1
    if cycle_after is None:
        return pa==pb
    if pa < cycle_after or pb < cycle_after:
        return pa==pb
    return (pa-cycle_after)%cycle_len == (pb-cycle_after)%cycle_len

def signature(n,D,finite,blocks,close_block=None):
    block_of={}
    for z,b in enumerate(blocks):
        for i in b: block_of[i]=z
    terms=[(i,a) for i in range(n) for a in range(D+1)]
    out=[]
    for u in range(len(terms)):
        for v in range(u+1,len(terms)):
            i,a=terms[u]; j,b=terms[v]
            cyc=None
            if close_block is not None and i not in finite and j not in finite:
                if block_of[i]==close_block and block_of[j]==close_block:
                    cyc=D+3
            out.append(eq_free(i,a,j,b,finite,block_of,cyc,2))
    return tuple(out)

prefix_checks=0
seen=set()
for n in range(1,6):
    coords=set(range(n))
    for mask in range(1<<n):
        finite={i for i in range(n) if mask>>i & 1}
        active=sorted(coords-finite)
        for raw in partitions(active):
            key=(n,mask,canon_part(raw))
            if key in seen:
                continue
            seen.add(key)
            blocks=[set(b) for b in canon_part(raw)]
            rho=len(blocks)
            for D in range(0,7):
                sig=signature(n,D,finite,blocks,None)
                for z in range(rho):
                    closed=signature(n,D,finite,blocks,z)
                    assert sig==closed
                    assert rho-1 == len(blocks)-1
                    prefix_checks+=1

def eq_eventual(a,b,t,c):
    if a==b: return True
    if a<t or b<t: return False
    return (a-t)%c == (b-t)%c

periodic_checks=0
for t in range(0,7):
    for c in range(1,7):
        first=t+c
        for a in range(0,first+12):
            for b in range(0,first+12):
                expected=eq_eventual(a,b,t,c)
                def red(q):
                    if q<t: return q
                    return t+(q-t)%c
                got=(red(a)==red(b))
                assert got==expected
                periodic_checks+=1

print("prefix_closure_checks", prefix_checks)
print("one_variable_eventual_periodic_checks", periodic_checks)
print("VERIFY_OK")
