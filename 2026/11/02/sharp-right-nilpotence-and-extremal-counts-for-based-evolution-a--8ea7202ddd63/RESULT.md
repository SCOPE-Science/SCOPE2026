# Sharp right-nilpotence and extremal counts for based evolution algebras over finite chain rings

## Finding
Let \(R\) be a finite commutative chain ring with maximal ideal \(\mathfrak m=(\pi)\), residue field \(R/\mathfrak m\cong\mathbb F_q\), and nilpotency length \(s\ge1\), so \(\pi^s=0\) and \(\pi^{s-1}\ne0\). For \(n\ge1\), choose a labeled natural basis \(e_1,\ldots,e_n\) of a free \(R\)-module. Every matrix \(C=(c_{ij})\in M_n(R)\) defines an evolution algebra \(E_C\) by \(e_i e_j=0\) for distinct indices and \(e_i^2=\sum_j c_{ij}e_j\). Define its right powers by \(E^{\langle1\rangle}=E\) and \(E^{\langle r+1\rangle}=E^{\langle r\rangle}E\), and define \(\nu(C)\) as the least \(r\) with \(E^{\langle r\rangle}=0\), when such an \(r\) exists.

Let \(G_C\) have vertices \(1,\ldots,n\), with directed edge \(i\to j\) exactly when \(c_{ij}\) is a unit, equivalently when its residue is nonzero. Then:

1. \(E_C\) is elementwise nil if and only if \(G_C\) is acyclic. In this case \(E_C\) is right nilpotent and \(\nu(C)\le ns+1\).
2. If \(s=1\), equality \(\nu(C)=n+1\) holds exactly when \(G_C\) admits a directed Hamiltonian path.
3. If \(s\ge2\), equality \(\nu(C)=ns+1\) holds exactly when \(G_C\) admits a directed Hamiltonian path \(\sigma_1\to\cdots\to\sigma_n\) and \(c_{\sigma_n,\sigma_1}\in\mathfrak m\setminus\mathfrak m^2\). This includes the one-vertex boundary, where the specified return entry is diagonal.

Put \(D_0(q)=1\) and, for \(n\ge1\),
\[
D_n(q)=\sum_{k=1}^{n}(-1)^{k+1}\binom nk q^{k(n-k)}D_{n-k}(q).
\]
The exact number of nil **based multiplication tables** is
\[
\boxed{N_{n,s}(q)=q^{(s-1)n^2}D_n(q)}.
\]
The exact number of tables attaining the maximal right nilindex is
\[
\boxed{H_{n,s}(q)=
\begin{cases}
n!(q-1)^{n-1}q^{\binom{n-1}{2}},&s=1,\\
n!(q-1)^n q^{(s-1)n^2+\binom{n-1}{2}-1},&s\ge2.
\end{cases}}
\]
These expressions depend only on the residue cardinality and chain length, not on the isomorphism type of \(R\). In particular the supremum \(ns+1\) is attained for every \(n,s,q\).

## Assumptions and scope
The ring is finite, commutative, local and a principal ideal chain ring; thus \(\lvert R\rvert=q^s\), \(\lvert\mathfrak m\rvert=q^{s-1}\), and for \(0\le t\le s-1\) the elements of exact \(\pi\)-valuation \(t\) number \((q-1)q^{s-t-1}\). We count matrices relative to one fixed labeled natural basis. Different matrices can give isomorphic algebras; no quotient by natural-basis changes or general algebra isomorphisms is taken. Elementwise nil means each element's left-associated principal powers eventually vanish. Right nilindex is distinct from ordinary nilindex where all parenthesizations are allowed.

## Proof
**(1) Path criterion.** Every \(E_C^{\langle r\rangle}\) is generated over \(R\) by left-associated products of \(r\) basis elements. Such a product can be nonzero only if its first two factors agree, after which each successive basis factor selects a coordinate. Explicitly,
\[
(((e_{i_0}^2 e_{i_1})e_{i_2})\cdots e_{i_{r-2}})
=\left(\prod_{j=0}^{r-3}c_{i_j i_{j+1}}\right)e_{i_{r-2}}^2
\qquad(r\ge2),
\]
where for \(r=2\) the right side is \(e_{i_0}^2\). This is nonzero exactly when at least one last coordinate \(c_{i_{r-2}i_{r-1}}\) gives a nonzero path coefficient. Thus \(E_C^{\langle r\rangle}\ne0\) if and only if some directed index walk of length \(r-1\) has nonzero product of its consecutive structure coefficients, including possible zero-residue edges. This is the finite-rank specialization of the path criterion in Tian–Zou, Theorem 2.3; the direct calculation also proves it here.

**(2) Nil and a universal sharp bound.** If \(E_C\) is nil, then its residue reduction \(E_C/\mathfrak m E_C\) is nil over \(\mathbb F_q\). The field theorem of Casas–Ladra–Omirov–Rozikov identifies nil finite-dimensional evolution algebras with those whose nonzero-coefficient graph is acyclic. Hence \(G_C\) is acyclic. Conversely, if it is acyclic, any maximal consecutive run of unit-coefficient edges in an index walk has length at most \(n-1\). A walk with \(t\) nonunit edges has at most \(t+1\) such runs, so its total length is at most \((t+1)(n-1)+t=n(t+1)-1\). Every walk of length \(ns\) therefore has at least \(s\) nonunit edges. Their coefficient product lies in \(\mathfrak m^s=0\); the path criterion yields \(E_C^{\langle ns+1\rangle}=0\). Right nilpotency implies elementwise nil, proving equivalence and the bound.

**(3) Characterization of equality.** If \(s=1\), the longest possible nonzero walk in the acyclic unit graph has length \(n-1\). It exists precisely when there is a Hamiltonian directed path. For \(s\ge2\), equality \(\nu(C)=ns+1\) requires a walk of length \(ns-1\) with nonzero coefficient product. It can have at most \(s-1\) nonunit edges, since each has valuation at least one and \(\mathfrak m^s=0\). The length estimate in (2) forces exactly \(s-1\) nonunit edges and \(s\) unit runs, each of length \(n-1\); every nonunit edge must have exact valuation one. Each unit run is a Hamiltonian path in the same acyclic digraph. The first Hamiltonian path uniquely fixes the topological ordering: its consecutive edges force every vertex to precede every later vertex. Hence every run uses the same order \(\sigma_1,\ldots,\sigma_n\), and the intervening nonunit edges are all the return edge \(\sigma_n\to\sigma_1\). Its valuation is one. Conversely, traversing the Hamiltonian path \(s\) times, joined by \(s-1\) such return edges, produces a walk of length \(ns-1\) whose coefficient product has exact valuation \(s-1\) and is nonzero. The sharp bound is attained.

**(4) Count all nil tables.** For any prescribed residue matrix over \(\mathbb F_q\), each of its \(n^2\) entries has exactly \(q^{s-1}\) lifts to \(R\). By (2), admissibility means the support digraph of the residue matrix is acyclic, including no loops. Let \(D_n(q)\) count such matrices. In any acyclic digraph there is at least one source. Inclusion–exclusion over a selected nonempty set of \(k\) sources gives \(\binom nk\) choices, \(q^{k(n-k)}\) possible outgoing residue coefficients, and \(D_{n-k}(q)\) configurations on the complement; this gives the recurrence displayed above. Multiplying by the independent lifting factor gives \(N_{n,s}(q)\).

**(5) Count extremal tables without overcounting.** A directed acyclic graph containing a Hamiltonian path has a **unique** topological ordering, so every extremal structure matrix is counted under exactly one of \(n!\) orders. In that order, the \(n-1\) consecutive forward entries are units; the remaining \(g=\binom{n-1}{2}\) forward entries are arbitrary; all backward and diagonal entries are nonunits. For \(s=1\) this gives \((q-1)^{n-1}q^g\) per order. For \(s\ge2\), the special return entry \(c_{\sigma_n,\sigma_1}\) has \((q-1)q^{s-2}\) choices (valuation exactly one); the \(n-1\) Hamiltonian entries each have \((q-1)q^{s-1}\) unit choices; \(g\) additional forward entries each have \(q^s\) choices; and the remaining \(n^2-n-g\) entries each have \(q^{s-1}\) choices. Multiplication gives
\[
n!(q-1)^n q^{(n-1)(s-1)+(s-2)+sg+(s-1)(n^2-n-g)}
=n!(q-1)^n q^{(s-1)n^2+g-1}.
\]
The calculation covers \(n=1\), since the Hamiltonian path has no edges and the return entry is the sole diagonal entry. All conclusions follow.

## Verification
The standalone `verify.py` exhaustively enumerates every structure matrix in nine finite ring configurations \(\mathbb Z/p^s\), including \(n=3\) over \(\mathbb Z/4\mathbb Z\) with \(262144\) candidate matrices. It constructs the original products and computes successive right-power generators without using path valuations for the index calculation. A tenth independent configuration uses explicit extension-field arithmetic in \(\mathbb F_4[\varepsilon]/(\varepsilon^2)\), and exhaustively examines all \(65536\) structure matrices of rank two. All ten cases agree with \(N_{n,s}(q)\) and \(H_{n,s}(q)\). Over \(\mathbb Z/4\mathbb Z\) at \(n=3\) the total nil and extremal counts are respectively \(12800\) and \(3072\); over \(\mathbb F_4[\varepsilon]/(\varepsilon^2)\) at \(n=2\) they are \(1792\) and \(1152\). The exact executable outputs are in `verification_output.txt`. These finite computations do not prove the symbolic arbitrary-rank theorem; the proof is given above.

## Relationship to prior work
Casas, Ladra, Omirov and Rozikov (2010), *On evolution algebras*, Theorem 2.7 and surrounding Section 2, prove the field-theoretic equivalence of nilness and a strictly triangular structure matrix. Elduque and Labra (2013), *Evolution algebras and graphs*, Theorem 3.4, describe nilness via acyclic digraphs over fields. Tian and Zou (2014), *Finitely Generated Nil but Not Nilpotent Evolution Algebras*, Theorems 2.2–2.4, study evolution algebras over general coefficient rings and supply a path-product criterion, which is explicitly used here. Their paper does not supply the finite-chain-ring sharp bound, Hamiltonian-return extremality classification, or exact table-count polynomials. Casas et al. (2012), *On nilpotent index and dibaricity of evolution algebras*, study the ordinary (all-parenthesizations) nilindex \(2^{n-1}+1\) over fields; that invariant is not the right nilindex \(n+1\) used here when \(s=1\). This statement does not claim originality for the field DAG criterion or the path criterion. No directly equivalent published or indexed prior formula was found in the comparisons performed; this is not a proof of historical priority.

## Limitations
The result classifies labeled based multiplication tables and their **right** nilpotency indices, not algebra isomorphism classes or arbitrary-parenthesization nilindex. Ring generality is limited to finite commutative principal chain rings; arbitrary finite nonprincipal local rings can behave differently. The complete distribution of all intermediate right nilindices is not determined. Uninspected or nonindexed literature may contain equivalent enumerations. Independent mathematical review has not been carried out.

## References
1. J. M. Casas, M. Ladra, B. A. Omirov and U. A. Rozikov, *On evolution algebras*, arXiv:1004.1050v1, first public 2010-04-07, https://arxiv.org/abs/1004.1050.
2. J. M. Casas, M. Ladra, B. A. Omirov and U. A. Rozikov, *On nilpotent index and dibaricity of evolution algebras*, arXiv:1208.1709v1, first public 2012-08-08, https://arxiv.org/abs/1208.1709.
3. A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1, first public 2013-12-17, https://arxiv.org/abs/1312.4685.
4. J. P. Tian and Y. M. Zou, *Finitely Generated Nil but Not Nilpotent Evolution Algebra*, arXiv:1404.5523v1, first public 2014-04-22, https://arxiv.org/abs/1404.5523.
