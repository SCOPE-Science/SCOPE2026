# Integral dihedral and arrow-reversal homology of cycle flex complexes

## Finding
For every integer \(n\ge3\), let \(F_n=\operatorname{Flex}(C_n)\) be the cubical complex of source/sink flips on orientations of a simple \(n\)-cycle. Let \(D_n=\langle r,s\rangle\) act by geometric polygon symmetries, and let the commuting involution \(\tau\) reverse all arrows without moving vertices. Then \(F_n\) has integral homology bases \(u_0,\ldots,u_n\) in degree zero and \(e_1,\ldots,e_{n-1}\) in degree one, with all higher homology zero, for which
\[
\begin{aligned}
r u_k&=u_k,& s u_k&=\tau u_k=u_{n-k},\\
r e_k&=e_k,&s e_k&=e_{n-k},&\tau e_k&=-e_{n-k}.
\end{aligned}
\]
These identities completely specify the integral \(D_n\times C_2\)-modules. In particular, the two natural involutions \(s\) and \(\tau\) act identically on the set of connected components but with opposite signs on the primitive loop generators.

For \(r^a s^b\tau^c\), with \(0\le a<n\) and \(b,c\in\{0,1\}\), let \(I_n\) equal one for even \(n\) and zero for odd \(n\). The ordinary homology traces are
\[
\operatorname{tr}(H_0)=\begin{cases}n+1,&b+c\equiv0\pmod2,\\I_n,&b+c\equiv1\pmod2,\end{cases}
\]
\[
\operatorname{tr}(H_1)=(-1)^c\begin{cases}n-1,&b+c\equiv0\pmod2,\\I_n,&b+c\equiv1\pmod2.\end{cases}
\]
Moreover, \(s\tau\) acts as negative identity on \(H_1\), hence \(H_1(F_n;\mathbb Q)^{D_n\times C_2}=0\). The quotient \(F_n/(D_n\times C_2)\) has exactly \(\lfloor n/2\rfloor+1\) components and no positive-degree rational homology.

## Assumptions and scope
All graphs are finite, simple and undirected. Number the edges of \(C_n\) as \(j\to j+1\) for \(j\in\mathbb Z/n\mathbb Z\), using this direction only to encode an orientation vector \(x\in\{0,1\}^n\): the bit \(x_j=1\) means that edge \(j,j+1\) points clockwise. An allowable flex reverses all arrows incident with a source or sink. At a vertex \(i\), this is exactly the swap of unequal bits \(x_{i-1},x_i\), transforming \(10\leftrightarrow01\). Independent simultaneous flexes provide higher cubes. The number \(k=\sum_j x_j\) is preserved under every flex. Spatial rotation \(r\) cyclically shifts bits; spatial reflection \(s\) reverses bit order and complements each bit; global arrow reversal \(\tau\) complements bits in their original positions. Both \(s\) and \(\tau\) exchange \(k\) and \(n-k\), while \(r\) fixes \(k\).

## Proof
**1. Published nonequivariant input.** Kozlov's Proposition 6.10 gives precisely one path component for each \(k\in\{0,\ldots,n\}\). At \(k=0\) and \(k=n\), it is a point; for \(1\le k\le n-1\), it is homotopy equivalent to a circle. This prior theorem establishes the integral homology ranks and degree concentration, but gives no signs of the actions considered here.

**2. Primitive flux cohomology class.** On a directed cellular one-cell (one elementary flex), define the integer-valued cochain \(\alpha_i\) to be \(+1\) when a clockwise bit-particle moves from edge \(i-1\) to edge \(i\), \(-1\) for its inverse move, and zero for every flex at a different vertex. A two-dimensional cube consists of flips at nonadjacent vertices with disjoint incident edge pairs. Its two boundary paths perform the same two commuting operations, so \(d\alpha_i=0\) on every cube; higher cubes impose no additional cochain condition. If \(x_i\) also denotes the integer-valued zero-cochain reading occupancy at edge \(i\), then the exact cochain identity \(d x_i=\alpha_i-\alpha_{i+1}\) holds on every directed one-cell. Thus the cohomology classes of all \(\alpha_i\) coincide. Denote this integral class on a fixed component by \([\alpha]\).

To see that \([\alpha]\) is primitive on each \(1\le k\le n-1\) component, start with occupied edges \(0,1,\ldots,k-1\). Move the bit on edge \(k-1\) forward through edges \(k,k+1,\ldots,n-1\), then move the remaining bits one step forward in descending order from edge \(k-2\) down to edge zero, and finally move the bit on edge \(n-1\) forward across the cyclic boundary to edge zero. This is a closed edge-path, because it restores precisely the initial configuration. It crosses each vertex in the forward direction exactly once, and never crosses a vertex backward. Hence \(\int\alpha_i=1\) for every \(i\). The published \(H_1\cong\mathbb Z\) and this unit pairing show that \([\alpha]\) is a primitive integral generator of \(H^1\). Choose \(e_k\in H_1\) as the generator pairing to \(+1\) with \([\alpha]\) on the \(k\) component.

**3. Group action on flux.** A spatial rotation sends a forward passage across one polygon vertex to a forward passage across the rotated vertex; it preserves the cohomology flux class. A spatial reflection reverses the cyclic order of edges *and* reverses the orientation-bit convention, replacing a clockwise particle by a hole; these two reversals preserve the signed clockwise particle passage. Consequently \(s\) carries \([\alpha]\) from the \(k\) component to the same positive flux class on the \(n-k\) component. A global arrow reversal replaces particles by holes but does not reverse the polygon order, so it sends a clockwise particle move to a counterclockwise particle move: \(\tau\) negates the flux class. This proves \(r e_k=e_k\), \(s e_k=e_{n-k}\) and \(\tau e_k=-e_{n-k}\), including at the middle component for even \(n\). The homology in degree zero is the free abelian group on connected components, so the formulas for \(u_k\) follow from the action on \(k\).

**4. Traces and quotient.** For any \(r^a s^b\tau^c\), the component index is fixed precisely when \(k=n-k\) if \(b+c\) is odd; otherwise all indices are fixed. The first-homology sign is \((-1)^c\) on every fixed circle component, giving both trace formulas. The element \(s\tau\) fixes each component but has sign \(-1\) on its first homology, so the full group's rational first-homology invariant subspace vanishes. A finite cubical group action admits an invariant subdivided triangulation; averaging over the finite group identifies rational cohomology of its orbit space with group invariants. Hence the quotient has no positive-degree rational homology. The \(D_n\times C_2\) action on components identifies exactly \(k\sim n-k\), giving \(\lfloor n/2\rfloor+1\) quotient components.

## Verification
The standalone standard-library script `verify.py` enumerates actual cubical cells by sets of independent simultaneously flippable vertices and orientations on unaffected edges. For every \(n\in\{3,4,5,6,7,8,9,10\}\), every cyclic shift and each choice of spatial reflection and global arrow reversal, it computes the signed trace on each cellular chain group and checks its alternating sum against the predicted difference of homology traces. All **208 signed cellular Lefschetz comparisons passed**. This finite test corroborates, but does not replace, the general flux pairing and published nonequivariant homotopy theorem. Reproduce by running `python3 verify.py` with Python 3 (standard library only).

## Relationship to prior work
Kozlov's 2026 paper studies flex complexes and proves the circle/point component classification for cycles in Proposition 6.10. That theorem is explicitly assumed, not attributed here as a new result. The new result is the complete **integral equivariant homology action**, including the distinction between reflection and global arrow reversal, and its rational quotient consequence. A relevant published result on complete-graph flex complexes determines \(S_n\)-equivariant rational homology for \(\operatorname{Flex}(K_n)\), which is a different graph family with a one-dimensional flex complex and does not imply the present cycle case.

## Limitations
The theorem concerns simple cycles, their geometric dihedral relabelings and the global arrow-reversal involution. It does not assert an equivariant homotopy equivalence, contractibility or integral acyclicity of the symmetry quotient, and does not classify arbitrary graph flex complexes. The source's circle classification is used as an essential external theorem. Equivalent results in unindexed literature have not been ruled out, and no independent audit has been performed.

## References
1. D. N. Kozlov, “Flex complexes of graphs,” *Journal of Applied and Computational Topology* **10**, article 10 (published online 2026-05-23), DOI: 10.1007/s41468-026-00235-1; especially Proposition 6.10, open full text: https://link.springer.com/content/pdf/10.1007/s41468-026-00235-1.pdf.
2. “Equivariant homology and symmetry quotients of complete-graph flex complexes,” published-finding corpus (published 2026-10-11), research record: https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-equivariant-homology-and-symmetry-quotients-of-complete-graph-fl--d33423646847. The comparison concerns the different family \(\operatorname{Flex}(K_n)\).
