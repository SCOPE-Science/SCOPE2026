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

The unrestricted result follows from the two residue-class inequalities and the exact offset-deficit obstruction in `RESULT.md`, not from enumeration.

Run `python3 verify.py` in a directory containing this file and `verify.py`. It computes the Apéry residues by Dijkstra's shortest-path algorithm using positive generators, independently of the proof's offset construction, for all integer parameters \(2\le n\le100\). Each computed Frobenius number is compared to \(n^3-2\). It should output `VERIFY_OK parameters=2..100 all_exact_frobenius_checks`.

This finite verification does not establish the infinite theorem or uniqueness in the literature. Independent audit has not been performed.
