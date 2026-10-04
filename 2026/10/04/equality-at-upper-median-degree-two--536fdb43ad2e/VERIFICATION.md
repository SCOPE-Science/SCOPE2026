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

The analytic proof establishes the theorem for every finite connected simple graph with upper median degree \(2\). The finite computation is an independent stress test, not an extrapolation argument.

`artifacts/verify.py` uses only the Python standard library. It enumerates every labeled simple graph on two through six vertices, filters connected graphs, computes \(\gamma_2\) by testing vertex subsets directly against the definition, and computes the upper median degree from the sorted degree sequence. It also checks the structural lemma \(\gamma_2(G)=n-1\) against its clique/degree criterion on every connected graph in the enumeration.

Replay command:

`python3 artifacts/verify.py`

Observed output:

`ALL CHECKS PASSED; graph_masks=33866; connected_graphs=27475; structural_checks=27475; m2_graphs=8595; m2_equalities=115; max_order=6`

The analytic proof independently forces every equality graph with \(m(G)=2\) to have order at most six. Therefore the enumeration covers all possible equality orders, but the proof—not the enumeration—establishes that cutoff. The count \(115\) is a labeled count; the theorem concerns five isomorphism types. No claim is made about equality for upper median degrees other than two.
