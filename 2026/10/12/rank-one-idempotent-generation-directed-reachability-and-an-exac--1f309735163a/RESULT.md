# Rank-one idempotent generation: directed reachability and an exact three-dimensional count

## Finding
Let \(k=\mathbb F_q\) be any finite field. Let \(\mathcal P_{n,q}\) be the set of rank-one idempotent matrices in \(M_n(k)\). For every \(n\ge2\), a tuple \(P_1,\ldots,P_n\in\mathcal P_{n,q}\) generates \(M_n(k)\) as a *unital* \(k\)-algebra exactly when both of its rank-one factor matrices are invertible and the normalized factor-overlap matrix has a strongly connected nonzero-entry digraph. In particular the minimum number \(d_1(n,q)\) of rank-one idempotent generators is
\[
d_1(n,q)=\begin{cases}n,&n\ge3,\\2,&n=2,\ q>2,\\3,&n=q=2.\end{cases}
\]
In dimension three, the number of ordered generating triples is precisely
\[
G_3(q)=\frac{|\operatorname{GL}_3(\mathbb F_q)|}{(q-1)^3}(q-1)^2\bigl(q^4+q^3-6q^2+2q+5\bigr)
=\frac{(q^3-1)(q^3-q)(q^3-q^2)}{q-1}\bigl(q^4+q^3-6q^2+2q+5\bigr).
\]
The normalized count is \(S_3(q)=(q-1)^2(q^4+q^3-6q^2+2q+5)\), with \(S_3(2)=9\), \(S_3(3)=260\), \(S_3(4)=2133\). Hence \(G_3(2)=1512\).

## Assumptions and scope
Fix a finite field \(k\), an integer \(n\ge2\), and ordered rank-one idempotents \(P_i=u_iv_i^{\mathsf T}\) with \(v_i^{\mathsf T}u_i=1\). Define \(U\) to have columns \(u_i\), \(V\) to have rows \(v_i^{\mathsf T}\), and the overlap matrix \(C=VU\) with \(C_{ii}=1\). The support digraph has vertices \(1,\dots,n\) and edge \(i\to j\) exactly when \(C_{ij}\ne0\). A vertex reaches itself through its empty path; directed loops are allowed. Generation is by \(k\)-linear combinations of all words in the \(P_i\) together with the identity. Only the first \(n\) projectors are used in the graph criterion; no claim is made that an analogous square matrix criterion applies verbatim to larger tuples.

## Proof
**1. Factor ranks are necessary.** Let \(W=\operatorname{span}\{u_i\}\). Every positive word has image contained in \(W\); their linear span has dimension at most \(n\dim W\). Adjoining the identity raises this by at most one. If \(\dim W<n\), the dimension is at most \(1+n(n-1)<n^2\), so the generated algebra is proper. Applying the dual argument to \(\operatorname{span}\{v_i^{\mathsf T}\}\) forces \(V\) invertible. Thus \(U,V\) must be invertible.

**2. Directed reachability is exact.** Suppose \(U,V\) invertible and conjugate by \(U\). We have \(U^{-1}P_iU=e_ic_i^{\mathsf T}\), where \(c_i^{\mathsf T}\) is row \(i\) of the invertible \(C=VU\), and \(C_{ii}=1\). For a word with successive letters \(i_0,\ldots,i_s\), multiplication gives
\[
(e_{i_0}c_{i_0}^{\mathsf T})\cdots(e_{i_s}c_{i_s}^{\mathsf T})=\bigl(\prod_{t=0}^{s-1}C_{i_ti_{t+1}}\bigr)e_{i_0}c_{i_s}^{\mathsf T}.
\]
Every nonzero word therefore corresponds to a directed walk, and each reachable ordered pair contributes the basis matrix \(e_ic_j^{\mathsf T}\). These \(n^2\) matrices form a basis of \(M_n(k)\). Furthermore, the *identity is in the span of the reachable pairs*: because \(C\) is invertible, \(C^{-1}\) is a polynomial in \(C\), hence also in \(N=C-I\); off-diagonal entries of powers of \(N\) vanish between vertices not joined by any directed path. Consequently \((C^{-1})_{ij}=0\) for any unreachable ordered pair, and
\[
I=\sum_{i,j}(C^{-1})_{ij}e_ic_j^{\mathsf T}
\]
is already in that reachable-pair span. Thus the generated unital algebra has dimension exactly the number of reachable ordered pairs and equals \(M_n(k)\) if and only if the digraph is strongly connected.

**3. The minimum number.** For any fewer than \(n\) rank-one projectors, the same image-space argument proves that the unital span is proper. For dimension two, strong connectivity of \(C=\left(\begin{smallmatrix}1&a\\b&1\end{smallmatrix}\right)\) requires \(a,b\ne0\), while invertibility requires \(ab\ne1\). Such \(a,b\) exist precisely for \(q>2\). Over \(\mathbb F_2\), three projectors \(E_{11},E_{11}+E_{12},E_{11}+E_{21}\) generate \(M_2\): subtracting the first from the other two yields \(E_{12},E_{21}\), and multiplying yields \(E_{11},E_{22}\).

For \(n=3\), the diagonal-one matrix \(C_3=\left(\begin{smallmatrix}1&0&1\\0&1&1\\1&1&1\end{smallmatrix}\right)\) has determinant \(-1\) and strongly connected support over *every* field. Inductively, assume an invertible diagonal-one strongly connected \(C_n\) exists for \(n\ge3\). Since its inverse cannot be the all-ones matrix, choose \(i,j\) with \((C_n^{-1})_{ji}\ne1\). Then
\[
C_{n+1}=\begin{pmatrix}C_n&e_i\\e_j^{\mathsf T}&1\end{pmatrix}
\]
has determinant \(\det(C_n)(1-(C_n^{-1})_{ji})\ne0\) and strongly connected support. Taking \(U=I\), \(V=C_n\) completes the construction.

**4. Exact dimension-three counting.** Normalize \(U=I\) and write \(C\in M_3(k)\) with all three diagonal entries equal to one. First count those which are invertible. Let \(I_j(q)\) be the number of invertible diagonal-one \(j\times j\) matrices. For \(j=1,2\), direct computation gives \(I_1=1\) and \(I_2=q^2-q+1\). Möbius inversion in the lattice of subspaces of \(k^3\) gives
\[
I_3=q^6-(q^2+q-2)q^3+q(q-1)^2=q^6-q^5-q^4+3q^3-2q^2+q.
\]
Indeed a \(d\)-subspace \(W\) is contained in the right kernel of a diagonal-one matrix only if it contains none of the coordinate axes. For each such \(W\), exactly \(q^{3(2-d)}\) matrices kill \(W\). The eligible lines number \(q^2+q-2\), the eligible planes \((q-1)^2\), and their subspace Möbius coefficients are respectively \(-1\) and \(q\).

A support digraph on three vertices is not strongly connected precisely when some nonempty proper subset \(S\subset\{1,2,3\}\) has no outgoing edge. There are six such cuts. Apply inclusion-exclusion to these cut events inside the invertible diagonal-one matrices. For a nonempty family \(\mathcal F\) of cuts, assign to vertex \(i\) its membership vector \((\mathbf1_{i\in S})_{S\in\mathcal F}\). The permitted off-diagonal entry \(C_{ij}\) is free exactly when the membership vector of \(i\) is componentwise at most that of \(j\). Group identical vectors into diagonal blocks of sizes \(d_B\), and let \(a(\mathcal F)\) be the number of permitted entries between distinct blocks. Ordering these blocks by the membership partial order makes every permitted matrix block triangular; its number of invertible diagonal-one choices is therefore
\[
q^{a(\mathcal F)}\prod_B I_{d_B}(q).
\]
Every nonempty family produces blocks of size at most two. Exhausting the \(2^6-1=63\) cut families is the finite, symbolic inclusion-exclusion calculation independently encoded in `verify.py`. Its signed contributions grouped by family size are
\[
\begin{array}{c|l}
|\mathcal F|&\text{signed polynomial}\,\\\hline
1&6q^4-6q^3+6q^2\\
2&-6q^3-9q^2+3q-3\\
3&6q^2+12q+2\\
4&-6q-9\\
5&6\\
6&-1
\end{array}
\]
Their sum is \(6q^4-12q^3+3q^2+9q-5\). Subtracting from \(I_3(q)\) yields
\[
S_3(q)=q^6-q^5-7q^4+15q^3-5q^2-8q+5=(q-1)^2(q^4+q^3-6q^2+2q+5).
\]
Finally, each ordered generating triple corresponds to exactly \((q-1)^3\) decompositions \(P_i=u_iv_i^{\mathsf T}\): each rank-one projector permits \(q-1\) nonzero rescalings \(u_i\mapsto\lambda_i u_i,\ v_i\mapsto\lambda_i^{-1}v_i\). Writing \(V=CU^{-1}\), there are \(|\operatorname{GL}_3(k)|\) choices for \(U\) and \(S_3(q)\) for \(C\), yielding the stated formula.

## Verification
Run `python3 verify.py` using only Python standard library. The checker reconstructs the 63-cut inclusion-exclusion polynomial over the integer polynomial ring, checks each of the six signed family-size contributions, and compares the exact formula with independent complete enumeration of normalized matrices over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\). It also checks the two-dimensional invertible-support criterion over four fields and explicitly constructs the word-generated matrix algebra for all \(64\) normalized binary three-by-three matrices. A separate direct census of all \(28^3=21952\) ordered rank-one projector triples over \(\mathbb F_2\) finds exactly \(1512\) generating triples. Replay ends with `VERIFY_OK`. Finite enumerations do not prove the all-field assertion: the Möbius and inclusion-exclusion arguments do.

## Relationship to prior work
Petrenko and Sidki study generation of matrix rings by arbitrary matrix pairs and their asymptotic density, without a rank-one idempotent constraint [1]. Kravchenko, Mazur, and Petrenko give an exact generation law for tuples chosen from *all* matrices in \(M_2\) and \(M_3\) over finite fields, by maximal-subalgebra inclusion-exclusion [2]; their unrestricted count does not determine the count conditional on all generators having rank one and being idempotent. Krupnik's earlier title concerns minimal idempotent generators without specifying rank-one restrictions; full text was unavailable for decisive comparison [3]. The result here concerns the rank-one restriction, a directed-reachability characterization, and a new exact dimension-three constrained enumeration. The general linear-algebraic and inclusion-exclusion techniques are not asserted to be new.

## Limitations
The graph criterion assumes the *number of generators equals the matrix dimension*; the minimum-generator claim addresses existence and sharpness, not a classification of all longer tuples. The explicit enumeration is for exactly three rank-one idempotents in dimension three, not all tuple lengths or arbitrary dimensions. Scholarly priority remains uncertain because full text of a plausible older idempotent-generator paper was not obtained; absence of a search hit alone does not prove novelty.

## References
1. B. V. Petrenko and S. N. Sidki, *On pairs of matrices generating matrix rings and their presentations*, arXiv:math/0512186 (first public version 9 December 2005); *J. Algebra* 310 (2007), 15–40. https://arxiv.org/abs/math/0512186
2. R. V. Kravchenko, M. Mazur, and B. V. Petrenko, *On the smallest number of generators and the probability of generating an algebra*, arXiv:1001.2873 (2010). https://arxiv.org/abs/1001.2873
3. N. Ya. Krupnik, *Minimal number of idempotent generators of matrix algebras over arbitrary field*, *Communications in Algebra* 20 (1992), 3251–3257, DOI:10.1080/00927879208824513 (bibliographic metadata only; full article not inspected).
