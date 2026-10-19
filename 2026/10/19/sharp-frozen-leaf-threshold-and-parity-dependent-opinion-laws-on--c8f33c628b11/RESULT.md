# Sharp frozen-leaf threshold and parity-dependent opinion laws on stars

## Finding
Consider the pure neighborhood Deffuant–Weisbuch (NDW) dynamics on the fixed unweighted star with \(k\ge2\) leaves, one uniformly random edge per step, homogeneous strict confidence threshold \(\varepsilon>0\), and compromise fraction \(0<\rho\le1/2\). A *fully unreceptive leaf profile* means that none of the leaves would change its opinion upon selection of its incident edge, regardless of the hub opinion; equivalently, every leaf fails its neighborhood-receptivity test.

**Sharp structural boundary.** Such a profile with leaf opinions in \([0,1]\) exists if and only if
\[
0<\varepsilon\le \delta_k:=\frac{\lfloor k/2\rfloor}{k}.
\]

**Persistent wandering at the boundary and below.** When the bound holds, take \(r=\lfloor k/2\rfloor\) leaves with opinion \(1\) and \(k-r\) leaves with opinion \(0\), with any initial hub opinion in \([0,1]\). Every leaf then remains fixed forever. Nevertheless the hub opinion \(H_t\) has, with probability one, the entire interval \([0,1]\) as its set of subsequential limits: for every nonempty relatively open subinterval \(U\subseteq[0,1]\), \(H_t\in U\) infinitely often.

**Exactly classified half-compromise occupation law.** For \(\rho=1/2\), the empirical hub occupation measures \(T^{-1}\sum_{t=0}^{T-1}\delta_{H_t}\) converge weakly almost surely to the law \(\nu_p\) of
\[
Z=\sum_{j=1}^{\infty}2^{-j}B_j,\qquad \mathbb P(B_j=1)=p:=\frac{r}{k},
\]
where the bits are independent. This law has full topological support \([0,1]\) and exact Hausdorff dimension
\[
\dim_H\nu_p=-p\log_2 p-(1-p)\log_2(1-p).
\]
It is Lebesgue-uniform exactly when \(k\) is even. For odd \(k\), it is singular continuous with dimension strictly between \(0\) and \(1\). In particular, the smallest possible such network consists of a hub and two leaves, and for three leaves the dimension is \(-\frac13\log_2\frac13-\frac23\log_2\frac23\).

## Assumptions and scope
Let \(G=K_{1,k}\) have hub \(h\) and leaves indexed \(1,\dots,k\). All opinions lie in \([0,1]\). Each discrete step independently selects exactly one of the \(k\) hub–leaf edges, uniformly. The graph does not rewire. For an oriented neighboring pair \((i,j)\), the pure transitive receptivity distance is \(d(i,j)=|x_i-\frac1{|N(j)|}\sum_{v\in N(j)}x_v|\), with open neighborhood \(N(j)\) and no self-loop. If edge \(\{i,j\}\) is selected, each endpoint independently uses its own oriented test \(d(i,j)<\varepsilon\) and, when receptive, updates by \(x_i\gets x_i+\rho(x_j-x_i)\); both updates use pre-interaction opinions. This is the asymmetric oriented formulation of the NDW rule of Krishnagopal and Porter, using neighborhood parameter \(\sigma=0\). The selection of one edge is an allowed sampling regime of that model. No network adaptation, stubbornness parameter, exogenous noise, or finite-time stopping rule is assumed.

In this star, for a current leaf vector \((\ell_1,\dots,\ell_k)\), let \(\bar\ell=k^{-1}\sum_i\ell_i\). Every hub update is permitted since \(d(h,i)=|H-H|=0<\varepsilon\); leaf \(i\) is permitted to update precisely when \(|\ell_i-\bar\ell|<\varepsilon\). Thus full leaf unreceptivity depends only on the leaf profile and is invariant if attained. The theorem does **not** claim that the hub always fails to converge for every initial condition, nor that every configuration with \(\varepsilon>\delta_k\) reaches consensus.

## Proof
**1. Exact sharp bound on the least mean deviation.** For arbitrary \(\ell_i\in[0,1]\), define \(m=\min_i|\ell_i-\bar\ell|\). If some \(\ell_i=\bar\ell\), then \(m=0\). Otherwise, let \(a\) of the leaves lie strictly below the mean and \(b=k-a\) strictly above it. Let \(L\) and \(U\) be the respective group means. Then \(a,b\ge1\), \(U-L\le1\), and the exact average identities are
\[
\bar\ell-L=\frac b{k}(U-L),\qquad U-\bar\ell=\frac a{k}(U-L).
\]
Every lower leaf is at distance at least \(m\) below \(\bar\ell\), so \(\bar\ell-L\ge m\); similarly \(U-\bar\ell\ge m\). Hence
\[
m\le\frac{\min(a,b)}k(U-L)\le\frac{\lfloor k/2\rfloor}{k}=\delta_k.
\]
Equality is attained by \(r=\lfloor k/2\rfloor\) unit leaves and \(k-r\) zero leaves: their mean is \(p=r/k\), the zero leaves' deviation is \(p\), and the unit leaves' deviation is \(1-p\ge p\). Because the receptivity test is the strict inequality \(<\varepsilon\), all leaves can fail it exactly when \(\varepsilon\le\delta_k\), including equality. This proves the iff statement.

**2. Stochastic affine reduction.** Fix this binary configuration with \(\varepsilon\le\delta_k\). All leaf values remain unchanged at every step, while the hub always receives the selected leaf's old value. If \(B_t\) is that value at the \(t\)-th edge selection, then independent uniform sampling gives iid \(B_t\in\{0,1\}\) with \(\mathbb P(B_t=1)=p=r/k\in(0,1)\), and
\[
H_{t+1}=(1-\rho)H_t+\rho B_{t+1}.
\]
Both maps \(f_0(x)=(1-\rho)x\) and \(f_1(x)=(1-\rho)x+\rho\) contract the interval \([0,1]\). For \(0<\rho\le1/2\) their images cover it because \([0,1-\rho]\cup[\rho,1]=[0,1]\). Consequently the intervals obtained as compositions of all words of length \(n\) cover \([0,1]\) and have length \((1-\rho)^n\). Given an open target interval \(U\) within \([0,1]\), there is some finite word whose entire image lies in \(U\): take any interior point and \(n\) sufficiently large. Every particular finite word of iid bits with both symbols of positive probability occurs infinitely many times almost surely, by applying independence to disjoint successive blocks. Therefore the hub visits \(U\) infinitely often. Apply this to the countable collection of rational subintervals, and use compactness of \([0,1]\): the hub's almost-sure \(\omega\)-limit set is exactly \([0,1]\). Nonconvergence follows immediately. In contrast, \(k=1\) has an always-receptive leaf and two-sided compromise on its single edge, so its two opinions converge and cannot have this behavior.

**3. Occupation law for half-compromise.** With \(\rho=1/2\), repeated substitution gives
\[
H_t=2^{-t}H_0+\sum_{j=0}^{t-1}2^{-j-1}B_{t-j}.
\]
For a fixed positive integer \(M\), truncating to the \(M\) most recent bits changes this value by at most \(2^{-M}\) whenever \(t\ge M\). Frequencies of each prescribed \(M\)-bit word converge almost surely to their product Bernoulli probabilities: split the observation times into \(M\) residue classes and use the strong law on disjoint blocks. For any Lipschitz continuous test function, the time average of its value at \(H_t\) therefore converges, by sending first \(t\to\infty\) and then \(M\to\infty\), to its expectation at \(Z=\sum_{j\ge1}2^{-j}B_j\). Lipschitz functions determine weak convergence on compact \([0,1]\), proving the claimed empirical law. The binary cylinder of length \(n\) with \(s\) ones has \(\nu_p\)-mass \(p^s(1-p)^{n-s}\). Every finite word has positive mass, so support is all of \([0,1]\). For \(p=1/2\), the masses of all level-\(n\) dyadic intervals are \(2^{-n}\), proving that \(\nu_p\) is Lebesgue measure.

**4. Odd-degree singularity and exact dimension.** For \(p\ne1/2\), the strong law implies that \(\nu_p\)-almost every point has binary-digit frequency \(p\), whereas Lebesgue-almost every point has frequency \(1/2\); ambiguous dyadic expansions form a null set for both measures. Thus \(\nu_p\) is singular. The same strong law yields, on \(\nu_p\)-almost every non-dyadic code,
\[
-\frac1n\log_2\nu_p(I_n)\longrightarrow -p\log_2p-(1-p)\log_2(1-p),
\]
where \(I_n\) is its length-\(2^{-n}\) dyadic cylinder. The standard dyadic entropy-dimension lemma (proved by typical-word counting for the upper bound and the dyadic mass-distribution estimate on high-measure uniform-convergence sets for the lower bound) gives the displayed Hausdorff dimension. Explicitly, typical words have at most \(2^{n(h(p)+o(1))}\) possible cylinders, yielding the upper bound; restricting the measure to a positive-mass set where \(\nu_p(I_n)\le2^{-n(h(p)-\eta)}\) for all large \(n\) gives the lower bound \(h(p)-\eta\), then \(\eta\downarrow0\). Since \(p\in(0,1)\) and \(p\ne1/2\) for odd \(k\), this dimension lies strictly between \(0\) and \(1\). The law is nonatomic because the mass of a prescribed infinite binary string is bounded by \(\max(p,1-p)^n\to0\). This finishes the proof.

## Verification
The standalone standard-library `verification.py` reproduces the exact oriented NDW star updates using rational arithmetic, checks the boundary over 19,525 rational-grid leaf profiles for \(2\le k\le6\), checks all canonical binary frozen profiles and 80 exact transitions per \(k\), constructs every dyadic cylinder through length nine, and verifies the stationary mean and variance identities for \(2\le k\le30\). Run `python3 verification.py` alongside this file. The verified finite tests are not substitutes for the preceding arbitrary-\(k\) inequality, almost-sure word-occurrence argument, or entropy-dimension proof.

## Relationship to prior work
Krishnagopal and Porter introduced neighborhood-based Deffuant–Weisbuch dynamics with asymmetric transitive receptivity and illustrated nonstandard opinion phenomena, including nonconvergent-looking finite simulations. Their available 2024 manuscript and 2025 revision do not state the star-specific sharp full-freeze threshold, almost-sure full-interval \(\omega\)-limit, or parity-dependent limiting occupation law established here. The standard Deffuant model's cluster-convergence theory instead assumes symmetric dyadic confidence interactions and does not imply this result: the hub responds to a frozen leaf, but the leaf never reciprocates. The dimension computation uses the classical entropy law for biased binary Bernoulli measures; the contribution is the exact, sharp reduction of the prescribed opinion model to that process and its resulting social-network phase statement, not a new general theorem about Bernoulli measures.

## Limitations
The result concerns a fixed star, independent uniform single-edge sampling, homogeneous positive confidence bounds, and pure transitive coupling \(\sigma=0\). General graph topologies, nonzero dyadic mixing, network adaptation, multiple edge selections per synchronous time step, and nonuniform sampling are not classified here. Full support and dense sample paths do not imply uniform occupation: odd star degree gives a singular limit measure. The sharp bound concerns **existence of completely unreceptive leaves**, not a universal consensus threshold. A later source revision clarifies asymmetric endpoint tests; we use those explicit tests throughout. Originality is a best-knowledge literature comparison rather than a proof of global uniqueness. Independent audit is not performed.

## References
1. S. Krishnagopal and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Neighborhood Effects*, arXiv:2402.05368v1 (first public 2024-02-08), Sections II–III and V–VIII, https://arxiv.org/html/2402.05368v1.
2. S. Krishnagopal and M. A. Porter, same work, arXiv:2402.05368v2 (2025 revision), Sections II–V, especially Eq. (3) and Figure 2, https://arxiv.org/html/2402.05368v2.
3. J. Gómez-Serrano, C. Graham, and J.-Y. Le Boudec, *The Bounded Confidence Model Of Opinion Dynamics*, arXiv:1006.3798v3, https://arxiv.org/html/1006.3798v3.
4. A. Dubovskaya et al., *Analysis of Mean-Field Approximation for Deffuant Opinion Dynamics on Networks*, SIAM Journal on Applied Mathematics 83 (2023), DOI:10.1137/22M1499765.
5. Y. Peres, K. Simon, and B. Solomyak, *Absolute continuity for random iterated function systems with overlaps*, Journal of the London Mathematical Society 74 (2006), DOI:10.1112/S0024610706023258 (background on random affine systems; no claim of the present NDW specialization).
