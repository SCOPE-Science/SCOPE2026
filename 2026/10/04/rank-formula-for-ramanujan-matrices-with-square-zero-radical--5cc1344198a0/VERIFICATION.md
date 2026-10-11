---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

In a local nonfield with square-zero maximal ideal, unit orbits in the nonzero radical are exactly projective directions over the residue field. The source entry formula then gives identical columns for all such directions, so rank is at most three. The unit column, one projective-direction column and the zero column have determinant minus h times q squared after compression and are independent, so local rank is exactly three. A field factor has the displayed two-by-two full-rank matrix. The source direct-product identity makes the global matrix a Kronecker product, so ranks multiply. A fresh symbolic calculation reproduced the determinant and the packaged exact verifier independently checks fifteen local parameter cells and four tensor products.

## originality

PASS

The primary paper gives the entry formula for the generalized Ramanujan matrix, proves the direct-product Kronecker factorization, and explicitly asks what can be said about its rank. It does not answer the rank question for square-zero radicals. The audited theorem uses the square-zero local orbit structure to collapse all projective-direction columns and obtains a genuinely new exact local rank three, then multiplies those local ranks across factors. No Resultary predecessor with an equivalent square-zero formula was located.

## value

PASS

The theorem answers the source paper's explicit rank question on the first broad non-Frobenius layer where singularity alone gives no rank information. The independence from radical embedding dimension is a structural phenomenon and the factorwise formula is reusable for arbitrary products of square-zero local rings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
