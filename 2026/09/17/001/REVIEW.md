# same-model review of the six-cycle C4 construction

**Overall conclusion: PASS under TBOK-v1.** This is the same researcher's same-model assessment, not independent validation. The exact claim and complete proof are in [RESULT.md](RESULT.md).

## Correctness: PASS

For all integers q>=5,t>=3, the initial rainbow K_q plus t six-cycles sharing one clique vertex has a single insertion order that works for every injective assignment of colors to its missing edges, including assignments colliding with old colors. It follows that rwsat(n,C4)<=6n/5+126/5 for every n>=20.

The proof was checked against the definition in Li--Ma--Xie, Introduction (job `d5e049325eb75b83eaa9425c7076698d`, offsets 1500--5500). In particular, initial rainbow C4s are permitted; new colors need only be distinct from one another; and the insertion order, unlike the witness cycle, must not depend on those colors. The proof satisfies these requirements.

The potentially fragile points were checked explicitly. In group 2 the old edge pairs for different choices of y are disjoint, so two forbidden colors remove at most two of at least three choices. In groups 4 and 7, different s give disjoint pairs of new edges; one old color can spoil at most one of at least two alternatives. If the inserted edge repeats that old color, an entirely old alternate path avoids the repeated edge. The switching observation uses four distinct new spokes and an old clique edge avoiding the inserted color. Group 6 uses only new edges. All witnesses have four distinct vertices and use previously present edges. The groups exhaust the complete graph, and the edge count and residue-class choice yield the claimed constant.

The independent finite check enumerates every eligible length-three path and solves the exact partial-matching collision condition. It passed all six tested constructions n=20,...,25. Its matching solver agrees with brute-force enumeration on all 4096 triples of 2-by-2 clauses. Negative controls with one and two gadgets yielded actual bad colorings, checked by direct cycle enumeration. Formula comparisons to [1, Theorem 1.5] were actually computed at n=40,100,1000,10000. Code and saved output are [check_c4.py](artifacts/check_c4.py) and [check_c4_results.txt](artifacts/check_c4_results.txt). These checks supplement, rather than replace, the proof for arbitrary n.

## Originality: PASS to the best of our knowledge

The completed initial problem was the candidate lower bound rwsat(n,C4)>=4n/3-o(n), beyond the then located 4n/3+O(1) construction. After screening that concrete target, active research produced the counterexample family proved here. The final result was then screened in its own form.

Equivalent forms checked were C4=K_(2,2), weak saturation for the family R(C4) of rainbow copies, upper asymptotic coefficient 6/5=1.2, and existence of qualifying graph families with average degree <=12/5+o(1). The universal coloring condition is also exactly a condition on partial matchings of equal old/new colors. The asymptotic assertion is weaker than the explicit construction, so a known upper coefficient <=6/5 would already undermine the substantive novelty even if its additive constant differed. We did not require a verbatim match to the theorem wording.

The closest result is Bo--Lian--Liu, *Weak rainbow saturation numbers of paths, stars and cycles*, arXiv:2609.03823v1, Theorem 1.5 and Section 4, Case 2, (S2.1)--(S2.5). At ell=4 it gives 4n/3+764/3, not 6n/5+O(1). Its proof uses eight-edge, six-private-vertex gadgets and absorbs them separately before completing edges between gadgets. The exact relevant proof was inspected (job `3384cc3e5343cada03b284b691a715bd`, offsets 38000--45000 and 47700--52150). The switching-through-the-clique argument is inherited and explicitly credited, not claimed as original.

The actual residual is the six-edge, five-private-vertex gadget together with the cross-gadget new-edge clique on the c_i vertices. It creates the two alternative paths that allow the remaining degree-two vertices to be absorbed. This step is not obtained by specializing the earlier formula or by its separate-gadget insertion proof. The negative controls illustrate why simply deleting an edge or using an isolated cheaper gadget does not validate this insertion argument.

Stronger containing-class results were also checked: Li--Ma--Xie, Theorem 1.3 and Proposition 4.3 (job `d5e049325eb75b83eaa9425c7076698d`, offsets 0--12500 and 33900--40100) give coefficients 2 and 3/2 for C4. Neither the theorem statements nor the inspected degree-two induced-P4 construction supply the six-cycle absorption step. Their limit-existence theorem makes our asymptotic restatement legitimate but does not imply the new numerical bound. The foundational weak-saturation discussion in Behague et al., Section 6, and the alternative notation in Chakraborti et al. were inspected. The latter's Theorem 1.6 applies to complete graphs, not C4. Proper rainbow saturation of cycles uses different coloring quantifiers and its inspected C4 coefficient is 11/6. Source details and precise evidence locations are in RESULT.md.

Recorded multi-angle searches are `8056794c6a5d4d2aac78b35375bb4bab`, `3e9a5bc4ba974333ad5e716e7fec8acd`, `d31f21eb90b440c9811a9f68beb5a9f5`, and `d8ad85c0687e4c07ab020612ae0d75fe`. They cover the original target, the emergent coefficient and construction, bipartite synonyms, and rainbow-family weak saturation notation. No equivalent or stronger coverage was found in the inspected relevant primary sections. This is an evidence-bounded assessment, not an inference from search silence or from a general problem being open.

## Value: PASS

This is a new explicit asymptotic upper bound for the smallest non-triangular cycle in an existing saturation invariant, improving the best located current coefficient by 2/15, or 10 percent. It narrows the known limiting-coefficient interval from [25/24,4/3] to [25/24,6/5]. The gain is linear in n, not merely a finite-size constant or a parameter renaming. The proof uses a substantive change in how gadgets interact. It does not claim tightness, a new lower bound, or a general-cycle theorem.

## Originality scope and inaccessible sources

To the best of our knowledge, within the documented search scope and accessible literature, no equivalent or stronger prior result was found. This is not an exhaustive guarantee of novelty.

No plausible novelty-threatening source whose full text could not be obtained was identified, and no concrete unresolved covering clue remains. The inspected documents were accessible preprint versions: Bo--Lian--Liu arXiv:2609.03823v1; Li--Ma--Xie arXiv:2401.11525v1; Behague et al. arXiv:2211.08589v2; Chakraborti et al. arXiv:2212.04640v2; Halfpap et al. arXiv:2403.15602v1. Their DOI metadata does not guarantee that every publisher revision was checked. Only the cited relevant sections, not all sections of these papers, are claimed as inspected. There is no invented inaccessible-source threat list. See RESULT.md for acquisition job IDs and extraction ranges. A later covering source would require revision of this PASS.

The success marker records this qualified same-model review only. The remaining mathematical uncertainty is optimality; the remaining originality uncertainty is the inherent incompleteness of the documented literature and version coverage.
