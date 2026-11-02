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

# Reproducibility and verification

The proof calculates **all** Cartier images in the explicit genus-fourteen regular-differential basis, not a sample of them. It reduces the rank to four permanent pivots plus the rank of \(\begin{psmallmatrix}2B&2A+B^2\\-2A&0\end{psmallmatrix}\). The determinant and rank-one conditions establish the classification over the entire algebraic closure. The tamely split six-dimensional \(+1\)-eigenspace has constant Cartier rank two.

The standard-library Python 3 script `verify_symbolic.py` reconstructs the symbolic matrix over \(\mathbb F_5[A,B]\) without hard-coding image generation. Expected output: `SYMBOLIC_CARTIER_AND_PRYM_OK`.

An independently organized script `verify_fields.py` computes directly over \(\mathbb F_5\) and \(\mathbb F_{25}\), checking all \(25\) and \(625\) coefficient pairs, respectively, including the involution quotient ranks. Expected outputs: `GF5_ALL_25_CARTIER_OK` and `GF25_ALL_625_CARTIER_AND_QUOTIENT_OK`.

Both scripts were executed successfully. Their finite-field checks corroborate, but do not prove, the universal algebraic-closure statement. The exact symbolic matrix and its determinant provide the proof. The claim is confined to the displayed family; no independent external audit or validation has been performed.
