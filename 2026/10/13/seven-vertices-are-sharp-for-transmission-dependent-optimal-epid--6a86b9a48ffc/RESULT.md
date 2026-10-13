# Seven vertices are sharp for transmission-dependent optimal epidemic sentinels on trees

## Finding

In a homogeneous susceptible--infectious--removed epidemic on an undirected contact tree with one uniformly chosen initial infection, the vertex most likely to register an outbreak can depend on the infection-to-recovery ratio. **Seven is the smallest possible number of vertices**, and precisely two of the eleven seven-vertex tree shapes permit a change in the set of optimal locations. One changes at the reciprocal golden ratio, the other at one half.

Write \(p=\beta/(\beta+\gamma)\) for the probability that a single infectious--susceptible edge transmits before the source recovers. The optimal-sentinel score at vertex \(v\) is
\[
P_v(p)=\frac1n\sum_{u\in V(T)}p^{d_T(u,v)}.
\]

**Broom.** Its vertices are \(H,A,B,C,D,L_1,L_2\) with edges \(HA,AB,BC,CD,HL_1,HL_2\). Define \(p_\mathrm{B}=(\sqrt5-1)/2\). Exactly \(H\) is optimal for \(0<p<p_\mathrm{B}\), exactly \(A\) for \(p_\mathrm{B}<p<1\), and the two vertices tie (and exclude all other vertices) at \(p=p_\mathrm{B}\). In terms of physical rates, the change occurs at \(\beta/\gamma=(1+\sqrt5)/2\).

**Two-claw tree.** Its vertices are \(U,M,V,L_1,L_2,R_1,R_2\), with edges \(UM,MV,UL_1,UL_2,VR_1,VR_2\). Exactly \(U,V\) tie for the optimum when \(0<p<1/2\); exactly \(U,M,V\) tie at \(p=1/2\); and \(M\) alone is optimal when \(1/2<p<1\). Thus two nonadjacent optimizers exist for sufficiently small positive transmissibility.

For each of the other nine isomorphism classes of seven-vertex trees, and for every tree with at most six vertices, the entire optimal set is fixed throughout \(0<p<1\).

## Assumptions and scope

All trees are finite, connected, simple, undirected, and unweighted. A single epidemic starts from one uniformly selected vertex; there are no initial recovered vertices. Each infectious vertex independently recovers at constant rate \(\gamma>0\); every edge to a susceptible neighbor transmits at constant rate \(\beta>0\) while its endpoint is infectious. A sentinel records whether its own vertex was ever infected, without affecting the epidemic. Ties are included in the set of optimal sentinels. Claims cover every real \(\beta,\gamma>0\) and every tree on at most seven vertices, with a sharp two-shape classification at exactly seven; the one-vertex case is immediate.

## Proof

**1. Exact score from the Markov epidemic.** Condition on the uniformly random seed \(u\). In a tree there is one simple path from \(u\) to the sentinel \(v\). Every path vertex, after first becoming infectious, must transmit to the next path vertex before recovery. Competing independent exponential clocks imply this one-step event has probability \(\beta/(\beta+\gamma)=p\). Recovery and transmission clocks associated with successive path vertices are independent, so the conditional infection probability of \(v\) equals \(p^{d_T(u,v)}\), including probability one if \(u=v\). Branches off the path cannot introduce alternate routes and do not affect the path-edge race. Averaging over seeds gives the displayed score, which is an exponential/decay-closeness polynomial up to the constant factor \(1/n\).

**2. Complete finite classification by exact polynomial dominance.** Fix \(n\in\{2,3,4,5,6,7\}\). The Prüfer bijection lists all labeled trees exactly once from all \(n^{n-2}\) words of length \(n-2\) over \(\{0,\dots,n-1\}\). For each such tree, compute the unique isomorphism-invariant AHU parenthesis encoding, retaining one representative per unlabelled class. The resulting numbers of classes are exactly \(1,1,2,3,6,11\). For every representative and vertex \(v\), compute the integer distance-shell counts \(a_{v,k}=|\{u:d_T(u,v)=k\}|\), \(0\le k<n\), and the score polynomial \(S_v(p)=\sum_{k=0}^{n-1}a_{v,k}p^k\).

For any two vertices \(v,w\), set \(m=n-1\), \(g_k=a_{v,k}-a_{w,k}\), and
\[
b_j(v,w)=\sum_{k=0}^{j}\frac{\binom{j}{k}}{\binom{m}{k}}g_k,\qquad0\le j\le m.
\]
The exact Bernstein identity
\[
S_v(p)-S_w(p)=\sum_{j=0}^{m}b_j(v,w)\binom mjp^j(1-p)^{m-j}
\]
shows that coefficientwise nonnegative \(b_j\) imply \(S_v(p)\ge S_w(p)\) over \([0,1]\); if the polynomial is nonzero, this inequality is strict for every \(0<p<1\), since all Bernstein basis factors are positive there. The accompanying standard-library checker computes all \(b_j\) as exact rational numbers and, in each of **22 of the 24** unlabelled classes up to order seven, finds a vertex with nonnegative Bernstein differences against every other vertex. Any other vertex tied with this witness in the interior must have exactly the same score polynomial. Consequently the *entire argmax set* is independent of \(p\) in each of those 22 classes. There are no omitted labeled or unlabelled trees: the word enumeration and the AHU encoding cover all trees and identify isomorphisms exactly.

The only two classes without the displayed uniform-maximizer certificate are isomorphic to the broom and two-claw trees explicitly defined above. The checker verifies their canonical encodings and separately supplies exact Bernstein dominance against all noncandidate vertices. It follows that only the candidate sets named below need comparison.

**3. Broom switch.** Distance shells yield
\[
S_H(p)=1+3p+p^2+p^3+p^4,\qquad S_A(p)=1+2p+3p^2+p^3.
\]
Hence
\[
S_H(p)-S_A(p)=p-2p^2+p^4=p(1-p)(1-p-p^2).
\]
For \(p\in(0,1)\), the first two factors are positive and the strictly decreasing final factor vanishes exactly at \((\sqrt5-1)/2\). The other five vertices are strictly below the better candidate for all \(p\in(0,1)\) by the nonnegative rational Bernstein certificates in the checker. This proves the full three-phase optimum including the tie.

**4. Two-claw switch.** Symmetry yields
\[
S_U(p)=S_V(p)=1+3p+p^2+2p^3,\qquad S_M(p)=1+2p+4p^2.
\]
The gap is
\[
S_U(p)-S_M(p)=p-3p^2+2p^3=p(1-p)(1-2p).
\]
Its sign changes once at \(p=1/2\). Every leaf is strictly dominated by a candidate over \((0,1)\) as certified by exact Bernstein coefficients, giving exactly the optimizer sets stated above. This completes the finite classification. \(\square\)

## Verification

Run `python3 check.py` in the directory containing this file and `check.py`. The checker needs Python's standard library only and has no network or third-party package dependency. It exhaustively visits **18,248 Prüfer words**, groups them into classes of sizes \(1,1,2,3,6,11\), computes all distance-shell score polynomials, and uses exact `fractions.Fraction` Bernstein coefficients to certify 22 parameter-independent classes and the two exceptional classes. It asserts their exact candidate score coefficients, difference polynomials, canonical isomorphism classes, and strict noncandidate exclusions. The expected final console line starts `VERIFY_OK`. This is a finite exhaustive proof within the stated order bound, not a numerical grid search over \(p\); the analytical factorizations above cover all real \(p\in(0,1)\).

## Relationship to prior work

The decay-distance centrality itself is not new: Wang and Tang (2014) develop its computation on trees; Tsakas (2016) analyzes parameter-dependent decay rankings; and Riveros, Salas and Skibski (2021/2022) investigate which centralities choose roots of trees and already show that decay centrality need not have the tree-rooting property. Neither the existence of parameter-dependent rankings nor the possibility of separated best vertices is claimed as original. Holme (2018) studies frequency of epidemic sentinel detection, while Holme (2017) examines exact small-network SIR rankings under a *different*, time-to-detection objective. The present finite claim joins the tree-specific epidemic detection probability to the decay score and supplies the exact **smallest order**, **two and only two exceptional tree shapes**, and **both phase diagrams**. These specific conclusions are not stated or implied by the inspected theorems and figures of the closest papers.

A separate analysis of intervention optimization on small contact trees may feature the same algebraic constants because related distance polynomials arise. Optimal deletion of vertices or edges to reduce outbreak size, however, is a different objective from placing a nonintervening sentinel to maximize detection probability. No equivalence reducing the entire present classification to those intervention statements is assumed.

## Limitations

This classification covers single uniformly seeded outbreaks on undirected trees with homogeneous, memoryless infection and recovery rates, and a single perfectly sensitive permanent sentinel. It does not assert that transmission events on **different edges** are independent in the full continuous-time SIR process; only the path-event product is used. It does not address cyclic networks, nonuniform seeding, false-negative or periodic testing, multiple sentinels, weighted or directed edges, or trees larger than seven vertices. Originality remains subject to the possibility that an independent full small-tree decay-centrality census exists outside the inspected literature; the cited authors previously identified the general centrality and its qualitative parameter effects.

## References

1. W. Wang and C. Y. Tang, *Distributed computation of classic and exponential closeness on tree graphs*, American Control Conference (June 4–6, 2014), DOI `10.1109/ACC.2014.6858727`.
2. N. Tsakas, *On Decay Centrality*, arXiv:1604.05582 (first posted April 19, 2016), https://arxiv.org/abs/1604.05582.
3. P. Holme, *Three faces of node importance in network epidemiology: Exact results for small graphs*, arXiv:1708.06456 (2017), https://arxiv.org/abs/1708.06456.
4. P. Holme, *Objective measures for sentinel surveillance in network epidemiology*, arXiv:1803.10637 (2018), https://arxiv.org/abs/1803.10637.
5. C. Riveros, J. Salas and O. Skibski, *How do centrality measures choose the root of trees?*, arXiv:2112.13736 (first posted December 27, 2021), https://arxiv.org/abs/2112.13736.
