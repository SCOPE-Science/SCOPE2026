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

The infinite theorem is proved from Mirabi's tree-closure and dividing criterion. The accompanying `verification.py` is an independent finite regression check of the combinatorial identities used by that proof.

A finite tree plan is encoded by a rooted labeled tree together with a \(0/1\) label on each nonroot node, where \(1\) represents an infinity-node. The checker exhausts all parent arrays with parent index smaller than child index and all infinity-label assignments through seven nodes, giving 50,363 plans.

For each plan it verifies:

- the recursively defined counting polynomial agrees, at several integer inputs, with \(\sum_\sigma x^{I(\Gamma,\sigma)}\);
- for every comparable pair of nodes, the local degree is the difference of infinity-node counts;
- the recursive rank obtained by allowing one dividing step at any newly absorbed infinity-node equals that local degree;
- the polynomial degree equals the maximum node rank and its leading coefficient counts maximal-rank node types;
- the rank-weighted finite strata satisfy the first- and second-moment identities obtained from differentiating the polynomial.

The script performs 2,399,626 assertions and prints:

`VERIFY_OK`

This finite checker does not verify compactness, simplicity theory, or Mirabi's dividing theorem; those are sourced mathematical inputs to the proof.
