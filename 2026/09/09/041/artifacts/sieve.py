# Twin census [1030000000,1050000000]
LO=1030000000
HI=1050000000
N=HI-LO+1

import math,time,json
t0=time.time()

lim=int(math.isqrt(HI))+1
bs=bytearray(b'\x01')*(lim+1)
bs[0:2]=b'\x00\x00'
for i in range(2,int(math.isqrt(lim))+1):
    if bs[i]:
        step=i; start=i*i
        bs[start:lim+1:step]=b'\x00'*(((lim+1-1-start)//step)+1)
base=[i for i in range(2,lim+1) if bs[i]]
print("nbase",len(base),"t",time.time()-t0,flush=True)

is_p=bytearray(b'\x01')*N
for p in base:
    start=((LO+p-1)//p)*p
    if start<p*p: start=p*p
    if start>HI: continue
    is_p[start-LO:N:p]=b'\x00'*(((HI-start)//p)+1)
print("sieved",time.time()-t0,flush=True)

twins=[]
for n in range(LO if LO%2==1 else LO+1, HI-1, 2):
    if is_p[n-LO] and is_p[n+2-LO]:
        twins.append(n)
C=len(twins)
print("C",C,"t",time.time()-t0,flush=True)

gaps=[twins[i+1]-twins[i] for i in range(C-1)]
G=max(gaps) if gaps else 0
gi=gaps.index(G) if gaps else -1
print("G",G,"at idx",gi,flush=True)
if gi>=0:
    print("pair1",twins[gi],twins[gi]+2,"pair2",twins[gi+1],twins[gi+1]+2,flush=True)

cousin=None
for n in range(LO, HI-3):
    if is_p[n-LO] and is_p[n+4-LO]:
        cousin=n
        break
print("cousin",cousin,cousin+4 if cousin else None,flush=True)

import collections
ctr=collections.Counter(gaps)
print("ngaps",len(gaps),"distinct",len(ctr),flush=True)
print("top gaps",sorted(ctr.items(),key=lambda x:-x[0])[:10],flush=True)
print("total time",time.time()-t0,flush=True)

out={"LO":LO,"HI":HI,"C":C,"G":G,
 "gap_index":gi,
 "pair1":[twins[gi],twins[gi]+2] if gi>=0 else None,
 "pair2":[twins[gi+1],twins[gi+1]+2] if gi>=0 else None,
 "cousin":[cousin,cousin+4] if cousin else None,
 "first_twins":twins[:10],"last_twins":twins[-10:]}
with open("output/summary.json","w") as f: json.dump(out,f,indent=1)
with open("output/twins.json","w") as f: json.dump(twins,f)
with open("output/gaps.json","w") as f: json.dump(gaps,f)
print("saved",flush=True)
