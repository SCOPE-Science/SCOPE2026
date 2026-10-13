# Idempotent enumeration in strict Margolis–Rhodes path semigroups
## Finding
Let \(P_n\) be the path on \(n\ge 1\) vertices, and let \(St(P_n)\) be the strict Margolis–Rhodes semigroup of Margolis and Rhodes: every nonempty vertex fiber is an edge. Let \(e_{n,k}\) be the number of rank-\(k\) idempotents in \(St(P_n)\). For the generating functions below, put \(P_0=\varnothing\) and \(e_{0,0}=1\).

For every \(0\le k\le\lfloor n/2\rfloor\),
\[
e_{n,k}=\sum_{j=0}^{\lfloor k/2\rfloor}(-1)^j2^{k-2j}
\frac{(n-k-j)!}{(n-2k)!(k-2j)!j!}.
\]
Equivalently, the complete rank-refined enumerator is
\[
\sum_{n\ge0}\sum_{k\ge0}e_{n,k}x^ny^k
=\frac{1}{1-x-2yx^2+y^2x^4}.
\]

Consequently, if
\[
a_n=|E(St(P_n))|=\sum_k e_{n,k},
\]
then
\[
a_0=1,\qquad a_1=1,\qquad a_2=3,\qquad a_3=5,
\]
and for every \(n\ge4\),
\[
a_n=a_{n-1}+2a_{n-2}-a_{n-4}.
\]
Hence
\[
\sum_{n\ge0}a_nx^n=\frac{1}{1-x-2x^2+x^4}.
\]
The first values for \(n=1,2,\ldots\) are
\[
1,3,5,10,19,36,69,131,250,476,907,1728,\ldots.
\]

More generally, for any finite simple graph \(\Gamma\), an element of \(St(\Gamma)\) is idempotent exactly when every matching edge in its domain is collapsed to one of its own endpoints and the set of selected endpoints is independent.

## Assumptions and scope
The semigroup \(St(\Gamma)\) is the one in Definition 3.2 of Margolis–Rhodes, arXiv:2609.39370: each vertex fiber is an edge or empty. Lemma 3.3 of that paper identifies its elements with a matching in the domain, an independent image set of the same cardinality, and a bijection assigning one image vertex to each matching edge.

The result counts idempotents of this strict semigroup, not idempotents of the full monoid \(MR(P_n)\). The convention \(P_0=\varnothing\) is introduced only to make the generating function and recurrence uniform.

## Proof
Take \(f\in St(\Gamma)\). By Lemma 3.3, write its domain matching as
\[
M_f=\{e_1,\ldots,e_k\}
\]
and its independent image as
\[
I_f=\{v_1,\ldots,v_k\},
\]
where both endpoints of \(e_i\) map to \(v_i\).

Suppose first that \(f^2=f\). Equality of partial maps forces every image point \(v_i\) to lie in \(\operatorname{Dom}(f)\) and to satisfy \(v_if=v_i\). Since the domain is the disjoint union of the matching edges, \(v_i\) lies in a unique edge \(e_j\). But then \(v_if=v_j\). The vertices \(v_1,\ldots,v_k\) are distinct, so \(v_j=v_i\) implies \(j=i\). Thus \(v_i\in e_i\) for every \(i\).

Conversely, if every assigned image vertex satisfies \(v_i\in e_i\), then the whole edge \(e_i\) maps to \(v_i\), so in particular \(v_if=v_i\). Every point of the image is fixed, and therefore \(f^2=f\). This proves the graph-theoretic characterization: idempotents are precisely matchings equipped with one selected endpoint per edge, subject to independence of the selected endpoints.

Now specialize to \(P_n\). Read the vertices from left to right. Encode an unused vertex by a monomer \(M\), and encode a matched edge by a domino carrying label \(L\) or \(R\) according to whether its left or right endpoint is selected. Matching ensures that these monomers and dominoes tile the path. Independence of the selected endpoints has exactly one local obstruction: an \(R\)-domino cannot be immediately followed by an \(L\)-domino. Indeed, in that configuration the two selected endpoints are consecutive vertices; every other pair of selected endpoints from distinct matching edges is separated by at least one vertex.

Let
\[
I_n(y)=\sum_k e_{n,k}y^k.
\]
Appending a monomer to a tiling of length \(n-1\) gives \(I_{n-1}(y)\). Appending an \(R\)-domino to a tiling of length \(n-2\) gives \(yI_{n-2}(y)\). Appending an \(L\)-domino gives the same contribution except when the preceding tile is an \(R\)-domino. Tilings of length \(n-2\) ending in an \(R\)-domino have weight \(yI_{n-4}(y)\). Hence, for \(n\ge4\),
\[
I_n(y)=I_{n-1}(y)+2yI_{n-2}(y)-y^2I_{n-4}(y).
\]
The initial polynomials are
\[
I_0(y)=1,\quad I_1(y)=1,\quad I_2(y)=1+2y,\quad I_3(y)=1+4y.
\]
Therefore
\[
\sum_{n\ge0}I_n(y)x^n=\frac{1}{1-x-2yx^2+y^2x^4}.
\]

For the coefficient formula, expand
\[
\frac{1}{1-(x+2yx^2-y^2x^4)}
=\sum_{q\ge0}(x+2yx^2-y^2x^4)^q.
\]
To obtain \(x^ny^k\), choose \(j\) copies of \(-y^2x^4\), \(k-2j\) copies of \(2yx^2\), and \(n-2k\) copies of \(x\). The total number of chosen factors is \(q=n-k-j\). The multinomial coefficient gives
\[
(-1)^j2^{k-2j}
\frac{(n-k-j)!}{(n-2k)!(k-2j)!j!},
\]
and summing over \(0\le j\le\lfloor k/2\rfloor\) proves the stated formula. Setting \(y=1\) gives the total recurrence and ordinary generating function.

## Verification
The included `check_idempotents.py` performs two independent finite checks. First, for \(1\le n\le6\), it exhaustively enumerates all partial maps on \(P_n\), tests the defining strict-continuity conditions directly on vertex and edge preimages, and then tests \(f^2=f\). It recovers the rank distributions
\[
(1),\ (1,2),\ (1,4),\ (1,6,3),\ (1,8,10),\ (1,10,21,4).
\]
Second, it evaluates the closed coefficient formula and the polynomial recurrence through \(n=14\) and checks exact agreement. The program terminates with `CHECK_OK`.

The finite computation is a cross-check only. The characterization, generating function, recurrence, and coefficient formula are proved symbolically above for all \(n\).

## Relationship to prior work
Margolis and Rhodes define \(St(\Gamma)\), characterize its elements by matchings and independent sets, prove regularity for paths, compute the full order
\[
|St(P_n)|=\sum_{k=0}^{\lfloor n/2\rfloor}\binom{n-k}{k}\binom{n-k+1}{k}k!,
\]
and use explicit idempotents in their complexity arguments. Their proof of Theorem 7.2 also observes the endpoint-collapse form of an idempotent inside a regular class. The inspected paper does not give a count or generating function for all idempotents of \(St(P_n)\), nor the rank-refined distribution above.

The earlier Margolis–Rhodes paper on degree-two transformation semigroups already develops strict continuous maps and the matching/anti-clique description of singular maps. Its strict monoid is broader in the connected case because it also includes automorphisms. It does not give the path idempotent enumeration established here.

Targeted mathematical-record searches for strict-continuous path idempotents, the exact recurrence, and the rank-refined generating function returned no covering result. A web search for the initial integer sequence surfaced an unrelated OEIS sequence that agrees only initially and already differs at the ninth path value, so it does not supply the stated enumeration.

## Limitations
The explicit rational generating function and coefficient formula are proved for paths. The general graph statement is only the structural idempotent characterization; no comparable closed enumeration is claimed for arbitrary graphs or cycles.

The result concerns the strict semigroup \(St(\Gamma)\), not all idempotents in \(MR(\Gamma)\). The literature comparison was targeted rather than exhaustive, so an uncrawled combinatorics source could conceivably contain an equivalent oriented-matching enumeration without using Margolis–Rhodes terminology.

## References
1. S. Margolis and J. Rhodes, “The Margolis-Rhodes Monoid of a Graph,” arXiv:2609.39370v1, first submitted 2026-09-30; revised as v2 on 2026-10-01. See Definition 3.2, Lemma 3.3, Theorems 7.1–7.3, Section 8, and Sections 11–12.
2. S. Margolis and J. Rhodes, “Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Foundations and Structure,” arXiv:2005.02606, 2020. See the strict-continuity discussion, Lemma 2.5, Corollary 2.10, and Lemma 3.11.
