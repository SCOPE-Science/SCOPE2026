# Self-review

## Correctness

PASS. The proof reduces adjacency to nilpotency of the restriction \((AB)|_{\operatorname{im}A}\). The restriction map from all \(B\) onto \(\operatorname{End}(\operatorname{im}A)\) is explicitly proved surjective, so every nilpotent restriction has the same fiber size. Combining this with the Fine--Herstein count gives exactly \(q^{n^2-r}\) products before deleting zero and a possible loop. The loop correction is exactly the nilpotency indicator because \(A^2\) is nilpotent exactly when \(A\) is nilpotent. Exhaustive checks for \((n,q)=(2,2),(2,3),(3,2)\) agree with every degree profile. Source: the displayed proof and the included exhaustive verifier. Risk: the computation is finite and is not used as evidence for the universal quantifier; the universal step rests on the surjective linear map and the cited nilpotent count.

## Originality

PASS. The dedicated matrix-algebra paper was inspected through its substantive Section 2 and lists vertex, connectivity, diameter, girth, independence, planarity and isomorphism results rather than a general local-degree law. The 2015 regular-graph classification explicitly computes \(\deg(e_{11})\) and bounds \(\deg(e_{11}+e_{22})\), while the 2017 Eulerian classification explicitly computes the rank-one degrees of \(e_{11}\) and \(e_{12}\). Those are special cases of the present formula, not a statement implying the all-rank theorem or the inverse recovery of both rank and nilpotency. Semantic database searches using the graph name, full-matrix notation, rank, nilpotency and the proposed degree shape returned no covering finding. Sources: Nikmehr--Khojasteh, Mahmoodi, and Kuzmina--Maltsev (2015, 2017), as listed in RESULT.md. Risk: an older theorem under different terminology could remain unindexed; this is retained as a residual originality risk rather than treated as negative evidence.

## Value

PASS. Rank and nilpotency are fundamental algebraic strata of a matrix algebra. Recovering both from one intrinsic local graph statistic supplies a structural dictionary between the graph and its matrix algebra, explains earlier ad hoc degree calculations, sharpens a previously used rank-two bound to equality, and gives exact extremal-degree characterizations. This is a natural complete classification of vertex degrees rather than an arbitrary finite slice. Sources: the prior papers show that selected vertex degrees are already useful for global regularity/Eulerian questions, while the present theorem resolves the full local stratification. Risk: the value claim is confined to the full finite-field matrix-algebra family and is not asserted for broader coefficient rings.

## Closest literature and limitations

The closest direct antecedents are Kuzmina--Maltsev's 2015 and 2017 degree calculations for selected matrix units, Mahmoodi's rank-based global study of matrix-algebra nilpotent graphs, and Fine--Herstein's nilpotent-matrix count. The theorem is limited to finite fields. A differently phrased older all-rank local-degree theorem not surfaced by the inspected sources remains a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
