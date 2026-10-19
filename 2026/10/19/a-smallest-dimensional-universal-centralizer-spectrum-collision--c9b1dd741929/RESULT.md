# A smallest-dimensional universal centralizer-spectrum collision among connected graphical Lie algebras

## Finding

Let \(G\) and \(H\) be the following two simple graphs on the common vertex set \(\{0,1,2,3,4,5\}\), with edges written as unordered pairs:

\[
\begin{aligned}
E(G)&=\{01,02,03,04,14,23,35\},\\
E(H)&=\{04,05,13,14,23,24,34\}.
\end{aligned}
\]

For a graph \(F=(V,E)\), write \(L_F(k)=k^V\oplus k^E\) for the two-step graphical Lie algebra, with vertex basis \(e_i\), central edge basis \(f_{ij}\), and \([e_i,e_j]=f_{ij}\) for each edge with \(i<j\); all other brackets follow from bilinearity and alternation. These two Lie algebras have dimension \(13\).

For every finite field \(k=\mathbb F_q\), every positive integer \(t\), and every integer \(r\), the numbers of ordered \(t\)-tuples \((a_1,\ldots,a_t)\in L_G(k)^t\) and \((b_1,\ldots,b_t)\in L_H(k)^t\) for which the common centralizer has codimension \(r\) are **equal**. Nevertheless, for every finite field of odd characteristic, the Lie algebras are **not isomorphic**. In particular, even the full sequence of all finite-field simultaneous-centralizer rank distributions is not a complete invariant of graphical Lie algebras.

The dimension \(13\) is minimal for this phenomenon **within graphical Lie algebras of connected simple graphs**: for dimension at most \(12\), two such algebras that have the same centralizer-rank distributions for every finite field and every tuple length must be isomorphic (in odd characteristic). We claim neither minimality among arbitrary nilpotent Lie algebras nor nonisomorphism in characteristic \(2\).

## Assumptions and scope

The graph is finite, simple, undirected, and connected. Each Lie algebra is formed over the indicated finite field; its bracket convention depends on an arbitrary ordering of vertices but not the resulting isomorphism type. The equality of distributions holds for all prime powers \(q\), including powers of \(2\). Nonisomorphism and the inverse-classification statement use the characteristic-not-two graph-rigidity theorem of Mainkar, and are asserted only for odd characteristic. The minimal-dimension statement allows graphs of any connected order and any number of edges, without an imposed regularity condition.

## Proof

**1. Universal common-centralizer formula.** For a graph \(F\) on \(n\) vertices and \(m\) edges, put \(N_F[S]=S\cup\bigcup_{i\in S}N_F(i)\). For a tuple of \(t\) graphical Lie algebra elements, collect their vertex coordinates at vertex \(i\) into \(u_i\in k^t\), and let \(S=\{i:u_i\ne0\}\). The vertex coefficients \(x_i\) of an element common-centralizing the tuple satisfy, for every edge \(ij\),
\[
 u_i x_j-u_j x_i=0\quad\text{in }k^t.
\]
If \(i\in S\) is adjacent to \(j\notin S\), then \(x_j=0\). Every vertex outside \(N_F[S]\) contributes one free coefficient. On a connected component \(C\) of \(F[S]\), the relations permit one independent free coefficient precisely when all the nonzero vectors \(u_i\), \(i\in C\), are projectively equal; otherwise they force all those coefficients to zero. Thus, if \(h\) is the number of projectively monochromatic connected components of \(F[S]\), the codimension in the vertex space of the common centralizer is \(|N_F[S]|-h\), which is also the full Lie-algebra codimension because every edge coordinate is central.

Write \(P_t=(q^t-1)/(q-1)\). On a specified component of size \(c\), there are \(P_t(q-1)^c\) projectively monochromatic choices of nonzero \(u_i\), and \((q^t-1)^c-P_t(q-1)^c\) other choices. Hence the common-centralizer enumerator is
\[
 \mathcal J_{F,q,t}(z)=q^{mt}\sum_{S\subseteq V(F)}z^{|N_F[S]|}
 \prod_{C\in\operatorname{Comp}(F[S])}
 \left((q^t-1)^{|C|}-P_t(q-1)^{|C|}
 +P_t(q-1)^{|C|}z^{-1}\right).
\]
Each term is a polynomial in nonnegative powers of \(z\), because the exponent subtracted is at most the number of vertices in \(S\), hence at most \(|N_F[S]|\). This general formula was already available in earlier work; it is used here to establish a sharp inverse-invariant counterexample and is **not** claimed as a new general enumeration theorem.

**2. The two witnesses have identical profiles.** For each graph define
\[
 h_F(d,\lambda)=\#\left\{S\subseteq V(F):|N_F[S]|=d,\ \operatorname{sizes}(\operatorname{Comp}(F[S]))=\lambda\right\},
\]
where \(\lambda\) is a sorted integer partition recording component sizes (empty for the empty set). Exact direct enumeration of all \(64\) subsets for each of the two explicit seven-edge graphs gives \(h_G(d,\lambda)=h_H(d,\lambda)\) for every \(d,\lambda\). The complete common \(27\)-row certificate, including the multiplicity of each profile, is `profile.tsv`. Its counts sum to \(64\). Every summand in the displayed enumerator depends on \(S\) only through \(d\) and \(\lambda\); therefore their complete enumerators agree, for **every** field size \(q\), tuple length \(t\), and codimension \(r\).

**3. They are not isomorphic in odd characteristic.** Both graphs are connected with six vertices and seven edges. The multiset of numbers of triangles incident with each vertex is \((0,1,1,1,1,2)\) for \(G\) and \((0,0,1,1,2,2)\) for \(H\). An isomorphism of graphs preserves this multiset, so the graphs are nonisomorphic. By Mainkar's graph-rigidity theorem for graphical two-step Lie algebras in characteristic different from two [1,2], their associated Lie algebras are nonisomorphic over every odd finite field.

**4. Sharp dimension among connected graphical algebras.** A connected \(n\)-vertex graph has at least \(n-1\) edges, so its graphical Lie algebra has dimension at least \(2n-1\). Thus any connected graphical Lie algebra of dimension less than \(13\) has at most six vertices. For \(n\le5\), the standalone checker enumerates every labeled simple graph, discards disconnected ones, canonicalizes graphs using all permutations of their vertices, and verifies that the polynomial
\[
 \sum_{S\subseteq V(F)}(q-1)^{|S|}z^{|N_F[S]|-c(F[S])}
\]
(where \(c(F[S])\) is the number of induced components) is different for every pair of nonisomorphic connected graphs. The exact numbers of connected isomorphism classes for \(n=1,2,3,4,5\) are \(1,1,2,6,21\), each equal to the number of distinct coefficient signatures. At \(n=6\), dimension below \(13\) permits only \(m\le6\) edges. Connectedness forces \(m\ge5\). For \(m=5\) there are exactly six connected classes and six distinct signatures; for \(m=6\) exactly thirteen classes and thirteen distinct signatures. Distinct signatures represent distinct bivariate polynomials, since the powers \((q-1)^s\) are linearly independent; hence their specializations cannot agree for **every** finite-field size \(q\). For any connected graph with at least two vertices, the centre of the graphical Lie algebra consists exactly of the edge span: every vertex basis element has a nonzero commutator with an adjacent vertex, and the different edge coordinates prevent cancellations. Hence the coefficient of \(z^0\) in the one-tuple distribution is \(q^m\); also the sum of the coefficients is \(q^{n+m}\). Equality of distributions for all fields therefore forces equal \(m\) and equal \(n\), so comparisons across vertex orders or edge counts cannot provide lower-dimensional collisions. The unique one-vertex connected case is abelian of dimension \(1\) and causes no exception. Consequently no lower-dimensional connected graphical Lie-algebra pair has identical all-field, all-tuple distributions unless the graphs are isomorphic. The explicit pair realizes dimension \(13\), proving sharpness.

## Verification

The attachments `verify.py` and `profile.tsv` are standalone: run `python verify.py` from their common directory using only the Python standard library. The checker independently reconstructs both graphs, lists all support profiles, compares them to `profile.tsv`, verifies different triangle-participation multisets, evaluates the joint-centralizer formula in six \((q,t)\) cases, compares independent Gaussian-elimination ranks of the actual stacked bracket matrices over \(\mathbb F_2\) and \(\mathbb F_3\), and exhaustively canonicalizes all connected graphs required for the below-13 minimality assertion. Its output is preserved in `verification_output.txt`, ending `VERIFY_OK`. The exhaustive graph enumeration proves the claimed finite cutoff because all labeled graphs in the specified ranges are covered; the finite-field matrix checks are consistency checks, **not** a proof of the all-field formula. The all-field identity follows from the complete \(64\)-subset profile equality and the symbolic product formula.

For example, with one vertex tuple element and before multiplying by the \(q^7\) choices of central coefficients, both witnesses have distribution polynomial
\[
\begin{aligned}
1 & +(q-1)z+(q-1)(2q+1)z^2\\
  & +(q-1)(q^3+2q^2-q-1)z^3\\
  & +q^2(q-1)(2q^2-1)z^4+q^4(q-1)^2z^5.
\end{aligned}
\]

## Relationship to prior work

The graph-Lie construction and rigidity theorem originate with Mainkar [1,2]. Rossmann [3] developed general element-centralizer distributions of finite graphical groups, and an earlier exact result supplies the generic simultaneous-tuple formula in Step 1. Accordingly, the formula and an isolated one-tuple specialization are **not** independent novelty claims. The present contribution is the explicit nonisomorphic **universal all-length and all-field** collision, accompanied by a complete support-profile certificate and the sharp smallest-dimensional boundary for connected graphical Lie algebras. Liao and Hou [4] previously described nonrigidity of a different induced-subgraph component polynomial; this is a related caution about graph invariants but neither identifies these two seven-edge graphs as a universal Lie-centralizer collision nor proves the dimension-13 boundary.

## Limitations

The result concerns graphical Lie algebras built from **connected** simple graphs. Minimality is not asserted for arbitrary nilpotent Lie algebras, non-graph two-step Lie algebras, or disconnected graphical cases. The Lie-algebra nonisomorphism claim relies on a graph-rigidity theorem under the restriction \(\operatorname{char}k\ne2\). The support-profile computation is exhaustive for six-vertex graphs but should not be confused with a proof for arbitrary graph orders. The possibility of a specialized prior article already giving the exact collision or minimality is a residual literature risk; no independent external mathematical validation has been performed.

## References

1. M. G. Mainkar, *A short note on 2-step nilpotent Lie algebras associated with graphs*, arXiv:1010.4005v1 (first public 19 October 2010), https://arxiv.org/abs/1010.4005.
2. M. G. Mainkar, *Graphs and two-step nilpotent Lie algebras*, arXiv:1310.3414v1 (12 October 2013), https://arxiv.org/abs/1310.3414; published *Groups Geom. Dyn.* **9** (2015), 55–65.
3. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564v1 (2021), https://arxiv.org/abs/2107.05564.
4. Y. Liao and Y. Hou, *Note on the subgraph component polynomial*, arXiv:1311.6856v1 (2013), https://arxiv.org/abs/1311.6856; *Electron. J. Combin.* **21** (2014), P3.27.
