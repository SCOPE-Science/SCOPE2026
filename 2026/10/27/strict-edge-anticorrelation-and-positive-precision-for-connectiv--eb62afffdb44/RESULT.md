# Strict edge anticorrelation and positive precision for connectivity-conditioned \(K_{3,n}\)

## Finding
For every integer \(n\ge2\) and every \(p\in(0,1)\), retain independently each edge of the complete bipartite graph \(K_{3,n}\) with probability \(p\), and condition on the retained spanning subgraph being connected. Let \(X_e\) be the resulting presence indicator of each edge. For any two distinct edges \(e,f\),
\[
\operatorname{Cov}(X_e,X_f)<0.
\]
The covariance matrix \(\Sigma=(\operatorname{Cov}(X_e,X_f))_{e,f}\) is strictly positive definite; every entry of \(\Sigma^{-1}\) is strictly positive. In particular, every full-order *linear* partial correlation between distinct edge indicators is strictly negative. The theorem holds uniformly across graph size and probability, without asserting nonlinear conditional independence or full negative association.

## Assumptions and scope
The graph has three distinct left vertices and \(n\ge2\) distinct right vertices, with exactly one edge between each left/right pair. The same \(p\in(0,1)\) is used for all \(3n\) edges. Connectivity includes every vertex. The conditioning event has positive probability. Edges fall into three orbits under permutations of vertices within the two parts: two edges in the same right-vertex column, two in different columns with the same left endpoint, or two with neither endpoint shared. This is the complete pair classification.

## Proof
Set \(t=p/(1-p)>0\), \(x=1+t>1\), \(f=x^2+x+1\), \(g=x+2\), and \(h=3\). Every edge configuration of size \(m\) has relative weight \(t^m\). For each of the \(n\) right-hand columns, the weighted nonempty support is \(t f\). To require all three left vertices to lie in one connected component, apply Möbius inversion on their set partitions. A column's nonempty support constrained to remain inside the blocks of a partition has weight \(t f\), \(t g\), or \(t h\) for partition types \((3)\), \((2,1)\), or \((1,1,1)\), respectively. Since the partition-lattice Möbius coefficients from the top are \(1,-1,+2\), the total weight of connected configurations is \(t^n P\), where
\[
P=f^n-3g^n+2h^n>0.
\]
This counts configurations without isolated right vertices and with all left vertices connected; these two properties are equivalent to connectivity of the whole bipartite graph.

Differentiating column weights by marking a specified retained edge gives the single-edge numerator \(t^n E\), and marking two edges in the three geometries gives \(t^n C_{\mathrm{col}}\), \(t^n C_{\mathrm{row}}\), or \(t^n C_{\mathrm{dis}}\), respectively. Direct expansion of these marked partition sums gives
\[
\begin{aligned}
E&=x^2f^{n-1}-(2x+1)g^{n-1}+2h^{n-1},\\
C_{\mathrm{col}}&=t\big(xf^{n-1}-g^{n-1}\big),\\
C_{\mathrm{row}}&=x^4 f^{n-2}-(1+2x^2)g^{n-2}+2h^{n-2},\\
C_{\mathrm{dis}}&=x^4 f^{n-2}-x(x+2)g^{n-2}+2h^{n-2}.
\end{aligned}
\]
Thus each off-diagonal covariance has the sign of \(P C_j-E^2\) for its corresponding geometry \(j\). We show all three numerators strictly negative.

Put \(k=n-2\ge0\), \(u=h/g\), \(v=g/f\), and
\[
A=xg(2x+1),\qquad B=2(2x+1)^2,\qquad C=g^2.
\]
We have \(0<v<u<1\), since \(3f-g^2=(2x+1)(x-1)>0\). Elementary expansion and regrouping gives the *exact* identity
\[
P C_{\mathrm{dis}}-E^2=t^2f^kg^k\big(-A+B u^k-C v^k\big).
\]
At \(k=0\), \(A-B+C=2(x-1)^2(x+1)>0\). For every \(k\ge1\), the geometric-sum comparison gives
\[
\frac{1-v^k}{1-u^k}=\frac{1-v}{1-u}\frac{1+v+\cdots+v^{k-1}}{1+u+\cdots+u^{k-1}}\le\frac{1-v}{1-u}.
\]
Also \(B(1-u)>C(1-v)\), because the equivalent polynomial inequality is
\[
Bf-g^3(x+1)=(x-1)(7x^3+16x^2+16x+6)>0.
\]
Consequently \(B u^k-C v^k\le B-C\), giving \(-A+B u^k-C v^k\le -A+B-C<0\). This proves the disjoint-edge covariance is strictly negative for all \(n\ge2\).

For the same-left-endpoint type, \(C_{\mathrm{row}}=C_{\mathrm{dis}}-t^2g^k\), so its covariance numerator is strictly smaller and therefore negative. For \(n\ge3\), the remaining comparison is
\[
C_{\mathrm{col}}-C_{\mathrm{row}}=-xf^k+(x^2-x+3)g^k-2h^k.
\]
Writing \(r=f/g>1\), \(s=h/g<1\), observe \(xr+2s=x^2-x+3\). By Bernoulli's inequality \(z^k\ge1+k(z-1)\) for \(z>0\) and integer \(k\ge1\),
\[
xr^k+2s^k\ge x+2+k\big(x(r-1)+2(s-1)\big)=x+2+k(x-1)^2\ge x^2-x+3.
\]
Hence \(C_{\mathrm{col}}\le C_{\mathrm{row}}\) and the same-column covariance is strictly negative for \(n\ge3\). At \(n=2\), the direct identities
\[
P=(x-1)^2(x^2+4x+7),\qquad E=(x-1)^2(x^2+3x+4),\\
P C_{\mathrm{col}}-E^2=-2(x-1)^4(x+1)<0
\]
finish the classification.

For strict positive definiteness, note that the full edge set and each full set with exactly one deleted edge induce connected spanning subgraphs of \(K_{3,n}\). All have positive conditional probability. If a linear combination \(\sum_e a_eX_e\) had zero variance, comparing its values at the full configuration and each single-edge-deletion configuration would force every \(a_e=0\). Therefore \(\Sigma\) is positive definite.

Finally, \(\Sigma\) has strictly negative off-diagonal entries. Set \(\lambda=\max_e\Sigma_{ee}\) and \(B_0=\lambda I-\Sigma\), a symmetric entrywise nonnegative matrix with strictly positive off-diagonal entries. Its spectral radius is \(\lambda-\lambda_{\min}(\Sigma)<\lambda\) because the Perron eigenvalue is the largest eigenvalue of \(B_0\), while \(\lambda_{\min}(\Sigma)>0\). Thus
\[
\Sigma^{-1}=\frac1\lambda\sum_{m=0}^{\infty}(B_0/\lambda)^m
\]
converges and is strictly positive entrywise. The usual precision formula yields the negative linear partial correlations.

## Verification
Run `python verify.py` with Python 3 standard library. It enumerates all connected subgraphs of \(K_{3,n}\) for \(2\le n\le5\) by independent connectivity testing, compares the resulting exact weighted sums against all five closed formulas at three positive odds, and performs additional exact-integer checks of the covariance sign inequalities and the disjoint-edge factorization for larger parameters. The reported 1320 exact assertions passed. These finite tests do not prove the infinite-size claim; the preceding algebra and inequalities do.

## Relationship to prior work
The connectivity-conditioned edge law is the all-terminal reliability model. Grimmett and Winkler formulated the broad edge negative-correlation question for uniform connected subgraphs. Semple and Welsh proved relevant cases for graphs assembled from \(K_4\) and its minors using series and parallel extensions, a theorem that does not directly cover the family \(K_{3,n}\) for \(n\ge3\) (which contains \(K_{3,3}\)). Brown and McMullin studied graph connectivity and split-reliability optimization rather than edge covariances. The result here establishes the explicitly stated family and the stronger positive precision property; it is not a general-graph conjecture proof.

## Limitations
The proof requires three vertices on one side, independent homogeneous Bernoulli edge retention, and conditioning on all-terminal connectivity. It does not establish full negative association, unequal edge probabilities, arbitrary multipartite graphs, or nonlinear conditional independence. Although source comparisons did not identify an equivalent all-parameter theorem for this family, historical priority cannot be conclusively established by finite literature searches. Independent proof review has not been performed.

## References
1. G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), 444–460; preprint arXiv:math/0302185.
2. C. Semple and D. J. A. Welsh, *Negative Correlation in Graphs and Matroids*, theorem 4.4; available preprint: https://www.math.canterbury.ac.nz/~c.semple/papers/SW07.pdf.
3. J. I. Brown and I. McMullin, *On the Split Reliability of Graphs*, arXiv:2306.03884 (first posted 2023-06-06); Networks 82 (2023), 177–185.
