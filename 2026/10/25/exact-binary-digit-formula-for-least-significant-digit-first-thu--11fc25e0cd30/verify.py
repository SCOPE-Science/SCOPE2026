from collections import deque

def delta(x,bit):
    j,s=x
    z=j+bit
    return (z//2,s^(z%2))

def states(c):
    seen={(c,0)}; que=deque([(c,0)])
    while que:
        q=que.popleft()
        for b in (0,1):
            z=delta(q,b)
            if z not in seen:
                seen.add(z);que.append(z)
    return seen

def formula(c):
    if c<4: return (2,3,5,6)[c]
    m=c.bit_length()-1
    val=7
    for e in range(2,m):
        r=c%(1<<e)
        val+=2 if r==0 else 3 if r==1 or r==(1<<e)-1 else 4
    val+=2*(c>=3*(1<<(m-1)))
    val+=(c==3*(1<<(m-1))-1)
    return val

for c in range(16384):
    qs=states(c)
    expected=formula(c)
    assert len(qs)==expected,(c,len(qs),expected,sorted(qs))
print('EXACT_FORMULA_OK 16384 offsets: c=0..16383')
for c in range(513):
    qs=states(c)
    index={q:(q[0].bit_count()^q[1])%2 for q in qs}
    for iteration in range(40):
        signs={q:(index[q],index[delta(q,0)],index[delta(q,1)]) for q in qs}
        values={sig:i for i,sig in enumerate(sorted(set(signs.values())))}
        nxt={q:values[signs[q]] for q in qs}
        if len(set(nxt.values()))==len(qs):break
        index=nxt
    assert len(set(nxt.values()))==len(qs),(c,len(qs),len(set(nxt.values())))
print('DISTINGUISHABILITY_OK 513 offsets: c=0..512 via partition refinement')
for m in range(2,14):
    vals={c:formula(c) for c in range(1<<m,1<<(m+1))}
    assert min(vals.values())==2*m+3,(m,min(vals.values()))
    assert max(vals.values())==4*m+1,(m,max(vals.values()))
    assert vals[1<<m]==min(vals.values()) and vals[(1<<(m+1))-2]==max(vals.values())
print('SHARP_ENVELOPES_OK m=2..13')
