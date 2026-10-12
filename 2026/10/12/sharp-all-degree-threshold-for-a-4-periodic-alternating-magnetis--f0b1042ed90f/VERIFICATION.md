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

The proof is analytic and does not depend on a finite search. The accompanying `verify.py` provides a reproducibility check of the key identities against the source's three-variable 4-periodic equations.

It performs exact rational checks for every integer \(2\le k\le100\) that at \(\theta=2/(k-1)\), the root \(v=1\) has vanishing first and second derivatives and third derivative \(k(k+1)\). It then solves the exact hyperbolic branch numerically for representative degrees and parameters, substitutes both reciprocal roots into all three source equations with \(u=1\), \(w=v\), and checks the stated onset coefficient at small positive parameter increments.

These finite tests are corroborative. The infinite statement for every \(k\ge2\) rests on the symbolic reduction and the proof that \(s\coth s\) is strictly increasing for \(s>0\). No exhaustive computation, timeout, or numerical root count is used as proof.
