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

# Verification record

The proof applies to all \(m\ge1\) and \(r\ge0\). The embedded script `verify_involution_matching.py` uses only the Python standard library. It starts with an actual transposition involution on the ground vertices of a complete graph, enumerates all unordered graph edges, partitions them into involution orbits, and keeps only those whose unions are matchings. It independently constructs faces by disjoint supports and computes exact reduced simplicial boundary ranks over \(\mathbb F_2\) for fourteen parameter pairs, checking every predicted reduced Betti number. It also checks the reduced Euler characteristic for four larger paired-block cases.

Observed final line when the embedded script was executed:

`MATCHING_INVOLUTION_FIXED_COMPLEX_VERIFIED`

This does not constitute an exhaustive test over unbounded parameters and does not independently verify integral torsion; torsion is obtained by the proven suspension decomposition and published integral homology of \(M_7\). No independent external mathematical audit has been performed.
