# Binary open-neighborhood parity codes of biclique two-token graphs

## Finding
Fix integers \(2\le m\le n\), let \(G=K_{m,n}\), and let \(H=F_2(G)\) be its two-token graph. A *parity configuration* is a subset \(S\subseteq V(H)\) for which every vertex of \(H\) has an even number of neighbors in \(S\), **excluding itself**. Write \(W_{m,n}(z)=\sum_S z^{|S|}\) for the cardinality enumerator of these configurations.

Put \(\delta=1\) if both \(m,n\) are even, and \(\delta=0\) otherwise. Define, for each integer \(q\ge2\),
\[
E_q(z)=2^{-q}\sum_{j=0}^q\binom qj(1+z)^{\binom q2-j(q-j)}(1-z)^{j(q-j)},
\]
\[
O_q(z)=2^{-q}\sum_{j=0}^q(-1)^j\binom qj(1+z)^{\binom q2-j(q-j)}(1-z)^{j(q-j)},
\]
and, with \(w(p,q)=p(n-q)+(m-p)q\),
\[
X_{m,n}(z)=2^{-(m+n-2)}\sum_{\substack{0\le p\le m\\p\text{ even}}}\sum_{\substack{0\le q\le n\\q\text{ even}}}\binom mp\binom nq(1+z)^{mn-w(p,q)}(1-z)^{w(p,q)}.
\]
Despite their rational-looking presentations, these are integer polynomials. The complete, all-cardinality result is
\[
\boxed{W_{m,n}(z)=X_{m,n}(z)\big(E_m(z)E_n(z)+\delta O_m(z)O_n(z)\big).}
\]
The binary adjacency matrix of \(H\) has rank \(2(m+n-2-\delta)\), and hence the number of parity configurations is
\[
\boxed{W_{m,n}(1)=2^{\binom{m+n}{2}-2(m+n-2-\delta)}.}
\]
The minimum size of a nonempty parity configuration is \(2\) when \(m=2\), and \(3\) when \(m\ge3\). For \(m=2<n\) there are exactly \(n\) configurations of size two; for \(m=n=2\) there are exactly seven. For \(3\le m\le n\), the number of size-three configurations is
\[
\boxed{\binom m3+\binom n3+6\mathbf1_{m=n=3}.}
\]

## Assumptions and scope
All graphs are finite, simple, undirected and labelled. The two parts of the original biclique are \(A\) and \(B\), with \(|A|=m\), \(|B|=n\). The vertices of \(H\) are unordered pairs from \(A\cup B\). Two token vertices are adjacent exactly when they differ in one member and the two exchanged original vertices are adjacent in \(K_{m,n}\). The field is \(\mathbb F_2\). This is an **open**-neighborhood parity condition, not the closed-neighborhood Lights-Out condition. The nonzero minimum concerns nonempty \(S\); the zero configuration is included in \(W_{m,n}\).

## Proof
Partition \(V(H)\) into the \(mn\) mixed token vertices \(\mathcal X=\{\{a,b\}:a\in A,b\in B\}\) and the \(\binom m2+\binom n2\) pure vertices \(\mathcal Y=\binom A2\cup\binom B2\). The token graph is bipartite between \(\mathcal X\) and \(\mathcal Y\). Write its adjacency matrix as
\[
A_H=\begin{pmatrix}0&T\\T^{\mathsf T}&0\end{pmatrix},
\]
where \(T\) maps a selection of pure vertices to its neighbor-parity vector on the mixed vertices.

**Image and rank of \(T\).** Interpret a binary vector on \(\binom A2\) or \(\binom B2\) as an edge set of a complete graph. Its degree-parity vector has even coordinate sum; conversely every even-sum vector occurs (since the vectors \(e_i+e_j\) span the even-sum subspace for \(q\ge2\)). Thus
\[
\operatorname{im}T=\{(\alpha_a+\beta_b)_{a\in A,b\in B}:\ \sum_a\alpha_a=0,\ \sum_b\beta_b=0\}.
\]
The kernel of the displayed parametrization consists of the constant pairs \((\alpha,\beta)=(t\mathbf1_m,t\mathbf1_n)\). The choice \(t=1\) is allowed exactly when both part sizes are even. Therefore \(\operatorname{rank}_{\mathbb F_2}T=m+n-2-\delta\). The two off-diagonal blocks act on disjoint coordinate groups, so \(\operatorname{rank}_{\mathbb F_2}A_H=2\operatorname{rank}T\). Rank-nullity gives the asserted dimension and total count.

**The pure-coordinate factor.** A binary pure vector belongs to \(\ker T\) precisely when its two degree-parity vectors are equal constants, say \(t\mathbf1_m\) and \(t\mathbf1_n\). For \(t=0\), both selected complete-graph edge sets have even degrees. For \(t=1\), both have odd degrees, which is possible only if both \(m,n\) are even. The two edge-set enumerators therefore multiply as \(E_mE_n+\delta O_mO_n\).

To verify the explicit formulas for \(E_q,O_q\), take a binary edge vector on \(K_q\), apply the character projection \(2^{-q}\sum_{u\in\mathbb F_2^q}(-1)^{u\cdot(d-t\mathbf1)}\) to its degree-parity vector \(d\), and sum the edge choices. If \(u\) has \(j\) ones, exactly \(j(q-j)\) edges cross its sign partition. This yields \((1+z)^{\binom q2-j(q-j)}(1-z)^{j(q-j)}\), with the extra \((-1)^j\) for \(t=1\), proving both formulas.

**The mixed-coordinate factor.** The mixed-vector condition is \(T^{\mathsf T}x=0\), meaning that all \(m\) row parities of the \(m\times n\) binary matrix \(x\) are equal and all \(n\) column parities are equal. More directly, by character orthogonality for the code \(\ker T^{\mathsf T}\),
\[
\sum_{x\in\ker T^{\mathsf T}}z^{\operatorname{wt}(x)}
=\frac1{|\operatorname{im}T|}\sum_{h\in\operatorname{im}T}\prod_{a,b}(1+(-1)^{h_{ab}}z).
\]
Use the even-sum parametrization \(h_{ab}=\alpha_a+\beta_b\). Every image vector has exactly \(2^\delta\) preimages, while the image has \(2^{m+n-2-\delta}\) elements. If \(\alpha\) and \(\beta\) have even weights \(p\) and \(q\), the image vector has exactly \(w(p,q)=p(n-q)+(m-p)q\) ones. Combining the multiplicity and denominator gives the stated \(X_{m,n}\) formula. Mixed and pure choices are independent, proving the factorization.

**Least nonzero weights.** Each vertex of \(H\) has a neighbor, hence a single selected vertex cannot satisfy all parity equations. If \(m=2<n\), selecting both mixed tokens involving any fixed member of \(B\) gives a weight-two codeword. There are exactly \(n\) such words: a two-one matrix satisfying constant row and column parities must have its two ones in one column. For \(m=n=2\), all six two-one patterns on the mixed \(2\times2\) matrix satisfy the parity equations; additionally, the two pure vertices form one weight-two codeword, giving seven.

For \(m,n\ge3\), no mixed matrix of weight one or two can have all row parities equal and all column parities equal: at weight two all row parities must be zero (because at least one of the three or more rows is empty), so both ones must occupy one row in distinct columns; then the column parities are not all equal. The pure weight-two case is also impossible. Indeed, a nonempty even-degree simple edge set contains a cycle, of length at least three; an odd-degree pair of complete-graph edge sets, if permitted, has at least \((m+n)/2\ge4\) edges. A triangle in either pure block supplies weight three. The number of such triangles is \(\binom m3+\binom n3\). A weight-three mixed matrix can satisfy the parity conditions only when both part sizes are three, in which case it is one of the six permutation matrices. This gives the asserted coefficient.

## Verification
The standalone `verify.py` constructs the original two-token graph directly from symmetric-difference adjacency and performs independent binary Gaussian elimination and complete kernel enumeration for \((m,n)=(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\). It independently implements the closed-form polynomial sums, compares every coefficient and the computed rank, and checks total kernel cardinalities for all \(2\le m\le n\le10\). All checks return `VERIFY_OK`. Enumerations are finite consistency checks, not the proof for unrestricted parameters.

## Relationship to prior work
The October 2026 two-token biclique studies by Chinman and collaborators, and by Acosta Troncoso and collaborators, determine **ordinary domination numbers** and describe token adjacency, rather than the binary open-neighborhood parity-kernel weight enumerator. Klostermeyer's October 2026 nullspace-matrix paper studies **closed-neighborhood** parity in rectangular grid graphs using Fibonacci-polynomial recurrences; neither that graph nor that parity operator is the present one. Standard binary-code character orthogonality is used explicitly as a proof method, not claimed as novel. The present content is the biclique two-token family-specific rank defect, complete weight distribution, and sharp minimum supports.

## Limitations
The formula covers only two-token graphs of complete bipartite graphs with both part sizes at least two and uses the zero-diagonal adjacency operator over \(\mathbb F_2\). It does not determine the analogous closed-neighborhood kernel or higher-token parity codes. No assertion of independent certification or absolute historical priority is made. Some relevant older token-graph literature may use a different language for equivalent binary codes.

## References
1. N. Chinman, A. Cortijo, B. Pedroni, I. Seong, L. Stenger, *The domination number of the \(k\)-token graph of the complete bipartite graph \(K_{m,n}\)*, arXiv:2610.28936, first posted 2026-10-20, https://arxiv.org/abs/2610.28936.
2. E. Acosta Troncoso, I. Caldera Caldera, L. M. Rivera, *The domination number of the 2-token graph of the complete bipartite graph*, arXiv:2610.31557, first posted 2026-10-22, https://arxiv.org/html/2610.31557v1.
3. W. F. Klostermeyer, *Prime Nullspace Matrices and Even Dominating Sets*, arXiv:2610.31475, first posted 2026-10-22, https://arxiv.org/abs/2610.31475.
