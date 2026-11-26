# Parity-dependent correlation reversal in fully refilled annihilating complete graphs

## Finding

Fix an integer \(N\ge2\) and a rate \(r>0\). On the complete graph on \(N\) labeled sites, each ordered pair of distinct sites has its own rate-one Poisson attempt clock. If the source is empty, the attempt has no effect. If the source is occupied, the attempt moves its particle to an empty target, or removes both particles when the target is occupied. Independently, a rate-\(r\) Poisson clock resets the occupied set to the full board. All attempt clocks and the refill clock are mutually independent; particle removals are outcomes of attempts, not separate clocks.

Let \(K\) be the stationary occupancy, \(m=\lfloor N/2\rfloor\), \(k_j=N-2j\), and \(a_j=k_j(k_j-1)\) for \(0\le j\le m\). Then
\[
p_j(r)=\Pr(K=k_j)=\frac{r}{r+a_j}\prod_{h<j}\frac{a_h}{r+a_h}.
\]
The occupied subset conditional on \(K=k_j\) is uniform. For distinct sites \(u,v\) with occupancy indicators \(\eta_u,\eta_v\), the covariance is
\[
C_N(r)=\frac{\sum_j a_j p_j(r)}{N(N-1)}-\left(\frac{\sum_j k_j p_j(r)}{N}\right)^2.
\]
For fixed \(N\), as \(r\downarrow0\), this is \(r/[2(N-1)]+O_N(r^2)\) for even \(N\) and tends to \(-1/N^2\) for odd \(N\). For every \(N\ge2\), it is \(2/r+O_N(r^{-2})\) as \(r\to\infty\). Thus for each odd \(N\ge3\) there is a positive rate at which the covariance crosses from negative to positive. For \(N=3\), \(C_3(r)=2(r-2)/(r+6)^2\), and the unique crossing is at \(r=2\).

## Proof

From \(k\) occupied sites, \(k(k-1)\) ordered pairs have both endpoints occupied and thus remove two particles on an attempt. All other attempts preserve the count. From any starting configuration a refill reaches full occupancy; all states reachable from the full configuration form one finite closed communicating class since every such state can also reach full. This gives a unique stationary law, invariant under relabeling of the sites. Its support has count parity \(N\), and relabeling acts transitively on each count level, giving the claimed uniform conditional law.

The stationary inflow to the full-count state from refills of other states is \(r(1-p_0)\), balanced by \(a_0p_0\). For \(1\le j\le m\), stationarity gives \((r+a_j)p_j=a_{j-1}p_{j-1}\), where the final rate \(a_m\) is zero. These balances give the product above. Its normalization also follows by writing each factor as \(p_j=q_j-q_{j+1}\) with \(q_j=\prod_{h<j}a_h/(r+a_h)\), \(q_0=1\), and \(q_{m+1}=0\). At level \(k\), the conditional one-site mean is \(k/N\), and the joint two-site mean is \(k(k-1)/[N(N-1)]\); substitution proves the covariance formula.

As \(r\downarrow0\), the terminal level has probability tending to one. For odd \(N\), that level is a uniformly distributed singleton, giving the negative limit. For even \(N\), the terminal count is zero and each of the \(N/2\) nonterminal levels has probability \(r/a_j+O_N(r^2)\). The factorial moment \(\mathbb E[K(K-1)]\) is therefore \(Nr/2+O_N(r^2)\), and \(\mathbb E K=O_N(r)\), giving the stated positive leading term.

As \(r\to\infty\), \(p_1=N(N-1)/r+O_N(r^{-2})\) and the mass below \(N-2\) is \(O_N(r^{-2})\) (zero when there is no lower level). The pair of vacancies at level \(N-2\) is uniform. The probability of both specified sites being vacant is consequently \(p_1/\binom N2+O_N(r^{-2})=2/r+O_N(r^{-2})\). The product of the two single-site vacancy probabilities is \(O_N(r^{-2})\). Since occupancy covariance equals vacancy covariance, this proves the fast-reset result.

For odd \(N\), the rational covariance, with no poles at positive \(r\), has opposite signs for small and large rates; its finitely many zeros on the positive axis include a negative-to-positive crossing. For \(N=3\), if \(p=r/(r+6)\) is the mass at full occupancy, \(C_3=p-[(1+2p)/3]^2=2(r-2)/(r+6)^2\).

## Verification and scope

`verify_annihilation.py` constructs the original configuration-space generator, solving the stationary equations on all \(2^N\) states. It compares the state probabilities and two-site covariances to the formulas, using NumPy and SciPy for \(2\le N\le7\) and selected positive rates. The reported checks are finite; the proof covers all fixed finite \(N\). There is no claim of general uniqueness for the odd-size crossing, no even-size all-rate sign classification, and no joint large-system/reset limit. A convention with unit total attempt rate per occupied site rescales the clock and the numerical crossing rates.

## Relationship to prior work

The global Poisson resetting principle is standard; see Evans and Majumdar, *Diffusion with Stochastic Resetting*, [arXiv:1102.2704](https://arxiv.org/abs/1102.2704). Krapivsky and Ben-Naim, *Irreversible Reactions and Diffusive Escape*, [arXiv:1503.04236](https://arxiv.org/abs/1503.04236), treat a spatial half-line annihilation/coalescence problem. Reset-induced covariance reversal also arises for nonadjacent sites on finite **coalescing** cycles, where the terminal state is a singleton for all sizes and the fast-reset covariance begins at order \(r^{-2}\); see [Reset-induced long-range correlation reversal in finite coalescing cycles](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-reset-induced-long-range-correlation-reversal-in-finite-coalesci--0788102fd099/RESULT.md). Here the specific content is the complete-graph **paired annihilation** law and the parity-sensitive site covariance under full refills. A singleton makes two sites negatively correlated at weak refill; a single annihilation simultaneously vacates two sites and makes the leading covariance positive at fast refill. No exclusive priority for the general reset-driven reversal mechanism is asserted.
