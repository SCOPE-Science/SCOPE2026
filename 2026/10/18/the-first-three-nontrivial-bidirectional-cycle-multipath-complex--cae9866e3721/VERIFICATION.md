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

# Verification of finite homotopy classification

Run `python3 verify_bidirectional_multipaths.py`. The program enumerates every subset of the directed arcs for each of the three stated graph orders, rejects all faces with excessive in/out degree or any directed cycle, constructs explicit acyclic discrete-Morse matchings, and checks complete directed Hasse graphs using topological sorting. Its expected augmented counts are `33, 81, 197`, with matching-pair counts `14, 39, 97` and directed Hasse incidence counts `64, 200, 588`. It checks every top-dimensional face in the last two cases and verifies the two disjoint tetrahedral sphere boundaries plus all four bridges in the first.

For the largest case it checks an integer 2-cocycle on every oriented three-simplex, checks that its reduction is not in the mod-two degree-one coboundary image (whose rank is 37), and checks that its Alexander–Whitney cup square is zero on every four-simplex. These statements suffice to eliminate the two integral Hopf attaching coefficients because the CW model has one degree-two generator and free degree-four cohomology of rank two.

The reproducibility target is the program's final marker `VERIFY_OK: exact discrete Morse, top-cycle and Hopf-cup certificates`. These are exhaustive finite certificates, not a proof of the wedge conjecture at unexamined graph lengths. The homotopy-theoretic implications of the certificates are proved in `RESULT.md`.

Self-review: passed. Independent audit: not yet performed.
