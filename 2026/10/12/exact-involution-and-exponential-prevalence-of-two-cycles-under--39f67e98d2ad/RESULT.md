# Exact involution and exponential prevalence of two-cycles under dominant antagonistic coupling

## Finding

For the synchronous binary multiplex majority model of Hughes, Kusmartseva, Muschert, Jelinek and Kusmartsev, a sufficiently strong negative one-to-one interlayer interaction produces a completely solvable global dynamical phase. Let the two layers have \(N\ge 1\) correspondingly labeled vertices, with maximum degree \(\Delta\) across both intralayer graphs. For \(J=-j<0\), the full microscopic update is **exactly**
\[
F(A,B)=(-B,-A)
\]
for every initial configuration if and only if \(j>\Delta\), with fair random tie resolution at zero field. Hence every microstate is either stationary or belongs to a strict two-cycle, with exactly
\[
2^N\quad\text{fixed states},\qquad \frac{4^N-2^N}{2}\quad\text{two-cycle orbits}.
\]
For the paper's product initial ensemble at bias \(r\in[0,1]\), the number of paired coordinates which alternate is \(\operatorname{Binomial}(N,2r(1-r))\). In particular,
\[
\mathbb P(\text{stationary})=[r^2+(1-r)^2]^N,\qquad
\mathbb P(\text{strict period two})=1-[r^2+(1-r)^2]^N.
\]
The chance of starting at one of the two homogeneous, oppositely polarized consensus states is exactly \(r^{2N}+(1-r)^{2N}\). For every fixed interior \(r\), nonconstant cycles therefore dominate the initial ensemble exponentially fast as \(N\to\infty\).

## Assumptions and scope

The two intralayer graphs \(G_A,G_B\) are arbitrary finite simple undirected graphs on the same labeled vertex set \(\{1,\ldots,N\}\), not necessarily equal, regular or connected. A configuration consists of two spin vectors \(A,B\in\{-1,+1\}^N\). For each node \(i\), the synchronous evolution is
\[
A_i(t+1)=\operatorname{sign}\!\left(\sum_{k\in\mathcal N_A(i)} A_k(t)+J B_i(t)\right),\qquad
B_i(t+1)=\operatorname{sign}\!\left(\sum_{k\in\mathcal N_B(i)} B_k(t)+J A_i(t)\right).
\]
When a field is zero, the update is a fair random sign as in the motivating model. Write \(d_i^A=|\mathcal N_A(i)|\), \(d_i^B=|\mathcal N_B(i)|\), and \(\Delta=\max_i\{d_i^A,d_i^B\}\). We restrict the main classification to \(J=-j\) with \(j>\Delta\). To discuss sharpness, \(j\ge0\) is permitted; the conclusions fail as a *state-uniform deterministic identity* for \(j\le\Delta\). The finite-population model, rather than its smoothly regularized mean-field approximation, is the object of the theorem.

## Proof

**Dominant-field identity.** At each site, both intralayer spin sums lie between negative and positive respective vertex degrees. When \(j>\Delta\), the sign of \(\sum_{k\in\mathcal N_A(i)}A_k-jB_i\) is \(-B_i\) for every possible spin assignment: the strictly larger antagonistic contribution determines it regardless of all neighbors. Analogously, the sign of the other field is \(-A_i\). Both fields are nonzero, so tie randomness disappears. Thus \(F(A,B)=(-B,-A)\).

**Sharpness.** If \(0\le j<\Delta\), choose the all-positive state in both layers and a site of degree \(\Delta\). Its field in the corresponding layer is \(\Delta-j>0\), whereas the proposed involution would output negative there. If \(j=\Delta\), the same state produces a zero field at a maximum-degree site and therefore a fair random update instead of the fixed deterministic involution. When \(\Delta=0\), the boundary \(j=0\) has zero fields everywhere, with the same failure. Therefore \(j>\Delta\) is also necessary for the update rule to equal that particular deterministic map for *every* configuration. No statement is made that all systems below the threshold must have long cycles or lose polarization.

**Complete orbit census.** Applying the map twice yields \(F^2(A,B)=(A,B)\) for every configuration. The fixed-point equation reads \(A=-B\), which imposes one free binary choice at each of \(N\) sites: exactly \(2^N\) fixed configurations. There are \(4^N\) states in total; the remaining states form disjoint two-element orbits, giving \((4^N-2^N)/2\) distinct strict two-cycles. Sitewise, \(A_i=-B_i\) means the pair remains frozen and \(A_i=B_i\) means the pair changes from \((+1,+1)\) to \((-1,-1)\) or vice versa at each step. Consequently, \(A_i-B_i\) is a first integral and \(A_i+B_i\) alternates sign. In particular, the magnetization difference \(m_A-m_B\) is invariant, while \(m_A+m_B\) alternates sign.

**Product-law probabilities.** Independently for each site, the initialization assigns \(\mathbb P(A_i=+1)=r\) and \(\mathbb P(B_i=+1)=1-r\). The probability of opposite signs, hence a frozen pair, is \(r^2+(1-r)^2\). The probability of equal signs, hence a flipping pair, is \(2r(1-r)\). Independence across sites yields the binomial law and the exact probability of all pairs frozen. The two homogeneous opposed states have independent probabilities \(r^{2N}\) and \((1-r)^{2N}\). Finally, for \(0<r<1\), the quantity \(r^2+(1-r)^2\) is strictly below one, proving exponential decay of the stationary probability, and its complement gives almost-sure two-cycling in the large-population limit.

## Verification

The standalone `verify.py` uses exact integer and rational arithmetic. For every pair of simple undirected graphs on each of \(N=1,2,3\) labeled vertices, it enumerates **all** \(4^N\) initial spin configurations at \(j=\Delta+1\), verifies the one-step map and its involution, and counts fixed states and distinct length-two orbits. It also checks the exact product-law and polarized probabilities at three rational biases, and verifies a boundary witness for \(j\le\Delta\). The checker prints `VERIFY_OK`. The unrestricted theorem follows from the preceding proof, not from the finite census.

## Relationship to prior work

Hughes et al. [1, Sections 2--4] define the same local sign-rule model and initial ensemble, identify two fully homogeneous opposed absorbing configurations, and study numerical metastability and entropy peaks, especially on independent cubic graphs at \(J=-1\). Their examined results do not provide this strong-coupling state-space classification, the exact count of fixed and two-cycle orbits, or the all-bias initial-ensemble law. This finding examines the different parameter region \(J<-\Delta\), for which the dominance mechanism eliminates all intralayer influence on updates.

Goles and Olivos [2] provide the classical general result that symmetric threshold dynamics eventually reach fixed points or period-two orbits. That broad period bound should not be confused with the stronger conclusion here of an **immediate involution on every state**, a sharp state-uniform coupling criterion, exact microstate orbit counts, and explicit ensemble probabilities. The full text of [2] was unavailable for inspection; the accessible abstract establishes the stated general period bound. We do not claim general period-two behavior as novel.

## Limitations

The sharpness refers only to the property that the whole state-transition map equals \((A,B)\mapsto(-B,-A)\) for every configuration. It is **not** a sharp threshold for consensus, metastability, or any broader dynamical classification. The result requires synchronous deterministic sign updates away from ties, fixed undirected intralayer graphs, one-to-one inhibitory cross-links and a scalar uniform coupling. It does not apply to the authors' baseline \(J=-1\), cubic-degree simulations. It does not quantify noise-driven escape when independent noise is applied even at nonzero fields. The binomial and exponential assertions depend on the explicitly specified independent product initialization. The cited 1980 threshold-function article was compared through its accessible abstract rather than complete text; potential more specialized earlier enumerations remain a bibliographic originality risk. No separate independent scientific audit is claimed.

## References

[1] J. C. M. Hughes, A. Kusmartseva, G. Muschert, H. F. Jelinek and F. V. Kusmartsev, *Metastability and Entropy Peaks in Antagonistic Multiplex Consensus Dynamics*, Entropy 28 (2026), article 857, published 1 August 2026, doi:10.3390/e28080857; full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13512852/.

[2] E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187--189, doi:10.1016/0012-365X(80)90121-1.
