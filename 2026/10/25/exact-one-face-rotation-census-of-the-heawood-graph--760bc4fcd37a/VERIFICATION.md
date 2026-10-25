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

The standalone program at `verification/heawood_rotation_census.py` was run successfully using only the Python standard library. Its SHA-256 is `b7a1469d218241047dcb1cb270df5ab822fd532fa5a2c98f404f9dc877849b91`.

Actual checks completed:
- The incidence construction has \(14\) vertices, \(21\) edges, and degree \(3\) at every vertex.
- The explicit collineations and point-line dualities give \(336\) distinct adjacency-preserving automorphisms.
- All \(16{,}384\) local cyclic-order assignments were enumerated.
- Two independent face-tracing implementations agree on the complete distribution: \(4{,}480\) systems have one face, \(10{,}880\) have three, \(1{,}008\) have five, and \(16\) have seven.
- The \(4{,}480\) one-face systems form \(16\) automorphism orbits: \(12\) of size \(336\) and \(4\) of size \(112\).
- Burnside's lemma independently returns \(16\) orbits: one automorphism fixes \(4{,}480\) systems, \(56\) fix \(16\) each, and \(279\) fix none.
- Global mirror reversal pairs the \(16\) orbits into \(8\) classes: six of combined size \(672\) and two of combined size \(224\).
- Euler's formula gives genus \(4\) for every one-face embedding.

Scope limits: the enumeration is exhaustive only for the Heawood graph's rotation systems. It does not certify any statement for other graphs or any metric/geodesic property beyond the standard strip-to-cut-locus realization implication. The search did not establish global novelty against all possibly unindexed sources.
