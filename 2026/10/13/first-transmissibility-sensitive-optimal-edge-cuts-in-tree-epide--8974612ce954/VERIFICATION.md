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

# Reproducibility and boundaries

Run `python3 check_edge_switch.py` (standard library only). The exact checker enumerates every labeled Prüfer tree of orders 2 through 8, canonicalizes by recursive tree-center codes, computes all single-edge outbreak-reduction polynomials both by cross-cut vertex pairs and by endpoint-distance convolution, and certifies polynomial domination by nonnegative integer coefficients in the basis \(p^j(1-p)^{d-j}\).

The checker asserts unlabeled counts \(1,1,2,3,6,11,23\) and exactly two failures of universal polynomial-dominance certificates at order 8, then verifies explicitly that both are genuine switchers with thresholds \(1/2\) and \((\sqrt5-1)/2\). The named witness edge polynomials are recomputed rather than read from a log. The mathematical justification for exhaustive scope is the Prüfer bijection together with the complete unrooted-tree canonical code.

Checks establish the result for finite trees up to eight vertices, not larger trees, arbitrary graphs, correlated transmissions, or nonuniform seeds. Finite parameter-grid tests are not used to infer universal polynomial inequalities. This is a proof plus executable finite-exhaustion certificate, not an independent audit.
