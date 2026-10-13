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

# Verification of the seven-cell flat-band counterexamples

Run `python verify.py` beside the bundled `atlas_n6.graph6`, after installing the dependencies in `requirements.txt`. The independent mathematical identities to examine are the two explicit adjacency multiplication statements and the two selector orthogonality equations stated in `RESULT.md`. The exact checker asserts these equations as polynomial divisibilities for both nonconstant minimal polynomials, checks both motifs are connected and both selectors nonzero, verifies the discriminants \(17\) and \(316\), irreducibility and coprimality, then proves that neither minimal polynomial divides the characteristic polynomial of any of the \(156\) six-vertex simple graph atlas representatives.

The bundled `atlas_n6.graph6` is a frozen complete Graph Atlas enumeration that includes disconnected graphs. The checker compares all its entries to `networkx.graph_atlas_g`, verifies they are pairwise distinct, and uses exact SymPy integer/rational arithmetic for each factor test. This finite census is exhaustive for the six-vertex obstruction, and no other finite check or floating-point plot is used as an infinite-graph proof: the intercell cancellation is a direct algebraic identity for every translate and every Bloch phase.

Expected successful output:

```
VERIFIED: two connected seven-cell witnesses; five distinct real flat-band values;
VERIFIED: no six-vertex simple graph in all 156 classes has either minimal polynomial.
```

Limitations: this verifier is for the stated two seven-cell graphs and every simple six-vertex adjacency motif, not arbitrary weighted or potential-bearing periodic operators. All published literature remains subject to a possible weakly indexed equivalent construction. Independent validation has not been performed.
