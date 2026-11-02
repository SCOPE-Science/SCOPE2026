# Scientific review

## Correctness — PASS

For a connected tree, the vertex-edge incidence matrix is injective on edge flows. A configuration has period dividing two precisely when every signed edge comparison reverses. On a rooted parent-child edge of sign \(t\), its strictly reversed difference must have the form \(g=tk\) with \(1\le k\le t(q_v-q_w)-1\); flat edges impose \(q_v=q_w\). These necessary and sufficient local restrictions are independent on trees, so rooted coefficient extraction counts every integrable gap assignment exactly once modulo common translation. The descendant-size weight \(z^{-m_w g}\) records exactly the negative gap contribution to the conserved chip total modulo the vertex count. The unique constant fixed state is removed and primitive cycles consist of two states. Root changes and the claim's distinction between fixed-total counts and translation classes follow from that bijection.

The standalone checker compared the recurrence to independent edge-gap enumeration on all 1,442 labelled trees through six vertices, including all mass residue vectors. A separate unweighted comparison tested 1,441 nontrivial trees. Exact integer two-step simulations and independent recurrence replay also passed. The proof covers all tree sizes; these finite tests do not establish the infinite theorem by themselves.

## Originality — PASS with documented historical risk

The earliest relevant source is Duffy–Lidbetter–Messinger–Nowakowski, arXiv:1609.05792 (first posted 2016-09-19). It introduces and analyzes the diffusion game on several graph classes. Long–Narayanan, arXiv:1704.04295, proves eventual period one or two on arbitrary graphs and supplies the edge-reversal property. Neither supplies the exact all-tree transfer at each conserved total. Mullen–Nowakowski–Cox, arXiv:2010.04750, enumerates path periodic configurations using a linear recurrence, whereas its original full text does not provide an arbitrary-tree mass-resolved formula. Their complete-graph study, arXiv:2010.07745, concerns another family; only its abstract was accessible in this comparison.

Comparisons with available prior claims cover star and double-star special families and a cyclic transfer formulation. Those are not equivalent to, and do not imply, a general tree recurrence with integer chip-total residues. Semantic research-record searches using the same objects, aliases, parameters, and enumeration forms identified no dominating all-tree result. Absence from search is not a proof of absolute novelty. A related thesis was not accessible in full and remains a historical-overlap risk.

## Mathematical value — PASS

The exact mass-resolved census solves a natural family-independent recurrence problem for unbounded integer state spaces on arbitrary labelled trees, with polynomial-time exact computation. Previously studied paths, stars and double-stars are special shapes; placing all finite trees under one algorithm, while retaining the conserved-total split, is structurally informative. The two nonisomorphic degree-multiset twins on six vertices have 279 versus 197 primitive two-cycles modulo translation and different six-component mass profiles. This exhibits a nontrivial geometric invariant beyond degree statistics and provides a natural test for future tree dynamics.

## Limits and relevant literature

The method uses acyclicity; a cyclic graph has extra gap-sum constraints. It does not describe transient basins, convergence time, or arbitrary graph systems. The earliest preprint date anchors the historical source; later revision and journal dates are not substituted. Historical equivalents in unindexed or incompletely accessible literature cannot be ruled out. Verification is not independent expert validation.

Self-review: passed. Independent audit: not yet performed.
