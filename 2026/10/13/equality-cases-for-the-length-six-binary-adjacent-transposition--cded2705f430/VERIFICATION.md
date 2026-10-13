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

`artifacts/verify.py` is standalone and uses only the Python standard library. It reconstructs the \(64\) length-six binary words and each closed one-adjacent-transposition error ball directly from the channel definition.

As a separate compatibility route, the script builds each constant-weight token graph and computes shortest-path distances by breadth-first search. For every same-weight pair it requires exact equivalence between disjoint error balls and token-graph distance at least \(3\).

For each Hamming weight \(k\), the script enumerates every subset at the claimed layer optimum and every subset of cardinality one larger. The resulting maximum layer sizes are \((1,2,4,6,4,2,1)\), with maximizing-set counts \((1,6,14,1,14,6,1)\); every one-larger search is empty. Different weights are checked to have disjoint error balls automatically, so the global maximum is \(20\) and every global maximum is a unique Cartesian product of layer maxima.

The script explicitly constructs all \(7056\) such products, rechecks every one with the original error-ball definition, confirms the unique weight-three set, and applies global complement and coordinate reversal to recompute the \(1810\)-orbit partition. It also recomputes a secondary received-word coverage distribution recorded in `artifacts/certificate.json`.

The claim is finite and exact for length \(6\). No timeout, random sampling, heuristic bound, or extrapolation to other lengths is used. The declared order-four action is not asserted to be the full graph automorphism group.
