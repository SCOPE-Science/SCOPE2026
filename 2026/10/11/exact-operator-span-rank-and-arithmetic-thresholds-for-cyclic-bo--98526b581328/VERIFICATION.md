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

# Verification and limits

The rank argument reduces each operator-span rank to the number of nonzero self-ambiguity coefficients of a cyclic Weyl–Heisenberg orbit, using the character diagonalization of its Gram matrix. The interval overlaps were enumerated exactly, and roots of unity were counted with divisibility and elementary congruences, including the overlapping two-interval case. Every assertion for unbounded dimension follows from those algebraic arguments rather than experimentation.

Run `python3 verify_boxcar.py` using Python 3's standard library. The script recomputes every cyclic self-ambiguity coefficient as an integer polynomial and checks its vanishing at a primitive root by exact cyclotomic divisibility. This verifies the predicted number of nonzero coefficients for every lag, frequency and rectangular-window length in dimensions \(3\) through \(24\). It checks the odd-order threshold and the power-of-two optimal lengths in the same finite range, and prints additional arithmetic rank profiles. This finite verification cannot prove the all-dimension theorem independently.

The result concerns linear operator-span informational completeness, not an assertion that every rank-deficient POVM fails to retrieve pure vectors up to global phase. The statement covers full (not subsampled) cyclic time-frequency orbits of normalized constant-on-an-interval windows and gives no noise-stability bound or nonrectangular classification. The general ambiguity-rank equivalence and earlier sufficient coprimality results are credited as prior work. Independent audit is not yet performed.
