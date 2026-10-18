# Scientific review: Clebsch total four-cut and Alexander dual

## Correctness

**PASS.** Both complexes are defined by independent four-vertex sets in the explicit sixteen-vertex graph. Exhaustive enumeration and complete acyclicity checks give the stated critical-cell dimensions, with \(392{,}720\) and \(70{,}368\) directed-cover relations verified. Signed integer gradient-path projection gives \(\partial_7^K=(2)\), \(\partial_8^K=0\), \(\partial_6^B=0\), and \(\partial_7^B=(-2)\). The exact two-torsion, free ranks, vanishing of other groups, connectivity, and shellability obstruction follow from this chain model. Two runnable programs and their executed outputs are included: a complete signed integral Morse checker, and an independently generated raw mod-two boundary-rank computation on the dual. The full homotopy type is not asserted.

## Originality

**PASS, with residual literature risk.** Full-text scientific comparisons included *Total Cut Complexes of Graphs* (arXiv:2209.13503), *Topology of Cut Complexes of Graphs* (arXiv:2304.13675), and *Total cut complexes and their duals* (arXiv:2602.21427). The first classifies different families, the second treats a distinct ordinary-cut condition, and the third gives a torsion example constructed from a disconnected graph rather than the Clebsch graph. Relevant indexed summaries concern the same graph's ordinary independence, three-cut, neighborhood, dominance, and forest complexes; no inspected statement implies the paired total-four-cut calculation. Searches are not a uniqueness proof; unindexed equivalent results remain possible.

## Mathematical value

**PASS.** The connected, triangle-free, strongly regular Clebsch graph is a canonical test object for graph-complex topology. Its total four-cut complex has integral torsion and free homology in a different dimension despite being pure of dimension eleven. The paired Alexander-dual computation locates torsion on both sides, and supplies a concrete boundary to the sphere-wedge patterns in commonly classified graph families. The precise graph and parameter are structurally motivated, and the outcome is not implied by the cited existing classifications.

## Scope of validation

A finite exhaustive integer-chain computation, with every face and incidence checked, is a proof of the stated *finite* homology calculation when combined with the matching and algebraic cancellation arguments. It does not settle higher attaching homotopy classes or any larger graph family. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
