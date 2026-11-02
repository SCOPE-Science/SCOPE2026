# Sharp centered maximal-variation constants for paths through six vertices

## Finding
Let \(P_n\) be the path on vertices \(\{0,1,\ldots,n-1\}\) with nearest-neighbor edges, where \(n=5\) or \(n=6\). For a real function \(f\) on its vertices, define the centered Hardy–Littlewood maximal function and edgewise first variation by
\[
(Mf)(i)=\max_{0\le r\le n-1}\frac{\sum_{j\in B(i,r)}|f(j)|}{|B(i,r)|},\qquad
B(i,r)=\{j:0\le j<n,\ |j-i|\le r\},\qquad
\operatorname{Var}(f)=\sum_{i=0}^{n-2}|f(i+1)-f(i)|.
\]
**For both path lengths, the exact sharp constant is**
\[
\boxed{\operatorname{Var}(Mf)\le\frac{n-1}{n}\operatorname{Var}(f)\qquad(n\in\{5,6\}).}
\]
Equality is attained by the endpoint impulse \(f=(0,\ldots,0,1)\). In combination with the published exact cases through four vertices, this establishes the conjectured optimal constants rigorously for all path lengths from three through six.

## Assumptions and scope
The graph is an unweighted finite path with counting measure and **centered** graph balls. Only \(n\in\{5,6\}\) is proved here, and the variation exponent is \(p=1\). Arbitrary real vertex data are permitted, including all nonmonotone sign and variation patterns. The operator averages \(|f|\) before taking its maximal value.

## Proof
**Reduction to increments.** Since \(M(f)=M(|f|)\) and \(\operatorname{Var}(|f|)\le\operatorname{Var}(f)\), it is sufficient to prove the bound for nonnegative inputs. Put \(x_j=f(j+1)-f(j)\) for \(0\le j\le n-2\). Subtracting the common constant \(f(0)\) leaves maximal-function variation unchanged because every centered ball average changes by the same constant. Thus we may analyze the auxiliary vector \(y_0=0\), \(y_k=\sum_{j<k}x_j\) and the auxiliary linear-form maxima
\[
\widetilde M_i(x)=\max_{r}\frac{1}{|B(i,r)|}\sum_{k\in B(i,r)}y_k.
\]
Even if \(y\) has negative entries, translating all entries to be nonnegative leaves output variation unchanged; every real increment vector therefore represents an admissible nonnegative input up to translation. The original inequality is equivalent to
\[
 F_n(x):=\sum_{i=0}^{n-2}|\widetilde M_{i+1}(x)-\widetilde M_i(x)|
 \le\frac{n-1}{n}\sum_{j=0}^{n-2}|x_j|\qquad(x\in\mathbb R^{n-1}).
\]
Both sides are positively homogeneous, so it suffices to consider the \(\ell^1\)-unit sphere.

**Exact ball-average forms.** Every ball has size between one and six. Put \(L=60\) and define integer vectors \(a_{i,r}\in\mathbb Z^{n-1}\) by
\[
 a_{i,r,j}=\frac{60}{|B(i,r)|}\#\{k\in B(i,r):k>j\},\qquad 0\le j\le n-2.
\]
It follows directly from the definition of \(y\) that
\[
60\widetilde M_i(x)=\max_r\, a_{i,r}\cdot x.
\]
We discard duplicate linear forms at any fixed vertex.

**Complete reduction to finitely many rays.** For each vertex \(i\), form every nonzero difference \(a_{i,r}-a_{i,s}\) and make it a primitive integer normal with its first nonzero entry positive. Adjoin all \(n-1\) coordinate normals \(e_j\). This gives 27 different normals for \(n=5\), and 46 for \(n=6\). All planes pass through the origin. Their arrangement subdivides each orthant simplex of the \(\ell^1\)-unit sphere into compact convex polytopes on which, simultaneously for each vertex, a fixed linear form realizes \(\widetilde M_i\). Therefore \(F_n\) is a sum of absolute values of linear forms on each cell, hence convex there. Its maximum on each cell occurs at a cell vertex.

A cell vertex on an \((n-2)\)-dimensional orthant simplex satisfies \(n-2\) independent homogeneous equations from the comparison and coordinate planes. Thus it lies on the one-dimensional intersection of some \(n-2\) independent normals from the generated family; the oriented integer generators of those nullspaces form an overinclusive finite list of every possible maximizing vertex. A generator is computed exactly by the signed maximal minors of the \((n-2)\times(n-1)\) matrix of chosen normals. All \(\binom{27}{3}=2925\) normal triples and all \(\binom{46}{4}=163185\) normal quadruples are enumerated; both orientations are checked whenever the maximal minors are not all zero. This is exhaustive because every vertex is represented, irrespective of degeneracy or switching ties.

**Exact integer certificate.** The two attached standalone checkers regenerate the full normal families from the definitions, calculate the minors by exact arithmetic, and verify at every oriented ray \(x\) the integer inequality
\[
 n\sum_{i=0}^{n-2}\left|\max_r a_{i+1,r}\cdot x-\max_r a_{i,r}\cdot x\right|
 \le 60(n-1)\sum_{j=0}^{n-2}|x_j|.
\]
For \(n=5\), there are 2829 nondegenerate triples and 5658 oriented rays. For \(n=6\), there are 151429 nondegenerate quadruples and 302858 oriented rays. All comparisons pass, in both the C++ signed-integer implementation and a separately written Python arbitrary-integer implementation. The bound on the coefficient magnitudes and the dimensions ensure no signed 64-bit overflow in C++; the second implementation provides an independent arithmetic check. By the convexity and vertex argument, these exact finite computations imply the inequality for every real input, not merely a finite sample.

**Sharpness.** For the endpoint impulse \(f=(0,\ldots,0,1)\), each maximal average at a vertex is maximized by the smallest centered ball containing the endpoint. These maximal values are nondecreasing as the vertices approach that endpoint, their first value is \(1/n\), and their last value is \(1\). Hence
\[
\operatorname{Var}(Mf)=1-\frac1n=\frac{n-1}{n},\qquad \operatorname{Var}(f)=1,
\]
which proves optimality for both \(n\).

## Verification
The complete, independent C++ and Python sources are `path_maximal_exact.cpp` and `path_maximal_independent.py`. From this directory, run `c++ -std=c++17 -O2 path_maximal_exact.cpp -o path_maximal_exact && ./path_maximal_exact`, and independently `python3 path_maximal_independent.py` (standard library only). The expected exact counters are: \(n=5\), 27 normals, 2925 triples, 2829 full-rank intersections, 5658 oriented rays, 288 equality occurrences counted with multiplicity; \(n=6\), 46 normals, 163185 quadruples, 151429 full-rank intersections, 302858 oriented rays, 7268 equality occurrences with multiplicity. Both programs were executed against the packaged sources and returned these counters. The finite verification is exhaustive **because of the proved polyhedral reduction**, not because of a dense numerical grid.

## Relationship to prior work
González-Riquelme, Kovač and Madrid, arXiv:2603.12462v1 (first posted 12 March 2026), give exact path results through four vertices, present a computational observation for all connected five-vertex graphs, and state as Conjecture 5 that the path constant should be \(1-1/n\) for every \(n\ge3\). They explicitly label their tests through \(n\le10\) as numerical evidence and caution that their five-vertex optimization commands may not certify global maxima. Their theorem covering all graph orders applies to complete graphs, not general paths. The publicly available 2026 note *Monotone data attain the conjectured path-graph variational constant* proves the conjectured bound for monotone inputs on paths of every size but does not cover nonmonotone data. The present theorem provides exact complete certificates for arbitrary data at both five and six vertices. Earlier González-Riquelme–Madrid work, arXiv:2005.03146, establishes sharp estimates for complete and star graphs rather than these path cases.

## Limitations
This does not prove the conjecture for paths on seven or more vertices, does not characterize every extremizer, and does not address exponents other than \(1\). The exact finite proof requires running, or independently checking, the included exhaustive integer programs; the mathematical reduction specifies why the finite list is complete. Searches and full-text comparisons cannot exclude an unindexed or unpublished equivalent proof. No external independent mathematical audit has been performed.

## References
1. C. González-Riquelme, V. Kovač, J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1, 12 March 2026, https://arxiv.org/abs/2603.12462.
2. C. González-Riquelme, J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146v1, 6 May 2020, https://arxiv.org/abs/2005.03146.
3. F. Liu, Q. Xue, *On the variation of the Hardy–Littlewood maximal functions on finite graphs*, Collectanea Mathematica 72 (2021), 333–349, https://doi.org/10.1007/s13348-020-00290-6.
4. *Monotone data attain the conjectured path-graph variational constant*, publicly available research note (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-monotone-data-attain-the-conjectured-path-graph-variational-cons--2ae83e2401fb.
