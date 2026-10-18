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

# Verification and limitations

The construction is proved for every integer \(d\ge1\) in `RESULT.md` by an exact quotient-monotonicity argument, polynomial identity, Vandermonde determinant, and the standard top-Chern/Euler zero theorem. No finite computation replaces an infinite-dimensional proof.

Run `python3 check.py` to test all permutations at dimensions \(1\) through \(5\). The program checks the radial inverse and positivity, exact coefficient identities to floating tolerance, and the squared Vandermonde determinant. It prints `FINITE_CHECKS_OK` on success. The checker uses only the Python standard library and is a supporting consistency test, not an exhaustive verification of all dimensions.

The source construction uses smooth functions supported in \([-1/2,1]\) and \([0,1]\); every resulting window is supported in \([-1/2,1]^d\). Boundary and denominator issues are ruled out analytically. The universal bound requires transverse zeros. No independent verification has been performed.
