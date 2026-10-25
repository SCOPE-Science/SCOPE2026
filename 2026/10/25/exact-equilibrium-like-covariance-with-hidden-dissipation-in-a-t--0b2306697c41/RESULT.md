# Exact equilibrium-like covariance with hidden dissipation in a two-state fluctuating harmonic trap

## Finding

An overdamped Brownian particle confined by a randomly switching **strictly positive** harmonic stiffness can have *exactly the same stationary position autocovariance at every lag* as an equilibrium Ornstein–Uhlenbeck (OU) particle, while its physical stationary entropy production is strictly positive and can be arbitrarily large. The coincidence occurs at one, and only one, nontrivial switching rate: the geometric mean of the two stiffnesses. On that curve, a strictly positive fourth cumulant identifies the dissipation exactly.

More precisely, assume positive numbers \(a,b,\kappa,D\) with \(a\ne b\), and write \(C(t)=\mathbb E[X_0X_t]\) for stationary positions. For all \(t\ge0\), the following are equivalent:

1. \(C(t)=V e^{-\alpha t}\) for some constants \(V,\alpha>0\) and every \(t\ge0\), so that the covariance is that of an equilibrium OU process;
2. \(\kappa^2=ab\).

When these conditions hold, necessarily
\[
C(t)=\frac{D}{\kappa}e^{-\kappa t},\qquad
\Sigma=\frac{a+b-2\kappa}{2}=\frac{(\sqrt a-\sqrt b)^2}{2}>0.
\]
Here \(\Sigma\) is the dimensionless steady-state *internal entropy-production rate of the jointly observed position and switching environment*, in the convention of Alston, Cocconi and Bertrand [1], not an entropy production inferred from the position process alone. Define the standardized fourth cumulant (excess kurtosis)
\[
K=\frac{\mathbb E[X^4]-3(\mathbb E[X^2])^2}{(\mathbb E[X^2])^2}.
\]
Then the exact dissipation–kurtosis calibration is
\[
K=\frac{9(a+b-2\kappa)}{a+b+4\kappa}
 =\frac{9\Sigma}{\Sigma+3\kappa},\qquad
0<K<9,\qquad
\Sigma=\frac{3\kappa K}{9-K}.
\]
For fixed \(D,\kappa\), the family \(b=\kappa^2/a\), \(a>0\), has the *same complete position covariance* while \(\Sigma\) ranges over \([0,\infty)\) (with the equilibrium endpoint at \(a=b=\kappa\)). For distinct stiffnesses the range is \((0,\infty)\), and the kurtosis ranges over \((0,9)\).

The case \(a=b\) is the trivial equilibrium OU process for **every** positive switching rate and is excluded from the nontrivial equivalence above.

## Assumptions and scope

Let \((S_t)_{t\in\mathbb R}\) be a two-state, continuous-time Markov chain with transition rate \(\kappa>0\) in each direction, independent of a two-sided standard Brownian motion \(W\). Write \(k_0=a>0\), \(k_1=b>0\), and consider the Itô diffusion
\[
dX_t=-k_{S_t}X_t\,dt+\sqrt{2D}\,dW_t,\qquad D>0.
\]
The environment is initialized in its stationary law \(\Pr(S_t=i)=1/2\) and \(X\) is initialized in the unique joint stationary state. Positive stiffnesses ensure the causal representation
\[
X_t=\sqrt{2D}\int_{-\infty}^{t}
\exp\left(-\int_u^t k_{S_s}\,ds\right)dW_u,
\]
which exists in every finite \(L^m\) and gives zero mean, finite moments of all orders, and a unique stationary law. We assess stationary \(C(t)\), not the finite-time variance from a nonequilibrium initial condition. The entropy-production normalization is exactly that of [1, §4.2.2, Eq. (41)]; the external switching process is reversible in isolation, but its coupled position dynamics is not.

## Proof

**Step 1: Exact state-resolved second moments.** Write \(u_i=\mathbb E[X_0^2\mathbf1_{\{S_0=i\}}]\). Stationarity and the joint generator give
\[
\begin{pmatrix}2a+\kappa&-\kappa\\-\kappa&2b+\kappa\end{pmatrix}
\begin{pmatrix}u_0\\u_1\end{pmatrix}
=D\begin{pmatrix}1\\1\end{pmatrix}.
\]
Define \(s=a+b\), \(p=ab\), \(J=2p+\kappa s\), \(L=s+2\kappa\), and \(P=p+\kappa s\). Inversion yields
\[
u_0=\frac{D(b+\kappa)}{J},\quad
u_1=\frac{D(a+\kappa)}{J},\quad
C(0)=\frac{DL}{J}.
\]
Applying Itô's formula to \(X^2\) and averaging in stationarity gives \(\mathbb E[k_{S_0}X_0^2]=D\); therefore \(C'(0+)=-D\).

**Step 2: Complete two-time covariance.** Condition first on \((X_0,S_0)\), then on the future switching path. The independent future Brownian increments have zero conditional mean. The Feynman–Kac formula therefore gives the exact, all-lag representation
\[
C(t)=(u_0,u_1)
\exp\!\left[t\begin{pmatrix}-a-\kappa&\kappa\\\kappa&-b-\kappa\end{pmatrix}\right]
\begin{pmatrix}1\\1\end{pmatrix}.
\]
The matrix has trace \(-L\) and determinant \(P\). Cayley–Hamilton thus implies, for every \(t>0\),
\[
C''(t)+L C'(t)+P C(t)=0,
\quad C(0)=DL/J,\quad C'(0+)=-D.
\]
This is an exact two-dimensional linear evolution; no Gaussian assumption about the stationary \(X\) was used.

**Step 3: Necessary and sufficient threshold.** If \(C(t)=V e^{-\alpha t}\) for every \(t\ge0\), then \(V=DL/J\) and the slope enforces \(\alpha=J/L\). The ODE requires \(\alpha^2-L\alpha+P=0\), equivalently
\[
J^2-L^2J+PL^2
=(p-\kappa^2)(4p-s^2)=0.
\]
But \(4p-s^2=-(a-b)^2\ne0\); hence \(p=\kappa^2\) is necessary. Conversely, if \(p=\kappa^2\), then \(J=\kappa L\), \(C(0)=D/\kappa\), and \(\alpha=J/L=\kappa\) is a root of the ODE. Uniqueness of the initial-value problem gives \(C(t)=(D/\kappa)e^{-\kappa t}\) for all \(t\ge0\). When \(a=b\), the environmental switch does not affect the drift, and equilibrium OU covariance holds for any \(\kappa\).

**Step 4: Positive fourth cumulant.** Define \(v_i=\mathbb E[X_0^4\mathbf1_{\{S_0=i\}}]\). Stationarity of fourth moments yields
\[
\begin{pmatrix}4a+\kappa&-\kappa\\-\kappa&4b+\kappa\end{pmatrix}
\begin{pmatrix}v_0\\v_1\end{pmatrix}
=12D\begin{pmatrix}u_0\\u_1\end{pmatrix}.
\]
Direct inversion produces the independent exact checkpoint
\[
\mathbb E[X^4]
=\frac{6D^2\big(2a^2+3a\kappa+2b^2+3b\kappa+2\kappa^2\big)}
{(2ab+\kappa(a+b))(4ab+\kappa(a+b))}.
\]
Subtracting \(3C(0)^2\) yields
\[
\operatorname{cum}_4(X)
=\frac{3D^2(a-b)^2(4ab+3\kappa(a+b)+2\kappa^2)}
{(2ab+\kappa(a+b))^2(4ab+\kappa(a+b))}.
\]
This is strictly positive when \(a\ne b\). Restricting to \(ab=\kappa^2\) simplifies it to
\[
\operatorname{cum}_4(X)
=\frac{9D^2}{\kappa^2}\frac{a+b-2\kappa}{a+b+4\kappa}.
\]
Divide by \(C(0)^2=D^2/\kappa^2\) to obtain the asserted \(K\).

**Step 5: Thermodynamic calibration and its range.** The established exact entropy-production law for symmetric two-state harmonic switching [1, Eq. (41)] reads
\[
\Sigma=\frac{\kappa(a-b)^2}{4ab+2\kappa(a+b)}.
\]
On \(ab=\kappa^2\), factor \((a-b)^2=(a+b-2\kappa)(a+b+2\kappa)\) to obtain \(\Sigma=(a+b-2\kappa)/2\). Substitute \(a+b=2\Sigma+2\kappa\) into the kurtosis expression to get
\(K=9\Sigma/(\Sigma+3\kappa)\). This is strictly increasing from zero to nine as the nonnegative dissipation increases, so its inversion and strict bounds follow. Fixing \(\kappa,D\) and letting \(a\to\infty\), \(b=\kappa^2/a\to0\), proves unbounded entropy production without changing the stationary two-time covariance.

**Exact example.** With \((a,b,\kappa,D)=(1,4,2,1)\), the covariance is \(C(t)=\tfrac12 e^{-2t}\) but \(\Sigma=\tfrac12\). The fourth moment is \(12/13\), whereas the equilibrium OU process with this covariance has fourth moment \(3/4\). Consequently \(\operatorname{cum}_4(X)=9/52\) and \(K=9/13\). These fractions are checked separately by exact rational arithmetic.

## Verification

Run `python checks/check.py` after installing the Python dependencies in `requirements.txt`. `checks/results.txt` records the output of the included checker, which independently constructs the stationary second/fourth moment matrices, symbolically verifies the key factorization and thermodynamic relation, tests thirty numerical matrix-exponential lag values on five nonidentical parameter quadruples, tests four off-criterion values, and checks the example with exact rational arithmetic. This checker was executed before packaging; its tests passed. The proof above is analytic for all positive real parameters and all nonnegative time lags. Numerical checks do not replace that proof.

## Relationship to prior work

Alston, Cocconi and Bertrand [1] introduce and solve the two-state fluctuating harmonic trap, deriving the stationary state-resolved second moments [Eq. (38)] and stationary entropy production [Eq. (41)]; neither is claimed as new. Their article analyzes energy dissipation, limiting rates and marginal statistics. The new contribution is the **if-and-only-if finite-rate equality of the entire autocovariance with an equilibrium OU process**, accompanied by the exact positive fourth-cumulant witness and entropy–kurtosis calibration on that equality curve. The covariance computation uses the known general Markov/Feynman–Kac method, not a new stochastic-calculus formalism.

Zhang and Wang [2] study stationary distributions for two-state Markov-switching OU models. Santra, Das and Nath [3] analyze an on/off trap (one stiffness zero), excluding the strictly-positive nontrivial equality curve. Behme and Sideris [4] develop a general framework for Markov-modulated OU stationary laws, providing background sufficient to derive general propagation formulas, but their inspected material does not establish the exact scalar-observable cancellation threshold and entropy/kurtosis calibration. Cocconi, Alston, Romano and Bertrand [5] examine continuously OU-modulated stiffness, not a two-valued jump stiffness. Frydel [6] analyzes the on/off version, whereas the later semi-Markovian two-stiffness framework [7] develops stationary moment and work formulas without the evaluated **two-time** OU-camouflage theorem. Related results on identical low-order statistics in other stochastic models do not directly imply this precise equality curve.

These are implication comparisons, not a claim that searches prove uniqueness. An equivalent restatement in the wider regime-switching literature remains a priority risk; independent scientific audit has not been performed.

## Limitations

The equality concerns **only the full stationary covariance (equivalently the power spectrum)**, not equality of finite-dimensional distributions, transition kernels or path laws. The position distribution is demonstrably non-Gaussian when the two stiffnesses differ. The entropy rate belongs to the physical joint position–environment model, and deriving it requires the model assumption and prior exact thermodynamic formula, not only the two-point data. The theorem assumes exactly two equally likely environment states with equal switching rates, independent additive Brownian noise with state-independent intensity, positive stiffnesses, harmonic forces and stationary preparation. It does not establish such a cancellation for asymmetric rates, state-dependent diffusion, continuous noisy stiffness, or nonharmonic potentials. No independent priority validation or external certificate has been performed.

## References

1. H. Alston, L. Cocconi and T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630 (public 2022-02-05), *Journal of Physics A: Mathematical and Theoretical* **55** (2022), 274004; https://arxiv.org/abs/2202.02630. In particular §4, Eqs. (37)–(43).
2. Z. Zhang and W. Wang, *The stationary distribution of Ornstein–Uhlenbeck process with a two-state Markov switching*, *Communications in Statistics—Simulation and Computation* **46** (2017), 4783–4794, https://doi.org/10.1080/03610918.2015.1132321.
3. I. Santra, S. Das and S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609 (2021), https://arxiv.org/abs/2104.00609.
4. A. Behme and A. Sideris, *Markov-modulated generalized Ornstein-Uhlenbeck processes and an application in risk theory*, arXiv:2012.10712 (2020), https://arxiv.org/abs/2012.10712.
5. L. Cocconi, H. Alston, J. Romano and T. Bertrand, *The OU² process: characterising dissipative confinement in noisy traps*, arXiv:2405.09460 (2024), https://arxiv.org/abs/2405.09460.
6. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213 (2024), https://arxiv.org/abs/2407.12213.
7. D. Frydel, *Semi-Markovian switching in a fluctuating harmonic trap: An age-structured formulation*, arXiv:2607.05173 (2026), https://arxiv.org/abs/2607.05173.
