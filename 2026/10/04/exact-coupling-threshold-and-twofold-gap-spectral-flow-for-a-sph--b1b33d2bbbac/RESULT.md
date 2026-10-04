# Exact coupling threshold and twofold gap spectral flow for a spherical non-local Dirac shell
## Finding
Let \(m>0\), let \(S_R^2\subset\mathbb R^3\) be the sphere of radius \(R>0\), and specialize the non-local relativistic shell operator of Heriban and Tušek to the constant coefficient matrices \(F=I_4\) and \(G=\lambda I_4\), with \(\lambda\in\mathbb R\). In the formal notation of the source, the perturbation is
\[
\lambda|\delta_{S_R^2}\rangle\langle\delta_{S_R^2}|.
\]
Define
\[
\lambda_c=\frac{1}{8\pi mR^3}.
\]
The open gap \((-m,m)\) contains an eigenvalue if and only if \(|\lambda|>\lambda_c\). Whenever it exists, it is unique as an energy and has multiplicity exactly two.

For \(\lambda>\lambda_c\), write that energy as \(E(\lambda)\). It is the unique \(E\in(-m,m)\) satisfying
\[
\lambda\,\frac{2\pi R^2(1-e^{-2R\sqrt{m^2-E^2}})}{\sqrt{m^2-E^2}}(m-E)=1.
\]
The map \(\lambda\mapsto E(\lambda)\) is strictly increasing, with \(E(\lambda)\to-m\) as \(\lambda\downarrow\lambda_c\) and \(E(\lambda)\to m\) as \(\lambda\to+\infty\). It crosses zero at
\[
\lambda_0=\frac{1}{2\pi R^2(1-e^{-2mR})}.
\]
For negative coupling the spectrum is reflected: \(E(-\lambda)=-E(\lambda)\).

The edge laws are
\[
E(\lambda)+m\sim32\pi^2mR^4(\lambda-\lambda_c)^2
\quad(\lambda\downarrow\lambda_c),
\]
and
\[
m-E(\lambda)\sim\frac{1}{4\pi R^3\lambda}
\quad(\lambda\to+\infty).
\]

## Assumptions and scope
The dimension is three, the mass is positive, the supporting hypersurface is exactly the round sphere \(S_R^2\), and the source coefficients are the constant matrices \(F=I_4\), \(G=\lambda I_4\). This is a rank-four non-local surface-average perturbation. It is not the usual local electrostatic or Lorentz-scalar Dirac \(\delta\)-shell model, whose transmission condition acts pointwise on the surface.

The source proves self-adjointness for this Hermitian choice and gives the finite-dimensional eigenvalue criterion in the free gap. The result here evaluates that criterion completely for the spherical constant-coefficient specialization.

## Proof
For \(z\in(-m,m)\), put \(\kappa=\sqrt{m^2-z^2}>0\). The three-dimensional free resolvent kernel in the source is
\[
R_z(x)=\left(zI_4+m\alpha_0+(1+\kappa|x|)\frac{i(\alpha\cdot x)}{|x|^2}\right)
\frac{e^{-\kappa|x|}}{4\pi|x|}.
\]
Because the columns of \(F=I_4\) are linearly independent, the source spectral condition reduces to
\[
-1\in\sigma\left(\lambda\int_{S_R^2}M(z)I_4\,d\sigma\right).
\]
Using the source formula for the Weyl function, the matrix inside the integral is the principal-value double surface integral of \(R_z(x-y)\). The vector part is antisymmetric under \(x\leftrightarrow y\), so its symmetric principal value is zero. For fixed \(x\in S_R^2\), spherical coordinates give the Yukawa identity
\[
\int_{S_R^2}\frac{e^{-\kappa|x-y|}}{4\pi|x-y|}\,d\sigma_y
=\frac{1-e^{-2\kappa R}}{2\kappa}.
\]
After the outer surface integration,
\[
Q(z):=\int_{S_R^2}M(z)I_4\,d\sigma
=Y(\kappa)(zI_4+m\alpha_0),
\qquad
Y(\kappa)=\frac{2\pi R^2(1-e^{-2\kappa R})}{\kappa}.
\]
The matrix \(\alpha_0\) has eigenvalues \(+1\) and \(-1\), each of multiplicity two. Hence the Birman--Schwinger matrix \(\lambda Q(z)\) has eigenvalues
\[
\lambda Y(\kappa)(z+m),\qquad \lambda Y(\kappa)(z-m),
\]
each twice. If \(\lambda>0\), only the second can equal \(-1\), giving
\[
\lambda f(z)=1,
\qquad
f(z)=Y(\sqrt{m^2-z^2})(m-z).
\]
If \(\lambda<0\), the first branch gives the reflected equation, so \(E(-\lambda)=-E(\lambda)\).

It remains to prove that \(f\) is strictly decreasing and identify its endpoint values. Put \(z=m\cos\theta\) with \(0<\theta<\pi\), then \(y=\tan(\theta/2)>0\), and set \(a=4mR\). A direct half-angle simplification gives
\[
f(z)=2\pi R^2 h_a(y),
\qquad
h_a(y)=y\left(1-e^{-a y/(1+y^2)}\right).
\]
With \(u=a y/(1+y^2)>0\) and \(c=(1-y^2)/(1+y^2)>-1\),
\[
e^u h_a'(y)=e^u-1+cu>e^u-1-u>0.
\]
Thus \(h_a\) is strictly increasing in \(y\), while \(z\) is strictly decreasing in \(y\); hence \(f\) is strictly decreasing in \(z\). The endpoint limits are
\[
\lim_{z\uparrow m}f(z)=0,
\qquad
\lim_{z\downarrow-m}f(z)=8\pi mR^3.
\]
Therefore \(\lambda f(z)=1\) has exactly one solution in the gap precisely when \(\lambda>1/(8\pi mR^3)\). The corresponding nullspace is one eigenspace of \(\alpha_0\), hence two-dimensional; the boundary-triple eigenfunction map is injective in the free resolvent set, so the operator eigenvalue multiplicity is exactly two.

At \(z=0\), the equation gives the displayed \(\lambda_0\). For the lower edge, write \(z=-m+\delta\). Then
\[
Y(\kappa)=4\pi R^3-4\pi R^4\kappa+O(\kappa^2),
\qquad
\kappa=\sqrt{2m\delta}+O(\delta^{3/2}),
\]
so
\[
f(-m+\delta)=8\pi mR^3-8\sqrt2\,\pi m^{3/2}R^4\sqrt\delta+O(\delta).
\]
Expanding \(1/\lambda\) at \(\lambda_c\) yields
\[
\delta\sim32\pi^2mR^4(\lambda-\lambda_c)^2.
\]
At the upper edge, with \(z=m-\delta\), one has \(f(z)=4\pi R^3\delta+o(\delta)\), which gives the strong-coupling law.

## Verification
The proof is analytic. A standalone numerical checker accompanies this result only to corroborate the algebra: it evaluates the exact critical and zero-crossing couplings, solves the scalar gap equation for representative parameters, checks the reflection law, and verifies convergence of the two displayed asymptotic ratios. Finite numerical checks are not used to prove uniqueness, multiplicity, or the infinite-parameter statements.

## Relationship to prior work
Heriban and Tušek introduce the non-local relativistic shell model, prove self-adjointness, identify the free essential spectrum, and reduce gap eigenvalues to a finite-dimensional matrix condition. Their inspected article does not specialize that condition to a round sphere with constant \(F\) and \(G\), nor state the sharp coupling threshold, complete gap spectral flow, exact multiplicity, zero crossing, or edge laws above.

Classical and modern Dirac \(\delta\)-sphere papers concern local surface interactions and pointwise transmission conditions; those results do not imply the finite-rank global surface-average calculation here. Zolotarev's non-local Dirac spectral work is on a finite interval rather than a three-dimensional spherical shell. Targeted searches for the source, spherical specialization, exact threshold, spectral-flow aliases, and separable-shell formulations found no covering published statement.

## Limitations
The result is specific to a round sphere and constant scalar matrix coupling. It does not classify nonconstant matrix-valued coefficients or nonspherical hypersurfaces. It makes no claim about threshold resonances exactly at \(|\lambda|=\lambda_c\), embedded eigenvalues outside the gap, scattering, or the local Dirac \(\delta\)-shell model. An equivalent result could exist in older separable-potential literature under a different formalism; the closest located non-local Dirac work is one-dimensional and is retained as an originality risk.

## References
1. L. Heriban and M. Tušek, *Non-local relativistic \(\delta\)-shell interactions*, Letters in Mathematical Physics 114, 79 (2024), arXiv:2311.02638, DOI:10.1007/s11005-024-01828-6.
2. V. A. Zolotarev, *Direct and inverse spectral problems for a Dirac operator with non-local potential*, Journal of Mathematical Analysis and Applications 503 (2021), 125075, DOI:10.1016/j.jmaa.2021.125075.
3. N. Arrizabalaga, A. Mas, and L. Vega, *Shell interactions for Dirac operators*, Journal de Mathématiques Pures et Appliquées 102 (2014), 617--639, arXiv:1303.2519.
