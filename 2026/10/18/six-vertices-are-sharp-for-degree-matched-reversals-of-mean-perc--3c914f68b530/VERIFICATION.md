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

# Verification and scope

Run `python3 verify.py`. The standalone verifier uses only the Python standard library. It exhausts all \(2^{\binom n2}\) labeled edge sets on \(1\le n\le5\), checks connectivity, canonicalizes over all \(n!\) permutations, and computes exact polynomial coefficients by summing the squared component sizes over every open-edge subset. The connected unlabeled counts are \((1,1,2,6,21)\), matching the elementary enumeration. The only degree-matched nonisomorphic connected pairs through five vertices occur for profiles \((1,2,2,2,3)\) and \((2,2,2,3,3)\); both polynomial differences are verified as fixed-sign products.

For the six-vertex pair, the program computes edge-state sums and separately computes pair connectivity by the exact two-arc formula for unicyclic graphs. The two methods agree coefficientwise. The unique interior root follows from a strictly decreasing quadratic, not floating-point root approximation. Its `certificate.json` contains the exact counts and polynomial coefficients.

This is an exact finite proof and reproducibility check for the stated graph class, not a certificate of generic SIR equivalence, infinite graph order, literature exhaustiveness, or independent review.
