# Universal first-collision side marks and an exact multi-walker lifetime law on bicliques

## Finding
Let \(A\) and \(B\) be the two vertex parts of \(K_{m,n}\), with \(|A|=m\), \(|B|=n\), and let \(k\) independent continuous-time simple random walkers start at pairwise distinct vertices. Each walker has an independent rate-one exponential jump clock and chooses a neighbor uniformly on jumping. Let \(T\) be their **first collision time** (first jump entering a vertex occupied by another walker), \(L\in\{A,B\}\) the side of this first collision, and \(P\) its unordered pair of involved walkers. Assume integers \(m,n\ge1\), \(2\le k\le m+n\).

**Theorem.** For every such graph, number of walkers, and initial distinct configuration,
\[
\Pr(L=A)=\frac{n}{m+n},\qquad \Pr(L=B)=\frac{m}{m+n}.
\]
Moreover the side mark \(L\) is independent of \(T\), \(P\), and the collision-free trajectory information strictly preceding the collision jump. In particular, the smaller part is *more likely* to contain the first collision, even though a single stationary walker assigns probability \(1/2\) to each part.

For \(a\) walkers in \(A\), put \(b=k-a\) and \(\kappa=m^{-1}+n^{-1}\). Define \(h_a(s)=\mathbb E_a[e^{-sT}]\). For every \(s\ge0\), this transform is the unique solution of
\[
(s+k)h_a(s)=\frac{a(n-b)}n h_{a-1}(s)+\frac{b(m-a)}m h_{a+1}(s)+ab\kappa,
\]
for \(\max(0,k-n)\le a\le\min(m,k)\); terms with coefficients zero are omitted. This reduces the exact many-particle first-collision distribution to at most \(k+1\) transient states, irrespective of graph order.

For fixed \(k\ge2\) and any sequence \(m,n\to\infty\), without an assumption on the ratio of part sizes,
\[
\kappa T\Longrightarrow\operatorname{Exp}\left(\frac{k(k-1)}4\right)
\]
uniformly in the initial number of walkers on each side, among feasible distinct configurations. The first-collision side remains independent of that rescaled time at every finite size.

## Assumptions and scope
Times are continuous, individual jump rates are exactly one, jumps choose uniformly among all neighbors, and all walkers are independent *until* the first meeting; the evolution after the meeting does not enter the statement. Initial locations are deterministic and pairwise distinct. This prevents a collision at time zero. The first collision involves exactly two labeled walkers almost surely because independent continuous-time clocks have no ties. The probability law in the theorem is conditional on any fixed such initial placement. No stationarity assumption is made.

## Proof
**1. Exact killed-state reduction.** Before \(T\), all walker positions are distinct. If there are \(a\) walkers in \(A\) and \(b=k-a\) in \(B\), the rate at which an \(A\)-walker moves to a vacant \(B\)-vertex is \(a(n-b)/n\), changing \(a\) to \(a-1\). The reverse noncolliding rate is \(b(m-a)/m\), changing \(a\) to \(a+1\). Each of the \(ab\) cross-part walker pairs can collide by a \(B\)-walker jumping into its partner's \(A\)-vertex at rate \(1/m\), or by its \(A\)-walker jumping into its partner's \(B\)-vertex at rate \(1/n\). Consequently the total killing rates, separated by destination side, are
\[
q_A(a,b)=\frac{ab}{m},\qquad q_B(a,b)=\frac{ab}{n},\qquad q(a,b)=ab\kappa.
\]
The sum of the four rates is \(k\). Thus the occupation count \(a\) itself is a birth-death chain killed at rate \(ab\kappa\). First-step conditioning on an independent rate-\(k\) exponential waiting time proves the stated recurrence for the Laplace transform. Almost-sure absorption follows since the finite unreduced walker chain is irreducible and every distinct configuration can reach a collision, or by the finite killed-chain system. Uniqueness for \(s\ge0\) follows from transience of the killed finite-state semigroup.

**2. Exact spatial-mark independence.** At every collision-free state and for every unordered pair \(\{i,j\}\) lying across the two parts, the hazard that this pair collides in \(A\) is \(1/m\), and its hazard of colliding in \(B\) is \(1/n\). The ratio of these hazards is the constant \(n:m\), regardless of time, particle labels, present positions, or the number of other walkers. All other jump channels are noncolliding. At any first collision, the standard competing-exponential construction can therefore use an independent Bernoulli mark with success probability
\[
p_A=\frac{1/m}{1/m+1/n}=\frac{n}{m+n},
\]
after the first colliding pair and time have been selected. Equivalently, both marked first-collision compensators are \(p_A\) and \(1-p_A\) times the common unmarked collision compensator, resolved by pair. This proves independence of \(L\) from the first collision time, the colliding pair, and the information prior to the colliding jump. If \(ab=0\), no collision is possible at that instant, so the argument resumes at the first state with cross-part walkers and remains valid.

**3. Fixed-particle rare-collision limit.** For fixed \(k\), write \(Q_{m,n}\) for the transient generator of the killed occupation-count chain on the integer states \(0,\ldots,k\), eventually all feasible when \(m,n\to\infty\). Its off-diagonals are \(a(1-b/n)\) and \(b(1-a/m)\), and its diagonals are \(-k\). Hence \(Q_{m,n}=Q_0+E_{m,n}\), with \(\|E_{m,n}\|=O_k(\kappa)\), where \(Q_0\) is the generator of the \(k\)-particle Ehrenfest chain (each particle switches sides independently at rate one). The irreducible chain \(Q_0\) has unique stationary distribution \(\pi(a)=2^{-k}\binom ka\); its eigenvalues are \(0,-2,-4,\ldots,-2k\). Its zero eigenvalue is simple. The row sum of the perturbation is \(-ab\kappa\), and
\[
\sum_{a=0}^k\pi(a)a(k-a)=\frac{k(k-1)}4.
\]
Finite-matrix simple-eigenvalue perturbation and the spectral gap give a simple leading eigenvalue \(-\kappa k(k-1)/4+O_k(\kappa^2)\), whose spectral projector tends to the projection onto constants; all other eigenvalues have real part bounded away from zero. Therefore, for every fixed \(t\ge0\),
\[
\Pr_a(\kappa T>t)=\bigl(e^{Q_{m,n}t/\kappa}\mathbf1\bigr)_a
\longrightarrow e^{-k(k-1)t/4},
\]
uniformly over \(a\in\{0,\ldots,k\}\). This proves weak convergence to the claimed exponential law, including every deterministic distinct initial placement.

## Verification
`collision_mark_checker.py` uses exact rational arithmetic to derive, independently, the one-step rates from explicit labeled-vertex choices, solve the first-step Laplace systems for the total and each side mark, and check \(\mathbb E[e^{-sT}\mathbf1_{\{L=A\}}]=\frac{n}{m+n}\mathbb E[e^{-sT}]\). It passes 6,133 checks for integers \(1\le m,n\le5\), \(2\le k\le\min(5,m+n)\), and \(s\in\{0,1/3,2\}\). These finite checks corroborate the algebra; the universal and asymptotic statements are proved above, not inferred from enumeration.

## Relationship to prior work
Figueiredo, Iacobelli and Shneer (2019) derive two-walker meeting-time transforms on complete bipartite graphs for a mobile-agent SIS model. Their two-walker calculations should not be counted as new here. The present assertion is the all-\(k\) exact killed occupation-count law, the first-collision *location-side* Bernoulli factor independent of both the pair and lifetime, and the fixed-\(k\) exponential collision limit. Sanders (2009) develops stationary recurrence formulae for *mean intervals between encounters* of many walkers rather than the nonstationary first-collision law. Nguyen (2022) studies many-walker collision measures on the infinite integer lattice rather than finite bicliques or side marks. The standard competing-hazard and finite-matrix methods are acknowledged ingredients. Historical priority is not independently certified.

## Limitations
The independent-mark assertion depends crucially on equal per-walker jump rates and uniform neighbor selection. If walkers have unequal clock speeds, the two orientation hazards for a given opposing pair depend on which walker occupies which part, and the universal side mark generally fails. The exact chain is specific to complete bipartite graphs and collision-free distinct starts. The asymptotic exponential law assumes \(k\) is fixed and *both* side sizes diverge; no growing-particle limit or fixed-small-side limit is established. The probability of a collision at a particular individual vertex is not generally uniform under arbitrary deterministic initial placements.

## References
- D. Figueiredo, G. Iacobelli, S. Shneer, *The end time of SIS epidemics driven by random walks on edge-transitive graphs* (first public 2019-03-21), https://arxiv.org/abs/1903.09178, especially Section 5.3.
- D. P. Sanders, *Exact encounter times for many random walkers on regular and complex networks* (first public 2009-06-04), https://arxiv.org/abs/0906.0810, especially Sections I–II.
- D.-T. Nguyen, *Scaling limit of the collision measures of multiple random walks* (first public 2022-03-16), https://arxiv.org/abs/2203.08523, especially Sections 1 and 5.
