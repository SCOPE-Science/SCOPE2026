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

# Reproducibility and verification

Run `python3 verify_isolated.py` with Python 3 (standard library only). It computes 21 Apéry sets by Dijkstra's shortest-path algorithm, separately derives the proposed representatives, checks each representative and the isolated-gap count, and directly tests representability for the first three eligible parameters. It outputs `PASS` only after all assertions succeed.

The symbolic proof uses three exact denomination identities and a full residue-by-residue height argument. No finite computation is used to infer the unrestricted \(n\equiv3\pmod4\) theorem. The checker establishes agreement for a specified finite range, not an infinite computational certificate. Independent scientific audit has not been conducted.
