# Exact stabilization census and Poisson critical window for cyclic majority automata

## Finding
For every integer \(n\ge3\), let \(F_n\) update every site of a binary cyclic ring simultaneously by the majority of that site and its two nearest neighbors (elementary cellular automaton Rule 232). The *transient length* \(\tau_n(x)\) is the least nonnegative time at which the orbit of \(x\) enters its eventual periodic cycle. For each edge define \(e_i=x_i\oplus x_{i+1}\), with cyclic indexing. Unless every \(e_i=1\), let \(D(x)\) be the maximum length of a cyclic run of 1s in \(e\) between two occurrences of 0. When all \(e_i=1\), set \(D(x)=0\).

**Exact time and sharp maximum.** Every orbit reaches a fixed point, except for the two checkerboards on even rings, which form one two-cycle. For every configuration,
\[
\tau_n(x)=\left\lfloor\frac{D(x)}{2}\right\rfloor.
\]
In particular, the worst-case transient is \(\lfloor(n-1)/2\rfloor\), attained by exactly \(2n\) labelled initial states for every \(n\ge3\).

**Exact finite-size time distribution.** For \(t\ge0\), let \(L=2t+2\), and let \(M_L\) be the \(2L\)-square nonnegative integer matrix whose states are \((j,p)\) with \(0\le j<L\) and \(p\in\{0,1\}\). There is one edge from \((j,p)\) to \((0,p)\); and, when \(j<L-1\), one edge from \((j,p)\) to \((j+1,1-p)\). (The two possible edges record a zero or a one in the binary edge-difference sequence.) Then the number \(A_n(t)\) of labelled binary configurations having transient at most \(t\) is exactly
\[
 A_n(t)=\operatorname{tr}(M_{2t+2}^{\,n})+2\mathbf1_{\{2\mid n\}}.
\]
Consequently the exact law under the uniform initial distribution is \(\Pr(\tau_n\le t)=A_n(t)/2^n\), for all \(n\ge3\) and all integer \(t\ge0\).

**Poisson critical window and typical time.** Consider any sequence of ring lengths \(n_j\to\infty\) and nonnegative integer thresholds \(t_j\) such that, at each length, the initial configuration is sampled uniformly from all \(2^{n_j}\) binary rings and
\[
 n_j\,2^{-(2t_j+3)}\longrightarrow\lambda\in(0,\infty).
\]
Then
\[
 \Pr(\tau_{n_j}\le t_j)\longrightarrow e^{-\lambda},
 \qquad \mathbb E\tau_n=\tfrac12\log_2 n+O(1).
\]
This is a nonvacuous lattice-subsequence critical-window statement: for example, taking \(t_j=j\) and \(n_j=\lfloor8\lambda4^j\rfloor\) realizes any prescribed positive \(\lambda\). No unqualified continuous Gumbel weak limit is asserted, since integer-time scaling has persistent lattice oscillations. Thus worst-case settling grows linearly, while the average grows logarithmically.

## Assumptions and scope
The sites are labelled \(0,\dots,n-1\), indices are modulo \(n\), and one synchronous update is one time step. Initial states are arbitrary unless uniformly random states are explicitly specified. The dynamic is deterministic, without noise or asynchronous updates. A periodic checkerboard is already on its two-cycle at time zero, so its transient length is zero. Runs of 1s in the edge-difference sequence are cyclic and are measured in *edges*. The all-zero edge sequence has \(D=0\); the all-one edge sequence is possible only for even \(n\), when it is given the exceptional convention \(D=0\).

## Proof
**1. Erosion identity.** A cell whose value agrees with either immediate neighbor never changes: with the cell and this neighbor already agreeing, a strict majority in its three-site neighborhood supports the cell, and the agreement persists inductively. Hence every adjacent equal pair (zero edge) remains an adjacent equal pair under all future updates. Between consecutive zero edges, the cell values alternate. The two sites directly next to the stationary adjacent-equal boundary pairs are determined permanently; at each subsequent update the alternating strip loses exactly one unresolved cell from each end until none remains. More precisely, a strip with \(d\) consecutive one edges separates \(d-1\) interior sites, and after \(s\) updates its unresolved alternating interior has length \(\max(d-1-2s,0)\). Its last changing update occurs at time \(\lfloor d/2\rfloor\). Different strips are disjoint and their boundary pairs are stationary, so their transient lengths maximize independently. If there are no zero edges the ring is a checkerboard, and the majority rule flips all bits each step; this is possible only when \(n\) is even. This proves the asserted orbit types and \(\tau_n=\lfloor D/2\rfloor\).

For maximum \(D\), the number of zero edges cannot be zero except for the period-two exception; moreover the parity sum \(\sum_i e_i\equiv0\pmod2\) forces the number of one edges to be even. For odd \(n\), the unique largest possible run uses \(n-1\) one edges and one zero edge. For even \(n\), it uses \(n-2\) one edges and two consecutive zero edges. The maximum transient is thus \(\lfloor(n-1)/2\rfloor\). These maximal edge words have exactly \(n\) possible placements; each edge word has exactly two choices of the first spin, hence exactly \(2n\) maximizers.

**2. Trace formula.** On the cycle, \(\tau_n(x)\le t\) away from the checkerboard exception precisely when there is at least one zero edge and no cyclic run of \(L=2t+2\) consecutive one edges. The assignment \(x\mapsto e\) is two-to-one onto length-\(n\) binary edge words of even total parity. The transition matrix \(M_L\) records the current trailing run length \(j<L\) and the running parity \(p\); reading 0 resets \(j\), while reading 1 increments \(j\) and toggles parity. Every permitted cyclic edge word with at least one zero has a uniquely determined run-length state at every cyclic position. Parity zero on the full cycle permits exactly two cyclic choices for its parity state, so the trace counts exactly twice each permitted even-parity edge word. Conversely, any closed length-\(n\) walk in \(M_L\) must contain a zero (one edges strictly increase \(j\)), and its parity resets after one circuit, giving exactly such an edge word. The two checkerboard spin states occur only when \(n\) is even; their edge words are all ones and therefore are not counted in the matrix trace. Adding them proves \(A_n(t)=\operatorname{tr}(M_L^n)+2\mathbf1_{\{2\mid n\}}\).

**3. Poisson window.** For \(L=2t+2\), let \(I_i\) indicate the event \(e_{i-1}=0\), \(e_i=\cdots=e_{i+L-1}=1\) (indices modulo \(n\)). Along a critical subsequence, \(L\sim\log_2 n\), these constraints involve only \(L+1<n\) edge bits, which are exactly independent fair Bernoulli bits under uniform choice of spin configuration, since the full \(n\) edge bits have only the one global even-parity restriction. Thus \(\mathbb EI_i=2^{-(L+1)}\). Distinct occurrences whose starting points have cyclic distance at most \(L\) are incompatible: the demanded zero edge of one lies among the demanded one edges of the other. For any fixed integer \(k\), a tuple of \(k\) occurrences with pairwise disjoint length-\(L+1\) windows has probability \(2^{-k(L+1)}\) for all sufficiently large \(n\), because their total length is less than \(n\). The number of these ordered tuples is \(n^k(1+O_k(L/n))\); all remaining distinct tuples are incompatible. Consequently the \(k\)th factorial moment of \(N=\sum_i I_i\) satisfies
\[
 \mathbb E(N)_k=(n2^{-(L+1)})^k(1+O_k(L/n))\longrightarrow\lambda^k.
\]
The factorial-moment criterion yields \(N\Rightarrow\operatorname{Poisson}(\lambda)\). Every cyclic run of \(L\) one edges (unless all edges are one) has a preceding zero and hence contributes at least one \(I_i\). Checkerboards have no such zero and already satisfy \(\tau_n=0\). Therefore \(\{\tau_n\le t\}=\{N=0\}\), proving the critical-window probability limit.

**4. Expected settling time.** Set \(t_0=\lfloor\tfrac12\log_2 n\rfloor\). When \(t\) lies within any fixed bounded distance of \(t_0\), the event intensity \(\mu_t=n2^{-(2t+3)}\) is comparable to a constant. For \(t\ge t_0\), the union bound \(\Pr(\tau_n>t)\le C\min(1,\mu_t)\) holds with an absolute constant \(C\), including the last exceptional threshold if a length-\(n\) parity constraint doubles an event probability; the subsequent times have zero tail. For \(t\le t_0\) with \(L=O(\log n)\), two distinct indicators have nonpositive covariance (overlap makes them mutually exclusive, while disjoint windows are independent), so \(\operatorname{Var}N\le\mu_t\). Therefore Chebyshev gives \(\Pr(\tau_n\le t)=\Pr(N=0)\le1/\mu_t\). Applying this bound to the range \(t\ge0\) up to \(t_0\) (where \(L\le\log_2 n+O(1)\)) and summing the geometric upper- and lower-tail bounds yields \(\mathbb E\tau_n=t_0+O(1)\), as asserted.

## Verification
The accompanying standalone `verify.py` uses exact integers and no external dependencies. It independently simulates all \(2^n\) ring configurations for each \(3\le n\le12\), recovers the actual first cycle-entry time, checks the run-length formula and the \(2n\) maximum count, and for every \(0\le t\le\lfloor n/2\rfloor+1\) compares the empirical number of states with transient at most \(t\) against the exact integer matrix trace. It reports 8,184 configuration tests, 55 matrix-count comparisons, and ten maximum tests. These finite checks cannot establish the all-size identity or the asymptotic law; those follow from the proof above.

## Relationship to prior work
Fukś (1997) introduced and analyzed elementary majority Rule 232 in a two-rule density-classification procedure; that work gives erosion of isolated minority bits for special inputs, rather than an all-configuration *cyclic* transient-time formula, an exact time census, or a Poisson scaling law. Inokuchi and Sato (2000) investigate threshold cellular automata with **fixed** boundary conditions and discuss Rule 232 transient lengths in that setting; the current ring result does not follow from merely replacing their boundary conditions. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014) treat general synchronous majority dynamics and eventual period-two behavior, rather than this sharp ring-specific time law and distribution. Search of related available dynamical results found exact transient or cycle-census theorems for different rules/graphs but no result implying all three statements here. A familiar extreme-value result for independent rare binary-word events is used through a self-contained factorial-moment argument; the application to majority-ring settling times and exact trace formula is the contribution, not a claim to a new Poisson limit theorem in isolation.

## Limitations
Novelty is assessed only against the actually inspected available sources and searched records, not an exhaustive historical priority certification. Classical run-distribution theory may contain an equivalent transform in different terminology. Results apply to periodic spatial boundary conditions, binary strict three-site majority and synchronous deterministic updates only. The Poisson law applies to integer subsequences with the specified intensity limit; no continuous unrestricted Gumbel convergence is claimed. The finite verifier provides computational corroboration, not a proof for arbitrary ring sizes.

## References
1. H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules*, Physical Review E **55** (1997), R2081–R2084, DOI: 10.1103/PhysRevE.55.R2081; arXiv:comp-gas/9703001 (submitted March 7, 1997). The journal publication date shown by the publisher is March 1, 1997.
2. S. Inokuchi and T. Sato, *On Limit Cycles and Transient Lengths of Cellular Automata with Threshold Rules*, Bulletin of Informatics and Cybernetics (2000), DOI: 10.5109/13492.
3. I. Benjamini, S. Chan, R. O'Donnell, O. Tamuz and L. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, arXiv:1405.2486 (May 11, 2014).
