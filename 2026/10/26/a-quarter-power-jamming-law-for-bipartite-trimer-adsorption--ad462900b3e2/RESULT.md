# A quarter-power jamming law for bipartite trimer adsorption

## Finding
Let \(A_n\) and \(B_n\) be disjoint classes of \(n\) initially vacant sites. Each unordered three-site set meeting both classes receives independent rate-one Poisson attempts. An attempted trimer deposits irreversibly if all three sites are vacant. There are no other allowed adsorbates or adsorption events. Let \(R_n\) be the number of vacant sites after jamming (the unique terminal state, reached after finitely many accepted deposits).

**Theorem.** As \(n\to\infty\),
\[
\frac{R_n}{(2n)^{1/4}}\ \Longrightarrow\ |Z|^{3/2},\qquad Z\sim N(0,1).
\]
Equivalently, the limiting distribution function is
\[
F(t)=\begin{cases}0,&t<0,\\2\Phi(t^{2/3})-1,&t\ge0,\end{cases}
\]
where \(\Phi\) is the standard normal distribution function. Its density on \((0,\infty)\) is \(\frac43t^{-1/3}\phi(t^{2/3})\), with \(\phi\) the standard normal density. In particular the jammed vacancy count has non-Gaussian fluctuations on the \(n^{1/4}\) scale, rather than on a fixed or square-root scale.

## Assumptions and scope
The process is on the complete two-type three-uniform hypergraph with allowed edge compositions \((2,1)\) and \((1,2)\). Each allowed unordered triple has the same strictly positive attempt rate, normalized to one; a common change in rate leaves the accepted-event chain unchanged. The class sizes are exactly equal at time zero. The limit is along every integer \(n\ge2\), without a parity restriction. Only the total number of uncovered vertices at jamming is asserted. This is a terminal-time distributional theorem, not a theorem about physical jamming time or mixed-size adsorbates.

## Proof
**1. Exact embedded chain.** Let \(X_k,Y_k\) be the counts vacant in the two classes after \(k\) successful deposits and put \(s_k=X_k+Y_k=2n-3k\), \(d_k=X_k-Y_k\). As long as \(X_k,Y_k\ge1\) and \(s_k\ge3\), the available numbers of edges of types \((2,1)\) and \((1,2)\) are
\[
\binom{X_k}{2}Y_k,\qquad X_k\binom{Y_k}{2}.
\]
Their sum is \(X_kY_k(s_k-2)/2\); hence, conditional on an accepted deposition, the probability of the first type is precisely \((X_k-1)/(s_k-2)\), including the cases where a class contains one vertex. Accordingly \(d_{k+1}-d_k\) equals \(-1\) with this probability and \(+1\) otherwise, and
\[
\mathbb E[d_{k+1}\mid\mathcal F_k]
=\frac{s_k-3}{s_k-2}d_k,\qquad
\operatorname{Var}(d_{k+1}\mid\mathcal F_k)
=1-\frac{d_k^2}{(s_k-2)^2}.
\]
The chain terminates if a class is empty, or at \((X_k,Y_k)=(1,1)\). Both stopping alternatives have no allowed triple.

**2. Normalized martingale and exact product.** For every index with deterministic \(s_k\ge4\), define
\[
p_k=\prod_{j=0}^{k-1}\frac{s_j-3}{s_j-2}
=\frac{\Gamma(2n/3)}{\Gamma((2n+1)/3)}
 \frac{\Gamma((s_k+1)/3)}{\Gamma(s_k/3)},\qquad p_0=1.
\]
Up to the first terminal step, \(M_k=d_k/p_k\) is a martingale. We always stop it before the deterministic size drops below the stated positive cutoff, so no zero denominator is used. Stirling's gamma-ratio estimate gives, uniformly whenever \(s_k\ge n^{1/8}\),
\[
p_k=\left(\frac{s_k}{2n}\right)^{1/3}
\left(1+O(s_k^{-1}+n^{-1})\right).
\tag{1}
\]
At an active step its predictable quadratic-variation increment is
\[
\mathbb E[(M_{k+1}-M_k)^2\mid\mathcal F_k]
=\frac{1-d_k^2/(s_k-2)^2}{p_{k+1}^2},
\tag{2}
\]
and its absolute increment is at most \(2/p_{k+1}\).

**3. Gaussian variable at a mesoscopic cutoff.** Choose \(k_+\) so that \(s_{k_+}\) is the first available integer at most \(n^{1/2}\). For all indices before this cutoff, the stopped martingale has second moment at most \(V_k:=\sum_{j<k}p_{j+1}^{-2}\le Cn\), by (2). If termination occurs while \(s_k\ge n^{1/2}-3\), it occurs with one class empty (the \((1,1)\) alternative is impossible there), and \(|d_k|=s_k\). By (1) this entails \(|M_k|\ge c n^{1/3}s_k^{2/3}\ge c n^{2/3}\). Doob's inequality therefore bounds the chance of such early termination by \(O(n^{-1/3})\).

The deterministic sum of the leading terms in (2) satisfies
\[
\frac{1}{2n}\sum_{j<k_+}p_{j+1}^{-2}
=1-\left(\frac{s_{k_+}}{2n}\right)^{1/3}+o(1)
\longrightarrow1.
\tag{3}
\]
The correction is negligible: for a still-active state, \(d_j^2\mathbf1_{\{j<\tau\}}\le p_j^2M_{j\wedge\tau}^2\) and the stopped-martingale second moment is at most \(Cn\). Consequently
\[
\mathbb E\sum_{j<k_+,j<\tau}
\frac{d_j^2}{(s_j-2)^2p_{j+1}^2}
\le Cn\sum_{s_j\ge n^{1/2}-3}s_j^{-2}=O(n^{1/2})=o(n).
\]
An early stop affects the deterministic sum in (3) only on an event of vanishing probability. Moreover, \(\max_{j<k_+}|M_{j+1}-M_j|/\sqrt{2n}\le C n^{-1/6}(n^{1/2})^{-1/3}=o(1)\). The martingale central limit theorem (or its standard conditional characteristic-function proof using (2)--(3)) therefore yields
\[
Z_n:=\frac{M_{k_+\wedge\tau}}{\sqrt{2n}}\Longrightarrow N(0,1).
\tag{4}
\]
Here \(\tau\) denotes the terminal index, and all normalizations stop before a size below four; the negligible exceptional early-stop paths may be assigned any bounded value.

**4. Frozen randomness through the terminal boundary layer.** Let \(k_-\) be the first index with \(s_{k_-}\le n^{1/8}\). By Doob's \(L^2\) inequality applied between the two cutoffs, including stopping at terminal absorption,
\[
\mathbb E\!\left[\max_{k_+\le k\le k_-}
\frac{|M_{k\wedge\tau}-M_{k_+\wedge\tau}|^2}{2n}\right]
\le \frac{C}{n}\sum_{k_+\le j<k_-}p_{j+1}^{-2}
\le C\left(\frac{n^{1/2}}n\right)^{1/3}=o(1).
\tag{5}
\]
Thus \(M_{k\wedge\tau}/\sqrt{2n}=Z_n+o_{\mathbb P}(1)\) uniformly between cutoffs. The probability that jamming has not occurred by \(k_-\) vanishes: in that event both counts are positive, \(|d_{k_-}|\le s_{k_-}-2\), and (1) forces \(|M_{k_-}|/\sqrt{2n}\le C(s_{k_-}/(2n)^{1/4})^{2/3}=o(1)\). By (4)--(5), this event has probability at most \(\Pr(|Z_n|\le\varepsilon)+o(1)\) for each fixed \(\varepsilon>0\), and then its upper bound tends to zero as \(\varepsilon\downarrow0\).

Therefore, with probability tending to one, the terminal index lies between the cutoffs and one class is empty. In this case \(R_n=s_\tau=|d_\tau|\). From (1) and (5), uniformly on these terminal paths,
\[
\frac{|M_\tau|}{\sqrt{2n}}
=\frac{R_n}{p_\tau\sqrt{2n}}
=\left(\frac{R_n}{(2n)^{1/4}}\right)^{2/3}(1+o(1))
=|Z_n|+o_{\mathbb P}(1).
\]
By the continuous-mapping theorem and (4), \(R_n/(2n)^{1/4}\Longrightarrow |Z|^{3/2}\), as claimed. The stated CDF and density are ordinary changes of variables from a standard Gaussian.

## Verification
Run `python3 verify_adsorption.py` from the same directory, using Python 3.10 or later; there are no third-party dependencies. The script independently enumerates allowed labeled triples and reduces the embedded chain to class counts, checks exact-rational distributions for initial class sizes one through seven, verifies conditional edge-count identities on a grid of states, and checks the gamma-product formula numerically at many finite sizes. At preparation time all 622 assertions passed. Additional Monte Carlo runs at larger sizes produced the expected progression toward the explicitly stated limiting law. Neither finite-state calculations nor simulation replace the martingale proof for unbounded \(n\).

## Relationship to prior work
Penrose and Sudbury formulate graph deposition for monomer blocking and edge dimers (arXiv:math/0503519v1, first publicly posted 2005-03-24). Their graphs and normal approximations do not treat three-site-path deposition or this terminal minority-depletion boundary layer. Bennett and Bohman study random greedy matching in regular uniform hypergraphs (arXiv:1210.3581, first posted 2012-10-12). Their general maximum-unmatched bound controls a proportion, but does not provide the exact \(n^{1/4}\) terminal scale or a non-Gaussian distribution for this two-type hypergraph. Indeed its pair codegree is of order \(n\), its degree is of order \(n^2\), and their bound gives only a much larger order \(n^{3/4+o(1)}\) for the total number unmatched. Their theorem is not being contradicted.

Cieśla and Barbasz study spatially deposited trimers and hexamers on a planar continuum (arXiv:1309.7021, first posted 2013-09-26). Their Section II deposition geometry and Section III numerical coverage and kinetics do not specialize to a complete two-class hypergraph with the above embedded count transition. Talbot, Tarjus, Van Tassel, and Viot's review covers the general physical RSA formalism and mixed adsorbates, rather than this finite-partite terminal scaling limit.

The previously recorded *Balanced substrates optimize exact trimer adsorption: a Pólya-urn profile and a Gaussian design window* (scientific identifier `d94b8bba-d564-45c1-b2bd-743b0b6a5dfc`) treats exactly the same complete-bipartite three-site-path deposition mechanism, but determines probabilities of **perfect coverage** as the starting class sizes vary with a divisible-by-three total. Its Gaussian law is for the normalized *across-composition* perfect-cover profile; it expressly does not provide the entire terminal vacancy distribution on a fixed balanced graph. The present quarter-power law studies a different random observable, the terminal vacancy count, and does not follow from that perfect-cover Gaussian statement. Another earlier record, *Exact residual-vacancy law for competing dimers and trimers on a complete substrate* (`9a74bf00-c1ee-413a-9ea4-f2ab41c54d24`), uses one uncolored pool and two competing particle sizes and obtains a bounded vacancy law; it does not imply the two-type three-site-only scaling theorem. Literature comparisons are limited to the identified relevant primary sources and available research records; no universal historical-priority claim is made.

## Limitations
This result requires two *equally sized* classes, all triples of compositions \((2,1)\) and \((1,2)\), identical edge rates, and no desorption. Unequal initial class sizes, type-dependent rates, finite physical-time observables, and spatially local adsorption require separate analysis. The theorem is distributional; no convergence of unbounded moments is asserted. The literature comparison is not an independently certified exhaustive novelty search.

## References
1. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, *Ann. Appl. Probab.* 15 (2005), 853–889; arXiv:math/0503519v1 (2005-03-24).
2. P. Bennett and T. Bohman, *A natural barrier in random greedy hypergraph matching*, arXiv:1210.3581 (first public version 2012-10-12), later *Combinatorics, Probability and Computing* (2019).
3. M. Cieśla and J. Barbasz, *Random sequential adsorption of trimers and hexamers*, arXiv:1309.7021v1 (2013-09-26).
4. J. Talbot, G. Tarjus, P. R. Van Tassel, and P. Viot, *From car parking to protein adsorption: an overview of sequential adsorption processes*, *Colloids and Surfaces A* 165 (2000), 287–324, DOI 10.1016/S0927-7757(99)00409-4.
