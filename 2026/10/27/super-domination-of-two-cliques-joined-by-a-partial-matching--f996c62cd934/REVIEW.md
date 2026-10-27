# Scientific review

## Correctness — PASS
The defining private-witness condition permits exactly three disjoint types of omitted sets. When both sides have omissions, two or more on either side is impossible because each candidate internal witness sees at least two omissions and any candidate external witness sees an omitted vertex on its own side as well. One omission on each side always works using a third index, so the requirement \(n\ge3\) is essential. When omissions occupy only one clique, omitted vertices beyond a singleton require their matched partners as unique witnesses. The all-set and minimal-set polynomials follow by disjoint counting and maximal-omission duality. All boundary cases \(t=0,1,2,n\) are explicitly handled.

The packaged Python checker independently evaluates the defining predicate and maximality on 167,424 subsets for the 30 pairs \(3\le n\le7\), \(0\le t\le n\), agreeing with all formulas. This is corroborating finite evidence; the proof handles all \(n\ge3\).

## Originality — PASS with residual priority risk
Klein--Rodríguez-Velázquez--Yi (arXiv:1705.00928), inspected through its Cartesian-product theorem, already implies the scalar value for the complete-prism endpoint; this is not claimed anew. Ghanbari--Jäger--Lehtilä (arXiv:2209.01795), inspected in its full open preprint, counts minimum sets of other graph classes and analyzes different products and gluing constructions, not this complete two-parameter census. The closest mathematical-index result for complete multipartite graphs concerns a graph class with a different cross-edge pattern and cannot entail this matching-dependent polynomial. Related complete-prism findings about Roman domination, total domination and zero forcing use different predicates. Kaidash's 2024 polynomial chapter was inspected only at abstract level; unnamed graph examples therein are a residual priority risk rather than proof of novelty.

## Mathematical value — PASS
The two-parameter classification counts **all** super dominating sets, not solely optima, on the natural interpolation from two disjoint cliques through a bridge to a full clique prism. It exposes an exact threshold: all inclusion-minimal solutions have one size for \(t\le2\), but for \(t\ge3\) their two sizes differ by \(t-2\). Taking the connected full-matching endpoint makes this inclusion-minimal gap unbounded. The extremal multiplicities are explicit, distinguishing the genuinely minimum sets from much larger inclusion-minimal ones.

## Limits and status
The result is restricted to \(n\ge3\), with labeled vertices and ordinary (open-neighborhood) super domination. Independent mathematical review has not been performed. Further literature review may find an equivalent specialization of a general super-domination polynomial formula.

Self-review: passed. Independent audit: not yet performed.
