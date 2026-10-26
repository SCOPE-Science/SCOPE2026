# Exact fragmentation-length covariance in an interval nearest-neighbor graph

## Finding

Let \(n\ge2\) points be sampled independently and uniformly from \((0,1)\). Join each point to its closest *other* sampled point, and forget orientations and duplicate edges. Write \(C_n\) for the number of connected components of the resulting undirected graph and \(L_n\) for the sum of the lengths of its **distinct** edges. Then

\[
\operatorname{Cov}(C_n,L_n)=
\begin{cases}
0,&n=2,3,\\[3pt]
-11/135,&n=4,\\[3pt]
-(139n+405)/(2700(n+1)),&n\ge5.
\end{cases}
\]

In particular this covariance is strictly negative for every \(n\ge4\), is strictly increasing in \(n\) for \(n\ge4\), and converges to the nonzero constant \(-139/2700\). For \(n\ge3\), the complementary first-moment identities are
\[
\mathbb E[C_n]=n/3,\qquad
\mathbb E[L_n]=(7n+15)/(18(n+1)).
\]

## Assumptions and scope

All points are i.i.d. with the uniform law on the unit interval; nearest-neighbor ties have probability zero. An edge is counted once if either of its endpoints selects the other. This undirected, simple edge set must be distinguished from the directed nearest-neighbor multiset, where mutual choices are counted twice. The result is exact for every finite sample size in the indicated ranges. The first moments are stated only for \(n\ge3\).

## Proof

**1. Gaps and removed edges.** Order the sample as \(X_{(1)}<\cdots<X_{(n)}\), and define its \(n-1\) internal gaps by \(G_i=X_{(i+1)}-X_{(i)}\), indexed by \(1\le i\le n-1\). A nearest-neighbor edge always joins consecutive sample points. The boundary edges \(G_1,G_{n-1}\) are always present. For \(2\le i\le n-2\), the edge of length \(G_i\) is absent precisely when \(G_i>\max(G_{i-1},G_{i+1})\). Call this event \(A_i=1\). The graph is a path with these locally maximal gaps deleted, so
\[
 C_n=1+\sum_{i=2}^{n-2}A_i,
 \qquad L_n=\sum_{i=1}^{n-1}G_i-\sum_{i=2}^{n-2}A_iG_i.
\]

**2. Exponential representation and covariance transfer.** Let \(E_0,E_1,\ldots,E_n\) be independent standard exponential random variables and \(S=\sum_{j=0}^n E_j\). Standard uniform-spacing theory gives the joint distribution \((G_1,\ldots,G_{n-1})\overset d=(E_1/S,\ldots,E_{n-1}/S)\). The indicators \(A_i\) are therefore the local-maximum indicators of the internal exponential sample. Set \(W=\sum_{i=1}^{n-1}E_i\) and \(B=\sum_{i=2}^{n-2}A_iE_i\), so \(L_n=(W-B)/S\). The exponential vector's sum \(S\) is independent of its normalized proportions, hence of \((C_n,L_n)\); moreover \(C_n\), which depends only on the relative ranks of the internal exponentials, is independent of their sum \(W\). Since \(\mathbb E S=n+1\),
\[
\operatorname{Cov}(C_n,L_n)
=\frac{\operatorname{Cov}(C_n,W-B)}{n+1}
=-\frac{\operatorname{Cov}(C_n,B)}{n+1}.
\]

**3. Three local mixed moments.** For any interior index, exchangeability gives \(\mathbb E A_i=1/3\). Conditional on being the maximum of its three independent exponential neighbors, \(E_i\) has the distribution of the largest of three exponentials, whose expectation is \(H_3=11/6\). Thus \(\mathbb E[A_iE_i]=11/18\). Consequently the on-site covariance is
\[
\operatorname{Cov}(A_i,A_iE_i)=11/27.
\]
Adjacent peaks cannot both occur, so for adjacent indices
\[
\operatorname{Cov}(A_i,A_{i+1}E_{i+1})=-11/54.
\]
Peaks two steps apart overlap at one exponential. Among the \(5!=120\) possible relative-rank arrangements of the relevant five variables, those having peaks in positions two and four contain the value at position four as the third, fourth, or fifth order statistic with multiplicities respectively \(2,6,8\). As the expected \(r\)-th order statistic among five standard exponentials equals \(H_5-H_{5-r}\), this gives
\[
\mathbb E[A_iA_{i+2}E_{i+2}]
=\frac{2(H_5-H_2)+6(H_5-H_1)+8H_5}{120}
=\frac{413}{1800},
\]
and therefore
\[
\operatorname{Cov}(A_i,A_{i+2}E_{i+2})
=\frac{413}{1800}-\frac{11}{54}=\frac{139}{5400}.
\]
All mixed covariances at separation at least three vanish because the underlying exponential sets are disjoint.

**4. Summation.** There are \(t=n-3\) possible removed edges when \(n\ge4\). Summing the ordered on-site, adjacent, and distance-two pairs yields
\[
\operatorname{Cov}(C_n,B)
=t\frac{11}{27}-2(t-1)\frac{11}{54}
+2\max(t-2,0)\frac{139}{5400}
=\frac{11}{27}+\max(t-2,0)\frac{139}{2700}.
\]
For \(n=4\), the second term vanishes and division by \(n+1=5\) gives \(-11/135\). For \(n\ge5\), substituting \(t=n-3\) and simplifying gives the displayed rational formula. For \(n=2,3\), no internal gap can be deleted, hence \(C_n\equiv1\). The limit and strict sign are immediate. The finite-size covariance is strictly increasing after \(n=5\), since its expression equals \(-(139+266/(n+1))/2700\); direct comparison covers the step from \(n=4\) to \(n=5\).

**5. First moments.** For \(n\ge3\), the formulas above and \(\mathbb E[A_iE_i]=11/18\) give \(\mathbb E C_n=1+(n-3)/3=n/3\) and
\[
\mathbb E L_n
=\frac{(n-1)-(n-3)(11/18)}{n+1}
=\frac{7n+15}{18(n+1)}.
\]
This completes the proof.

## Verification

The standalone standard-library Python script `verify_nearest_neighbor.py` computes the weighted five-rank count independently, checks that direct nearest-neighbor edges agree with locally maximal-gap deletion for all permutations of distinct integer gaps up to six gaps, and exhaustively averages all \((n-1)!\) possible internal-gap rank patterns in exact rational arithmetic for each \(2\le n\le9\). It independently recovers every case of the covariance formula in that finite range, including both exceptional sample sizes. Run `python3 verify_nearest_neighbor.py`; the recorded output is `verification_output.txt`. These finite checks corroborate, but are not substitutes for, the general proof.

## Relationship to prior work

Penrose and Wade (arXiv:math/0603561v1, first public 2006-03-23) analyze length functionals of nearest-neighbor graphs on uniform points in one dimension. Their Theorem 2.3 and Section 5 concern the mean and variance of the **directed** sum of nearest-neighbor lengths; Section 4.2 supplies the Dirichlet-spacing representation. These statements do not give the cross-covariance of **undirected distinct-edge length** with the number of connected components. Sadasiv and Meng (2001) study cluster-size distributions in nearest-neighbor networks, but their available abstract does not state joint edge-length moments. Baryshnikov and Yukich (2004) give general Gaussian-limit covariance functionals for spatial graph scores; those limit statements do not evaluate the finite-\(n\) mixed covariance above or its explicit rational limiting constant. Generic laws for sample-gap order statistics do not by themselves give the adjacency-sensitive mixed moment of two local peaks used in the proof.

## Limitations

The formula is specific to independent uniform points on a bounded interval and to the undirected, distinct-edge interpretation. It has not been proved here for nonuniform input, circles, higher dimensions, directed multiplicity-weighted length, or higher moments. Exhaustive verification covers only \(n\le9\), while the theorem for all \(n\) is established analytically. The full text of Sadasiv and Meng (2001) could not be materially inspected through the available sources; this leaves a priority risk, though its accessible abstract addresses cluster-size distributions rather than the present mixed functional. Historical originality is not independently certified.

## References

1. M. D. Penrose and A. R. Wade, *Limit theory for the random on-line nearest-neighbour graph*, arXiv:math/0603561v1, 23 March 2006. https://arxiv.org/abs/math/0603561 (especially Sections 2.2, 4.2 and 5).
2. G. Sadasiv and Y. Meng, *Clustering of points randomly distributed in n-dimensional space*, Physical Review E 63 (2001), 027101. https://doi.org/10.1103/PhysRevE.63.027101.
3. Yu. Baryshnikov and J. E. Yukich, *Gaussian Limits for Random Measures in Geometric Probability*, 19 May 2004 manuscript. https://www.lehigh.edu/~jey0/by2.pdf (particularly Section 3.1).
4. A. R. Wade, *Explicit laws of large numbers for random nearest-neighbour-type graphs*, Advances in Applied Probability 39 (2007), 326-342; arXiv:math/0603559. https://arxiv.org/abs/math/0603559.
