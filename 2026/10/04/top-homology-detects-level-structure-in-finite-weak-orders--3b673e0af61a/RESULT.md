# Top homology detects level structure in finite weak orders
## Finding
For integers \(h\ge 2\) and \(r_1,\ldots,r_h\ge 2\), let \(W=A_1\oplus\cdots\oplus A_h\) be the finite weak order with \(|A_i|=r_i\). For every continuous self-map \(f:W\to W\), the induced endomorphism of \(H_{h-1}(W;\mathbb Z)\cong\mathbb Z^{\prod_i(r_i-1)}\) is nonzero if and only if \(f\) preserves every level \(A_i\) setwise and each restriction \(f|_{A_i}\) is nonconstant. In that case, if \(s_i=|f(A_i)|\), its rank is \(\prod_i(s_i-1)\). Hence exactly \(\prod_i(r_i^{r_i}-r_i)\) self-maps act nontrivially on top homology, and a self-map induces an isomorphism on top homology if and only if it is a homeomorphism.

## Assumptions and scope
Let \(h\ge 2\). For each \(1\le i\le h\), let \(A_i\) be an antichain of cardinality \(r_i\ge 2\), and give \(W=A_1\oplus\cdots\oplus A_h\) the ordinal-sum order. This is a finite weak order and a finite \(T_0\)-space. Integral homology is computed through the natural order complex.

## Proof
The order complex \(K(W)\) is the simplicial join of the discrete sets \(A_1,\ldots,A_h\). Put \(M_i=\mathbb Z[A_i]\) and let \(\varepsilon_i:M_i\to\mathbb Z\) be augmentation. The top chain group is
\[
C_{h-1}(K(W))\cong M_1\otimes\cdots\otimes M_h.
\]
The boundary component omitting level \(i\) is, up to sign, obtained by applying \(\varepsilon_i\). Different omitted levels lie in distinct direct summands of \(C_{h-2}\). Hence, with \(V_i=\ker(\varepsilon_i)\),
\[
H_{h-1}(W;\mathbb Z)=\ker\partial\cong V_1\otimes\cdots\otimes V_h
\cong\mathbb Z^{\prod_i(r_i-1)}.
\]

Let \(f:W\to W\) be order preserving. A top simplex \((a_1,\ldots,a_h)\) has a nondegenerate top-dimensional image exactly when its images form a strict chain of length \(h\). Such a chain uses every target level once, so necessarily \(f(a_i)\in A_i\) for every \(i\). Define \(g_i:M_i\to M_i\) by \(g_i(a)=f(a)\) when \(f(a)\in A_i\) and \(g_i(a)=0\) otherwise. On top chains the induced map is \(g_1\otimes\cdots\otimes g_h\).

Assume its restriction to \(V_1\otimes\cdots\otimes V_h\) is nonzero. Then each \(g_i|_{V_i}\) is nonzero. Fix \(i\), choose vectors in all other \(V_j\) with nonzero \(g_j\)-images, and use that a chain map sends top cycles to top cycles. Applying the \(i\)-th augmentation gives \((\varepsilon_i g_i)(v)=0\) for every \(v\in V_i\). On a basis point \(a\in A_i\), \(\varepsilon_i g_i(a)\) is the indicator of \(B_i=\{a\in A_i:f(a)\in A_i\}\). An indicator vanishes on all differences \(a-a'\) only when it is constant. Nonzero \(g_i|_{V_i}\) rules out the constant zero case, hence \(B_i=A_i\). Thus \(f\) preserves every level.

Write \(\alpha_i=f|_{A_i}\) and \(s_i=|\alpha_i(A_i)|\). The image of \(V_i\) is the augmentation-zero subgroup on \(\alpha_i(A_i)\), of rank \(s_i-1\). Therefore
\[
\operatorname{rank}H_{h-1}(f)=\prod_i(s_i-1).
\]
This is nonzero exactly when every \(\alpha_i\) is nonconstant. Conversely, any levelwise choice of nonconstant \(\alpha_i\)'s defines an order-preserving self-map with nonzero top action. Since an \(r_i\)-point level has \(r_i^{r_i}-r_i\) nonconstant self-functions,
\[
\#\{f:H_{h-1}(f)\ne0\}=\prod_i(r_i^{r_i}-r_i).
\]
The rank is maximal exactly when every \(s_i=r_i\), equivalently every \(\alpha_i\) is a permutation. These are precisely the homeomorphisms of \(W\), proving the final assertion.

## Verification
The proof is symbolic for arbitrary \(h\) and \(r_i\). The included `verify.py` independently enumerates every order-preserving self-map for level-size vectors \((2,2)\), \((2,3)\), and \((2,2,2)\). It computes the induced top-chain map on a difference-tensor basis and performs exact row reduction. The totals are respectively \(36\), \(197\), and \(446\) monotone maps, with \(4\), \(48\), and \(8\) nonzero top-homology actions. The replay ends with `VERIFY_OK`.

## Relationship to prior work
Barmak and Minian identify finite \(T_0\)-spaces with finite posets, continuous maps with order-preserving maps, and use McCord's order complex for homotopy and homology; their minimal-sphere results include the all-two-point-level special family but not this general endomorphism criterion. Pouzet and Zaguia describe finite weak orders as lexicographic sums of antichains and study their endomorphisms, but the inspected material does not discuss induced homology maps. The later pseudosphere literature identifies joins of discrete sets and their wedge-of-spheres topology; the inspected treatment does not classify arbitrary self-maps by top-homology action. The present theorem supplies the missing exact rigidity, rank, and counting statement.

## Limitations
All levels are required to have at least two points; singleton levels create contractible join factors and require a different formulation. Only top integral homology is classified, not the complete homotopy class of every self-map. Finite enumeration is a consistency check rather than the proof. A residual literature risk is that the tensor-factor argument may have appeared implicitly in work on simplicial joins or pseudospheres even though the inspected sources and searches did not state this theorem.

## References
1. J. A. Barmak and E. G. Minian, “Minimal Finite Models,” arXiv:math/0611156v1, submitted 6 November 2006.
2. M. Pouzet and I. Zaguia, “Weak orders admitting a perpendicular linear order,” Discrete Mathematics 307 (2007), 97–107, DOI: 10.1016/j.disc.2006.05.038.
3. “Pseudospheres: combinatorics, topology and distributed systems,” Journal of Applied and Computational Topology, DOI: 10.1007/s41468-023-00162-5.
