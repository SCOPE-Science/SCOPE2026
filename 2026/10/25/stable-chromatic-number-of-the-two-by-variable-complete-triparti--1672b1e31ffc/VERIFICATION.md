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
# Reproducible checks and limits

Run `python3 verify.py` from the extracted file directory with Python 3 and no third-party packages. `verify_output.txt` contains the deterministic output from the script. It enumerates all \(96\) proper named four-color assignments of \(K_{2,2,2}\) and checks their envy directed cycles. It also enumerates all \(2940\) proper five-color assignments for \(K_{2,3,3}\) and all \(165360\) proper six-color assignments for \(K_{2,4,4}\), for the explicit amplified profiles. The script computes adjacency and preference arcs from definitions and detects directed cycles; no cached classification table is used. It checks the four cases lacking an envy two-cycle directly for a directed triangle.

For the infinite claim, verification relies on the proof's quantified induction and an explicit acyclic orientation. No finite enumeration is presented as an infinite certificate. The accessible foundational arXiv paper supplies the general reachability and subgraph-monotonicity theorems; the seed has a separate internal exhaustive checker and a published triangular-prism implication. Independent audit remains not performed.
