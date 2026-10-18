# Double sign reversal of edge–isolate covariance on the random geometric circle

## Finding

Place \(n\ge2\) independent uniform points on a circle of circumference one. Join two points precisely when their shorter circular distance is at most \(r\), with \(0<r<1/2\). Let \(E_{n,r}\) be the number of graph edges and \(I_{n,r}\) the number of isolated vertices. Set \(a=1-2r\), and
\[
 p(r)=\begin{cases}1-\bigl((1-3r)/(1-2r)\bigr)^2,&0<r\le1/3,\\1,&1/3<r<1/2.\end{cases}
\]
Then for every stated \(n,r\),
\[
 \operatorname{Cov}(E_{n,r},I_{n,r})
 =n a^{n-1}\left[\binom{n-1}{2}p(r)-n(n-1)r\right].\tag{1}
\]
In particular, on \(0<r\le1/3\),
\[
 \operatorname{Cov}(E_{n,r},I_{n,r})
 =\frac{n(n-1)}2r(1-2r)^{n-3}
 \bigl[-4+(3n+10)r-8nr^2\bigr].\tag{2}
\]
For \(n\le5\) the covariance is strictly negative at every \(0<r<1/2\). For every \(n\ge6\) put
\[
 r_-(n)=\frac{3n+10-\sqrt{(3n+10)^2-128n}}{16n},
 \qquad r_+(n)=\frac{n-2}{2n}.
\]
They obey \(0<r_-(n)<r_+(n)<1/2\), with \(r_-(6)=1/4\), \(r_+(6)=1/3\); for \(n\ge7\), \(r_-(n)<1/3<r_+(n)\). The covariance is **strictly negative** for \(0<r<r_-(n)\), **strictly positive** for \(r_-(n)<r<r_+(n)\), and **strictly negative** for \(r_+(n)<r<1/2\). Its only zeros in the open radius range are these two thresholds.

As \(n\to\infty\),
\[
 r_-(n)=\frac4{3n}+\frac8{27n^2}+O(n^{-3}),\qquad
 r_+(n)=\frac12-\frac1n.
\]
For each fixed \(c>0\), the sparse window \(r=c/n\) has the limit
\[
 \frac{\operatorname{Cov}(E_{n,c/n},I_{n,c/n})}{n}
 \longrightarrow \frac12 e^{-2c}c(3c-4).\tag{3}
\]
Thus a growing sparse-circle graph changes covariance sign when its asymptotic mean degree \(2c\) passes \(8/3\).

## Assumptions and scope

The circle is the quotient \(\mathbb R/\mathbb Z\) equipped with the shortest-arc distance. The points are independent and exactly uniform; the vertex number \(n\) is deterministic. Edges are undirected and the radius is shared by every pair. Ties in the distance criterion have probability zero. The result concerns ordinary (unstandardized) covariance, not correlation; no Poissonization, independent-edge approximation, or asymptotic assumption is used in equations (1) and (2). The symbols \(E_{n,r}\) and \(I_{n,r}\) refer to the same random graph.

## Proof

**Conditional geometry.** Fix a labeled vertex \(v\). The event \(\{v\text{ is isolated}\}\) requires all other \(n-1\) points to avoid the open circular arc of length \(2r\) centered at \(v\); hence its probability is \(a^{n-1}\). Conditional on this event and on the position of \(v\), the remaining \(n-1\) positions are independent uniform points on the complementary connected arc of length \(a\). Parametrize this arc by \([0,a]\). For two of its independent positions \(U,V\), note that \(0\le |U-V|\le a=1-2r<1-r\). Therefore their circular graph edge is equivalent to \(|U-V|\le r\) (the alternative \(|U-V|\ge1-r\) is impossible). The difference of two independent uniforms on \([0,a]\) has triangular law. Consequently
\[
 \Pr(|U-V|\le r)=
 \begin{cases}1-(a-r)^2/a^2,&r\le a,\\1,&r>a,\end{cases}
\]
which is exactly \(p(r)\), because \(r\le a\) is equivalent to \(r\le1/3\). All edges incident to the isolated vertex are absent, while each of the \(\binom{n-1}{2}\) other pairs is conditionally an edge with probability \(p(r)\). Thus
\[
 \mathbb E[E_{n,r}\mid v\text{ isolated}]=\binom{n-1}{2}p(r).
\]

**Mixed moment.** Sum over the \(n\) isolation indicators and use exchangeability:
\[
 \mathbb E[E_{n,r}I_{n,r}]
 =n a^{n-1}\binom{n-1}{2}p(r).
\]
A uniformly chosen pair has circular distance at most \(r\) with probability \(2r\), so \(\mathbb E[E_{n,r}]=\binom n2 2r=n(n-1)r\), while \(\mathbb E[I_{n,r}]=na^{n-1}\). Subtract their product to prove (1). On \(0<r\le1/3\), substitute \(p(r)=(2r-5r^2)/(1-2r)^2\) and collect terms; the resulting exact identity is (2).

**Sign classification.** For \(r\ge1/3\), equation (1) becomes a strictly positive factor times \((n-2)-2nr\). If \(n\le5\), this is strictly negative for \(r>1/3\), and nonpositive at the junction. For \(n\le5\) the quadratic \(Q_n(r)=-4+(3n+10)r-8nr^2\) is strictly negative on \(0<r\le1/3\): for \(n=2\) it is \(-4(1-2r)^2\), and for \(n=3,4,5\) its discriminant \((3n+10)^2-128n\) is negative. For \(n=6\), \(Q_6(r)\) has roots \(1/4,1/3\), is positive precisely between them, and the second branch is negative above \(1/3\). For every \(n\ge7\), \(Q_n(0)=-4<0\), while \(Q_n(1/3)=(n-6)/9>0\); since this is a concave quadratic with two real roots, exactly its smaller root \(r_-(n)\) lies in \((0,1/3)\). The second-branch factor is positive at \(1/3\) and crosses zero once at \(r_+(n)=(n-2)/(2n)>1/3\). These observations prove both sign changes and exclude further zeros.

**Scaling.** Algebraic Taylor expansion of the explicit smaller root yields \(r_-(n)=4/(3n)+8/(27n^2)+O(n^{-3})\); the second root is already exact. At \(r=c/n\), for sufficiently large \(n\), \(p(r)=2r+3r^2+O(r^3)\) and \((1-2r)^{n-1}\to e^{-2c}\). Substitute in (1): the bracket is \((3c^2-4c)/2+O(n^{-1})\) after its factor \(\binom{n-1}{2}\) is accounted for; equivalently \(\binom{n-1}{2}p(r)-n(n-1)r=(3c^2-4c)/2+O(n^{-1})\). Division by \(n\) proves (3). The asymptotic expected degree is \(2nr\to2c\), producing the threshold \(8/3\).

## Verification

The accompanying standalone Python file `verify_edges_isolates.py` checks the polynomial identity with exact rational arithmetic for every integer \(2\le n\le40\) and each rational \(r=k/200\), \(1\le k\le99\), including predicted signs away from zero. It separately estimates covariance by independent graph simulation at six parameter pairs on both sides of the transitions. The arithmetic checks and simulations passed. Neither finite arithmetic checks nor random simulation replaces the preceding proof for all \(n,r\).

## Relationship to prior work

Dall and Christensen (2002) give the basic spatial random-geometric graph framework, including degree and cluster properties. Decreusefond and Ferraz (2010) derive component-count distributions for a **Poisson** graph on intervals and circles. Penrose (2015) studies Poisson approximation to isolated vertices and, separately, edge counts in general spatial graphs. These works motivate the mixed observable but the inspected texts do not provide the finite-\(n\) piecewise covariance identity (1) or its two sign transitions. Penrose's earlier monograph *Random Geometric Graphs*, especially its chapter on subgraph and component counts, describes limiting covariance calculations and is a significant overlap risk: the full chapter was not accessible for definitive comparison. Distinct source models and asymptotic covariance statements do not by themselves entail the exact all-radius sign classification, but an implicit or previously tabulated equivalent is possible.

## Limitations

This is a self-review, not independent audit. The theorem is limited to a fixed number of independent uniform points on a one-dimensional circle and a deterministic hard connection radius; it does not establish analogous thresholds for intervals, higher dimensions, Poisson point counts, soft connection functions, or heterogeneous sampling. The limiting calculation fixes \(c>0\), and uniform behavior for growing \(c\) is not claimed. Some closely related earlier monograph material could not be inspected in full, so literary originality retains residual risk.

## References

1. J. Dall and M. Christensen, *Random Geometric Graphs* (2002), arXiv:cond-mat/0203026, first public version 2002-03-01, https://arxiv.org/abs/cond-mat/0203026 .
2. L. Decreusefond and E. Ferraz, *On the One dimensional Poisson Random Geometric Graph* (2010), arXiv:1008.5140, https://arxiv.org/abs/1008.5140 .
3. M. D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation* (2015), arXiv:1507.07132, https://arxiv.org/abs/1507.07132 .
4. M. D. Penrose, *Random Geometric Graphs*, Oxford University Press (2003), chapter 3, https://doi.org/10.1093/acprof:oso/9780198506263.003.0003 .
