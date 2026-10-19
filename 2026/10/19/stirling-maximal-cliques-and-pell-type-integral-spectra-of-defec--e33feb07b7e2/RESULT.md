# Stirling-maximal cliques and Pell-type integral spectra of defect-one transformation idempotents

## Finding

Let \(X\) be a labeled set of cardinality \(n\ge2\). In the full transformation monoid \(\mathcal T(X)\), consider the induced commuting graph \(\Gamma_n\) on the idempotents of rank \(n-1\). For distinct vertices, adjacency means equality of the two compositions.

Every vertex is uniquely an elementary collapse \(e_{a\to b}\), where \(a,b\in X\), \(a\ne b\), and \(e_{a\to b}\) sends \(a\) to \(b\) while fixing all other points. Two distinct vertices commute precisely when their tails are different and neither head is the other's tail. More strongly, every nonempty clique is uniquely a function \(f:T\to X\setminus T\) on a nonempty proper set \(T\subset X\), with vertex set \(\{e_{a\to f(a)}:a\in T\}\).

**Maximal-clique classification.** Such a clique is inclusion-maximal if and only if \(f\) is surjective. Thus the possible sizes of inclusion-maximal cliques are exactly \(\lceil n/2\rceil,\ldots,n-1\), and the number of maximal cliques of size \(r\) is
\[
M_{n,r}=\binom nr (n-r)!\,\left\{\begin{matrix}r\\n-r\end{matrix}\right\},
\]
where the bracket denotes the Stirling number of the second kind. In particular, there are exactly \(n\) maximum cliques of size \(n-1\); the clique complex is nonpure for every \(n\ge4\).

**Complete adjacency spectrum.** For \(n\ge3\), with \(A_n\) the ordinary \(n(n-1)\)-by-\(n(n-1)\) adjacency matrix, its characteristic polynomial is
\[
\boxed{\det(\lambda I-A_n)=\bigl(\lambda-(n-2)^2\bigr)
\bigl(\lambda^2+(n-3)\lambda-(n-2)^2\bigr)^{n-1}
(\lambda-1)^{n(n-3)/2}(\lambda+1)^{(n-1)(n-2)/2}.}
\]
For \(n=2\), the graph has two isolated vertices and characteristic polynomial \(\lambda^2\). For \(n=3\), it consists of three disjoint edges. For \(n\ge4\), it is connected, regular of degree \((n-2)^2\), and has five distinct adjacency eigenvalues.

The graph is integral (all eigenvalues integers) exactly when \(5n^2-22n+25\) is a perfect square. An infinite family of such orders is
\[
n_j=\frac{L_{4j+3}+11}{5}\qquad(j\ge0),
\]
where \(L_m\) is the Lucas sequence \(L_0=2\), \(L_1=1\), \(L_{m+2}=L_{m+1}+L_m\). The first displayed orders are \(3,8,42,275\). This follows from the Lucas–Fibonacci identity \(L_m^2-5F_m^2=4(-1)^m\).

For context, the entire (not necessarily maximal) clique polynomial is
\[
P_n(z)=1+\sum_{r=1}^{n-1}\binom nr(n-r)^r z^r.
\]
This last coefficient formula is the classical count of idempotent transformations by the number of nonfixed points, under the unique commuting elementary-collapse factorization. **Its numerical enumeration is not claimed as new.** The assessed contribution is the full maximal-clique structure and the complete graph spectrum, including the integral-spectrum phenomenon.

## Assumptions and scope

No field, characteristic, asymptotic assumption, or choice of multiplication convention is needed. The monoid consists of *all* maps \(X\to X\). The graph is induced only on the rank-\(n-1\) idempotents, not on all noncentral elements of \(\mathcal T(X)\). Commutation is symmetric and independent of whether transformations are written as acting on the left or the right. All cliques are unordered sets of distinct vertices. A maximal clique means inclusion-maximal, not necessarily of largest size. The Stirling convention is that the number of onto maps from an \(r\)-point set to an \(s\)-point set is \(s!\left\{\begin{matrix}r\\s\end{matrix}\right\}\).

## Proof

**1. Elementary composition.** Every idempotent with image of size \(n-1\) fixes its image pointwise, and there is a unique excluded point \(a\); its image under the idempotent is some \(b\ne a\). Therefore it is \(e_{a\to b}\). If \(e_{a\to b}\ne e_{c\to d}\) and \(a=c\), the two composites disagree at the common tail. For \(a\ne c\), if \(b=c\) the composites disagree at \(a\); if \(d=a\) they disagree at \(c\). Conversely, when \(a\ne c\), \(b\ne c\), and \(d\ne a\), the maps commute: each changes only its own tail, and both heads are fixed by the other map. This establishes the adjacency rule.

**2. Cliques and maximality.** Pairwise commutation forces different tails. Moreover, no head may equal any selected tail: a head cannot equal its own tail, and the adjacency rule excludes another selected tail. Hence a clique determines its tail set \(T\) and a map \(f:T\to X\setminus T\), and conversely every such map gives a clique. To add an elementary collapse with a new tail \(c\), that tail must be outside \(T\cup f(T)\), and a suitable head must lie outside \(T\cup\{c\}\). Since \(f(T)\ne\varnothing\), at least one such head exists whenever there is an available tail. Thus the clique is maximal exactly when \(X\setminus(T\cup f(T))=\varnothing\), i.e. when \(f\) is onto \(X\setminus T\). If \(|T|=r\), surjectivity is possible precisely for \(r\ge n-r\), with \(r\le n-1\). There are \(\binom nr\) choices of \(T\) and \((n-r)!\left\{\begin{matrix}r\\n-r\end{matrix}\right\}\) surjections. At \(r=n-1\), the sole head is the missing point, giving exactly \(n\) largest cliques. For \(n\ge4\), sizes \(n-2\) and \(n-1\) are both realized, so the clique complex is nonpure. (When \(n=4\), these are sizes two and three.) The general clique coefficient follows by counting all maps \(T\to X\setminus T\), or by the standard idempotent count.

**3. Adjacency operator.** Work over \(\mathbb Q\), and regard a function on graph vertices as an array \(h(a,b)\) for \(a\ne b\). Define its row sums \(R_a=\sum_{b\ne a}h(a,b)\), column sums \(C_a=\sum_{b\ne a}h(b,a)\), and grand total \(S=\sum_aR_a\). The adjacency rule gives the exact identity
\[
(A_nh)(a,b)=\sum_{c\notin\{a,b\}}\sum_{d\notin\{a,c\}}h(c,d)
=S-R_a-R_b-C_a+h(b,a).
\]
When \(n\ge3\), the vector space decomposes as the direct sum of (i) the constants, (ii) the arrays \(h(a,b)=u_a+v_b\) with \(\sum_a u_a=\sum_a v_a=0\), and (iii) the arrays satisfying \(R_a=C_a=0\) for all \(a\). To verify that this is a direct decomposition, observe that the first two spaces together have dimension \(2n-1\), that the row/column-sum map has rank \(2n-1\), and that an array of the additive form in the kernel must vanish: for zero-sum \(u,v\), the equations are \((n-1)u_a-v_a=0\), \(-u_a+(n-1)v_a=0\), whose determinant is \(n(n-2)\ne0\). The remaining dimension is \(n^2-3n+1\).

On the constant subspace, \(A_n\) acts by the degree \((n-2)^2\). On the \(2(n-1)\)-dimensional additive zero-sum subspace, the displayed identity sends the pair \((u,v)\) to
\[
\begin{pmatrix}u'\\v'\end{pmatrix}
=\begin{pmatrix}-(n-2)&-(n-3)\\-(n-2)&1\end{pmatrix}
\begin{pmatrix}u\\v\end{pmatrix},
\]
acting identically on each independent coordinate of the standard \((n-1)\)-dimensional zero-sum representation. The characteristic polynomial of this two-by-two matrix is \(\lambda^2+(n-3)\lambda-(n-2)^2\).

For the row-and-column-zero subspace, \(A_nh(a,b)=h(b,a)\). Its symmetric part has dimension \(\binom n2-n=n(n-3)/2\), because the unsigned vertex-edge incidence matrix of the complete graph has rank \(n\) over \(\mathbb Q\) for \(n\ge3\). Its antisymmetric part has dimension \(\binom n2-(n-1)=(n-1)(n-2)/2\), because an oriented incidence matrix has rank \(n-1\). Transposition acts as \(+1\) and \(-1\), respectively. Multiplying the factors from these invariant direct summands proves the asserted full characteristic polynomial.

For \(n\ge4\), the degree eigenvalue occurs only once: the two quadratic roots are distinct from the degree and from \(\pm1\). In a regular undirected graph, the degree's multiplicity equals the number of connected components, hence \(\Gamma_n\) is connected. The five eigenvalues are distinct. For \(n=3\), direct inspection gives three edges; for \(n=2\), there are no edges.

**4. Integral-spectrum family.** The two possibly irrational eigenvalues are the roots of the quadratic. Their discriminant is \(D_n=5n^2-22n+25\). The graph is integral if and only if \(D_n\) is a square: when it is a square, the square root has the parity of \(n-3\), since \(D_n\equiv(n-3)^2\pmod4\), so both roots are integers. For \(m=4j+3\), the Lucas recurrence implies \(L_m\equiv4\pmod5\), so \(n_j=(L_m+11)/5\) is an integer at least three and \(5n_j-11=L_m\). Now
\[
5D_{n_j}=(5n_j-11)^2+4= L_m^2+4=5F_m^2,
\]
using \(L_m^2-5F_m^2=-4\). Thus \(D_{n_j}=F_m^2\), proving an infinite integral subfamily.

## Verification

Run the standalone program `verify.py` with Python 3. It builds the rank-defect-one transformations literally and checks commutation by both composition orders, not by assuming the adjacency criterion. It enumerates every graph clique and tests maximality directly for \(2\le n\le7\), comparing size distributions with the formulas. It independently computes integer adjacency characteristic polynomials by matrix traces and Newton identities for \(2\le n\le6\). All checks passed, ending with `VERIFY_OK_DEFECT_ONE_COMMUTING_SPECTRUM`.

Selected exhaustive maximal-clique counts, indexed by clique size, are \(\{2:12,3:4\}\) for \(n=4\), \(\{3:60,4:5\}\) for \(n=5\), \(\{3:120,4:210,5:6\}\) for \(n=6\), and \(\{4:1260,5:630,6:7\}\) for \(n=7\). These are finite corroborations, not the proof of the uniform formulas.

## Relationship to prior work

Araújo, Kinyon, and Konieczny (2010) established general theory of commuting graphs of finite semigroups and a centralizer criterion for idempotent transformations, with their emphasis on diameters and minimal paths. Their Section 6 also explicitly asks for clique/chromatic information on transformation commuting graphs. Cameron, Castillo-Ramírez, Gadouleau, and Mitchell (2016) studied the same elementary collapses as generating transformations, including a source-to-sink bipartition criterion for when an arc-generated semigroup is a band (Theorem 2.12). The standard enumeration of idempotent transformations by fixed-image size and the corresponding clique coefficient formula are not novelty claims here. The new assessed assertion is the exact maximal-clique surjection classification alongside the complete adjacency spectrum and its Pell-type integral subfamily, for the *induced rank-defect-one idempotent commuting graph*, not the full commuting graph.

## Limitations

The result does not describe adjacency spectra of the whole transformation commuting graph, nor of arbitrary rank classes. It does not classify all integral-spectrum orders beyond the exact discriminant-square criterion, and does not determine clique-complex homology or graph automorphism groups. The proof applies to every finite cardinal \(n\), while the executable checker covers bounded values only. An equivalent graph-theoretic description or spectrum in literature under another graph name remains possible; no claim of absolute publication priority or independent validation is made.

## References

1. J. Araújo, M. Kinyon, J. Konieczny, *Minimal Paths in the Commuting Graphs of Semigroups*, arXiv:1003.2809, initial version 2010-03-14; see Section 2 (in particular Lemma 2.2) and Section 6. https://arxiv.org/abs/1003.2809
2. P. J. Cameron, A. Castillo-Ramírez, M. Gadouleau, J. D. Mitchell, *Lengths of words in transformation semigroups generated by digraphs*, arXiv:1602.00935, initial version 2016-02-02; Journal of Algebraic Combinatorics 45 (2017), 149–170, especially Theorem 2.12. https://arxiv.org/abs/1602.00935
3. G. Ayik, H. Ayik, Y. Ünlü, J. M. Howie, *Rank Properties of the Semigroup of Singular Transformations on a Finite Set*, Communications in Algebra 36 (2008), 2581–2587, DOI:10.1080/00927870802067658 (abstract/bibliographic comparison; complete text not inspected).
