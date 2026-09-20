# Same-model review

## Correctness

**Assessment: PASS.**

The precompact-rigidity argument uses only internal metric functionals. For a point
\(z\) at distance at least \(r\) from \(x\), an \(r/4\)-net point \(w\) near \(z\)
satisfies
\[
h_w(z)-h_w(x)=d(z,w)-d(x,w)<r/4-r=-3r/4,
\]
so finitely many internals cut the relative weak neighborhood down inside the metric
\(r\)-ball. Together with the known fact that \(\sigma(X,X^\diamondsuit)\) is coarser
than the metric topology, this proves exact equality on every totally bounded subset.
The proper-space corollary follows because bounded sets lie in compact closed balls.

For the binary metric tree, the metric-functional classification was checked directly.
A pointwise-convergent family of internals either has a bounded cofinal subnet, which
converges inside a compact ball to an internal functional, or escapes to infinity.
In the escaping case, compactness of the Cantor end space gives a limiting end, and the
tree identity
\[
h_w(x)=d(o,x)-2(x|w)_o
\]
forces pointwise convergence to the corresponding Busemann functional. Thus there are
no additional metric functionals omitted from the limit test.

For the sequence on the rays
\(\eta_n=0^{n-1}1\,0^\infty\) at radius \(2(n-1)+C\), the distinguished Busemann
functional is identically \(C\), every other end functional diverges to \(+\infty\),
and every internal functional diverges to \(+\infty\). Hence the d-weak limit condition
is exactly \(b_\xi(a)\le C\). Moving the same points out to radius \(3n\) also sends
\(b_\xi\) to \(+\infty\), so every metric functional tends to \(+\infty\), proving
simultaneous convergence to every point.

Potential failure modes checked:
- the example uses the geometric realization of the tree, not merely its discrete
  vertex set, so the ambient space is genuinely geodesic and CAT(0);
- the radial point \(2(n-1)+C\) lies beyond the branching point for all sufficiently
  large \(n\), which is all that is needed;
- arbitrary real \(C\), not only integer levels, are allowed because points may lie in
  edge interiors;
- the proof tests all metric functionals via the explicit closure classification, not
  only internal functionals;
- the proper-space corollary is stated for bounded nets, where a single compact ball
  contains the full range and the proposed limit.

## Originality

**Assessment: PASS, to the best of our knowledge.**

The primary September 2026 paper was inspected at its definition of d-weak convergence,
construction of \(\sigma(X,X^\diamondsuit)\), equivalence of topological and d-weak net
convergence, and non-Hausdorff example. It already records that the sequence \(n\) in
the snowflaked line \((\mathbb R,\sqrt{|x-y|})\) converges to every point. Its text does
not contain a tree, CAT(0), properness, compactness, or total-boundedness theorem.

The earlier Gutiérrez--Nevanlinna paper was also inspected. It already gives
every-point examples on nonconvex metric subspaces, proves agreement with ordinary weak
convergence for bounded sequences in normed spaces, and proves that in \(W\)-convex
spaces every d-weak limit set is closed and \(W\)-convex. It does not state a
total-bounded-subset rigidity theorem, an R-tree example, or an exact horoball
realization. The present horoballs are consistent with, but are not implied as an
existence statement by, the closed-convex limit-set theorem.

Targeted literature searches covered combinations of:
- d-weak convergence with trees, R-trees, CAT(0) spaces, proper spaces, and horoballs;
- metric-functional weak topology with compact and totally bounded subsets;
- metric functionals, horofunction boundaries, trees, and Busemann functions;
- the established projection/\(\Delta\)-weak topology on CAT(0) spaces.

No prior statement of the precompact-rigidity theorem, the exact Busemann-horoball
limit sets, or an every-point d-weak sequence in a proper CAT(0) tree was found.
The current SCOPE archive was searched by d-weak and metric-functional terminology and
showed no overlapping record.

The main residual risk is recency: *A Weak Topology on Metric Spaces* was submitted only
days ago, so parallel or not-yet-indexed work could exist. No specific inaccessible
paper was identified as likely to contain these exact claims.

## Value

**Assessment: PASS.**

The two theorems identify a sharp structural boundary for the new topology.
Precompactness completely removes the weakening, so proper spaces have no bounded
d-weak pathology at all. The binary-tree construction then shows that escape to
infinity can nevertheless produce the strongest possible failure of uniqueness inside
one of the most rigid nonlinear geometries: a proper complete CAT(0) tree.

The exact family
\[
\Lambda_d(y_n)=\{b_\xi\le C\}
\]
does more than produce one counterexample. It realizes every Busemann horoball as a
multi-limit set and explains the mechanism through one surviving boundary functional.
This complements the earlier abstract theorem that limit sets in \(W\)-convex spaces
must be closed and convex.

## Scientific limitations

The universal-limit construction is proved for the regular binary \(\mathbb R\)-tree,
not for arbitrary proper CAT(0) spaces. Boundedness implies metric convergence in
proper spaces because bounded sets there are precompact; bounded subsets of
non-proper spaces can behave differently. The topology studied here is the
metric-functional d-weak topology and should not be conflated with the standard
projection/\(\Delta\)-weak topology of CAT(0) geometry. The motivating topology paper
is exceptionally recent, leaving a residual risk of unindexed parallel work.

Same-model review: passed. Independent audit: not yet performed.
