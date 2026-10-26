# Exact delay transfer and a universal quadratic boundary for deterministic-first tandem queues

## Finding
Let \(F(c)\) denote the stationary mean waiting time *at the second station*, excluding both service durations. With stationary Poisson input of rate \(\lambda\), deterministic service \(c\) at station one, and iid service \(S\) at station two, assume \(\lambda\max(c,\mathbb ES)<1\). The following linked conclusions hold.

**Pathwise transfer.** For any finite ordered sequence of arrivals \(a_1\le\cdots\le a_n\), any downstream services \(s_i\ge c\) and an initially empty tandem, the final-station departures obey \(D_{2,k}(c)=D_{2,k}(0)+c\) for every \(1\le k\le n\). Equivalently, the total waiting time across both stations with upstream duration \(c\) equals the downstream waiting time with upstream duration zero. This is a deterministic identity, with no Poisson assumption. The condition \(s_i\ge c\) is sharp for uniform validity over arrival/service paths.

**Exact stationary law with a downstream service floor.** If \(S\ge s_*>0\) almost surely and \(\mathbb ES^2<\infty\), then for all \(0\le c\le s_*\) in the stable range,
\[
F(c)=\frac{\lambda\mathbb ES^2}{2(1-\lambda\mathbb ES)}-\frac{\lambda c^2}{2(1-\lambda c)}.
\]
This identity is distribution-free except for two moments of downstream service.

**Universal small-duration law.** Even without any positive essential lower bound, if \(S>0\) almost surely has a continuous law with \(\mathbb E e^{\theta S}<\infty\) for some \(\theta>0\), and \(\lambda\mathbb ES<1\), then
\[
\lim_{c\downarrow0}\frac{F(0)-F(c)}{c^2}=\frac\lambda2.
\]
The limiting quadratic coefficient depends on the external arrival rate only, not the downstream service law.

## Assumptions and scope
Both stations are single-server first-come-first-served queues with unlimited buffers, common order and no losses or blocking. For finite paths the initial state is empty and times/services are nonnegative, including ties resolved by arrival index. For stationary results external arrivals form a rate-\(\lambda\) Poisson process; stage-two service requirements are iid and independent of arrivals. The mean \(F\) measures second-stage queueing delay only. For the second theorem a positive service floor and finite second moment suffice; for the third, strict positivity almost surely, atomlessness, finite exponential moment and \(\lambda\mathbb ES<1\) are assumed. Choose \(c\) small enough for stability and, in the final theorem, for \(\lambda\mathbb EB(c)\mathbb ES<1\).

## Proof
**1. Deterministic transfer.** Set \(X_k(c)=\max\{a_k,X_{k-1}(c)\}+c\) and \(Y_k(c)=\max\{X_k(c),Y_{k-1}(c)\}+s_k\), starting from empty state. For \(c=0\), \(X_k(0)=a_k\) and \(Y_k(0)=\max\{a_k,Y_{k-1}(0)\}+s_k\). The first customer has \(Y_1(c)=Y_1(0)+c\). Suppose this holds for index \(k-1\). Since \(s_{k-1}\ge c\),
\[
X_{k-1}(c)\le Y_{k-1}(c)-s_{k-1}\le Y_{k-1}(0).
\]
Consequently \(X_k(c)\le c+\max\{a_k,Y_{k-1}(0)\}\), while \(X_k(c)\ge a_k+c\). Thus
\[
\max\{X_k(c),Y_{k-1}(c)\}=c+\max\{a_k,Y_{k-1}(0)\},
\]
which proves \(Y_k(c)=Y_k(0)+c\) by induction. Subtracting the arrival epoch and both service requirements from departure times yields \(W_{1,k}(c)+W_{2,k}(c)=W_{2,k}(0)\).

The uniform hypothesis cannot be relaxed. If the first downstream service is \(0<s<c\), take \(a_1=0\) and \(a_2=\varepsilon\) with \(0<\varepsilon<\min\{s,c-s\}\), and an arbitrary second service \(s_2\ge0\). Then \(Y_2(c)=2c+s_2\), whereas \(Y_2(0)=2s+s_2\), so the claimed shift fails by \(c-s>0\). For \(s=0\), choose \(0<\varepsilon<c\) and again the shift fails.

**2. Exact stationary mean when there is a service floor.** Apply the preceding identity to a two-sided stationary Poisson input via finite-prefix approximations and the stationary Lindley limit. Stability ensures the requisite backward maxima are finite almost surely and the waiting-time expectations converge (finite second moments). Therefore \(W_1(c)+W_2(c)=W_2(0)\) almost surely for a Palm-typical customer. Pollaczek–Khinchine at \(c=0\), for the ordinary \(M/G/1\) second station, gives \(F(0)=\lambda\mathbb ES^2/[2(1-\lambda\mathbb ES)]\). At station one, the \(M/D/1\) formula is \(\mathbb EW_1(c)=\lambda c^2/[2(1-\lambda c)]\). Subtraction gives the exact displayed identity.

**3. Quadratic limit without a service floor.** Put \(\rho=\lambda c\). A first-station busy group has size \(B(c)\) with Borel probabilities
\[
\nu_n(c)=\mathbb P(B(c)=n)=\frac{e^{-n\rho}(n\rho)^{n-1}}{n!},\qquad
\mathbb EB(c)=\frac1{1-\rho}.
\]
A typical downstream arrival belongs to a size-biased such group; conditional on its group size \(n\), its position \(r\in\{1,\dots,n\}\) is uniform. Define \(p_r(c)\) as the stationary probability that the \(r\)-th member of a first-stage group finds station two empty. Let \(t_m(c)\) be the expected number of customers in a downstream busy period begun by a customer arriving to an empty downstream server, with exactly \(m\) other arrivals remaining in the present first-stage group. Future groups have their stationary ordinary iid group law.

For all sufficiently small positive \(c\) except the null set of degeneracy parameters, the sample-path derivative and marked-group mass-transport argument of [1, §4, equations (7)–(14)] yields
\[
F'(c)=\frac1{2\mathbb EB(c)}\sum_{n\ge1}\nu_n(c)
\sum_{r=1}^n(2r-n-1)p_r(c)t_{n-r}(c). \tag{1}
\]
This identity itself does not depend on exponential downstream service: the group reversibility in [1, Appendix A.1], the derivative formula in [1, §2], and the conditional factorization in [1, text preceding (14)] require only iid independent second-stage requirements. The exponential assumption in [1, §4] is used subsequently for order comparisons of \(p_r\) and \(t_m\), which are not invoked here. A continuous downstream service law guarantees the usual almost-sure uniqueness of relevant maximizing indices; Poisson gaps provide the remaining nondegeneracy.

We justify a uniform bound for (1). Compress *within* each future first-stage group by setting its \(B-1\) internal arrival gaps to zero, then delete the residual fixed \(c\) from each inter-group gap. The resulting downstream arrival process is a rate-\(\lambda\) compound-Poisson batch process with iid Borel batch sizes \(B(c)\). Its successive interarrival gaps are no larger than those of the original grouped departures. Hence the customer-count length of any busy period beginning with \(m+1\) grouped arrivals is bounded, under the same service sequence, by the corresponding batch-queue busy-period count. That count has expectation
\[
\frac{m+1}{1-\lambda\mathbb EB(c)\mathbb ES},
\]
by the standard branching exploration of an \(M^X/G/1\) busy period. Fixing small \(c_0>0\) so that \(\lambda\mathbb EB(c_0)\mathbb ES<1\), we have \(0\le t_m(c)\le C(m+1)\) for \(0<c\le c_0\), with a constant \(C\) independent of \(c,m\). This bounds the entire contribution in (1) from \(n\ge3\) by \(C\sum_{n\ge3}\nu_n(c)n^3=O(c^2)\), using the Borel distribution.

At \(c\downarrow0\), the grouped departure stream converges locally to the original Poisson arrival stream: the probability a typical arrival belongs to a group larger than one is \(O(c)\), and finite windows can be coupled directly. The exponential-moment hypothesis and subcritical batch comparison provide uniform integrability of the relevant stationary backlog/busy counts. Consequently
\[
p_1(c)\longrightarrow1-\lambda\mathbb ES,\qquad
t_1(c)\longrightarrow\frac2{1-\lambda\mathbb ES}.
\]
For the second member of a group to find station two empty, the preceding member's positive service must finish during the fixed gap \(c\), so \(0\le p_2(c)\le\mathbb P(S\le c)\longrightarrow0\). The quantities \(t_0(c)\) are uniformly bounded by the same batch comparison. Terms with \(n=1\) vanish identically in (1), and the \(n=2\) term equals
\[
\frac{\nu_2(c)}{2\mathbb EB(c)}\big[-p_1(c)t_1(c)+p_2(c)t_0(c)\big]
=-\lambda c+o(c),
\]
because \(\nu_2(c)=\rho e^{-2\rho}=\lambda c+O(c^2)\). We conclude that \(F'(c)=-\lambda c+o(c)\) for almost every sufficiently small \(c>0\). The stationary IPA interchange of [1, Appendix A.2], with its exponential uniform moment bound on the maximizing indices, makes \(F\) locally absolutely continuous down to zero. Integrating proves \(F(c)=F(0)-\lambda c^2/2+o(c^2)\), as claimed.

## Verification
The independent exact-arithmetic script `verify.py` exhaustively checks the sample-path transfer identity on 20,736 four-customer paths, including simultaneous arrivals, zero services and boundary equality \(s_i=c\). It checks an explicit counterexample when \(s_1<c\). The universal limit is established by (1), Borel-group bounds, and passage to \(c\downarrow0\), not by finite simulation. Standard Pollaczek–Khinchine and Borel identities are invoked with their stated stability hypotheses.

## Relationship to prior work
Cao–Hu–Wang [1] proves the nonincreasing downstream waiting-time conjecture for general renewal arrivals and iid second-stage services, and strict decrease for the exponential downstream special case. Their full text contains the first-group derivative, Borel grouping, and mass-transport machinery used in step 3. The **new assertion** is the exact sample-path transfer for a downstream service floor, its global-in-\(c\) mean formula for general service laws, and the universal \(\lambda/2\) quadratic coefficient at zero without a service floor. These are not equivalent to monotonicity or strictness and are not supplied by its exponential-service ordering argument. Palomo–Pender [3] develops the tandem Lindley recursion underlying step 1, without a covering floor-transfer theorem located in the material consulted. Ciucu–Mehri [2] investigates tails of end-to-end sojourn times rather than the small upstream-duration stationary mean coefficient.

## Limitations
The pathwise transfer need not hold once some downstream service is less than \(c\); the universal quadratic asymptotic does not claim an explicit formula at fixed positive \(c\) for such laws. The quadratic theorem assumes positive atomless downstream services with exponential moments; heavy-tailed and service-at-zero laws are not covered. No third-stage queue, blocking, non-FCFS discipline or input other than Poisson is covered by the quadratic coefficient theorem. The finding has received only self-review; independent validation has not occurred.

## References
1. H. Cao, J.-Q. Hu, and Q. Wang, “On Niu’s Conjecture for Two-Station Tandem Queues,” arXiv:2610.22837v1, public 2026-10-16, https://arxiv.org/html/2610.22837v1. Particularly §§2–4, identity (14) and Appendix A.1–A.2.
2. F. Ciucu and S. Mehri, “On the Distribution of Sojourn Times in Tandem Queues,” ACM SIGMETRICS 2025, DOI:10.1145/3727140, https://wrap.warwick.ac.uk/id/eprint/190706/.
3. S. Palomo and J. Pender, “Learning the Tandem Network Lindley Recursion,” Winter Simulation Conference, 2021.
4. Pollaczek–Khinchine mean-waiting identity for an \(M/G/1\) queue (classical).
