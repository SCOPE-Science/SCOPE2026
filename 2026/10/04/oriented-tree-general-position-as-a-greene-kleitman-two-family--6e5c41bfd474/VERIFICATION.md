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

The mathematical proof has two critical steps. First, in an oriented tree, three selected vertices lie on a common directed geodesic if and only if they form a three-element chain in the reachability poset. The forward direction reads the vertices in path order; the reverse direction uses uniqueness of the underlying tree path, which makes the directed path geodesic. Second, the Greene–Kleitman theorem at \(k=2\) identifies the maximum two-family size with the stated minimum over chain partitions.

The bundled `verify.py` stress-tests these steps without using the proof implementation. It exhaustively generates every labeled tree through six vertices from Prüfer codes and every orientation. For each oriented tree it separately computes: the largest general-position set by direct directed-geodesic tests; the largest subset with no three-element reachability chain; and the minimum chain-partition objective. The verifier requires all three values to agree in every case.

The finite replay is not evidence for the universal quantifier by itself. The universal claim rests on the proof above and the cited classical theorem. No independent audit has been performed.
