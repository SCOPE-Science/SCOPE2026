# Sharp negative type and an exact distance-exponential cutoff on the odd graph \(O_4\)

## Finding
Let \(X=\binom{\{1,\ldots,7\}}{3}\), a set of \(35\) vertices. Join two distinct triples exactly when they are disjoint, and let \(d\) be the shortest-path distance in this odd graph \(O_4=KG(7,3)\). There is a unique exponent \(p_*\in(0,1)\) satisfying
\[
3(3^{p_*}-2^{p_*})=1,\qquad p_*=0.516584374300590\ldots.
\]
For every real \(p>0\), the kernel \(d^p\) is conditionally negative semidefinite exactly when \(p\le p_*\); it is strictly conditionally negative definite when \(0<p<p_*\). The least Euclidean dimension for points \(v_S\) with \(\|v_S-v_T\|^2=d(S,T)^p\) is \(34\) below the threshold and \(20\) at the threshold.

Consequently, for every \(p>0\), the kernels \(\exp(-t d^p)\) are positive semidefinite for **every** \(t>0\) exactly when \(0<p\le p_*\), and they are then strictly positive definite for every \(t>0\). For ordinary graph distance (\(p=1\)), the full individual-bandwidth classification is
\[
\bigl[\exp(-t d(S,T))\bigr]_{S,T\in X}\succeq0
\quad\Longleftrightarrow\quad t=0\ \text{or}\ t\ge\tfrac12\log 3.
\]
The ordinary distance-exponential kernel has rank \(1\) at \(t=0\), rank \(21\) at \(t=\frac12\log 3\), and rank \(35\) for larger \(t\).

## Assumptions and scope
All statements refer to the **finite**, simple, undirected graph on three-element subsets of a seven-element set, with unweighted shortest-path metric. Conditional negative semidefiniteness means that for every real vector \(c=(c_S)_{S\in X}\) satisfying \(\sum_S c_S=0\),
\[
\sum_{S,T\in X}c_S c_T d(S,T)^p\le0.
\]
Strictness means equality only when \(c=0\). Distances are not normalized: edges have length \(1\). The exponential scale \(t\) is nonnegative. Embedding dimension means the smallest real Euclidean affine dimension realizing the **squared** distances \(d^p\), not the original distances \(d\). Only the all-bandwidth statement is asserted for general \(p\); an individual-bandwidth phase diagram for \(p>p_*\), other than the specified case \(p=1\), is not claimed.

## Proof
For distinct triples with intersection cardinality \(r\), the graph distance is
\[
d(S,T)=\min\{2(3-r),\ 2r+1\}.
\]
This is \(2\) when \(r=2\), \(3\) when \(r=1\), and \(1\) when \(r=0\); the diagonal has distance \(0\). Let \(A_i\) be the binary matrix of pairs with \(|S\cap T|=3-i\), for \(i=0,1,2,3\). Thus \(A_0=I\) and
\[
D_p=(d(S,T)^p)_{S,T}=2^p A_1+3^p A_2+A_3.
\]

The four real isotypic subspaces of the Johnson association scheme \(J(7,3)\) have dimensions \(1,6,14,14\). The eigenvalue of \(A_i\) on sector \(j\) is the Eberlein coefficient
\[
P_{ji}=\sum_{h=0}^{j}(-1)^h\binom jh\binom{3-j}{i-h}\binom{4-j}{i-h},
\]
where an out-of-range binomial coefficient is zero. Explicit substitution gives the following rows \((P_{j0},P_{j1},P_{j2},P_{j3})\), listed with multiplicities:
\[
\begin{array}{c|c|rrrr}
j & m_j & P_{j0}&P_{j1}&P_{j2}&P_{j3}\\\hline
0&1&1&12&18&4\\
1&6&1&5&-3&-3\\
2&14&1&0&-3&2\\
3&14&1&-3&3&-1
\end{array}
\]
Hence the three eigenvalues of \(D_p\) on the orthogonal complement of constants are
\[
\lambda_1(p)=5\,2^p-3\,3^p-3,\qquad
\lambda_2(p)=2-3\,3^p,\qquad
\lambda_3(p)=3\,3^p-3\,2^p-1.
\]
The first two are strictly negative for every \(p>0\). The second assertion is immediate. For the first, put \(u=2^{p/2}\ge1\). Since \(3>2^{3/2}\), one has \(3^p>u^3\), and therefore
\[
-\lambda_1(p)>3u^3-5u^2+3\ge\frac{229}{243}>0,
\]
with the minimum of the displayed cubic on \([1,\infty)\) at \(u=10/9\). Finally \(\lambda_3(0)=-1\), \(\lambda_3(1)=2\), and
\[
\lambda_3'(p)=3(3^p\log3-2^p\log2)>0
\]
for every \(p\ge0\). Thus \(\lambda_3\) has precisely one zero \(p_*\in(0,1)\) and changes from negative to positive there. The constants are the sole excluded sector in the conditional quadratic form, proving the stated negative-type classification. The centered Gram matrix \(-\frac12 H D_p H\), with \(H=I-\frac1{35}J\), has ranks \(34\) and \(6+14=20\) in the respective regimes. The standard finite squared-distance characterization proves these are the least Euclidean dimensions.

For the exponential statement, conditional negative semidefiniteness of \(D_p\) gives a Euclidean realization of its squared distances. The Gaussian \(e^{-t\|v_S-v_T\|^2}\) is strictly positive definite on distinct points for every \(t>0\): expanding the exponential kernel into nonnegative polynomial Gram kernels and applying polynomial interpolation proves strictness. Conversely, for \(p>p_*\), on the third sector \(\lambda_3(p)>0\), whereas \(e^{-tD_p}\) **entrywise** (not as a matrix exponential) has sector eigenvalue \(-t\lambda_3(p)+O(t^2)<0\) as \(t\downarrow0\). Thus it cannot be positive semidefinite for all positive \(t\).

For \(p=1\) set \(x=e^{-t}\in(0,1]\). The kernel matrix is \(I+x A_3+x^2 A_1+x^3 A_2\). Its four sector eigenvalues, in the same order, factor as
\[
\begin{aligned}
F_0(x)&=1+4x+12x^2+18x^3,\\
F_1(x)&=(1-x)(1-2x+3x^2),\\
F_2(x)&=(1-x)(1+3x+3x^2),\\
F_3(x)&=(1-x)(1-3x^2).
\end{aligned}
\]
For \(0<x<1\), the first three are strictly positive; \(F_3(x)\ge0\) if and only if \(x\le3^{-1/2}\), equivalently \(t\ge\frac12\log3\). At \(x=1\), the matrix is \(J\) of rank one. At \(x=3^{-1/2}\), only sector three is zero, giving rank \(1+6+14=21\). For smaller positive \(x\), every eigenvalue is strictly positive, giving rank \(35\).

## Verification
The included standalone `verify_odd4.py` uses only the Python standard library. It independently enumerates all \(35\) triples; checks all-pairs shortest paths by breadth-first search; computes the four exact Eberlein rows; constructs rational spectral projectors from the disjointness adjacency matrix; checks every sector identity and rank; and checks the distance-exponential factorizations at \(51\) rational sample parameters. A direct execution returned `VERIFY_OK`, the sector multiplicities \([1,6,14,14]\), the ordinary-distance eigenvalues \([82,-2,-7,2]\), and \(p_*\approx0.516584374300590\). The universal sign arguments and the endpoint theorems are proved above, not inferred from the finite diagnostics.

Reproduce with `python3 verify_odd4.py` in a directory containing the extracted script; it reads no external data. Its exact finite calculations are supplementary to, not substitutes for, the analytic inequalities and the cited Johnson-scheme eigenspace formula.

## Relationship to prior work
Sánchez's 2011 study gives a general framework for supremal negative type in finite metrics but does not calculate this odd-graph invariant. Aalipour and collaborators (2015), especially their equations (7), Theorems 3.9 and 3.10, supply the Kneser distance relation and the Johnson/Eberlein decomposition **for the ordinary distance spectrum**; the table used here is a specialization of that classical scheme. Those results do not state the sharp powered-distance negative-type exponent, the \(14\)-dimensional endpoint loss, or the exact positive-bandwidth cutoff on the \(35\)-vertex graph. Tanaka's work on graph \(Q\)-matrices characterizes graphs with positive definiteness at all parameters, rather than providing the individual cutoff for this nonbipartite odd graph. The claim is an explicit new parameter classification on a canonical graph, not a new general eigenspace theorem. An equivalent calculation elsewhere in the literature is possible.

## Limitations
This is a finite homogeneous-space statement, not a theorem for all odd graphs or all Kneser graphs. For \(p>p_*\), the full set of individually admissible \(t\) is determined only at \(p=1\); general supercritical values are shown to fail for sufficiently small \(t\). The code confirms finite algebraic identities and selected parameters but is not an independent mathematical audit. The originality review is bounded, especially because the known Eberlein spectral formula makes some specializations accessible; priority over unindexed equivalent evaluations is not established. Independent audit and independent validation have not been performed.

## References
1. Stephen Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, first posted 2011-08-02, arXiv:1108.0451, https://arxiv.org/abs/1108.0451.
2. G. Aalipour et al., *On the distance spectra of graphs*, first posted 2015-09-03, arXiv:1509.01196, especially Section 3.2 and Theorems 3.9–3.10, https://arxiv.org/abs/1509.01196.
3. Hajime Tanaka, *Characterizing graphs with fully positive semidefinite \(Q\)-matrices*, arXiv:2208.11002, https://arxiv.org/abs/2208.11002.
