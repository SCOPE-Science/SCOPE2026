# Critical Sobolev circle polynomials: an effective-weight limit and a sharp first correction

## Finding

Fix real parameters \(\lambda>0\) and \(0<c<1/2\). Equip the unit circle with normalized Haar measure \(dm=d\theta/(2\pi)\) and the strictly positive probability measure \(d\nu(e^{i\theta})=(1+2c\cos\theta)\,dm\). For each \(n\ge1\), let \(Q_n\) be the monic polynomial of degree \(n\) orthogonal to polynomials of lower degree in
\[
\langle f,g\rangle_n=\int f\overline g\,dm+\frac{\lambda}{n^2}\int f'\overline{g'}\,d\nu.
\]
Define
\[
\Delta=\sqrt{(1+\lambda)^2-4\lambda^2c^2},\qquad
\rho=\frac{1+\lambda-\Delta}{2\lambda c},\qquad
A=-\frac1\Delta,\qquad B=1-\frac{1+\lambda}{\Delta^2}.
\]
Then \(0<\rho<1\), and, for every fixed \(R>1\), uniformly for \(|z|\ge R\), with \(q=-\rho/z\),
\[
\boxed{\frac{Q_n(z)}{z^n}=\frac1{1-q}+\frac1n\left[A\frac{q(1+q)}{(1-q)^3}+B\frac q{(1-q)^2}\right]+O_{\lambda,c,R}(n^{-2}).}
\]
In particular the limit is \(z/(z+\rho)\), determined by the effective weight \(1+2\lambda c(1+\lambda)^{-1}\cos\theta\). It depends strictly on \(\lambda\) for fixed \(c\), rather than depending only on \(\nu\). The rational first-order correction is not identically zero, and its order is sharp at every exterior point where it does not vanish.

More strongly, let \(Q_n(z)=\sum_{k=0}^{n-1}(-1)^ku_{n,k}z^{n-k}\), where \(u_{n,0}=1\). There exists \(C_{\lambda,c}>0\), independent of \(n\), such that
\[
\boxed{\max_{0\le k\le n-1}\left|u_{n,k}-\rho^k\left(1+\frac{Ak^2+Bk}{n}\right)\right|\le C_{\lambda,c}n^{-2}.}
\]

## Assumptions and precise scope

The derivative is the usual complex polynomial derivative. Both circle measures have bounded, strictly positive densities and belong to the Szegő class. The norm depends on \(n\), with penalty \(\lambda/n^2\); this is not a fixed-penalty Sobolev problem. The first formula holds for all exterior \(|z|\ge R>1\) after division by \(z^n\), and the coefficient bound is absolute even when \(k\) is comparable with \(n\). We make no assertion about relative errors for exponentially small coefficients, nor arbitrary pairs of Szegő-class measures.

## Proof

**1. Exact orthogonality equations.** Fourier orthogonality for nonnegative \(j,k\) gives
\[
\langle z^j,z^k\rangle_n
=\delta_{jk}+\frac{\lambda jk}{n^2}\bigl(\delta_{jk}+c\delta_{j,k+1}+c\delta_{j,k-1}\bigr).
\]
In particular \(1\) is orthogonal to each positive power, so the constant coefficient of \(Q_n\) is zero, giving the asserted representation. Orthogonality to \(z^{n-k}\), \(1\le k\le n-1\), yields
\[
\left(1+\lambda(1-k/n)^2\right)u_{n,k}
-\lambda c(1-k/n)(1-(k-1)/n)u_{n,k-1}
-\lambda c(1-k/n)(1-(k+1)/n)u_{n,k+1}=0.\tag{1}
\]
Here \(u_{n,0}=1\). At \(k=n-1\), the formal \(u_{n,n}\) term has zero coefficient and is absent.

**2. Uniform inverse estimate.** The system in \(u_{n,1},\dots,u_{n,n-1}\) has positive diagonal, nonpositive off-diagonal entries, and row diagonal excess at least
\[
1+\lambda(1-2c)(1-k/n)^2\ge1;
\]
the missing end neighbors can only increase this excess. At a component of maximum absolute magnitude of an arbitrary vector \(x\), the corresponding matrix-vector product has magnitude at least \(\|x\|_\infty\). Thus the system is invertible and the inverse satisfies \(\|M_n^{-1}\|_{\infty\to\infty}\le1\), uniformly in \(n\). This is a direct estimate, not a spectral approximation.

**3. Correct first-order cancellation.** The number \(\rho\) is the unique root in \((0,1)\) of
\[
\lambda c(\rho+\rho^{-1})=1+\lambda,
\]
with \(\Delta=\lambda c(\rho^{-1}-\rho)>0\). Let \(h(k)=Ak^2+Bk\) and define the comparison vector
\[
v_{n,k}=\rho^k\left(1+\frac{h(k)}n\right),\qquad k\ge0.
\]
Substitute this into the left side of (1) and divide by \(\rho^k\). The coefficient of \(n^0\) is zero by the characteristic-root identity. **The correct coefficient of \(n^{-1}\)** is
\[
(1+\lambda)h(k)-\lambda c\bigl(\rho^{-1}h(k-1)+\rho h(k+1)\bigr)+\boxed{2k-\Delta}.\tag{2}
\]
To evaluate it, introduce \(\mathcal Lh(k)=(1+\lambda)h(k)-\lambda c(\rho^{-1}h(k-1)+\rho h(k+1))\). Then \(\mathcal L(k)=\Delta\) and \(\mathcal L(k^2)=2\Delta k-(1+\lambda)\). Consequently the stated \(A=-1/\Delta\) and \(B=1-(1+\lambda)/\Delta^2\) give \(\mathcal Lh(k)=\Delta-2k\), which cancels the actual forcing \(2k-\Delta\) in (2). Note that reversing this forcing sign would *not* yield cancellation; equation (2) explicitly fixes that sign in the earlier proof.

After cancellation, the exact residual has the form
\[
\rho^k\left[n^{-2}P_2(k)+n^{-3}P_3(k)\right],
\]
where \(P_2,P_3\) are fixed polynomials with coefficients depending only on \(\lambda,c\). Since \(0<\rho<1\), \(\sup_{k\ge0}\rho^k(|P_2(k)|+|P_3(k)|)<\infty\); hence the residual is bounded by \(C_{\lambda,c}/n^2\) uniformly for \(0\le k\le n-1\). The omitted last neighbor has coefficient zero, so this reasoning remains valid at \(k=n-1\). The boundary value \(v_{n,0}=1=u_{n,0}\) agrees with the exact one. The uniform inverse estimate in Step 2 proves the boxed coefficient approximation. For \(n=1\), the polynomial is exactly \(Q_1=z\) and the coefficient statement is immediate.

**4. Exterior sum and sharpness.** Divide \(Q_n\) by \(z^n\). The coefficient error contributes at most \(C n^{-2}\sum_{k\ge0}R^{-k}=O_{\lambda,c,R}(n^{-2})\) for \(|z|\ge R>1\). The discarded tails in the geometric and the first two power-moment series beyond \(k=n-1\) are exponentially small uniformly in that region. Using
\[
\sum_{k\ge0}q^k=\frac1{1-q},\qquad
\sum_{k\ge0}kq^k=\frac q{(1-q)^2},\qquad
\sum_{k\ge0}k^2q^k=\frac{q(1+q)}{(1-q)^3}
\]
proves the stated exterior expansion. Since \(A\ne0\), the correction is a nonzero rational function, and so the order \(1/n\) cannot generally be improved. Finally, \(\rho/(1+\rho^2)=\lambda c/(1+\lambda)\). The right side increases strictly with \(\lambda\), and the left side increases on \((0,1)\); hence \(\rho\) and the limiting exterior function vary strictly with \(\lambda\).

## Verification and literature comparison

The accompanying unchanged `verify.py` independently solves finite Gram equations in exact rational arithmetic, checks orthogonality for \(n=2,\dots,12\) and large-degree approximants; these checks are supplementary to the proof. An additional exact rational evaluation at \((\lambda,c,\rho)=(1,5/13,1/5)\) gives \(\mathcal Lh(1)=-2/13\) and \(2-\Delta=2/13\), confirming the corrected first-order cancellation. The earlier displayed sign \(\Delta-2k\) on the forcing itself is erroneous, although the theorem and its coefficients remain unchanged.

Majumder and Swaminathan, *Sobolev Orthogonal Polynomials on the unit circle with varying inner product*, arXiv:2610.31994v1 (2026), Theorem 3.2 and Corollary 3.2, consider the same critical Sobolev scaling but give a derivative-measure-only limiting expression. For the admissible two-measure example here, exact Gram equations instead produce the nonconstant \(\lambda\)-dependent limit. This is a comparison with the printed 2026 theorem, not a claim about subsequent corrected versions. Castillo, Garza and Marcellán (2013) consider a single common circle measure; Marcellán and Sri Ranga (2017) consider coherent measure pairs with a fixed multiplier. Neither directly gives the balanced two-measure first correction. A general tridiagonal asymptotic theorem or an unindexed older result could provide equivalent formulas; no absolute historical-priority claim is made.

## Limitations

The result concerns this explicit first-Fourier-mode weight and only monic normalization. It does not establish a general theorem for arbitrary two-measure Szegő pairs, other scaling exponents, relative coefficient error, or asymptotics within the closed unit disk. The correction to the earlier algebraic sign does not change the original exact theorem or its advertised value.

## References

1. S. Majumder and A. Swaminathan, *Sobolev Orthogonal Polynomials on the unit circle with varying inner product*, arXiv:2610.31994v1 (2026), especially Theorem 3.2 and Corollary 3.2, https://arxiv.org/html/2610.31994v1.
2. K. Castillo, L. E. Garza and F. Marcellán, *Asymptotic behaviour of Sobolev orthogonal polynomials on the unit circle*, Integral Transforms and Special Functions 24 (2013), 23–38, DOI 10.1080/10652469.2011.649751.
3. F. Marcellán and A. Sri Ranga, *Sobolev Orthogonal Polynomials on the Unit Circle and Coherent Pairs of Measures of the Second Kind*, Results in Mathematics 71 (2017), 1127–1149, DOI 10.1007/s00025-016-0631-y.
