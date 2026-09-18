# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The algebraic characterization was checked in both directions.

For an integer relation
\[
t(1+\alpha\cdot\beta)=a\cdot\beta,
\]
the vector \(v=a-t\alpha\) satisfies \(v\cdot\beta=t\), and direct substitution
gives
\[
v\cdot\lambda_n\in\mathbb Z-t/2.
\]
Hence every frequency has the same translation phase \((-1)^t\).

Conversely, if all frequencies have a common phase under translation by \(v\),
comparison with \(\lambda_0=-\beta/2\) gives
\[
v\cdot n+(v\cdot\beta)\{n\cdot\alpha\}\in\mathbb Z.
\]
Choosing \(n\) with \(\{n\cdot\alpha\}>1/2\) and comparing \(n\) with \(2n\)
forces \(v\cdot\beta\in\mathbb Z\). Coordinate tests then give
\(v+t\alpha\in\mathbb Z^d\), recovering the integer relation. Rational
independence of \(1,\alpha_1,\ldots,\alpha_d\) prevents a nontrivial relation
from mapping to \(v=0\).

The nonuniqueness construction is also exact: on disjoint translates
\(E\) and \(E+v\), the function obtained by placing opposite phase-weighted
copies of an arbitrary \(g\) has Fourier transform
\[
\widehat g(\lambda)\left(1-c e^{-2\pi i\lambda\cdot v}\right)=0
\]
on the whole frequency set. The construction works on arbitrarily small bounded
sets and produces annihilators in every dual \(L^{p'}\), including \(L^\infty\)
for \(p=1\).

The positive half of the final iff statement is not reproved: it is item (1) of
Section 6 of arXiv:2609.20805v1. The current arXiv PDF was inspected at the
higher-dimensional theorem and the formalization discussion, where the second
rational-independence condition is an explicit hypothesis.

## Originality

**PASS, to the best of our knowledge.**

The full text of arXiv:2609.20805v1 was inspected. Its Section 6 states the
higher-dimensional universal uniqueness/completeness theorem under independence
of \(1+\alpha\cdot\beta,\beta_1,\ldots,\beta_d\); the formalization discussion
calls the corresponding hypothesis `Nonresonant`. No converse theorem,
common-phase translation-group characterization, or arbitrarily-small-measure
resonant obstruction was located in the inspected version.

Searches were made using the paper title and arXiv identifier together with
variants of `resonance`, `nonresonant`, `rational dependence`, `phase lock`,
`quasicrystal completeness`, and the defining frequency formula. No matching
prior statement of the iff criterion or the phase-lock group was found.

Relevant older literature was also checked for stronger coverage. Matei--Meyer
studies stable sampling by simple quasicrystals, while Grepstad--Lev studies
universal sampling, Riesz bases, bounded remainder sets, and arithmetic
conditions at critical density. These are closely related and establish that
arithmetic structure matters for quasicrystal sampling, but the located
statements do not give the present universal \(L^1\)-uniqueness converse for
the 2026 family or the exact group formula above.

The main residual originality risk is temporal: arXiv:2609.20805 is extremely
recent, so a contemporaneous observation may not yet be indexed. The current
arXiv submission history lists only v1. No inaccessible paper was found whose
available metadata specifically suggests that it contains this converse.

SCOPE archive searches for `universal completeness exponentials`,
`quasicrystal resonance`, `cut-and-project completeness frequencies`, and the
rational-independence formulation found no prior SCOPE record covering this
claim family.

## Value

**PASS.**

The source theorem introduces a second arithmetic independence condition in
higher dimensions. This result identifies exactly what that hypothesis excludes:
a nontrivial common translation character of the entire exponential family.
More importantly, failure is not marginal. Resonance collapses the universality
radius to zero by producing nonuniqueness on sets of arbitrarily small measure,
whereas the source theorem gives universality throughout \(|S|<1\) in the
nonresonant case when \(\|\beta\|_2<1/2\).

The exact phase-lock group also turns the arithmetic hypothesis into a geometric
and harmonic-analytic invariant. In one dimension the exceptional parameters
are explicitly the countable set
\[
\beta=-1/(\alpha+r),\qquad r\in\mathbb Q,
\]
and the resonant frequency set lies in an affine lattice. This provides a
mechanism, not only a counterexample.

## Limitations and residual risks

The result does not address frame bounds, Riesz-basis stability, or other
cut-and-project families. Its positive direction inherits the assumptions of
the source theorem, including \(\|\beta\|_2<1/2\). The converse itself does not
need that norm bound.

The source preprint is very recent, so unindexed contemporaneous work remains
the principal originality risk. The older Matei--Meyer paper was not inspected
in full text during this review; its abstract and the source paper's discussion
identify it as a stable-sampling result, which is scientifically adjacent but
not the same universal uniqueness claim.
