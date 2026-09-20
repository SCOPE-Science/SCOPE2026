# Review — exact Sylvester--Gallai dimension of \(K_{2,n}\)

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof reduces an arbitrary special-line realization to a finite simple bipartite incidence graph \(Q\). The key points were checked separately:

1. An off-spine point \(b\) determines two distinct lines \(xb\) and \(yb\), so its pair of line labels defines a unique edge of \(Q\); hence \(Q\) is simple.
2. Specialness of every edge \(xb\) and \(yb\) forces every line-vertex of \(Q\) to contain at least two off-spine points. A witness cannot come from the opposite distinguished vertex or from an on-spine vertex. Thus \(\delta(Q)\ge2\).
3. Every component of a finite simple bipartite graph with minimum degree at least two contains a cycle of length at least four, so each component consumes at least four off-spine vertices.
4. Connectivity in \(Q\) propagates coplanarity: all points belonging to one component lie in a single affine plane through the common line \(xy\).
5. A union of \(c\) affine planes through one common line spans dimension at most \(c+1\).
6. The explicit four-point page construction satisfies all required special-line incidences, pages are disjoint away from the common line, and the displayed coordinates span \(q+1\) dimensions.

The small cases \(n=1,2,3,4\) agree with the formula and stress the only possible boundary in the component-count argument.

## Originality

**PASS, to the best of our knowledge.**

The most relevant source is Dvir's 2026 paper introducing \(\operatorname{SGdim}\). Its full HTML text was inspected. Observation 2.5 explicitly discusses \(K_{m,s}\) and gives only an asymptotic lower bound \(\Omega(m/s)\), paired with an asymptotically matching upper bound from the quantitative Sylvester--Gallai theorem. No exact \(K_{2,n}\) or \(K_{n,2}\) formula is stated there.

Targeted searches covered:
- “Sylvester--Gallai dimension” with \(K_{2,n}\), \(K_{n,2}\), and \(K_{m,s}\);
- “SGdim” with complete bipartite graphs;
- “special-line realization” with complete bipartite graphs;
- the source preprint identifier together with complete-bipartite terms.

These searches returned the source paper and secondary descriptions of it, but no separate exact formula matching
\[
1+\left\lfloor n/4\right\rfloor.
\]

No inaccessible paper was identified as a concrete likely source of coverage. The residual originality risk is instead that this very recent parameter may have an unindexed or newly posted follow-up, or that the exact fixed-side computation appears informally outside the indexed literature. Accordingly, the originality claim is explicitly limited to the best of our knowledge.

## Value

**PASS.**

The source paper itself singles out complete bipartite graphs and obtains only asymptotically matching bounds. The present result closes the first fixed nontrivial side \(s=2\) exactly, for every order, with a sharp coefficient and floor term. The proof also isolates a reusable structural mechanism: off-spine special-line witnesses form a bipartite incidence graph whose connected components are geometric pages, with each page requiring at least four vertices.

This is a substantive sharpening rather than a numerical example or a routine parameter increment.

## Scope of the claim

The theorem does not resolve exact \(\operatorname{SGdim}(K_{s,n})\) for \(s\ge3\), and it does not classify every extremal realization. Those are natural extensions but are not claimed here.

No independent validation, formal verification, or peer review is asserted.
