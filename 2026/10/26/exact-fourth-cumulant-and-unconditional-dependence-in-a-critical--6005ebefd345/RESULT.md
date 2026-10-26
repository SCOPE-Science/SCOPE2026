# Exact fourth cumulant and unconditional dependence in a critically switching reinforced diffusion

## Finding

Consider the stationary telegraph-modulated Gaussian diffusion identified as the critical hybrid-fluctuation limit in Cruz-Suárez (2026), with parameters as specified below. Its collective fluctuation mode has the **exact fourth cumulant**

\[
\operatorname{cum}_4(Z^U_0)=\frac{3c\delta^4(a-1)^2\left(9a^3+10a^2c+7a^2+3a+2c-1\right)}{a^2(a+2c)^2(2a-1)(3a+2c)(4a-1)(3a+2c-1)}.
\]

Consequently, the collective mode is marginally Gaussian **if and only if** \(\rho+\kappa=0\). The collective and disagreement modes have zero covariance for every admissible parameter choice, but they are independent **if and only if** \(\rho+\kappa=0\). Indeed, for \(\rho+\kappa>0\), their squared amplitudes have strictly positive covariance, described by a two-by-two rational-resolvent formula below. The assertions apply to the stationary limiting diffusion; they are not claims of finite-size identities for the underlying interacting urns.

## Assumptions and scope

Let \(\rho,\kappa\ge0\), \(\delta>0\), \(\rho+\kappa+2\delta<1\), and \(c>0\). Put \(a=1-\rho-\kappa\), \(b=1-\rho+\kappa\), \(r=1-a=\rho+\kappa\), and \(k=2a-1\), \(\ell=2b-1\). These assumptions give \(1/2<a\le b\le1\), \(k>0\), and \(\ell>0\). Let \(E_t\in\{-1,+1\}\) be a stationary symmetric continuous-time chain flipping at rate \(c\). Let \(U\) be its unique bounded stationary causal filter solving

\[
\mathrm dU_t=(-aU_t+\delta E_t)\,\mathrm dt,\qquad
U_t=\delta\int_{-\infty}^t e^{-a(t-s)}E_s\,\mathrm ds.
\]

Define the positive stochastic volatility \(Q_t=\sigma^2(U_t,E_t)\) by

\[
Q_t=\frac18-\frac12(rU_t+\delta E_t)^2.
\]

In fact \(|rU_t+\delta E_t|\le\delta/a<1/2\), so \(Q_t>0\). On a stationary extension, let \(W^U,W^V\) be independent two-sided Brownian motions independent of \(E\), and define the stationary centered modes

\[
\mathrm dZ^U_t=-(a-\tfrac12)Z^U_t\,\mathrm dt+\sqrt{Q_t}\,\mathrm dW^U_t,\qquad
\mathrm dZ^V_t=-(b-\tfrac12)Z^V_t\,\mathrm dt+\sqrt{Q_t}\,\mathrm dW^V_t.
\]

This is the conditional Gaussian pair appearing in the critical switching fluctuation theorem of Cruz-Suárez; the telegraph path is shared but the Gaussian noises are independent. Write \(V_z=\int_0^\infty e^{-zs}Q_{-s}\,\mathrm ds\) for \(z>0\). Conditional on the whole telegraph path, \(Z^U_0,Z^V_0\) are independent centered Gaussians with variances \(V_k,V_\ell\).

## Proof

**Stationary moments of the telegraph filter.** The generator acting on functions \(f(u,e)\) is

\[
\mathcal Lf=(-au+\delta e)\,\partial_uf+c\bigl(f(u,-e)-f(u,e)\bigr).
\]

Applying the stationary identity \(\mathbb E\mathcal Lf=0\) to \(ue,u^2,u^3e,u^4\), successively, and defining \(D=a+2c\) and \(H=3a+2c\), gives

\[
\mathbb E[UE]=\frac\delta D,\quad
\mathbb E[U^2]=\frac{\delta^2}{aD},\quad
\mathbb E[U^3E]=\frac{3\delta^3}{aDH},\quad
\mathbb E[U^4]=\frac{3\delta^4}{a^2DH}.
\]

All moments exist because \(U\) is bounded. In particular,

\[
\overline Q:=\mathbb E Q_0=\frac18-\frac{\delta^2(1+2ac)}{2a(a+2c)},
\qquad \mathbb E[(Z^U_0)^2]=\frac{\overline Q}{k}.
\]

**A closed covariance representation.** Define the centered random vector

\[
A_t=\begin{pmatrix}U_t^2-\mathbb E U^2\\U_tE_t-\mathbb E(UE)\end{pmatrix},\qquad
v=\begin{pmatrix}r^2\\2r\delta\end{pmatrix},\qquad
M=\begin{pmatrix}-2a&2\delta\\0&-D\end{pmatrix}.
\]

The generator preserves the affine span of \(U^2,UE,1\). Thus for \(t\ge0\), \(\mathbb E[A_t\mid U_0,E_0]=e^{Mt}A_0\). The stationary covariance matrix \(S=\mathbb E[A_0A_0^{\mathsf T}]\) is exactly

\[
S=\begin{pmatrix}
\dfrac{4c\delta^4}{a^2D^2H}&\dfrac{4c\delta^3}{aD^2H}\\[5pt]
\dfrac{4c\delta^3}{aD^2H}&\dfrac{2c\delta^2}{aD^2}
\end{pmatrix}.
\]

Since \(Q_t-\overline Q=-\tfrac12v^{\mathsf T}A_t\), the stationary autocovariance, for \(t\ge0\), is

\[
C_Q(t):=\operatorname{Cov}(Q_0,Q_t)
=\frac14v^{\mathsf T}S e^{M^{\mathsf T}t}v.
\]

The entries of \(S\) are strictly positive, and \(e^{M^{\mathsf T}t}\) is entrywise nonnegative. For \(r>0\), both entries of \(v\) are positive. Therefore \(C_Q(t)>0\) for every \(t\ge0\) in this regime, whereas \(r=0\) makes \(Q\) constant and \(C_Q\equiv0\).

**Variance mixing and the exact formula.** Introduce the Laplace transform

\[
L(z)=\int_0^\infty e^{-zt}C_Q(t)\,\mathrm dt
=\frac14v^{\mathsf T}S(zI-M^{\mathsf T})^{-1}v\qquad(z>0).
\]

Stationarity and Fubini's theorem (all variables are bounded) give

\[
\operatorname{Var}(V_k)=\frac{L(k)}k,\qquad
\operatorname{Cov}(V_k,V_\ell)=\frac{L(k)+L(\ell)}{k+\ell}.
\]

Conditional Gaussian fourth moments imply

\[
\operatorname{cum}_4(Z^U_0)=3\operatorname{Var}(V_k)=\frac{3L(k)}k,\qquad
\operatorname{Cov}\big((Z^U_0)^2,(Z^V_0)^2\big)=\frac{L(k)+L(\ell)}{k+\ell}.
\]

For complete reproducibility, the needed inverse is explicit:

\[
(zI-M^{\mathsf T})^{-1}=
\begin{pmatrix}
\dfrac1{z+2a}&0\\[5pt]
\dfrac{2\delta}{(z+2a)(z+D)}&\dfrac1{z+D}
\end{pmatrix}.
\]

Substitution of the displayed \(S,v\) and \(z=k=2a-1\) into \(3L(k)/k\), followed by collecting denominators, yields the fourth-cumulant expression in the finding. Every denominator factor is positive. Its remaining polynomial factor is

\[
9a^3+7a^2+3a-1+2c(5a^2+1)>0
\quad\text{for }a>1/2,\ c>0.
\]

Hence \(\operatorname{cum}_4(Z^U_0)>0\) exactly when \(r>0\). A nondegenerate centered Gaussian has fourth cumulant zero; at \(r=0\), \(Q_t\equiv1/8-\delta^2/2>0\) and \(Z^U\) is exactly Gaussian. This proves the marginal Gaussianity dichotomy.

Finally, conditional on \(E\), the two modes have independent centered Gaussian laws, so their covariance is zero unconditionally. The preceding strict inequality \(L(z)>0\) for \(r>0\) gives strictly positive covariance of squared amplitudes; thus the modes are dependent. For \(r=0\), their diffusion coefficients are deterministic and their Brownian drivers independent, so the modes themselves are independent. This proves the dependence dichotomy and the resolvent formula for all allowed \(b\).

## Verification

The standalone `CHECK.py` uses only exact rational arithmetic from Python's standard library. Run `python3 CHECK.py` from the directory containing this document. It checks the four stationary filter moments, the covariance matrix, the source's second-moment identity, the resolvent and polynomial formulas, and a separately derived stationary augmented-generator calculation on 96 rational parameter/mode cases. It additionally checks two exact regression fractions, \(13/24576\) and \(8103/16662500000\), for parameter sets described in the script. These finite checks support algebraic reproducibility; the generator and covariance arguments above, not the parameter grid, prove the all-parameter result.

## Relationship to prior work

Cruz-Suárez (2026, Sections 2 and 4) constructs the critical two-mode switching diffusion, proves conditional Gaussianity, and computes stationary **second** moments; it explicitly observes that conditional independence need not imply unconditional independence. The present result computes a closed fourth cumulant of its specific continuously filtered switching volatility and settles the marginal Gaussianity and unconditional mode-independence questions exactly, including the strictness boundary. Huang et al. (2014) develop general moment tools for finite-state Markov-modulated Ornstein–Uhlenbeck processes, but their coefficient process depends directly on a finite-state chain, whereas the volatility here also depends on its continuous causal filter \(U\). The calculation above gives the model-specific closed rational identity and the sign of cross-mode square dependence.

## Limitations

The finding concerns the **stationary limiting diffusion**, not a finite-size urn concentration bound, not nonstationary initial laws, and not joint Gaussianity with the telegraph environment. Fourth cumulants alone do not characterize arbitrary distributions, but nonzero fourth cumulant decisively rules out a Gaussian marginal here, while constancy of the volatility proves Gaussianity at the boundary. The literature comparison is based on identified accessible primary material; an equivalent result in older stochastic-volatility or Markov-switching terminology remains possible.

## References

1. H. Cruz-Suárez, *Exact random centering and hybrid fluctuation limits for interacting reinforced processes under critical Markov switching* (2026), arXiv:2610.02609v1, first posted October 2, 2026, https://arxiv.org/abs/2610.02609.
2. G. Huang, H. Jansen, M. Mandjes, P. Spreij, and K. De Turck, *Markov-modulated Ornstein-Uhlenbeck processes* (2014 preprint), arXiv:1412.7952v1, https://arxiv.org/abs/1412.7952.
