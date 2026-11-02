# A Gamma-mixed two-type collision transition in recursive 2-DAG ancestry

## Finding

**Theorem.** Fix any \(c\in(0,\infty)\). Consider the uniform recursive directed acyclic multigraph with \(m=m_n\) initial roots and \(n-m\) later vertices, where each later vertex independently draws two ordered parents uniformly **with replacement** among preceding vertices. Assume \(m/n^{2/3}\to c\). Explore the ancestor set of the newest vertex \(n\), in decreasing label order.

Write \(Y_m\) for the number of frontier edges left when vertices above \(m\) have been processed. For each non-root \(k\), let \(Z_k\) count currently active edges ending at \(k\), and put
\[
D_{n,m}:=\sum_{k=m+1}^{n-1}(Z_k-1)_+.
\]
After processing non-roots, allocate the \(Y_m\) frontier edges independently among the \(m\) roots. If \(R_{n,m}\) distinct roots receive at least one edge, put \(E_{n,m}:=Y_m-R_{n,m}\). If \(X_{n,m}\) counts every ancestor of \(n\), including \(n\), then the following identity holds **exactly**:
\[
X_{n,m}=2Y_m-1+D_{n,m}-E_{n,m}.
\]
There is joint weak convergence
\[
\left(\frac{mY_m}{n},D_{n,m},E_{n,m}\right)
\ \Longrightarrow\ (\xi,P_I,P_R),
\qquad \xi\sim\Gamma(2,1),
\]
where, given \(\xi\), the integer random variables \(P_I\) and \(P_R\) are **independent** and
\[
P_I\mid\xi\sim\operatorname{Poisson}\!\left(\frac{\xi^2}{6c^3}\right),
\qquad
P_R\mid\xi\sim\operatorname{Poisson}\!\left(\frac{\xi^2}{2c^3}\right).
\]
In particular, \(X_{n,m}-2Y_m+1\Rightarrow P_I-P_R\). The two mechanisms have conditional mean ratio \(1:3\), and the probability of a completely collision-free ancestry converges to
\[
\mathbb E\exp\!\left(-\frac{2\xi^2}{3c^3}\right).
\]
Conversely, for any deterministic root count with \(m/n^{2/3}\to\infty\) and \(m\le n-1\), \(\Pr(D_{n,m}=E_{n,m}=0)\to1\), so the exact identity simplifies to \(X_{n,m}=2Y_m-1\) with high probability.

## Assumptions and scope

Integers satisfy \(n>m\ge2\), with \(m/n^{2/3}\to c>0\) for the nondegenerate limit. All independent choices are uniform from the available older labels; parallel edges are permitted. A zero-sum convention defines \(D_{n,m}=0\) when no non-root labels lie between \(m\) and \(n\). Counts include every distinct reached root and non-root, but count each distinct vertex only once. The Gamma law uses *shape 2 and rate 1*, with density \(t e^{-t}\) for \(t>0\). Conditional independence is asserted for the limit, not for the finite model. Only the regime \(m\asymp n^{2/3}\) and its collision-free upper side are claimed; no characterization of the subcritical collision process is asserted.

## Proof

**1. The backward process and exact conservation.** Start with \(Y_{n-1}=2\). Conditional on all revealed edges above label \(k\), every active edge has a uniformly chosen endpoint among the \(k\) remaining labels. Consequently
\[
Z_k\mid\mathcal F_k\sim\operatorname{Bin}(Y_k,1/k),
\quad J_k=\mathbf1_{\{Z_k\ge1\}},
\quad Y_{k-1}=Y_k-Z_k+2J_k.
\]
Summing this recurrence from \(k=n-1\) down to \(m+1\) and writing \(Z_k=J_k+(Z_k-1)_+\) gives \(\sum_{k=m+1}^{n-1}J_k=Y_m-2+D_{n,m}\). The red non-root vertices are vertex \(n\) and these \(J_k\)-vertices: exactly \(Y_m-1+D_{n,m}\). The number of red roots is \(Y_m-E_{n,m}\), proving the identity.

**2. The random Yule amplitude.** Set \(W_k=(k+1)Y_k\) and \(n_1=\lfloor n/\log n\rfloor\), and let \(\Xi_n=W_{n_1}/n\). The full-text analysis in Janson (2023, Lemma 3.2 and Theorem 4.3) proves
\[
\Xi_n\Rightarrow\xi\sim\Gamma(2,1),\qquad
\max_{m\le k\le n_1}|W_k/n-\Xi_n|\xrightarrow{\mathsf P}0,
\]
for every \(m\gg\sqrt n\), and its Lemma 2.1 gives \(\mathbb E\max_k W_k^2\le96n^2\). Here \(m\asymp n^{2/3}\), so the hypothesis holds and \(mY_m/n\Rightarrow\xi\). These are **cited premises**, not new lemmas; the proof below independently establishes the new collision law from them and the exact recursion.

**3. Internal rare collisions.** For \(k>m\), let \(I_k=\mathbf1_{\{Z_k\ge2\}}\) and \(b_{k,n}=\Pr(I_k=1\mid\mathcal F_k)\). On the event \(\max W_k/n\le K\) (which has arbitrarily high probability for large \(K\)), binomial expansion yields, uniformly in relevant \(k\),
\[
\left|b_{k,n}-\frac{Y_k(Y_k-1)}{2k^2}\right|
\le C_K\frac{n^3}{k^6},
\quad
\Pr(Z_k\ge3\mid\mathcal F_k)\le C_K\frac{n^3}{k^6}.
\]
The latter probabilities sum to \(O_K(n^3/m^5)=o(1)\); thus with high probability every \((Z_k-1)_+\) is exactly \(I_k\). From the flatness of \(W_k/n\), the compensators satisfy
\[
\sum_{k=m+1}^{n-1}
\left|b_{k,n}-\frac{\Xi_n^2n^2}{2k^4}\right|
\xrightarrow{\mathsf P}0,
\qquad
\sum_{k=m+1}^{n-1}\frac{\Xi_n^2n^2}{2k^4}
=\frac{\Xi_n^2}{6c^3}+o_{\mathsf P}(1).
\]
For \(k>n_1\), the first sum's omitted terms are negligible: Janson's Lemma 2.2 bounds \(\sum_{k>n_1}\Pr(I_k=1)\le24n^2\sum_{k>n_1}k^{-4}=o(1)\). The squared approximating probabilities sum to \(O_{\mathsf P}(n^4/m^7)=o_{\mathsf P}(1)\).

For precision about independence despite the evolving frontier: reveal the history down to \(n_1\), thereby fixing \(\Xi_n\), and realize each later-time \(I_k\) for \(m<k\le n_1\) through a fresh independent uniform variable with threshold \(b_{k,n}\). Use the **same fresh uniforms** with thresholds \(\Xi_n^2 n^2/(2k^4)\) for proxy indicators. Truncation on bounded-amplitude events, the sum-of-errors bound above, and conditional Le Cam approximation show that the internal count is coupled with a Poisson variable of random intensity \(\Xi_n^2/(6c^3)\) with error tending to zero in probability. Truncating any exceptional proxy threshold greater than 1 changes nothing asymptotically.

**4. Root occupancy repeats.** Conditional on the non-root exploration, the \(Y_m\) root endpoint labels are fresh independent uniform draws from \(\{1,\ldots,m\}\). Process them sequentially. The chance that draw \(j\) repeats a root already observed is \((j-1-E_{j-1})/m\), where \(E_{j-1}\) is the number of earlier excess repeats. Replace these adapted Bernoulli indicators by fresh independent Bernoulli trials of deterministic conditional probabilities \((j-1)/m\). On events \(Y_m=O(n/m)\), the expected cumulative discrepancy is at most \(O(Y_m^3/m^2)=o(1)\): indeed \(\mathbb E(E_{j-1}\mid Y_m)\le\binom{j-1}{2}/m\). The squared proxy probabilities also sum to \(O(Y_m^3/m^2)=o(1)\). Le Cam's inequality therefore yields an independent Poisson proxy with parameter \(Y_m(Y_m-1)/(2m)\). Since \(mY_m/n-\Xi_n\xrightarrow{\mathsf P}0\), this parameter equals \(\Xi_n^2/(2c^3)+o_{\mathsf P}(1)\). Root endpoints are fresh after the internal process and can be coupled using uniforms independent of the latter. Hence the two proxies are **jointly conditionally independent given \(\Xi_n\)**. Since \(\Xi_n\Rightarrow\xi\), the asserted stable mixed joint distribution follows, including the residual and the no-collision probability.

**5. Collision-free side of the boundary.** The moment estimate \(\mathbb E W_k^2\le24n^2\) and the binomial factorial moment bound show
\[
\mathbb E D_{n,m}\le\sum_{k>m}\mathbb E\binom{Z_k}{2}
\le12n^2\sum_{k>m}k^{-4}=O(n^2/m^3).
\]
Also \(\mathbb E E_{n,m}\le\mathbb E\binom{Y_m}{2}/m\le12n^2/[m(m+1)^2]=O(n^2/m^3)\). Therefore both counts vanish with probability tending to one when \(m\gg n^{2/3}\), by Markov's inequality.

## Verification

Run \(`python3 checker.py`\) with a standard Python 3 interpreter. The self-contained program uses exact fractions to compare the full \((Y_m,D_{n,m},E_{n,m},X_{n,m})\) distribution from an independent state-space recurrence against exhaustive enumerations of the underlying DAGs for \(m=2\) and \(n=4,5,6\). It also checks the deterministic critical-window compensators and seeded large-sample simulations. Its recorded output is `PASS 17603 exact, algebraic, and seeded simulation assertions`; the independent Monte Carlo averages were \(0.9432\) internal repeats, \(2.91\) root repeats, and \(196.7588\) frontier edges at \(n=10^6\) and \(m=10^4\). These finite checks do not replace the infinite-asymptotic proof above.

## Relationship to prior work

Janson's 2023 preprint (published 2023) supplies the precise backward frontier construction, Yule/Gamma approximation, and flatness and moment bounds needed as **premises**; Section 10.1 analyses multiple-root descendant counts primarily on the different \(m\asymp\sqrt n\) scale and explicitly leaves larger root counts for further analysis. Its established first-order results do not state the two-type mixed-Poisson collision counts or the \(n^{2/3}\) cutoff. Björnberg and collaborators' uniform-attachment fixed-cycle Poisson approximation concerns global counts of small graph cycles, not ancestor-conditioned frontier and root-occupancy collisions. Briend, Calvillo and Lugosi study different questions concerning archaeology and root recovery in random recursive DAGs. Independent collisions can be studied using standard rare-event Poisson coupling, but that tool alone does not provide this model-specific joint Gamma mixture or the \(1:3\) splitting.

## Limitations

The two-parent model allows repeated parent selection; sampling parents without replacement is not covered. The mixed limit is weak convergence with no general explicit convergence rate, assumes deterministic \(m/n^{2/3}\to c\in(0,\infty)\), and does not describe the growing-collision regime below the critical scale. No independent mathematical audit or exhaustive historical priority certification has been performed. The 2024 global cycle-count paper is not identical, although related uniform-attachment models remain a residual priority risk. Gamma conditioning describes the **limiting** pair, not exact finite-sample conditional independence.

## References

1. Svante Janson, *The number of descendants in a random directed acyclic graph*, arXiv:2302.12467, first publicly posted 2023-02-24; *Random Structures & Algorithms* **64** (2024), 768–803. https://arxiv.org/abs/2302.12467 ; full text https://onlinelibrary.wiley.com/doi/full/10.1002/rsa.21195 . See Sections 2–4 and 10.1.
2. Briend, Calvillo and Lugosi, *Archaeology of random recursive dags and Cooper–Frieze random networks*, arXiv:2207.14601, first posted 2022-07-29. https://arxiv.org/abs/2207.14601 .
3. *Approximation of subgraph counts in the uniform attachment model*, *Combinatorics, Probability and Computing* (2024). https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/approximation-of-subgraph-counts-in-the-uniform-attachment-model/BDFB2B1AE2914E86E0BDD6CA981952A7 .
