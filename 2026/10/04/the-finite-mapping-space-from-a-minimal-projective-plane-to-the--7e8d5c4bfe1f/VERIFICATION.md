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

The standalone `verify.py` reconstructs the 13-point source poset \(P=\mathbb{P}^2_2\) from the cover data stored in `beat_certificate.json` and reconstructs the four-point target circle \(C\) as two incomparable minima below two incomparable maxima.

It recursively enumerates all order-preserving maps along a fixed linear extension of the source and obtains exactly \(868\) maps. It then constructs the complete pointwise order on those maps and verifies that its undirected comparability graph has a single component.

The verifier replays every one of the \(864\) certificate entries. Before each deletion it recomputes the strict upper and lower sets inside the current induced subposet and checks that the recorded witness is respectively the least strict upper point or greatest strict lower point. The replay totals \(196\) up-beat and \(668\) down-beat deletions.

After replay, the only remaining map indices are the four constant maps. Their inherited order is checked entry-by-entry against the target order, and the terminal four-point poset is checked to have no beat point. Thus the certificate establishes a strong-deformation reduction to a core isomorphic to \(C\).

The exact replay output is stored in `verification_output.txt`. The computation is exhaustive for this finite source and target. General theorems identifying the compact-open specialization order with pointwise order and beat-point deletion with strong deformation retraction are cited rather than rederived by the script.
