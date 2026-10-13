# Scientific review: plateau–nesting covariance

## Correctness — PASS
The statement covers precisely uniform two-copy Stirling permutations and all positive integer orders. The depth-first contour bijection yields exactly \(P_n=L_n\) and \(D_n=2(H_n-n)\). The finite tree insertion rule has \(2n+1\) equally likely gaps. The sum of parent depths over slots, the leaf-depth sum, the conditional mixed-product formula, and the two required mean identities have been rederived algebraically. These give \(c_{n+1}=\frac{2n+2}{2n+1}c_n-\frac29\) from \(c_1=0\). The asserted binomial expression solves the recurrence; strict negativity and the limit follow analytically. `verify.py` independently replayed exact enumeration, tree decoding, conditional identities, and moment formulas. Risk: the computation checks finite orders only, so the proof, not the program, carries the infinite quantifier.

## Originality — PASS, with residual historical risk
The primary full texts [1]–[3] give the tree correspondence, marginal plateau/leaf counts, individual label gaps, and various *other* joint statistics, but not the explicitly evaluated mixed total-nesting/plateau covariance. [4] is particularly close: its multivariate generating function includes leaf count and total path length and implicitly determines mixed moments, but the stated theorems concern normalized differences of average depths and do not give the exact covariance or its all-orders sign. The new direct mixed-moment closure and formula are not direct numerical substitutions into a prior stated covariance. A more elaborate extraction from the full generating-function system may reproduce this result; historical priority is not independently established.

## Value — PASS
A plateau measures a leaf of the increasing tree (a terminal local structure), whereas the aggregate nesting span measures total tree path length (global hierarchical depth). These are two natural, independently studied statistics. The exact, strictly negative covariance for every nontrivial size, with a linear drift constant, quantitatively relates terminal abundance to hierarchical nesting. It does not follow from the marginal laws alone, nor does it consist only of one arbitrary finite coefficient. Generalizations and full joint laws are not claimed.

## Prior literature and limitations
[1] Janson (2008), arXiv:0803.1129v1; [2] Janson–Kuba–Panholzer (2008), arXiv:0805.4084; [3] Kuba–Panholzer (2010 preprint), `https://www.dmg.tuwien.ac.at/kuba/preprintStirblock.pdf`; [4] Lundblad–Wagner (2026), DOI:10.4230/LIPIcs.AofA.2026.2. Full-text comparisons focus on each paper's relevant structural and theorem sections. The result is restricted to ordinary uniform Stirling permutations. No independent historical priority determination or external mathematical validation is asserted.

Self-review: passed. Independent audit: not yet performed.
