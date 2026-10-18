---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each N>=3 a tensor-bosonic expansion of one photon per spatial input yields P_U=||sum_{sigma} a_sigma P_sigma V||^2, with determinant sum of alternating a_sigma equal det U!=0. For rank N independent internal labels make all orbit tensors independent. For rank N-1, expand the unique dependence phi_N=sum_{i in T}c_i phi_i into linearly independent repeated-label sectors: zero probability forces a_{sigma(i N)}=-a_sigma for every i in T. If |T|>=2 these transpositions force six alternating products in a nonzero 3x3 submatrix of the unitary, contradicting r_x=-r_y, r_y=-r_z, r_x=-r_z for ratios of two columns. If |T|=1, a balanced two-port HOM beamsplitter kills full coincidence. For full-support T, Gram J has exactly sign-representation kernel; projection and van der Waerden permanent inequality yield P_U>=lambda_*(J)[N!/N^N-1/N!]>0. Independent exact tensor/Gram/HOM tests check small N but the all-N statement is proved by the algebra.

## originality

PASS

Shchesnovich 1410.1506 proves the rank-two three-photon nonzero case and states a broader many-photon conjecture, while its matrix formalism provides the setting, not an all-N codimension-one proof. The 1712.03191 generating-function framework and Crespi restricted-Sylvester suppression laws do not yield this all-U positivity and positive spectral gap. Search of published Resultary records found no implication-equivalent theorem; result is best-of-knowledge original within stated product-input domain.

## value

PASS

The first failure of full linear independence in N photon labels is a natural threshold for perfect destructive interference. Exact all-unitary exclusion and a positive internal-Gram-dependent gap answer a motivating multiphoton question in a full infinite family, stronger than isolated interferometer examples, without claiming the broader conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
