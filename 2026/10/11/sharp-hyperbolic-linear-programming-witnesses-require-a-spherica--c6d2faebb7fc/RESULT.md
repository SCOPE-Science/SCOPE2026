# Sharp hyperbolic linear-programming witnesses require a spherical zero
## Finding
Let \(S=G/K\) be an irreducible symmetric space of noncompact type and let \(r>0\). For an invariant random \(r\)-sphere packing \(\mu\) of positive intensity \(i_\mu\), denote its autocorrelation by \(\eta_\mu^+\), its reduced autocorrelation by
\[
\eta_\mu=\eta_\mu^+-i_\mu^2m_G,
\]
and its positive reduced spherical diffraction measure by \(\widehat\eta_\mu\).

Let \(F\) be a real bi-\(K\)-invariant compactly supported continuous admissible linear-programming witness in the compact-support class used in Wackenhuth's proof, satisfying
\[
F(g)\le 0\quad\text{when}\quad d(go,o)\ge 2r,
\qquad
\widehat F\ge0,
\qquad
\widehat F(\mathbf 1)>0.
\]
If \(\mu\) attains the corresponding linear-programming bound
\[
D(\Lambda_\mu)
=
m_S(B_r(o))\frac{F(e)}{\widehat F(\mathbf 1)},
\]
then
\[
\widehat\eta_\mu\bigl(\{\varphi:\widehat F(\varphi)>0\}\bigr)=0,
\qquad
\operatorname{supp}\widehat\eta_\mu
\subseteq
\{\varphi:\widehat F(\varphi)=0\}.
\]
The reduced diffraction is nonzero whenever \(i_\mu>0\). Hence every sharp witness has a nontrivial spherical zero. In particular, if \(\widehat F(\varphi)>0\) for every spherical parameter \(\varphi\), then every positive-density invariant random \(r\)-packing satisfies the linear-programming inequality strictly.

## Assumptions and scope
The normalization is the one used in Wackenhuth's hyperbolic/symmetric-space packing argument: the packing density is
\[
D(\Lambda_\mu)=i_\mu m_S(B_r(o)),
\]
and the reduced autocorrelation is obtained by subtracting the independent background \(i_\mu^2m_G\). The spherical transform of \(m_G\) is the atom at the trivial spherical representation \(\mathbf 1\).

The witness is deliberately restricted to the compact-support class for which the autocorrelation--spherical-transform identity is used directly, rather than to a larger class reached only through approximation. The theorem is conditional on attainment of the linear-programming bound; it does not assert existence of an attaining packing or witness.

## Proof
Wackenhuth's proof gives the exact spectral decomposition
\[
\eta_\mu^+(F)
=
\widehat\eta_\mu(\widehat F)
+i_\mu^2\widehat F(\mathbf 1),
\]
where \(\widehat\eta_\mu\) is a positive measure and \(\widehat F\ge0\). The hard-core condition and the sign of \(F\) outside distance \(2r\) give the spatial estimate
\[
\eta_\mu^+(F)\le i_\mu F(e).
\]
If the density bound is attained, then
\[
i_\mu=\frac{F(e)}{\widehat F(\mathbf 1)}.
\]
Therefore
\[
i_\mu^2\widehat F(\mathbf 1)
\le
\eta_\mu^+(F)
\le
i_\mu F(e)
=
i_\mu^2\widehat F(\mathbf 1).
\]
Both inequalities are equalities and hence
\[
\widehat\eta_\mu(\widehat F)=0.
\]
A nonnegative continuous function has zero integral against a positive measure only if the measure gives no mass to its strict positivity set. Thus
\[
\widehat\eta_\mu(\{\widehat F>0\})=0,
\]
which is the asserted support condition.

It remains to show that the reduced diffraction cannot vanish. Suppose \(\widehat\eta_\mu=0\). Injectivity of the spherical transform for the positive-definite bi-\(K\)-invariant distribution then gives \(\eta_\mu=0\) on compactly supported bi-\(K\)-invariant tests. Choose a nonnegative such test \(h\) with \(h(e)=1\), supported on displacements strictly smaller than \(2r\), and with
\[
m_G(h)<\frac1{i_\mu}.
\]
Such a test exists by shrinking a radial neighborhood of the compact subgroup \(K\); its Haar mass tends to zero. Because distinct packing centers are separated by at least \(2r\), only diagonal pairs contribute to \(\eta_\mu^+(h)\), so
\[
\eta_\mu^+(h)=i_\mu.
\]
Consequently
\[
\eta_\mu(h)
=
i_\mu-i_\mu^2m_G(h)>0,
\]
contradicting \(\eta_\mu=0\). Hence \(\widehat\eta_\mu\neq0\). Since sharpness forces all of this nonzero measure onto the zero set of \(\widehat F\), that zero set must contain a nontrivial spherical parameter. If \(\widehat F\) is everywhere strictly positive, sharpness is impossible.

## Verification
The argument was reconstructed directly from the source normalization and the two inequalities used in the proof of the hyperbolic linear-programming bound. The equality chain was checked symbolically at the level of algebra, while the nonvanishing step was checked independently by a small-support radial test that isolates diagonal pairs. No finite enumeration, numerical experiment, or unproved limiting argument is used.

The critical boundary conditions are \(r>0\) and \(i_\mu>0\). They are needed respectively to choose a test supported below the hard-core distance and to choose it with Haar mass less than \(1/i_\mu\).

## Relationship to prior work
Wackenhuth proves the hyperbolic/symmetric-space linear-programming inequality by combining positivity of reduced spherical diffraction with the packing sign condition. The inspected short paper and its broader homogeneous-space follow-up do not state the equality consequence above, do not force the reduced diffraction onto a zero set, and do not establish the small-support lemma showing that positive-intensity hard-core packings have nonzero reduced diffraction.

Cohn and Elkies identify an analogous zero requirement for a sharp Euclidean lattice bound: Poisson summation forces the auxiliary function to vanish on nonzero lattice vectors and its Fourier transform to vanish on nonzero dual-lattice vectors. The present statement replaces the dual lattice by the reduced spherical diffraction of a possibly aperiodic invariant random packing in a noncompact symmetric space.

## Limitations
The result is a necessary condition for equality, not an existence or classification theorem. It is stated only for the compact-support direct witness class, avoiding any claim that equality survives the approximation step used for more general Harish--Chandra Schwartz witnesses. It supplies no quantitative gap when \(\widehat F\) is merely small rather than zero, and it does not determine where spherical zeros must occur beyond the support constraint.

## References
1. Maximilian Wackenhuth, *Bounds on hyperbolic sphere packings: on a conjecture by Cohn and Zhao*, arXiv:2411.07139; Comptes Rendus Mathématique 364 (2026), DOI:10.5802/crmath.821.
2. Maximilian Wackenhuth, *Linear programming bounds in homogeneous spaces, I: Optimal packing density*, arXiv:2505.23572.
3. Henry Cohn and Noam Elkies, *New upper bounds on sphere packings I*, Annals of Mathematics 157 (2003), DOI:10.4007/annals.2003.157.689.
