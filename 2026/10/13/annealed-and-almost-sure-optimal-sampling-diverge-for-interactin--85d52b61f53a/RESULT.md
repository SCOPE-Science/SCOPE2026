# Annealed and almost-sure optimal sampling diverge for interacting Wasserstein coordinate descent

## Finding

For diagonal positive quadratic potential and interaction energies, random Wasserstein coordinate descent has two distinct, exactly solvable optimization problems: minimizing worst-case expected objective error at every finite iteration, and minimizing the worst-case almost-sure exponential error rate. Both choose the same unique coordinate steps, but they generally choose **different** fixed independent-coordinate sampling distributions. The distinction can be arbitrarily costly for the expected objective: a sequence of instances has uniformly bounded optimal expected contraction while the almost-sure-optimal sampling has worst-case expected contraction approaching one.

Precisely, for each coordinate let \(a_i>0\), \(\beta_i>0\), \(b_i=a_i+\beta_i/2\), and define
\[
t_i=\left(\frac{b_i-a_i}{b_i+a_i}\right)^2\in(0,1),\qquad
\delta_i=1-t_i=\frac{4a_i b_i}{(a_i+b_i)^2},\qquad
c_i=-\log t_i>0.
\]
Among all fixed independent coordinate probabilities \(p_i>0\) summing to one and all stable positive steps \(0<\eta_i<2/b_i\), both minimax criteria uniquely select the step
\[
\eta_i^*=\frac{2}{a_i+b_i}.
\]
For every integer \(k\ge1\), the unique minimizer of the worst-case \(k\)-step expected-energy ratio uses
\[
p_i^{\mathrm A}=\frac{\delta_i^{-1}}{\sum_j\delta_j^{-1}},\qquad
R_{\mathrm A}^*=1-\frac{1}{\sum_j\delta_j^{-1}},
\qquad \mathbb E E(\mu_k)=(R_{\mathrm A}^*)^k E(\mu_0).
\]
The last identity holds for **every** initial probability measure with finite second moment, not only a worst-case measure. In contrast, the unique minimizer of the worst-case almost-sure exponential ratio uses
\[
p_i^{\mathrm Q}=\frac{c_i^{-1}}{\sum_j c_j^{-1}},\qquad
R_{\mathrm Q}^*=\exp\left(-\frac1{\sum_j c_j^{-1}}\right),\qquad
\lim_{k\to\infty}E(\mu_k)^{1/k}=R_{\mathrm Q}^*\quad\text{almost surely}
\]
for every initial measure of positive energy (the limit is interpreted as an exponential factor; the zero-energy case is excluded). The optimal probability vectors coincide exactly when all \(t_i\) coincide.

For two coordinates with \(a_1=a_2=1\), \(\beta_2=4\) and \(\beta_1\downarrow0\) through positive values, the worst-case one-step expected factor under \(p^{\mathrm Q}\) tends to one, whereas \(R_{\mathrm A}^*\to4/7\). Thus optimizing typical almost-sure decay can sacrifice the expected-energy guarantee by an arbitrarily severe *contraction-factor* margin.

## Assumptions and scope

Fix an integer \(d\ge2\) and a Borel probability measure \(\mu\in\mathcal P_2(\mathbb R^d)\). Write \(m_i=\int x_i\,d\mu(x)\) and \(v_i=\int(x_i-m_i)^2\,d\mu(x)\). The energy is the diagonal potential-and-interaction model
\[
E(\mu)=\frac12\int\sum_{i=1}^d a_i x_i^2\,d\mu(x)
+\frac18\iint\sum_{i=1}^d\beta_i(x_i-y_i)^2\,d\mu(x)d\mu(y).
\]
The parameters \(a_i,\beta_i\) are strictly positive and fixed. Hence \(E(\mu)\ge0\), with equality exactly at \(\mu=\delta_0\). Each iteration independently draws one coordinate \(I_k\) with \(\Pr(I_k=i)=p_i>0\), and applies the affine pushforward corresponding to step \(\eta_i\) along the negative Wasserstein gradient in coordinate \(i\); other coordinates are unchanged. Steps and probabilities remain fixed over time. There is no finite-particle approximation, stochastic gradient noise, or non-diagonal coupling in the theorem.

Define worst-case annealed rate after \(k\ge1\) by
\[
\mathcal A_k(p,\eta)=\sup_{\mu_0\in\mathcal P_2,\ E(\mu_0)>0}
\frac{\mathbb E[E(\mu_k)]}{E(\mu_0)}.
\]
Define worst-case quenched exponential factor by
\[
\mathcal Q(p,\eta)=\sup_{\mu_0\in\mathcal P_2,\ E(\mu_0)>0}
\limsup_{k\to\infty}E(\mu_k)^{1/k},
\]
where limits are taken along the single infinite iid coordinate sequence. Almost-sure statements hold simultaneously for all deterministic \(\mu_0\) on the probability-one event where every coordinate frequency converges.

## Proof

**1. Exact mean–fluctuation decomposition.** The identity
\[\iint(x_i-y_i)^2\,d\mu(x)d\mu(y)=2v_i\]
gives
\[
E(\mu)=\frac12\sum_i\bigl(a_i m_i^2+b_i v_i\bigr),\qquad
b_i=a_i+\beta_i/2.
\]
Its Wasserstein gradient in the selected coordinate is
\[
G_i[\mu](x)=a_i m_i+b_i(x_i-m_i).
\]
Thus the affine update \(x_i'=x_i-\eta_iG_i[\mu](x)\) gives precisely
\[
m_i'=(1-\eta_i a_i)m_i,\qquad
x_i'-m_i'=(1-\eta_i b_i)(x_i-m_i),
\]
while all other coordinate means and variances are unchanged. Correlations between distinct coordinates may be arbitrary because the energy does not depend on them.

For a general square-integrable coordinate perturbation \(T_i\) of mean \(h=\int T_i\,d\mu\), the change in the composed Wasserstein gradient is \(a_i h+b_i(T_i-h)\). Therefore its squared \(L^2(\mu)\) norm is \(a_i^2h^2+b_i^2\operatorname{Var}(T_i)\le b_i^2\int T_i^2\,d\mu\). Equality for a nonconstant mean-zero perturbation on a two-atom measure shows \(b_i\) is the sharp uniform coordinate-gradient Lipschitz constant for this model.

**2. Exact evolution.** Let \(N_i(k)\) count how often coordinate \(i\) is sampled among the first \(k\) steps. The coordinate maps have constant scalar actions on their two invariant modes and commute on the relevant moments. Hence for every realized coordinate sequence,
\[
E(\mu_k)=\frac12\sum_i\left[a_i m_i(0)^2(1-\eta_i a_i)^{2N_i(k)}
+b_i v_i(0)(1-\eta_i b_i)^{2N_i(k)}\right].
\]
Each marginal \(N_i(k)\) is binomial with parameters \(k,p_i\), even though their joint law is multinomial. Therefore
\[
\mathbb E E(\mu_k)=\frac12\sum_i\left[
 a_i m_i(0)^2\bigl(1-p_i[1-(1-\eta_i a_i)^2]\bigr)^k
+b_i v_i(0)\bigl(1-p_i[1-(1-\eta_i b_i)^2]\bigr)^k\right].
\]
For a deterministic initial measure with energy only in a chosen coordinate and mode, equality holds with the corresponding single term. Every mean-mode extreme is realized by a nonzero Dirac mass and every fluctuation-mode extreme by a symmetric two-atom law, both supported on that coordinate axis. Thus
\[
\mathcal A_k(p,\eta)=
\left[\max_i\left\{1-p_i\left(1-r_i(\eta_i)^2\right)\right\}\right]^k,
\quad r_i(\eta)=\max\{|1-\eta a_i|,|1-\eta b_i|\}.
\]
By the strong law of large numbers \(N_i(k)/k\to p_i\) simultaneously for all coordinates. Applying the elementary finite-sum exponential maximum principle to the pathwise identity yields, for the *fixed* initial law, an almost-sure limiting factor equal to the largest of the factors \(|1-\eta_i a_i|^{2p_i}\) and \(|1-\eta_i b_i|^{2p_i}\) over modes initially carrying positive energy (a zero mode factor contributes zero). Taking the supremum over initial laws gives
\[
\mathcal Q(p,\eta)=\max_i r_i(\eta_i)^{2p_i}.
\]
This proves the quenched formula without confusing an almost-sure rate with an expected rate.

**3. Simultaneously optimal coordinate steps.** For \(0<a_i<b_i\), the two affine functions \(1-\eta a_i\) and \(1-\eta b_i\) have a unique positive equioscillation point \(\eta_i^*=2/(a_i+b_i)\). On \(\eta>0\) it uniquely minimizes \(r_i(\eta)\), with minimal square \(t_i\in(0,1)\). Both displayed minimax objectives are increasing in \(r_i\). Every optimal rule therefore uses all these steps. More explicitly, if the modal decrease at a given step is \(d_i(\eta_i)=1-r_i(\eta_i)^2\), then the best sampling value of \(\min_i p_i d_i(\eta_i)\) is at most \((\sum_i 1/d_i(\eta_i))^{-1}\) whenever all decreases are positive; it strictly increases if any \(d_i\) increases. The same harmonic-bound argument applies to the positive logarithmic decreases \(c_i(\eta_i)=-\log r_i(\eta_i)^2\). Hence replacing any nonoptimal step by its equioscillating value strictly improves each globally optimized criterion.

At these steps the mean and centered multipliers are opposite with equal magnitude. Thus an update of coordinate \(i\) multiplies the **entire** coordinate energy by exactly \(t_i\), independently of its current mean, variance, and correlations. For \(E_i(0)=(a_i m_i(0)^2+b_i v_i(0))/2\),
\[
E(\mu_k)=\sum_i E_i(0)t_i^{N_i(k)},\quad
\mathbb E E(\mu_k)=\sum_iE_i(0)(1-p_i\delta_i)^k.
\]

**4. Optimize the two criteria.** Maximizing \(\min_i p_i\delta_i\) on the probability simplex gives the unique equalization \(p_i\delta_i=(\sum_j\delta_j^{-1})^{-1}\), proving \(p^{\mathrm A}\), \(R_{\mathrm A}^*\), and the all-initial-law identity. Maximizing \(\min_i p_i c_i\) instead gives the unique equalization \(p_i c_i=(\sum_jc_j^{-1})^{-1}\), proving \(p^{\mathrm Q}\), \(R_{\mathrm Q}^*\), and the all-initial-law almost-sure rate. Uniqueness follows because any strict inequality between active coordinate factors can be improved by shifting probability from the better coordinate to the worse one. The function \(t\mapsto-\log(t)/(1-t)\) is strictly decreasing for \(0<t<1\), as \(-\log t=\int_t^1 ds/s<(1-t)/t\). Therefore the two probability vectors are equal if and only if all \(t_i\) agree.

**5. Sharp incompatible-risk family.** Fix \(a_1=a_2=1\) and \(\beta_2=4\), so \(b_2=3\), \(t_2=1/4\), and \(\delta_2=3/4\). Let \(\beta_1\downarrow0\) with every \(\beta_1>0\). Then \(t_1\to0\), \(c_1\to\infty\), and \(p_1^{\mathrm Q}\to0\), while \(p_1^{\mathrm A}\to3/7\). The quenched-optimal worst-case expected factor is at least \(1-p_1^{\mathrm Q}\delta_1\to1\), and cannot exceed one; the annealed-optimal factor converges to \(1-(1+4/3)^{-1}=4/7\). The sample-starved coordinate is witnessed exactly by the initial Dirac law at the first coordinate axis. All examples satisfy the strict assumptions before taking the limit.

## Verification

Run `python verify.py` with Python 3. The self-contained script checks 1,197 exact-rational identities and inequalities, including coordinate energy under affine pushforwards, equioscillation, the multinomial/binomial finite-horizon expectation, and the annealed minimax equalization. It separately cross-checks logarithmic equalization and the limiting family numerically. The analytical proof above, rather than finite sampling or enumeration, establishes the arbitrary-dimension, arbitrary-horizon, and almost-sure statements.

## Relationship to prior work

Xu and Li, arXiv:2604.01606v1 (2026), introduce coordinate Wasserstein pushforwards and recommend sampling proportional to directional smoothness with reciprocal-smoothness steps (Algorithm 1 and Theorem 12). Their Section 5.1 treats a quadratic potential-plus-interaction energy. The present classification applies to its **diagonal** subclass and resolves a different question: exact finite-horizon annealed and almost-sure minimax sampling over the full finite-second-moment measure class. The source's general expected-descent guarantee neither determines the almost-sure exponent nor identifies the unique two-risk sampling policies. In this diagonal subclass, its simple directional smoothness estimate \(a_i+\beta_i\) is conservative; the exact coordinate field Lipschitz constant is \(a_i+\beta_i/2\), obtained by separating constant and zero-mean perturbation fields.

Richtárik and Takáč (2016) establish arbitrary-probability Euclidean coordinate-descent complexity bounds and optimize those bounds. Those are conceptual precursors, but do not state the simultaneous exact annealed/quenched minimax classification for the affine mean-and-fluctuation Wasserstein update. Agaskar, Wang, and Lu (2014) explicitly distinguish annealed and quenched randomized Kaczmarz exponents, and provide exact mean-square analysis and sampling optimization in a projection-based linear-system model. That distinction is credited here. A Kaczmarz orthogonal projection has a different mode operator from the present mean/fluctuation pair of generally nonprojective multipliers, and the accessible abstract does not establish the displayed reciprocal-log probability formula for this model. General randomized matrix-product ideas are relevant; equivalent coverage in uninspected historical full text remains possible.

A separate published analysis of inverse-positive SPD quadratic coordinate sampling optimizes the sharp expected-energy factor for **exact one-coordinate minimization**. It does not address two distinct multipliers within each selected Wasserstein coordinate or optimize an almost-sure exponent. That distinction prevents directly importing its optimizer. These comparisons do not constitute a proof of global novelty.

## Limitations

The classification assumes diagonal interactions, strictly positive potential and interaction coefficients, exact affine gradient pushforwards, positive fixed iid coordinate probabilities, and positive fixed stable steps. It does not apply to non-diagonal quadratic interactions, nonquadratic energies, adaptive samplers, state-dependent step choices, gradient noise, finite-particle approximation error, or wall-clock costs. The optimization concerns worst-case initial laws and two explicitly defined error criteria; a distribution-specific policy can outperform it on a particular initial law. The almost-sure exponential rate is not a pathwise guarantee at a fixed finite iteration. No uniform finite-\(k\) tail bound is claimed. Classical random matrix-product methods may provide alternative derivations or equivalent special cases; full historical coverage has not been exhaustively established.

## References

1. Y. Xu and Q. Li, *Random Coordinate Descent on the Wasserstein Space of Probability Measures*, arXiv:2604.01606v1, first posted 2 April 2026. https://arxiv.org/html/2604.01606v1
2. P. Richtárik and M. Takáč, *On optimal probabilities in stochastic coordinate descent methods*, Optimization Letters 10 (2016), 1233–1243, DOI: 10.1007/s11590-015-0916-1; first preprint arXiv:1310.3438.
3. A. Agaskar, C. Wang, and Y. M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, IEEE GlobalSIP (2014), 389–393, DOI: 10.1109/GlobalSIP.2014.7032145.
4. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, SIAM J. Matrix Anal. Appl. 36 (2015), 1660–1690, DOI: 10.1137/15M1025487.
