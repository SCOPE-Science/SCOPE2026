# Independent-coordinate occupation limits with two noise sources in elephant hypercube walks

## Finding

Fix an integer \(k\ge2\), deterministic initial spins \(x_i\in\{-1,1\}\), and memory parameters \(p_i\in(0,1)\). In the coordinate-wise elephant walk on \(\{-1,1\}^k\), let \(X_i(t)\) be spin \(i\) at global time \(t\) and define the cumulative coordinate occupation imbalance
\[
A_i(n,t)=\sum_{s=0}^{\lfloor nt\rfloor-1}X_i(s),\qquad 0\le t\le1.
\]
Put \(\alpha_i=2p_i-1\). For each coordinate use the normalization
\[
b_i(n)=\begin{cases}
\sqrt n,&\alpha_i<1/2,\\
\sqrt{n\log n},&\alpha_i=1/2,\\
n^{\alpha_i},&\alpha_i>1/2.
\end{cases}
\]
Then the vector process \(\big(A_i(n,\cdot)/b_i(n)\big)_{i=1}^k\) converges jointly in \(D([0,1],\mathbb R^k)\), with the Skorokhod \(J_1\) topology, to independent coordinate processes \(Z_i\):
\[
Z_i(t)=\begin{cases}
\displaystyle\sqrt{k}\,t^{\alpha_i}\int_0^t u^{-\alpha_i}\,dB_i(u)+\sqrt{k-1}\,W_i(t),&\alpha_i<1/2,\\[6pt]
\sqrt{k t}\,N_i,&\alpha_i=1/2,\\[3pt]
k^{1-\alpha_i}t^{\alpha_i}L_i,&\alpha_i>1/2.
\end{cases}
\]
Here the \(B_i,W_i\) are mutually independent standard Brownian motions, the \(N_i\) are independent standard normal variables, and the \(L_i\) are mutually independent nondegenerate classical one-dimensional elephant-walk limits; all listed families are jointly independent. The processes are defined to equal zero at \(t=0\). For \(\alpha_i>1/2\), if the initial spin is \(x_i\), then
\[
\mathbb E L_i=\frac{x_i}{\Gamma(1+\alpha_i)},\qquad
\mathbb E L_i^2=\frac1{(2\alpha_i-1)\Gamma(2\alpha_i)}.
\]

In particular, for \(\alpha_i<1/2\) and \(0\le s\le t\le1\),
\[
\operatorname{Cov}(Z_i(s),Z_i(t))
=\frac{k}{1-2\alpha_i}s^{1-\alpha_i}t^{\alpha_i}+(k-1)s.
\]
At unit time, the sharp Gaussian variance is \(k/(3-4p_i)+k-1\), not the memory-independent Doob-martingale variance of the original walk. For \(p_i=1/2\), the limit is Brownian motion of variance parameter \(2k-1\); at \(p_i=3/4\) it is a time-degenerate Gaussian process \(\sqrt{k t}\,N_i\); for \(p_i>3/4\) it has non-Gaussian elephant-memory scaling.

## Assumptions and scope

At each integer global step \(t\ge1\), independently choose a coordinate \(I_t\) uniformly from \(\{1,\ldots,k\}\). If coordinate \(i\) has so far been selected \(m\) times, its history consists of its initial value and its \(m\) subsequently generated values. Choose one entry uniformly from those \(m+1\) values, copy it with probability \(p_i\) or reverse it with probability \(1-p_i\), and replace the current spin with that value. All auxiliary random choices are independent except for dependence explicitly introduced by copying history. Unselected coordinates hold their values. This is the uniform-coordinate model of Escobar Parra [1]. The claim is for fixed \(k\), all \(p_i\in(0,1)\), and arbitrary fixed deterministic initial spins; it does not concern a varying dimension, adaptive coordinate-selection weights, or random-walk trajectory fluctuations conditional on the coordinate history.

Let \(Y_{i,0}=x_i\) and let \(Y_{i,m}\) be the \(m\)-th subsequently generated coordinate value for \(m\ge1\). For each \(i\), the sequence \((Y_{i,m})_{m\ge0}\) can be generated as an independent ordinary elephant increment sequence, independently of the global selector process. Write
\[
N_i(n)=\sum_{t=1}^n\mathbf1_{\{I_t=i\}},\qquad
T_i(m)=\sum_{j=0}^{m-1}Y_{i,j},\quad T_i(0)=0.
\]
The classical superdiffusive limit appearing above is \(L_i=\lim_{m\to\infty}m^{-\alpha_i}T_i(m)\), which exists almost surely and in \(L^2\) for \(\alpha_i>1/2\).

## Proof

### 1. An exact decomposition, with no independence approximation

The current coordinate spin is \(X_i(t-1)=Y_{i,N_i(t-1)}\). Define
\[
R_i(n)=\sum_{t=1}^n\bigl(1-k\mathbf1_{\{I_t=i\}}\bigr)X_i(t-1).
\]
Every selected old spin appears exactly once in the list \(Y_{i,0},\ldots,Y_{i,N_i(n)-1}\). Thus, pathwise for every integer \(n\ge0\),
\[
\boxed{A_i(n,1)=kT_i(N_i(n))+R_i(n).} \tag{1}
\]
The same identity holds at each truncated time \(\lfloor nt\rfloor\). The embedded \(T_i\) are independent across coordinates, but the clocks \(N_i\) and the corrections \(R_i\) are not independent: equation (1) is an identity, not a heuristic renewal approximation.

### 2. The independent embedded elephant limits

For one coordinate, write \(\alpha=2p-1\), \(T_m=T_i(m)\), and \(\mathcal G_m=\sigma(Y_0,\ldots,Y_{m-1})\). The elementary conditional mean is
\[
\mathbb E[Y_m\mid\mathcal G_m]=\alpha T_m/m\qquad(m\ge1).
\]
Consequently, with
\[
a_m=\prod_{r=1}^{m-1}(1+\alpha/r)
=\frac{\Gamma(m+\alpha)}{\Gamma(1+\alpha)\Gamma(m)},
\]
the sequence \(T_m/a_m\) is a martingale. Its increments equal
\[
\frac{Y_m-\alpha T_m/m}{a_{m+1}},
\]
with predictable conditional variance \([1-\alpha^2(T_m/m)^2]/a_{m+1}^2\). Moreover,
\[
\mathbb E T_{m+1}^2=(1+2\alpha/m)\mathbb E T_m^2+1,
\qquad\mathbb E T_1^2=1. \tag{2}
\]
Recurrence (2) gives \(\mathbb E T_m^2=O(m+m^{2\alpha})\) off criticality and \(O(m\log m)\) at \(\alpha=1/2\), so \(T_m/m\to0\) in \(L^2\) for all \(\alpha<1\). Martingale functional limit theory, or the published one-dimensional elephant-walk invariance principles [2,4,5], then yields
\[
\frac{T_i(\lfloor mt\rfloor)}{\sqrt m}\Rightarrow
G_{\alpha_i}(t):=t^{\alpha_i}\int_0^t u^{-\alpha_i}\,dB_i(u)
\quad(\alpha_i<1/2), \tag{3}
\]
and
\[
\frac{T_i(\lfloor mt\rfloor)}{\sqrt{m\log m}}
\Rightarrow\sqrt t\,N_i\quad(\alpha_i=1/2). \tag{4}
\]
For (3), the normalized martingale bracket converges to \(\int_0^t u^{-2\alpha_i}du\); bounded original increments give Lindeberg, and tightness at the origin follows from the classical elephant invariance principle. At (4), the martingale bracket grows as \(\Gamma(3/2)^2\log m\); over any fixed positive fraction of the horizon the difference of normalized martingales is negligible. Near the origin, Doob's inequality and (2) give tightness, yielding the common normal factor \(N_i\) at all positive times.

For \(\alpha_i>1/2\), the martingale quadratic variation is summable and \(T_i(m)/m^{\alpha_i}\to L_i\) almost surely and in \(L^2\), uniformly after rescaling on compact time intervals. The mean follows from \(\mathbb E T_m=x_i a_m\). The second moment follows by dividing (2) by \(\Gamma(m+2\alpha_i)/\Gamma(m)\), giving the exact finite identity
\[
\frac{\mathbb E T_m^2}{\Gamma(m+2\alpha_i)/\Gamma(m)}
=\frac1{\Gamma(1+2\alpha_i)}+\sum_{r=1}^{m-1}\frac{\Gamma(r+1)}{\Gamma(r+1+2\alpha_i)}.
\]
The resulting convergent beta-integral series is
\[
\sum_{r=1}^\infty\frac{\Gamma(r+1)}{\Gamma(r+1+2\alpha_i)}
=\frac1{\Gamma(1+2\alpha_i)(2\alpha_i-1)}.
\]
The resulting value is \(\mathbb E L_i^2=1/[(2\alpha_i-1)\Gamma(2\alpha_i)]\), as stated. Nondegeneracy for \(\alpha_i\in(1/2,1)\) is classical and also follows from the positive limiting variance.

### 3. The clock-correction martingale, its exact bracket, and independence

Condition on all embedded sequences \(Y_{i,m}\) and reveal selectors \(I_t\) successively. Since the selector at time \(t\) is fresh and uniform, \(R=(R_1,\ldots,R_k)\) is a vector martingale with increments bounded by \(k-1\) in absolute value. Direct averaging over the possible selectors gives, exactly,
\[
\mathbb E[\Delta R_i(t)\mid\mathcal F_{t-1},\mathbf Y]=0,
\]
\[
\mathbb E[\Delta R_i(t)\Delta R_j(t)\mid\mathcal F_{t-1},\mathbf Y]
=\begin{cases}k-1,&i=j,\\-X_i(t-1)X_j(t-1),&i\ne j.
\end{cases} \tag{5}
\]
By the bounded-observable weak law in [1] applied to \(f(x)=x_ix_j\), whose mean under the uniform hypercube law is zero for \(i\ne j\),
\[
\frac1n\sum_{t=1}^{\lfloor nt_0\rfloor}X_i(t-1)X_j(t-1)
\xrightarrow{\mathbb P}0
\quad(0\le t_0\le1). \tag{6}
\]
The convergence is uniform in \(t_0\) in probability: use finitely many rational grid points and the deterministic Lipschitz bound \(|\sum_{t=r}^sX_iX_j|\le s-r+1\). Equations (5)–(6) show that the bracket matrix divided by \(n\) converges uniformly in probability to \((k-1)tI_k\). Bounded jumps imply the conditional martingale functional central limit theorem
\[
\frac{R(\lfloor n\cdot\rfloor)}{\sqrt n}
\Rightarrow\sqrt{k-1}\,W(\cdot). \tag{7}
\]
In fact this is asymptotically independent of the full embedded sequences: conditional on \(\mathbf Y\), the preceding bracket convergence holds in conditional probability for all but a set of \(\mathbf Y\)-environments of vanishing probability, by the tower property. The conditional martingale limit theorem therefore yields convergence of conditional bounded-Lipschitz expectations to those of the same deterministic Gaussian law, in probability over \(\mathbf Y\). Boundedness upgrades this to \(L^1\), so (7) holds jointly and independently of **any bounded, possibly \(n\)-dependent, embedded-sequence statistic**. This is stronger than merely establishing zero covariance with an ordinary elephant walk.

### 4. Random-clock substitution and the three regimes

The multinomial selector law gives, simultaneously for all coordinates,
\[
\sup_{0\le t\le1}\left|\frac{N_i(\lfloor nt\rfloor)}n-\frac tk\right|\to0
\qquad\text{almost surely}. \tag{8}
\]
Each of the limiting paths in (3)–(4) and in the superdiffusive law is continuous. Therefore random-time-change convergence and (8) permit replacing \(N_i(\lfloor nt\rfloor)\) with \(\lfloor nt/k\rfloor\) in the appropriately scaled \(T_i\), with an error tending uniformly to zero in probability. Since the latter deterministic-clock statistics depend only on mutually independent embedded sequences, the conditional independence conclusion after (7) combines with the independent-coordinate elephant limits.

For \(\alpha_i<1/2\), the two terms of (1) are both of order \(\sqrt n\); (3) and (7) give \(\sqrt{k}\,G_{\alpha_i}(t)+\sqrt{k-1}\,W_i(t)\). At \(\alpha_i=1/2\), the first term is of order \(\sqrt{n\log n}\), whereas the clock correction is only \(O_{\mathbb P}(\sqrt n)\), so the limit is \(\sqrt{k t}\,N_i\). If \(\alpha_i>1/2\), then \(n^{\alpha_i}\) dominates \(\sqrt n\) and the limit is \(k^{1-\alpha_i}t^{\alpha_i}L_i\). Joint convergence holds because the number of coordinates is fixed and the correction is jointly Gaussian and independent of the embedded limits.

Finally, for \(s\le t\), the first term's covariance in the diffusive regime is \(k\,t^{\alpha_i}s^{1-\alpha_i}/(1-2\alpha_i)\), and the independent clock term contributes \((k-1)s\). This yields the stated exact covariance and the variance \(k/(3-4p_i)+k-1\).

## Verification

The standalone file `VERIFY.py` checks exact martingale coefficient and bracket identities over all sign configurations for several dimensions; it enumerates all finite selector-and-memory branches of a two-coordinate instance and confirms (1) pathwise; it compares recurrence (2) against exhaustive rational probability trees; and it verifies exact raw coordinate-occupation moments in the \(p_i=1/2\) refresh specialization. The saved output `CHECKS.txt` reports the assertion count and separately labels finite approximations to the superdiffusive moment coefficient as illustrations, not proofs of an infinite limit. These computations validate finite identities that enter the proof. Functional convergence, tightness, bracket convergence, and asymptotic independence are established mathematically in the preceding argument.

## Relationship to prior work

Escobar Parra [1] defines the same finite-hypercube asynchronous elephant model, proves a bounded-observable weak law, and obtains a central limit theorem for the associated Doob martingale. That is not the central limit theorem for the cumulative occupation imbalance \(\sum_{s<n}X_i(s)\); the latter includes a nontrivial embedded-memory contribution and a separate clock-correction contribution. The weak law in [1] is used in (6), with full credit.

Tokumitsu [2] and Baur–Bertoin [4] establish the one-dimensional elephant functional limits used in the embedded coordinate part. They do not address coordinate holding times, multinomial selector dependence, or the additional Brownian term in (7). Tokumitsu's dynamic elephant model [3] has \(\{-1,+1\}\)-valued **increments** whose conditional mean is a combination of a global empirical increment mean and a prescribed environmental bias. The present coordinate occupation process has **held spins** whose update law remembers the embedded per-coordinate history; the two models are not the same process under a parameter substitution. Thus the present claim is the explicitly combined asynchronous-hypercube occupation law, not a claim of novelty for the classical elephant invariance principle, the bounded martingale CLT, or elementary time-change theory.

## Limitations

All coordinates are selected uniformly and independently in a fixed finite dimension, and the memory parameters are strictly interior. The conclusion is for uncentered coordinate-occupation partial sums and finite-horizon functional convergence; it is not a full empirical-process theorem over all observables, does not treat a dimension growing with \(n\), and gives no convergence rates. Although the included literature comparisons did not identify an equivalent theorem, broader historical random-clock or reinforced-walk invariance principles could contain the result as a corollary; definitive historical priority and independent proof audit remain open.

## References

[1] D. A. Escobar Parra, *Coordinate-wise Elephant Random Walk*, arXiv:2607.07022v1, first public 2026-07-08. https://arxiv.org/abs/2607.07022

[2] G. Tokumitsu, *Stable functional CLTs for scaled elephant random walks*, arXiv:2603.13690v1, first public 2026-03-14. https://arxiv.org/abs/2603.13690

[3] G. Tokumitsu, *Functional central limit theorems for the dynamic elephant random walk*, arXiv:2507.01708v1, first public 2025-07-02. https://arxiv.org/abs/2507.01708

[4] E. Baur and J. Bertoin, *Elephant random walks and their connection to Pólya-type urns*, arXiv:1608.01305, 2016. https://arxiv.org/abs/1608.01305

[5] C. F. Coletti, R. Gava, and G. M. Schütz, *Central limit theorem for the elephant random walk*, arXiv:1608.01662, 2016. https://arxiv.org/abs/1608.01662
