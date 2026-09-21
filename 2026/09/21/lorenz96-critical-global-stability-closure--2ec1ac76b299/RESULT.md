# Exact closed global-stability window for energy-preserving Lorenz-96-type systems

## Result

Let \(N\ge 2\), let \(e=(1,\ldots,1)^T\in\mathbb R^N\), and let
\[
G:\mathbb R^N\to\mathbb R^N
\]
be a homogeneous quadratic map with two properties:

1. **energy preservation:** \(x^TG(x)=0\) for every \(x\in\mathbb R^N\);
2. **cyclic equivariance:** \(G(\rho x)=\rho G(x)\) for the cyclic shift \(\rho\).

Consider
\[
\dot x=G(x)-x+Fe,\qquad F\in\mathbb R.
\tag{1}
\]
Cyclic equivariance and energy preservation imply \(G(e)=0\), so \(x_F=Fe\) is an equilibrium. Put
\[
A=DG(e),\qquad S=\frac{A+A^T}{2},
\]
and denote the extreme eigenvalues of the real symmetric circulant matrix \(S\) by
\[
p_+=\lambda_{\max}(S)\ge0,\qquad p_-=\lambda_{\min}(S)\le0.
\tag{2}
\]
Then the constant equilibrium has the exact global stability characterization
\[
\boxed{
 x_F=Fe\text{ is globally asymptotically stable}
 \iff Fp_+\le1\text{ and }Fp_-\le1.
}
\tag{3}
\]
If both inequalities are strict, convergence is exponential. The new boundary point is that equality is allowed: whenever a finite endpoint is reached, \(x_F\) is nonhyperbolic but remains globally asymptotically stable.

Equivalently, if \(p_+>0>p_-\), the exact global-stability window is the closed interval
\[
\boxed{\frac1{p_-}\le F\le\frac1{p_+}.}
\tag{4}
\]
The evident one-sided or all-real variants apply if an extreme eigenvalue is zero.

### Lorenz-96 corollary

For the classical Lorenz-96 system
\[
\dot x_j=x_{j-1}(x_{j+1}-x_{j-2})-x_j+F,
\qquad j\in\mathbb Z/N\mathbb Z,\quad N\ge4,
\tag{5}
\]
the equilibrium \((F,\ldots,F)\) is globally asymptotically stable exactly for
\[
\boxed{F_-\le F\le F_+,}
\tag{6}
\]
where
\[
F_+=\left[\max_{0\le k<N}\left(\cos\frac{2\pi k}{N}-\cos\frac{4\pi k}{N}\right)\right]^{-1},
\tag{7}
\]
and
\[
\boxed{
F_-=\begin{cases}
-\dfrac12,&N\text{ even},\\[1.2ex]
-\dfrac1{\cos(\pi/N)+\cos(2\pi/N)},&N\text{ odd}.
\end{cases}}
\tag{8}
\]
Thus the global nonlinear stability window closes exactly at the first linear-instability thresholds, including the nonhyperbolic Hopf, double-Hopf, or pitchfork boundary itself.

## Proof

Because \(G(e)\) is fixed by every cyclic shift, \(G(e)=ce\) for some \(c\). Energy preservation gives \(0=e^TG(e)=cN\), hence \(G(e)=0\). Homogeneity then gives \(Ae=2G(e)=0\). Equivariance makes \(A\) circulant, so also \(e^TA=0\).

Write
\[
w=x-Fe.
\]
Quadratic homogeneity gives the exact translated equation
\[
\dot w=G(w)+(FA-I)w.
\tag{9}
\]
For
\[
V(w)=\frac12\|w\|^2,
\]
energy preservation yields
\[
\dot V=w^T(FS-I)w.
\tag{10}
\]
If \(Fp_+<1\) and \(Fp_-<1\), then \(FS-I\) is negative definite and the standard quadratic-energy argument gives exponential global convergence. This strict case is already known in the Lorenz-96-type literature.

It remains to treat equality. Suppose first that \(F=1/p_*\), where \(p_*\ne0\) is the relevant extreme eigenvalue of \(S\). Then (10) is negative semidefinite, and its zero set is
\[
E_*=\ker(S-p_*I).
\tag{11}
\]
Since \(Se=0\) and \(p_*\ne0\), every \(w\in E_*\) satisfies \(e^Tw=0\).

The energy-preserving identity contains an additional piece of information that is invisible in (10). For arbitrary \(w\) and scalar \(s\),
\[
0=(e+sw)^TG(e+sw).
\]
Using \(G(e)=0\) and quadratic homogeneity,
\[
G(e+sw)=sAw+s^2G(w).
\]
The coefficient of \(s^2\) therefore gives
\[
\boxed{e^TG(w)=-w^TAw.}
\tag{12}
\]
Now let \(w\in E_*\). Since \(e^TA=0\) and \(e^Tw=0\), (9), (12), and \(w^TAw=w^TSw\) imply
\[
\frac{d}{dt}(e^Tw)
=e^TG(w)
=-w^TSw
=-p_*\|w\|^2.
\tag{13}
\]
For every nonzero \(w\in E_*\), the right side is nonzero. Hence the vector field is transverse to the zero-dissipation set at every nonzero point: no nonzero complete trajectory can remain in \(E_*\). The largest invariant subset of \(\{\dot V=0\}\) is therefore \(\{0\}\).

Equation (10) makes every forward trajectory bounded at the endpoint, hence globally defined. LaSalle's invariance principle and (13) give \(w(t)\to0\); monotonicity of \(V\) gives Lyapunov stability. Thus \(Fe\) is globally asymptotically stable at either finite endpoint.

Conversely, if either inequality in (3) fails, then because the circulant matrix \(A\) is normal, an eigenvalue of the linearization \(FA-I\) has positive real part. The equilibrium is therefore unstable. This proves (3).

For (5),
\[
(Aw)_j=w_{j+1}-w_{j-2},
\]
so the real part of the \(k\)-th Fourier eigenvalue is
\[
d_k=\cos\frac{2\pi k}{N}-\cos\frac{4\pi k}{N}.
\tag{14}
\]
Equations (7)--(8) follow by taking the discrete maximum and minimum. If \(N\) is even the minimum is attained at \(k=N/2\), giving \(-2\); if \(N\) is odd the closest modes to \(\pi\) give
\(-\cos(\pi/N)-\cos(2\pi/N)\). Substitution into (3) proves the Lorenz-96 corollary.

## Relation to prior work and originality check

Lorenz introduced the model as a test problem for atmospheric predictability and noted decay to the constant state for sufficiently small forcing. Later bifurcation analyses by van Kekem and Sterk located the first loss of linear stability and classified the positive-forcing first bifurcation as Hopf or double-Hopf, while the negative-forcing boundary includes pitchfork and Hopf cases depending on dimension.

The closest prior result is Kerin and Engler's analysis of energy-preserving, cyclically equivariant quadratic Lorenz-96 generalizations. In the published version, their Proposition 1 proves global asymptotic stability of \(Fe\) under the **strict** inequalities \(Fp_+<1\) and \(Fp_-<1\) for localized G-maps, using exactly the negative-definite quadratic-energy argument. Their spectral analysis also identifies the bifurcation thresholds. The present result closes that open Lyapunov gap at equality, removes the localization hypothesis from this stability statement, and turns the sufficient open interval into the exact closed global-stability region (3).

This equality case is not a generic consequence of energy preservation. Schlegel and Noack explicitly note, for general energy-preserving quadratic systems, that replacing negative definiteness by negative semidefiniteness requires additional information and give examples showing qualitatively different outcomes. Here the extra cyclic structure and the polarization identity (12) force strict transversality of every nonzero zero-dissipation state, which is what closes the endpoint.

Targeted searches through Lorenz-96 stability, bifurcation, generalized-model, and lossless-quadratic literature did not locate the closed endpoint theorem (3), the identity (12) used in this setting, or the endpoint transversality argument (13). To the best of our knowledge, these statements are new. Residual priority uncertainty remains because the final publisher text of Kerin--Engler was not fully accessible in the source inspected here; its strict Proposition 1 was checked through an accessible manuscript copy together with the arXiv version and publisher metadata. No claim is made that the strict interior result or the bifurcation locations are new.

## Scientific limitations

The theorem assumes a homogeneous quadratic nonlinearity, Euclidean energy preservation, cyclic equivariance, uniform linear damping, and spatially uniform forcing. It does not cover inhomogeneous Lorenz-96 variants, generalized dissipations, or arbitrary lossless quadratic systems. At the nonhyperbolic endpoints it proves global asymptotic stability but does not quantify the generally non-exponential critical decay rate. It also does not describe the post-bifurcation attractors outside the closed stability window.

## References

1. E. N. Lorenz, *Predictability: A Problem Partly Solved*, ECMWF Seminar on Predictability (1995); reprinted in *Predictability of Weather and Climate*, Cambridge University Press (2006), 40--58. https://doi.org/10.1017/CBO9780511617652.004
2. D. L. van Kekem and A. E. Sterk, *Wave propagation in the Lorenz-96 model*, Nonlinear Processes in Geophysics **25** (2018), 301--314. https://doi.org/10.5194/npg-25-301-2018
3. J. Kerin and H. Engler, *On the Lorenz '96 model and some generalizations*, Discrete and Continuous Dynamical Systems - B **27** (2022), 769--797. https://doi.org/10.3934/dcdsb.2021064 ; arXiv:2005.07767.
4. M. Schlegel and B. R. Noack, *On long-term boundedness of Galerkin models*, Journal of Fluid Mechanics **765** (2015), 325--352. https://doi.org/10.1017/jfm.2014.736 ; arXiv:1310.0053.
