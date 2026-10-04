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
The proof is symbolic and applies to every integer \(m\ge3\) and every commutative coefficient ring. The replay program is an independent finite consistency check: it constructs the graph from the definition, enumerates allowed four-paths, forms forbidden boundary constraints directly from the alternating path boundary, and checks the predicted nullities over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) for every width from \(3\) through \(24\).

Run:

`python3 verify_cyclic_path_chain.py`

Expected terminal line:

`CYCLIC_PATH_CHAIN_VERIFY_OK`

The finite-width replay is not used to infer the universal theorem; it only checks the implementation and the five-family boundary accounting against many instances. No claim is made here about \(PH_4(G_m;R)\) or about widths below \(3\).
