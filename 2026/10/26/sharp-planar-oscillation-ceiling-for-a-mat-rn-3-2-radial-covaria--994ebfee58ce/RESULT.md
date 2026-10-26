# Sharp planar oscillation ceiling for a Matérn-\(3/2\) radial covariance

## Finding

Let \(a>0\) and \(\omega\ge0\). On the Euclidean plane define the stationary, unit-diagonal, isotropic kernel
\[
K_{a,\omega}(x,y)=(1+a\|x-y\|_2)e^{-a\|x-y\|_2}\cos(\omega\|x-y\|_2).
\]
Then **on every finite configuration of points in \(\mathbb R^2\)**, this kernel is positive semidefinite if and only if
\[
\boxed{\frac{\omega}{a}\le\sqrt{2\sqrt3-3}=0.681250038633213\ldots.}
\]
For every admissible parameter, including equality, the Gram matrix is positive definite whenever the sample points are pairwise distinct. At equality the radial Fourier density vanishes **only** at the origin of frequency space. Beyond equality that density is strictly negative on an open neighborhood of the origin.

## Assumptions and scope

Fourier transforms are unnormalized: \(\widehat f(\xi)=\int_{\mathbb R^2} f(x)e^{-i x\cdot\xi}\,dx\). The norm is Euclidean, \(\omega\ge0\), and \(a>0\); the assertion is about arbitrary finite point configurations in the complete plane, not merely sampled grids. For nonnegative \(\omega\) the sign of the cosine depends only on the ratio \(\lambda=\omega/a\). Positive definiteness is characterized by the nonnegative Fourier density using the Bochner theorem. The kernel is integrable and continuous.

## Proof

**1. Scale and Fourier–Bessel transform.** Set \(a=1\), \(\lambda=\omega/a\), \(\rho=\|\xi\|_2/a\); general Fourier densities have the factor \(a^{-2}\). Put \(z=1-i\lambda\) and \(D=z^2+\rho^2\), using principal complex powers. The standard planar radial Laplace integral gives, for \(\Re z>0\),
\[
2\pi\int_0^\infty r e^{-zr}J_0(\rho r)\,dr
=\frac{2\pi z}{(z^2+\rho^2)^{3/2}}.
\]
Differentiate with respect to \(z\), multiply by the real coefficient of the linear term, and take real parts. The Fourier density becomes
\[
\boxed{\widehat K_{1,\lambda}(\rho)
=2\pi\operatorname{Re}\left[\frac{-i\lambda}{D^{3/2}}+
\frac{3z^2}{D^{5/2}}\right].}\tag{1}
\]
The complex integral and differentiation are justified by exponential domination. For \(\lambda=0\), (1) simplifies to the everywhere-positive \(6\pi(1+\rho^2)^{-5/2}\).

**2. Sharp necessity.** Evaluating (1) at \(\rho=0\) gives
\[
\widehat K_{1,\lambda}(0)
=2\pi\frac{3-6\lambda^2-\lambda^4}{(1+\lambda^2)^3}.
\]
If \(\lambda^2>t_*=2\sqrt3-3\), the right-hand side is negative. Continuity makes the density negative on a nonempty open disk. The Bochner characterization rules out positive semidefiniteness. Hence \(\lambda^2\le t_*\) is necessary.

**3. A polynomial positivity certificate valid at every frequency.** Suppose \(0<\lambda^2=t\le t_*\). Write the principal square root as \(\sqrt D=R e^{-i\phi}=X-iY\) with \(R>0\), \(X>0\), \(Y>0\). As \(\rho\) ranges from zero to infinity, the argument of \(D\) changes continuously from \(-2\arctan\lambda\) to \(0\). Thus \(0<\phi\le\arctan\lambda\), and
\[
u=\frac{Y}{\lambda X}=\frac{\tan\phi}{\lambda}\in(0,1].
\]
The imaginary part of \(D\) implies \(XY=\lambda\). Substituting into (1), using elementary multiple-angle identities, gives the **exact identity**
\[
\frac{\widehat K_{1,\lambda}(\rho)}{2\pi}
=\frac{P(u,t)}{R^5(1+tu^2)^{5/2}},
\]
where the denominator is strictly positive and
\[
\begin{aligned}
P(u,t)={}&3+30tu+(-30t+35t^2)u^2-60t^2u^3\\
&+(15t^2-14t^3)u^4+6t^3u^5-t^4u^6.
\end{aligned}
\]
An exact change to the degree-six Bernstein basis yields
\[
P(u,t)=\sum_{j=0}^{6}\binom6j B_j(t)u^j(1-u)^{6-j},
\]
with
\[
\begin{aligned}
B_0&=3,& B_1&=3+5t,& B_2&=(t+3)(7t+3)/3,\\
B_3&=3+9t+4t^2,&
B_4&=(45+120t+45t^2-14t^3)/15,\\
B_5&=(1+t)(9+6t-11t^2)/3,&
B_6&=(1+t)^2(3-6t-t^2).
\end{aligned}
\]
For \(0\le t\le t_*<1/2\), all coefficients are nonnegative, and \(B_0,\ldots,B_5\) are strictly positive. In particular \(B_4>0\) since \(45-14(1/2)^3>0\), \(B_5>0\) since \(9-11(1/2)^2>0\), and \(B_6\ge0\) by the definition of \(t_*\). Each Bernstein basis function is nonnegative on \([0,1]\), so \(P\ge0\). Moreover, \(P>0\) whenever \(u<1\). At \(u=1\),
\[
P(1,t)=(1+t)^2(3-6t-t^2),
\]
which vanishes exactly when \(t=t_*\). Since \(u=1\) occurs only at \(\rho=0\), this proves sufficiency and identifies the only spectral zero at the critical parameter.

**4. Strict positivity for distinct points.** The Fourier density is strictly positive on an open dense subset of \(\mathbb R^2\) for every admissible parameter. For distinct \(x_1,\ldots,x_n\), the trigonometric sum \(\sum_{j=1}^n c_j e^{i\xi\cdot x_j}\) cannot vanish identically on a nonempty open frequency set unless all \(c_j\) vanish (choose a line with distinct projected sites and apply uniqueness of one-variable exponential sums). Integrating its squared modulus against the nonnegative spectral density gives a strictly positive Gram quadratic form for nonzero coefficients. This also covers the critical parameter.

## Verification

Run `python CHECK.py` with Python 3 and the packages `sympy`, `numpy`, and `scipy`. The script checks the exact algebraic identities both for the complex-angle numerator and the seven Bernstein coefficients, then compares (1) with twenty-five independently evaluated Bessel integrals. It tests positive nonzero-frequency density at the sharp boundary, negative origin density beyond the boundary, and a concrete finite negative eigenvalue witness on a \(6\times6\) square sampling grid at \(\omega/a=0.8\). On the recorded run all tests passed; the maximum absolute integral discrepancy was \(5.33\times10^{-15}\), and the witness minimum eigenvalue was approximately \(-0.012938854494\). Finite numerical tests corroborate rather than replace the all-frequency proof.

## Relationship to prior work

The classical Matérn-\(3/2\) envelope \((1+ar)e^{-ar}\) is a known strictly positive-definite radial covariance in every Euclidean dimension. Separate earlier results characterize damped cosine covariances without the linear Matérn factor; those restrictions cannot be applied directly to the present product. A related exact calculation in three dimensions yields the sharper-in-dimension but smaller allowable ratio \(\omega/a\le1/\sqrt5\). Restriction from \(\mathbb R^3\) to \(\mathbb R^2\) certifies only that smaller sufficient interval; it does **not** imply the planar bound \(\sqrt{2\sqrt3-3}>1/\sqrt5\). The planar boundary and its Bernstein-basis all-frequency certificate are the distinct statements proved here. Hu and collaborators (2013) developed oscillatory Gaussian fields by complex-valued stochastic partial differential equations, but their displayed spectral density is a reciprocal quartic in radial frequency, not the Fourier transform of the Matérn-times-cosine family classified here.

## Limitations

This theorem treats the precisely specified planar family, not arbitrary products of Matérn and oscillatory covariances or other smoothness indices. It does not classify analogous kernels in dimensions four and above. A zero of the spectral density at one frequency does not undermine finite-set strict positive definiteness. Literature comparison is bounded; an unindexed equivalent formula remains a possibility, and the original 1993 damped-cosine article was not inspected in full.

## References

Gneiting, T., *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077 (first public posting 2011-11-30), especially §2 on radial positive definiteness and the Matérn family, https://arxiv.org/abs/1111.7077.

Gneiting, T. and Guttorp, P., *Continuous Parameter Stochastic Process Theory*, in *Handbook of Spatial Statistics* (CRC Press, 2010), §2.7, p. 26 on the damped cosine and its citation of the Zastavnyi (1993) result. Only the relevant accessible extract was available for this particular comparison.

Hu and collaborators, *Multivariate Gaussian Random Fields with Oscillating Covariance Functions using Systems of Stochastic Partial Differential Equations*, arXiv:1307.1384 (2013), especially §3.1 and equation (19), https://arxiv.org/abs/1307.1384.

The standard Fourier–Bessel transform and the Bochner characterization are used in their classical forms. An additional three-dimensional sharp Matérn-modulation result is compared by its mathematical statement in the research record, not asserted to cover this planar case.
