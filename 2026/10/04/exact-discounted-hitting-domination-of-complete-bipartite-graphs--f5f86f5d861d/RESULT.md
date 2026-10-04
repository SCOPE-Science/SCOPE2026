# Exact discounted hitting domination of complete bipartite graphs
## Finding
Let \(K_{m,n}\) have bipartition \(A\cup B\) with \(|A|=m\) and \(|B|=n\), where \(m,n\ge 1\). Fix homogeneous fidelity \(0<\lambda<1\) and threshold \(0<\tau\le 1\). Then
\[
\delta_{\lambda,\tau}(K_{m,n})=\begin{cases}
m+n,&\tau>\lambda,\\
\min\{m,n\},&\tau=\lambda,\\
\min_{0\le a\le m}\bigl(a+b_a\bigr),&0<\tau<\lambda,
\end{cases}
\]
where \(b_m=0\). For \(0\le a<m\), define
\[
R_x(a)=\frac{n\left[\tau\left(m-\lambda^2(m-a)\right)-\lambda^2a\right]}{\lambda m-\lambda^2a-\tau\lambda^2(m-a)},
\]
\[
R_y(a)=\frac{n\left[\tau\left(m-\lambda^2(m-a)\right)-\lambda a\right]}{\lambda^2(m-a)(1-\tau)},
\]
and
\[
b_a=\min\!\left\{n,\max\!\left(0,\left\lceil R_x(a)\right\rceil,\left\lceil R_y(a)\right\rceil\right)\right\}.
\]
For fixed \(a<m\), \(b_a\) is exactly the least number of sources in \(B\) compatible with choosing \(a\) sources in \(A\). Thus the exponential source-set optimization collapses to a one-dimensional integer minimum.

A concrete structural consequence is
\[
\delta_{3/5,3/10}(K_{10,10})=6,
\]
and the unique optimal part-count profile is \((3,3)\). Hence an optimal source set on a complete bipartite graph need not be concentrated in one part.
## Assumptions and scope
The graph is finite, simple, and complete bipartite. The walk is the simple random walk and the fidelity is homogeneous. For a source set \(S\), the equilibrium support is \(h_v^S=\mathbb E_v[\lambda^{T_S}]\), and \(\delta_{\lambda,\tau}\) is the minimum \(|S|\) for which \(h_v^S\ge\tau\) at every vertex.

The formula includes stars and \(K_{1,1}\), but its new content is the full two-part family. It does not claim a formula for general complete multipartite graphs, heterogeneous fidelity, or non-simple transition weights.
## Proof
Choose \(a\) sources in \(A\) and \(b\) sources in \(B\). By automorphism symmetry, every non-source in \(A\) has a common support \(x\), and every non-source in \(B\) has a common support \(y\).

First suppose \(a<m\) and \(b<n\). The equilibrium equations are
\[
x=\frac{\lambda}{n}\bigl(b+(n-b)y\bigr),\qquad
y=\frac{\lambda}{m}\bigl(a+(m-a)x\bigr).
\]
Their determinant is positive because
\[
mn-\lambda^2(m-a)(n-b)>0.
\]
Solving gives
\[
x=\frac{\lambda m b+\lambda^2a(n-b)}{mn-\lambda^2(m-a)(n-b)},
\]
\[
y=\frac{\lambda n a+\lambda^2b(m-a)}{mn-\lambda^2(m-a)(n-b)}.
\]

Assume \(0<\tau<\lambda\). For fixed \(a<m\), cross-multiplication by the positive denominator shows that \(x\ge\tau\) is equivalent to \(b\ge R_x(a)\), while \(y\ge\tau\) is equivalent to \(b\ge R_y(a)\). The denominators defining \(R_x(a)\) and \(R_y(a)\) are positive: for the first,
\[
\lambda m-\lambda^2a-\tau\lambda^2(m-a)=\lambda\bigl(m-\lambda[a+\tau(m-a)]\bigr)>0,
\]
and the second is positive because \(a<m\) and \(\tau<1\). Therefore the least feasible integer \(b<n\) is the maximum of zero and the two ceilings. If that lower bound reaches or exceeds \(n\), selecting all \(n\) vertices of \(B\) is feasible because every remaining vertex of \(A\) then hits a source in one step and has support exactly \(\lambda>\tau\). This proves the stated expression for \(b_a\). The boundary profile \(a=m\) is feasible with \(b=0\) for the same one-step reason. Minimizing \(a+b_a\) over \(0\le a\le m\) proves the third case.

Now let \(\tau=\lambda\). A non-source at distance one from \(S\) has support at most \(\lambda\), with equality only if all of its neighbors are sources. In \(K_{m,n}\), if non-sources remain in both parts, every such vertex has a non-source neighbor, so the threshold cannot be met. Hence all non-sources must lie in one part, which forces the entire opposite part to be selected. Selecting the smaller part works and costs \(\min\{m,n\}\).

Finally, if \(\tau>\lambda\), every non-source has support at most \(\lambda<\tau\), so every vertex must be selected. This gives \(m+n\).

For the displayed \(K_{10,10}\) example, direct substitution into the exact profile inequalities shows that the only six-source feasible profile is \((3,3)\).
## Verification
The accompanying `verify_complete_bipartite.py` uses exact rational arithmetic only. It performs two independent checks.

First, for \(1\le m,n\le8\) and five rational fidelities, it compares the theorem's one-dimensional formula against exhaustive enumeration of every source-count profile; this covers \(1280\) parameter cases including thresholds below, at, and above \(\lambda\).

Second, for seven small complete bipartite graphs and four rational parameter pairs, it enumerates every source subset, solves the full equilibrium linear system over `Fraction`, and compares the optimum with the theorem. This gives \(28\) direct subset-level cases. The checker also verifies that \((3,3)\) is the unique optimum profile for \(K_{10,10}\) at \((3/5,3/10)\). Its stored output is `ALL CHECKS PASSED; profile_cases=1280; subset_cases=28; split_example=K10,10:(3,3)`.

These finite checks are stress tests of the symbolic proof; they are not used as an infinite proof.
## Relationship to prior work
Allagan, Pereyra, and Massey introduced discounted hitting domination and proved exact formulas for spiders, stars, and complete graphs. Their full text states that the exact graph-family results specialize to homogeneous fidelity and simple random walk, gives the star formula in Corollary 6.7, and treats complete graphs in Proposition 7.1. The paper contains no complete-bipartite theorem beyond the star subfamily, so the result above supplies the next natural dense two-class benchmark.

Guo, Lin, Wang, Wong, and Lin study the same terminating-walk hitting probability as a node-to-prescribed-group proximity quantity. Their pairwise and top-\(k\) queries evaluate or rank specified target groups relative to a source node; they do not minimize target-set cardinality subject to a uniform floor at every vertex. Li, Yu, Huang, and Cheng study fixed-budget finite-horizon random-walk objectives, again with aggregate rather than uniform-floor optimization. Thus neither prior model implies the stated \(K_{m,n}\) optimization formula.
## Limitations
For \(0<\tau<\lambda\), the answer is an exact one-dimensional integer minimization rather than a single elementary closed form in \(m\) and \(n\). The result is specific to homogeneous simple random walk on complete bipartite graphs. No claim is made for complete multipartite graphs with three or more parts, weighted walks, or heterogeneous fidelities.
## References
1. J. D. Allagan, K. Pereyra, and W. A. Massey, “Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms,” arXiv:2609.31535v1, submitted 2026-09-25.
2. Q. Guo, D. Lin, S. Wang, R. C.-W. Wong, and W. Lin, “Efficient Algorithms for Group Hitting Probability Queries on Large Graphs,” IEEE Transactions on Knowledge and Data Engineering 36 (2024), 2995–3008, DOI 10.1109/TKDE.2023.3349164.
3. R.-H. Li, J. X. Yu, X. Huang, and H. Cheng, “Random-walk domination in large graphs: problem definitions and fast solutions,” arXiv:1302.4546; ICDE 2014.
