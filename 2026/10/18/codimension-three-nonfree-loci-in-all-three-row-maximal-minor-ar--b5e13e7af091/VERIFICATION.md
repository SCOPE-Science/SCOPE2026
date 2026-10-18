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
# Reproducibility and proof dependencies

Run `python3 verify.py` with the Python standard library. The executed check confirms for \(n=6,7,8,9,10\) that the stated integer matrices of rank three have exactly ten vanishing maximal minors, all from the first five columns; the other \(\binom n3-10\) maximal minors are nonzero. It independently checks a simpler six-column witness with final column \((0,0,1)^T\). The computation also checks \(16+3(n-5)=3n+1\), using the number sixteen from the cited five-column theorem.

For the all-\(n\) claim, the essential arguments are: (i) irreducibility and codimension three of the five-column rank-deficiency variety; (ii) nonemptiness of the complement of finitely many proper determinant hypersurfaces on that variety; (iii) unit localization of all mixed maximal minors; (iv) stability and reflection of local freeness under addition of smooth coordinates; and (v) Zariski-closedness of the nonfree locus. These are proved in `RESULT.md` and are not replaced by finite experiments.

The numerical local generator count sixteen at a rank-two five-column matrix comes from Theorem B(3) of the cited 2026 paper. Its computer algebra calculation is a source premise and has not been independently repeated. No external independent audit has been performed.
