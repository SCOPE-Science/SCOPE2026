# Trace-norm Carleman scaling and an Euler rank-one correction for gamma-weighted Helson matrices

## Finding
For real \(\beta>1\) and \(q\ge1\), define the positive Helson operator \(R_{q,\beta}\) on \(\ell^2(\mathbb N)\) by
\[
(R_{q,\beta})_{mn}=\frac{\Gamma(\beta)}{\sqrt{mn}\,(q+\log(mn))^{\beta}},\qquad m,n\ge1.
\]
On \(L^2(0,\infty)\), put
\[
a_\beta(x)=x^{(\beta-1)/2}e^{-x/2},\qquad
K_\beta(x,y)=\frac{a_\beta(x)a_\beta(y)}{x+y},\qquad
P_\beta=|a_\beta\rangle\langle a_\beta|.
\]
Let \(S_{q,\beta}\) have integral kernel
\[
S_{q,\beta}(x,y)=\frac{a_\beta(x)a_\beta(y)}q\zeta\!\left(1+\frac{x+y}q\right).
\]
These are positive trace-class operators, and the nonzero eigenvalues of \(S_{q,\beta}\), counted with multiplicities, equal those of \(q^{\beta-1}R_{q,\beta}\). Writing \(\gamma\) for the Euler–Mascheroni constant, the precise trace-norm expansion is
\[
\boxed{\left\|S_{q,\beta}-K_\beta-\frac{\gamma}qP_\beta\right\|_{\mathcal S_1}
\le\frac{8\sqrt{\Gamma(\beta)\Gamma(\beta+2)}}{q^2}.}
\]
In particular, with nonincreasing eigenvalues and zeros inserted if needed,
\[
\sum_{j\ge1}\left|\lambda_j(q^{\beta-1}R_{q,\beta})-\lambda_j(K_\beta)\right|
\le \frac{\Gamma(\beta)}q\sqrt{\frac{\beta+1}\beta}.
\]
The trace and the sharp trace-norm first-order limit satisfy
\[
q^{\beta-1}\operatorname{Tr}R_{q,\beta}
=\frac{\Gamma(\beta-1)}2+\frac{\gamma\Gamma(\beta)}q+O_\beta(q^{-2}),
\qquad
\lim_{q\to\infty}q\|S_{q,\beta}-K_\beta\|_{\mathcal S_1}=\gamma\Gamma(\beta).
\]
The top eigenvalue of \(K_\beta\) is simple. With its positive normalized eigenvector \(\phi_\beta\),
\[
\lambda_1(q^{\beta-1}R_{q,\beta})
=\lambda_1(K_\beta)+\frac{\gamma|\langle a_\beta,\phi_\beta\rangle|^2}q+O_\beta(q^{-2}),
\]
and the displayed first-order coefficient is strictly positive.

## Assumptions and scope
All Hilbert spaces are complex, with their standard \(L^2\) or \(\ell^2\) inner products. The parameter \(q\) is real and at least one; \(\beta\) is real and strictly greater than one. Here \(\zeta\) is the Riemann zeta function on its real half-line of absolute convergence, \(\Gamma\) the gamma function, and \(\mathcal S_1\) the trace-class ideal. The statement concerns the complete nonzero spectrum, not convergence of individual eigenvectors under an asserted unitary equivalence between the two original spaces.

## Proof
**1. Moment factorization and nuclearity.** On \((0,\infty)\), let \(d\mu_{q,\beta}(u)=u^{\beta-1}e^{-qu}du\). For a finite sequence \(c\), define
\[
(N_qc)(u)=\sum_{n\ge1}c_n n^{-1/2-u}.
\]
The Laplace–gamma identity gives
\[
\langle N_qe_m,N_qe_n\rangle_{L^2(\mu_{q,\beta})}
=\frac{\Gamma(\beta)}{\sqrt{mn}(q+\log(mn))^\beta}.
\]
Moreover,
\[
\sum_{n\ge1}\|N_qe_n\|^2
=\Gamma(\beta)\sum_{n\ge1}\frac1{n(q+2\log n)^\beta}<\infty
\]
by the integral test because \(\beta>1\). Thus \(N_q\) extends to a Hilbert–Schmidt operator and \(R_{q,\beta}=N_q^*N_q\) is positive trace class. The companion \(N_qN_q^*\) on \(L^2(\mu_{q,\beta})\) has kernel \(\zeta(1+u+v)\) relative to that weighted measure. These two positive operators have identical nonzero eigenvalue lists, including multiplicities.

**2. Rescaling the exact companion.** The unitary map \(U_q:L^2(\mu_{q,\beta})\to L^2(0,\infty)\) defined by
\[
(U_qf)(x)=q^{-\beta/2}a_\beta(x)f(x/q)
\]
transforms \(q^{\beta-1}N_qN_q^*\) exactly into \(S_{q,\beta}\), whose kernel is the one displayed above. This proves the precise spectral correspondence.

**3. Rank-one integral representation.** For \(v\ge0\), set \(a_v(x)=a_\beta(x)e^{-vx}\) and \(F(v)=|a_v\rangle\langle a_v|\). All identities below hold as Bochner integrals in the trace-class ideal:
\[
S_{q,\beta}=\frac1q\sum_{n\ge1}\frac1nF\left(\frac{\log n}q\right),
\qquad
K_\beta=\int_0^\infty F(v)dv.
\]
Indeed, the first kernel is the Dirichlet series defining \(\zeta\), and the second uses \(\int_0^\infty e^{-v(x+y)}dv=1/(x+y)\). The nuclear integral converges because
\[
\|F(v)\|_{\mathcal S_1}=\|a_v\|_2^2
=\frac{\Gamma(\beta)}{(1+2v)^\beta},\qquad
\int_0^\infty\|F(v)\|_1dv=\frac{\Gamma(\beta-1)}2.
\]
The map \(F\) is trace-norm differentiable, with
\[
F'(v)=-|x a_v\rangle\langle a_v|-|a_v\rangle\langle x a_v|,
\quad
\|F'(v)\|_1\le\frac{2\sqrt{\Gamma(\beta)\Gamma(\beta+2)}}{(1+2v)^{\beta+1}}.
\]
Consequently \(F'\) is nuclear-integrable and \(\int_0^\infty F'(v)dv=-F(0)=-P_\beta\).

**4. Harmonic quadrature and the Euler term.** Write \(H_N=\sum_{n=1}^N1/n\), set \(N(v)=\lfloor e^{qv}\rfloor\), and put
\[
D_q(v)=\frac{H_{N(v)}}q-v,\qquad v\ge0.
\]
The elementary integral comparison for harmonic numbers gives \(0<D_q(v)\le1/q\). Stieltjes integration by parts for the discrete measure \(q^{-1}\sum_{n\ge1}n^{-1}\delta_{(\log n)/q}\) against Lebesgue measure yields
\[
S_{q,\beta}-K_\beta=-\int_0^\infty D_q(v)F'(v)dv.
\]
To capture the leading term, use \(0\le H_N-\log N-\gamma\le1/N\) and \(0\le qv-\log N(v)\le1/N(v)\). Since \(N(v)\ge e^{qv}/2\),
\[
|qD_q(v)-\gamma|\le\frac2{N(v)}\le4e^{-qv}.
\]
Therefore
\[
S_{q,\beta}-K_\beta-\frac{\gamma}qP_\beta
=-\frac1q\int_0^\infty(qD_q(v)-\gamma)F'(v)dv,
\]
and hence
\[
\left\|S_{q,\beta}-K_\beta-\frac{\gamma}qP_\beta\right\|_1
\le\frac4q\int_0^\infty e^{-qv}\|F'(v)\|_1dv
\le\frac{8\sqrt{\Gamma(\beta)\Gamma(\beta+2)}}{q^2}.
\]
Similarly \(\|S_{q,\beta}-K_\beta\|_1\le q^{-1}\int_0^\infty\|F'(v)\|_1dv=\Gamma(\beta)\sqrt{(\beta+1)/\beta}/q\).

**5. Spectral and trace consequences.** The trace norm eigenvalue perturbation inequality for positive compact operators gives the asserted \(\ell^1\) bound. Since \(\operatorname{Tr}K_\beta=\Gamma(\beta-1)/2\) and \(\operatorname{Tr}P_\beta=\Gamma(\beta)\), the displayed trace asymptotic follows. Trace-norm continuity and the rank-one limit \(q(S_{q,\beta}-K_\beta)\to\gamma P_\beta\) give the sharp trace-norm coefficient. The integral kernel of \(K_\beta\) is strictly positive almost everywhere. Thus a maximizer for its top Rayleigh quotient has a strictly positive representative; any sign-changing real vector in the top eigenspace would produce, on taking absolute values, a strictly larger Rayleigh quotient. Orthogonal real vectors in a multiple top eigenspace would force such a sign change. Hence the top eigenvalue is simple. Standard perturbation of an isolated simple eigenvalue, applied to the trace-norm expansion, gives the final eigenvalue formula. The coefficient is positive because \(a_\beta\) and \(\phi_\beta\) are strictly positive almost everywhere.

## Verification
Every displayed infinite-dimensional assertion follows from the Hilbert–Schmidt factorization, trace-norm Bochner integral identities, explicit harmonic-number inequalities, and a standard compact self-adjoint eigenvalue perturbation bound. The accompanying `check_numeric.py` evaluates an independent scalar trace integral at several \(q\) and \(\beta\) values, checking the convergence scale without using finite computations as proofs. The exact matrix-to-integral spectral correspondence and nuclear remainders are proved above rather than inferred from finite truncations.

## Relationship to prior work
Ma, Lu and Zu establish the general moment-factorization/trace-class framework and discuss the fixed-shift gamma-weighted family (their Example 3.6); they do not give the trace-norm large-shift spectral limit or an Euler-rank-one correction. Perfekt and Pushnitski establish a zeta-kernel representation for multiplicative Hilbert matrices and describe their noncompact \(\beta=1\) spectrum. Miheisi and Pushnitski prove qualitative Schatten-class comparisons between discrete and integral Helson operators and eigenvalue asymptotics for an unrelated fixed logarithmic-logarithmic decay profile; their qualitative weighted-Carleman correction does not imply the explicit uniform first-order nuclear expansion here. Brevig, Perfekt, Seip, Siskakis and Vukotić study the unweighted multiplicative Hilbert matrix. The new claim is the full nuclear spectral scaling and its explicit sharp leading correction, not those established representations or the trace-class criterion.

## Limitations
The result assumes fixed \(\beta>1\) and \(q\to\infty\). It does not classify the complete eigenvalues of the weighted Carleman limit in elementary closed form, prove the same nuclear expansion at the non-trace-class boundary \(\beta=1\), or establish uniformity as \(\beta\downarrow1\). It is not an independent external audit or a proof of absolute historical priority; equivalent results in unindexed literature remain possible.

## References
1. T. Ma, Y. Lu, and C. Zu, *Unbounded Helson Forms with a Moment Representation*, arXiv:2610.12252v1 (first posted 2026-10-08), especially Theorem 3.4 and Example 3.6.
2. K.-M. Perfekt and A. Pushnitski, *On the Spectrum of the Multiplicative Hilbert Matrix*, arXiv:1705.01959, especially Section 2.
3. N. Miheisi and A. Pushnitski, *A Helson Matrix with Explicit Eigenvalue Asymptotics*, arXiv:1709.06326v1, especially Sections 2–3.
4. O. F. Brevig, K.-M. Perfekt, K. Seip, A. G. Siskakis, and D. Vukotić, *The Multiplicative Hilbert Matrix*, arXiv:1411.7294.
