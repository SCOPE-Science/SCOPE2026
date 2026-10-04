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
# Verification

The proof uses the exact identity
\[
f(N[u])=(N-n_i)-2t_i+f(u)
\]
for \(u\) in part \(V_i\), where \(t_i\) counts negative labels outside that part. The minimality witness criterion then gives the lower bound \(M\ge\lfloor(N-L)/2\rfloor\) on the total number \(M\) of negative labels. The construction puts exactly that many negative labels outside a largest part and checks every closed-neighborhood inequality directly.

`verify.py` independently enumerates all ordered positive part-size profiles through order \(10\) and every vertex labeling by \(\{-1,+1\}\). It tests signed domination from the closed-neighborhood definition, tests minimality by attempting every allowed positive-to-negative decrease, and compares the resulting maximum weight with the theorem. It also checks the stated extremal construction for every profile.

The exhaustive range is finite and does not certify orders above \(10\). The all-orders conclusion depends on the proof, not the census.
