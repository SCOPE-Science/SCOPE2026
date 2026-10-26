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

Run `python verify.py` with Python 3.10+ and SymPy installed. No third-party datasets or external source files are required. The program directly enumerates all \(7462\) two-dimensional subspaces of \(\mathbb F_9^4\), checks the \(112\) Hermitian lines and every line intersection, and verifies an integral \(22\)-line geometric lattice basis of determinant \(-9\). For determinant-square and determinant-nonsquare models it reconstructs twisted Frobenius, counts invariant lines and touching conjugate pairs, counts rational points, and computes **saturated** integral Frobenius-fixed lattices and their Smith normal forms. A column Hermite-normal-form calculation verifies that rational line classes and conjugate-line orbit sums generate the full primitive invariant lattice with index \(1\). It separately verifies the second diagonal representative in the square class.

Exact algebraic inputs are nondegenerate quadratic-form classification in dimension four over \(\mathbb F_3\), the Hermitian incidence theorem, the established geometric Néron–Severi line-basis identification, and the vanishing of the Brauer group of a finite field. The enumerations do not, by themselves, certify the external geometric theorem or independence of the result from all mathematical literature. Only self-review has been performed.
