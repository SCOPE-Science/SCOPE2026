# Independent audit — 2026-10-01

## Final claim

Every connected bipartite nonpath graph on \(n\) vertices has standard expected-range deficit at least \(1/(60\sqrt n)\), this order is sharp on the one-fork tree with the stated exact reflection-principle formula, and every connected nonpath graph has the stated explicit lazy deficit, with the stronger \(2/(405\sqrt n)\) bound for nonpath trees.

## Correctness — PASS

The audited proof correctly retains the quantitative surplus in Zhu's comparison. Zhu's Proposition 3.3 gives the deficit term \(-\Delta J_d\); Lemma 3.4 gives the \(p=1/2\) parity-error bound, and the lazy cyclic argument gives the explicit \(p=2/3\) margin used here. The elementary lower bound on \(J_d\), the branching-triangle surplus, and the exact conditioned cycle surplus then give the stated universal standard gap. The one-fork coupling was independently replayed exactly for orders 4 through 11 and matched \(\frac12\Pr(M_{n-3}=1)\) in every case. The cycle-surplus formula was independently evaluated and its minimum over the replayed range occurs at the stated \(2/5\) endpoint. The lazy tree estimate follows from zero-edge contraction and the event that three fixed branch edges are nonzero. These finite checks corroborate, but do not replace, the analytic proof.

Checked sources:
- Y. Zhu, Paths maximize the expected range of graph-indexed random walks, arXiv:2609.19728v1 (2026), full primary PDF relevant sections inspected.
- Y. Wu, Z. Xu, Y. Zhu, Average Range of Lipschitz Functions on Trees, Moscow J. Combin. Number Theory 6 (2016), indexed primary PDF/abstract inspected; direct full-PDF retrieval was unavailable during this run.
- Published finding dated 2026-09-18: Unique BHM maximizers and a quantitative standard-to-lazy gap transfer, complete RESULT inspected.
- Independent exact replay of the fork identity for orders 4 through 11 and of the cycle rank-surplus formula for cycle-class sizes 3 through 9.

Residual risks:
- The proof depends on Zhu's published comparison/rank-surplus lemmas as stated; no independent reproving of those full lemmas was attempted.

## Originality — PASS

Best-of-knowledge originality passes for the dimension-explicit stability scale and sharp one-fork asymptotics. Zhu proves path extremality and supplies the comparison machinery, but does not state a graph-independent \(n^{-1/2}\) stability theorem or the fork identity. The earlier 2026-09-18 published finding gives equality classification and a standard-to-lazy transfer with factor \(p_G\), which is exponentially small for trees and therefore does not imply the present polynomial stability bounds.

### Equivalent formulations

Searches:
- Resultary semantic search: quantitative stability path expected range graph-indexed random walks fork tree
- Published 2026-09-18 BHM equality/gap-transfer finding
- Wu--Xu--Zhu 2016 tree paper

Evidence:
- The only exact quantitative-stability published-record hit is the assigned finding.
- The earlier finding's transfer is \(h(P_n)-h(G)\ge p_G(\widehat h(P_n)-\widehat h(G))\) with \(p_G=(2/3)^{n-1}\) on trees.
- The 2016 source establishes tree extremality/equality, not an inspected polynomial deficit formula.

Reasoning: Equivalent formulations include a uniform deficit from path extremality, a near-extremizer stability theorem, and the exact fork perturbation gap; no prior equivalent polynomial-scale statement was located.

### Broader coverage

Searches:
- Zhu arXiv:2609.19728 full proof
- Published 2026-09-18 equality/gap-transfer theorem

Evidence:
- Zhu's theorem is broader in graph class for qualitative extremality but weaker on quantitative separation.
- The earlier transfer theorem is quantitative but loses an exponentially small factor on trees.

Reasoning: Neither broader result dominates the claimed polynomial scale and matching fork order.

### Exact database or table

Searches:
- Resultary semantic search above
- Wu--Xu--Zhu finite/tree literature
- Bok--Nešetřil unicyclic literature

Evidence:
- No prior exact table or formula for the one-fork deficit or universal stability constant was located.
- The package replay agrees with the exact formula on bounded orders but is not originality evidence.

Reasoning: This is an infinite stability theorem, so finite tables do not imply it.

### Claim versus prior implication

Searches:
- Zhu Proposition 3.3 and Lemmas 3.4/5.4
- Published 2026-09-18 gap transfer

Evidence:
- Zhu's displayed inequalities contain ingredients from which one can extract strictness, but the sharp-order uniform stability theorem additionally requires retaining a constant rank surplus, lower-bounding \(J_d\), treating cycles quantitatively, and constructing a matching fork family.
- The earlier gap transfer cannot yield the polynomial tree bound because its factor is exponentially small.

Reasoning: The prior statements do not mechanically imply the combined sharp-scale final claim as a stated corollary.

### Source inspections

- **Paths maximize the expected range of graph-indexed random walks** — Supplies prior extremal theorem and quantitative ingredients, but not the audited sharp stability theorem. Material read: Full primary PDF relevant to Proposition 3.3, the \(p=1/2\) error estimate, cyclic rank surplus, and the lazy \(p=2/3\) estimate. Method: Primary full-text inspection with rendered PDF-page checks. Evidence: The source states the comparison formula and explicit error/rank bounds used by the audited extraction.
- **Average Range of Lipschitz Functions on Trees** — Tree equality coverage is prior art; quantitative polynomial-deficit coverage remains a residual access risk, not asserted absent from the whole paper. Material read: Indexed primary PDF first-page/abstract material; direct end-to-end PDF retrieval was unavailable in this run. Method: Primary-source indexed-text inspection plus comparison with the complete 2026-09-18 published finding that quotes its equality corollaries. Evidence: Accessible material confirms the paper proves both tree extremal conjectures; the earlier published finding identifies Corollaries 2.6 and 2.12 as the equality statements.
- **Unique BHM maximizers and a quantitative standard-to-lazy gap transfer** — Does not cover the present polynomial stability scale. Material read: Complete RESULT.md. Method: Published-result full-text inspection. Evidence: Its quantitative transfer has factor \(p_G=(2/3)^{n-1}\) for trees and explicitly disclaims a sharp graph-independent stability gap.

Checked sources:
- Y. Zhu, Paths maximize the expected range of graph-indexed random walks, arXiv:2609.19728v1 (2026), full primary PDF relevant sections inspected.
- Y. Wu, Z. Xu, Y. Zhu, Average Range of Lipschitz Functions on Trees, Moscow J. Combin. Number Theory 6 (2016), indexed primary PDF/abstract inspected; direct full-PDF retrieval was unavailable during this run.
- Published finding dated 2026-09-18: Unique BHM maximizers and a quantitative standard-to-lazy gap transfer, complete RESULT inspected.
- Independent exact replay of the fork identity for orders 4 through 11 and of the cycle rank-surplus formula for cycle-class sizes 3 through 9.

Residual risks:
- The full 2016 tree paper could not be retrieved end-to-end during this run; its exact tree equality corollaries are independently quoted in the earlier published finding, but a differently phrased quantitative refinement remains a residual risk.
- The constants are not optimized and the universal lazy \(n^{-3/2}\) exponent is not claimed sharp.

## Scientific value — PASS

This is a motivated stability refinement of a newly solved extremal theorem. It identifies the correct standard-model stability exponent, provides an exact near-extremizer realizing that exponent, and gives explicit lazy separation including a polynomial tree bound. The result is structural rather than a routine numerical tightening.

Checked sources:
- Y. Zhu, Paths maximize the expected range of graph-indexed random walks, arXiv:2609.19728v1 (2026), full primary PDF relevant sections inspected.
- Y. Wu, Z. Xu, Y. Zhu, Average Range of Lipschitz Functions on Trees, Moscow J. Combin. Number Theory 6 (2016), indexed primary PDF/abstract inspected; direct full-PDF retrieval was unavailable during this run.
- Published finding dated 2026-09-18: Unique BHM maximizers and a quantitative standard-to-lazy gap transfer, complete RESULT inspected.
- Independent exact replay of the fork identity for orders 4 through 11 and of the cycle rank-surplus formula for cycle-class sizes 3 through 9.

Residual risks:
- The full 2016 tree paper could not be retrieved end-to-end during this run; its exact tree equality corollaries are independently quoted in the earlier published finding, but a differently phrased quantitative refinement remains a residual risk.
- The constants are not optimized and the universal lazy \(n^{-3/2}\) exponent is not claimed sharp.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
