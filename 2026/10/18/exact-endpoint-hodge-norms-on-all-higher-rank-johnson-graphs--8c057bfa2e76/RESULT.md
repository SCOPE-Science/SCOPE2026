# Exact endpoint Hodge norms on all higher-rank Johnson graphs

## Finding
Let \(n\ge6\) and \(3\le k\le\lfloor n/2\rfloor\) be integers, and let \(G=J(n,k)\) be the simple graph whose vertices are the \(k\)-element subsets of an \(n\)-element set, adjacent when their intersection has size \(k-1\). Give every edge unit conductance and fix any orientation. Write \(D:\mathbb R^{E}\to\mathbb R^{V}\) for the vertex-edge incidence operator and \(L=DD^{\mathsf T}\) for the combinatorial Laplacian. Define the **canonical Euclidean orthogonal** projections
\[
 Q=D^{\mathsf T}L^+D\quad\text{and}\quad C=I-Q
\]
onto the graph's real cut and cycle spaces, respectively. The same matrices act on the counting-measure edge space \(\ell_1(E)\) or \(\ell_\infty(E)\).

Their exact endpoint norms are
\[
 \boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}
 =\frac{(k+1)n^2-(k^2+3)n+2}{n(n-1)}}. \tag{1}
\]
With \(N=\binom nk\), the complementary projection has norm
\[
 \boxed{\|C\|_{1\to1}=\|C\|_{\infty\to\infty}
 =1+\frac{(k+1)n^2-(k^2+3)n+2}{n(n-1)}
   -\frac{4(1-N^{-1})}{k(n-k)}}. \tag{2}
\]
Consequently, \(\|C\|_{1\to1}>\|Q\|_{1\to1}\) throughout the stated domain. For fixed \(k\), these norms converge to \(k+1\) and \(k+2\) as \(n\to\infty\). Among Johnson ranks \(1\le j\le\lfloor n/2\rfloor\), the cut norm strictly increases with \(j\) and is maximal at the balanced rank. At \(k=\lfloor n/2\rfloor\), both norms equal \(n/4+O(1)\), while their difference tends to \(1\). The isomorphism \(J(n,k)\cong J(n,n-k)\) extends these statements to complementary ranks.

The previously established rank-two formula is recovered by formally taking \(k=2\), but **only ranks \(k\ge3\) are asserted as new**. The theorem concerns the canonical orthogonal projections, not least norms over all projections onto their ranges.

## Assumptions and scope
The edge-coordinate spaces are real, finite dimensional, and not normalized by \(|E|\). The Euclidean orthogonal projectors \(Q,C\) are uniquely defined by the ordinary counting inner product and do not depend, up to signed coordinate conjugation, on the orientation. Every graph is simple, connected and unweighted. A source edge carries net electrical injection \(+1\) at one endpoint and \(-1\) at the other. The Moore–Penrose inverse \(L^+\) is zero on constants. The proof treats all integers in the stated range, not just the finitely checked examples.

## Proof
**1. Edge-rooted potential levels.** Fix adjacent \(k\)-sets \(U\cup\{a\}\) and \(U\cup\{b\}\), where \(|U|=k-1\) and \(a,b\notin U\). Put \(W=[n]\setminus(U\cup\{a,b\})\), so \(|W|=n-k-1\). Let \(h\) solve \(Lh=\mathbf1_{U\cup\{a\}}-\mathbf1_{U\cup\{b\}}\) with zero mean. Permutations of \(U\) and \(W\), and the transposition of \(a,b\), imply that \(h\) is zero on vertices containing both or neither of \(a,b\). On a vertex containing \(a\) but not \(b\), it takes a value \(p_i\), where \(i\) is the number of elements of \(U\) present; on the exchanged vertex containing \(b\) but not \(a\), it takes \(-p_i\). Here \(0\le i\le k-1\).

The number of positive vertices at level \(i\) is
\[
 w_i=\binom{k-1}{i}\binom{n-k-1}{k-1-i}.
\]
From a positive vertex of level \(i\), the number of positive neighbors at levels \(i+1\) and \(i-1\) is, respectively,
\[
 u_i=(k-1-i)^2,\qquad d_i=i(n-2k+i).
\]
There is exactly one negative neighbor (obtained by exchanging \(a\) and \(b\)) and exactly \(n-2\) zero-potential neighbors. All other positive neighbors have unchanged level. Thus the Poisson equation becomes
\[
 (n+u_i+d_i)p_i-u_ip_{i+1}-d_ip_{i-1}
 =\mathbf1_{\{i=k-1\}}, \tag{3}
\]
with absent boundary terms understood to vanish. Because \(n\ge2k\), the tridiagonal operator on the left is irreducible and strictly diagonally dominant, with nonpositive off-diagonal entries. Its inverse is strictly positive, so every \(p_i>0\).

**2. Strict ordering of levels.** For \(0\le i\le k-2\), set \(\Delta_i=p_{i+1}-p_i\). Subtracting consecutive equations (3) yields
\[
 (n+d_{i+1}+u_i)\Delta_i
   -u_{i+1}\Delta_{i+1}-d_i\Delta_{i-1}
   =\mathbf1_{\{i=k-2\}}. \tag{4}
\]
In each row, the diagonal coefficient exceeds the sum of absolute off-diagonal coefficients by \(2(n-1)>0\), since \(u_i-u_{i+1}+d_{i+1}-d_i=n-2\). The off-diagonal entries are nonpositive and nearest-neighbor couplings inside the index interval are strictly positive. Hence the inverse is positive and (4) implies \(\Delta_i>0\) for every \(i\). Therefore
\[
 0<p_0<p_1<\cdots<p_{k-1}. \tag{5}
\]
This sign classification is essential: the absolute values of all edge currents can now be summed exactly.

**3. Two Green-function moments.** Set
\[
 (Tf)_i=u_i(f_{i+1}-f_i)+d_i(f_{i-1}-f_i),
\]
so (3) reads \((nI-T)p=\mathbf1_{\{k-1\}}\). The detailed-balance identity \(w_i u_i=w_{i+1}d_{i+1}\) makes \(T\) self-adjoint for the weighted sum \(\sum_iw_i\,\cdot\). Summing (3), using \(w_{k-1}=1\), gives
\[
 S_0:=\sum_{i=0}^{k-1}w_ip_i=\frac1n. \tag{6}
\]
Moreover, \((Ti)_i=u_i-d_i=(k-1)^2-(n-2)i\), where \(i\) in this expression denotes the coordinate function on the level set. Multiply (3) by \(iw_i\) and sum to obtain
\[
 S_1:=\sum_{i=0}^{k-1}i w_ip_i
 =\frac{(k-1)+(k-1)^2/n}{2(n-1)}. \tag{7}
\]
By shifting indices with detailed balance,
\[
 \sum_{i=1}^{k-1}w_id_i(p_i-p_{i-1})
 =\sum_iw_i(d_i-u_i)p_i
 =(n-2)S_1-(k-1)^2S_0. \tag{8}
\]

**4. Exact absolute-current norm.** The transfer-current column of the test edge is the vector of edge differences of \(h\). Each positive vertex has \(n-2\) zero-potential neighbors, and one negative neighbor across which the potential difference is \(2p_i\). The positive–zero and negative–zero edges together contribute \(2(n-2)S_0\); the positive–negative edges contribute \(2S_0\). Between consecutive positive levels, edges contribute \(\sum_{i=1}^{k-1}w_id_i(p_i-p_{i-1})\); the negative levels contribute the same amount. No other edges contribute. Using (5), their absolute current sum is exactly
\[
 \|Q\mathbf e_e\|_1
 =2\left((n-1)S_0+\sum_{i=1}^{k-1}w_id_i(p_i-p_{i-1})\right). \tag{9}
\]
Insert (6)–(8) into (9), expand and simplify:
\[
 \|Q\mathbf e_e\|_1
 =\frac{(k+1)n^2-(k^2+3)n+2}{n(n-1)}.
\]
The symmetric group acts transitively on the unordered edges of \(J(n,k)\); signed coordinate conjugation preserves absolute column sums. Hence every column of \(Q\) has this norm, establishing (1).

**5. Complementary projection.** The graph has \(N=\binom nk\) vertices and \(Nk(n-k)/2\) edges. As \(Q\) is an orthogonal projector of rank \(N-1\) with equal diagonal entries, every diagonal entry is
\[
 R=\frac{N-1}{Nk(n-k)/2}
   =\frac{2(1-N^{-1})}{k(n-k)}. \tag{10}
\]
Because \(0\le R\le1\), the diagonal entry in the corresponding column of \(C=I-Q\) has absolute value \(1-R\), while all off-diagonal magnitudes agree with those of \(Q\). Therefore \(\|C\mathbf e_e\|_1=1+\|Q\mathbf e_e\|_1-2R\), giving (2). Symmetry of each matrix gives equal \(\ell_1\) and \(\ell_\infty\) operator norms. For the stated \(k\), one has \(k(n-k)\ge9\), so \(2R<1\) and the cycle norm exceeds the cut norm.

**6. Extremal rank and growth.** The right-hand side of (1) at successive ranks differs by
\[
 \|Q_{J(n,k+1)}\|_{1\to1}-\|Q_{J(n,k)}\|_{1\to1}
 =\frac{n-2k-1}{n-1}>0
\]
whenever \(1\le k<\lfloor n/2\rfloor\). The rank-one and rank-two endpoint identities also follow from the same calculation; the rank-two case was independently known. At \(k=\lfloor n/2\rfloor\), (1) equals \(n/4+5/4+O(1/n)\). The correction term in (2) is \(O(n^{-2})\) at balanced rank, so the cycle norm is \(n/4+9/4+O(1/n)\). For fixed \(k\), the right-hand sides of (1)–(2) tend to \(k+1\) and \(k+2\), respectively. This proves all assertions.

## Verification
The accompanying `verify_johnson.py` uses only Python's standard library. It constructs Johnson-graph Laplacians independently of the level-chain derivation, solves exact rational grounded Poisson systems, sums the absolute edge currents directly and checks their diagonal contributions. It also reconstructs the orbit potentials and tests their strict ordering and the two weighted identities (6)–(7). The following instances passed exactly:

| \((n,k)\) | Vertex count | Edge count | \(\|Q\|_{1\to1}\) | \(\|C\|_{1\to1}\) |
|---|---:|---:|---:|---:|
| \((6,3)\) | 20 | 90 | \(37/15\) | \(137/45\) |
| \((7,3)\) | 35 | 210 | \(19/7\) | \(356/105\) |
| \((8,3)\) | 56 | 420 | \(81/28\) | \(305/84\) |
| \((8,4)\) | 70 | 560 | \(85/28\) | \(1061/280\) |
| \((9,4)\) | 126 | 1260 | \(59/18\) | \(257/63\) |

Two rank-two instances were also checked as controls. A separate exact-rational check of the level-chain equations passed at \((n,k)=(10,5),(18,9),(40,20),(100,3),(100,50)\). The checker certifies only these finite tests; equations (3)–(10) provide the all-rank proof.

## Relationship to prior work
Dilworth, Kutzarova, and Ostrovskii (2023, arXiv:2305.12582) develop orthogonal/invariant graph cycle-space projections and evaluate the Hamming-cube cut norm. The present Johnson-graph family is a distinct permutation-homogeneous graph construction, not a Cartesian Hamming graph; the cited paper's theorems do not give (1)–(2). Schild, Rao, and Srivastava (2017, arXiv:1708.01632) bound electrical-flow localization on general graphs and explain its connection to routing, but establish no exact Johnson-rank expression. Later general transfer-current bounds likewise do not imply the exact absolute-value formula. The known triangular-graph result, corresponding to \(k=2\), is expressly excluded from the new contribution. Related Johnson-scheme spherical projections act on **vertex** coordinates rather than on oriented **edge** gradients and do not supply the sign ordering (5) or the endpoint norms (1)–(2).

## Limitations
Only the canonical Euclidean orthogonal cut and cycle projections are evaluated. The results do **not** claim minimal operator norms among all linear projections, nor any exact norms for \(1<p<\infty\) aside from the Hilbert norm \(1\). The checker treats finite sample graphs and is not a formal infinite-family certification. A differently phrased exact result in unindexed electrical-network or Johnson-scheme literature remains a bibliographic possibility. No independent mathematical audit is asserted.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first posted 2023-05-21, sections 1 and 2.6–2.7.
2. A. Schild, S. Rao, N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632, first posted 2017-08-04, Theorems 1.4–1.5.
3. O. Gurel-Gurevich, A. Nachmias, S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130, first posted 2026-05-22, Theorems 1.1–1.3.
