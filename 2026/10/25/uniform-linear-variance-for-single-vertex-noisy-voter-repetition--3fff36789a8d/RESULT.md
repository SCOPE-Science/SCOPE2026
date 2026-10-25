# Uniform linear variance for single-vertex noisy-voter repetitions on locally finite graphs

## Finding
For any connected locally finite simple graph \(G\), finite or infinite, and any vertex \(u\) of degree \(\Delta\ge1\), the temporal repetition count at lag \(d\ge1\) in the discrete-time binary noisy voter model has a uniform, explicit linear-in-time variance lower bound. For any noise rate \(0<\varepsilon<1\) and integer \(T\ge d+1\),
\[
\operatorname{Var}(Q_T)\ge \frac{\varepsilon^{\Delta+4}}{2}
\left(1+\left\lfloor\frac{T-d-1}{2d+2}\right\rfloor\right),
\qquad Q_T=\sum_{s=1}^T\mathbf1\{X_s(u)=X_{s+d}(u)\}.
\]
In particular,
\[
\liminf_{T\to\infty}\frac{\operatorname{Var}(Q_T)}{T}
\ge \frac{\varepsilon^{\Delta+4}}{4(d+1)}>0.
\]
The lower bound excludes the logarithmic/sublinear alternative explicitly left unresolved by Benjamini, Helman Tov, and Zhukovskii (2022/2023). Their variance-limit theorem and conditional normal-limit theorem then imply that the **unthinned** count admits a central limit theorem with strictly positive asymptotic variance for every such graph, under their independent, initially fair Bernoulli configuration.

## Assumptions and scope
Let \(G=(V,E)\) be a connected simple graph with every vertex of finite positive degree. At time zero, each vertex has an independent fair binary opinion when the central-limit corollary is invoked; for the finite-sample variance lower bound, initial opinions may have any law independent of future update randomness. At each integer time \(t\ge1\), all vertices independently choose whether to refresh, with probability \(\varepsilon\). On a refresh, the new opinion is a fresh independent fair bit \(Y_t(v)\). Otherwise it is the previous opinion of a neighbor sampled uniformly and independently. Update coins, neighbor selections, and refresh bits are independent across space and time. For a fixed observed vertex \(u\), integer lag \(d\ge1\), and integer sample size \(T\ge d+1\), set \(\zeta_s=\mathbf1\{X_s(u)=X_{s+d}(u)\}\) and \(Q_T=\sum_{s=1}^T\zeta_s\). The graph need not be regular or finite. The bound is quantitative but not asserted to be sharp.

## Proof
Put \(h=2d+2\), choose \(t_j=d+1+jh\le T\), where \(j=0,\ldots,k-1\), and observe that
\[
k=1+\left\lfloor\frac{T-d-1}{h}\right\rfloor.
\]
The only random variables to be left unexposed are selected fresh *bit values* \(U_j=Y_{t_j}(u)\); all refresh coins are exposed, so a fresh bit on a nonrefresh is harmless. The times \(t_j\) are disjoint from every other relevant refresh-bit time \(t_i-d\), \(t_i+d\), or \(t_i+1\).

Define \(A_j\) in terms of update variables **other than all \(U_i\)** as the intersection of: (i) \(u\) refreshes at \(t_j\); (ii) every vertex in the closed neighborhood \(\{u\}\cup N(u)\) refreshes at \(t_j+1\); (iii) \(u\) refreshes at both \(t_j-d\) and \(t_j+d\); and (iv) \(Y_{t_j-d}(u)=Y_{t_j+d}(u)\). No restrictions are placed on copies or refresh bits at intermediate times. Independence gives
\[
\mathbb P(A_j)\ge\frac{\varepsilon^{\Delta+4}}2.
\]
For \(d=1\), the refresh at \(t_j+d=t_j+1\) was already required in (ii), so the actual probability is larger; the displayed bound remains valid. The two endpoint fair bits are independent because \(d\ge1\).

On \(A_j\), the state at \(u\) at time \(t_j\) equals \(U_j\). At time \(t_j+1\), the vertex \(u\) and **all its neighbors** refresh, so every possible recipient of a copy of \(U_j\) is cut off; consequently no state at a later time depends on \(U_j\). States at earlier times are of course unaffected. Exactly the two summands \(\zeta_{t_j-d}\) and \(\zeta_{t_j}\) of \(Q_T\) contain the affected observation \(X_{t_j}(u)\). By (iii)–(iv), their other endpoints both equal a fixed fair bit \(b_j\); hence the joint contribution is
\[
\zeta_{t_j-d}+\zeta_{t_j}=2\mathbf1\{U_j=b_j\}.
\]
Both indices lie in \(1,\ldots,T\) because \(t_j\ge d+1\) and \(t_j\le T\). As the chosen times are separated by \(2d+2\), neither the displayed summands nor their endpoint refresh-bit constraints collide with those of another selected index.

Expose every random variable except the values \(U_j\) at indices for which \(A_j\) occurs, and also expose the bits at all indices for which \(A_j\) fails. This exposure is legitimate because \(A_j\) does not use any selected \(U_i\). Conditional on it, the remaining \(U_j\) are independent fair bits. By the preceding barrier argument, the conditional dependence of \(Q_T\) on them is a sum of independent variables \(2\mathbf1\{U_j=b_j\}\), each having variance exactly one. Thus
\[
\operatorname{Var}(Q_T\mid\mathcal F)=\sum_{j=0}^{k-1}\mathbf1_{A_j}.
\]
The law of total variance yields
\[
\operatorname{Var}(Q_T)\ge\mathbb E[\operatorname{Var}(Q_T\mid\mathcal F)]
=\sum_j\mathbb P(A_j)\ge k\varepsilon^{\Delta+4}/2.
\]
Dividing by \(T\) and letting \(T\to\infty\), with \(k/T\to1/[2(d+1)]\), proves the asserted asymptotic lower bound.

Under the standard independent fair initial configuration, Lemma 2.3 of the cited primary paper proves the existence of the linear variance coefficient unless its logarithmic alternative occurs, and Theorem 2.7 proves a normal limit for the original (not thinned) repetition statistic once \(\log T/T^2=o(\operatorname{Var}(Q_T/T))\). The bound just established gives \(\operatorname{Var}(Q_T/T)\ge c/T\), hence that condition. Consequently, for a finite \(\sigma^2\ge\varepsilon^{\Delta+4}/[4(d+1)]\),
\[
\frac{Q_T-\mathbb E Q_T}{\sqrt{T}}\xrightarrow{\mathrm d}N(0,\sigma^2).
\]
Only the explicit lower bound and its local-resampling proof are derived here; the existence of the variance limit and central-limit implication rely on the cited theorems.

## Verification
The standalone `verify.py` independently implements exact finite-state transition matrices of the synchronous noisy voter model and recursively computes the first two moments of the lagged repetition count, using `fractions.Fraction` throughout. Running `python verify.py` passes 150 exact assertions involving two- and three-vertex graphs, two noise probabilities, lags one through three, and several finite observation horizons. Those checks corroborate the finite formulas and lower-bound direction; they do not replace the infinite-graph or all-time proof above. Source assertions about the existence of variance limits and the CLT were inspected in the original source's Sections 2.2 and 2.3.

## Relationship to prior work
Benjamini, Helman Tov, and Zhukovskii explicitly ask whether the variance of a single-vertex count of lagged repetitions can be sublinear, and prove a dichotomy between logarithmic growth and positive linear growth (Section 2.2, Lemma 2.3). Their Theorem 2.7 establishes the original count's central limit theorem subject to a positive-variance condition, while also offering a thinned version if the condition is not known. The present bound rules out the logarithmic branch on every locally finite graph, including infinite ones, and removes the unthinned theorem's variance condition. Classical finite-state Markov-chain central limit theorems do not alone cover the arbitrary infinite-graph assertion. The related continuous-time/asynchronous noisy-voter fluctuation literature studies different update mechanisms and observables.

## Limitations
Noise must have strictly positive refresh rate, graph degrees must be finite, and the binary refresh law must assign two nondegenerate outcomes independently. The degree-dependent lower bound can be small and is not optimal. The CLT conclusion imports an existing theorem and requires its standard initial-law assumptions. Finite exact computations corroborate but cannot replace the infinite-graph proof; an exhaustive historical-priority determination is not claimed.

## References
1. I. Benjamini, H. Helman Tov, and M. Zhukovskii, *Global information from local observations of the noisy voter model on a graph*, arXiv:2207.01224, first public version 2022-07-04; *Annals of Probability* 51 (2023), DOI:10.1214/23-AOP1637. Sections 2.2 (variance, Lemma 2.3) and 2.3 (normal limit, Theorem 2.7). https://arxiv.org/abs/2207.01224
2. B. Pymar and N. Rivera, *Asymptotic behaviour of the noisy voter model density process*, arXiv:2112.01478 (2021). A distinct update mechanism and global observable. https://arxiv.org/abs/2112.01478
