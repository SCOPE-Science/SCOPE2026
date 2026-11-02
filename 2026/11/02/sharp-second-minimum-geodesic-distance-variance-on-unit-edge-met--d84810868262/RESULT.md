# Sharp second-minimum geodesic distance variance on unit-edge metric trees

## Finding

Let \(T\) be a finite simple tree with exactly \(m\ge3\) edges, each identified with a segment of length one. Sample independent points \(P,Q\) using normalized arclength on the whole metric tree, and write \(D_T=d_T(P,Q)\). Then

\[
\operatorname{Var}(D_T)\ge V_\star(m):=\frac{3m^2+6m-8}{18m^2},
\]

with equality if and only if \(T\) is the \(m\)-arm star. Among **all trees other than that star**, the unique second-minimum shape is the tree obtained by subdividing exactly one edge of the \((m-1)\)-arm star, and the exact strict gap is

\[
\operatorname{Var}(D_T)-V_\star(m)\ge
G_m:=\frac{2(m-2)(3m^2-2m+12)}{3m^4}>0.
\]

Equality holds in this second inequality precisely for that once-subdivided star. In particular, the theorem gives both the smallest and second-smallest values over **all isomorphism classes** with \(m\) unit edges, for every integer \(m\ge3\).

There is also an exact nonnegative variance-surplus identity. Choose two edges \(E,F\) independently and uniformly from the \(m\) edge labels, let \(d_L\) be shortest-path distance in the line graph of \(T\), and put

\[
Z=d_L(E,F)-\mathbf1_{\{E\ne F\}}\ge0.
\]

Then

\[
\boxed{\operatorname{Var}(D_T)-V_\star(m)
=\operatorname{Var}(Z)+\frac4{3m}\mathbb E[Z].}
\]

## Assumptions and scope

The graph is finite, connected, simple, acyclic and has \(m\ge3\) genuine unit-length edges; degree-two subdivisions therefore count as new unit edges. All distances use intrinsic shortest paths in its geometric realization, not ambient Euclidean distances. The two random points are independently uniform with respect to one-dimensional arclength, so each of the \(m\) edges is selected with probability \(1/m\). Vertex sampling has zero mass.

A star has one vertex of degree \(m\) and \(m\) leaves. A once-subdivided \((m-1)\)-arm star has degree multiset \((m-1,2,1,\ldots,1)\). At \(m=3\), it is exactly the three-edge path.

## Proof

**1. Exact integration conditional on the edge pair.** Let \(X=d_L(E,F)\). If \(E=F\), two uniform positions on a unit interval have distance \(|U-V|\), with first moment \(1/3\) and second moment \(1/6\). If \(E\ne F\), the unique tree route runs through \(X-1\) entire intervening edges and two independently uniform terminal edge portions. Thus its conditional mean is \(X\), and its conditional second moment is \(X^2+1/6\). Averaging gives

\[
\mathbb E D_T=\mathbb E X+\frac1{3m},\qquad
\mathbb E D_T^2=\mathbb E X^2+\frac16.
\]

Consequently,

\[
\operatorname{Var}(D_T)=\operatorname{Var}(X)+\frac16-
\frac{2\mathbb E X}{3m}-\frac1{9m^2}.
\]

**2. Exact variance surplus.** Set \(B=\mathbf1_{\{E\ne F\}}\) and \(Z=X-B\). Since distinct edges have positive integral line-graph distance, \(Z\ge0\). Because \(Z=0\) whenever \(B=0\),

\[
\mathbb E B=1-\frac1m,\quad
\operatorname{Var}(B)=\frac{m-1}{m^2},\quad
\operatorname{Cov}(B,Z)=\frac{\mathbb EZ}{m}.
\]

Using \(X=B+Z\) in step 1 and comparing with a star (where \(Z=0\) almost surely) gives the displayed surplus identity. Its constant term is

\[
V_\star(m)=\frac16+\frac1{3m}-\frac4{9m^2}.
\]

This already proves unique minimality of the star because any nonstar has a pair of nonincident edges and hence \(\mathbb EZ>0\).

**3. Exact incidence bounds.** Put \(p=\Pr(Z>0)\). Nonincident distinct edges are precisely those whose line-graph distance is at least two. For a tree with degrees \(d_v\), the number of unordered incident edge pairs is \(\sum_v\binom{d_v}{2}\); each pair has at most one common endpoint. Hence

\[
p=\frac2{m^2}\left[\binom m2-\sum_v\binom{d_v}{2}\right].
\]

There are \(m+1\) vertices, so the nonnegative integers \(a_v=d_v-1\) sum to \(m-1\). For a nonstar, every \(a_v\le m-2\). By convexity (or successive transfer of one unit from a smaller positive coordinate to a larger one), the maximum of \(\sum_v a_v^2\) under these integer constraints is \((m-2)^2+1\); equality requires the multiset \((m-2,1,0,\ldots,0)\). It follows that

\[
\sum_v\binom{d_v}{2}\le\binom{m-1}{2}+1,
\qquad p\ge q_m:=\frac{2(m-2)}{m^2}.
\]

Equality occurs only for a once-subdivided \((m-1)\)-arm star: the unique vertex of degree \(m-1\) has just one nonneighbor, and the degree-two vertex must join that vertex to the remaining leaf. (For \(m=3\), the same degree sequence uniquely specifies a path.)

Conversely \(\binom{d_v}{2}\ge d_v-1\) for all positive degrees, yielding \(\sum_v\binom{d_v}{2}\ge m-1\) and

\[
p\le r_m:=\frac{(m-1)(m-2)}{m^2}.
\]

Crucially, \(r_m+q_m=1-(m+2)/m^2<1\). Thus for every nonstar, \(q_m\le p\le r_m<1-q_m\).

**4. The sharp second minimum.** Conditional on \(Z>0\), the integer-valued \(Z\) is at least one. The law-of-total-variance identity therefore gives

\[
\begin{aligned}
\operatorname{Var}(Z)&=p\operatorname{Var}(Z\mid Z>0)
 +p(1-p)\big(\mathbb E[Z\mid Z>0]\big)^2\\
&\ge p(1-p),\qquad \mathbb EZ\ge p.
\end{aligned}
\]

For any \(p\in[q_m,1-q_m]\), \(p(1-p)\ge q_m(1-q_m)\). Applying the exact surplus identity yields

\[
\operatorname{Var}(D_T)-V_\star(m)
\ge q_m(1-q_m)+\frac4{3m}q_m
=\frac{2(m-2)(3m^2-2m+12)}{3m^4}.
\]

Equality forces \(p=q_m\), hence the once-subdivided star. In that tree every nonincident edge pair is separated by exactly one intermediate edge, so \(Z\in\{0,1\}\) and \(\Pr(Z=1)=q_m\). Both inequalities in step 4 are equalities. This establishes attainment and uniqueness for every \(m\ge3\).

For example, when \(m=4\), the minimum variance is \(2/9\); the unique second-minimum is \(71/144\). The theorem makes no claim about the *maximum* variance among unit-edge trees.

## Verification

The companion `verify_tree_variance.py` uses Python's standard library only and was executed after packaging-source review. It reconstructs trees independently via Prüfer codes, computes exact line-graph distances and integrates the two-point distance moments with rational arithmetic. It checks the variance-surplus equality, global lower bound, second-minimum value and equality classification exhaustively over every labeled tree with four through seven vertices, and on 1,300 seeded additional labeled trees with eight through twenty vertices (19,544 exact instances total). Four independent direct shortest-route midpoint quadratures test the geometry without using the line-graph moment formula. The recorded output was:

`VERIFY_OK 19544 exact Prüfer-coded trees plus four direct shortest-route quadratures; n=4..7 exhaustive, n=8..20 seeded samples`

Finite tests do not prove the inequalities for unbounded \(m\); the proof above does.

## Relationship to prior work

López de los Mozos and Mesa (2000; day-verified electronic source 2002-08-15) study continuous-demand *one-facility* variance, optimizing the position of a chosen point in a network. Their distance variance fixes one endpoint and does not give a two-independent-point tree-topology extremum. Puerto, Ricca and Scozzari (2009) likewise optimize the location of a path-shaped facility in a tree rather than the variance of two independent arclength samples.

Garijo, Márquez and Silveira (2023), Proposition 4.4, prove the sharp **mean**-distance bounds for uniform trees with stars and paths as extremizers. The first-order stochastic ordering of unit-edge tree-distance laws and even the sharp nonstar **mean** gap do not alone imply any ordering of variances: variances are not monotone under first-order stochastic dominance. What is additionally required here is the positive variance-surplus decomposition and the two-sided bound on the positive mass of the line-graph excess variable. Existing phylogenetic work on leaf-to-leaf distances studies a distinct sampling rule.

The claims of mean-distance extremality, location-variance algorithms, and generic moment integration are prior foundations, not originality claims. The specific sharp global and second-minimum **pairwise arclength-distance variance** classifications, their equality cases, and the exact remainder identity are the assertions being made here.

## Limitations

All original optimization statements require equal positive edge lengths, acyclicity, and independently sampled points over the full arclength. The results are not asserted for arbitrary positive edge lengths, cyclic graphs, vertex- or leaf-uniform sampling, or maximum variance. The exact formulas involve intrinsic network distances, not Euclidean embeddings. Historical priority has not been independently certified, and the finite verifier is not an infinite proof.

## References

1. M. C. López de los Mozos and J. A. Mesa, “The variance location problem on a network with continuously distributed demand,” *RAIRO Operations Research* **34** (2000), 155–181. DOI: `10.1051/ro:2000109`. Full primary text: https://www.numdam.org/item/RO_2000__34_2_155_0/ . Day-verified electronic publication: 2002-08-15, Cambridge Core.
2. J. Puerto, F. Ricca and A. Scozzari, “The continuous and discrete path-variance problems on trees,” *Networks* **53** (2009), 221–228. DOI: `10.1002/net.20284`.
3. D. Garijo, A. Márquez and R. I. Silveira, “Continuous Mean Distance of a Weighted Graph,” *Results in Mathematics* **78** (2023), article 139. DOI: `10.1007/s00025-023-01902-w`. Open-access full text: https://link.springer.com/article/10.1007/s00025-023-01902-w .
4. M. Sheinman, F. Massip and P. F. Arndt, “Statistical Properties of Pairwise Distances between Leaves on a Random Yule Tree,” arXiv:1407.7821 (2014). This concerns random leaf samples rather than arbitrary arclength pairs.
