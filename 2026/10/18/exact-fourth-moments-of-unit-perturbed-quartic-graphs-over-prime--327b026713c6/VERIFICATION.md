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

# Verification record

The standalone exact-integer program `artifacts/verify.py` was run using a local Python interpreter. It derives each ordered two-sum fiber directly from polynomial evaluations modulo the relevant prime square and sums its squared multiplicities. For primes \(5,7,11,13,17\) it checks all \(c\in\{1,2,1+p,2+p\}\) against the displayed closed formula, a total of 20 direct cases and 518,996 ordered pairs. The separate residue-geometry enumeration checks the union, multiple intersection, both plane–quadric conics, triple intersection, and the lifting formula at nine primes through \(31\), covering 328,460 residue triples. It additionally compares the unperturbed quartic at \(p=5\) and verifies the quadratic-residue class reversal for five primes.

The actual execution result is embedded as `artifacts/verification_output.txt` and records:

```
PASS direct_fibers=518996 residue_points=328460 cases=20 moduli=5 geometry_primes=9 pure_comparison=1 phase_split=5
```

The infinite-prime proof is in `RESULT.md`, not in the finite enumeration; neither the checker nor this verification record asserts independent audit. The remaining scope limits concern nonunit perturbations, higher ring exponents, sharp unrestricted extension inequalities, and possible older unindexed equivalent computations.
