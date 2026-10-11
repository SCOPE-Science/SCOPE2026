# Fiberwise competitor-load calibration and RMS locking in the Guckenheimer–Holmes cycle
## Finding
Consider the Guckenheimer–Holmes system
\[
\dot x_1=x_1(\mu-a x_1^2-bx_2^2-cx_3^2),
\]
\[
\dot x_2=x_2(\mu-a x_2^2-bx_3^2-cx_1^2),
\]
\[
\dot x_3=x_3(\mu-a x_3^2-bx_1^2-cx_2^2),
\]
with
\[
\mu>0,\qquad a>0,\qquad b>0,\qquad c>0,
\]
and suppose \(a,b,c\) are not all equal.

Let \(\nu\) be a compactly supported invariant Borel probability measure such that
\[
\nu\{x_i=0\}=0,\qquad i=1,2,3.
\]
Thus \(\nu\) is fully active: it does not charge any invariant coordinate plane.

Set
\[
X_i=x_i^2,\qquad s=a+b+c,
\]
and define the cyclic competitor loads
\[
Q_1=bX_2+cX_3,\qquad
Q_2=bX_3+cX_1,\qquad
Q_3=bX_1+cX_2.
\]

Then each competitor load is calibrated exactly on the squared-amplitude fiber it drives:
\[
\boxed{\mathbb E_\nu[Q_i\mid X_i]=\mu-aX_i,\qquad i=1,2,3.}
\]

Taking expectations and using the nonsingularity of the corresponding circulant interaction matrix gives the exact coordinate RMS locking
\[
\boxed{
\mathbb E_\nu[X_1]
=
\mathbb E_\nu[X_2]
=
\mathbb E_\nu[X_3]
=
\frac{\mu}{a+b+c}.
}
\]

Write the per-capita speeds
\[
r_i=\frac{\dot x_i}{x_i}
=
\mu-aX_i-Q_i
\]
on the full-measure set where \(x_i\ne0\). The fiber law says
\[
\mathbb E_\nu[r_i\mid X_i]=0.
\]
Consequently
\[
\boxed{
\operatorname{Var}_\nu(Q_i)
=
a^2\operatorname{Var}_\nu(X_i)
+
\mathbb E_\nu[r_i^2]
}
\]
and
\[
\boxed{
\operatorname{Cov}_\nu(X_i,Q_i)
=
-a\operatorname{Var}_\nu(X_i).
}
\]
Whenever
\[
\operatorname{Var}_\nu(X_i)>0,
\]
this becomes the exact anticorrelation formula
\[
\boxed{
\operatorname{Corr}_\nu(X_i,Q_i)
=
-
\left(
1+
\frac{\mathbb E_\nu[r_i^2]}
{a^2\operatorname{Var}_\nu(X_i)}
\right)^{-1/2}.
}
\]

There is also an aggregate defect identity. With
\[
S=X_1+X_2+X_3,
\]
the three per-capita speeds satisfy pointwise
\[
r_1+r_2+r_3
=
3\mu-sS.
\]
Hence
\[
\boxed{
\mathbb E_\nu[S]=\frac{3\mu}{s}
}
\]
and
\[
\boxed{
\operatorname{Var}_\nu(S)
=
\frac{1}{s^2}
\mathbb E_\nu[(r_1+r_2+r_3)^2].
}
\]

At the standard parameter choice used to illustrate the robust heteroclinic cycle,
\[
(\mu,a,b,c)
=
\left(
1,1,\frac{11}{20},\frac32
\right),
\]
one has
\[
s=\frac{61}{20}.
\]
Every fully active compact stationary state therefore satisfies
\[
\boxed{
\mathbb E_\nu[x_i^2]=\frac{20}{61},
\qquad i=1,2,3,
}
\]
and
\[
\boxed{
\mathbb E_\nu[x_1^2+x_2^2+x_3^2]=\frac{60}{61}.
}
\]

Thus asymmetric cyclic coupling does not permit the three stationary RMS amplitudes to drift independently: their common value is fixed by the source parameters, while deviations from perfect anticorrelation with the instantaneous competitor load are measured exactly by mean-square per-capita speed.

## Assumptions and scope
The statement concerns compact invariant probability measures that give zero mass to each coordinate plane. This assumption is essential because the coordinate planes are invariant and support the classical heteroclinic network itself.

For an ergodic invariant measure, each invariant coordinate plane has measure either zero or one. Hence the theorem applies automatically to every ergodic compact invariant state that is not carried by a coordinate plane.

The model is the classical Guckenheimer–Holmes robust heteroclinic-cycle system. The foundational monograph was published in hardcover on 1 August 1983. A modern bibliographic record classifies that work under MSC \(34C15\) among its ordinary-differential-equations classifications.

The theorem does not require cyclic symmetry of the measure. In particular, the equal RMS conclusion is a stationarity constraint rather than an assumption that the invariant state itself is symmetric.

## Proof
Define
\[
r_1=\mu-aX_1-bX_2-cX_3
\]
and cyclically \(r_2,r_3\). Then
\[
\dot x_i=x_i r_i.
\]

Fix \(i\), and let \(\phi\) be continuous on the compact range of \(X_i\). For \(\varepsilon>0\), choose a continuously differentiable function \(H_\varepsilon\) satisfying
\[
H_\varepsilon'(t)
=
\phi(t^2)\frac{t}{t^2+\varepsilon}.
\]
The generator gives
\[
LH_\varepsilon
=
\phi(X_i)
\frac{X_i}{X_i+\varepsilon}
r_i.
\]
Invariance implies
\[
\mathbb E_\nu
\left[
\phi(X_i)
\frac{X_i}{X_i+\varepsilon}
r_i
\right]
=
0.
\]
All factors are uniformly bounded on the compact support. Since
\[
\nu\{X_i=0\}=0,
\]
dominated convergence as \(\varepsilon\downarrow0\) yields
\[
\mathbb E_\nu[\phi(X_i)r_i]=0
\]
for every continuous \(\phi\). Therefore
\[
\mathbb E_\nu[r_i\mid X_i]=0,
\]
which is equivalent to
\[
\mathbb E_\nu[Q_i\mid X_i]=\mu-aX_i.
\]

Taking expectations produces
\[
aM_1+bM_2+cM_3=\mu,
\]
\[
cM_1+aM_2+bM_3=\mu,
\]
\[
bM_1+cM_2+aM_3=\mu,
\]
where
\[
M_i=\mathbb E_\nu[X_i].
\]
The determinant of this circulant linear system is
\[
(a+b+c)
\left(
a^2+b^2+c^2-ab-bc-ca
\right).
\]
Its second factor equals
\[
\frac12
\left(
(a-b)^2+(b-c)^2+(c-a)^2
\right),
\]
which is positive because \(a,b,c\) are not all equal. Hence the solution is unique, and cyclic symmetry of the equations gives
\[
M_1=M_2=M_3=\frac{\mu}{a+b+c}.
\]

For the fluctuation law,
\[
Q_i=\mu-aX_i-r_i.
\]
The conditional relation gives
\[
\mathbb E_\nu[r_i]=0
\]
and
\[
\mathbb E_\nu[(X_i-M_i)r_i]=0.
\]
Therefore
\[
\operatorname{Var}(Q_i)
=
a^2\operatorname{Var}(X_i)
+
\mathbb E[r_i^2],
\]
and
\[
\operatorname{Cov}(X_i,Q_i)
=
-a\operatorname{Var}(X_i).
\]
The correlation formula follows immediately when \(\operatorname{Var}(X_i)>0\).

Finally,
\[
r_1+r_2+r_3
=
3\mu-(a+b+c)(X_1+X_2+X_3).
\]
Taking expectations gives the mean of \(S\), and squaring the centered identity gives the aggregate variance formula.

## Verification
The packaged checker uses exact rational arithmetic.

It verifies the circulant determinant factorization, the unique stationary mean vector when \(a,b,c\) are not all equal, the pointwise residual identity
\[
Q_i-(\mu-aX_i)=-r_i,
\]
the covariance and variance decompositions under conditional orthogonality, and the aggregate identity
\[
r_1+r_2+r_3=3\mu-(a+b+c)S.
\]

For
\[
(\mu,a,b,c)
=
\left(
1,1,\frac{11}{20},\frac32
\right),
\]
it verifies
\[
\frac{\mu}{a+b+c}=\frac{20}{61}
\]
and
\[
\frac{3\mu}{a+b+c}=\frac{60}{61}.
\]

The conditional-expectation step is proved analytically by cutoff logarithmic tests; it is not inferred from numerical trajectory data.

## Relationship to prior work
Guckenheimer and Holmes introduced the system as a prototypical robust heteroclinic cycle. The foundational treatment emphasizes invariant coordinate planes, saddle connections, symmetry, and global bifurcation geometry.

A complete open 2015 review writes the three Guckenheimer–Holmes equations explicitly and illustrates the classical parameter set
\[
\mu=1,\qquad a=1,\qquad b=0.55,\qquad c=1.5.
\]
It analyzes the heteroclinic cycle and its symmetry structure. Full-document searches found no `invariant measure`, `moment`, or `covariance` formulation; occurrences of `average` concern unrelated sensor magnetization.

A later coupled-cell review again uses the Guckenheimer–Holmes cycle as a canonical phase-space network and describes its equilibria, connections, and slowing switching. Its accessible article text contains no `invariant measure`, `moment`, or `average` statement.

The global identity obtained by averaging each per-capita growth rate is closely related to standard generalized Lotka–Volterra balance reasoning and is not treated here as the sole originality claim. The stronger statement is the fiberwise disintegration
\[
\mathbb E[Q_i\mid X_i]=\mu-aX_i,
\]
together with its exact covariance and mean-square-speed defects. Those conditional identities imply infinitely many weighted stationary balances and are not recovered from the three scalar global averages alone.

## Limitations
The theorem excludes measures that charge a coordinate plane. This is mathematically significant for the Guckenheimer–Holmes model because the robust heteroclinic cycle itself lies in the union of such planes.

The individual RMS locking assumes \(a,b,c\) are not all equal. The aggregate law
\[
\mathbb E[S]=\frac{3\mu}{a+b+c}
\]
remains valid without that nondegeneracy.

The result does not prove existence of an interior periodic or chaotic invariant state for a chosen parameter set.

The theorem determines selected conditional means and second-order defects, not the full invariant distribution.

The foundational book was inspected for bibliographic, classification, and structural context rather than used for a whole-document noncoverage assertion.

Because the system is a cyclic generalized Lotka–Volterra equation in the squared amplitudes, some global per-capita average identities have broader antecedents; the residual originality risk is an unindexed prior use of the stronger conditional formulation.

## References
1. J. Guckenheimer and P. Holmes, *Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields*, Applied Mathematical Sciences 42, Springer, 1983, DOI 10.1007/978-1-4612-1140-2.
2. A. Palacios, V. In, and P. Longhini, “Symmetry-Breaking as a Paradigm to Design Highly-Sensitive Sensor Systems,” *Symmetry* 7, 1122–1150 (2015), DOI 10.3390/sym7021122.
3. O. Weinberger and P. Ashwin, “From coupled networks of systems to networks of states in phase space,” *Discrete and Continuous Dynamical Systems B* 23, 2021–2041 (2018), DOI 10.3934/dcdsb.2018193.
