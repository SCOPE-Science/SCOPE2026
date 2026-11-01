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

Place `verify.py` and `matching_pairs.csv` in the same directory. Execute:

`python3 verify.py matching_pairs.csv`

The certificate contains 268 distinct pairs of face masks. The verifier independently constructs the 10-vertex graph as three four-cycles with a common hub; enumerates every subset; checks whether it has an independent four-set; checks the complete matching against the 537 admissible faces; finds exactly one unmatched six-vertex face (mask 876); constructs all 2,130 directed cover relations and topologically sorts them. The successful sort is the complete finite acyclicity proof. No pseudorandom choices or external dependencies are involved.

The unrestricted family theorem is not the output of numerical extrapolation. Its non-computational proof shows that every face lies within three petals, that the low-support subcomplex and the attachment interfaces are cones, and that the quotient is a wedge of exactly one three-petal quotient for each triple of petals. Since these are elementary simplicial-CW arguments, no infinite exhaustive computation is needed.

Limitations: this certificate does not address higher robustness thresholds, general square-sequence graphs, or equivariant homotopy types. Independent audit is not performed.
