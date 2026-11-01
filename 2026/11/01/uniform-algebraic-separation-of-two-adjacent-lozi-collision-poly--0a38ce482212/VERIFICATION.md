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
# Verification of the resultant certificate

The file `verify_lozi.py` reproduces the two collision polynomials directly from the signed affine branch matrices, checks exact integer divisibility by \(a-b-1\), and constructs their Sylvester resultant exactly with SymPy. It confirms degree 30, values \(R(0)=-5\) and \(R(1)=-13\), all 31 positive coefficients in the expansion of \(-R(b)\) in \(b^k(1-b)^{30-k}\), and the exact lower bound \(5252318/6322725\). It also checks the exact rational minimizer among the 31 normalized coefficients.

**Observed execution:** the program completed normally and printed its four `VERIFIED` summaries. Only polynomial identities and exact integer/rational comparisons constitute the certificate. The script does not enumerate all dynamical orbits, establish admissibility throughout the strip, or prove the absence of unpublished equivalent theorems. The no-eigenvalue-one cone argument and the algebraic implication from nonzero resultant to no common complex root are justified in `RESULT.md`.
