---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact verification

Run `python check_tutte_integral.py` with Python 3 and SymPy. The program regenerates the full point/matching incidence graph and distance matrix, verifies cubic degree, 30 vertices, 45 edges, diameter four and girth eight. It constructs all signed length-five magnitude chains of degrees two, three and four for each of the two inequivalent ordered point-to-matching endpoint types. The program checks the chain identity, prints the exact boundary ranks and integer Smith factors and verifies the \(S_6\) orbit sizes \(45\) and \(180\). Its assertions test the global result \(\operatorname{MH}_{3,5}(T;\mathbb Z)\cong\mathbb Z^{1440}\).

Representative output:
```
d=1 C2/C3/C4=8/36/56 ranks=8/28 SNF_B4={1: 28} H3=Z^0
d=3 C2/C3/C4=14/45/40 ranks=14/27 SNF_B4={1: 27} H3=Z^4
S6 orbit 1 45 ordered point-to-line pairs
S6 orbit 3 180 ordered point-to-line pairs
PASS: integral MH_(3,5) = Z^1440; all relevant Smith factors are units
```
The original comparison result used characteristic-two ranks only. Exact integer Smith factors are needed to establish the present integral freeness. The computation proves only this finite graph and bidegree; it does not imply a general formula for other generalized quadrangles.
