# Review

## Correctness

**PASS.**

The proof was checked at the level of the full metric-functional compactification, not
only on internal distance functions.

For the comb tree \(T_L\), properness follows because each root ball meets only finitely
many teeth and only compact initial pieces of them. The metric realization of a tree is
an \(\mathbb R\)-tree and hence CAT(0).

The compactification computation is exact. If \(p(w)>p(z)\), the tree distance gives
\[
h_w(z)=d(z,w)-d(o,w)=r(z)-p(z)=b(z).
\]
Thus any net whose attachment coordinate tends to infinity converges pointwise to the
single Busemann function \(b\). If a pointwise-convergent net of internals does not have
attachment coordinate tending to infinity, it has a subnet inside
\(\{p\le R\}\), which is compact because it consists of a finite spine segment and
finitely many finite teeth. A further metric-convergent subnet forces the functional
limit to be internal. Hence there are no omitted metric functionals.

For the endpoint \(x_n\), the exact formulas
\[
h_w(x_n)=n+L_n-2p(w)\quad(n>p(w)),\qquad b(x_n)=L_n-n
\]
show that all internal constraints become vacuous at infinity and the Busemann
functional gives the complete limit-set criterion.

The Hausdorff dichotomy was stress-tested in both directions. If \(L_n-n\to-\infty\),
every Busemann superlevel set is bounded. A weakly convergent net is therefore
eventually bounded. The compact-range lemma for nets is valid: a hypothetical
metric-separated subnet has a metrically convergent further subnet, and testing against
the internal functional centered at its metric limit forces that limit to equal the
weak limit. Properness turns bounded tails into relatively compact ones. Conversely, if
\(L_n-n\not\to-\infty\), a subsequence of endpoints has Busemann value uniformly
bounded below while every internal tends to \(+\infty\); two distinct sufficiently far
spine points are then simultaneous weak limits, proving non-Hausdorffness.

For \(L_n=n\), \(b\le0\) everywhere and \(b(x_n)=0\), so the endpoint sequence converges
to every point. The hyperconnected conclusion follows directly from eventual membership
in every neighborhood of every point. The \(T_1\) assertion was checked independently
using the internal \(h_y\) to separate \(x\) from the singleton \(\{y\}\).

## Originality

**PASS, to the best of our knowledge.**

The full text of Gutiérrez--Nevanlinna's September 2026 paper was inspected. It defines
\(\sigma(X,X^\diamond)\), proves that its convergent nets are exactly the \(d\)-weakly
convergent nets, and gives a non-Hausdorff example on the snowflaked real line. Searches
within that paper found no occurrence of “CAT”, “tree”, “geodesic”, or “proper” in the
relevant development beyond the cited background; it does not state a geodesic or
CAT(0) counterexample, nor a Hausdorff criterion for a tree family.

The earlier Gutiérrez--Nevanlinna paper was also inspected in full-text form. It proves
that bounded \(d\)-weakly convergent sequences are strongly convergent when all closed
balls are compact, gives non-geodesic examples with multiple limits, and discusses other
notions of weak convergence in CAT(0) spaces. It does not contain the comb-tree
construction, the exact endpoint limit-set formula, or the \(L_n-n\) phase transition.

Related CAT(0) literature was checked for equivalent coverage. Lytchak--Petrunin study
the standard CAT(0) weak topology based on bounded \(\Delta\)-convergence, while Kell
constructed a CAT(0) example with non-Hausdorff co-convex topology. Those are different
weak topologies. Horofunction/metric-compactification work, including
Daniilidis--Garrido--Jaramillo--Tapia-García, concerns the compactification itself rather
than the one-sided lower-semicontinuity topology considered here.

Targeted searches combined “d-weak”, “metric functional”, “CAT(0)”, “R-tree”, “proper”,
“geodesic”, “non-Hausdorff”, “horofunction”, and “comb tree”; no matching theorem or
equivalent phase transition was located. Current successful SCOPE records were searched
by the source paper, terminology, and claim family without a collision.

No inaccessible paper was identified as a specific likely source of prior coverage.
The main residual originality risk is the extreme recency of the September 2026
topology paper and the fact that the comb computation is elementary once the new
topology is in hand.

## Value

**PASS.**

The result answers a natural geometric robustness question left open by the motivating
examples: non-Hausdorffness is not an artifact of snowflaking, discreteness, lack of
geodesics, failure of properness, or positive-curvature behavior. It persists on a
locally finite proper CAT(0) \(\mathbb R\)-tree.

More than a counterexample is obtained. The full metric-functional compactification is
computed and the entire comb family has a sharp dichotomy: the weak topology is the
ordinary metric topology exactly when the endpoint Busemann heights \(L_n-n\) escape to
\(-\infty\), and it is non-Hausdorff otherwise. The critical family \(L_n=n\) shows the
strongest possible sequential failure of uniqueness, with one sequence converging to
every point. This identifies a concrete geometric mechanism—persistent horospherical
dead ends—for the pathology.

## Limitations and residual risk

- The classification is for the explicit one-ended comb family, not arbitrary proper
  CAT(0) spaces or arbitrary \(\mathbb R\)-trees.
- Multi-ended trees are not classified.
- The theorem concerns the metric-functional \(d\)-weak topology, not the co-convex or
  standard CAT(0) weak/\(\Delta\) topology.
- The bounded-net compactness lemma is an extension of the earlier bounded-sequence
  mechanism, not a standalone originality claim.
- The motivating topology paper is extremely recent, so later revisions or unindexed
  parallel observations remain a genuine originality risk.
- Independent audit has not been performed.

Same-model review: passed. Independent audit: not yet performed.
