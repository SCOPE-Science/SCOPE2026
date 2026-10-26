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

# Reproduction and boundaries

Run `python clebsch_f3_verifier.py` with Python 3.9 or later and no external dependencies. The checker uses a canonical degree-two representation of \(\mathbb F_9\), independently computes the two families of lines by exhaustively permuting five coordinates, verifies all line equations exactly, and checks all Frobenius images. It independently counts projective points over \(\mathbb F_3\) and \(\mathbb F_9\).

Expected result: `PASS: 15+12 distinct lines, six Frobenius pairs, cubic identities, F3=25, F9=145, Frobenius trace=5, all-extension formula`.

The all-extension formula is a theorem derived from the Picard Frobenius eigenvalues; finite field enumeration for the first two extensions is a consistency check and a finite certificate of line containment/splitting, not a general proof for all finite extensions. The Jacobian smoothness argument, classical 27-line theorem, Picard generation, and Lefschetz trace identity are presented in the accompanying mathematical account. Independent scientific verification has not yet been performed.
