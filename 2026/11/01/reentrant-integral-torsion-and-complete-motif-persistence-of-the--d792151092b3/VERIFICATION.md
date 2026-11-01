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

The attached `verify.py` uses the Python standard library only and reads the three attached CSV tables from its own directory. The recorded command `python verify.py` completed with marker `PALEY11_TOURNAPLEX_PERSISTENCE_AND_INTEGRAL_SMITH_OK`.

The checker enumerates all 2047 nonempty subsets of the 11 vertices; identifies 55 cyclic triples among the 165 unordered triples in two ways; checks all 55 affine maps preserve the entire filtration; and checks the signed boundary operator squares to zero. It independently computes both complete field barcodes, verifies all seventeen direct mod-two stage Betti vectors, and performs integer Smith invariant calculations at all stages and degrees. The Smith procedure uses unimodular unit pivots and checks each remaining matrix is zero or rank one by exact two-by-two minor comparisons (including zeros), then reads its sole invariant from the gcd of all remaining entries. Only two nonunit factors occur: one factor two in the third boundary at zero and one factor two in the sixth boundary at twelve. The resulting integral groups are checked against `integral_stages.csv` and against the universal coefficient theorem.

The result is a finite, reproducible calculation and a mathematical deduction from standard Smith-form and persistence-pairing theorems. It does not certify homotopy groups, coefficients beyond the stated two fields for persistence, or a family of larger tournaments. No independent audit has been performed.
