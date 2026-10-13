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

The analytic proof is self-contained in `RESULT.md`. The decisive infinite step is the adjacent-magnitude inequality for \(b_k=|c_k|h_k\); finite computation is not used to infer the universal statement.

`artifacts/verify.py` uses exact rational arithmetic. It checks 124 nested chains with varying refinement factors, including mixed chains not of the form \(s r^k\). For each tested chain it verifies strict positivity, unit weight sum on \([0,1]\), the exact largest-weight formula, polynomial exactness through degree \(2d+1\), alternating Richardson coefficient signs, and strict growth of \(|c_k|h_k\). It also verifies the exact nonnested boundary example \((1,2,5)\), whose midpoint weight is \(-8/63\).

The recorded deterministic output is in `artifacts/verification.txt`. The checks do not test floating-point tableau stability, nonuniform spatial grids, or arbitrary nonnested division sequences.
