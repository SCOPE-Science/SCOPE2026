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

# Verification of the unicyclic signed-line theorem

Run `python verify_unicyclic.py` with Python 3 (standard library only). Successful output is

`VERIFY_OK exhaustive_unicyclic_graphs_n3_to6=3898 signed_switching_checks=262 sampled_n7_to12=270`

The program computes the degree/cycle quantities by leaf pruning, enumerates every labelled unicyclic graph on three through six vertices, and exhaustively enumerates their edge orientations. It separately constructs the signed line graph from incidence signs, then enumerates its switchings with one switch fixed to avoid global duplication in the 262 indicated test cases. It checks an additional deterministic sample of 270 labelled unicyclic graphs with orders seven to twelve.

The finite verification does **not** prove the all-parameter theorem. The proof is the parity obstruction, sharp local product bound, construction, and equality rigidity in `RESULT.md`. The full mathematical literature may contain an unlocated equivalent result. There is no independent expert or external formal verification.
