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

# Verification of the local image theorem

Run `python3 verify.py` using Python 3's standard library. The script independently enumerates all values of \(x^4+y^6\) modulo \(2^n\) for every \(1\le n\le16\), calculates the residues obtained by reducing each of the seven predicted two-adic cosets, and asserts equality of the **complete** sets at each modulus. The final printed word is `VERIFIED` only if all tests succeed. The exact cardinality vector is

\[
(2,3,3,5,10,18,36,68,136,270,538,1074,2148,4295,8587,17173).
\]

The verifier also checks that the rational sum of Haar measures is exactly \(1073/4095\) using integer fractions; no floating point is involved. The proof in RESULT.md separately establishes equality of the two-adic sets for every valuation and gives the limiting measure. Neither a successful finite run nor a tool log constitutes an infinite proof. It does not establish historical priority or independent certification.
