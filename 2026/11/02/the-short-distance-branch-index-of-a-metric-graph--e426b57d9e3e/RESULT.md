# The short-distance branch index of a metric graph

## Finding

Let \(G\) be a finite connected simple metric graph, with \(m\ge1\) positively long edges and total arclength \(L\). Let \(X,Y\) be independent points uniformly distributed by normalized arclength on \(G\), let \(d\) be the intrinsic shortest-path metric, and write \(F(r)=\mathbb P(d(X,Y)\le r)\). With \(\ell_{\min}\) the shortest edge length, **for every** \(0\le r<\ell_{\min}/3\) the distribution is exactly

\[
 F(r)=\frac{2r}{L}+\frac{r^2}{L^2}B(G),\qquad
 B(G)=\sum_{v\in V(G)}\binom{\deg(v)}2-|E(G)|
     =\frac12\sum_{v\in V(G)}\deg(v)(\deg(v)-2).
\]

Consequently both \(L\) and the integer, subdivision-invariant **branch index** \(B(G)\) are intrinsic statistics of the *unlabeled* two-point distance law:

\[
 L=\frac{2}{F'(0+)},\qquad
 B(G)=\frac{2F''(0+)}{(F'(0+))^2}.
\]

Writing \(g=|E(G)|-|V(G)|+1\) for the first Betti number, the index also satisfies
\[
 B(G)=2g-2+\frac12\sum_{v\in V(G)}(\deg(v)-2)^2.
\]

In particular, if \(G\) is a tree, then
\[
 B(G)=-1+\sum_{v:\,\deg(v)\ge3}\binom{\deg(v)-1}{2}.
\]
Thus a tree with vertex degrees at most three has exactly \(B(G)+1\) trivalent branching vertices, determined by the two-point distance distribution alone, without knowing any edge lengths or incidences. Among trees with \(m\) edges,
\[
 -1\le B(G)\le \binom m2-m,
\]
with the lower equality exactly for paths and, for \(m\ge3\), the upper equality exactly for stars. Both are sharp.

## Assumptions and scope

A finite connected **simple** combinatorial graph \(G=(V,E)\) is equipped with a strictly positive length \(\ell_e\) for every edge; each edge is realized as a closed interval and vertices are identified according to incidence. Length measure charges no vertices. The shortest-path metric is the length metric on this one-dimensional complex. Uniform sampling is arclength measure divided by \(L=\sum_e\ell_e\). The sampling points are independent and no edge labels are observed. All asserted derivatives are right derivatives of this population distribution. All results permit arbitrary positive and unequal edge lengths, and permit degree-two subdivision vertices. The range \(0\le r<\ell_{\min}/3\) is a conservative, explicit universal interval, not claimed to be maximal.

## Proof

**1. Exhaustive short-path classification.** Write \(\ell_{\min}=\min_e\ell_e\). Fix \(0<r<\ell_{\min}/3\). If two sampled points lie in nonincident distinct edges, any connecting path must contain at least one complete graph edge between endpoints and hence has length at least \(\ell_{\min}>r\). If they lie in two incident distinct edges \(e,f\) sharing the unique vertex \(v\), write their distances from \(v\) as \(s,t\). Their shortest-path distance is at most \(r\) precisely when \(s+t\le r\). Indeed any route not traversing their common vertex must traverse at least one complete edge and cannot be short. When both lie on the same edge \(e\) with interval coordinates \(s,t\), the distance is at most \(r\) precisely when \(|s-t|\le r\): any alternative path between its endpoints traverses another full edge and exceeds \(r\). The simplicity and positive minimum length assumptions make these three possibilities exhaustive, including in the presence of cycles.

**2. Exact area of the close-pair locus.** Product arclength of ordered pairs of points on the same edge \(e\) with \(|s-t|\le r\) equals \(2\ell_e r-r^2\); this is the square of side \(\ell_e\) minus two triangles of side \(\ell_e-r\). For two distinct incident edges meeting at \(v\), the triangle \(s,t\ge0\), \(s+t\le r\) has area \(r^2/2\) for each *ordered* selection of the two edges, and so contributes \(r^2\) per unordered incident-edge pair. Nonincident edge pairs contribute zero. The unnormalized product arclength of all close pairs is exactly

\[
 \sum_{e\in E}(2\ell_e r-r^2)
 +r^2\sum_{v\in V}\binom{\deg(v)}2
 =2Lr+\left(\sum_v\binom{\deg(v)}2-m\right)r^2.
\]

Dividing by \(L^2\) proves the displayed distribution formula. Continuity supplies the case \(r=0\). Differentiation gives \(F'(0+)=2/L\) and \(F''(0+)=2B(G)/L^2\), hence the asserted inversion formulas.

**3. Subdivision and homological identity.** Splitting an edge into two inserts a vertex of degree two and increases the edge count by one. Its contribution \(\binom22=1\) cancels the change in the edge count, proving invariance of \(B\). The handshaking identity \(\sum_v\deg(v)=2m\) gives
\[
 2B=\sum_v\deg(v)(\deg(v)-2)
 =\sum_v(\deg(v)-2)^2+2\sum_v(\deg(v)-2)
 =\sum_v(\deg(v)-2)^2+4g-4.
\]

**4. Tree classification and sharpness.** In a tree, the degree-sum identity yields \(\#\{v:\deg(v)=1\}=2+\sum_{\deg(v)\ge3}(\deg(v)-2)\). Substituting in the preceding formula gives \(B=-1+\sum_{\deg(v)\ge3}\binom{\deg(v)-1}{2}\). Each term is nonnegative; it vanishes exactly when there are no vertices of degree at least three, i.e. when the connected tree is a path (including the single-edge path). For degrees at most three each branching vertex contributes exactly one, giving the trivalent count. Finally \(\sum_v\binom{\deg(v)}2\) is the number of unordered pairs of incident edges and cannot exceed \(\binom m2\). Equality means all edge pairs meet; in a tree with \(m\ge3\) this forces every edge to meet at the same central vertex, i.e. the star. The path and star show both bounds are attained.

## Verification

The supplied `verify.py` uses exact rational vertex-to-vertex shortest paths and independently integrates the affine endpoint-route inequalities in all ordered edge-pair parameter rectangles, with exact polygon clipping and shoelace areas. It checks eight connected graphs with unequal lengths, including paths, different stars, a cycle, a lollipop, a theta graph and a branched tree, at three rational radii each. It also checks the Betti/degree identity and an explicit local non-identifiability pair. Running `python verify.py` produced `ALL_CHECKS_PASSED`. This is a finite cross-check only: the universal proof is the preceding exhaustive geometric area argument.

## Relationship to prior work

The general distance and K-function framework for linear networks appears in Baddeley, Nair, Rakshit and McSwiggan (2017) and Rakshit, Nair and Baddeley (2017), with an efficient implementation in Rakshit, Baddeley and Nair (2019). These frameworks motivate examination of pairwise intrinsic distances; the stated new information is the **closed local quadratic coefficient as a subdivision-invariant discrete branch statistic**, its recovery without network labels, and its sharp tree/degree-three interpretations. The published 2020 work of Eckardt and Mateu develops different edge-count-based network-intensity characteristics; its Section 2.3 explicitly distinguishes that distance from edge-length shortest-path distance. No claim is made to have exhaustively excluded earlier equivalent formulae: full texts of the two relevant 2017 papers were not accessible for complete comparison.

## Limitations

A full two-point distance distribution can carry more information, but the local coefficient alone does not identify a graph: a metric circle and a three-arm metric star both have \(B=0\), for example. Tree branch counts follow from \(B\) only under a maximum-degree-three hypothesis. The uniform-arclength and simple-graph assumptions are essential to the exact formula as stated. This work makes no assertion about noisy sampling, finite-sample estimation accuracy, continuous sampling densities other than uniform, or uniqueness of full graph recovery. Priority remains provisional because some relevant earlier full texts could not be inspected. No external independent validation has been performed.

## References

1. A. Baddeley, G. Nair, S. Rakshit and G. McSwiggan, “Stationary” point processes are uncommon on linear networks, *Stat* 6 (2017), 68–78, DOI: 10.1002/sta4.135 (first public online 8 February 2017).
2. S. Rakshit, G. Nair and A. Baddeley, Second-order analysis of point patterns on a network using any distance metric, *Spatial Statistics* 22 (2017), 129–154, DOI: 10.1016/j.spasta.2017.10.002.
3. S. Rakshit, A. Baddeley and G. Nair, Efficient Code for Second Order Analysis of Events on a Linear Network, *Journal of Statistical Software* 90 (2019), DOI: 10.18637/jss.v090.i01.
4. M. Eckardt and J. Mateu, Second-order and local characteristics of network intensity functions, *TEST* 30 (2021), 318–340, first online 12 June 2020, DOI: 10.1007/s11749-020-00720-4.
