import json
from collections import defaultdict
A=json.load(open("output/artifacts/tri_123_n10.json"))
B=json.load(open("output/artifacts/tri_132_n10.json"))
CAT=[1,1,2,5,14,42,132,429,1430,4862,16796]
# 1. Catalan marginals
for n in range(11):
    assert A[str(n)]["count"]==CAT[n], n
    assert B[str(n)]["count"]==CAT[n], n
    assert A[str(n)]["replay_ok"]==True and A[str(n)]["dyck_ok"]==True
print("Catalan + replay OK for all n<=10")
# 2. Elizalde: 123 has at most 2 fixed points
for n in range(11):
    for k in A[str(n)]["tri"]:
        fp=int(k.split(",")[0])
        assert fp<=2, (n,k)
print("Elizalde fp<=2 for 123 confirmed n<=10")
# 3. Eulerian (des) marginals for 123
print("des marginals 123:")
for n in range(8):
    d=defaultdict(int)
    for k,v in A[str(n)]["tri"].items():
        f,e,dd=map(int,k.split(","))
        d[dd]+=v
    print(n, dict(sorted(d.items())))
# Barnabei table row check: n=7: 0:0,3:56,4:252,5:120? paper: n=7: 0,0,0,56,252,120,1
d7=defaultdict(int)
for k,v in A["7"]["tri"].items():
    dd=int(k.split(",")[2]); d7[dd]+=v
print("n=7 des:",dict(sorted(d7.items())),"expect {3:56,4:252,5:120,6:1}")
assert dict(d7)=={3:56,4:252,5:120,6:1}
# 4. joint (exc,des),(fp,des) tables -> save
excdes={}; fpdes={}
for n in range(11):
    e=defaultdict(int); f=defaultdict(int)
    for k,v in A[str(n)]["tri"].items():
        fp,ex,dd=map(int,k.split(","))
        e[(ex,dd)]+=v; f[(fp,dd)]+=v
    excdes[str(n)]={"%d,%d"%k:v for k,v in sorted(e.items())}
    fpdes[str(n)]={"%d,%d"%k:v for k,v in sorted(f.items())}
json.dump({"exc_des":excdes,"fp_des":fpdes},open("output/artifacts/joint_123_n10.json","w"),indent=1)
print("wrote joint_123_n10.json")
# 5. minimal divergence cells 123 vs 132 trivariate
divs=[]
for n in range(11):
    keys=set(A[str(n)]["tri"])|set(B[str(n)]["tri"])
    for k in sorted(keys):
        a=A[str(n)]["tri"].get(k,0); b=B[str(n)]["tri"].get(k,0)
        if a!=b:
            divs.append((n,k,a,b))
print(f"total divergent cells: {len(divs)}")
# minimal per n
for n in range(11):
    dn=[x for x in divs if x[0]==n]
    print(f"n={n} ndiv={len(dn)} first3={dn[:3]}")
# global minimal (lex by n)
print("first 15 divergent cells:", divs[:15])
json.dump([{"n":n,"cell":k,"N123":a,"N132":b} for n,k,a,b in divs],open("output/artifacts/divergence_123_vs_132.json","w"),indent=1)
# 6. check (fp,exc) joint equality 123 vs 132? Elizalde says differ; show
print("fp,exc marginal n=5 123 vs 132:")
def fpe(n,D):
    d=defaultdict(int)
    for k,v in D[str(n)]["tri"].items():
        fp,ex,dd=map(int,k.split(","))
        d[(fp,ex)]+=v
    return dict(sorted(d.items()))
print("123:",fpe(5,A)); print("132:",fpe(5,B))
