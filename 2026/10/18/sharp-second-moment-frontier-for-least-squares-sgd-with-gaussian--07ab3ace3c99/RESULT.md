# Sharp second-moment frontier for least-squares SGD with Gaussian autoregressive designs

## Finding
Consider scalar least-squares SGD with stationary Gaussian AR(1) covariates and independent observation noise. The exact mean-square stability frontier is the Perron eigenvalue of a specified selfadjoint Gaussian transfer operator. Positive temporal correlation strictly worsens the second-moment growth factor, and every step size stable under independent Gaussian samples has one unique correlation boundary. Near the independent-sampling ceiling, the boundary has an explicit quadratic expansion:
\[
s_c(\rho)=\frac23-\frac{16}{9}\rho^2+O(\rho^4)\qquad(\rho\downarrow0).
\]
This is a numerical stability statement for an ordinary stochastic least-squares optimization update; it is not a claim about a diffusion-limit approximation.

## Assumptions and scope
Let \(s>0\), \(\sigma>0\), and \(0\le\rho<1\). On a two-sided stationary probability space, define the scalar Gaussian AR(1) design
\[
U_{n+1}=\rho U_n+\sqrt{1-\rho^2}\,G_{n+1},\qquad U_n\sim N(0,1),
\]
where the innovations \(G_n\) are independent standard Gaussians. Let \(Z_n\) be independent centered variables of variance one, iid over time and independent of the entire design process. The observed least-squares responses are \(Y_n=\theta_*U_n+\sigma Z_n\). Standard constant-step least-squares SGD updates \(\theta_{n+1}=\theta_n+sU_n(Y_n-U_n\theta_n)\); the error \(e_n=\theta_n-\theta_*\) satisfies
\[
e_{n+1}=b_s(U_n)e_n+s\sigma U_nZ_n,\qquad b_s(x)=1-sx^2.
\]
All finite-history conclusions begin with deterministic \(e_0\) independent of the design and noise. A stationary square-integrable solution refers to a causal process coupled to the entire two-sided design and noise, not necessarily an independently Markovian iterate.

Write \(\gamma\) for the standard Gaussian law and let \(T_\rho\) be its reversible Markov operator on \(L^2(\gamma)\):
\[
(T_\rho f)(x)=\int f\!\left(\rho x+\sqrt{1-\rho^2}\,z\right)\gamma(dz).
\]
Put \(a_s(x)=|1-sx^2|\) and define \(B_{s,\rho}=M_{a_s}T_\rho M_{a_s}\), the selfadjoint positive compact operator on \(L^2(\gamma)\) with top eigenvalue \(\Lambda(s,\rho)=\|B_{s,\rho}\|\). The operator has a well-defined Hilbert–Schmidt kernel for every \(\rho<1\), despite the unbounded polynomial factors.

**Exact criterion.** The mean-square error is bounded uniformly in time, and the unique stationary causal solution has finite variance, precisely when \(\Lambda(s,\rho)<1\). If \(\Lambda=1\), the second moment of the iterates grows at least linearly; if \(\Lambda>1\), it grows exponentially, even with \(e_0=0\).

**Strict dependence penalty.** For every \(s>0\), \(\Lambda(s,\rho)\) is continuous and strictly increasing on \(0\le\rho<1\), with
\[
\Lambda(s,0)=1-2s+3s^2,\qquad\lim_{\rho\uparrow1}\Lambda(s,\rho)=+\infty.
\]
For each \(0<s<2/3\), there is thus exactly one \(\rho_c(s)\in(0,1)\) such that finite stationary variance holds for \(0\le\rho<\rho_c(s)\), with divergence at and above the boundary. No \(s\ge2/3\) permits finite stationary variance.

**Local step boundary.** In a neighborhood of \((s,\rho)=(2/3,0)\), the unique positive solution of \(\Lambda(s,\rho)=1\) is analytic as an even function of \(\rho\) and satisfies the expansion displayed above.

## Proof
Set \(m_s(x)=b_s(x)^2\), and for integers \(k\ge0\) write
\[
c_k=\mathbb E\prod_{j=0}^{k-1}m_s(U_j),\qquad d_k=\mathbb E\left[U_0^2\prod_{j=1}^{k}m_s(U_j)\right].
\]
Empty products are one; thus \(c_0=d_0=1\). Iterating SGD and conditioning on the independent centered \(Z_n\) gives the **exact finite-horizon identity**
\[
\mathbb E[e_n^2]=e_0^2c_n+s^2\sigma^2\sum_{k=0}^{n-1}d_k.
\]
Stationarity and time reversibility of the Gaussian AR(1) chain imply, for \(k\ge1\),
\[
c_k=\langle a_s,B_{s,\rho}^{k-1}a_s\rangle_{L^2(\gamma)},\qquad
 d_k=\langle a_sT_\rho(x\mapsto x^2),B_{s,\rho}^{k-1}a_s\rangle_{L^2(\gamma)}.
\]
Both are exact identities: use the Markov property to alternately insert \(T_\rho\) and multiplication by \(m_s\), and split every \(m_s\) as \(a_s\cdot a_s\). The operator is Hilbert–Schmidt because the Mehler kernel has Gaussian decay for each fixed \(\rho<1\), and multiplying it by a fixed polynomial in both variables preserves square integrability. Its kernel is strictly positive outside the two zero lines of \(a_s\). Compact positivity theory yields a simple strictly positive top eigenfunction \(v\) and a strict spectral gap. Consequently
\[
c_k\sim C_c\Lambda^{k-1},\qquad d_k\sim C_d\Lambda^{k-1}\quad(k\to\infty),
\]
with \(C_c=\langle a_s,v\rangle^2>0\) and \(C_d=\langle a_sT_\rho(x^2),v\rangle\langle v,a_s\rangle>0\). At \(\rho=0\) this is immediate from the rank-one operator \(T_0\). The exact finite-horizon identity now proves boundedness for \(\Lambda<1\), linear growth for \(\Lambda=1\), and exponential growth for \(\Lambda>1\). The convergent infinite causal noise series is a stationary \(L^2\) solution when \(\Lambda<1\); the same positive summands show no square-integrable causal stationary solution when \(\Lambda\ge1\).

For the strict correlation comparison, the orthonormal probabilists' Hermite basis \(h_j\) diagonalizes \(T_\rho\):
\[
T_\rho=\sum_{j\ge0}\rho^j|h_j\rangle\langle h_j|.
\]
For \(0\le\rho_1<\rho_2<1\), \(B_{s,\rho_2}-B_{s,\rho_1}\) is positive semidefinite. Evaluating on the normalized top eigenvector \(v_1\) of \(B_{s,\rho_1}\), strictness fails only if \(a_sv_1\) is Gaussian-almost-surely constant. A nonzero constant would force \(v_1\) to be proportional to \(1/|1-sx^2|\), which is not square integrable near either root of \(b_s\); the zero constant would force \(v_1=0\). Thus \(\Lambda(s,\rho_2)>\Lambda(s,\rho_1)\). The case \(\rho=0\) is the rank-one Gaussian expectation: \(\Lambda(s,0)=\int m_s\,d\gamma=1-2s+3s^2\). Strong convergence \(T_\rho f\to f\) as \(\rho\uparrow1\), tested on bounded compactly supported functions at arbitrarily large \(|x|\), forces \(\Lambda\to\infty\). Continuity follows from the Hilbert–Schmidt kernel, which depends continuously on \(\rho\) on compact subintervals of \([0,1)\).

For the local expansion, the simple top eigenpair at \(\rho=0\) is \(\Lambda(s,0)=\mu(s)=1-2s+3s^2\) with \(v_0=a_s/\sqrt{\mu(s)}\). Its first-order perturbation vanishes by parity. Moreover, the first-order Hermite perturbation operator annihilates \(v_0\), so the only order-\(\rho^2\) contribution comes from \(h_2=(x^2-1)/\sqrt2\). Since
\[
\langle m_s,h_2\rangle=2\sqrt2\,s(3s-1),
\]
analytic perturbation of the compact operator yields
\[
\Lambda(s,\rho)=\mu(s)+\frac{8s^2(3s-1)^2}{\mu(s)}\rho^2+O(\rho^4).
\]
The spectrum is even in \(\rho\), by reflecting the Gaussian coordinate. At \(s=2/3\), \(\mu=1\), \(\mu'(s)=2\), and the quadratic coefficient is \(32/9\). The implicit-function theorem therefore gives
\[
s_c(\rho)=\frac23-\frac{16}{9}\rho^2+O(\rho^4).
\]
This completes the universal argument.

## Verification
The standalone file `gaussian_ar1_sgd_verify.py` uses normalized Gauss–Hermite quadrature, a symmetric Nyström representation of the Mehler operator, and independent two-variable Gaussian quadrature. Running `python gaussian_ar1_sgd_verify.py` passed 106 deterministic checks. For example, at \(\rho=0.04\), numerical root-finding gave \(s_c\approx0.6638237707\), versus the second-order prediction \(0.6638222222\). As separate exact moment identities, independent Gaussian integration verifies
\[
\operatorname{Cov}(m_s(U_0),m_s(U_1))=8s^2(3s-1)^2\rho^2+24s^4\rho^4
\]
and
\[
d_1=1-2s+3s^2+4s(3s-1)\rho^2.
\]
Quadrature truncation and floating-point arithmetic only test finite cases; all-integer-time and infinite-dimensional claims rest on the preceding proof.

## Relationship to prior work
Li and Wu, *Gaussian Limits for SGD Without Stationary Moments* (arXiv:2610.05599v1, first submitted 2026-10-04), study the same ordinary least-squares SGD recursion under dependent designs. Their Gaussian-refresh example has infinite stationary moments for every nonzero persistence parameter; their AR(1) counterexamples use heavy-tailed positive innovations. The finite Gaussian AR(1) innovation design here is different: it yields a nontrivial correlation-dependent second-moment stability window. Their paper is about small-step distributional limits, not the sharp Hermite-transfer boundary given above.

Classical LMS literature provides exact mean-square methods for Gaussian inputs. In particular, Scott C. Douglas (ICASSP 1993, doi:10.1109/ICASSP.1993.319549) states a recursive analysis for finite-time-correlated input data and possible exact step-size limits; full paper text was not available for comparison. This prior work is a material originality risk, especially for the transfer-operator criterion itself. The new result is the strict infinite-memory AR(1) correlation frontier together with the analytic \(-16/9\) coefficient; this is not claimed to supersede the older recursive framework. Independent-design heavy-tail theory in Gürbüzbalaban, Şimşekli and Zhu (arXiv:2006.04740) does not quantify the autocorrelation penalty.

## Limitations
The theorem applies only to a scalar least-squares recursion with standard Gaussian AR(1) design, independent finite-variance observation noise, exact arithmetic, and the second moment. It does not prove tail exponents, general nonlinear optimization convergence, almost-sure critical thresholds, non-Gaussian design universality or multidimensional extensions. Correlation \(\rho<0\) is equivalent at the squared-design level to \(|\rho|\), but the statement uses \(0\le\rho<1\). The literature comparison cannot rule out an equivalent result in the uninspected 1993 full paper or other adaptive-filtering literature.

## References
1. X. Li and W. B. Wu, *Gaussian Limits for SGD Without Stationary Moments*, arXiv:2610.05599v1 (2026-10-04), https://arxiv.org/abs/2610.05599 .
2. S. C. Douglas, *Exact expectation analysis of the LMS adaptive filter for correlated Gaussian input data*, Proceedings of ICASSP (1993), doi:10.1109/ICASSP.1993.319549 .
3. M. Gürbüzbalaban, U. Şimşekli and L. Zhu, *The Heavy-Tail Phenomenon in SGD*, arXiv:2006.04740, https://arxiv.org/abs/2006.04740 .
