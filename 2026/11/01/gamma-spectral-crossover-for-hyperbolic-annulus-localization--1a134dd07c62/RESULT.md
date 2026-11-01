# Gamma spectral crossover for hyperbolic annulus localization

## Finding
For the positive characteristic-function Toeplitz operator on a single annulus in normalized power-weighted analytic Bergman space, the maximal monomial mode has an exact twofold-degeneracy criterion. As the annulus escapes to the boundary, its entire spectral profile admits two universal gamma limits: a thin-annulus profile with explicit sharp operator norm and all positive Schatten-moment constants, and a finite relative-width crossover with an explicit maximizing mode.

Specifically, fix \(p>0\). Let \(A_p^2(\mathbb D)\) have area measure \(d\mu_p(z)=p\pi^{-1}(1-|z|^2)^{p-1}\,dA(z)\), and let \(P_p\) be the corresponding orthogonal projection. For \(S,L>0\), put
\[
\Omega_{S,L}=\left\{z\in\mathbb D:S<\frac{|z|^2}{1-|z|^2}<S+L\right\},\qquad T_{S,L}=P_p M_{\mathbf1_{\Omega_{S,L}}}\big|_{A_p^2}.
\]
This positive trace-class operator has diagonal eigenvalues \(\lambda_k(S,L)\), indexed by \(k\ge0\), and exactly
\[
\lambda_k=\int_S^{S+L}\frac{\Gamma(k+p+1)}{\Gamma(k+1)\Gamma(p)}\frac{t^k}{(1+t)^{k+p+1}}\,dt,\qquad \operatorname{Tr}T_{S,L}=pL.
\]
Set
\[
H_{p,S,L}=\frac{p\log((1+S+L)/(1+S))}{\log((S+L)(1+S)/(S(1+S+L)))}.
\]
When \(H_{p,S,L}\notin\mathbb N\), the unique norm-maximizing mode has degree \(\lfloor H_{p,S,L}\rfloor\); if \(H_{p,S,L}=m\in\mathbb N\), precisely degrees \(m-1\) and \(m\) share the largest eigenvalue. No other modes maximize it.

For any family with \(S\to\infty\) and \(L=L(S)>0\) satisfying \(L/S\to0\), define \(h_p(c)=c^p e^{-c}/\Gamma(p)\) on \(c\ge0\). Then
\[
\frac S L\lambda_{\lfloor cS\rfloor}\longrightarrow h_p(c)
\]
uniformly for \(c\) in compact intervals, and for every fixed real \(q>0\),
\[
\lim_{S\to\infty}\frac{S^{q-1}}{L^q}\operatorname{Tr}(T_{S,L}^q)
=\frac{\Gamma(pq+1)}{q^{pq+1}\Gamma(p)^q},\quad
\lim_{S\to\infty}\frac S L\|T_{S,L}\|=\frac{p^p e^{-p}}{\Gamma(p)},\quad
\frac{k_{\rm peak}}S\to p.
\]
Here \(k_{\rm peak}\) denotes any maximizing index, including either of the two at a resonance.

For any family \(S\to\infty\) with \(L/S\to\rho\in(0,\infty)\), put
\[
F_{p,\rho}(c)=\frac1{\Gamma(p)}\int_{c/(1+\rho)}^{c}x^{p-1}e^{-x}\,dx\quad(c\ge0),\qquad
c_{p,\rho}=\frac{p(1+\rho)}{\rho}\log(1+\rho).
\]
Then \(\lambda_{\lfloor cS\rfloor}\to F_{p,\rho}(c)\) uniformly on compact \(c\)-intervals, and for every fixed \(q>0\),
\[
\frac1S\operatorname{Tr}(T_{S,L}^q)\to\int_0^\infty F_{p,\rho}(c)^q\,dc,\qquad
\|T_{S,L}\|\to F_{p,\rho}(c_{p,\rho}),\qquad
\frac{k_{\rm peak}}S\to c_{p,\rho}.
\]
The scalar profile \(F_{p,\rho}\) has a unique positive maximum at \(c_{p,\rho}\). All displayed Schatten trace identities concern powers of this positive compact operator.

## Assumptions and scope
The weight exponent \(p\) and Schatten exponent \(q\) are fixed strictly positive real numbers. The annulus is centered at the origin and specified in the hyperbolic area coordinate \(t=|z|^2/(1-|z|^2)\). Both endpoints are finite for every individual operator. Thin and macroscopic limits are statements for arbitrary positive functions \(L(S)\) with the specified ratio limits, not only integer \(S\) or constant \(L\). The convergence and all constants depend on the stated normalization.

## Proof
**1. Diagonal spectrum and trace.** The orthonormal monomial basis is \(e_k(z)=[\Gamma(k+p+1)/(\Gamma(p+1)k!)]^{1/2}z^k\). Angular orthogonality makes the radial Toeplitz operator diagonal. With \(u=|z|^2\) and \(t=u/(1-u)\), the radial mass of \(|e_k|^2\) becomes the beta-prime density
\[
g_{p,k}(t)=\frac1{B(k+1,p)}\frac{t^k}{(1+t)^{k+p+1}}.
\]
The diagonal formula follows. The binomial series gives, for every \(t>0\),
\[
\sum_{k\ge0}g_{p,k}(t)
=\frac p{(1+t)^{p+1}}\sum_{k\ge0}\frac{(p+1)_k}{k!}\left(\frac t{1+t}\right)^k=p.
\]
Monotone convergence therefore gives \(\sum_k\lambda_k=pL\), also proving positivity and trace class.

**2. Exact maximizing degrees.** Write \(u=S/(1+S)\) and \(v=(S+L)/(1+S+L)\), so \(0<u<v<1\) and \(\lambda_k=I_v(k+1,p)-I_u(k+1,p)\), where \(I_x\) is the regularized incomplete beta function. Integration by parts or the incomplete-beta recurrence gives
\[
\lambda_{k+1}-\lambda_k=
\frac{u^{k+1}(1-u)^p-v^{k+1}(1-v)^p}{(k+1)B(k+1,p)}.
\]
The numerator is positive exactly when \(k+1<H_{p,S,L}\), zero exactly when \(k+1=H_{p,S,L}\), and negative exactly when \(k+1>H_{p,S,L}\). This proves the complete strict-unimodality and top-multiplicity alternatives; there are no other ties at the maximum.

**3. Common integrable envelope.** For fixed \(p>0\), the gamma-ratio estimate \(\Gamma(k+p+1)/\Gamma(k+1)\le C_p(k+1)^p\) holds for all integer \(k\ge0\). When \(S\ge1\) and \(0<L/S\le R\) for fixed \(R\), the elementary inequality \(\log(1+1/t)\ge1/(1+t)\) shows, uniformly for \(t\in[S,S+L]\),
\[
g_{p,k}(t)\le \frac{C_{p,R}}{S}\left(1+\frac{k}{S}\right)^p e^{-k/((2+R)S)}.
\]
Consequently \(\lambda_k\le C_{p,R}(L/S)(1+k/S)^p e^{-k/((2+R)S)}\), with a constant independent of \(S,L,k\). This integrable majorant persists after raising to any fixed \(q>0\). In particular the mass of modes \(k>AS\), in the Riemann-sum normalizations below, tends uniformly to zero as \(A\to\infty\).

**4. Thin boundary layer.** If \(L/S\to0\), then \(t/S\to1\) uniformly on \([S,S+L]\). If \(k/S\to c>0\), Stirling's gamma-ratio limit and the elementary exponential limit give
\[
Sg_{p,k}(t)\to c^p e^{-c}/\Gamma(p)\quad\text{uniformly for }t\in[S,S+L].
\]
The same convergence at \(c=0\) follows by the uniform bound \(Sg_{p,k}(t)\le C_p((k+1)/S)^p\) when \(k/S\to0\). Compact-uniform convergence follows by the same uniform estimates. Integrating and dividing by \(L\) proves \((S/L)\lambda_{\lfloor cS\rfloor}\to h_p(c)\). The envelope in step 3 yields convergence of every normalized positive Schatten trace by a Riemann sum:
\[
\frac{S^{q-1}}{L^q}\sum_k\lambda_k^q\to\int_0^\infty h_p(c)^qdc
=\frac{\Gamma(pq+1)}{q^{pq+1}\Gamma(p)^q}.
\]
As \(h_p\) has its unique maximum at \(c=p\), the envelope and compact convergence also yield the norm and maximizing-index limits; alternatively the latter follows directly from the exact formula for \(H_{p,S,L}\).

**5. Finite relative width.** If \(L/S\to\rho\in(0,\infty)\), for sequences \(k/S\to c>0\) and \(t/S\to y\in[1,1+\rho]\), Stirling gives \(Sg_{p,k}(t)\to c^p y^{-p-1}e^{-c/y}/\Gamma(p)\). Thus
\[
\lambda_{\lfloor cS\rfloor}\to\frac{c^p}{\Gamma(p)}\int_1^{1+\rho}y^{-p-1}e^{-c/y}dy
=\frac1{\Gamma(p)}\int_{c/(1+\rho)}^{c}x^{p-1}e^{-x}dx.
\]
The compact convergence includes \(c=0\) by step 3 and the small-degree estimate. The same integrable envelope gives all positive-power trace limits. Differentiating the profile yields
\[
F_{p,\rho}'(c)=\frac{c^{p-1}}{\Gamma(p)}\left[e^{-c}-(1+\rho)^{-p}e^{-c/(1+\rho)}\right],\qquad c>0.
\]
Its bracket changes sign exactly once, from positive to negative, at \(c=c_{p,\rho}\). Uniform convergence on compact sets and the envelope establish the norm and maximizing-index limits. This completes the proof.

## Verification
The standalone `check_escape_wavelet.py` runs 152 supplementary numerical assertions using NumPy and SciPy (requirements listed in `requirements.txt`): finite-spectrum positivity, exact-mode maximization, truncated trace normalization, thin and macroscopic norm laws, Hilbert–Schmidt constants, and positive fractional/integer Schatten-power Riemann-sum limits. The numerical tests are supporting finite checks; the infinite claims use the analytic arguments above. In particular, truncating the eigenvalue sum is not the trace-class proof.

For \(p=1\), \(L/S\to0\) gives \(\|T_{S,L}\|\sim L/(eS)\) and \(\|T_{S,L}\|_{\mathcal S_2}^2\sim L^2/(4S)\). When \(L/S\to1\), the limiting norm is \(1/4\). These independently calculable special cases corroborate the constants.

## Relationship to prior work
Abreu, Mouayn and Voigtlaender [1] derive the beta-prime diagonal spectrum for hyperbolically defined Cantor annuli and bound their localization norms. The present result uses that spectral representation for a *single* annulus but establishes the additional exact peak multiplicity criterion, two escaping-annulus scaling regimes, full gamma spectral profiles, and all positive Schatten-power constants. Nicola and Tilli [2] and Ramos and Tilli [3] prove optimal bounds and disk extremizers for wavelet concentration under mass constraints; these inequalities do not determine the spectral distribution or peak degree for an escaping annulus. Nicola and Riccardi [4] prove wavelet Hilbert–Schmidt rearrangement inequalities, rather than the annulus-specific asymptotic identities here. Priority for indirect derivations from more general spectral theory has not been independently audited.

## Limitations
The calculation is for one centered radial annulus, not a Cantor union or arbitrary nonradial region. It does not claim an optimal annulus among all regions of given hyperbolic area. The exponent \(p\) is fixed as \(S\to\infty\), and the results exclude relative widths diverging to infinity. The \(O\)-rates of convergence are not optimized or asserted. Noninteger Schatten exponents are positive powers of a compact positive operator, not operator ideals for all exponents. The result is supported by a self-review, not by independent external verification.

## References
[1] L. D. Abreu, Z. Mouayn, F. Voigtlaender, *A fractal uncertainty principle for Bergman spaces and analytic wavelets*, arXiv:2201.11705 (first public 2022-01-27); Journal of Mathematical Analysis and Applications 519 (2023), 126699. https://arxiv.org/abs/2201.11705

[2] F. Nicola, P. Tilli, *The norm of time-frequency and wavelet localization operators*, arXiv:2207.08624 (2022); Transactions of the American Mathematical Society 376 (2023), 7353–7375. https://arxiv.org/abs/2207.08624

[3] J. P. G. Ramos, P. Tilli, *A Faber–Krahn inequality for wavelet transforms*, Bulletin of the London Mathematical Society 55 (2023), 2018–2034. https://doi.org/10.1112/blms.12833

[4] F. Nicola, F. Riccardi, *The quantitative isoperimetric inequality for the Hilbert–Schmidt norm of localization operators*, arXiv:2401.04659 (2024); Journal of Fourier Analysis and Applications 31 (2025), article 12. https://arxiv.org/abs/2401.04659
