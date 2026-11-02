# Quenched Brownian normality for static cardinality-driven bootstrap walks

## Finding
Let \((\xi_j)_{j\ge1}\) be independent fair signs and let \((\beta_k)_{k\ge0}\) be an independent family of Bernoulli variables, independent of the signs, with fixed parameters \(\varepsilon\le p_k\le1-\varepsilon\) for some \(0<\varepsilon<1/2\). Define
\[
S_n=\sum_{j=1}^n\mathbf1_{\{\xi_j=-1\}},\qquad
f(s)=(-1)^{\sum_{k=0}^s\binom{s}{k}\beta_k},\qquad
\zeta_0=1,\quad \zeta_n=f(S_n)\ (n\ge1),
\]
and \(\eta_j=\zeta_{j-1}\xi_j\), \(X_n=\sum_{j=1}^n\xi_j\), \(Y_n=\sum_{j=1}^n\eta_j\).

**Theorem.** For almost every realization of the single, time-static environment \((\beta_k)_{k\ge0}\), the driving-sign law satisfies
\[
\lim_{N\to\infty}\frac1N\sum_{j=0}^{N-1}\zeta_j=0\quad\text{almost surely},
\]
and, for every finite \(T>0\),
\[
\left(\frac{X_{\lfloor Nt\rfloor}}{\sqrt N},\frac{Y_{\lfloor Nt\rfloor}}{\sqrt N}\right)_{0\le t\le T}
\ \Longrightarrow\ (B_t^{(1)},B_t^{(2)})_{0\le t\le T}
\quad\text{in }D([0,T],\mathbb R^2),
\]
where \(B^{(1)}\) and \(B^{(2)}\) are independent standard Brownian motions. This establishes the quenched analogue of the *annealed* conclusion of Corollary 12 of Hamza and Tournier (2026) for its full uniformly elliptic, time-invariant cardinality model.

## Assumptions and scope
The parameter sequence \((p_k)\) is deterministic and may be nonstationary. Independence is required only between the individual static coefficients \(\beta_k\), not between resampled coefficients at different times: the same \(\beta_k\) is used at every step. The signs are independent and symmetric. The initial convention \(\zeta_0=1\) is that of the cited bootstrap-walk model; it differs from \(f(S_0)\) by at most one bounded term.

Write \(\omega(s)\) for the number of ones in the binary expansion of \(s\). All assertions concern the infinite sequence, for every admissible parameter array. No independence of the time-indexed scenery \((f(S_n))\) is assumed.

## Proof
**1. The static Pascal scenery has zero spatial Cesàro mean almost surely.** By Lucas' parity theorem, let
\[
D(s)=\{k\ge0:k\preceq_2s\};
\qquad f(s)=\prod_{k\in D(s)}(-1)^{\beta_k},
\qquad |D(s)|=2^{\omega(s)}.
\]
Here \(k\preceq_2s\) means that every binary 1-bit of \(k\) is also a 1-bit of \(s\). If \(s\ne t\), then
\[
|D(s)\mathbin\triangle D(t)|\ge 2^{\min(\omega(s),\omega(t))}.
\]
Indeed, if one of the two Boolean downsets is strictly nested in the other, the larger set has at least twice the smaller cardinality; otherwise the intersection has at most half the smaller cardinality. This proves the displayed bound in either case.

Set \(q=1-2\varepsilon<1\). Independence of the coefficient bits gives the **exact** moment identity
\[
\mathbb E_\beta[f(s)f(t)]
=\prod_{k\in D(s)\triangle D(t)}(1-2p_k),
\]
whose absolute value is at most \(q^{|D(s)\triangle D(t)|}\). For \(m\ge2\), put \(L=\lceil\log_2m\rceil\), \(r=\lfloor L/4\rfloor\) and \(b_m=\#\{0\le s<m:\omega(s)<r\}\). A binomial Hoeffding bound yields
\[
\frac{b_m}{m}
\le\frac{2^L}{m}\Pr\{\operatorname{Bin}(L,1/2)<L/4\}
\le2e^{-L/8}.
\]
Separate the diagonal pairs, pairs involving one of the \(b_m\) exceptional indices, and all remaining pairs. For \(F_m=\sum_{s=0}^{m-1}f(s)\),
\[
\mathbb E_\beta\left[\left(\frac{F_m}{m}\right)^2\right]
\le\frac1m+\frac{2b_m}{m}+q^{2^r}
\le C_\varepsilon m^{-\delta},\qquad
\delta=\frac{1}{8\log 2}>0.
\]
The last inequality holds after enlarging the constant for finitely many small \(m\), because \(2^r\ge m^{1/4}/2\). On \(m_j=\lceil j^{12}\rceil\), the second-moment bound is summable. Chebyshev and Borel–Cantelli show \(F_{m_j}/m_j\to0\) almost surely. Since \(|f(s)|=1\) and \(m_{j+1}/m_j\to1\), interpolation gives
\[
\frac1m\sum_{s=0}^{m-1}f(s)\longrightarrow0
\quad\text{for almost every environment.}\tag{1}
\]
This argument treats arbitrary independent elliptic biases, not only fair coefficient bits.

**2. Geometric occupation of the scenery transfers (1) to time averages.** Fix an environment satisfying (1). As the driving fair signs evolve, \(S_n\) increases by one on a negative sign and otherwise holds its value. The completed holding lengths \(H_s=\#\{n\ge0:S_n=s\}\), indexed by visited states before the next increase, are independent geometric random variables on \(\{1,2,\ldots\}\), with mean 2 and variance 2. For the fixed bounded sequence \(f(s)\), Kolmogorov's strong law for independent centered variables with uniformly bounded variances gives
\[
\frac1m\sum_{s=0}^{m-1}f(s)(H_s-2)\longrightarrow0
\quad\text{almost surely.}
\]
Together with (1) and \(m^{-1}\sum_{s<m}H_s\to2\), the completed-occupation average vanishes. The incomplete last holding interval is negligible, since \(H_m/m\to0\) almost surely by the geometric tail and Borel–Cantelli. Consequently
\[
\frac1N\sum_{n=0}^{N-1}f(S_n)\longrightarrow0
\quad\text{almost surely under the driving-sign law.}\tag{2}
\]
Replacing the first term by \(\zeta_0=1\) changes the average by at most \(2/N\), proving the theorem's quenched almost-sure bracket statement.

**3. Conditional martingale invariance principle.** Condition on any environment where (2) holds. With the natural driving-sign filtration, \((X_n,Y_n)\) is a square-integrable two-dimensional martingale. Its increments are \((\xi_j,\zeta_{j-1}\xi_j)\), bounded in norm by \(\sqrt2\), and their predictable conditional covariance matrices equal
\[
\begin{pmatrix}1&\zeta_{j-1}\\\zeta_{j-1}&1\end{pmatrix}.
\]
The Cesàro conclusion implies that the off-diagonal brackets divided by \(N\) tend to zero uniformly on every compact rescaled time interval (split the prefix at \(\delta N\), then let \(\delta\downarrow0\)). The diagonal brackets are the deterministic step counts. The conditional Lindeberg condition is automatic from bounded increments. The multivariate martingale functional central limit theorem therefore gives the independent-coordinate Brownian limit. This holds for almost every environment, proving the claimed quenched statement.

## Verification
A standalone deterministic script, `check.py`, uses exact rational arithmetic to verify Lucas parity, the Boolean-downset symmetric-difference inequality, covariance factorization for four nonstationary parameter profiles, and exact second moments of finite empirical scenery averages. Executing it produced the results stored in `check_output.txt`, including 4,376 assertions. The proof above, not finite enumeration, establishes the almost-sure and functional limit claims.

## Relationship to prior work
Hamza and Tournier, *Are random random walks normal?* (arXiv:2610.01658v1, first submitted 2026-10-01), Section 4.3, Proposition 11 and Corollary 12, establish an annealed independent-Brownian limit for precisely the time-invariant elliptic cardinality environment. Their introduction explicitly distinguishes annealed-only conclusions from unresolved quenched ones. The present theorem proves that missing quenched conclusion using a spatial moment estimate for the single static Pascal transform and renewal occupation, rather than resampling independent coefficients at every time.

Collevecchio, Hamza, Shi and Williams, *Limit theorems and ergodicity for general bootstrap random walks* (2022), provide a general martingale criterion for deterministic recycling transformations; that general criterion does not supply the static random-environment almost-sure scenery law. Related results for environments independently refreshed with time and for freely sampled Boolean maps use different coefficient dependencies and do not imply the static model's quenched limit.

## Limitations
The theorem requires independent coefficient bits and a uniform ellipticity constant. It does not address dependent static coefficients, parameters tending to 0 or 1, nonsymmetric driving increments, or convergence rates. Earlier general results on random Boolean transforms or orthogonal-product arrays might imply the spatial lemma indirectly, so definitive historical-priority determination requires wider expert review. No independent validation is claimed.

## References
- K. Hamza and L. Tournier, *Are random random walks normal?*, arXiv:2610.01658v1 (2026-10-01), Sections 2, 4.1 and 4.3. https://arxiv.org/html/2610.01658v1
- A. Collevecchio, K. Hamza, M. Shi and R. J. Williams, *Limit theorems and ergodicity for general bootstrap random walks*, Electronic Journal of Probability 27 (2022), article 92; arXiv:2010.16000. https://arxiv.org/abs/2010.16000
- É. Lucas, *Théorie des Fonctions Numériques Simplement Périodiques*, American Journal of Mathematics 1 (1878), 197–240 (parity of binomial coefficients).
- J. Jacod and A. N. Shiryaev, *Limit Theorems for Stochastic Processes*, Springer (1987), martingale functional limit theorem.
