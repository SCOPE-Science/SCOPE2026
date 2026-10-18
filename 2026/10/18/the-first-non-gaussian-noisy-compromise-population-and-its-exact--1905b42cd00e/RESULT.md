# The first non-Gaussian noisy-compromise population and its exact fourth moment

## Finding
Consider the neutral-utility, always-interacting specialization of the stochastic pairwise opinion-update rule of Siebenmorgen and Restrepo (2026). At each discrete step, an unordered pair of distinct agents is chosen uniformly, they simultaneously compromise with strength \(0<\mu<1\), and the two selected agents receive independent centered Gaussian shocks with variance \(\Delta^2>0\). For \(N\ge2\), the centered opinion vector has a unique stationary distribution \(\Pi_N\) with finite fourth moment. Its exact per-agent stationary variance is
\[
\operatorname{Var}_{\Pi_N}(x_i-\bar x)=\frac{\Delta^2}{2\mu(1-\mu)}\left(\frac{N-1}{N}\right)^2.
\]
The stationary centered vector is jointly Gaussian **if and only if** \(N=2\). Thus three agents are the smallest population in which random partner selection produces non-Gaussian stationary disagreement despite strictly Gaussian microscopic shocks.

For \(N=3\), put \(t=2\mu(1-\mu)\in(0,1/2]\). Every centered coordinate has the exact standardized stationary fourth moment
\[
\boxed{\frac{\mathbb E_{\Pi_3}[(x_i-\bar x)^4]}{\mathbb E_{\Pi_3}[(x_i-\bar x)^2]^2} = \frac{3(16-11t)}{16-12t}}.
\]
Its excess kurtosis is \(3t/(16-12t)>0\), attaining its sharp maximum \(3/20\) at \(\mu=1/2\). These statements form one theorem describing the first departure from the Gaussian representative-agent approximation, with a finite-population variance correction and a quantitative fourth-moment witness.

## Assumptions and scope
There are \(N\ge2\) agents with real opinions \(x_i(k)\). A pair \(e=\{i,j\}\) is sampled uniformly from the \(\binom N2\) possible unordered pairs independently at each integer time. For the chosen pair,
\[
\begin{aligned}
 x_i(k+1)&=(1-\mu)x_i(k)+\mu x_j(k)+\eta_i(k),\\
 x_j(k+1)&=\mu x_i(k)+(1-\mu)x_j(k)+\eta_j(k),
\end{aligned}
\]
while all other coordinates are unchanged. The selected shocks are fresh, independent \(N(0,\Delta^2)\) variables. Their labels refer to the two selected agents; unselected agents receive no shocks. We assume constant positive utility \(U\equiv1\), and the confidence rule is inactive (equivalently, the complete-interaction extension \(\varepsilon=\infty\)). This extension isolates the neutral-utility single-cluster approximation; it is **not** an assertion about perpetual single-cluster membership under finite confidence and unbounded Gaussian noise.

Define \(\bar x=N^{-1}\sum_i x_i\), \(P=I-\mathbf1\mathbf1^\top/N\), and \(d=Px\in H=\{z\in\mathbb R^N:\sum_i z_i=0\}\). Only \(d\), not the uncentered mean opinion, has a stationary law: \(\bar x\) performs a Gaussian random walk. All limits and moments in the theorem concern the Markov chain \(d(k)\).

## Proof
**Step 1: contraction and existence.** Write \(v_{ij}=e_i-e_j\), \(A_{ij}=P-\mu v_{ij}v_{ij}^\top\), and \(\xi_{ij}=P(\eta_i e_i+\eta_j e_j)\). Then \(d'=A_{ij}d+\xi_{ij}\). Put \(t=2\mu(1-\mu)\). For every \(d\in H\),
\[
\|A_{ij}d\|^2=\|d\|^2-t(d_i-d_j)^2,
\qquad
\frac1{\binom N2}\sum_{i<j}(d_i-d_j)^2=\frac{2\|d\|^2}{N-1}.
\]
Hence synchronous coupling with the same edges and shocks contracts squared distance in expectation by
\[
\lambda_N=1-\frac{2t}{N-1}\in[0,1).
\]
It defines a strict contraction in quadratic Wasserstein distance, giving a unique invariant law and geometric convergence in that metric. A finite fourth moment follows from the fourth-power contraction estimate
\[
\mathbb E_e\|A_e d\|^4\le \left(1-\frac{4t(1-t)}{N-1}\right)\|d\|^4,
\]
obtained using \((d_i-d_j)^4\le2\|d\|^2(d_i-d_j)^2\), together with the finite fourth Gaussian shock moment and a small-parameter Young inequality. Symmetry of the transition kernel and uniqueness make the invariant law centered and exchangeable.

**Step 2: exact variance.** The conditional noise covariance is
\[
\Sigma_{ij}=\Delta^2P(e_ie_i^\top+e_je_j^\top)P,
\qquad \operatorname{tr}\Sigma_{ij}=2\Delta^2(1-1/N).
\]
For \(S=\|d\|^2\), the exact scalar moment equation is
\[
\mathbb E[S'\mid d]=\lambda_N S+2\Delta^2(1-1/N).
\]
Solving it at stationarity gives \(\mathbb E S=\Delta^2(N-1)^2/(tN)\). Exchangeability yields \(\mathbb E d_i^2=\mathbb E S/N\), which is the displayed variance because \(t=2\mu(1-\mu)\).

**Step 3: the sharp Gaussianity boundary.** For \(N=2\), there is just one pair; the centered difference is a deterministic-coefficient scalar autoregression with Gaussian innovations and contraction coefficient \(1-2\mu\). Its invariant law is Gaussian.

For \(N\ge3\), suppose instead the unique invariant centered law were multivariate Gaussian. Permutation invariance forces its covariance to be \(\sigma^2P\), \(\sigma^2>0\). Conditional on the selected edge \(ij\), the next state would then be centered Gaussian with covariance
\[
K_{ij}=\sigma^2P-\sigma^2t\,v_{ij}v_{ij}^\top+\Sigma_{ij}.
\]
A finite equally weighted mixture of centered Gaussian laws equals a centered Gaussian law only if all component covariances equal the mixture covariance (apply strict convexity to \(\exp(s^\top K_{ij}s/2)\), for every real \(s\)). Thus stationarity would require \(\Sigma_{ij}=\sigma^2t\,v_{ij}v_{ij}^\top\) for each pair. But \(\Sigma_{ij}\) has rank two on \(H\) for \(N\ge3\), since \(Pe_i\) and \(Pe_j\) are linearly independent, whereas \(v_{ij}v_{ij}^\top\) has rank one. Contradiction. This also proves that the all-agent centered invariant is not Gaussian for any \(N\ge3\).

**Step 4: exact three-agent fourth moment.** Let \(N=3\), \(S=d_1^2+d_2^2+d_3^2\). On the zero-sum plane,
\[
\sum_{i=1}^3d_i^4=\tfrac12S^2,\quad
\mathbb E_e(d_i-d_j)^2=S,\quad
\mathbb E_e(d_i-d_j)^4=\tfrac32 S^2.
\]
For a selected pair, write \(y=A_e d\). Its shock covariance has the two nonzero eigenvalues \(\Delta^2\) and \(\Delta^2/3\). The Gaussian identity
\[
\mathbb E\|y+\xi\|^4=\|y\|^4+2\|y\|^2\operatorname{tr}\Sigma+4y^\top\Sigma y+(\operatorname{tr}\Sigma)^2+2\operatorname{tr}(\Sigma^2)
\]
and \(\mathbb E_e(y_i^2+y_j^2)=(2/3-t)S\) give the **exact** conditional recurrence
\[
\mathbb E[S'^2\mid d]=\left(1-2t+\tfrac32t^2\right)S^2+\tfrac{16-20t}{3}\Delta^2 S+4\Delta^4.
\]
At stationarity \(\mathbb E S=4\Delta^2/(3t)\). Since \(1-(1-2t+3t^2/2)=t(2-3t/2)>0\),
\[
\mathbb E S^2=\frac{4\Delta^4(16-11t)}{9t^2(2-3t/2)}.
\]
Permutation invariance and the zero-sum identity imply \(\mathbb E d_i^4=\mathbb E S^2/6\) and \(\mathbb E d_i^2=\mathbb E S/3\). Their ratio simplifies to \(3(16-11t)/(16-12t)\). The excess \(3t/(16-12t)\) is strictly increasing in \(t\); \(t\) has its unique maximum \(1/2\) at \(\mu=1/2\). The claimed maximum is \(3/20\).

## Verification
The accompanying `check.py` uses only the Python standard library and exact rational arithmetic. Execute `python3 check.py`. It independently checks the pair-averaged second-moment drift for \(N=2,\ldots,9\), exact three-agent zero-sum polynomial identities and fourth-moment recurrence at several rational learning rates, the unique stationary second/fourth-moment formulas, and the endpoint kurtosis \(63/20\). These are finite algebraic checks corroborating, rather than replacing, the preceding proofs for all \(N\), \(\mu\), and positive noise variances.

## Relationship to prior work
Siebenmorgen and Restrepo (2026), main text equations (1), (10)–(15) and Supplementary Material appendices D–F, introduce the pair update and derive an approximate single-cluster Gaussian representative-agent closure with variance \(\Delta^2/[2\mu(1-\mu)]\). They explicitly neglect finite-population correlations. Their work does not assert an exact finite-\(N\) invariant distribution for centered opinions. Here the exact variance has correction \(((N-1)/N)^2\), and the first non-Gaussian invariant occurs already at three agents. These are statements about the **neutral, always-interacting microscopic limit**, not a correction to their approximate stationary distribution of the mean opinion for a nonconstant utility.

The earlier work of Acemoglu, Como, Fagnani and Ozdaglar (2013) studies stochastic gossip with *fixed-opinion stubborn agents*, derives stationary beliefs and their first two moments, but uses a different source of persistent randomness; it does not establish the selected-agent additive-Gaussian calculation here. Boyd et al. (2006) study noiseless randomized gossip convergence, not stationary fluctuations under fresh selected-pair shocks. The general Gaussian-mixture and random-affine-recursion principles used in the proof are standard; novelty is claimed only for the combined model-specific finite-population Gaussianity boundary and exact three-agent kurtosis, subject to historical-priority risk.

## Limitations
The absolute mean opinion has no stationary probability law in this neutral example. Gaussianity is excluded for the centered **joint** law for all \(N\ge3\); a universal positive excess kurtosis formula for each coordinate at arbitrary \(N\) is **not** proved. The displayed explicit fourth-moment coefficient applies only to \(N=3\). The exact process assumes independent Gaussian shocks and complete interaction at every step; finite confidence with unbounded shocks does not remain in one cluster indefinitely, and nonconstant utility breaks the linear closure used here. No statement is made about the accuracy of the nonconstant-utility Gibbs approximation in general.

## References
1. A. Siebenmorgen and J. G. Restrepo, *A Utility-Driven Bounded-Confidence Model for Opinion Dynamics*, arXiv:2605.21844, first submitted 2026-05-21. https://arxiv.org/html/2605.21844v1
2. D. Acemoglu, G. Como, F. Fagnani and A. Ozdaglar, *Opinion Fluctuations and Disagreement in Social Networks*, *Mathematics of Operations Research* 38 (2013), 1–27. https://arxiv.org/abs/1009.2653
3. S. Boyd, A. Ghosh, B. Prabhakar and D. Shah, *Randomized Gossip Algorithms*, *IEEE Transactions on Information Theory* 52 (2006), 2508–2530. https://stanford.edu/~boyd/papers/gossip.html
