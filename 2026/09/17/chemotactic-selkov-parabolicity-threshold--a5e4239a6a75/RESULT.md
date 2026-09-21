# Ultraviolet instability is loss of parabolicity in the chemotactic Selkov model

## Result

Karmakar and Basu (arXiv:2609.01159) study the chemotactic Selkov system
\[
\begin{aligned}
\phi_t&=-\phi+a\psi+\phi^2\psi+D_1\Delta\phi
+\xi_1\nabla\!\cdot(\phi\nabla\psi),\\
\psi_t&=b-a\psi-\phi^2\psi+D_2\Delta\psi
+\xi_2\nabla\!\cdot(\psi\nabla\phi),
\end{aligned}
\]
with \(a,b,D_1,D_2>0\), periodic boundary conditions, and chemotactic
coefficients \(\xi_1,\xi_2\in\mathbb R\). Its positive homogeneous equilibrium is
\[
(\phi_*,\psi_*)=\left(b,\frac{b}{a+b^2}\right).
\]

The source paper identifies, for reciprocal chemotaxis
\(\xi_1\xi_2>0\), a threshold at which the preferred wave number diverges and,
beyond it, an instability of arbitrarily large wave numbers. The following
observation classifies that threshold at the PDE level.

**Theorem.** Let
\[
\mathcal D_*=
\begin{pmatrix}
D_1 & \xi_1 b\\[2mm]
\dfrac{\xi_2 b}{a+b^2} & D_2
\end{pmatrix},
\qquad
Q:=\det\mathcal D_*
=D_1D_2-\frac{\xi_1\xi_2 b^2}{a+b^2}.
\]
Then:

1. \(Q>0\) is exactly the normal-ellipticity condition for the second-order
   principal part at the positive homogeneous equilibrium.
2. \(Q=0\) is a parabolic degeneracy: one eigenvalue of the diffusion matrix
   vanishes.
3. If \(Q<0\), the linearization is Hadamard-ill-posed in every Sobolev space
   \(H^s\) on the periodic domain. More precisely, one dispersion branch obeys
   \[
   \Lambda_+(k)=c\,|k|^2+O(1),\qquad |k|\to\infty,
   \]
   with
   \[
   c=
   \frac{
   \sqrt{(D_1-D_2)^2+\dfrac{4\xi_1\xi_2 b^2}{a+b^2}}
   -(D_1+D_2)}{2}>0.
   \]
   Hence the linear solution operator cannot be bounded
   \(H^s\to H^s\) for any positive time.

Consequently, the strong reciprocal-chemotaxis regime described in the source
as an instability whose preferred wave number tends to infinity is not a
finite-scale Turing-pattern regime of the continuum PDE. It is the approach to,
and then passage through, loss of normal ellipticity. Beyond the threshold, a
spatial discretization necessarily truncates an unbounded high-frequency
growth rate; the fastest represented modes are therefore tied to the numerical
cutoff rather than to a continuum-selected wavelength.

For fully reciprocal chemotaxis \(\xi_1=\xi_2=\xi\), the threshold is
\[
|\xi|=\frac{\sqrt{D_1D_2(a+b^2)}}{b}.
\]

## Proof

Write \(p=a+b^2\). The reaction Jacobian at the homogeneous equilibrium is
\[
R=
\begin{pmatrix}
\dfrac{b^2-a}{p} & p\\[2mm]
-\dfrac{2b^2}{p} & -p
\end{pmatrix}.
\]
The second-order principal matrix obtained by linearizing the diffusion and
chemotaxis terms is
\[
\mathcal D_*=
\begin{pmatrix}
D_1 & \xi_1b\\[2mm]
\dfrac{\xi_2b}{p} & D_2
\end{pmatrix}.
\]
A Fourier mode with spatial wave vector \(k\) therefore satisfies
\[
\frac{d}{dt}\widehat w_k
=
\left(R-|k|^2\mathcal D_*\right)\widehat w_k.
\]

The diffusion-matrix trace is \(D_1+D_2>0\), and
\[
\det\mathcal D_*=Q.
\]
For a real \(2\times2\) matrix with positive trace, \(Q>0\) implies that either
both eigenvalues are positive real numbers or they are a complex-conjugate pair
with positive real part. Thus \(Q>0\) is exactly normal ellipticity at this
state. When \(Q=0\), one diffusion eigenvalue is zero.

Suppose \(Q<0\). Then \(\mathcal D_*\) has two real eigenvalues of opposite
sign,
\[
\nu_\pm=
\frac{D_1+D_2
\pm\sqrt{(D_1-D_2)^2+\dfrac{4\xi_1\xi_2b^2}{p}}}{2},
\]
with \(\nu_-<0<\nu_+\). Standard finite-dimensional eigenvalue asymptotics for
\(R-\kappa\mathcal D_*\), \(\kappa=|k|^2\to\infty\), give
\[
\Lambda_+(k)=-\nu_-|k|^2+O(1).
\]
Since
\[
-\nu_-=
\frac{
\sqrt{(D_1-D_2)^2+\dfrac{4\xi_1\xi_2b^2}{p}}
-(D_1+D_2)}{2}=c>0,
\]
the growth rate is unbounded above quadratically in wave number.

Fix \(t>0\). Choosing a single Fourier mode in the unstable eigenvector
direction gives amplification
\[
\exp(\Lambda_+(k)t)\to\infty .
\]
The \(H^s\)-weight multiplies input and output of that same mode by the same
factor \((1+|k|^2)^{s/2}\); it does not offset the exponential amplification.
Hence the solution map at time \(t\), if defined on all Fourier data, is not a
bounded map \(H^s\to H^s\). This is Hadamard ill-posedness of the linearized
Cauchy problem in Sobolev spaces.

## Exact relation to the source dispersion polynomial

The source paper's determinant of the Fourier stability matrix has the form
\[
\det(R-k^2\mathcal D_*)
=(a+b^2)+\Gamma k^2+Qk^4,
\]
where
\[
\Gamma=
D_1(a+b^2)
-D_2\frac{b^2-a}{a+b^2}
+\xi_2b
-\frac{2\xi_1b^3}{a+b^2}.
\]
Thus the coefficient that appears in the denominator of the paper's selected
wave-number formula is precisely the determinant of the principal diffusion
matrix.

When \(Q>0\), the determinant grows positively like \(Qk^4\), so a conventional
finite-wave-number stationary instability can be isolated from the
high-frequency tail. As \(Q\downarrow0\), this ultraviolet regularization
weakens. At \(Q=0\), second-order damping vanishes in one principal direction;
for \(Q<0\), that direction becomes backward parabolic and produces
\(\Lambda_+(k)\sim c k^2\).

This explains structurally why the source paper finds a diverging selected
wave number at the same reciprocal-chemotaxis threshold.

## Nonlinear principal-symbol consequence

For the full quasilinear system, the second-order coefficient matrix at a
positive state \((\phi,\psi)\) is
\[
\mathcal D(\phi,\psi)=
\begin{pmatrix}
D_1 & \xi_1\phi\\
\xi_2\psi & D_2
\end{pmatrix}.
\]
Its trace remains \(D_1+D_2>0\), while
\[
\det\mathcal D(\phi,\psi)
=D_1D_2-\xi_1\xi_2\phi\psi.
\]

Therefore:

- if \(\xi_1\xi_2<0\), the positive-state principal matrix is normally elliptic
  for every \(\phi,\psi>0\);
- if \(\xi_1\xi_2>0\), normal ellipticity is restricted to the state region
  \[
  \phi\psi<\frac{D_1D_2}{\xi_1\xi_2}.
  \]
  Equality is degenerate, and above it the principal matrix has one negative
  eigenvalue.

At the homogeneous equilibrium,
\(\phi_*\psi_*=b^2/(a+b^2)\), so this nonlinear state-space boundary reduces
exactly to \(Q=0\).

This pointwise criterion does not by itself prove a global well-posedness
theorem in the \(Q>0\) regime; it identifies the normal-ellipticity region
required by standard quasilinear parabolic theory.

## Scientific implication

The source paper already observes that, for reciprocal chemotaxis beyond
\[
\xi_1\xi_2=\frac{D_1D_2(a+b^2)}{b^2},
\]
sufficiently large wave numbers are unstable and \(k\to\infty\) has the largest
growth rate. The new point is that this threshold is exactly the principal
symbol's normal-ellipticity boundary. Therefore the post-threshold phenomenon
should not be interpreted as ordinary wavelength-selecting pattern formation
without an additional small-scale regularization.

A regularized model could, for example, add higher-order smoothing or modify the
cross-diffusive flux at large gradients. Such a modification would define a
genuine ultraviolet scale and could convert the cutoff instability into a
well-posed finite-wavelength problem. No specific regularization is asserted
here.

## Scope and limitations

The Sobolev ill-posedness statement concerns the linearization about the
positive homogeneous equilibrium in the \(Q<0\) regime. It does not claim that
every nonlinear initial-value problem has no generalized solution, nor does it
classify weak solutions of a forward-backward system.

For \(Q>0\), the theorem establishes normal ellipticity at the homogeneous
state; it does not by itself prove global existence, positivity preservation, or
nonlinear stability.

At \(Q=0\), the principal symbol is degenerate. The present result does not give
a complete well-posedness classification at that exact boundary.

The result does not question the paper's finite-wave-number Turing analysis in
parameter regimes with \(Q>0\). It specifically reclassifies the reciprocal
strong-chemotaxis ultraviolet regime \(Q\le0\).

## Relation to prior literature and originality

Normal ellipticity is a standard well-posedness requirement for
cross-diffusion systems. For example, published cross-diffusion stability work
explicitly imposes positivity of the determinant of the diffusion tensor as a
well-posedness condition, and recent quasilinear cross-diffusion work likewise
assumes uniform parabolicity before applying standard strong-solution theory.

The source-specific point appears not to have been made for
arXiv:2609.01159: searches by exact identifier/title and combinations of
"Selkov", "chemotaxis", "parabolicity", "normal ellipticity", "ill-posed",
"cross-diffusion", and "high-wavenumber" found no paper or correction identifying
the paper's reciprocal threshold with loss of normal ellipticity, nor the
resulting Sobolev ill-posedness.

The standard definitions of normal ellipticity and the generic fact that a
negative diffusion eigenvalue creates backward-parabolic high-frequency growth
are not claimed as new. The contribution is the exact identification and proof
for this newly proposed chemotactic Selkov model, together with the nonlinear
state-space criterion and the consequence for interpreting its divergent
selected wave number.

Originality is asserted only **to the best of our knowledge**.

## References

1. M. Karmakar and A. Basu, *Chemotaxis-induced linear instabilities and
   pattern formation in a reaction-diffusion model*, arXiv:2609.01159 (2026).
   https://arxiv.org/abs/2609.01159
2. J. J. L. Velázquez et al., *A domain-dependent stability analysis of
   reaction-diffusion systems with linear cross-diffusion on circular domains*,
   Nonlinear Analysis: Real World Applications, DOI 10.1016/j.nonrwa.2023.104042.
   https://doi.org/10.1016/j.nonrwa.2023.104042
3. O. Noutchie, *Quantitative Nonlocal-to-Local Limits in Multispecies
   Interaction Systems via Relative Entropy and Modulated Energy*, Journal of
   Applied Mathematics (2026), which states a uniform-parabolicity hypothesis
   for its local cross-diffusion strong-solution theory.
   https://doi.org/10.1155/jama/6835155
