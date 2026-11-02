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

Run `python3 checker.py` with a standard Python 3 interpreter. The script checks exact rational one-arc and two-arc probabilities on the complete labelled directed-tour supports for orders \(3\) through \(7\) (\(3244\) individual edge-pair moment comparisons), and it checks predicted eigenvalue equations for symmetric and skew fundamental-cycle vectors of the incidence kernel. For orders \(3\) and \(4\), every maximal selected feature set is tested for complementary spanning-tree connectivity and its exact determinant. In order \(4\), all \(384\) positive determinants coincide out of \(792\) possible saturated coordinate sets, under both uniform and the strictly positive asymmetric tour weights \((1,2,3,4,5,9)\). It also checks \(120\) deterministic larger selections in order \(5\).

The universal arbitrary-law, all-order theorem is proved in RESULT.md by the covariance-kernel identification, the complementary-minor identity, and the matrix-tree theorem. Enumeration is a finite consistency test, not a proof for unbounded order. Historical equivalence and complete external proof validation remain open.
