# Euler characteristic of projectivized eigenvalue-coincidence filtrations
## Finding
Let \(n\ge2\). For a matrix
\[
x\in\mathfrak{gl}_n(\mathbb C),
\]
write \(x_{n-1}\) for its upper-left \((n-1)\times(n-1)\) cutoff. For
\[
0\le i\le n-1,
\]
let
\[
\mathfrak g(\ge i)
=
\{x:\text{the spectra of }x\text{ and }x_{n-1}\text{ share at least }i\text{ eigenvalues, counted with multiplicity}\}.
\]
These are homogeneous algebraic cones. Put
\[
X_{n,i}=\mathbb P\mathfrak g(\ge i).
\]
Then
\[
\boxed{
\chi_{\mathrm{top}}(X_{n,i})=n^2
\qquad
(0\le i\le n-1).
}
\]
In particular every closed level has the same Euler characteristic as the ambient space
\[
\mathbb P(\mathfrak{gl}_n)\cong\mathbb P^{n^2-1}.
\]

Let \(\mathfrak g(i)\) denote the locally closed stratum where exactly \(i\) eigenvalues are shared, counted with multiplicity, and put
\[
E_{n,i}=\mathbb P(\mathfrak g(i)).
\]
Then
\[
\boxed{
\chi_c(E_{n,i})=0
\quad(0\le i\le n-2),
\qquad
\chi_{\mathrm{top}}(E_{n,n-1})=n^2.
}
\]
Thus all compactly supported Euler mass of the projectivized coincidence filtration is concentrated in the deepest exact stratum.

## Assumptions and scope
The base field is \(\mathbb C\). Eigenvalue coincidences are counted with algebraic multiplicity, exactly as in the cited literature.

The projectivization is the ordinary projectivization of the scalar-invariant cone inside \(\mathfrak{gl}_n\). The statement concerns topological Euler characteristic for the closed projective levels and compactly supported Euler characteristic for the exact locally closed strata.

No smoothness, irreducibility, or normality hypothesis is imposed. The cited work shows that these coincidence varieties can have nontrivial component structure, so the constancy of Euler characteristic is not a consequence of geometric triviality.

## Proof
Let
\[
T\subset GL_n(\mathbb C)
\]
be the diagonal torus, acting on \(\mathfrak{gl}_n\) by conjugation. This action preserves every eigenvalue-coincidence condition because conjugation preserves the spectrum of \(x\), and diagonal conjugation also preserves the upper-left cutoff and its spectrum.

Choose integers
\[
w_1,\ldots,w_n
\]
such that all ordered differences
\[
w_a-w_b
\qquad(a\ne b)
\]
are nonzero and pairwise distinct. For example one may take
\[
w_j=2^{j-1}.
\]
The resulting one-parameter subgroup acts on the matrix unit \(E_{ab}\) with weight \(w_a-w_b\), while the whole diagonal subspace has weight zero.

Hence the fixed locus in the ambient projective space is
\[
\mathbb P(\mathfrak h)
\sqcup
\{[E_{ab}]:a\ne b\},
\]
where \(\mathfrak h\) is the diagonal subspace. Thus the fixed locus consists of one copy of \(\mathbb P^{n-1}\) and \(n(n-1)\) isolated points.

Every one of these ambient fixed points lies in the deepest coincidence level. Indeed, if \(x\) is diagonal, the spectrum of \(x_{n-1}\) is literally a submultiset of the spectrum of \(x\), so the common multiplicity is \(n-1\). If \(x=E_{ab}\) with \(a\ne b\), then both \(x\) and \(x_{n-1}\) are nilpotent, so their spectra consist only of zero and again have common multiplicity \(n-1\).

Therefore for every \(i\),
\[
X_{n,i}^{\mathbb C^*}
=
\mathbb P(\mathfrak h)
\sqcup
\{[E_{ab}]:a\ne b\}.
\]
For a complex algebraic variety with an algebraic \(\mathbb C^*\)-action, compactly supported Euler characteristic equals that of the fixed locus. Since \(X_{n,i}\) is projective,
\[
\chi_{\mathrm{top}}(X_{n,i})
=
\chi_c(X_{n,i})
=
\chi_c(X_{n,i}^{\mathbb C^*}).
\]
Consequently
\[
\chi_{\mathrm{top}}(X_{n,i})
=
\chi_{\mathrm{top}}(\mathbb P^{n-1})+n(n-1)
=
n+n(n-1)
=
n^2.
\]

For the exact stratum \(E_{n,i}\), the same action applies. Every ambient fixed point has the maximal possible coincidence multiplicity \(n-1\). Hence
\[
E_{n,i}^{\mathbb C^*}=\varnothing
\qquad(0\le i\le n-2),
\]
while
\[
E_{n,n-1}^{\mathbb C^*}
=
\mathbb P(\mathfrak h)
\sqcup
\{[E_{ab}]:a\ne b\}.
\]
Localization gives the stated compactly supported Euler characteristics.

## Verification
The bundled checker verifies, for \(2\le n\le50\), that the powers-of-two cocharacter has pairwise distinct nonzero off-diagonal weights, counts the fixed components, and confirms the identity
\[
n+n(n-1)=n^2.
\]
It also checks combinatorially that every diagonal fixed point and every off-diagonal matrix-unit fixed point has maximal coincidence multiplicity \(n-1\), so no lower exact stratum has a fixed point.

For \(2\le n\le8\), an additional exact polynomial check constructs characteristic polynomials of sample diagonal points and all off-diagonal matrix units and verifies that the greatest common divisor with the cutoff characteristic polynomial has degree \(n-1\).

These finite checks are regression evidence only. The theorem for arbitrary \(n\) is the symbolic fixed-locus argument above.

## Relationship to prior work
Colarusso and Evens introduced and studied exactly these eigenvalue-coincidence strata for a matrix and its upper-left cutoff. Their 2013 preprint and 2015 journal article determine irreducible components of the exact strata using \(GL(n-1)\)-orbits on the flag variety. Their 2014 follow-up explicitly formulates the closed varieties \(\mathfrak g(\ge i)\) and gives their irreducible-component decomposition in terms of orbit saturations.

The inspected primary full texts study flatness, component decompositions, orbit geometry, quotient maps, nilfibres, and regularity questions. Targeted full-text searches found no occurrence of “Euler” or “Poincaré” in either primary paper, and no topological fixed-point formula was located. Targeted literature searches for Euler characteristic, cohomology, topology, fixed points, and compactly supported Euler characteristic of these eigenvalue-coincidence varieties did not locate the formulas above.

The result is not implied by the component decomposition: different coincidence levels have different codimensions and component structures, yet their projectivizations have the same Euler characteristic, and every lower exact stratum has compactly supported Euler characteristic zero.

## Limitations
Euler characteristic is coarse. The theorem does not determine Betti numbers, intersection cohomology, singularities, component incidence, or mixed Hodge structures.

The proof uses the specific upper-left-cutoff coincidence problem and its diagonal-conjugation symmetry. It does not automatically extend to arbitrary pairs of unrelated matrix compressions.

The fixed-point argument is short once the right torus action is isolated, so an unindexed or folklore observation remains a residual originality risk.

## References
M. Colarusso and S. Evens, *Eigenvalue Coincidences and \(K\)-orbits, I*, arXiv:1303.6661, first submitted 26 March 2013; *Journal of Algebra* 422 (2015), 611--632, DOI 10.1016/j.jalgebra.2014.08.051.

M. Colarusso and S. Evens, *Eigenvalue Coincidences and Multiplicity Free Spherical Pairs*, arXiv:1410.3901, first submitted 15 October 2014.
