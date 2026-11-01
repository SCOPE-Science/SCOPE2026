# Stochastic distance ordering and exact transport gaps in equilateral complete bipartite networks

## Finding

Let \(m,n\ge 1\) be integers and realize the complete bipartite graph \(K_{m,n}\) as a compact metric graph, with every edge an interval of length one and with its intrinsic shortest-path metric. Let \(X,Y\) be independent samples from normalized total arclength and put \(D_{m,n}=d(X,Y)\). Write \(N=m+n\) and \(P=mn\).

The entire cumulative distribution function is
\[
F_{m,n}(t)=\mathbb P(D_{m,n}\le t)=
\begin{cases}
0,&t\le 0,\\
\displaystyle\frac{2t+(N-4)t^2/2}{P},&0\le t\le1,\\
\displaystyle(t-1)^2+\frac{(2-t)[(N-1)t-(N-2)(2-t)/2]}{P},&1\le t\le2,\\
1,&t\ge2.
\end{cases}
\]
For \(m=n=1\), the support is only \([0,1]\), consistently with the same formula.

Fix an integer \(N\ge4\). If \(m+n=r+s=N\) and \(mn<rs\), then
\[
F_{m,n}(t)>F_{r,s}(t)\qquad(0<t<2).
\]
Thus balancing the bipartition makes the distance of two independently arclength-uniform points **strictly larger in first-order stochastic order**. Among all \(K_{m,N-m}\), the star uniquely minimizes and the balanced complete bipartite graph uniquely maximizes the entire distance law in this order, up to swapping the parts.

Moreover, the two distance laws have exact one-Wasserstein and total-variation separations:
\[
W_1(D_{m,n},D_{r,s})=\frac{2N}{3}\left(\frac1{mn}-\frac1{rs}\right),
\qquad
\operatorname{TV}(D_{m,n},D_{r,s})=\frac{2(N-1)^2}{3N-4}\left(\frac1{mn}-\frac1{rs}\right).
\]
The total-variation optimum is witnessed by the distance threshold
\[
t_* = \frac{2(2N-3)}{3N-4}\in(1,2).
\]
As \(N\to\infty\), both distances between the star and the most balanced biclique converge to \(2/3\). Their limiting sampled-distance laws are respectively the sum of two independent \(\operatorname{Uniform}[0,1]\) variables and the random variable \(2-|U-V|\) with \(U,V\) independent \(\operatorname{Uniform}[0,1]\).

## Assumptions and scope

The metric is the shortest length along the **entire network**, including interior edge points. Edges all have the same positive length; the formulas above fix that length to one. With common length \(\ell>0\), replace distances and the Wasserstein quantity by \(\ell\) times the displayed values, and evaluate CDFs at \(t/\ell\); total variation is unchanged. Points are independently uniformly sampled with respect to total edge arclength; thus edge labels are equally likely. The strict comparison and transport formulas require the same fixed number \(N\) of vertices, but allow different numbers \(P\) of edges. They are not claims for arbitrary weighted bicliques or for sampling graph vertices only.

## Proof

Choose an orientation of each edge from the part of size \(m\) to the part of size \(n\), and let the positions of two points be \(x,y\in[0,1]\). Conditional on the two independently selected edge labels, there are exactly three edge-pair types:

* **Identical:** \(P\) ordered edge pairs, distance \(|x-y|\).
* **Distinct, incident:** \(P(N-2)\) ordered pairs, distance \(x+y\) if the shared endpoint is in the first part and \(2-x-y\) if in the second part. Both expressions have the same law.
* **Disjoint:** \(P(P-N+1)=P(m-1)(n-1)\) ordered pairs, distance \(2-|x-y|\).

For incident edges, the direct route through the shared vertex has length at most two; any route avoiding it cannot be shorter because two vertices in the opposite part are at graph distance two. For disjoint edges, the two cross-endpoint routes have lengths \(2+x-y\) and \(2-x+y\); same-part endpoint routes have lengths at least two. The minimum is exactly \(2-|x-y|\). On one edge, the direct segment wins against any detour.

For independent uniform \(U,V\in[0,1]\), the distribution functions of \(|U-V|\), \(U+V\), and \(2-|U-V|\) are respectively
\[
F_0(t)=\begin{cases}2t-t^2,&0\le t\le1,\\1,&t\ge1,\end{cases}
\qquad
F_1(t)=\begin{cases}t^2/2,&0\le t\le1,\\1-(2-t)^2/2,&1\le t\le2,\end{cases}
\]
and
\[
F_2(t)=\begin{cases}0,&t\le1,\\(t-1)^2,&1\le t\le2,\\1,&t\ge2.\end{cases}
\]
All CDFs vanish below zero. Hence the exact mixture identity is
\[
F_{m,n}=\frac{F_0+(N-2)F_1+(P-N+1)F_2}{P}.
\]
Direct substitution gives the stated full CDF. It also proves the following decomposition at fixed \(N\):
\[
F_{m,n}(t)=F_2(t)+\frac{B_N(t)}{P},\qquad
B_N(t)=\begin{cases}
2t+(N-4)t^2/2,&0\le t\le1,\\
(2-t)[(N-1)t-(N-2)(2-t)/2],&1\le t\le2.
\end{cases}
\]
For \(N\ge4\), \(B_N(t)>0\) for every \(0<t<2\), giving strict stochastic comparison whenever the product \(P\) increases. Since \(m(N-m)\) increases strictly as \(m\) moves from one toward \(N/2\), the extremizers are unique up to interchanging the parts.

The derivative of \(B_N\) is positive for \(0<t<1\). On the remaining interval put \(u=2-t\); then
\[
B_N(t)=2(N-1)u-\frac{3N-4}{2}u^2.
\]
This strictly concave quadratic is maximized at \(u=2(N-1)/(3N-4)\), giving
\[
\max_{0\le t\le2}B_N(t)=\frac{2(N-1)^2}{3N-4}
\]
at the unique stated threshold \(t_*\). The sign of the difference of the two probability densities changes just once, from positive to negative, at \(t_*\). The total-variation distance therefore equals the maximal CDF difference and has the asserted exact value.

For probability laws on the real line, \(W_1\) is the integral of the absolute CDF difference. Direct polynomial integration gives
\[
\int_0^2B_N(t)\,dt=\frac{2N}{3},
\]
which proves the Wasserstein formula. Equivalently, the exact first and second moments are
\[
\mathbb E[D_{m,n}]=\frac53-\frac{2N}{3P},\qquad
\mathbb E[D_{m,n}^2]=\frac{17}{6}-\frac{10N-4}{6P}.
\]
For the limit, the star has \(P=N-1\), whereas the most balanced biclique has \(P=\lfloor N^2/4\rfloor\). In the mixture above, their incident- and disjoint-pair probabilities respectively tend to one, proving the stated limiting distributions. Taking limits in the exact transport formulas gives \(2/3\) for each gap.

## Verification

A standalone exact-rational checker, `verify_exact.py`, independently constructs all-pairs vertex distances and evaluates all four endpoint routes for network points. It compares these shortest paths with the three conditional distance formulas for every edge pair on \(K_{m,n}\), \(1\le m,n\le5\), on a rational coordinate grid. It also checks the CDF identities, moments, strict order, and sharp transport constants across a range of vertex counts and partitions. Its successful execution reported 40,570 exact-rational assertions. The proof above is algebraic and covers infinitely many sizes and all real positions; finite checks are only corroborative.

To reproduce, run `python3 verify_exact.py` with standard Python 3; no third-party dependencies are needed.

## Relationship to prior work

The continuum-of-points network metric and farthest-point framework appear in Bose and collaborators (2013). Doyle and Graver (1982) studied means of graph-shaped continuous domains. Garijo, Márquez, and Silveira (first public preprint 2021; journal 2023) derived general continuous mean-distance algorithms and an explicit equilateral **complete-graph**, rather than bipartite-graph, formula. Baptista, Kennedy, and Mugnolo (preprint 2023) established general geometric inequalities, mean-distance surgery principles, and flower/star examples. These results establish context and some first-moment tools but do not state the complete-biclique CDF, strict fixed-order stochastic comparison, or sharp distributional transport distances here. The \(K_{2,2}\) uniform-distance special case is already the elementary circle law and is not claimed as a separate novelty.

The exact bibliographic day of the 1982 historical work is not established by the available record; the 2013 arXiv preprint below supplies a precisely documented earlier-than-2016 public date for the metric-network setting. The later 2021 and 2023 literature is context, not evidence for a pre-2016 first-public date.

## Limitations

The results apply only to equilateral complete bipartite networks and arclength-uniform independent sampling. They compare distinct networks with the **same number of vertices**, not necessarily equal total edge length, and therefore do not assert that adding edges increases pointwise distances on an unchanged measured space. The stochastic comparison does not imply an ordering of centered variances. Historical priority is not conclusively established: the full 1982 Doyle–Graver article was not accessible for complete text comparison. The proof needs no computational premise, and the reported finite checker is not an independent audit.

## References

1. P. Bose et al., *Network Farthest-Point Diagrams*, arXiv:1304.1909, first posted 2013-04-06; later *Journal of Computational Geometry* 4 (2013), 182–211, DOI 10.20382/jocg.v4i1a8.
2. J. K. Doyle and J. E. Graver, *Mean distance for shapes*, *Journal of Graph Theory* 6 (1982), 453–471, DOI 10.1002/jgt.3190060410.
3. D. Garijo, A. Márquez, and R. I. Silveira, *Continuous mean distance of a weighted graph*, arXiv:2103.11676 (first posted 2021-03-22); *Results in Mathematics* 78 (2023), article 139, DOI 10.1007/s00025-023-01902-w.
4. L. N. Baptista, J. B. Kennedy, and D. Mugnolo, *Mean distance on metric graphs*, arXiv:2312.04952 (first posted 2023-12-08).
