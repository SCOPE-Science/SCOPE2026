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

The proof is symbolic and applies to every connected loopless rank-two matroid. The executable check is supplementary.

`verify.py` enumerates every integer partition \((h_1,\ldots,h_s)\) of every \(n\le24\) with \(s\ge3\). For each partition it computes the closed formula with high-precision decimal arithmetic. Independently, it treats radius feasibility as the interval problem
\[
h_jr\sqrt{\frac{n-1}{n}}\le t_j\le 1-r\sqrt{\frac{h_j(n-h_j)}{n}},\qquad \sum_j t_j=2,
\]
and binary-searches for the largest feasible \(r\). The numerical optimum must agree with the closed formula to high precision, and a class-total vector is explicitly constructed at the claimed optimum.

The finite enumeration is not evidence for the universal quantifier by itself. Universality comes from the interval proof in `RESULT.md`; the script guards algebraic normalization, boundary cases, and implementation errors for a broad finite range.
