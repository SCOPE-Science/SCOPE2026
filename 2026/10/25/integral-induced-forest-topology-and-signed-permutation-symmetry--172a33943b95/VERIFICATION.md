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
# Reproduction of the finite certificate

Execute `python3 verify_clebsch.py` with Python 3.8+; no external packages, network connection or input files are needed. The deterministic output has one canonical JSON object and a final `VERIFY_OK` line; compare it byte-for-byte with `verification_output.txt`.

The checker regenerates all graph edges and verifies parameters \((16,5,0,2)\). It enumerates all 65,536 subsets with two separate acyclicity predicates, verifies the entire simplicial face vector, constructs the pivot matching on valid faces, and topologically sorts its directed full Hasse diagram. It computes all signed gradient-path projections and the exact integral critical-cell boundary matrix, checks an explicit maximal minor is unimodular, and independently computes every original simplicial mod-two boundary rank. Finally it enumerates all 1,920 graph automorphisms (five connection-vector permutations and translations), verifies each preserves adjacency, calculates signed Lefschetz characters and checks each against the proposed sign-twisted augmentation character.

The finite Morse reduction proves the integral wedge homotopy type using standard CW attachment-degree theory. The rational representation identification follows from equality of all group characters. This is a deterministic computation for one specified finite graph, not a machine proof of novelty or any infinite family. No independent external audit is represented by this file.
