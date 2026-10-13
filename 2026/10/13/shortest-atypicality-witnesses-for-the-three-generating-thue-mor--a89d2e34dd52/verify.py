#!/usr/bin/env python3
import json, math
from itertools import product
from pathlib import Path

def mu(s):
    return "".join("01" if c=="0" else "10" for c in s)

def tm_power(n):
    s="0"
    for _ in range(n):
        s=mu(s)
    return s

def tm_bit_prefix(N):
    return "".join(str(i.bit_count() & 1) for i in range(N))

def image_word(w,A,B):
    return "".join(A if c=="0" else B for c in w)

def factor_power(L):
    if L==1:
        return 1
    if L==2:
        return 3
    return 2+math.ceil(math.log2(L-1))

def is_factor(q):
    # Proposition 2.1 of Almeida--Klima gives this finite exact test.
    return q in tm_power(factor_power(len(q)))

root=Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))

# Independent generation check for the finite factor sets used below.
long_tm=tm_bit_prefix(2048)
for L in range(1,14):
    exact=set(tm_power(factor_power(L))[i:i+L]
              for i in range(len(tm_power(factor_power(L)))-L+1))
    direct=set(long_tm[i:i+L] for i in range(len(long_tm)-L+1))
    assert exact==direct

# Excluded global language-preserving morphisms mu^n and xi o mu^n.
trivial=set()
A0,B0="0","1"
tr=str.maketrans("01","10")
for n in range(8):
    trivial.add((A0,B0))
    trivial.add((A0.translate(tr),B0.translate(tr)))
    A0,B0=mu(A0),mu(B0)

expected={
    "aabab":(13,"0","11001"),
    "abaaba":(8,"0","11"),
    "aabbaab":(13,"0","101"),
}
total_tested=0
summary=[]
for name,(cost,EA,EB) in expected.items():
    info=cert["patterns"][name]
    w=info["pattern_binary"]
    ca=w.count("0")
    cb=w.count("1")
    valid=[]
    tested=0
    # This exhausts every nonerasing morphism whose image can challenge
    # minimality or tie the claimed minimum.
    for la in range(1,cost//ca+1):
        for lb in range(1,cost//cb+1):
            L=ca*la+cb*lb
            if L>cost:
                continue
            for At in product("01", repeat=la):
                A="".join(At)
                for Bt in product("01", repeat=lb):
                    B="".join(Bt)
                    tested+=1
                    if (A,B) in trivial:
                        continue
                    q=image_word(w,A,B)
                    if is_factor(q):
                        valid.append((L,A,B,q))
    total_tested += tested
    assert tested==info["tested_morphisms_through_claimed_minimum"]
    best=min(x[0] for x in valid)
    mins=sorted(x for x in valid if x[0]==best)
    assert best==cost
    assert len(mins)==2
    assert (cost,EA,EB,image_word(w,EA,EB)) in mins

    # The two minimizers are exactly exchanged by xi.
    cA=EA.translate(tr)
    cB=EB.translate(tr)
    assert set((A,B) for _,A,B,_ in mins)=={(EA,EB),(cA,cB)}

    certmins=sorted((z["image_length"],z["A"],z["B"],z["image"])
                    for z in info["minimum_witnesses"])
    assert certmins==mins
    summary.append(f"{name}:{best}:{len(mins)}")

assert total_tested==276
print("VERIFY_OK tested=276 " + " ".join(summary))
