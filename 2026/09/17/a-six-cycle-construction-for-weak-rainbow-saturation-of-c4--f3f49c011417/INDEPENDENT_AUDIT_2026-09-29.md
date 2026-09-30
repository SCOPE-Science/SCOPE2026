# Independent Audit — A six-cycle construction for weak rainbow saturation of C4

Audit date: 2026-09-29 (UTC)
Record path: `2026/09/17/a-six-cycle-construction-for-weak-rainbow-saturation-of-c4--f3f49c011417`
Audited tree: `0e34295bafc138a97db639a073098180a1b9bfc7`

## Disposition

**PASSED** — All three audit axes pass, subject to the explicit qualifications below.

## Correctness

**PASS**. The insertion proof satisfies the universal-coloring definition. In the switching step, the current new edge has a color distinct from all prior/new spokes, and one can choose an old clique edge xy whose old color differs from the current edge; because new colors are injective, at most one of the four spokes can share xy's color, so one of the two C4 orientations is rainbow. Group 2 has at least three y choices and the old-edge pairs used by different y are disjoint, so the two possible forbidden old-color collisions remove at most two choices. Groups 4 and 7 have at least two center choices with pairwise disjoint new-edge pairs, while the alternate all-old path handles the case when the inserted edge repeats the distinguished old edge color. Group 6 is entirely new and hence automatically rainbow. The groups leave every W-vertex complete to R before the final switching stage and exhaust K_{q+5t}. Independent execution of the exact partial-matching obstruction formulation passed (q,t)=(5,3),(6,3),(9,3),(5,4), matching the archived certificate; the edge-count formula gives the stated 6n/5+O(1) bound.

## Originality

**PASS**. Bo–Lian–Liu arXiv:2609.03823, posted 2026-09-03, gives for cycles the coefficient ell/(ell-1), hence 4/3 at C4. Li–Ma–Xie establish the general weak-rainbow-saturation framework and limit existence but not a 6/5 C4 construction. Targeted searches for rwsat(n,C4), the coefficient 6/5, and six-cycle gadget constructions did not locate an equivalent pre-2026-09-17 upper bound. The clique-switching device is inherited and explicitly credited; the novel residual is the five-private-vertex six-cycle gadget coupled through the clique on opposite vertices.

## Scientific value

**PASS**. The result changes the asymptotic leading coefficient for a concrete and actively studied invariant, from the prior 4/3 upper coefficient to 6/5, rather than merely improving an additive constant. The construction is explicit for every n>=20 and its cross-gadget coupling is a substantive structural change. It therefore has clear standalone value even though it does not determine the optimal coefficient.

## Literature evidence

- https://arxiv.org/abs/2609.03823 — Bo–Lian–Liu, Weak rainbow saturation numbers of paths, stars and cycles, posted 2026-09-03; gives cycle coefficient ell/(ell-1), i.e. 4/3 for C4.
- https://arxiv.org/abs/2401.11525 — Li–Ma–Xie, Weak rainbow saturation numbers of graphs; supplies the universal distinct-new-colors definition and existence of the asymptotic limit.
- https://discovery.ucl.ac.uk/id/eprint/10192107/7/Letzter_23m1566881.pdf — Behague et al., foundational weak rainbow saturation definition in the rainbow-saturation framework.

## Independent checks

- Checked each proof group against the quantifier that the insertion order is fixed while witness C4s may depend on the coloring.
- Re-derived the switching lemma with possible old/new color collisions allowed.
- Independently ran the exact partial-matching obstruction test on four representative parameter pairs, all passing.

## Limitations

- The result is an upper bound only; optimality and a matching lower bound remain open.
- The audit did not infer novelty from search silence alone: the closest primary results and their stated C4 coefficients were compared directly.
- No inaccessible source is represented as read.

GitHub was used only as read-only evidence. The repository tree matched the assigned tree exactly.
