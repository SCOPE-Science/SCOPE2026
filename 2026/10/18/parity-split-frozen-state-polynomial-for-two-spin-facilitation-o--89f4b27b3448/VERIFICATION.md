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

# Verification of the frozen-state polynomial

Run `python3 verify_frozen_ladder.py` using a standard Python 3 installation. The script has no third-party dependencies. It performs three logically distinct exact-integer checks: (i) enumerates every one of the \(2^{2n}\) binary microscopic configurations for \(3\le n\le9\), directly testing that each vertex has at most one facilitating neighbor, and compares all coefficients against the closed polynomial; (ii) independently enumerates independent sets of \(C_m^{\,2}\) for \(3\le m\le13\); (iii) builds the common-neighbor graph directly and compares it against the two alternative cyclic-square decompositions for \(3\le n\le50\).

Observed complete blocked-configuration totals for \(n=3,4,5,6,7,8,9\) were respectively \(10,25,46,100,211,441,973\). All checked cases passed. An additional symbolic calculation found \(\det(\lambda I-M(z))=\lambda^3-\lambda^2-z\) and \(\operatorname{tr}(M(z)^m)=F_m(z)\) for \(m=3,4,5,6,7,8\), with zero exact differences.

These checks cover finitely many sizes and do not independently certify the infinite-family conclusion. The full proof depends on the explicit neighbor enumeration, permutation-orbit analysis, labeled cyclic-gap counting and Perron–Frobenius theorem, as stated in the mathematical result. Independent external audit has not been performed.
