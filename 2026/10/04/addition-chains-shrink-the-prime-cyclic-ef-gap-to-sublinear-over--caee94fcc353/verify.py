#!/usr/bin/env python3

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

# Return an increasing binary-method addition chain together with predecessor pairs.
def binary_chain(n):
    assert n >= 1
    vals=[1]
    pred={}
    bits=bin(n)[3:]
    cur=1
    for bit in bits:
        nxt=cur+cur
        if nxt not in vals:
            pred[nxt]=(cur,cur)
            vals.append(nxt)
        cur=nxt
        if bit=='1':
            nxt=cur+1
            if nxt not in vals:
                pred[nxt]=(cur,1)
                vals.append(nxt)
            cur=nxt
    assert vals[-1]==n
    return vals,pred

def check_chain(vals,pred,target):
    assert vals[0]==1 and vals[-1]==target
    assert vals==sorted(set(vals))
    seen={1}
    for v in vals[1:]:
        a,b=pred[v]
        assert a in seen and b in seen and a+b==v
        seen.add(v)

# Mode p: select every entry except target p and close target-producing sum to e.
def check_p_mode(p,vals,pred):
    check_chain(vals,pred,p)
    selected=vals[:-1]
    assert all(1 <= a < p for a in selected)
    assert len(selected)==len(set(a%p for a in selected))
    a,b=pred[p]
    assert (a+b) % p == 0
    return len(selected)

# Mode p+1: if p occurs, truncate to p; otherwise close the last sum back to coefficient 1.
def check_pplus_mode(p,vals,pred):
    check_chain(vals,pred,p+1)
    if p in vals[:-1]:
        i=vals.index(p)
        sub=vals[:i+1]
        subpred={v:pred[v] for v in sub[1:]}
        return check_p_mode(p,sub,subpred)
    selected=vals[:-1]
    assert all(1 <= a < p for a in selected)
    a,b=pred[p+1]
    assert (a+b-1) % p == 0
    return len(selected)

# Mode p-1: select the target p-1 as well, then close (p-1)+1 to e.
def check_pminus_mode(p,vals,pred):
    check_chain(vals,pred,p-1)
    selected=vals
    assert all(1 <= a < p for a in selected)
    assert ((p-1)+1) % p == 0
    return len(selected)

count=0
for p in range(3,20000,2):
    if not is_prime(p):
        continue
    vals,pred=binary_chain(p)
    moves=check_p_mode(p,vals,pred)
    assert moves==len(vals)-1
    count += 1

# p+1 example avoiding p: 11+1 = 12 by 1,2,4,8,12.
vals=[1,2,4,8,12]
pred={2:(1,1),4:(2,2),8:(4,4),12:(8,4)}
assert check_pplus_mode(11,vals,pred)==4

# p+1 example that passes through p; truncation must be valid.
vals=[1,2,3,5,10,11,12]
pred={2:(1,1),3:(2,1),5:(3,2),10:(5,5),11:(10,1),12:(11,1)}
assert check_pplus_mode(11,vals,pred)==5

# p-1 example: p=17, chain to 16 has length 4 and selecting all 5 entries gives 5 moves.
vals=[1,2,4,8,16]
pred={2:(1,1),4:(2,2),8:(4,4),16:(8,8)}
assert check_pminus_mode(17,vals,pred)==5

print(f"VERIFY_OK prime_binary_cases={count} max_p=19999 pplus=2 pminus=1")
