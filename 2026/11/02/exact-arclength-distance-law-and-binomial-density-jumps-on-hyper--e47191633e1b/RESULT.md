# Exact arclength distance law and binomial density jumps on hypercube wireframes

## Finding

For every integer \(d\ge3\), let \(Q_d\) be the metric one-skeleton of the unit Euclidean \(d\)-cube: it consists of \(d2^{d-1}\) edges of intrinsic length one, with shortest-path length as distance. Independently sample \(X,Y\) from normalized one-dimensional arclength on this graph, and write \(D_d=d_{Q_d}(X,Y)\). Its **complete probability law** is an explicit binomial mixture of two triangular kernels and a same-edge exception. In particular, its density is affine between successive integers but has genuine jumps of known sizes at **every** interior integer \(k=2,\ldots,d-1\):

\[
 f_d(k^-)-f_d(k^+)=\frac{2\binom{d-1}{k-1}}{d2^{d-1}}.
\]

Define probability densities (zero outside the displayed intervals)
\[
 \ell(t)=2(1-t)\quad(0<t<1),\qquad h(t)=2t\quad(0<t<1),
\]
\[
 g(t)=\begin{cases}t,&0<t<1,\\ 2-t,&1<t<2.\end{cases}
\]
Then a version of the density, for almost every real \(t\), is
\[
 \boxed{f_d(t)=\frac{1}{d2^{d-1}}\left[\ell(t)+\sum_{k=1}^{d-1}\binom{d-1}{k}h(t-k)\right]
 +\frac{d-1}{d2^{d-2}}\sum_{k=0}^{d-2}\binom{d-2}{k}g(t-k).}
\]
The distribution is absolutely continuous, supported on \([0,d]\), and has no atoms at the integer knots. It is continuous at \(t=1\), and the density's interior jump spectrum is exactly the displayed binomial sequence.

With \(p_d=2^{-(d-1)}\), the first two moments and variance are
\[
 \mathbb E D_d=\frac d2+\frac{1-2p_d}{6d},
\qquad
 \mathbb E D_d^2=\frac{d^2}{4}+\frac d4-\frac16+\frac{1-2p_d}{6d},
\]
\[
 \operatorname{Var}(D_d)=\frac d4-\frac13+\frac{p_d}{3}+\frac{1-2p_d}{6d}-\frac{(1-2p_d)^2}{36d^2}.
\]
There is also a central limit law
\[
 \frac{D_d-d/2}{\sqrt d/2}\ \Longrightarrow\ N(0,1)
\]
with distribution-function error \(O(d^{-1/2})\) uniformly in the threshold. The mean formula is a consequence of the full law, not asserted independently to be historically new.

## Assumptions and scope

The graph \(Q_d\) has vertex set \(\{0,1\}^d\); vertices differing in exactly one coordinate are joined by a unit edge. A point in an open edge is represented by its freely varying coordinate \(s\in(0,1)\). Distances are **intrinsic metric-graph geodesic distances**, not Euclidean chord lengths or Hamming distances between vertices. Sampling is uniform in total graph arclength: each edge has probability \(1/(d2^{d-1})\) and conditional arclength coordinate is uniform on \([0,1]\). The two sampled points are independent. Densities at knots are irrelevant; all one-sided limits are taken from the open adjacent cells. The main claimed novelty and sharp classification concern \(d\ge3\); \(d=2\) is a four-cycle and is excluded to avoid duplicating existing special cases.

## Proof

**1. Partition the two oriented edges.** Each edge of \(Q_d\) is uniquely specified by a coordinate direction \(I\in\{1,\ldots,d\}\) and the remaining \(d-1\) fixed independent fair bits. Thus the directions \(I,J\) for \(X,Y\) are independent uniform choices. The equal-direction event has probability \(1/d\); the different-direction event has probability \((d-1)/d\). Edge coordinates \(S,T\) are independent uniform variables and independent of edge choices.

**2. Different directions.** Condition on \(I\ne J\). Let \(K\) be the number of mismatched fixed bits in the \(d-2\) coordinates other than \(I,J\); then \(K\sim\operatorname{Bin}(d-2,1/2)\). At the \(I\)-coordinate, the second edge has a fixed fair bit, giving a travel contribution distributed uniformly on \([0,1]\) from \(X\) to that vertex layer. Similarly, at the \(J\)-coordinate, the first edge has a fixed fair bit, independently giving a second uniform contribution. A shortest route must correct all those coordinate mismatches, so
\[
 D_d\mid(I\ne J)\ \overset{\mathrm d}=\ K+U+V,
\quad U,V\overset{\mathrm{iid}}\sim\operatorname{Unif}(0,1),
\]
with mutually independent summands. Equivalently, one may minimize the four endpoint-route lengths; all four choices collapse to this expression because a path traverses each of the two distinct free coordinates at least once. The density of \(U+V\) is \(g\).

**3. Equal directions.** Condition on \(I=J\). Let \(K\sim\operatorname{Bin}(d-1,1/2)\) be the Hamming distance between fixed coordinates on the chosen edges. If \(K=0\), both points are on the very same edge, and the direct subsegment is shortest:
\[
 D_d=|S-T|,\qquad \Pr(K=0\mid I=J)=p_d.
\]
Its density is \(\ell\). If \(K\ge1\), a shortest route exits at equal-coordinate endpoints of the two edges; using opposite-coordinate endpoints costs at least one more full graph edge and cannot improve on such a route. Hence
\[
 D_d=K+W,\qquad W=\min(S+T,2-S-T).
\]
Since \(S+T\) has triangular density \(g\), folding around one gives \(\Pr(W\in dw)=2w\,dw\) for \(0<w<1\), i.e. density \(h\). The \(K\) mixture is independent of \(S,T\).

**4. Assemble the density.** Multiply these conditionals by \(1/d\) and \((d-1)/d\), then expand the binomial weights. This yields the boxed \(f_d\) without omitted components. Its integrals sum to one, each kernel has support of length one or two, and the maximum possible distance is \(d\). The only nonzero interior density jumps arise at the right endpoints of the \(h(t-j)\) kernels. Their size at integer \(k\) is \(2\binom{d-1}{k-1}/(d2^{d-1})\), for \(2\le k\le d-1\); at \(k=1\) the \(\ell\) and \(h\) boundary values both tend to zero, so no jump occurs. All \(g\)-terms are continuous.

**5. Moments.** Use the exact elementary moments
\[
 \mathbb E|S-T|=\frac13,\quad \mathbb E|S-T|^2=\frac16,
 \quad \mathbb EW=\frac23,\quad \mathbb EW^2=\frac12,
\]
\[
 \mathbb E(U+V)=1,\quad \mathbb E(U+V)^2=\frac76.
\]
For a binomial \(K_r\) of parameter \((r,1/2)\), \(\mathbb EK_r=r/2\) and \(\mathbb EK_r^2=(r^2+r)/4\). The different-direction conditional moments are \(d/2\) and \(d^2/4+d/4-1/3\). The equal-direction conditional moments are \(d/2+1/6-p_d/3\) and \(d^2/4+5d/12-1/6-p_d/3\). Their weighted mixtures give the stated first and second moments. Subtracting the square of the mean yields the variance.

**6. Normal limit.** Couple \(D_d\) to \(K_{d-2}+U+V\) so that they coincide whenever \(I\ne J\), an event of probability \(1-1/d\). Their distribution functions therefore differ uniformly by at most \(1/d\). The centered binomial \(K_{d-2}\) has a Berry–Esseen error \(O(d^{-1/2})\) under \(\sqrt d/2\) scaling; the bounded additive term \(U+V-1\) and replacing \(\sqrt{d-2}\) by \(\sqrt d\) preserve this order. The displayed weak convergence and uniform rate follow.

## Verification

Run `python3 artifacts/verify_metric_cube.py` using Python's standard library. The executable uses exact rational arithmetic: it explicitly enumerates all ordered pairs of edges for dimensions \(1\) through \(6\), compares a four-endpoint shortest-path formula against the independently reduced expression at three rational position pairs, and reports **133,347 passed comparisons**. It additionally integrates the proposed piecewise-affine density symbolically on every unit interval for dimensions \(1\) through \(25\), obtaining total mass one and both theoretical moments exactly. Finally it recovers and checks all interior one-sided integer jumps by exact rational interpolation for dimensions \(3\) through \(25\). This is supplementary finite verification; the proof above establishes the all-dimensional statements.

## Relationship to prior work

The continuous intrinsic metric on a graph and its mean distance have a history going back to Doyle–Graver (1982). Garijo, Márquez and Silveira (2021 preprint; 2023 publication) give algorithms for the continuous mean distance of weighted graphs and identify several graph families. Baptista, Kennedy and Mugnolo (2023 preprint; 2024 publication) study mean-distance estimates and examples on metric graphs. These works establish the general setting and methods but, in the portions available and inspected, do not furnish the full all-dimensional arclength **distribution** of the hypercube one-skeleton or its binomial jump spectrum. Classical Hamming-binomial vertex-to-vertex distances are not the same statistic. The four-cycle case \(Q_2\) is outside the novel claim, being a complete bipartite graph \(K_{2,2}\) and a standard elementary cycle. A full historical-priority judgment requires checking potentially related early shape papers, some of whose complete texts were not accessible.

## Limitations

The claimed law applies to unit-edge, unweighted, intrinsic hypercube wireframes with independent **arclength-uniform** points. It does not address Euclidean distances, weighted/distorted cubes, general Cartesian-product metric graphs or nonuniform sampling. The normal approximation is an asymptotic consequence, not a numerical sharp constant. The continuous-mean-distance formula may have antecedents in historical shape literature; the full density and contact/jump classification are the central results. Older Doyle–Graver articles were only accessible as abstracts/metadata in this comparison, so equivalent priority within their full text cannot be excluded. No independent scientific validation has been performed.

## References

- J. K. Doyle and J. E. Graver, “A Summary of Results on Mean Distance in Shapes,” *Environment and Planning B* 9 (1982), https://doi.org/10.1068/b090177. Public abstract examined; full text unavailable.
- J. K. Doyle and J. E. Graver, “Mean Distance for Shapes,” *Journal of Graph Theory* 6 (1982), https://doi.org/10.1002/jgt.3190060410. Metadata/abstract only; full text unavailable.
- V. D. Blondel et al., “Distance distribution in random graphs and application to network exploration,” *Physical Review E* 76 (2007), 066101, https://doi.org/10.1103/PhysRevE.76.066101. Public date verified 2007-12-05; a discrete random-graph comparator, not continuous hypercube arclength.
- D. Garijo, A. Márquez, and R. I. Silveira, “Continuous Mean Distance of a Weighted Graph,” arXiv:2103.11676 (2021); *Results in Mathematics* 78, 139 (2023), https://doi.org/10.1007/s00025-023-01902-w. Open-access publisher full text examined.
- A. Baptista, J. Kennedy, and D. Mugnolo, “Mean Distance on Metric Graphs,” arXiv:2312.04952 (2023), published 2024. Open-access full text examined.
