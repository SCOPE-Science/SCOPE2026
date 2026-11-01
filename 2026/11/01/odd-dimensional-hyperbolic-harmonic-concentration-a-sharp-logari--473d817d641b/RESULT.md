# Odd-dimensional hyperbolic-harmonic concentration: a sharp logarithmic spectral excess

## Finding

Fix an **odd integer** \(n\ge3\), a weight \(\alpha>-1\), and a squared concentration radius \(T=R^2\in(0,1)\). On the real unit ball \(\mathbb B^n\), let \(\mathscr H^2_{\alpha}\) be the weighted Hilbert space of functions annihilated by the hyperbolic Laplacian, with volume weight \((1-|x|^2)^\alpha\). Let \(A_{\alpha,n,T}\) be the orthogonal compression of multiplication by \(\mathbf 1_{\{|x|^2<T\}}\) to this space. Let \(E_{\alpha,n,T}\) denote the corresponding compression on the **Euclidean-harmonic** weighted Bergman space, with the same volume weight. Count eigenvalues exceeding \(\varepsilon\), including their multiplicities, by \(N_H(\varepsilon)\) and \(N_E(\varepsilon)\).

Write \(d=n/2\), \(a=-\log T\), and let \(Y\) have the gamma distribution with shape \(d\) and unit rate. Define the strictly positive finite integral
\[
I_{\alpha,d}=\int_0^\infty e^{-u}u^\alpha\bigl(\mathbb E(u+Y)^{d-1}\bigr)^2\,du.
\]

For every spherical-harmonic degree \(m\ge1\), the compression eigenvalues satisfy
\[
\begin{aligned}
\Lambda_m^H &\sim \frac{T^d(1-T)^{\alpha+n-2}}{I_{\alpha,d}}\,m^{\alpha+n-2}T^m,\\
\Lambda_m^E &\sim \frac{T^d(1-T)^\alpha}{\Gamma(\alpha+1)}\,m^\alpha T^m.
\end{aligned}
\]
Each occurs with spherical-harmonic multiplicity \(h_{m,n}=(2m+n-2)(m+n-3)!/[m!(n-2)!]\). In particular,
\[
\frac{\Lambda_m^H}{\Lambda_m^E}\sim
\frac{\Gamma(\alpha+1)(1-T)^{n-2}}{I_{\alpha,d}}m^{n-2}.
\]

**The spectral counting conclusion** is the exact first difference term
\[
\boxed{\displaystyle N_H(\varepsilon)-N_E(\varepsilon)
=\frac{2(n-2)}{(n-2)!\,a^{n-1}}\,L^{n-2}\log L+O_{n,\alpha,T}(L^{n-2}),\qquad L=\log(1/\varepsilon)\to\infty.}
\]
The leading excess is positive and depends on \(n,T\), but not on \(\alpha\). In the first odd dimension \(n=3\) it is \(2a^{-2}L\log L+O(L)\); in \(n=5\) it is \(a^{-4}L^3\log L+O(L^3)\).

## Assumptions and scope

We use complex-valued functions harmonic for \(\Delta_h f=(1-|x|^2)[(1-|x|^2)\Delta f+2(n-2)x\cdot\nabla f]\). The normalized measure is \(c_{n,\alpha}(1-|x|^2)^\alpha dx\), with any positive normalization constant \(c_{n,\alpha}\); all eigenvalue ratios are independent of that choice. The Euclidean comparison space has \(\Delta f=0\). The subball and weight are fixed while \(m\to\infty\) and \(\varepsilon\downarrow0\). The theorem covers all fixed odd \(n\ge3\), including the nonterminating hypergeometric regime; no uniform-in-dimension or moving-radius estimate is asserted.

## Proof

**1. Exact spectral diagonalization.** A spherical harmonic of degree \(m\) has a unique regular hyperbolic-harmonic radial extension proportional to \(r^mF_{m,d}(r^2)\), with
\[
F_{m,d}(t)={}_2F_1(m,1-d;m+d;t),\quad 0\le t<1.
\]
The alternative boundary-normalized radial factor differs by a scalar, canceled in concentration ratios. Orthogonality of distinct spherical-harmonic degrees and rotational invariance of the subball show that every normalized vector in the degree-\(m\) component has the same eigenvalue
\[
\Lambda_m^H=\frac{\int_0^T t^{m+d-1}(1-t)^\alpha F_{m,d}(t)^2\,dt}{\int_0^1 t^{m+d-1}(1-t)^\alpha F_{m,d}(t)^2\,dt}.
\]
For Euclidean-harmonic extensions the factor is identically one, hence \(\Lambda_m^E=B_T(m+d,\alpha+1)/B(m+d,\alpha+1)\), where \(B_T\) is the incomplete beta integral. The degree multiplicity, valid for \(m\ge1\), is
\[
h_{m,n}=\binom{m+n-1}{n-1}-\binom{m+n-3}{n-1}=
\frac{(2m+n-2)(m+n-3)!}{m!(n-2)!}.
\]
The degree-zero multiplicity is one and affects no asymptotic term.

**2. The nonpolynomial beta-to-gamma boundary layer.** Euler's hypergeometric integral applies because \(m>0\) and \(d>0\). For \(V_m\sim\mathrm{Beta}(m,d)\), it gives the *positive* expectation
\[
F_{m,d}(t)=\mathbb E(1-tV_m)^{d-1}.
\]
Put \(W_m=m(1-V_m)\). Beta-density scaling, or the standard gamma-ratio representation, shows \(W_m\Rightarrow Y\sim\mathrm{Gamma}(d,1)\) and \(V_m\to1\) in probability. More importantly, for each fixed \(q\ge0\),
\[
\mathbb E W_m^q=m^q\frac{\Gamma(d+q)\Gamma(m+d)}{\Gamma(d)\Gamma(m+d+q)}
\]
is bounded uniformly for \(m\ge1\). Thus, for every fixed \(u\ge0\),
\[
m^{d-1}F_{m,d}(1-u/m)=\mathbb E[uV_m+W_m]^{d-1}\longrightarrow Q_d(u):=\mathbb E(u+Y)^{d-1}.
\]
Uniform moment bounds imply \(0\le m^{d-1}F_{m,d}(1-u/m)\le C_d(1+u)^{d-1}\) whenever \(0\le u\le m\). This justifies the next dominated-convergence step even though \(d\) is half-integral.

**3. Full norm and compact-subball mass.** Change variables \(u=m(1-t)\) in the full radial squared norm. Its value, *before normalization*, is
\[
\begin{aligned}
J_m&=\int_0^1 t^{m+d-1}(1-t)^\alpha F_{m,d}(t)^2dt\\
&=m^{-(\alpha+2d-1)}\int_0^m(1-u/m)^{m+d-1}u^\alpha
\bigl(m^{d-1}F_{m,d}(1-u/m)\bigr)^2du.
\end{aligned}
\]
Since \((1-u/m)^{m+d-1}\le e^{-u}\), the integrand is bounded by \(C e^{-u}u^\alpha(1+u)^{2d-2}\), integrable for \(\alpha>-1\). Therefore
\[J_m\sim I_{\alpha,d}\,m^{-(\alpha+2d-1)}.\]
For fixed \(T<1\), the beta expectation gives \(F_{m,d}(t)\to(1-t)^{d-1}\) uniformly on \([0,T]\). One-sided endpoint Laplace asymptotics give
\[
\int_0^T t^{m+d-1}(1-t)^\alpha F_{m,d}(t)^2dt
\sim\frac{T^{m+d}(1-T)^{\alpha+2d-2}}{m}.
\]
Dividing proves the asserted \(\Lambda_m^H\). The beta-function asymptotic \(B(m+d,\alpha+1)\sim\Gamma(\alpha+1)m^{-\alpha-1}\), together with the same endpoint estimate for the constant factor, proves \(\Lambda_m^E\) and the ratio.

**4. The logarithmic count and subtraction.** Let \(\lambda_m=Cm^pT^m(1+o(1))\), where \(C>0\). Its logarithm is \(-am+p\log m+\log C+o(1)\), and hence \(\lambda_{m+1}/\lambda_m\to T<1\). Apart from finitely many initial degrees, the eigenvalues are strictly decreasing. The last degree with \(\lambda_m>e^{-L}\) equals
\[
K(L)=\frac L a+\frac p a\log L+O(1).
\]
Using \(h_{m,n}=2m^{n-2}/(n-2)!+O(m^{n-3})\) and summation,
\[
\sum_{m\le K}h_{m,n}=\frac{2K^{n-1}}{(n-1)!}+O(K^{n-2}).
\]
Consequently, uniformly for fixed parameters,
\[
N_p(e^{-L})=\frac{2L^{n-1}}{(n-1)!a^{n-1}}+
\frac{2pL^{n-2}\log L}{(n-2)!a^{n-1}}+O(L^{n-2}).
\]
For the hyperbolic and Euclidean operators, respectively, \(p_H=\alpha+n-2\) and \(p_E=\alpha\). Subtracting the two expansions proves the displayed spectral excess. No finite experiment is used to infer an infinite limit.

## Verification

The proof above verifies all exponents, normalization cancellations, moment bounds and boundary cases \(n\ge3\), \(\alpha>-1\), \(T\in(0,1)\). The attached standalone `CHECK.py` reproduces 98 finite checks using SciPy and NumPy, including exact spherical-harmonic dimension identities and supplementary nonpolynomial hypergeometric quadrature at odd dimensions \(3\) and \(5\). It also checks the \(d=2\) integer-shape benchmark \(I_{0,2}=10\) solely to sanity-check the integral normalization. These finite tests are not a proof of the asymptotic theorem.

## Relationship to prior work

Üreyen's 2022 hyperbolic-harmonic Bergman-projection study supplies the all-dimensional radial hypergeometric basis and estimates for its reproducing-kernel coefficients, but does not state the compact-subball eigenvalue asymptotics, the odd-dimensional beta-to-gamma limit used above, or the precise Euclidean comparison of spectral counts. Üreyen's 2023 study gives atomic decomposition, interpolation and inclusions, rather than this spectral comparison. Stoll's 2019 analysis concerns the hyperbolic-harmonic Hardy reproducing kernel and radial Laplacian eigenfunctions, not weighted Bergman concentration spectral counting. A related four-real-dimensional computation can be made from the terminating hypergeometric case; the present odd-dimensional theorem does **not** claim that special case as new and deals with genuinely nonterminating hypergeometric functions. Earlier general spectral-counting results may still imply part of the theorem indirectly; historical priority is not independently certified.

## Limitations

The theorem gives the leading eigenvalue constants and first nontrivial difference of counting functions, not lower-order constant terms, uniform estimates under variable \(n\), \(\alpha\) or \(T\), or a closed form of \(I_{\alpha,d}\) for all half-integer \(d\). The spectral comparison concerns radial indicator compressions only. The displayed counting remainder is an asymptotic \(O\)-bound with fixed parameters. An independent audit and independent validation have not been performed.

## References

1. A. E. Üreyen, *\(\mathcal H\)-Harmonic Bergman Projection on the Hyperbolic Ball*, arXiv:2207.13140v1, first public 2022-07-26. https://arxiv.org/html/2207.13140v1
2. A. E. Üreyen, *Harmonic Bergman Spaces on the Real Hyperbolic Ball: Atomic Decomposition, Interpolation and Inclusion Relations*, arXiv:2303.12137v1, first public 2023-03-21. https://arxiv.org/abs/2303.12137
3. M. Stoll, *The reproducing kernel of \(\mathcal H^2\) and radial eigenfunctions of the hyperbolic Laplacian*, Mathematica Scandinavica **124** (2019), 81–101, DOI:10.7146/math.scand.a-109674. https://journals.msp.org/mscand/article/download/248/247/275
