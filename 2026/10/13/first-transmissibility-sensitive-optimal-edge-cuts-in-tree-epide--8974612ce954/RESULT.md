# First transmissibility-sensitive optimal edge cuts in tree epidemics

## Finding

Let \(T\) be a finite simple undirected tree with \(n\ge 2\) vertices. Independently retain each contact edge with probability \(p\in(0,1)\). Choose one outbreak seed uniformly from all \(n\) vertices, and define the final outbreak to be its retained-edge connected component. Before sampling the seed or the retained edges, permanently remove one edge \(e\) to minimize expected final outbreak size. Call an edge *uniformly optimal* if it attains this minimum simultaneously for every \(p\in(0,1)\).

**Classification theorem.** Every tree on at most seven vertices has a uniformly optimal edge. Among the \(23\) unlabeled eight-vertex trees, exactly \(21\) have a uniformly optimal edge. The remaining two trees, and only those two, have no uniformly optimal edge. They can be represented on vertices \(0,1,\ldots,7\) by the following edge sets, where \(ab\) denotes the edge joining vertices \(a\) and \(b\):

- Type I: `01,12,23,24,05,56,67`.
- Type II: `01,12,23,24,05,56,57`.

For Type I the uniquely optimal edge is `12` when \(0<p< (\sqrt5-1)/2\), is `01` when \((\sqrt5-1)/2<p<1\), and both tie exactly at \(p=(\sqrt5-1)/2\). For Type II the two edges `12` and `05` are exactly the optimal edges when \(0<p<1/2\), the uniquely optimal edge is `01` when \(1/2<p<1\), and all three tie exactly at \(p=1/2\). Thus eight vertices is the sharp first size at which the best single contact-edge intervention genuinely depends on transmissibility, with the complete first-size exception list and both exact transition values.

## Assumptions and scope

Edges are independent identically distributed Bernoulli transmissions with common probability \(p\). A single seed is drawn uniformly among *all* original vertices; removing an edge does not remove its endpoints. There are no subsequent external infections, reinfections, dynamic edges, or correlations among transmissions. Because a tree has unique paths, outbreak reachability is equivalent to independent bond percolation. All assertions concern the reduction of the **mean** number infected, not the variance, largest connected component, or epidemic threshold on an infinite graph. A uniformly optimal edge means an edge that remains an optimizer for every open-interval value of \(p\), not necessarily the only optimizer at every value.

## Proof

**1. Exact edge-benefit polynomial.** Denote the final component size of a uniformly chosen seed in the retained-edge graph by \(X_T(p)\). For different vertices \(u,v\), connectivity occurs precisely when every edge on the unique connecting path is retained; this has probability \(p^{d_T(u,v)}\). Therefore

\[
\mathbb E X_T(p)=1+\frac2n\sum_{\{u,v\}\subset V(T)}p^{d_T(u,v)}.
\]

Removing edge \(e=ab\) separates \(T\) into sides \(A_e\ni a\) and \(B_e\ni b\). Exactly the pairs with one vertex on each side lose all paths, so the reduction in mean outbreak size is

\[
G_e(p)=\frac2n\sum_{u\in A_e,v\in B_e}p^{d_T(u,v)}
       =\frac{2p}{n}F_e(p),
\qquad
F_e(p)=\left(\sum_{u\in A_e}p^{d_T(u,a)}\right)
\left(\sum_{v\in B_e}p^{d_T(v,b)}\right).
\]

The positive factor \(2p/n\) is common to all candidate edges, so an optimal removed edge maximizes \(F_e(p)\). Write \(F_e(p)=\sum_{k=0}^{n-2}c_{e,k}p^k\). Its coefficient \(c_{e,k}\) counts cross-cut unordered pairs of distance \(k+1\). In particular \(c_{e,0}=1\), \(c_{e,1}=\deg_T(a)+\deg_T(b)-2\), and \(F_e(1)=|A_e||B_e|\). These two endpoint statistics explain the possible tension between local contact degree and global cut balance.

**2. Exact polynomial dominance certificate.** Put \(d=n-2\). For two edges \(e,f\), the polynomial difference can be rewritten identically as

\[
F_e(p)-F_f(p)=\sum_{j=0}^{d}b_j(e,f)p^j(1-p)^{d-j},
\qquad
b_j(e,f)=\sum_{k=0}^{j}\binom{d-k}{j-k}(c_{e,k}-c_{f,k}).
\]

Indeed, substitute \(1=p+(1-p)\) into \(p^k\) to obtain this basis transformation. The coefficients \(b_j(e,f)\) are integers. If every one is nonnegative for every competitor \(f\), then \(F_e(p)\ge F_f(p)\) simultaneously for all \(p\in[0,1]\). This is a sufficient, entirely exact certificate of uniform optimality.

**3. Finite classification with an exhaustive certificate.** Every labeled tree on \(n\ge2\) vertices is represented by exactly one Prüfer word of length \(n-2\) over \(\{0,\ldots,n-1\}\). The accompanying checker visits all \(n^{n-2}\) words for each \(2\le n\le8\). It converts each word to a tree and collapses isomorphic trees using its recursively sorted center-rooted parenthesis code. The code is a complete invariant for unlabeled trees: rooted codes classify rooted trees by induction on height, and an unrooted tree has one center or two adjacent centers uniquely determined by recursive leaf deletion. Two trees have the same complete code exactly when they are isomorphic.

For every isomorphism-class representative, the checker computes each \(c_{e,k}\) twice (by enumerating cross-cut pairs and by multiplying the two endpoint-distance histograms), and searches for an edge \(e\) whose integer \(b_j(e,f)\) are all nonnegative for all edges \(f\). These are exhaustive finite inequalities, not tests at a numerical grid of parameter values. The exact numbers of classes examined at orders \(2,3,4,5,6,7,8\) are respectively \(1,1,2,3,6,11,23\). There are respectively \(0,0,0,0,0,0,2\) classes lacking such a certificate. The two noncertified classes have distinct complete center-rooted codes `U(((()()))((())))` and `V((()()))((()()))`; direct construction below identifies them as Type I and Type II. Consequently every other class has a concrete uniformly optimal edge, and there can be no smaller exceptional tree. The complete checker is `check_edge_switch.py`; it has no third-party dependencies and finishes by printing `VERIFY_OK` after all assertions.

**4. The two exceptions actually switch.** For Type I, the polynomials of the balanced cut `01` and branch cut `12` are

\[
F_{01}(p)=1+2p+4p^2+4p^3+3p^4+2p^5,\qquad
F_{12}(p)=1+3p+3p^2+3p^3+3p^4+2p^5.
\]

Every other edge has coefficients componentwise at most those of \(F_{01}\), with at least one strictly smaller coefficient of positive degree. Thus no other edge can maximize for \(p\in(0,1)\). The exact comparison is

\[
F_{12}(p)-F_{01}(p)=p(1-p-p^2),
\]

which changes sign once on the interval, at \(p=(\sqrt5-1)/2\), proving the Type I optimizer statement.

For Type II, again let `01` be the balanced cut. Its polynomial and those of the two symmetry-related branch cuts `12` and `05` are

\[
F_{01}(p)=1+2p+5p^2+4p^3+4p^4,\quad
F_{12}(p)=F_{05}(p)=1+3p+3p^2+4p^3+4p^4.
\]

Every other edge is componentwise dominated by \(F_{01}\), strictly for positive \(p\). Here

\[
F_{12}(p)-F_{01}(p)=p(1-2p),
\]

which changes sign at exactly \(p=1/2\). Both types thus fail to possess an edge optimal for all \(p\), proving that the two and only two eight-vertex exceptions detected in step 3 are genuine. This completes the classification.

## Verification

Run `python3 check_edge_switch.py` with Python 3. The checker exhausts \(1+3+16+125+1296+16807+262144=280392\) Prüfer words across orders \(2\) through \(8\) and reports the seven unlabelled-tree counts and the two exceptional canonical codes before `VERIFY_OK`. Its two independent constructions of each edge polynomial agree, and it checks the listed Type I and Type II coefficients, competitor domination and exact differences. The exhaustive enumeration is valid because of the Prüfer bijection, the complete center-rooted isomorphism code, and integer polynomial certificates; floating-point evaluation at finitely many probabilities is not used in the proof. The theorem does not claim a classification of trees with nine or more vertices.

## Relationship to prior work

Moore and Newman relate SIR-type transmission models to bond percolation (arXiv:cond-mat/9911492). Enns, Mounzer and Brandeau study link quarantine with known infection states using constrained partitioning (DOI:10.1016/j.mbs.2011.11.006), and Enns and Brandeau compare preventive and reactive link-removal algorithms on larger networks (DOI:10.1016/j.jtbi.2015.02.005). These works motivate selecting an edge intervention, but their objectives and results do not specify the uniform-seed finite-tree sharp threshold established here.

Khorramzadeh and collaborators (arXiv:1403.7074; DOI:10.1103/PhysRevE.91.042814) already explicitly demonstrated *parameter-dependent rankings of edge importance* in a cyclic network under a two-terminal reliability objective, including a switch near \(0.618\). Consequently neither the general phenomenon of edge-ranking switches nor the occurrence of a golden-ratio numerical threshold is asserted to be new. The separate contribution here is the complete smallest-order classification under a uniform-seed **expected outbreak size** objective on **trees**. A general reliability-polynomial framework is not itself a published classification of this finite-tree extremal optimization problem.

## Limitations

The sharpness conclusion is restricted to finite simple undirected trees with uniform seeds, one preemptively deleted edge, homogeneous independent bond transmissions, and mean final outbreak size. It does not extend without proof to arbitrary graphs, unequal edge probabilities, nonuniform starting distributions, time-dependent SIR infectious periods, or simultaneous deletion of multiple edges. The computational classification is exhaustive only through eight vertices; it makes no inference about all larger trees. The prior-art comparison does not establish that no unpublished or differently indexed equivalent result exists. Independent validation has not been performed.

## References

1. C. Moore and M. E. J. Newman, "Epidemics and percolation in small-world networks," arXiv:cond-mat/9911492, first public version 1999-11-30; *Physical Review E* **61**, 5678 (2000), DOI:10.1103/PhysRevE.61.5678.
2. E. A. Enns, J. J. Mounzer, M. L. Brandeau, "Optimal link removal for epidemic mitigation: a two-way partitioning approach," *Mathematical Biosciences* **235**, 138-147 (2012), DOI:10.1016/j.mbs.2011.11.006.
3. Y. Khorramzadeh, M. Youssef, S. Eubank, S. Mowlaei, "Analyzing network reliability using structural motifs," arXiv:1403.7074; *Physical Review E* **91**, 042814 (2015), DOI:10.1103/PhysRevE.91.042814.
4. E. A. Enns and M. L. Brandeau, "Link removal for the control of stochastically evolving epidemics over networks: a comparison of approaches," *Journal of Theoretical Biology* **371**, 154-165 (2015), DOI:10.1016/j.jtbi.2015.02.005.
