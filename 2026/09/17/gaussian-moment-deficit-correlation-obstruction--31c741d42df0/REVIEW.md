# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The proof was checked at the tensor, moment, and fixed-margin compatibility
levels.

For the cubature step, the spherical \(2q\)-th moment tensor lies in the convex
hull of the rank-one tensors \(u^{\otimes2q}\).  These tensors live in an affine
hyperplane because \(|u|^{2q}=1\), so Carathéodory gives at most
\({k+2q-1\choose2q}\) positive-weight nodes.  Contracting the tensor identity
against \(x^{\otimes2q}\) gives
\[
\sum_jw_j\langle a_j,x\rangle^{2q}
=
\frac{(2q-1)!!}{k(k+2)\cdots(k+2q-2)}|x|^{2q}.
\]
The identity itself forces the directions to span \(\mathbb R^k\).

The fixed-margin rank-decomposition characterisation was checked against
Phillips (2026, Lemma 2.1), which states it for an arbitrary standardised common
margin.  Substitution of the resulting isotropic vector into the cubature
identity and Jensen's inequality gives exactly the threshold in Theorem 1.

For \(q=2\), the algebra
\[
\kappa<\frac{3k}{k+2}
\quad\Longleftrightarrow\quad
k>\frac{2\kappa}{3-\kappa}
\]
was checked.  For the six icosahedral directions, the Gram matrix in `RESULT.md`
has eigenvalues \(2,2,2,0,0,0\), and the quartic identity
\(\sum_j\langle a_j,x\rangle^4=(6/5)|x|^4\) agrees with the explicit derivation
in Phillips (2026).  It yields the necessary fourth-moment bound \(9/5\).

For the symmetric Beta application, the standardised fourth moment
\[
3-\frac{6}{2a+3}
\]
equals \(3/2\) at \(a=1/2\), \(9/5\) at \(a=1\), and is strictly increasing.
Thus every \(1/2\le a<1\) is excluded in dimension six.  Devroye and Letac
(2015, Section 4) explicitly prove attainability of every correlation matrix
through dimension five for all \(\mathrm{Beta}(a,a)\) with \(a\ge1/2\).
Wang and Zhang (2026) prove the exact uniform threshold of nine.  These facts
give the claimed exact classification and the boundary jump.

No empirical computation is required for the general theorem.

## Originality

The originality claim is deliberately limited to the combined finite-cubature
moment-deficit obstruction and its stated consequences.

The following closely related sources were inspected:

- Devroye and Letac (2015), especially the statement that symmetric
  \(\mathrm{Beta}(a,a)\) margins with \(a\ge1/2\) realise every correlation
  matrix through dimension five, and their uniform result through dimension
  nine.
- Wang, Wang and Wang (2019), for the projected-random-vector
  characterisation and high-dimensional uniform incompatibility.
- Wang and Zhang (2026), for the exact dimension-nine threshold for uniform
  margins and their moment-based rank-four obstruction in dimension ten.
- Phillips (2026), including the general fixed-margin rank-decomposition
  lemma and the quartic icosahedral proof for the arcsine law.
- Hürlimann (2014), an earlier use of Carathéodory's theorem in constructing
  universal trivariate copulas.
- Carathéodory/Tchakaloff cubature references and spherical-design literature,
  for finite positive moment matching.

Searches included exact and synonymous combinations of fixed or prescribed
margins, correlation compatibility, elliptopes, copulas, fourth and higher
moments, kurtosis/platykurtosis, Gaussian moment bounds, spherical designs,
cubature, Carathéodory/Tchakaloff compression, and symmetric Beta margins.
Searches also targeted the possible dimension-six \(\mathrm{Beta}(a,a)\)
extension and equivalent formulations based on projected random vectors.

No located source stated the following combination: for an arbitrary
standardised common margin, any strict deficit of an even moment below the
Gaussian value forces a finite elliptope obstruction; nor was a source found
giving the exact threshold \(d=5\) for the entire interval
\(1/2\le a<1\).  Phillips proves only the arcsine endpoint of this Beta interval
and treats a separate uniform quartic identity; Wang and Zhang settle the
uniform boundary.

A conceptually related phenomenon is that rotationally symmetric and
elliptical constructions impose moment relations on one-dimensional
projections.  That does not by itself give the finite set of prescribed
projections needed to exhibit a specific unattainable correlation matrix.
The finite positive cubature reduction is what supplies that bridge here.

Residual originality risk remains in older copula-attainability literature,
multivariate moment-problem literature, and cubature/design literature under
different terminology.  The literature search cannot establish exhaustive
nonexistence of an equivalent theorem.  The originality verdict is therefore
to the best of our knowledge, not a claim of exhaustive coverage.

## Value

The result turns a scalar property of the target margin into a general
finite-dimensional obstruction criterion.  It covers every platykurtic
standardised law, supplies a polynomial upper bound on the size of an
obstruction once a suitable rank \(k\) is chosen, and extracts a sharp
six-dimensional fourth-moment boundary from the icosahedral configuration.

The symmetric Beta application is an exact classification on a nontrivial
continuum of margins: the threshold is five for every \(1/2\le a<1\), then nine
at the uniform boundary \(a=1\).  This links the recent arcsine and uniform
compatibility results by a single moment mechanism.

## Limitations

The theorem is one-sided: a Gaussian-sized or larger even moment does not imply
compatibility.  The Carathéodory cardinality bound need not be optimal, and for
\(a>1\) the Beta-family result proves eventual failure without locating the
exact threshold.

The primary statements of Phillips (2026), Wang and Zhang (2026), and
Devroye--Letac (2015) were inspected.  Some older literature was available only
through abstracts, bibliographic records, or secondary indexing; in particular,
the broad copula and multivariate moment literature remains the main source of
residual equivalence risk.
