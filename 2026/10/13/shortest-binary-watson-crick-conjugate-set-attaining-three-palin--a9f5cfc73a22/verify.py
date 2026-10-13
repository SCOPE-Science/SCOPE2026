#!/usr/bin/env python3
import itertools, json
from pathlib import Path

def theta(w):
    return "".join("1" if c=="0" else "0" for c in w[::-1])

def via_cuts(w):
    return {theta(w[i:])+w[:i] for i in range(len(w)+1)}

def via_definition(w):
    # Directly implement u v = theta(v) w, independently of the cut formula.
    n=len(w)
    out=set()
    for j in range(n+1):
        for t in itertools.product("01", repeat=j):
            v="".join(t)
            rhs=theta(v)+w
            u=rhs[:n]
            if u+v==rhs:
                out.add(u)
    return out

def pals(S):
    return sorted(x for x in S if x==x[::-1])

root=Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))

profiles=[]
winners={}
for n in range(1,8):
    dist={}
    best=-1
    arr=[]
    for t in itertools.product("01", repeat=n):
        w="".join(t)
        A=via_cuts(w)
        B=via_definition(w)
        assert A==B
        k=len(pals(A))
        dist[str(k)]=dist.get(str(k),0)+1
        if k>best:
            best=k
            arr=[w]
        elif k==best:
            arr.append(w)
    profiles.append({"length":n,"maximum_palindromes":best,"distribution":dict(sorted(dist.items(), key=lambda kv:int(kv[0])))})
    winners[n]=arr

assert profiles==cert["profiles_lengths_1_to_7"]
assert [p["maximum_palindromes"] for p in profiles]==[2,2,2,2,2,2,3]
assert winners[7]==cert["shortest_witnesses"]==["0100011","1011100"]
assert pals(via_cuts("0100011"))==["0001000","0010100","0011100"]
assert pals(via_cuts("1011100"))==["1100011","1101011","1110111"]

comp=str.maketrans("01","10")
assert "0100011".translate(comp)=="1011100"
assert sorted(x.translate(comp) for x in pals(via_cuts("0100011")))==pals(via_cuts("1011100"))

print(
    "VERIFY_OK shortest=7 witnesses=2 max_by_length=2,2,2,2,2,2,3 "
    "witnesses=0100011,1011100 pals_first=0001000,0010100,0011100"
)
