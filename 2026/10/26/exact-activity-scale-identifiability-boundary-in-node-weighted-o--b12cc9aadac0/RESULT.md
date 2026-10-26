# Exact activity-scale identifiability boundary in node-weighted opinion dynamics

## Finding

**Theorem (unoriented interaction-law identifiability).** Let \(G=(A\sqcup B,E)\) be a finite, connected, simple bipartite graph with two nonempty vertex classes, and assign every vertex a strictly positive activity weight \(w_v\). At each integer time, first choose vertex \(i\) with probability proportional to \(w_i\), then choose a neighbor \(j\) with probability proportional to \(w_j\), and retain only the *unordered* interacting pair. Set \(W_A=\sum_{i\in A}w_i\), \(W_B=\sum_{j\in B}w_j\), and \(S_v=\sum_{u\sim v}w_u\). For \(t>0\), multiply every weight in \(A\) by \(t\), leaving all weights in \(B\) unchanged, and let \(P_t\) be the law of the next unordered edge.

Define two probability laws on the edges (with \(i\in A\), \(j\in B\)) by
\[
Q_A(ij)=\frac{w_iw_j}{W_A S_i},\qquad Q_B(ij)=\frac{w_iw_j}{W_B S_j}.
\]
For every \(t>0\), exactly
\[
P_t=\theta_tQ_A+(1-\theta_t)Q_B,\qquad
\theta_t=\frac{tW_A}{tW_A+W_B},
\]
and for any two scales \(s,t>0\),
\[
\operatorname{TV}(P_t,P_s)=|\theta_t-\theta_s|\operatorname{TV}(Q_A,Q_B).
\]
Thus \(P_t=P_s\) for distinct scales if and only if there exists a common number \(\eta\in(0,1]\) such that
\[
\frac{S_i}{W_B}=\eta\quad(i\in A),\qquad
\frac{S_j}{W_A}=\eta\quad(j\in B).
\]
In particular, **all** strictly positive weight profiles have scale-invariant edge laws if and only if \(G\) is complete bipartite. On \(K_{a,b}\), for every weight profile and every scale,
\[
P_t(ij)=\frac{w_i}{W_A}\frac{w_j}{W_B}.
\]
On each noncomplete connected bipartite graph, scale-invariant weight profiles form a proper algebraic subset of Lebesgue measure zero. Outside that exceptional set, if within-class normalized activity weights are known, the relative total activity of the two classes is uniquely recoverable from the exact unordered-edge law. For complete bipartite graphs it is never recoverable from those observations.

For symmetric, edge-only Deffuant--Weisbuch updates, the entire law of opinion trajectories (at every finite horizon, for any fixed initial opinion profile, confidence bound and compromise parameter) is correspondingly invariant under classwise activity rescaling in a complete bipartite graph. The same remains true when the classwise scale is changed adaptively in response to the past, as long as relative weights within each class remain fixed.

## Assumptions and scope

* The graph is connected, bipartite, finite, undirected, simple, with no isolated vertices, and \(w_v>0\) for all vertices.
* The first vertex is drawn with probability \(w_i/\sum_v w_v\), and the second from its neighborhood with probability \(w_j/S_i\). Each time step uses an independently sampled pair conditional on the current (possibly adaptively rescaled) weights.
* Only unordered pairs are observed. Observing *which vertex was chosen first* distinguishes the classwise scale, even on complete bipartite graphs. Unconditional global rescaling of all weights is always irrelevant.
* The identifiability statement assumes that the relative weights *within* each bipartition class are known. No identifiability of all individual unknown weights is asserted.
* For the opinion-dynamics corollary, both interacting vertices update symmetrically, using solely the unordered edge and their current opinions. The theorem is about equality of trajectory distributions, not about guaranteed consensus or a particular convergence time.

## Proof

**1. Edge law.** For any undirected edge \(ij\), summing its two possible orientations gives
\[
P_w(ij)=\frac{w_iw_j}{W_A+W_B}\left(\frac1{S_i}+\frac1{S_j}\right).
\]
For the directed sampling conditioned on the first vertex belonging to \(A\), the edge law is \(Q_A\); similarly it is \(Q_B\) when the first vertex belongs to \(B\). Both sum to one because their inner neighbor-selection probabilities do. Under classwise scaling, the within-class probabilities and the conditional neighbor choices are unchanged; only the probability \(\theta_t\) that the first vertex belongs to \(A\) changes. This proves the mixture identity. The signed measure \(P_t-P_s=(\theta_t-\theta_s)(Q_A-Q_B)\) gives the exact total-variation identity.

**2. Exact equality condition.** Since \(\theta_t\) is strictly increasing, two different scales yield the same edge law if and only if \(Q_A=Q_B\). Positivity of the weights makes the equality on edge \(ij\) equivalent to \(W_A S_i=W_B S_j\), or \(S_i/W_B=S_j/W_A\). Connectivity propagates this equality along all edges, forcing one common \(\eta\) on both vertex classes. Conversely those equalities imply \(Q_A=Q_B\). Every ratio belongs to \((0,1]\).

**3. Universal graph characterization.** For a complete bipartite graph, every \(i\in A\) has \(S_i=W_B\) and every \(j\in B\) has \(S_j=W_A\). Hence \(Q_A=Q_B\) and both equal the stated product law. Conversely, suppose that a connected graph is not complete bipartite. Pick a nonedge \(ib\) with \(i\in A,b\in B\), and pick any neighbor \(j\in B\) of \(i\). For the edge \(ij\), scale-invariance requires \(W_A S_i=W_B S_j\). Fix all weights except \(w_b\). Because \(b\not\sim i\), the left side is unchanged when \(w_b\) varies, while the right side increases strictly because \(S_j>0\). Therefore this identity cannot hold for every positive weight profile. This proves the if-and-only-if classification.

**4. Generic identifiability.** With the nonedge \(ib\) above, \(F(w)=W_B S_j-W_A S_i\) is a nonzero polynomial: its coefficient of \(w_b\), with all other weights fixed, is \(S_j>0\). Every exceptional weight profile satisfies \(F(w)=0\). Its zero set has Lebesgue measure zero and no nonempty open subset of the positive orthant. On any other profile \(Q_A\ne Q_B\), so at least one edge \(e\) has \(Q_A(e)\ne Q_B(e)\). From its observed probability \(P_t(e)\),
\[
\theta_t=\frac{P_t(e)-Q_B(e)}{Q_A(e)-Q_B(e)},\qquad
\frac{tW_A}{W_B}=\frac{\theta_t}{1-\theta_t}.
\]
These expressions recover the relative class total mass when the within-class proportions, which determine \(Q_A,Q_B\), are known. Complete bipartite graphs have \(Q_A=Q_B\) identically, so the relative mass cancels for all profiles.

**5. Dynamics.** With the same initial opinions and the same sequence of unordered sampled edges, symmetric Deffuant--Weisbuch trajectories agree step by step. On complete bipartite graphs, the conditional edge law is the unchanged product law even if the interclass scale is chosen based on prior observations. Induction on discrete time, or coupling through one common edge sequence, proves the finite-dimensional and whole-path distribution statements.

## Verification

A standalone standard-library checker (`verify.py`) evaluates the original two-orientation edge law independently of the conditional-mixture expression using exact rational arithmetic. It exhaustively checks connected labeled bipartite graphs with total order at most six and canonical ordered bipartitions (up to relabeling), the universal complete-bipartite identity, and a pair of explicit rational profiles revealing noninvariance for each noncomplete case. It also verifies the following boundary examples:

* On the four-vertex path \(0-1-2-3\), put \(A=\{0,2\}\), \(B=\{1,3\}\), initially all weights one. In edge order \((01,12,23)\), \(P_1=(3/8,1/4,3/8)\). Tripling the \(A\)-weights gives \(P_3=(7/16,1/4,5/16)\), hence \(\operatorname{TV}(P_1,P_3)=1/16\).
* On the six-cycle with equal within-class weights, \(Q_A=Q_B\) is uniform on the six edges, although the graph is not complete bipartite. This is an exceptional nongeneric weight profile, not a counterexample to the universal classification.
* On \(K_{3,4}\), arbitrary within-class weights \((2,3,5)\) and \((7,11,13,17)\) give the same product edge law after multiplying the first class's weights by seven.

Running `python verify.py` returned `CERTIFICATE_OK: 465 exact graph/edge checks across connected bipartite graphs up to six vertices plus examples`. The infinite-family, generic-measure, and path-law statements are proved algebraically above; they do not follow from the finite tests.

## Relationship to prior work

Li and Porter (arXiv:2206.09490, original public version 2022-06-19; published in 2023) introduce the weighted-first-node/weighted-neighbor interaction protocol and investigate the effects of heterogeneous activity weights computationally. Their equation (2) is precisely the starting sampling rule here. Their paper does not state a complete-bipartite class-rescaling invariance theorem, the total-variation identity, a universal graph characterization, or the exceptional-set identifiability dichotomy. Those are derived here for their particular protocol.

Alizadeh and Cioffi-Revilla (2015) compare different asynchronous activation schemes with a separate two-opinion updating model; they do not derive an edge-probability inverse problem for this weighted-neighbor rule. Sîrbu and coauthors (2019) alter partner selection using current opinion similarity in a mean-field bounded-confidence model, not time-independent relative node activities. The shared concepts of asynchronous opinion updates and nonuniform interactions do not supply the conditional-mixture characterization proved here. General conditional-probability and algebraic-zero-set facts are classical mathematical ingredients and are not claimed as original.

## Limitations

The invariance applies to *unordered* edge observations and symmetric edge-only updates; first-selection labels, event rates in physical time, or asymmetrically directed updates can reveal the changed class activity. The generic identifiability conclusion presumes within-class normalized weights known, not recovered from the same data. The graph characterization is bipartite and connected; no classification is claimed for nonbipartite graphs. The results are exact structural statements about the specified interaction protocol and do not validate it as an empirical social model or imply universal consensus behavior.

## References

1. G. J. Li and M. A. Porter, “A Bounded-Confidence Model of Opinion Dynamics with Heterogeneous Node-Activity Levels,” arXiv:2206.09490, original submission June 19, 2022; *Physical Review Research* **5**, 023179 (2023). https://arxiv.org/html/2206.09490v2 ; https://doi.org/10.1103/PhysRevResearch.5.023179 .
2. M. Alizadeh and C. Cioffi-Revilla, “Activation Regimes in Opinion Dynamics: Comparing Asynchronous Updating Schemes,” *Journal of Artificial Societies and Social Simulation* **18**(3), 8 (2015). https://www.jasss.org/18/3/8.html .
3. A. Sîrbu, D. Pedreschi, F. Giannotti, and J. Kertész, “Algorithmic Bias Amplifies Opinion Fragmentation and Polarization: A Bounded Confidence Model,” *PLOS ONE* **14**, e0213246 (2019). https://doi.org/10.1371/journal.pone.0213246 .
