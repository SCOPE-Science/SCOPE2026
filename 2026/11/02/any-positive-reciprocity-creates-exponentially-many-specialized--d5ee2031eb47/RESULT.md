# Any positive reciprocity creates exponentially many specialized equilibria on random rings

## Finding

Consider the specialized public-good equilibria of the directed network game of Huang, Sun, Xu and Zhao, on the simple ring with \(n\ge 3\) vertices. Independently for each ring edge, make it bidirectional with probability \(r\in[0,1]\); otherwise orient it uniformly in one of the two directions. Write \(K_n(r)\) for the number of specialized equilibria (equivalently, digraph kernels). Set
\[
 a=\frac{1+r}{2},\qquad u=a(2-a),\qquad v=a^2.
\]
The following jointly describe the exact existence and multiplicity laws and their asymptotic separation.

**Exact nonexistence and first moment.** For all \(n\ge3\),
\[
 \Pr\{K_n(r)=0\}=\begin{cases}
 2^{1-n}(1-r)^n,&n\text{ odd},\\
 0,&n\text{ even},
 \end{cases}
\]
and
\[
 \mathbb E K_n(r)=\sum_{\substack{s,t\ge0\\2s+3t=n}}
 \frac{n}{s+t}\binom{s+t}{s}u^sv^t
 =\lambda_1^n+\lambda_2^n+\lambda_3^n,
\]
where the \(\lambda_j\) are the three roots, counted with multiplicity, of
\[
 z^3-uz-v=0.
\]

**A sharp reciprocal/one-way dichotomy.** At \(r=0\), \(K_n(0)=1\) unless all edges form one of the two coherent directed cycles: those exceptional orientations give \(K_n(0)=0\) for odd \(n\), and \(K_n(0)=2\) for even \(n\). In contrast, for every **fixed** \(0<r\le1\), there is a constant \(c_r>0\) such that
\[
 \Pr\{K_n(r)\ge 2^{c_r n}\}\longrightarrow1\qquad(n\to\infty).
\]
For \(0<r<1\), an explicit choice is \(c_r=r^4((1-r)/2)^4/36\), and for \(n\ge18\),
\[
 \Pr\{K_n(r)<2^{c_r n}\}\le
 \exp\left(-\frac{n r^4((1-r)/2)^4}{144}\right).
\]
At \(r=1\), the number is the classical Perrin count of maximal independent sets on the cycle, growing exponentially with its plastic-constant base.

**Exact mean growth and small-reciprocity crossover.** Let \(\lambda(r)\) be the positive root of \(z^3-uz-v\). It is the unique dominant root, and for every fixed \(r>0\),
\[
 \mathbb E K_n(r)=\lambda(r)^n(1+o(1)),\qquad \lambda(r)>1.
\]
Near zero, \(\lambda(r)=1+4r/9+O(r^2)\). If \(r=r_n\ge0\) with \(nr_n\to c<\infty\), then
\[
 \mathbb E K_n(r_n)\longrightarrow \exp(4c/9).
\]
Thus the expected-equilibrium crossover occurs at reciprocal-link probability of order \(1/n\), while every fixed positive probability also produces typical exponential multiplicity.

## Assumptions and scope

The underlying undirected graph is the simple labeled cycle \(C_n\), \(n\ge3\). Its edges are independent three-state random variables: clockwise-only and counterclockwise-only, each with probability \((1-r)/2\), or both directions with probability \(r\). These are not independently sampled directed arcs. The network game is the strictly concave local-public-good model with a common contribution threshold \(e^*>0\); a *specialized equilibrium* is one in which each player contributes either \(0\) or \(e^*\). A subset \(S\) of vertices is a *kernel* if no edge in either direction joins two members of \(S\) and every vertex outside \(S\) has an **outgoing** edge to a vertex in \(S\). The cited network-game theorem equates these subsets with specialized equilibria. Other, nonspecialized Nash equilibria are not counted.

## Proof

**1. Kernel existence and the complete one-way law.** A strict orientation of a simple cycle is acyclic unless every edge is directed coherently around the cycle. Every finite acyclic digraph has a unique kernel, obtained recursively by choosing all sinks and deleting their in-neighbors. A coherent directed cycle has exactly two alternating kernels if its length is even, and none if odd. If a ring has a bidirectional edge, choose one direction of every bidirectional edge to obtain a noncoherent strict orientation (choose at least one reverse edge if necessary). Its unique kernel remains a kernel after the removed reverse edges are restored: independence depends only on the underlying undirected edges, and the outgoing-domination condition is preserved by added arcs. Therefore the only kernel-free rings are the two entirely one-way, coherently oriented odd cycles. Each occurs with probability \(((1-r)/2)^n\). This proves the exact probability and the full \(r=0\) classification.

**2. Weighted cycle gaps give the first moment.** Every kernel is a maximal independent set of the underlying undirected cycle. Its cyclic membership word has no adjacent ones (independence) and no three consecutive zeros (domination); hence the distances between successive selected vertices are either two or three edges. A distance-two gap contains one nonselected vertex adjacent to two specialists, which has an outgoing arc to at least one with probability \(1-(1-a)^2=u\). A distance-three gap contains two nonselected vertices, each adjacent to exactly one specialist, and both needed arcs exist independently with probability \(a^2=v\). For a fixed candidate kernel, these edge events use different edges, hence the probabilities multiply. If it has \(s\) distance-two gaps and \(t\) distance-three gaps, its length is \(2s+3t=n\) and its kernel probability is \(u^sv^t\). There are exactly \(\frac n{s+t}\binom{s+t}{s}\) labeled cyclic selections with these gaps: mark one of the \(s+t\) selected vertices, choose its location in \(n\) ways, and order the two gap types. Summing the survival probabilities proves the finite formula.

A direct formal-power-series calculation establishes the root formula without any boundary conventions. If \(F_n\) is the displayed cyclic-gap sum, then
\[
 \sum_{n\ge1}F_n z^n
 =z\frac{d}{dz}\left[-\log(1-uz^2-vz^3)\right]
 =\frac{2uz^2+3vz^3}{1-uz^2-vz^3}.
\]
Indeed, expanding the logarithm as \(\sum_{k\ge1}(uz^2+vz^3)^k/k\) gives precisely the factor \(n/(s+t)\) for each gap composition. Now \(1-uz^2-vz^3=\prod_{j=1}^3(1-\lambda_jz)\), where \(\lambda_j\) are the roots of \(w^3-uw-v\). Taking the logarithmic derivative of that factorization gives \(F_n=\sum_j\lambda_j^n\) for every \(n\ge1\). Equivalently, \(F_n=\operatorname{tr}(T^n)\) for the nonnegative companion matrix
\[
 T=\begin{pmatrix}0&u&v\\1&0&0\\0&1&0\end{pmatrix}.
\]
For example \(F_3=3v\), \(F_4=2u^2\), and \(F_5=5uv\).

**3. Spectral law and crossover.** For \(0\le r\le1\), \(u,v>0\), and the nonnegative matrix \(T\) is primitive because its directed transitions contain closed walks of lengths two and three. Its Perron root \(\lambda(r)\) therefore strictly dominates the other two roots in modulus. Since \(u+v=1+r\), the polynomial \(z^3-uz-v\) is negative at \(z=1\) for \(r>0\), so \(\lambda(r)>1\), while \(\lambda(0)=1\). Implicit differentiation at \(r=0\), using \(u(0)=3/4\), \(v(0)=1/4\), and \(u'(0)=v'(0)=1/2\), gives
\[
 \lambda'(0)=\frac{u'(0)\lambda(0)+v'(0)}{3\lambda(0)^2-u(0)}=\frac49.
\]
The other roots at \(r=0\) are both \(-1/2\), so uniformly for \(r\) sufficiently small their moduli are bounded strictly below one. When \(nr_n\to c\), the root formula consequently yields \(\lambda(r_n)^n\to e^{4c/9}\), and the other root powers tend to zero.

**4. Exponentially many equilibria with high probability.** For \(0<r<1\), consider eight consecutive edges on nine consecutive vertices labeled \(-1,0,1,2,3,4,5,6,7\). Prescribe the four strictly oriented boundary edges \(-1\to0\), \(1\to0\), \(5\to6\), \(7\to6\); prescribe the four central edges \(1\leftrightarrow2\), \(2\leftrightarrow3\), \(3\leftrightarrow4\), \(4\leftrightarrow5\) to be bidirectional. This event has probability
\[
 \gamma_r=r^4((1-r)/2)^4>0.
\]
Vertices \(0\) and \(6\) are sinks (no outgoing arcs) and so belong to every kernel; their immediate neighbors \(1\) and \(5\) are excluded from every kernel. On the remaining internal path \(2,3,4\) there are exactly two feasible patterns, selecting \(\{3\}\) or \(\{2,4\}\). Either choice satisfies all kernel conditions locally, and changing between them never affects a vertex outside the gadget because \(0\) and \(6\) remain selected and the other boundary vertices remain unselected. Thus \(X\) edge-disjoint gadgets entail at least \(2^X\) distinct kernels, provided one exists. One such gadget already guarantees a kernel by Part 1 because the graph is neither a coherent strict odd cycle nor kernel-free.

Take \(m=\lfloor n/9\rfloor\) disjoint nine-edge blocks around the ring and test the first eight edges of each for this pattern. The number \(X\) of successes is exactly \(\mathrm{Binomial}(m,\gamma_r)\). For \(n\ge18\), \(m\ge n/18\). The multiplicative Chernoff bound gives
\[
 \Pr\{X<m\gamma_r/2\}\le e^{-m\gamma_r/8}\le e^{-n\gamma_r/144}.
\]
Outside that event, \(K_n(r)\ge2^X\ge2^{n\gamma_r/36}\). At \(r=1\), every edge is bidirectional, all kernels are the maximal independent sets of \(C_n\), and the Perrin formula from Part 2 at \(u=v=1\) has exponentially growing Perron root. This proves the dichotomy.

## Verification

Run `python3 verify.py` with a standard Python 3 installation. The program separately enumerates every one of the \(3^n\) directed-ring configurations for each \(3\le n\le8\), enumerates all \(2^n-1\) candidate nonempty kernel subsets, and counts them using the literal independence and outgoing-domination definitions. It then compares exact rational expected-kernel counts and exact zero-kernel probabilities at \(r=0,1/4,1/2,3/4,1\) against the theorem formulas. The actual run passed all 9,828 configurations and 60 exact-rational aggregate identities. This finite verification supports, but is not a substitute for, the all-\(n\) proof, spectral argument, or probability bound.

## Relationship to prior work

Huang, Sun, Xu and Zhao (2025), especially their Theorem 1, Proposition 4, and Appendix A, establish the underlying specialized-equilibrium/kernel correspondence and monotonicity under reciprocating existing edges. Their random-network existence proposition studies a dense independent-arc model, not a fixed cycle architecture with independent reciprocation of ring edges. The present result does **not** claim those structural principles as new: it supplies exact model-specific existence and multiplicity laws and the typical exponential-multiplicity transition at any fixed positive reciprocity.

Bisdorff and Marichal (2008) state the classical Perrin enumeration of maximal independent sets on undirected cycles. That covers the full-reciprocity endpoint \(r=1\), not the partial-reciprocity expectation, small-\(r\) crossover, kernel-free probability, or random-network high-probability lower bound. Any general weighted Perrin enumeration may imply the trace identity but does not by itself establish the high-probability doubling-gadget theorem. Priority over unindexed related random-kernel literature has not been independently certified.

## Limitations

The results concern **specialized**, not all Nash equilibria; simple cycles, not arbitrary networks; an independent three-state edge model with symmetric one-way orientation probabilities; and fixed positive \(r\) for the high-probability exponential lower bound. The \(r\sim 1/n\) result is for the expectation only, not a distributional limit. The coefficient in the typical bound is deliberately explicit rather than optimal. The standard all-bidirectional Perrin count and the kernel correspondence are previously known. No independent external validation has been performed.

## References

1. Jingmin Huang, Yang Sun, Fanqi Xu, Wei Zhao. *Public Goods Provision in Directed Networks: A Kernel Approach* (first posted December 29, 2025), arXiv:2512.23193. https://arxiv.org/abs/2512.23193
2. Raymond Bisdorff and Jean-Luc Marichal. *Counting Non-Isomorphic Maximal Independent Sets of the n-Cycle Graph*. Journal of Integer Sequences 11 (2008), Article 08.5.7. https://cs.uwaterloo.ca/journals/JIS/VOL11/Marichal/marichal.html
3. M. Richardson. *On weakly ordered systems*. Bulletin of the American Mathematical Society 52 (1946), 113–116. Classical existence theorem for kernels without odd directed cycles, recalled in Reference 1.
