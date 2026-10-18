# Scientific assessment

## Correctness — PASS

The claim is \(\operatorname{sdim}(\operatorname{GP}(25,2))=34\). The vertex-cover reduction for mutually maximally distant pairs is justified by extending geodesics. The exact all-pairs distance table identifies a 175-edge strong resolving graph split into two circulants. Five cliques of the nonneighbors of a fixed outer vertex bound the outer independent number by six, while five disjoint inner five-cycles bound the inner independent number by ten. Both bounds are attained by displayed independent sets, so \(50-(6+10)=34\). Separate breadth-first and Floyd–Warshall programs reconstruct the graph; the former directly checks strong resolution for all 1,225 unordered vertex pairs. The proof is a complete finite classification of this invariant, not a claim about untested orders.

## Originality — PASS (with residual risks)

The closest full text is Kratica–Kovačević-Vujčić–Čangalović (arXiv:1507.00881v1, 2015; journal version, 2017), which proves only the bound \(\operatorname{sdim}(\operatorname{GP}(4k+1,2))\leq5k+5\), and explicitly predicts equality when \(k\ge5\). Their table of exact small cases stops at \(n=19\). The value 34 for \(n=25\), where their prediction gives 35, contradicts rather than restates their proposal. The known vertex-cover reduction is credited. Search of accessible mathematical records and related published metric-invariant work found no stronger theorem or database entry giving this exact value; incompletely indexed subsequent literature remains a risk. No publication-priority or external certification claim is made.

## Value — PASS

This is an exact, proof-certified counterexample to a named, long-standing infinite-family prediction at its second eligible parameter, not an arbitrary numerical computation. The explicit clique partition and five odd cycles explain optimality structurally and identify the precise 34-vertex strong resolving basis; they do not merely corroborate a solver output. This changes the status of the proposed formula while leaving the correct full-family replacement open.

## Limits

The result determines one finite generalized Petersen graph only; no claim is made about all residue-class-one orders. Independent external scientific review has not occurred. Potential equivalence in otherwise inaccessible or unindexed literature is a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
