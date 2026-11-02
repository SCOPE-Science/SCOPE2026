# Scientific review: exact sixth-order positivity on strongly regular graphs

## Correctness

**PASS.** The conclusion covers every connected, noncomplete, simple strongly regular graph with uniform positive edge conductance, not just the six tested examples. The proof derives its three spectral projectors, computes all three entry types, and establishes the two strict scalar inequalities \(r'(z)<0\) and \(((1-r(z))/z)'<0\) for \(z>0\). These force all off-diagonal entries to be strictly positive. The common diagonal is strictly decreasing from \(1\) to \((2-v)/v<0\), giving one unique exact transition and excluding re-entry. Denominators stay positive on the claimed domain. Exact rational full-matrix comparisons and polynomial identities provide independent finite cross-checks, not the infinite-family proof.

## Originality

**PASS, qualified by the stated historical limits.** The general rational-method invariance framework of Horváth–Song–Terlaky gives sufficient thresholds and an algorithm but does not yield the universal off-diagonal sign result or sharp strongly regular graph horizon. The Padé smoothing work of Wade and collaborators is foundational context, but its full text was unavailable, so no assertion of whole-document noncoverage is made. Previously considered fourth-order strongly regular graph results concern a different update and can have negative *edge* entries or unconditional positivity. A sixth-order complete-bipartite result already covers balanced bicliques, and these overlapping cases are explicitly credited. The claim newly assessed here is the complete strongly regular classification, including primitive examples, with a universal diagonal-only failure mechanism. Searches for equivalent scalar monotonicity formulations, matrix-positivity treatments, and more general graph-family coverage did not reveal a dominating prior statement. Specialist unindexed work remains possible.

## Mathematical value

**PASS.** The sharp positivity domain describes when sixth-order Gauss–Legendre diffusion is a bona fide stochastic transition on an entire classical graph family. The fact that *no* off-diagonal becomes negative for any positive step, while every diagonal does so at a unique finite step, establishes the precise failure mechanism. The result also identifies a meaningful nonmonotonic method-order effect: fourth-order positivity on the four-cycle is unconditional, but sixth-order positivity ceases at a finite timestep. Exact spectral formulas give implementable, non-asymptotic safety thresholds for Petersen, rook, triangular and other strongly regular networks. This is a natural complete classification rather than an isolated computation.

## Closest literature and limitations

- Horváth, Song, and Terlaky (2015), *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, preprint https://engineering.lehigh.edu/sites/engineering.lehigh.edu/files/_DEPARTMENTS/ise/pdf/tech-papers/14/14T_007.pdf : rational threshold framework, inspected introduction and section 3.2, not the special graph-family theorem.
- Wade, Khaliq, Siddique, and Yousuf (first online September 29, 2004), *Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data*, https://doi.org/10.1002/num.20039 : method context; abstract and bibliography available but full body not accessible.
- Horváth (2005), *On the positivity step size threshold of Runge–Kutta methods*, https://doi.org/10.1016/j.apnum.2004.08.026 : general positivity and step-size criteria, abstract inspected.
- Earlier exact work on fourth-order Padé positivity for strongly regular graphs and sixth-order Padé positivity for complete bipartite graphs is credited mathematically in the main result. The latter covers balanced complete bipartite special cases, which are not independently claimed as new.

Limits: equal edge conductances, undirected strongly regular graphs, and endpoint matrices only. No full historical uniqueness guarantee or independent external validation is asserted; in particular, the inaccessible full Padé smoothing article remains a literature risk.

Self-review: passed. Independent audit: not yet performed.
