# A density-dependent rigidity theorem for exact exclusion conditioning on finite graphs

## Finding

Let \(G\) be a connected finite undirected support graph on \(n\ge3\) vertices. A continuous-time walker may jump along each oriented edge \(u\to v\) at rate \(q_{uv}>0\), with both orientations present; other off-diagonal rates vanish. Put \(w_{uv}=q_{uv}+q_{vu}\) for each unordered pair, including zero for nonedges. Let \(2\le k\le n-1\), and start \(k\) independent identical walkers from distinct vertices. Denote their first collision time by \(\tau\), and their unordered occupied-vertex process by \(S_t\). Compare the full occupation-set path distribution on \([0,T]\) conditional on \(\tau>T\) with the \(k\)-particle exclusion law that simply rejects jumps to occupied vertices.

**Rigidity at a single horizon.** For even one initial \(k\)-subset \(S\) and one \(T>0\), the two full path distributions are equal if and only if
\[
 c_k(A):=\sum_{\{u,v\}\subseteq A}w_{uv}
 \]
is independent of the \(k\)-subset \(A\subseteq V\). In that event equality holds for every initial \(k\)-subset and every positive horizon, and
\[
 \Pr_S(\tau>T)=\exp(-c_k T).
\]

**Complete rate classification.** If \(2\le k\le n-2\), the above equality holds precisely when \(G\) is complete and there exists \(a>0\) with \(q_{uv}+q_{vu}=a\) for every distinct vertex pair; then \(c_k=a\binom{k}{2}\). For \(k=n-1\), equality holds precisely when the symmetrized weighted degree \(d_w(v)=\sum_{u\ne v}w_{uv}\) is the same for all vertices. This latter case allows sparse regular supports and nonuniform edge weights. The orientations may be asymmetric in either regime.

Thus a single intermediate density forces exact agreement at every density, whereas agreement with one vacant vertex need not imply agreement with two or more vacancies.

## Assumptions and scope

The vertex set is finite; the off-diagonal jump rates are finite and strictly positive in both directions on every support edge; the support graph is connected; walkers have independent exponential-clock jumps with the same single-walker generator; \(2\le k\le n-1\); and the time horizon satisfies \(T>0\). Equality means equality of probability measures on the full right-continuous path space of *unlabeled occupancy sets* over \([0,T]\), not merely agreement of a one-time marginal. Conditional survival is well defined because a positive no-jump probability always exists. No reversibility or equality of outgoing holding rates is assumed.

## Proof

**1. The killed and exclusion generators.** For any occupied \(k\)-set \(A\), a jump from an occupied vertex \(u\in A\) into another occupied vertex \(v\in A\) kills the independent-walker system. Its total killing rate is
\[
 \kappa(A)=\sum_{u\in A}\sum_{v\in A\setminus\{u\}}q_{uv}
 =\sum_{\{u,v\}\subseteq A}(q_{uv}+q_{vu})=c_k(A).
\]
The surviving off-diagonal transitions have exactly the rates of exclusion. Consequently the killed generator is \(K=Q^{\mathrm{ex}}-\operatorname{diag}(c_k)\). Comparing positive continuous-time path densities between consecutive jump times (or applying finite-state Feynman--Kac) gives, for each initial \(S\),
\[
 \frac{d\mathbb P^{\mathrm{ind}}_S(\,\cdot\mid\tau>T)}
 {d\mathbb P^{\mathrm{ex}}_S}(\omega)
 =\frac{\exp\!\left(-\int_0^T c_k(\omega_t)\,dt\right)}
 {\mathbb E^{\mathrm{ex}}_S\!\left[\exp\!\left(-\int_0^T c_k(S_t)\,dt\right)\right]}.
\]
This change-of-measure identity itself is established for a broader setting in the motivating literature and is *not* claimed as a new result.

**2. A single starting set and finite horizon force constant killing.** If \(c_k\) is constant, the displayed Radon--Nikodym derivative is identically one, for all initial states and horizons; the survival probability is the indicated exponential. Conversely suppose the path laws are equal for a single starting set \(S\) and a single \(T>0\). Then \(\int_0^T c_k(S_t)\,dt\) is almost surely constant under exclusion.

The exclusion state graph, whose vertices are the \(k\)-subsets and whose transitions swap an occupied and a vacant endpoint of a support edge, is connected: edge transpositions of a connected underlying graph generate all vertex permutations, hence act transitively on sets of fixed size. Fix any permitted transition \(A\to B\), and select a finite permitted transition path from \(S\) through \(A\) and finally to \(B\). The event that these are exactly the transitions on \([0,T]\) has positive probability. Conditional on that event the ordered jump times have a strictly positive density on the corresponding open time simplex. The path integral is an affine function of these jump times. Its partial derivative with respect to the final jump time is \(c_k(A)-c_k(B)\). Since it is almost surely constant under a strictly positive density, this derivative must vanish. Every exclusion transition therefore joins equal \(c_k\) values, and connectedness forces \(c_k\) constant across all \(k\)-subsets.

**3. The intermediate occupancy layers.** Assume \(2\le k\le n-2\). Fix distinct \(u,v\) and any \((k-1)\)-subset \(L\subset V\setminus\{u,v\}\). Constancy of \(c_k\) on the two sets \(L\cup\{u\}\) and \(L\cup\{v\}\) yields
\[
 \sum_{x\in L}(w_{ux}-w_{vx})=0.
\]
Here \(1\le k-1\le(n-2)-1\). For a vector of length \(n-2\), if *every* \((k-1)\)-subset sum vanishes in this proper, nonempty cardinality range, replacing one selected index by one omitted index shows all coordinates equal; their common value is zero because their nonempty subset sum is zero. Thus \(w_{ux}=w_{vx}\) for every third vertex \(x\). Symmetry of \(w\) implies all pair weights share one common value \(a\). Connectivity and positivity on support edges imply \(a>0\); all pairs must therefore be edges. Conversely complete uniform symmetrized weights give \(c_k(A)=a\binom{k}{2}\) at every occupancy layer. Notice that individual oriented rates \(q_{uv}\) may differ from \(q_{vu}\).

**4. Exactly one hole.** For \(k=n-1\), let \(W=\sum_{\{u,v\}\subseteq V}w_{uv}\). Each \(k\)-subset is \(V\setminus\{v\}\) for a unique vertex, and
\[
 c_{n-1}(V\setminus\{v\})=W-d_w(v).
\]
This is constant precisely when \(d_w(v)\) is vertex independent. The condition is independent of the orientation of each edge, and admits many noncomplete supports.

**5. Sharp distinction.** On the four-cycle, set \(q_{uv}=q_{vu}=1/2\) for each adjacent pair. Every symmetrized degree is two, and \(c_3(A)=2\) for every three-vertex set. But \(c_2(A)=1\) when the two vertices are neighbors and \(c_2(A)=0\) when they are opposite, so two-particle path equality fails. This proves that one-hole equality need not propagate to any intermediate layer.

## Verification

The standalone `verify.py` enumerates all connected support graphs with integer symmetrized weights \(0,1,2\) on three or four vertices; a deterministic selection of sparse, complete and nonuniform connected graphs on five through seven vertices; the intermediate-layer and one-hole subset sums; and an asymmetric oriented-rate split of every complete uniform pair weight. It independently compares constant-subset-sum conditions against the asserted rate classifications and verifies the four-cycle separation example. The script passed 22,872 finite classification assertions. These checks are consistency tests, not a proof for unbounded graph size or real-valued rates; those are handled by the five analytical steps above. Execute with `python3 verify.py`.

## Relationship to prior work

Shiatis's 2026 paper proves a change-of-measure relation between noncolliding and exclusion dynamics for general continuous-time Markov systems and explicitly derives the finite-horizon Feynman--Kac identity (equation (2.4)). The present statement uses that known principle, but gives the graph-theoretic *if-and-only-if* classification of when this change of measure becomes exactly trivial, with only one observed starting set and horizon; it identifies a change of class precisely at the one-hole layer. The original paper's examples concern (a)symmetric exclusion on rings and lattices, rather than this finite connected graph classification. Johnston and Shiatis (2025) concern integrable ring dynamics, a distinct model family; the full text was not used to assert an absence of equivalent older results.

## Limitations

The result concerns finite connected bidirectional support, indistinguishable occupancy paths and conditioning on survival for a finite positive horizon. It does not classify graphs with genuinely one-way directed support, disconnected support, or partial observation of one-time marginals. It does not assert the same classification for arbitrary multi-species walkers. The general killed/exclusion Feynman--Kac relation and the elementary fixed-size subset-sum fact predate this finding; the claimed additional contribution is their exact graph-rate classification and the sharp occupancy-layer distinction. Historical equivalent formulations under other terminology have not been categorically ruled out, and no independent audit has been carried out.

## References

1. Rohan Shiatis, *Exclusion vs Noncolliding Dynamics in Markov Processes*, arXiv:2610.00741v1 (first publicly posted 2026-09-30), especially Theorem 1.4 and Section 2, equation (2.4). https://arxiv.org/html/2610.00741v1
2. S. G. G. Johnston and R. Shiatis, *The Integrable Snake Model*, arXiv:2501.15483 (2025); used only as contextual prior work identified in the bibliography of reference 1. https://arxiv.org/abs/2501.15483
