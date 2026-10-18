# A strictly negative exact covariance between reciprocal nearest neighbors and isolated vertices on the uniform circle

## Finding

Place \(n\ge5\) independent uniform random points on the unit circle \(\mathbb R/\mathbb Z\), with arc-length geodesic metric. Let \(M_n\) be the number of unordered pairs that are each other's nearest neighbor. For \(0\le r\le 1/2\), form the geometric graph connecting points at geodesic distance at most \(r\), and let \(I_n(r)\) be its number of isolated vertices. Write \(h_j(n,r)=(1-jr)_+^{n-1}\), where \(u_+=\max\{u,0\}\). Then, **for every finite \(n\ge5\)**,

\[
\operatorname{Cov}(M_n,I_n(r))=-\frac n3\left[h_2(n,r)-2h_3(n,r)+h_4(n,r)\right].
\]

This covariance is strictly negative for every \(0<r<1/2\), and is zero at \(r=0\) and \(r=1/2\). In the isolated-vertex critical window, with \(r_n=(\log n+x)/(2n)\) for a fixed real \(x\),

\[
\lim_{n\to\infty}\operatorname{Cov}(M_n,I_n(r_n))=-e^{-x}/3.
\]

A more general and exact conditional identity drives the result. If \(G_0,\ldots,G_{n-1}\) are positive, exchangeable and almost surely pairwise distinct circular gaps, set \(Q_r=\#\{i:G_i>r\}\), \(M=\#\{i:G_i<\min(G_{i-1},G_{i+1})\}\), and \(I=\#\{i:G_{i-1}>r,G_i>r\}\), with cyclic indices. Then \(M\) is independent of \(Q_r\), and for every integer \(0\le k\le n\) with positive conditioning probability,

\[
\operatorname{Cov}(M,I\mid Q_r=k)=-\frac{k(k-1)(n-k)(n-k-1)}{3(n-1)(n-2)(n-3)}.
\]

The conditional identity applies beyond the Dirichlet-gap case; the displayed unconditional formula specializes to uniform points on the circle.

## Assumptions and scope

All vertex locations are iid uniform relative to arc length; the number \(n\ge5\) is deterministic. A random rotation may put one uniformly selected point at the origin. The resulting cyclic gap vector \((G_i)\) has the \(\operatorname{Dirichlet}(1,\ldots,1)\) law on the unit simplex, which is exchangeable and has distinct coordinates almost surely. For a deterministic threshold \(0\le r\le1/2\), the graph has undirected edges exactly at geodesic distances at most \(r\). A nearest-neighbor tie has probability zero. Endpoint cases are included.

A nearest-neighbor reciprocal pair is an edge across a circular gap smaller than both of its neighboring gaps. A vertex has no neighbor within radius \(r\) exactly when its two bordering gaps both exceed \(r\). Thus the geometric quantities equal the displayed local-minimum and adjacent-threshold statistics. These characterizations are valid for the circle metric, not the straight-line interval metric.

## Proof

**1. Independent ranks and number of large gaps.** For any absolutely continuous exchangeable gap vector without ties, conditional on the increasing order statistics, the assignment of their values to the \(n\) indexed sites is a uniformly random permutation. In particular, the random relative order that determines \(M\) is independent of the number \(Q_r\) of coordinates above a threshold. By three-coordinate symmetry, \(\mathbb E[M\mid Q_r=k]=n/3\).

**2. Conditional local-minimum calculation.** Fix \(Q_r=k\). Let \(A\) be the event that a specified pair of consecutive gaps, indexed \(0,1\), both exceed \(r\). Its conditional probability is \(k(k-1)/[n(n-1)]\). Given \(A\), the remaining \(m=n-2\) gaps consist of \(h=k-2\) high and \(\ell=n-k\) low gaps, independently uniformly ranked within each category; every high value exceeds every low value. The local-minimum probabilities at gap indices \(0,1\) are both \(b=h/[3(n-2)]\). At their immediate exterior neighbors \(-1,2\), the probabilities are both

\[
a=\frac{\ell h+\ell(\ell-1)/2+h(h-1)/3}{(n-2)(n-3)}.
\]

This follows by sampling the two still-unfixed gaps without replacement: if the candidate is low and the other is high, it is certainly below the other and the prescribed high gap; if both are low, its chance is \(1/2\); if both are high, its chance of being the smallest of three highs is \(1/3\). At the other \(n-4\) gap indices, the local-minimum probability remains \(1/3\) by symmetry of their three positions; each of these remaining triples avoids both prescribed high-gap sites, so their ranks remain symmetric and the minimum occurs at each location with probability \(1/3\). Consequently,

\[
\mathbb E[M\mid A,Q_r=k]-n/3=2a+2b-4/3=-\frac{\ell(\ell-1)}{3(n-2)(n-3)}.
\]

This identity also follows by direct counting of uniform permutations of the high and low ranks. The cases \(k=0,1\) have \(\Pr(A\mid Q_r=k)=0\), and the conditional covariance formula then holds trivially. Because \(I=\sum_i\mathbf 1\{G_{i-1}>r,G_i>r\}\), and cyclic symmetry makes the \(n\) summands interchangeable,

\[
\operatorname{Cov}(M,I\mid Q_r=k)=n\Pr(A\mid Q_r=k)\big(\mathbb E[M\mid A,Q_r=k]-n/3\big),
\]

which gives the claimed rational expression.

**3. Removing the condition.** As \(\mathbb E[M\mid Q_r]=n/3\) is constant, the law of total covariance gives

\[
\operatorname{Cov}(M,I)=-\frac{\mathbb E[(Q_r)_2(n-Q_r)_2]}{3(n-1)(n-2)(n-3)},
\]

with falling factorial \((t)_j=t(t-1)\cdots(t-j+1)\). The expectation is \((n)_4\) times the probability that two specified gaps exceed \(r\) while two other specified gaps do not.

For Dirichlet spacings, the volume of the truncated simplex gives, for distinct coordinates and any integer \(j\ge0\),

\[
\Pr(G_1>r,\ldots,G_j>r)=(1-jr)_+^{n-1}.
\]

Applying inclusion-exclusion to the two required small gaps yields exactly \(h_2-2h_3+h_4\); since \((n)_4=n(n-1)(n-2)(n-3)\), the asserted finite covariance follows.

**4. Strict sign and critical asymptotics.** For \(0<r<1/2\), the event that two named gaps exceed \(r\) and two other named gaps do not has strictly positive simplex volume. Hence its probability \(h_2-2h_3+h_4\) is strictly positive. At \(r=0\), all gaps exceed zero, so \(I_n(0)=0\); at \(r=1/2\), two consecutive gaps cannot both exceed the half-circle, so \(I_n(1/2)=0\). Finally, for \(r_n=(\log n+x)/(2n)\), \(n h_2(n,r_n)\to e^{-x}\), whereas \(n h_3(n,r_n)\to0\) and \(n h_4(n,r_n)\to0\). This yields the limit \(-e^{-x}/3\).

## Verification

The accompanying standalone `verify.py` runs with the standard Python library. It exhaustively enumerates all cyclic orders of lengths \(5\) through \(8\) (\(46{,}200\) permutations) and every admissible high-gap count, checking the conditional covariance by exact rational arithmetic. It also checks the Dirichlet inclusion-exclusion distribution at eight rational radii, the finite covariance identity, three large-size numerical critical-window values, and direct geometric interpretations for reproducible random point sets. A completed run prints `VERIFY_OK permutations= 46200 checks= 45131`. Exact rational finite enumeration does not replace the analytic proof for all \(n\).

## Relationship to prior work

Decreusefond and Ferraz analyze component-count distributions and coverage structure in a one-dimensional Poisson random geometric graph, including circular geometry. The present statistic counts reciprocal nearest-neighbor pairs and their mixed moment with hard-radius isolated vertices; it is neither a component-count formula nor a marginal isolated-vertex formula. Pickard's early work concerns isolated *nearest-neighbor pairs* in spatial point processes; this is distinct from isolated vertices in a fixed-radius geometric graph, and the exact mixed covariance here is not established by the available description. Ma and Chow enumerate cyclic permutation peaks and valleys in a permutation-cycle model, a related but different statistic from local minima among circular order spacings with threshold marks. The classical one-third reciprocal-pair mean is not claimed as new. The value of the finding is the all-radii mixed covariance, its universal conditional-rank form and the nonzero rare-isolation critical-window limit.

## Limitations

The result concerns a fixed number of iid uniform points on a one-dimensional circle, a hard geodesic threshold, and the count of reciprocal 1-nearest-neighbor pairs. It does not establish higher-dimensional analogues, a joint central-limit or Poisson approximation, or stronger forms of asymptotic independence. Historical priority has not been independently established: a sufficiently general published joint local-pattern enumeration could subsume the conditional identity. Pickard's 1982 full text was not accessible during source inspection, so its exact implications have not been ruled out beyond the available abstract and bibliographic description.

## References

- L. Decreusefond and E. Ferraz, *On the One dimensional Poisson Random Geometric Graph*, arXiv:1008.5140v1, publicly submitted 2010-08-30; original full text inspected (especially the circle-component section). https://arxiv.org/abs/1008.5140
- S.-M. Ma and T. Chow, *Enumeration of permutations by number of cyclic occurrence of peaks and valleys*, arXiv:1203.6264v1, publicly submitted 2012-03-28; original full text inspected for the precise permutation-cycle definition. https://arxiv.org/abs/1203.6264
- D. K. Pickard, *Isolated nearest neighbors*, Journal of Applied Probability 19 (1982), 444–449, DOI 10.2307/3213499. Abstract/bibliographic material inspected; original full text not accessible. https://doi.org/10.2307/3213499
