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

## Reproduction and scope
Run the C++17 and Python 3 commands from `RESULT.md` within the directory containing the accompanying source. There are no external data dependencies. The scripts independently reconstruct both graphs from their sixteen labeled coordinate vertices, verify all graph degrees and common-neighbor counts, exhaustively test every possible subset through size five or six as appropriate, and reconstruct the optimum exchange graphs from the enumerated configurations.

## Actual checks
`cpp_output.txt` and `python_output.txt` record successful executions. Both report exactly \(96\) optimum Shrikhande codes and \(16\) six-vertex cycle components, and exactly \(2208\) optimum rook codes, \(28800\) exchange edges, a single component, and eccentricity \(6\) at all \(2208\) states. The checks also compare the Shrikhande optima against the geometric construction, and the Python program verifies their affine automorphism orbit.

## Limits
This is a complete computation on two explicit finite graphs, not a theorem about all graphs with similar parameters. A printed success marker alone is not a proof; the included source, exact finite universes and assertions are necessary for reproduction. An independent scientific audit has not been performed.
