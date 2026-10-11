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

Run `python3 verify_cactus.py` in this directory with a standard Python 3 interpreter. The source constructs every graph-product cell, all signed boundary columns, and independent finite-field ranks for the seven specified cactus graphs. All four moduli \(2,3,5,7\) produce the claimed Betti dimensions and `VERIFY_OK`. The extra complete graph is explicitly outside the theorem's domain.

The verifier is a finite consistency test, not an exhaustive check of infinitely many cactus graphs and not an integral Smith-normal-form computation. Torsion-freeness is instead established by the primitive disjoint-support image and splitting in the complete integral long exact sequence. The swap character is established by the signed product action on the explicitly described integral basis and by equivariant splitting over the rationals, not by a sampled trace table. No independent audit has been performed.
