# A joint Gaussian limit for idle and total rounds in random block-merging shuffles

## Finding

At each round independently shuffle the current labeled blocks uniformly and fuse every adjacent increasing successor pair. Starting with \(n\) singleton blocks, write \(T_n\) for the number of rounds until one block remains and \(Q_n\) for the number of *idle* rounds, in which no fusion occurs. Set \(q=e^{-1}\). As \(n\to\infty\),
\[
\left(\frac{T_n-n}{\sqrt n},\frac{Q_n-qn}{\sqrt n}\right)
\Longrightarrow N_2\!\left(0,
\begin{pmatrix}1&2q\\2q&q+2q^2\end{pmatrix}\right).
\]
In particular, \(\operatorname{Var}(Q_n)/n\to q+2q^2\), \(\operatorname{Cov}(T_n,Q_n)/n\to2q\), and the limiting correlation is \(2\sqrt q/\sqrt{1+2q}\). For the productive-round count \(T_n-Q_n\), its asymptotic variance divided by \(n\) is \((1-q)(1-2q)\).

The coupling statement is stronger. Let \((Y_i)_{i\ge1}\) be independent Poisson variables of mean one, \(Z_i=\mathbf1\{Y_i=0\}\), \(\tau_m=\inf\{t\ge0:\sum_{i=1}^tY_i\ge m\}\), and \(H_m=\sum_{i=1}^{\tau_m}Z_i\). For every \(n\ge2\) the two processes can be realized so that \(T_n\ge\tau_{n-1}\), \(Q_n\ge H_{n-1}\) and
\[
\|T_n-\tau_{n-1}\|_2+\|Q_n-H_{n-1}\|_2=O(\log n).
\]
The constant in the last estimate is universal.

## Assumptions and scope

A shuffle on \(k\ge2\) blocks is a fresh uniform permutation of \(1,\ldots,k\). A bond occurs when a value \(j\) is immediately followed by \(j+1\) in that ordering, with \(1\le j<k\). Merge all maximal such runs simultaneously, then relabel the survivors in increasing order. If \(R_k\) is the number of bonds, the next state is \(k-R_k\), and an idle round means \(R_k=0\). All new shuffles, conditionally on the block count, are independent. The starting state is deterministic \(n\); the state \(1\) is absorbing. The limit is for integer \(n\to\infty\), without tuning the model.

## Proof

**1. Exact decrement moments.** If a prescribed set of \(r\) out of the \(k-1\) directed successor adjacencies must occur, contracting those edges leaves exactly \((k-r)!\) permutations. Hence, for every integer \(0\le r\le k-1\),
\[
\mathbb E(R_k)_r=(k-r)/k.
\]
In particular, \(\mathbb ER_k=(k-1)/k\) and \(\mathbb ER_k^2=2-3/k\). The classical stochastic (indeed likelihood-ratio) domination \(R_k\le_{\mathrm{st}}\operatorname{Pois}(1)\) follows from Brown--Peköz--Ross [2, Corollary 2]; their explicit coupling is prior work, not claimed here.

**2. Quantile coupling and a logarithmic error.** Use independent uniforms each round to generate the current decrement \(R_{K_{i-1},i}\) and an independent-in-time variable \(Y_i\sim\operatorname{Pois}(1)\) in quantile order, so \(0\le R_{K_{i-1},i}\le Y_i\) almost surely. Put \(D_n=\sum_{i=1}^{T_n}(Y_i-R_{K_{i-1},i})\). At state \(k\), the conditional gap has mean \(1/k\). Because \(0\le R\le Y\), \((Y-R)^2\le Y^2-R^2\), whence its conditional second moment is at most \(2-(2-3/k)=3/k\).

By Cauchy--Schwarz, the chance of a positive decrement satisfies
\[
\Pr(R_k>0)\ge\frac{(\mathbb ER_k)^2}{\mathbb ER_k^2}
=\frac{(k-1)^2}{k(2k-3)}\ge\frac49
\qquad(k\ge2).
\]
The last inequality is equivalent to \((k-3)^2\ge0\). A state is never revisited after a positive decrement. If \(V_k\) denotes the number of visits to state \(k\) (zero when skipped), it is stochastically bounded by a geometric variable with success probability \(4/9\). Consequently \(\|V_k\|_2\le C\) uniformly. For the predictable compensator \(A_n=\sum_{i=1}^{T_n}1/K_{i-1}=\sum_{k=2}^nV_k/k\), Minkowski's inequality yields \(\|A_n\|_2=O(\log n)\). Its centered gap martingale has stopped variance bounded by
\[
\mathbb E\bigl(D_n-A_n\bigr)^2\le3\mathbb EA_n=O(\log n).
\]
Thus \(\|D_n\|_2=O(\log n)\).

**3. Comparison of total and idle times.** The cumulative Poisson count dominates the cumulative actual decrement, hence \(\tau_{n-1}\le T_n\). At the Poisson passage time, the number of bonds still required is bounded above by \(D_n\). Given a remaining state with \(h\) required bonds, the number of additional rounds is stochastically dominated by a sum of \(h\) geometric variables with success probability \(4/9\), so its conditional second moment is at most \(C(h+1)^2\). It follows that
\[
\|T_n-\tau_{n-1}\|_2\le C\|D_n+1\|_2=O(\log n).
\]
For each shared round before Poisson passage, \(\mathbf1\{R=0\}-\mathbf1\{Y=0\}\) is nonnegative and at most \(Y-R\) (all variables are integer-valued). Later idle rounds contribute at most \(T_n-\tau_{n-1}\). Therefore
\[
0\le Q_n-H_{n-1}\le D_n+T_n-\tau_{n-1},
\]
proving the asserted joint \(L^2\) comparison.

**4. Renewal Gaussian limit and moments.** Write \(m=n-1\), \(U_i=Y_i-1\) and \(V_i=Z_i-q\). In the canonical rate-one Poisson process, \(\tau_m\) is the ceiling of the time of its \(m\)-th arrival. Thus \(\mathbb E|\tau_m-m|=O(\sqrt m)\), and the passage overshoot \(\sum_{i\le\tau_m}Y_i-m\) has bounded second moment (conditionally, the unconsumed portion of the final unit time interval has length at most one). Stopped-martingale isometry then shows that replacing either centered sum stopped at \(\tau_m\) by its version stopped at deterministic \(m\) incurs an \(L^2\) error \(O(m^{1/4})\). Therefore
\[
\frac1{\sqrt m}\binom{\tau_m-m}{H_m-qm}
=\frac1{\sqrt m}\sum_{i=1}^{m}
\binom{-U_i}{V_i-qU_i}+o_{L^2}(1).
\]
The iid vectors on the right have covariance entries \(\mathbb EU_i^2=1\), \(\mathbb EV_i^2=q(1-q)\), \(\mathbb E(U_iV_i)=-q\). Their covariance matrix is exactly the matrix displayed in the finding. The multivariate iid central limit theorem proves convergence for the Poisson comparison process; the joint logarithmic \(L^2\) error transfers it to \((T_n,Q_n)\). The same \(L^2\) comparison and iid variance calculations give the stated limits of variances and covariance, rather than weak convergence alone. Finally \(m=n-1\) changes the centerings by bounded amounts.

## Verification

Run `python3 verification/verify_card_shuffle.py` using Python 3. No external modules are needed. The program exhaustively enumerates the bond statistic for uniform permutations through eight blocks, evaluates exact rational factorial and mixed-moment recurrences, and computes large-state approximations for the predicted covariance matrix. The checker reported 159 passed assertions on the packaged source. These finite checks are corroboration; proof of the infinite limits is in the preceding four steps.

## Relationship to prior work

Brown, Peköz and Ross [2] introduced the random-merging shuffle and proved stochastic domination of the one-round bond count by a unit Poisson, including an explicit coupling; neither the domination nor this coupling mechanism is presented as new. Chern, Jiu and Simonelli [1] proved the univariate Gaussian limit and asymptotic moments for the total number of rounds. The contribution here is the **joint** limit with the previously untracked idle-round count, the explicit asymptotic covariance, and the two-dimensional logarithmic \(L^2\) coupling. Their univariate theorem alone does not imply this joint distribution, and a marginal Gaussian law is compatible with many different cross-covariances. Fu [4] considers successions in permutations and related waiting times under different dynamics, not these repeated coalescence runs. The 2016 shuffle analysis [3] covers related completion-time calculations; its full text was not available for a decisive line-by-line comparison, leaving a historical-priority risk.

## Limitations

The theorem uses independently uniform reshuffles and the directed successor-bond rule, and does not establish rates in Kolmogorov or total-variation distance or variants with biased reshuffling. The historic-priority assessment remains provisional, particularly for less accessible earlier work. The proof is a mathematical argument corroborated by finite computations, not an independent audit or machine-checked formal proof.

## References

[1] S. Chern, L. Jiu and I. Simonelli, *A central limit theorem for a card shuffling problem*, arXiv:2309.08841 (initial public version September 16, 2023), https://arxiv.org/abs/2309.08841.

[2] M. Brown, E. A. Peköz and S. M. Ross, *A Random Permutation Model Arising in Chemistry*, Journal of Applied Probability 45 (2008), 1060--1070, doi:10.1239/jap/1231340233; author-accessible text: https://people.bu.edu/pekoz/chemistry.pdf.

[3] Z. Rao, et al., *A discrete probability problem in card shuffling*, Communications in Statistics--Theory and Methods 45 (2016), 612--620, doi:10.1080/03610926.2013.834451.

[4] J. C. Fu, *Exact and limiting distributions of the number of successions in a random permutation*, Annals of the Institute of Statistical Mathematics 47 (1995), 435--446, doi:10.1007/BF00773393; https://www.ism.ac.jp/editsec/aism/pdf/047_3_0435.pdf.
