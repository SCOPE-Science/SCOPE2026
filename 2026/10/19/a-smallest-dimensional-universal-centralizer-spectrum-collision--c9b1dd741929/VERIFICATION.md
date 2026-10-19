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

# Verification evidence and limits

Run `python verify.py` with `verify.py` and `profile.tsv` in the same directory. There are no third-party dependencies. The complete standard output from a successful run is `verification_output.txt` and ends in `VERIFY_OK`.

The program builds both adjacency lists from the seven explicit edges, tests connectedness, recomputes all 64 induced-support profiles, compares their 27 populated bins to the separate TSV certificate, and verifies unequal triangle-incidence multisets. It independently computes joint-centralizer counts from the induced-component formula for multiple field-size/tuple-length pairs and compares them to direct Gaussian elimination on actual bracket matrices over the prime fields of orders 2 and 3 (tuple lengths one and two). The direct matrix checks are finite spot tests rather than all-field proofs.

To establish the finite cutoff, the program exhaustively visits every labeled simple graph on one through five vertices and every six-vertex graph with five or six edges; it tests connectivity, canonicalizes each graph by every vertex permutation, and compares exact coefficient signatures of the one-tuple rank polynomial. Found isomorphism-class counts are 1, 1, 2, 6, and 21 through five vertices; at six vertices they are 6 (five edges) and 13 (six edges), all having distinct signatures. Each enumeration loop iterates over **every** graph in the specified finite range, rather than sampling. The one-vertex case is handled as a unique boundary.

The proof of equality for all finite fields and all positive tuple lengths is the algebraic product identity indexed by the 27 support-profile bins; no finite computation is used as an extrapolation theorem. The nonisomorphism conclusion in odd characteristic invokes the stated published graph-rigidity theorem. No independent external audit was performed.
