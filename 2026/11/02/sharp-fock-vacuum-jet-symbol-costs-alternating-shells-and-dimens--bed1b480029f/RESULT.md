# Sharp Fock vacuum-jet symbol costs: alternating shells and dimension-degree growth

## Finding

Fix integers \(d\ge1\) and \(N\ge1\). On the Gaussian Bargmann–Fock space in \(\mathbb C^d\), let \(P_{\le N}\) project onto holomorphic polynomials of total degree at most \(N\), and let \(P_0\) project onto the vacuum (constant functions). Determine the least possible essential-supremum norm of a bounded measurable symbol whose Toeplitz compression acts as the vacuum projector:
\[
\mathcal M_{d,N}:=\inf\{\|F\|_\infty:P_{\le N}T_FP_{\le N}=P_0\}.
\]

Put \(d\mu_d(s)=s^{d-1}e^{-s}\,ds/\Gamma(d)\) on \((0,\infty)\). There is a **unique** real polynomial \(p_{d,N}\) minimizing \(\int|p|\,d\mu_d\) among all real polynomials of degree at most \(N\) satisfying \(p(0)=1\). It has exactly \(N\) simple positive roots. With \(\sigma_{d,N}(s)=\operatorname{sgn}p_{d,N}(s)\), its switching radii are the unique positive roots of the moment system
\[
\int_0^\infty\sigma_{d,N}(s)s^k\,d\mu_d(s)=0,\qquad k=1,\ldots,N.
\]
The exact optimal symbol norm is
\[
\boxed{\mathcal M_{d,N}=\left(\int\sigma_{d,N}\,d\mu_d\right)^{-1}=\left(\min_{\deg p\le N,\,p(0)=1}\int|p|\,d\mu_d\right)^{-1}.}
\]
Moreover, **among all bounded measurable complex-valued symbols, with no symmetry restriction, the unique minimizer up to Lebesgue-null sets** is the alternating-shell symbol
\[
\boxed{F_{d,N}(z)=\mathcal M_{d,N}\sigma_{d,N}(\|z\|^2).}
\]
It takes values \(\pm\mathcal M_{d,N}\) on \(N+1\) radial shells. The costs increase strictly with \(N\) and obey the explicit, dimension-sharp growth bounds
\[
\boxed{\binom{\lfloor N/2\rfloor+d}{d}\le\mathcal M_{d,N}\le2^d\binom{N+d}{d};\qquad\mathcal M_{d,N}\asymp_d N^d.}
\]
The same infimum over real-valued smooth compactly supported radial symbols is \(\mathcal M_{d,N}\), but it is not attained in that subclass.

For \(N=1\), the unique switching radius is the median of the Gamma distribution with shape \(d+1\), and the cost is the reciprocal of \(2\Pr\{\mathrm{Gamma}(d,1)\le r\}-1\) at that radius. For illustration, \(\mathcal M_{1,1}\approx1.595824\) and \(\mathcal M_{2,2}\approx3.345091\); these numbers are checks, not definitions of the exact costs.

## Assumptions and scope

The Hilbert norm is \(\|f\|^2=\pi^{-d}\int_{\mathbb C^d}|f(z)|^2e^{-\|z\|^2}\,dV(z)\). All Toeplitz symbols \(F\) are in \(L^\infty(\mathbb C^d)\), complex-valued unless stated otherwise, and \(T_F=P_{\mathcal F}M_F\). Equalities between symbols hold almost everywhere. Both \(d\) and \(N\) are arbitrary positive integers; constants in \(\asymp_d\) may depend on \(d\). The finite-jet constraint is not a claim that the full Toeplitz operator has finite rank.

## Proof

**1. Radial reduction.** Average any feasible \(F\) over the unitary group \(U(d)\). The vacuum projector and the full total-degree cutoff are invariant under this action, so the averaged symbol is feasible and has no larger essential-supremum norm. An invariant symbol equals \(u(s)\) with \(s=\|z\|^2\). Its action on every homogeneous polynomial of degree \(n\) is multiplication by
\[
\lambda_n(u)=\frac1{\Gamma(n+d)}\int_0^\infty u(s)s^{n+d-1}e^{-s}\,ds.
\]
Thus the compression condition is equivalent to \(\int u\,d\mu_d=1\) and \(\int us^k\,d\mu_d=0\) for every \(1\le k\le N\).

**2. Alternating-sign duality.** On the finite-dimensional affine polynomial space \(p(0)=1\), the weighted \(L^1(\mu_d)\) norm is coercive and admits a minimizer \(p\). Its nonconstant-coordinate directional derivatives exist because its zero set has \(\mu_d\)-measure zero. Hence
\[
\int\operatorname{sgn}(p(s))s^k\,d\mu_d(s)=0,\qquad 1\le k\le N.
\]
If \(p\) had only \(m<N\) sign-changing positive roots \(r_1,\ldots,r_m\), the polynomial \(q(s)=s\prod_{i=1}^m(s-r_i)\) would have degree \(m+1\le N\) and would have, up to global sign, the same sign as \(p\) on \((0,\infty)\). Then \(\int\operatorname{sgn}(p)q\,d\mu_d\ne0\), contrary to the derivative equations. Consequently \(p\) has exactly \(N\) simple positive roots. Any two minimizers have the same sign almost everywhere by equality in the convexity triangle inequality; their \(N\) simple roots then coincide, and the constant normalization makes the polynomials equal. This proves uniqueness and the switching property.

Put \(\sigma=\operatorname{sgn}p\) and \(J=\int|p|\,d\mu_d\). Orthogonality gives \(J=\int\sigma p\,d\mu_d=\int\sigma\,d\mu_d>0\). For any feasible radial \(u\),
\[
1=\int up\,d\mu_d\le\|u\|_\infty J.
\]
The radial choice \(u=\sigma/J\) attains equality and satisfies every prescribed moment. Equality in the absolute-integral inequality forces \(u=\sigma/J\) almost everywhere, even for complex \(u\). Now suppose an arbitrary nonradial \(F\) has the same optimal norm. Its unitary average is this unique radial minimizer and has modulus \(\mathcal M_{d,N}\) almost everywhere. Since the averaged values lie in the closed disk of radius \(\mathcal M_{d,N}\), equality on the disk boundary forces \(F\) to equal that constant phase at almost every point of almost every unitary orbit. Hence the nonradial optimizer is also unique.

**3. Strict increase with the polynomial cutoff.** The sign \(\sigma_{d,N}\) does not annihilate the \((N+1)\)-st moment: with the \(N\) simple positive roots above, \(s\prod_{i=1}^N(s-r_i)\) has sign \(\pm\sigma_{d,N}\), so its pairing with \(\sigma_{d,N}\) is nonzero, while all lower positive moments vanish. Thus the unique degree-\(N\) optimal symbol cannot satisfy the \(N+1\) moment constraint. Compactness in the finite-dimensional polynomial dual minimization, or uniqueness and attainment above, now yields \(\mathcal M_{d,N+1}>\mathcal M_{d,N}\).

**4. Exact power-order growth.** Put \(m=\lfloor N/2\rfloor\) and let \(L_j^{(a)}\) denote the standard associated Laguerre polynomial. Define
\[
K_m(s)=L_m^{(d)}(s)=\sum_{j=0}^m L_j^{(d-1)}(s).
\]
Laguerre orthogonality and normalization give
\[
K_m(0)=\binom{m+d}{d},\qquad \int K_m(s)^2\,d\mu_d(s)=\binom{m+d}{d}.
\]
The admissible polynomial \(p(s)=[K_m(s)/K_m(0)]^2\) has degree at most \(N\) and weighted \(L^1\)-norm \(\binom{m+d}{d}^{-1}\). The dual formula therefore gives the lower bound.

For the upper bound, take the explicit bounded radial feasible symbol
\[
u_{d,N}(s)=2^d e^{-s}L_N^{(d)}(2s).
\]
After \(x=2s\), the positive moments of orders \(1,\ldots,N\) vanish by Laguerre orthogonality against degrees \(0,\ldots,N-1\) for weight \(x^de^{-x}\). The zeroth moment is one by the elementary Laguerre integral \(\int_0^\infty x^{d-1}e^{-x}L_N^{(d)}(x)\,dx=\Gamma(d)\). The identity
\[
L_N^{(d)}(x)=\sum_{j=0}^N\binom{N-j+d-1}{d-1}L_j(x)
\]
and the classical inequality \(e^{-x/2}|L_j(x)|\le1\) for \(x\ge0\) yield
\[
\|u_{d,N}\|_\infty\le2^d\binom{N+d}{d}.
\]
The Laguerre inequality follows, for instance, because \(e^{-x/2}L_j(x)\) is a diagonal matrix coefficient of a unitary Fock displacement operator. Equality holds at \(s=0\), so this is the exact norm of the displayed feasible symbol. The binomial estimates yield \(\mathcal M_{d,N}\asymp_d N^d\).

**5. Smooth, compactly supported exact interpolation.** Approximate the alternating-sign optimizer \(u_{d,N}\) in weighted \(L^1((1+s^N)d\mu_d)\) by smooth, real, compactly supported radial functions \(v\) with \(\|v\|_\infty\le\mathcal M_{d,N}\). To restore the exact moments, choose a nonzero, nonnegative \(\chi\in C_c^\infty((1,2))\). The matrix \(G_{kj}=\int\chi(s)s^{k+j}\,d\mu_d(s)\), \(0\le k,j\le N\), is positive definite, so a correction \(\chi(s)\sum_{j=0}^N c_js^j\) with coefficients tending to zero cancels all moment errors. The corrected smooth compactly supported symbols have costs converging to \(\mathcal M_{d,N}\). None attains it, because uniqueness would force equality with the noncompactly supported, discontinuous alternating-shell symbol.

## Verification

The standalone `verification/check_vacuum_cost.py` reproduces 330 exact rational Laguerre and moment identities and 102 numerical checks of the root conditions, moment cancellations, and sharp finite-degree bounds (432 supplementary checks total). It uses Python 3 with NumPy and SciPy for numerical checks. Execute `python verification/check_vacuum_cost.py` from the extracted package. These finite checks do not replace the all-dimension, all-degree analytic argument above. Independent validation is not claimed.

## Relationship to prior work

García and Maximenko (arXiv:2503.23276, initially public 2025-03-30) establish density of radial Toeplitz–Fock eigenvalue sequences and approximation constructions, along with obstruction to exact full finite rank; their Proposition 3.4 and Theorem 4.3 do not provide the finite-jet constrained \(L^\infty\)-minimum, unique optimizer, or dimensional growth law here. Galbis (2022) proves norm estimates for selfadjoint radial Toeplitz operators, a different optimization direction. Borichev and Rozenblum's finite-rank theorem concerns actual finite-rank full operators, not a prescribed finite compression. General weighted \(L^1\) polynomial and Chebyshev sign-alternation tools are classical; their use in the duality step is not itself claimed as original. The asserted contribution is their sharp Fock-symbol realization, rigidity among nonradial symbols, and dimension-degree cost classification.

## Limitations

The theorem concerns finite vacuum isolation through degree \(N\), not the full rank-one vacuum operator. It does not determine a simple elementary closed form for every switching radius; they are uniquely determined by a finite nonlinear incomplete-Gamma system. The binomial bounds determine the exact polynomial growth exponent in \(N\), but not the optimal large-\(N\) multiplicative constant. A more general previously published weighted \(L^1\) endpoint extremal theorem might imply the polynomial part; priority for the complete Fock operator formulation has not been independently certified. The verification script is supplementary, not a computer proof.

## References

1. K. E. García and E. A. Maximenko, *Constructive approximation of convergent sequences by eigenvalue sequences of radial Toeplitz–Fock operators*, arXiv:2503.23276v1 (public 2025-03-30), https://arxiv.org/abs/2503.23276. Relevant: Proposition 3.4 and Theorem 4.3; full text inspected.
2. A. Galbis, *Norm Estimates for Selfadjoint Toeplitz Operators on the Fock Space*, *Complex Analysis and Operator Theory* 16 (2022), article 15, https://doi.org/10.1007/s11785-021-01187-3. Relevant full-text norm theorem and proof inspected.
3. A. Borichev and G. Rozenblum, *The finite rank theorem for Toeplitz operators in the Fock space*, arXiv:1303.2996 (2013), https://arxiv.org/abs/1303.2996. Abstract-level comparison; full text not inspected.
4. Z. Lin, Y. Lu, and C. Zu, *A Fourier Criterion for Recognizing Toeplitz Operators on Fock Spaces*, arXiv:2607.04102 (2026), https://arxiv.org/abs/2607.04102. Abstract-level context only, not asserted to exclude the present result.
