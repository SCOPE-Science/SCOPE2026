# Leaf-sibling Lie factors and modular cycle resonance in functional evolution algebras

## Finding

For every finite nonempty set \(V\), endofunction \(f:V\to V\), and field \(k\), consider the evolution algebra \(E_f(k)\) with natural basis \(\{e_v:v\in V\}\) and multiplication
\[
e_v e_w=0\quad(v\ne w),\qquad e_v^2=e_{f(v)}.
\]
Let \(P=f(V)\), and let \(B=V\setminus P\) be the indegree-zero vertices (called *leaves* here). For each \(y\in V\) put \(B_y=\{v\in B:f(v)=y\}\) and \(m_y=|B_y|\). Each connected component of the underlying functional directed graph has one cycle; denote their lengths by \(L_1,\dots,L_c\). For \(\operatorname{char}k\ne2\), let
\[
r_k=\#\{j:2^{L_j}=1\text{ in }k\}.
\]
Thus \(r_k=0\) in characteristic zero; in odd characteristic \(p\), the equality means that the multiplicative order of \(2\) in \(\mathbb F_p^\times\) divides \(L_j\).

**Theorem (Lie-algebra classification).** With commutator bracket on derivations, if \(\operatorname{char}k\ne2\), then
\[
\operatorname{Der}_k(E_f(k))\cong
k^{r_k}\oplus\bigoplus_{y\in V}\mathfrak{so}_{m_y}(k),
\]
where \(k^{r_k}\) is central and \(\mathfrak{so}_{m}(k)\) is the Lie algebra of skew-symmetric \(m\times m\) matrices. In characteristic two,
\[
\operatorname{Der}_k(E_f(k))\cong
\bigoplus_{y\in V}\operatorname{Sym}_{m_y}(k),
\]
where \(\operatorname{Sym}_m(k)\) means the **Lie algebra** of symmetric matrices under the ordinary commutator, not an associative matrix algebra. In characteristic two the commutator of two symmetric matrices is symmetric, so the notation indeed defines a Lie algebra.

In particular,
\[
\dim_k\operatorname{Der}_k(E_f(k))=
\begin{cases}
 r_k+\displaystyle\sum_{y\in V}\binom{m_y}{2},&\operatorname{char}k\ne2,\\[2mm]
 \displaystyle\sum_{y\in V}\binom{m_y+1}{2},&\operatorname{char}k=2.
\end{cases}
\]
For \(k=\mathbb F_q\), the number of individual derivations is \(q\) raised to the indicated dimension.

The two kinds of graph information are independent in the formulas: directed cycles control only the possible central diagonal directions in odd characteristic; groups of sibling leaves control all noncentral Lie factors. In characteristic two only the leaf-sibling data survive.

## Assumptions and scope

There is no condition on separability, algebraic closure, finiteness of the field, injectivity of \(f\), or the number of connected components. Every basis square is nonzero. A functional component is the weakly connected component of the directed graph having exactly one arrow \(v\to f(v)\) out of every vertex. The indegree-zero set \(B\) is defined using incoming arrows, even when fixed points and cycles occur. Empty and singleton blocks contribute zero skew-symmetric dimension; the singleton symmetric block in characteristic two contributes one dimension.

The displayed decompositions are Lie-algebra isomorphisms induced by the specified natural basis, not claims of a basis-free canonical splitting across different presentations. A diagonal derivation indexed by a resonant functional component has the form \(D(e_v)=\delta_v e_v\), where \(\delta_{f(v)}=2\delta_v\) and its value at a chosen cycle vertex is arbitrary. Such a diagonal derivation is central in the full derivation Lie algebra.

## Proof

Write an arbitrary linear map as \(D(e_v)=\sum_{u\in V}a_{uv}e_u\). Its Leibniz identities need only be checked on basis pairs. For \(v\ne w\), applying \(D\) to \(e_ve_w=0\) gives
\[
a_{wv}e_{f(w)}+a_{vw}e_{f(v)}=0.\tag{1}
\]
Applying \(D\) to \(e_v^2=e_{f(v)}\) gives
\[
D(e_{f(v)})=2a_{vv}e_{f(v)}.\tag{2}
\]
Conversely, (1) and (2) for all indicated vertices are sufficient, by bilinearity, to make \(D\) a derivation.

First, (2) implies that every column indexed by a vertex of \(P=f(V)\) is diagonal. If \(f(v)\ne f(w)\), the two distinct basis vectors in (1) force \(a_{wv}=a_{vw}=0\). If \(f(v)=f(w)\), (1) says \(a_{wv}=-a_{vw}\). In the latter case, an off-diagonal pair can be nonzero only if *both* vertices lie outside \(P\); otherwise the diagonal-column condition eliminates both entries. Consequently all off-diagonal derivation entries occur inside the disjoint leaf-sibling sets \(B_y\). Within each such set they are skew-symmetric; in characteristic two, this is the symmetry equation \(a_{vw}=a_{wv}\).

The remaining diagonal conditions are
\[
a_{f(v),f(v)}=2a_{vv}\qquad(v\in V).\tag{3}
\]
Suppose \(2\ne0\) in \(k\). Within a leaf-sibling set \(B_y\), (3) forces \(a_{vv}=a_{ww}\), since both are \(\tfrac12a_{yy}\). On each directed cycle of length \(L\), iterating (3) yields \((2^L-1)a_{vv}=0\). If \(2^L\ne1\), all diagonal entries on that cycle vanish and, by invertibility of two, so do the diagonal entries on the incoming trees. If \(2^L=1\), choosing any one cycle value determines all other cycle values via (3), and also uniquely determines all tree values by division by two. There is therefore exactly one free diagonal scalar per resonant weak component. Because the diagonal entries are constant on each \(B_y\), their matrices commute with every permitted leaf-sibling skew block. Moreover distinct leaf blocks have disjoint supports. This proves both the direct-sum Lie decomposition and the dimension formula in characteristic different from two.

If \(2=0\), (3) reads \(a_{f(v),f(v)}=0\), and hence exactly all diagonal entries indexed by \(P\) vanish. The diagonal entries indexed by \(B\) are individually free. For each \(B_y\) the whole supported matrix is thus an arbitrary symmetric \(m_y\times m_y\) block. Such blocks commute with blocks on other supports. If \(A^T=A\) and \(C^T=C\) in characteristic two, then \([A,C]^T=-[A,C]=[A,C]\), so each symmetric block is closed under the Lie bracket. No conditions remain by (1) and (2), proving the characteristic-two decomposition and count. All statements include the boundary case of singleton functional components and empty leaf sets.

## Verification

The accompanying program `verify_functional_derivations.py` independently constructs the complete homogeneous Leibniz linear system from the multiplication table over small prime fields. For each test it compares the rank of the full equation system with the proposed block-and-cycle basis, verifies that every proposed basis vector satisfies all equations, and samples matrix commutators for closure. It covers **1164** configurations: all endofunctions on one through four labeled vertices over each of \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\), plus three five-vertex examples per prime. The expected successful termination message is `VERIFY_OK_FUNCTIONAL_DERIVATION_LIE`. Run with `python3 verify_functional_derivations.py`; no third-party packages are required. Direct linear algebra is a finite check and is not used as a proof for arbitrary \(V\) or \(k\).

As a concrete separation, the five-vertex star map \(f(0)=0\) and \(f(i)=0\) for \(1\le i\le4\) has one leaf-sibling set of size four. The five-vertex chain map \(f(0)=0\), \(f(i)=i-1\) for \(1\le i\le4\), has one leaf-sibling set of size one. Both have exactly one fixed-point cycle and thus identical idempotent element schemes. Indeed, writing \(x=\sum_v z_ve_v\), the equations \(x^2=x\) force every indegree-zero coordinate to vanish, then eliminate all noncyclic coordinates successively; the one remaining fixed-point coordinate obeys \(z_0^2=z_0\). Hence in both examples the scheme is \(\operatorname{Spec}k[T]/(T^2-T)\), including its scheme structure in every characteristic. Nevertheless, their derivation Lie-algebra dimensions are respectively \(6\) and \(0\) when \(\operatorname{char}k\ne2\), and \(10\) and \(1\) when \(\operatorname{char}k=2\). Thus the derivation invariant detects tree information missed by cycle-only idempotent data. In odd characteristic the dimension statement for the fixed-point cycle has \(r_k=0\), because \(2-1\ne0\).

## Relationship to prior work

The universal Leibniz equations for evolution-algebra derivations predate this theorem. Camacho, Gómez, Omirov and Turdibaev (2010) studied complex evolution algebras by structure-matrix rank and include the rank-one-defect and full-rank regimes. Cadavid, Rodiño Montoya and Rodríguez (2018) classified derivations of evolution algebras associated to undirected adjacency graphs using twin partitions. Cabrera Casado, Cadavid, Rodiño Montoya and Rodríguez (2019) established a characteristic-zero directed-graph twin-block restriction; it contains the general mechanism for leaf-pair off-diagonals in that characteristic. Elduque and Labra (2019) classified derivations of *perfect* evolution algebras in arbitrary characteristic, including the already-covered bijective-function cycle-resonance specialization. Cabrera Casado, Cadavid and Reis (2022/2023) gave general necessary-and-sufficient derivation conditions for nondegenerate evolution algebras, including arbitrary-characteristic rank-one-square cases; those conditions subsume some special configurations here.

The result isolated in this note is the **simultaneous closed Lie-algebra isomorphism type and all-characteristic dimension formula for every non-surjective functional digraph**, with the distinction between skew and symmetric leaf blocks, a modular resonance term for cycles, and a tree-sensitive comparison. It is not a claim that the general derivation equations, block restrictions, bijective-case resonance, or star examples are novel. The broader necessary-and-sufficient criteria are not themselves explicit leaf-sibling Lie factorizations for all functional endomaps. No identical statement was located in the inspected sources; this does not settle historical priority.

## Limitations

This is a classification for **unweighted** single-outgoing-edge evolution algebras, not for weighted arrows, multiple descendants, degenerate algebras having zero basis squares, or arbitrary natural-basis changes. It does not reconstruct all attached trees from derivations: distinct functional graphs can share the multiset of leaf-sibling sizes and cycle resonances. The finite-field formula counts derivations, not algebra automorphisms. The comparison against published literature is incomplete: a direct closed-form decomposition under other graph-theoretic terminology may exist, and general if-and-only-if derivation criteria contain ingredients sufficient to recover the special case after further analysis. The mathematical argument establishes only the stated classification, not publication priority or independent validation.

## References

1. L. M. Camacho, J. R. Gómez, B. A. Omirov, R. M. Turdibaev, *The derivations of some evolution algebras*, arXiv:1004.1936v1, 12 April 2010. https://arxiv.org/abs/1004.1936
2. P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez, *Characterization theorems for the spaces of derivations of evolution algebras associated to graphs*, arXiv:1807.02493, 6 July 2018. https://arxiv.org/abs/1807.02493
3. Y. Cabrera Casado, P. Cadavid, M. L. Rodiño Montoya, P. M. Rodríguez, *On the characterization of the space of derivations in evolution algebras*, arXiv:1912.06925v1, 14 December 2019. https://arxiv.org/abs/1912.06925
4. A. Elduque, A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191, 6 February 2019. https://arxiv.org/abs/1902.02191
5. Y. Cabrera Casado, P. Cadavid, T. Reis, *Derivations and loops of some evolution algebras*, arXiv:2203.13657, first posted March 2022, published 2023. https://arxiv.org/abs/2203.13657
