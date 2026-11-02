# Dihedral homology of unordered two-particle wheel configurations

## Finding
For every integer \(k\ge5\), let \(W_k=C_k*K_1\) be the wheel consisting of a rim cycle on vertices \(\mathbb Z/k\mathbb Z\) and one central hub adjacent to every rim vertex. Let \(X_k=\operatorname{UConf}_2(|W_k|)\) denote the space of unordered pairs of distinct points of its geometric realization. The rim symmetry group \(D_k=\langle r,s:r^k=s^2=1,\ srs=r^{-1}\rangle\) acts on \(X_k\), with \(r(i)=i+1\), \(s(i)=-i\), both fixing the hub.

Write \(\varepsilon(g)=1\) for a rotation and \(\varepsilon(g)=-1\) for a reflection; let \(E_k\) be the set of the \(k\) unoriented rim edges, and let \(\mathbb Q[E_k]\) be its rational permutation representation. Then
\[
H_1(X_k;\mathbb Q)\cong\varepsilon\otimes(\mathbb Q\oplus\mathbb Q[E_k])
\quad\text{as rational }D_k\text{-modules}.
\]
The integral homology is torsion-free, with \(H_0(X_k;\mathbb Z)\cong\mathbb Z\), \(H_1(X_k;\mathbb Z)\cong\mathbb Z^{k+1}\), and \(H_j(X_k;\mathbb Z)=0\) for every \(j\ge2\).

Equivalently, if \(f(g)\) is the number of rim edges setwise fixed by \(g\), the first-homology character is \(\chi_1(g)=\varepsilon(g)(1+f(g))\). Thus \(\chi_1(1)=k+1\), every nonidentity rotation has character \(1\), and reflection characters are \(-2\) when \(k\) is odd, or \(-1\) on vertex-axis and \(-3\) on edge-axis reflections when \(k\) is even. The cyclic quotient \(X_k/C_k\) has rational first Betti number \(2\), whereas \(X_k/D_k\) has the rational homology of a point. More generally, for any rotational subgroup \(H\le C_k\) of order \(q\), its quotient has rational first Betti number \(1+k/q\). All such quotients have no higher rational homology.

## Assumptions and scope
Graphs are finite one-dimensional CW spaces with their standard geometric realization. The unordered configuration space excludes particle collisions in the interiors of edges and at vertices. The \(D_k\)-action is induced by permuting rim vertices and extending linearly over edges. Graph homology is integral unless another coefficient ring is displayed. No claim is made about the fundamental groups of the quotients or integral torsion in their homology.

Use the standard cubical two-particle graph configuration model \(D_2(W_k)\): an open cell is an unordered pair of open vertices or edges whose *closed* graph cells are disjoint. In \(W_k\), every simple cycle has at least three edges, and any two distinct essential vertices are separated by at least one edge. These are precisely the two-particle Abrams subdivision requirements (respectively \(n+1=3\), \(n-1=1\)). Thus the natural inclusion \(D_2(W_k)\hookrightarrow X_k\) induces homology isomorphisms; because the inclusion is \(D_k\)-equivariant, these are isomorphisms of \(D_k\)-modules.

## Proof
Orient each rim edge \(e_i=[i,i+1]\) in increasing cyclic order and each spoke \(a_i=[i,h]\) toward the hub \(h\). Put a fixed total order on these \(2k\) oriented edges and use exterior-product orientation on cubical two-cells. The cells of dimensions \(0,1,2\) are respectively unordered distinct vertex pairs, pairs \((e,v)\) with \(v\) outside the endpoints of \(e\), and unordered edge pairs \(\{e,f\}\) with disjoint endpoints. Their counts are
\[
 c_0=\binom{k+1}{2},\qquad c_1=2k(k-1),\qquad c_2=\binom{2k}{2}-k\binom32-\binom k2=\frac{k(3k-7)}2.
\]
There are no cells in dimensions greater than two. This cubical complex is connected: from two occupied rim vertices, one particle can traverse its incident spoke to the unoccupied hub, and the remaining rim particle can travel around the rim to a selected vertex; when the hub is initially occupied, only the second step is needed. Thus \(H_0=\mathbb Z\).

**Forest injectivity lemma (all coefficients).** Consider any cellular two-cycle \(z=\sum_{\{e,f\}}z_{e,f}[e,f]\) over an arbitrary field. Fix an oriented edge \(e\). Project \(\partial_2z\) to the one-cells \((e,v)\) with stationary vertex \(v\) disjoint from \(e\). Up to consistent orientation factors, these coefficients form exactly the graph boundary of the edge-one-chain \(\sum_{f\cap e=\varnothing}\pm z_{e,f}f\) on the vertex-induced graph \(W_k[V(W_k)\setminus\partial e]\), where \(\partial e\) is the two-endpoint set. If \(e=a_i\) is a spoke, deleting the hub and rim vertex \(i\) leaves a path on the remaining rim vertices. Its first chain boundary is injective: every one-cycle in a forest is zero over any coefficient field. Thus every coefficient containing any spoke vanishes. All remaining coefficients concern pairs of rim edges. Fixing a rim edge \(e_i\) and repeating the projection after these spoke terms vanish, the allowed partner rim edges lie on the path obtained by deleting rim vertices \(i\) and \(i+1\); the same forest argument forces their coefficients to vanish. Hence \(\partial_2\) is injective over every field, including characteristic two.

Since \(H_2(X_k;\mathbb F_p)=0\) for all primes \(p\), while \(H_2(X_k;\mathbb Z)=0\) by the identical integer forest argument, the universal coefficient theorem shows that \(H_1(X_k;\mathbb Z)\) has no prime-power torsion. With \(H_0=\mathbb Z\) and Euler characteristic \(c_0-c_1+c_2=-k\), it follows that \(H_1\cong\mathbb Z^{k+1}\).

**The character calculation.** For an element \(g\in D_k\), let \(t_j(g)\) be the trace of its signed action on the oriented cubical \(j\)-cells. The Lefschetz chain-trace identity, together with vanishing \(H_2\) and trivial connected \(H_0\), yields \(\chi_1(g)=1-t_0(g)+t_1(g)-t_2(g)\). Each fixed zero-cell contributes \(+1\); a one-cell contributes the sign with which its edge orientation is preserved; a two-cell contributes the product of its two edge-orientation signs multiplied by \(-1\) if the two edge factors are exchanged. Counting invariant configurations gives:

| Element \(g\) | \(t_0(g)\) | \(t_1(g)\) | \(t_2(g)\) | \(\chi_1(g)\) |
|---|---:|---:|---:|---:|
| Identity | \(k(k+1)/2\) | \(2k(k-1)\) | \(k(3k-7)/2\) | \(k+1\) |
| Rotation other than identity and half-turn | \(0\) | \(0\) | \(0\) | \(1\) |
| Half-turn, even \(k\) | \(k/2\) | \(0\) | \(-k/2\) | \(1\) |
| Reflection, odd \(k\) | \((k+1)/2\) | \(-2\) | \(-(k-1)/2\) | \(-2\) |
| Vertex-axis reflection, even \(k\) | \(k/2+2\) | \(2\) | \(2-k/2\) | \(-1\) |
| Edge-axis reflection, even \(k\) | \(k/2\) | \(-2\) | \(2-k/2\) | \(-3\) |

To verify the nonidentity cases structurally: a half-turn fixes \(k/2\) opposite rim-vertex pairs and swaps \(k/2\) opposite rim-edge pairs, the latter reversing square orientation. An odd-rim reflection has one reversed fixed rim edge and one fixed spoke; its two fixed oriented one-cells contribute \(-2\), one fixed rim-edge/spoke square contributes \(-1\), and its \((k-3)/2\) disjoint exchanged rim-edge pairs contribute another \(-(k-3)/2\). A vertex-axis reflection of an even rim has two fixed spokes, two contributing one-cells, and \((k-4)/2\) disjoint exchanged rim-edge pairs. An edge-axis reflection fixes two reversed rim edges, giving two negative one-cells, their one jointly fixed square contributes \(+1\), and \((k-2)/2\) disjoint exchanged rim-edge pairs contribute negative signs. These lists account for all possible fixed cells, since two distinct spokes share the hub.

For the representation \(\varepsilon\otimes(\mathbb Q\oplus\mathbb Q[E_k])\), the character is \(\varepsilon(g)(1+f(g))\). The identity fixes all \(k\) rim edges; nonidentity rotations fix none; odd-rim reflections fix one; even-rim reflections fix zero or two according to their axes. This equals the computed character on every element of \(D_k\). The semisimplicity of rational representations of finite groups therefore proves the stated isomorphism.

Finally, the rational homology of a quotient of a finite CW space by a finite group equals the invariant rational homology (a transfer/averaging argument, valid even for nonfree actions). Averaging over the \(k\) rotations gives \((k+1+k-1)/k=2\). Averaging over any rotation subgroup of order \(q\) gives \((k+1+q-1)/q=1+k/q\). The sum of \(f(s)\) over all \(k\) reflections is exactly \(k\), because each rim edge is fixed by precisely one reflection. Thus the sum of all reflection characters is \(-2k\), canceling the rotation sum \(2k\); the \(D_k\)-invariant degree-one homology vanishes. Connectedness and vanishing higher rational homology finish the quotient statements.

## Verification
The self-contained file `checker.py` reconstructs all graph cells, oriented boundary matrices, and all dihedral cellular traces without consulting the claimed character formula when constructing those matrices. It checks the integer equation \(\partial_1\partial_2=0\), exact finite-field ranks at primes \(2\), \(3\), and \(1000003\), and equality of the independently computed character with \(\varepsilon(g)(1+f(g))\) for every group element for each \(5\le k\le12\). It also checks the rotation and reflection character sums and the exact cell counts. Run `python3 checker.py`; the final output is `WHEEL_TWO_PARTICLE_DIHEDRAL_CHECKS_OK`. These finite checks corroborate, but do not replace, the all-parameter forest proof and fixed-cell classification.

## Relationship to prior work
Maciążek and Sawicki (2018 preprint) give comprehensive **nonequivariant** homology calculations for wheel graph configuration spaces; those ranks and the absence of torsion are not claimed as new. Harrison, Keating, Robbins, and Sawicki (2013) prove general first-homology structural results for two-particle braid spaces of three-connected planar graphs, again not a complete action of every wheel automorphism. An and Maciazek (2020 preprint) provide geometric braid presentations and the discrete configuration model used here. The present statement specifically identifies the full \(D_k\)-module and the even-reflection axis distinction, then derives the rational homology of its rotational and dihedral quotients. No equivalent action or stronger theorem was identified among the compared claims; this search cannot exclude all unindexed literature.

## Limitations
The representation is over \(\mathbb Q\), not a claimed decomposition of the integral \(\mathbb Z[D_k]\)-lattice. The ordinary integral homology is torsion-free, but no assertion is made about integral quotient homology or integral cohomology operations. The proof is restricted to two indistinguishable particles and wheel rims of length at least five. Literature indexing gaps and potentially implicit consequences of earlier general braid-group presentations are remaining originality risks; independent validation has not been performed.

## References
1. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, first public arXiv version June 7, 2018, arXiv:1806.02846v1, Section 5.3–5.4. https://arxiv.org/abs/1806.02846
2. B. H. An and T. Maciazek, *Geometric presentations of braid groups for particles on a graph*, arXiv:2006.15256v1, June 27, 2020; full text §§2–4. https://arxiv.org/abs/2006.15256
3. J. M. Harrison, J. P. Keating, J. M. Robbins, and A. Sawicki, *n-particle quantum statistics on graphs*, arXiv:1304.5781v1, April 21, 2013, the section on three-connected planar graphs. https://arxiv.org/abs/1304.5781
4. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648, 2011 (abstract consulted). https://arxiv.org/abs/1101.2648
