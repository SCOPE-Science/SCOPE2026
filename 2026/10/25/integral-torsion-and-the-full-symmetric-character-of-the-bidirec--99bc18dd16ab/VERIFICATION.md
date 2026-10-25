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

# Reproducibility

Execute `python3 check_integral.py` and `python3 check_character.py` with both files in the same working directory. They require only Python 3 standard-library functions, with no network connection. The former exhaustively constructs all 710 simplices, verifies both differential compositions are zero, and computes exact integer Smith data; the latter computes fourteen signed fixed-simplex traces and the complete irreducible S5 decomposition. Both were executed successfully against the included code.

The rank-one residual test verifies all two-by-two minors vanish and that the gcd of its entries equals two. Therefore the claimed torsion does not depend on rational or finite-field approximations. The character calculation uses ordinary rational Lefschetz theory once the integral homology verifies rational concentration in degree three. No independent audit has been performed; the homotopy type and integral representation lattice are not determined.
