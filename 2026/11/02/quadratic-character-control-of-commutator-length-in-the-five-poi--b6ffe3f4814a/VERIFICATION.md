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

# Reproduction and limits

Run `python3 verify.py` using Python 3 and the standard library. The script reimplements the binary quandle multiplication in the cyclic group-ring basis; the symbolic proof uses instead a diagonalizing nilpotent parameter. The script checks both coordinate systems agree, then exhaustively computes the image of every bracket in characteristic five by ranging over the 625 effective first inputs and computing each associated linear-image subspace.

A successful run prints `VERIFY_OK`, `F5_single_bracket_outputs = 585`, `F5_length_two_outputs = 40`, and `F25_nonsquare_discriminant_outputs = 7200`. The \(\mathbb F_{25}\) count is made directly using an explicit quadratic extension, counting nonsquare discriminants across all \((b,c,d)\) with \(b\ne0\). The latter is a verification of the counting step, not exhaustive enumeration of every binary bracket in that extension field.

The complete mathematical proof is in `RESULT.md`; it separately proves the normal form, the discriminant's necessity and sufficiency, the width bound, and the general formula. The finite computations cannot establish historical priority or independently certify the all-field theorem. Independent mathematical audit has not been performed.
