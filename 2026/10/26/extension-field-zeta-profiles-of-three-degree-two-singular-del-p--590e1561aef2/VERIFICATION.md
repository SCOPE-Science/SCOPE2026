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

# Reproducibility and limits

From the extracted package directory, run:

- `python3 code/verify_point_counts.py`
- `python3 code/verify_f4_independent.py`

The first checker uses polynomial-basis representations of \(\mathbf F_{2^m}\) for \(1\leq m\leq6\), enumerates every normalized weighted-projective point on each displayed equation, and tests the equation and all four partial derivatives. It asserts the total and smooth-locus counts, derives the trace sequences from \(\#X(\mathbf F_q)=q^2+q+1+qt_m\), and checks the Newton-identity characteristic polynomials in the required ranks. The second checker uses an explicit multiplication table for \(\mathbf F_4\), not the first checker's polynomial-reduction routine, and independently reproduces the three \(\mathbf F_4\) counts.

Recorded output: `ALL_EXHAUSTIVE_CHECKS_PASS` and `INDEPENDENT_F4_CHECK_PASS`. The geometric singularity types and the general point-count and zeta-function formulas are supported by the cited primary literature. The finite computations do not prove those literature theorems, and the formulas are not extrapolated from point counts without the Frobenius trace argument. Only the three named surfaces are covered; no all-types classification or independent external validation is claimed.
