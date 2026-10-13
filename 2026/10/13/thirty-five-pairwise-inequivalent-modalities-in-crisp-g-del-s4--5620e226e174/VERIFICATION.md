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
# Verification

The files `witnesses.json` and `verify.py` form the complete finite certificate for the lower bound.

`verify.py` checks, for each witness model, that both relations are reflexive and transitive, the intuitionistic preorder is locally linear, the modal preorder is forward, backward, and downward confluent, and the atomic valuation is an upset. It then evaluates negation, box, and diamond using the birelational \(\mathsf{GS4^c}\) clauses.

The verifier requires all \(35\) modality fingerprints to be distinct and separately checks all \(inom{35}{2}=595\) unordered pairs. Its expected terminal line is:

`VERIFY_OK modalities=35 models=8 pairs=595`

The certificate proves only pairwise inequivalence of the displayed \(35\) words. It does not enumerate all models, does not prove that \(35\) is the exact number, and does not improve the literature upper bound of \(105\).
