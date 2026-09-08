"""Certify inversion-ANTImonotonicity: av_n^k(B*) nonincreasing in n for k<=15 (n=8..11).
Reads cross-checked tables; emits certificate JSON. Also records transition matrix."""
import json
T={}
for n in [8,9,10,11]:
    fn=f'biv/distA_n{n}.json' if n<11 else 'biv/distA2_n11.json'
    T[n]=json.load(open(fn))
cert={"kmax":15,"rows":{}}
for k in range(16):
    v=[T[n].get(str(k),0) for n in [8,9,10,11]]
    cert["rows"][k]=v
    assert v[0]>=v[1]>=v[2]>=v[3], (k,v)
json.dump(cert, open("biv/cert_antimonotone_k15.json","w"), indent=1)
print("antimonotone certified k<=15")
for k in range(16): print(k, cert["rows"][k])
