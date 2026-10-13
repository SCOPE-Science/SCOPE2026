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
# Computational verification

Run `python3 verify.py` using Python 3; only the standard library is required. The verifier independently generates all evaluation tuples, computes coordinate term functions and their pointwise Lie brackets, and enlarges a row-reduced vector-space basis until closure. It does not assume the dimension theorem in its basis generation. The expected formula is evaluated only after the closure process.

The seven completed comparisons are \((p,s,n,\dim)=(2,1,1,1),(2,1,2,5),(2,2,2,8),(2,3,2,11),(2,2,3,31),(3,1,2,10),(3,2,2,18)\). The verifier also applies \(D^p-D\) to the top Jordan vector, checking at each of four consecutive lengths in characteristics two and three that its \(s\)-th power vanishes in length \(s\) and does not vanish in length \(s+1\).

Observed terminal status: `DIMENSION_CHECKS=7 IDENTITY_CHECKS=8 VERIFY_OK`.

The calculations cover only the displayed prime fields, sizes, and ranks. For all prime powers and unbounded Jordan lengths, correctness is established by the symbolic kernel, Chinese-remainder, and Jordan-polynomial arguments in `RESULT.md`. The methods do not constitute independent external validation.
