# Sharp small-deviation exponent for three-line correlated Brownian last passage

## Finding
Let \(B=(B_1,B_2,B_3)\) be a centered three-dimensional Brownian motion with covariance \(\operatorname{Cov}(B(s),B(t))=(s\wedge t)\Sigma\), where \(\Sigma\) is symmetric positive semidefinite and \(\Sigma\mathbf 1=0\). Put \(X_1=B_1-B_2\) and \(X_2=B_2-B_3\), and assume their time-one covariance matrix \(C\) is positive definite. Set
\[
F=B_3(1)+\sup_{0\le s\le t\le1}\{X_1(s)+X_2(t)\},\qquad
\rho=\frac{C_{12}}{\sqrt{C_{11}C_{22}}},\qquad
\kappa(C)=2+\frac{2\pi}{\arccos(-\rho)}.
\]
Then, for every such fixed \(C\), there exist \(0<c_C\le C_C<\infty\) and \(\varepsilon_0(C)>0\) such that
\[
c_C\varepsilon^{\kappa(C)}\le
\mathbb P(F\le\varepsilon)\le
C_C\varepsilon^{\kappa(C)}
\quad\text{for all }0<\varepsilon<\varepsilon_0(C).
\]
In particular, the sharp logarithmic lower-tail exponent exists:
\[
\lim_{\varepsilon\downarrow0}
\frac{\log\mathbb P(F\le\varepsilon)}{\log\varepsilon}
=2+\frac{2\pi}{\arccos(-\rho)}.
\]
This is a two-sided power law, **not** an assertion that the normalized probability converges to a particular constant. For the three-state Markov-chain covariance in Example 5.4 of Houdré--Kidonakis (2026), \(C=\frac19\bigl(\begin{smallmatrix}14&-13\\-13&14\end{smallmatrix}\bigr)\), it gives
\[
\kappa(C)=2+\frac{2\pi}{\arccos(13/14)}
=18.523774800939642819\ldots.
\]
The exponent equals \(8\) at the cyclic/isotropic boundary \(\rho=-1/2\), rises above \(8\) for \(\rho<-1/2\), and is less than \(8\) for \(\rho>-1/2\). The covariance and exponent for the explicit Markov chain were already identified as an **upper-bound exponent** in the motivating paper; the new assertion is that the upper power is sharp and is valid for every nondegenerate three-line covariance.

## Assumptions and scope
All Brownian motions start at zero and have continuous paths. The time-one increment covariance is
\[
C=\begin{pmatrix}
\mathbb E[X_1(1)^2]&\mathbb E[X_1(1)X_2(1)]\\
\mathbb E[X_1(1)X_2(1)]&\mathbb E[X_2(1)^2]
\end{pmatrix}\succ0.
\]
The condition \(\Sigma\mathbf1=0\) implies \(B_1(t)+B_2(t)+B_3(t)=0\) almost surely for every \(t\). Conversely, any positive-definite \(C\) determines a centered rank-two Brownian motion through the invertible difference coordinates on this hyperplane. Thus \(-1<\rho<1\) always holds. All constants are allowed to depend on the fixed covariance; no uniformity is asserted as \(\rho\) approaches either endpoint.

## Proof
**1. Necessary endpoint and path constraints.** The three choices \((s,t)=(0,0),(0,1),(1,1)\) in the definition of \(F\) give \(F\ge B_j(1)\) for each \(j=1,2,3\). Since their sum is zero, \(F\ge0\), and on \(\{F\le\varepsilon\}\) each terminal coordinate lies in \([-2\varepsilon,\varepsilon]\). Consequently,
\[
-3\varepsilon\le X_j(1)\le3\varepsilon,\qquad j=1,2.
\]
For every \(u\in[0,1]\), selecting \((s,t)=(u,1)\) gives \(F\ge B_2(1)+X_1(u)\); selecting \((s,t)=(0,u)\) gives \(F\ge B_3(1)+X_2(u)\). It follows that
\[
\{F\le\varepsilon\}\subseteq
\{\sup_{0\le u\le1}X_1(u)\le3\varepsilon,\ 
\sup_{0\le u\le1}X_2(u)\le3\varepsilon,\ 
X(1)\in[-3\varepsilon,3\varepsilon]^2\}.
\tag{1}
\]

**2. Sufficient smaller confinement event.** For \(\delta>0\), let
\[
E_\delta=\{\sup_{u\in[0,1]}X_1(u)<\delta,\ 
\sup_{u\in[0,1]}X_2(u)<\delta,\ 
0<X_1(1)<\delta/2,\ 0<X_2(1)<\delta/2\}.
\]
Because \(\Sigma\mathbf1=0\), the terminal third coordinate equals \(B_3(1)=-(X_1(1)+2X_2(1))/3\). Therefore \(B_3(1)<0\) on \(E_\delta\), and
\[
F\le B_3(1)+\sup X_1+\sup X_2<2\delta.
\]
Hence \(E_{\varepsilon/2}\subseteq\{F\le\varepsilon\}\). This **positive-area terminal confinement inside a strict wedge** is the ingredient that makes the cone upper bound sharp.

**3. Whitening identifies the wedge.** Let \(A=C^{-1/2}\), its positive-definite symmetric square root inverse, and write
\[
\mathcal W=A(0,\infty)^2,\quad a=A(1,1)^\top\in\mathcal W,\quad
Z_\delta(t)=A(\delta(1,1)^\top-X(t)).
\]
Then \(Z_\delta\) is a standard planar Brownian motion started at \(\delta a\). The requirement \(X_1(t)<\delta\) and \(X_2(t)<\delta\) throughout \([0,1]\) is precisely survival of \(Z_\delta\) in \(\mathcal W\). The two boundary rays are columns of \(A\). Since the normalized off-diagonal entry of \(C^{-1}\) is \(-\rho\), their opening angle is
\[
\theta=\arccos(-\rho)\in(0,\pi),\qquad \beta=\pi/\theta.
\]
The lower event from step 2 becomes
\[
\mathbb P(E_\delta)
=\mathbb P_{\delta a}\bigl(\tau_{\mathcal W}>1,\ Z(1)\in\delta K\bigr),
\quad K=A([1/2,1]\times[1/2,1]),
\tag{2}
\]
where \(K\) has strictly positive area and is compactly contained in \(\mathcal W\). Boundary choices in the terminal rectangle do not affect the probability.

**4. A two-point small-start/endpoint wedge lemma.** For an open planar wedge \(\mathcal W\) of angle \(\theta\in(0,\pi)\), any point \(a\) in its interior, and a compact positive-area set \(K\) in its interior,
\[
\mathbb P_{\delta a}(\tau_{\mathcal W}>1,Z(1)\in\delta K)
=\delta^{2+2\beta}\bigl(J(a,K)+o(1)\bigr),
\quad J(a,K)>0,
\quad\beta=\pi/\theta.
\tag{3}
\]
Furthermore, for any bounded Borel terminal set \(M\subset\mathbb R^2\),
\[
\mathbb P_{\delta a}(\tau_{\mathcal W}>1,Z(1)\in\delta M)
=O_{a,M}(\delta^{2+2\beta}).
\tag{4}
\]
For completeness, here is the precise kernel justification. Use polar coordinates \((r,\varphi)\) with \(0<\varphi<\theta\). The killed Brownian transition density at time one is
\[
p_{\mathcal W}(1;r,\varphi;r',\varphi')
=\frac2\theta e^{-(r^2+(r')^2)/2}
\sum_{n=1}^{\infty}
\sin(n\beta\varphi)\sin(n\beta\varphi') I_{n\beta}(rr'),
\tag{5}
\]
where \(I_\nu(z)=\sum_{k\ge0}(z/2)^{\nu+2k}/(k!\Gamma(k+\nu+1))\). For \(r=\delta|a|\), \(r'=\delta|b|\), and bounded \(b\) in the wedge, this absolutely convergent series has, uniformly in \(b\) on bounded sets, leading term
\[
p_{\mathcal W}(1;\delta a,\delta b)
=\delta^{2\beta}
\left(\frac{2^{1-\beta}}{\theta\Gamma(\beta+1)}
 h(a)h(b)+o(1)\right),
\qquad
h(v)=|v|^{\beta}\sin(\beta\varphi_v).
\tag{6}
\]
The \(n\ge2\) terms contribute higher powers \(\delta^{4\beta}\) or smaller, and the next term in \(I_\beta\) contributes \(\delta^{2\beta+4}\); the Gaussian factor is \(1+O(\delta^2)\). These controls are uniform on each bounded terminal region. The function \(h\) is strictly positive in the interior, nonnegative up to the wedge walls. Changing variables \(y=\delta b\), with \(dy=\delta^2db\), proves both (3) and (4), with the explicit positive coefficient
\[
J(a,K)=\frac{2^{1-\beta}}{\theta\Gamma(\beta+1)}
 h(a)\int_Kh(b)\,db>0.
\]
This is the standard Dirichlet wedge heat-kernel expansion, spelled out to show that the lower coefficient is positive. Path survival in a closed wedge differs from survival in its interior by a null event, using immediate boundary crossing and absolute continuity of Brownian endpoints.

**5. Apply the same wedge at the two endpoint scales.** For the lower bound, combine (2)--(3) with \(\delta=\varepsilon/2\):
\[
\mathbb P(F\le\varepsilon)\ge
\mathbb P(E_{\varepsilon/2})
=2^{-(2+2\beta)}J(a,K)\varepsilon^{2+2\beta}(1+o(1)).
\]
For the upper bound, (1) shows that \(Z_{3\varepsilon}\) stays in the closed wedge and finishes in \(\varepsilon A[0,6]^2=(3\varepsilon)M\) for the fixed bounded set \(M=A[0,2]^2\). Applying (4) to \(\delta=3\varepsilon\) yields the upper bound \(O(\varepsilon^{2+2\beta})\). The exponent \(2+2\beta\) equals \(\kappa(C)\), completing the proof. Taking logarithms of the positive two-sided bounds gives the asserted logarithmic limit.

## Verification
The accompanying standalone file `verify_small_ball.py` can be run with Python, SymPy and mpmath. It checks, using exact rational arithmetic, the covariance calculation for the motivating explicit Markov chain and the nonzero incremental covariance. It separately checks 700 deterministic finite-grid path inclusions and endpoint inequalities, 15 high-precision positive/leading-coefficient comparisons for the Bessel wedge kernel, and the boundary exponent \(8\). The reported example value is \(18.523774800939642819\ldots\). Grid paths and small-argument evaluations corroborate the derivations but do **not** prove the continuous-path or infinite-series assertions; those are established in steps 1--5.

## Relationship to prior work
Houdré and Kidonakis, *Markovian Random Words, a Gaussian Random Matrix Model and Beyond*, arXiv:2610.12950v1 (submitted 2026-10-09), Theorem 5.3, prove the **one-sided upper estimate** \(O(\varepsilon^{2+2\pi/\arccos(-\rho)})\) for \(-1<\rho<-1/2\) and deduce a Gaussian-Hermitian nonrepresentation result. Their Lemma 5.1 supplies a general cone upper estimate. Example 5.4 provides the explicit chain and covariance reused here, and Remark 5.5 notes the critical exponent \(8\). The present statement identifies the matching **lower** power, proves sharpness, and extends the exponent identity to **all** \(-1<\rho<1\). It does not claim novelty for the limiting Brownian functional, Markov-chain covariance, heat-kernel expansion, or the prior nonrepresentation result.

Houdré and Litherland, *On the Limiting Shape of Young Diagrams Associated With Markov Random Words*, arXiv:1110.4570, provide foundational Brownian functional limits for Markov random words, but do not establish this two-sided small-deviation exponent. Bañuelos and Smits, *Brownian Motion in Cones*, Probability Theory and Related Fields 108 (1997), 299--319, supply the underlying cone Dirichlet heat-kernel tools; those concern wedge events, rather than the last-passage event, for which steps 1 and 2 prove the necessary and sufficient comparisons.

## Limitations
The result is for exactly three centered Brownian coordinates, with positive-definite covariance of their two successive differences. It provides a sharp exponent and positive finite two-sided constants; it does not identify an exact asymptotic prefactor or exclude possible normalized oscillations. It does not claim finite-sample uniform estimates for the corresponding Markov-word longest increasing subsequence, nor extensions to singular difference covariance, more than three letters, or covariances without the zero-sum condition. Its bibliographic novelty assessment is limited by indexing and alternative equivalent formulations; independent scholarly verification has not been performed.

## References
1. C. Houdré and D. Kidonakis, *Markovian Random Words, a Gaussian Random Matrix Model and Beyond*, arXiv:2610.12950v1, first submitted 2026-10-09. https://arxiv.org/html/2610.12950v1 . Relevant items: Lemma 5.1; Theorem 5.3; Example 5.4; Remark 5.5.
2. C. Houdré and T. J. Litherland, *On the Limiting Shape of Young Diagrams Associated With Markov Random Words*, arXiv:1110.4570. https://arxiv.org/html/1110.4570v4 .
3. R. Bañuelos and R. G. Smits, *Brownian Motion in Cones*, Probab. Theory Relat. Fields **108** (1997), 299--319. https://doi.org/10.1007/s004400050111 .
4. M. Chupeau, O. Bénichou, and S. N. Majumdar, *Survival probability of a Brownian motion in a planar wedge of arbitrary angle*, Phys. Rev. E **91** (2015), 032106. https://doi.org/10.1103/PhysRevE.91.032106 .
