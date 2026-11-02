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

# Verification and reproducibility

The mathematical proof in RESULT.md is the primary certificate. For reproducibility, execute \(\texttt{python3 verify_components.py}\) with Python 3 and only its standard library. It enumerates every partial set partition of six coordinate labels, filters blocks shorter than two and the forbidden full-support singleton block, independently tabulates all nine shapes, and returns coefficients \(15,45,90,51\) for descending powers of \(d\). It checks \(5451\) components at \(d=6\), and exact arithmetic Vandermonde determinants of orders one through three. In the recorded execution the program ended in \(\texttt{VERIFY_OK}\).

Finite computations do not establish the infinite theorem. The unbounded steps are proved symbolically by the moment/Vandermonde equivalence, irreducibility of Fermat cones of at least three coordinates, a projective-bundle dimension count, and injective recovery of a generic partition and the size-two root choices. The analysis proves reduced support and irreducible components, not Hilbert-Samuel or generic multiplicities of the full incidence scheme.
