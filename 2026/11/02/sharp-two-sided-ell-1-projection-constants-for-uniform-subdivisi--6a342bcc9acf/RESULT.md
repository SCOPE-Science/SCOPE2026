# Sharp two-sided \(\ell_1\) projection constants for uniform subdivisions of complete graphs

## Finding
For integers \(n\ge 3\) and \(r\ge 1\), let \(G_{n,r}\) be the unweighted simple graph obtained by replacing each edge of the complete graph \(K_n\) with an internally vertex-disjoint path of \(r\) edges. Give the real oriented edge space \(\mathbb R^{E(G_{n,r})}\) the coordinate \(\ell_1\) norm. Let \(Z_{n,r}\) be its real circulation space (kernel of the signed vertex-edge incidence matrix), and let \(C_{n,r}=Z_{n,r}^{\perp}\) be its real cut space (Euclidean orthogonal complement).

The two **relative** projection constants, with no symmetry restriction on the competitors, are
\[
\boxed{\lambda(Z_{n,r},\ell_1(E))=\frac{3(n-2)}{n}},
\qquad
\boxed{\lambda(C_{n,r},\ell_1(E))=1+\frac{3(n-2)}n-\frac{2(n-2)}{nr}}.
\]
Both constants are attained by the orthogonal projections \(P\) and \(I-P\). Each is the **unique norm-minimizing projection among projections commuting with all label permutations**, although no uniqueness of arbitrary norm-minimizing projections is asserted.

In particular, the ordering of the two optimum costs reverses on subdivision: for \(n\ge5\), the cut-space constant is smaller than the circulation constant at \(r=1\), while the inequality is reversed for every \(r\ge2\). In all cases
\[
\lambda(C_{n,r})-\lambda(Z_{n,r})=1-\frac{2(n-2)}{nr}.
\]

## Assumptions and scope
All scalars are real. The original graph has \(n\) labeled vertices. Subdivision paths have a common integer length \(r\), with no intersections except at their original endpoints. The edge coordinates have unit \(\ell_1\) weights, independent of the chosen reference orientations. By a projection *onto* a subspace \(Y\) we mean a linear idempotent operator with image exactly \(Y\), and \(\lambda(Y,\ell_1(E))\) is the infimum of its operator norms. The graph has \(r\binom n2\) edges and circulation dimension \(\binom{n-1}{2}\).

Orient each base edge from its smaller endpoint to its larger endpoint, and orient each segment of its subdivided path in the same direction. Write \(e_{a,t}\) for the edge coordinate at position \(1\le t\le r\) on base edge \(a\). Let \(E_0=E(K_n)\), \(Z_0=Z(K_n)\), and define \(R:\mathbb R^{E_0}\to\mathbb R^{E(G_{n,r})}\) by \((Rf)_{a,t}=f_a\). Then \(Z_{n,r}=R Z_0\). This follows from conservation at each internal degree-two vertex and then at the original vertices.

## Proof
**1. The base orthogonal projection.** Let \(P_0\) be the Euclidean orthogonal projection from \(\mathbb R^{E_0}\) onto \(Z_0\). For an antisymmetric edge-flow array \(f_{ij}=-f_{ji}\), set \(s_i=\sum_{j\ne i}f_{ij}\). As \(\sum_i s_i=0\), the formula
\[
(P_0 f)_{ij}=f_{ij}-\frac{s_i-s_j}{n}
\]
produces a divergence-free flow, fixes every divergence-free flow, and subtracts a gradient orthogonal to \(Z_0\). Thus it is \(P_0\). For any fixed base edge \(a=\{i,j\}\), the column \(P_0e_a\) has entry \(d=(n-2)/n\) at \(a\), magnitude \(1/n\) on the \(2(n-2)\) other edges incident to exactly one of \(i,j\), and zero elsewhere. Its absolute column sum, and by symmetry also every absolute row sum, is
\[
L=d+\frac{2(n-2)}n=\frac{3(n-2)}n=3d.
\]

**2. All invariant circulation projections.** The label-permutation group \(S_n\) acts on the subdivided oriented edge space by signed coordinate permutations, preserving \(Z_{n,r}\), \(C_{n,r}\), and the coordinate \(\ell_1\) norm. Fix a base edge with ordered ends \(i,j\). A circulation on \(K_n\) invariant under all permutations fixing \(i,j\) is one-dimensional: its antisymmetric coordinates satisfy \(f_{ij}=a\), \(f_{ik}=b\), \(f_{jk}=c\) for all remaining \(k\), and \(f_{k\ell}=0\) when both indices are remaining vertices. The last equality is forced by exchanging \(k,\ell\). Conservation gives \(b+c=0\) and \(a+(n-2)b=0\). Hence this fixed space is spanned by \(P_0e_{ij}\). The argument also holds for \(n=3\), when there is only one remaining vertex.

Let \(T\) be a label-invariant projection onto \(Z_{n,r}\). Its value on any \(e_{a,t}\) must therefore be
\[
T(e_{a,t})=w_t R(P_0e_a)
\]
for real weights \(w_1,\ldots,w_r\), independent of \(a\). A label permutation reversing the ends of \(a\) also reverses its subdivision path, so the weights satisfy \(w_t=w_{r+1-t}\). Because \(T(Rf)=\bigl(\sum_t w_t\bigr)R(P_0f)\), and \(T\) fixes \(RZ_0\), we have \(\sum_t w_t=1\). Conversely, every such symmetric weight vector of sum one defines an invariant projection onto \(Z_{n,r}\); denote it \(T_w\).

Each column of \(T_w\) is \(w_t\) times a vector consisting of \(r\) copies of \(P_0e_a\). Consequently,
\[
\|T_w\|_{1\to1}=rL\max_t |w_t|\ge L,
\]
with equality exactly for \(w_t=1/r\) for every \(t\). Averaging any projection over the finite isometry group \(S_n\) preserves its projection property and cannot increase its norm. Thus this is the global minimum. For these equal weights,
\[
P=T_w=\frac1r RP_0R^{\mathsf T},
\]
which is exactly the Euclidean orthogonal projection onto \(Z_{n,r}\), since \(R^{\mathsf T}R=rI\). It is the unique label-invariant cycle projection attaining the minimum.

**3. All invariant cut projections and their sharp bound.** Suppose \(Q\) is a label-invariant projection onto \(C_{n,r}\). Its adjoint \(Q^{\mathsf T}\) has kernel \(C_{n,r}^{\perp}=Z_{n,r}\). Therefore \(I-Q^{\mathsf T}\) is a label-invariant projection onto \(Z_{n,r}\), so \(Q=I-T_w^{\mathsf T}\) for some symmetric real weights of sum one. Since the base matrix \(P_0\) is symmetric, the row of \(T_w\) indexed by \((a,t)\) has entries \(w_s(P_0)_{ab}\) as \((b,s)\) varies. Writing \(W=\sum_s|w_s|\ge1\), the absolute row sum of \(I-T_w\) at \((a,t)\) is exactly
\[
F_t=|1-dw_t|+LW-d|w_t|.
\]
Choose \(t\) with \(w_t\le1/r\). If \(w_t\le0\), then \(F_t=1+LW\ge1+L\). If \(0<w_t\le1/r\), then \(d<1\) implies
\[
F_t=1+LW-2dw_t\ge1+L-\frac{2d}{r}.
\]
In either case \(\|Q\|_{1\to1}=\|I-T_w\|_{\infty\to\infty}\ge1+L-2d/r\). Equality is achieved when every \(w_t=1/r\), for which every row gives that same value. The argument shows equal weights are the only invariant minimizing weights. Averaging an arbitrary cut projection over \(S_n\) proves the global lower bound; the equal-weight operator is \(Q=I-P\). Substitution of \(L=3d\) gives the claimed second formula.

**4. Ordering change.** Subtracting the first constant from the second gives \(1-2(n-2)/(nr)\). For \(r=1\), this is \((4-n)/n\), negative when \(n\ge5\); for every \(r\ge2\) it is at least \(2/n>0\). This proves the strict order reversal without any asymptotic approximation. \(\square\)

## Verification
The accompanying Python 3 standard-library program `CHECK.py` constructs the complete orthogonal projection matrices with exact `fractions.Fraction` arithmetic, checks idempotence, incidence conservation, path-constancy, permutation covariance, and both column-norm formulas for every integer pair \(3\le n\le7\), \(1\le r\le4\). Run `python3 CHECK.py`. Its complete terminal summary is `CHECK_OK 94060 exact rational assertions, all pairs 3<=n<=7,1<=r<=4`. The proof above is independent of and strictly stronger than these finite calculations.

## Relationship to prior work
The representation-theoretic principle that a minimum-norm projection can be found by averaging over isometries is classical; [1] develops the cycle-space version and studies Hamming graphs and discrete tori. The present calculation exploits a different, explicitly described one-parameter-per-subdivision-layer invariant family and determines both complementary \(\ell_1\)-projection constants for all complete-graph uniform subdivisions. The finite metric and transportation-space context is also developed in [2]. In the inspected portions of [1] and [2], no theorem directly gives the two-parameter formulas or the strict subdivision-driven order reversal.

## Limitations
The claim concerns **relative** projection constants in the specified coordinate real \(\ell_1\) edge space, not absolute projection constants or norms in all Banach spaces. It does not cover unequal path lengths, weighted edges, other base graphs, or non-\(\ell_1\) norms. Uniqueness is proved only among label-permutation-invariant projections; it is not asserted for all minimizers. These formulas alone do not settle distortion or complementability invariants outside the stated ambient edge space.

## References
[1] S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first public version 2023-05-21. https://arxiv.org/abs/2305.12582

[2] S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814, first public version 2018-07-10. https://arxiv.org/abs/1807.03814
