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

Run `python3 verify.py` with a standard Python 3 interpreter. The verifier has no third-party dependencies and contains the exact 16-triangle \(242\) seed used in the proof.

It checks the surface conditions, exhaustive legal \(2\)-\(2\) flip closure, exact six-class canonicalization, the published valence signatures and \(323\) distinction, every directed flip-multiplicity entry, and the simple graph's connectivity, nine edges, diameter \(3\), unique leaf \(404\), and self-flips only at \(1133\) and \(161\).

Expected final line:
`VERIFY_OK classes=6 flip_counts=242:7,323-A:6,404:4,161:8,1133:5,323-B:6 underlying_edges=9 diameter=3 leaf=404 self_flip_types=1133,161`

The verification is finite and exhaustive for vertex-preserving \(2\)-\(2\) flips on these six isomorphism types. It does not test flip paths that add vertices or geometric immersion properties.
