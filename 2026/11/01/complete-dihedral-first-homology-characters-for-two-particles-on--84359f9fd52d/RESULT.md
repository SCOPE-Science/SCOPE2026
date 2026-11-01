# Complete dihedral first-homology characters for two particles on wheel graphs

## Finding
For each integer \(n\ge4\), let \(W_{n+1}=C_n*K_1\) be the wheel with rim vertices \(0,\ldots,n-1\) and hub \(h\). Let \(X_n=\operatorname{UConf}_2(|W_{n+1}|)\) be the configuration space of two distinct **unordered** points on its geometric realization. The complete graph-automorphism group is the dihedral group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\), acting by \(r(i)=i+1\), \(s(i)=-i\) on rim indices modulo \(n\) and fixing \(h\).

The complete rational first-homology character \(\chi_n(g)=\operatorname{tr}(g_*\mid H_1(X_n;\mathbb Q))\) is
\[
\chi_n(r^k)=\begin{cases}n+1,&k=0,\\1,&1\le k<n,\end{cases}
\qquad
\chi_n(sr^k)=\begin{cases}
-2,&n\text{ odd},\\
-1,&n\text{ even and }k\text{ even},\\
-3,&n\text{ even and }k\text{ odd}.
\end{cases}
\]
Here \(s r^k\) sends \(i\) to \(-i-k\); since \(k\) and \(-k\) have the same parity, the even-rim reflection types are unambiguous.

Over \(\mathbb C\), write \(\varepsilon_s(r)=1\), \(\varepsilon_s(s)=-1\), and, for even \(n\), \(\varepsilon_r(r)=-1\), \(\varepsilon_r(s)=1\). Let \(\rho_j\) be the standard two-dimensional dihedral representation with \(\operatorname{tr}\rho_j(r^k)=2\cos(2\pi jk/n)\), \(\operatorname{tr}\rho_j(sr^k)=0\). Then
\[
H_1(X_n;\mathbb C)\cong\begin{cases}
2\varepsilon_s\oplus\displaystyle\bigoplus_{j=1}^{(n-1)/2}\rho_j,&n\text{ odd},\\
2\varepsilon_s\oplus\varepsilon_r\oplus\displaystyle\bigoplus_{j=1}^{n/2-1}\rho_j,&n\text{ even}.
\end{cases}
\]
The summands \(\rho_j\) are specified as complex, not necessarily rational, irreducibles. A conceptual equivalent formulation is the rational-module identity
\[
H_1(X_n;\mathbb Q)\cong H_1(|W_{n+1}|;\mathbb Q)\oplus\varepsilon_s\qquad\text{as }\mathbb Q[D_n]\text{-modules}.
\]
In particular, all full-dihedral invariant vectors vanish, while the rotation-invariant subspace has dimension two:
\[
H_1(X_n;\mathbb Q)^{D_n}=0,\qquad \dim H_1(X_n;\mathbb Q)^{\langle r\rangle}=2.
\]
The ordinary finite-group orbit spaces consequently satisfy \(\widetilde H_*(X_n/D_n;\mathbb Q)=0\) and \(H_1(X_n/\langle r\rangle;\mathbb Q)\cong\mathbb Q^2\). The original space has \(H_0(X_n;\mathbb Z)=\mathbb Z\), \(H_2(X_n;\mathbb Z)=0\), and \(\operatorname{rank}H_1(X_n;\mathbb Z)=n+1\). **The new claim is the complete dihedral character and its ordinary-quotient consequences, not these underlying ranks.**

## Assumptions and scope
All edges are topological closed intervals and two particles may pass through vertices but never coincide. The graph is simple, undirected, finite, and has unit edge lengths only as convenient geometric coordinates. The wheel has \(n\) rim edges and \(n\) spokes; for \(n\ge4\), the hub has degree \(n>3\), proving \(\operatorname{Aut}(W_{n+1})=D_n\). The wheel's triangles have three edges, so the standard sufficient-subdivision hypothesis for a two-particle Abrams cubical model is satisfied. The inclusion of that model into \(X_n\) is a graph-automorphism-equivariant homotopy equivalence. All representation statements are over the indicated coefficient fields. The quotient notation means an **ordinary** orbit space, not a homotopy/Borel quotient.

## Proof
**1. The finite cubical model.** A zero-cell is a pair of distinct vertices, a one-cell is a pair \((v,e)\) with \(v\) a vertex outside the endpoints of edge \(e\), and a square is an unordered pair \(\{e,f\}\) of edges with disjoint endpoints. Number these cells in degrees zero, one, and two. Their exact counts are
\[
c_0=\binom{n+1}{2},\quad c_1=2n(n-1),\quad c_2=\binom{2n}{2}-\binom n2-3n=\frac{n(3n-7)}2.
\]
For \(c_2\), subtract the incident edge pairs at the degree-\(n\) hub and at the \(n\) degree-three rim vertices. Hence \(\chi(X_n)=-n\). The space is connected: any unordered configuration can be moved to two distinct graph vertices, then to a hub–rim pair using a free spoke; two hub–rim pairs are connected by moving the hub point to a spare rim vertex, moving the other point into the hub, and moving the remaining rim point along the rim to the target vertex. At least one spare rim vertex exists for \(n\ge4\).

**2. No top two-cycles.** Orient every graph edge arbitrarily, and give a square \(\{e,f\}\) the product orientation. Suppose \(z=\sum a_{\{e,f\}}[e,f]\) is an **integral** two-cycle. Fix a spoke \(f=\{h,i\}\). In the boundary rows indexed by \((v,f)\), the coefficients \(a_{\{e,f\}}\) form a one-cycle in the graph obtained by deleting \(h\) and \(i\) and all their incident edges. That graph is a path on the remaining \(n-1\) rim vertices, so all those coefficients vanish. Thus no square involving a spoke has nonzero coefficient. Now fix a rim edge \(f=\{i,i+1\}\) and use the same boundary rows: only its disjoint rim-edge partners remain, and those lie in a path after deleting the two consecutive rim vertices. Their coefficients vanish as well. Therefore \(z=0\), \(\partial_2\) is injective over \(\mathbb Z\), and \(H_2(X_n;\mathbb Z)=0\). Connectivity and Euler characteristic give \(\dim_{\mathbb Q}H_1(X_n;\mathbb Q)=n+1\).

**3. Signed cellular Lefschetz traces.** Orient each edge \([a,b]\) by increasing vertex label (with the hub labeled \(n\)), and orient square \([e,f]\) by the product when edge \(e\) precedes edge \(f\) in lexicographic order. For an automorphism \(g\), let \(t_q(g)=\operatorname{tr}(g\mid C_q(X_n;\mathbb Q))\), using the signed action on oriented cells. A fixed vertex pair contributes \(+1\) to \(t_0\). A fixed one-cell \((v,e)\) contributes the orientation sign of \(g\) on \(e\) to \(t_1\). For a fixed square, the product of the two edge-orientation signs is multiplied by \(-1\) if its edge factors are interchanged.

These rules give the following exhaustive table of cellular trace contributions. An even-rim vertex-axis reflection fixes two opposite rim vertices; an edge-axis reflection fixes two opposite rim edges setwise.

| Automorphism type | \(t_0\) | \(t_1\) | \(t_2\) |
| --- | ---: | ---: | ---: |
| Identity | \(n(n+1)/2\) | \(2n(n-1)\) | \(n(3n-7)/2\) |
| Nonidentity rotation, not half-turn | \(0\) | \(0\) | \(0\) |
| Antipodal half-turn, even \(n\) | \(n/2\) | \(0\) | \(-n/2\) |
| Reflection, odd \(n\) | \((n+1)/2\) | \(-2\) | \(-(n-1)/2\) |
| Vertex-axis reflection, even \(n\) | \((n+4)/2\) | \(2\) | \(2-n/2\) |
| Edge-axis reflection, even \(n\) | \(n/2\) | \(-2\) | \(2-n/2\) |

To verify the nontrivial entries directly, every nonidentity rotation has no fixed rim vertex or edge; only an antipodal half-turn interchanges two disjoint rim edges, with \(n/2\) such pairs and square orientation sign \(-1\). An odd-rim reflection fixes the hub, one rim vertex, one spoke pointwise, and one rim edge setwise but reversed. Its fixed one-cells are the two pairs of the reversed rim edge with the fixed vertices, each contributing \(-1\). Among its fixed squares, the fixed spoke–rim-edge square contributes \(-1\), while the \((n-3)/2\) remaining disjoint reflected rim-edge pairs each contribute \(-1\). An even vertex-axis reflection fixes the hub and two rim vertices; the two fixed spokes contribute \(+1\) to the one-cell trace, and the \((n-4)/2\) disjoint reflected rim-edge pairs contribute \(-1\) each to the square trace. An even edge-axis reflection fixes the hub and two reversed rim edges; its two fixed one-cells contribute \(-1\) each, while the square of the two reversed edges contributes \(+1\) and the \((n-2)/2\) additional disjoint reflected rim-edge pairs contribute \(-1\) each. Finally, fixed zero-cells are unordered pairs of individually fixed vertices or transposed rim-vertex pairs, giving the displayed values.

Because \(H_0\) is the trivial line and \(H_2=0\), the Lefschetz identity reads
\[
\chi_n(g)=1-t_0(g)+t_1(g)-t_2(g).
\]
Substituting all rows proves the asserted formulas for every group element, including both even-rim reflection types.

**4. Representation and quotient statements.** For odd \(n\), the sum of the \(\rho_j\)-characters is \(n-1\) at the identity, \(-1\) on every nonidentity rotation, and \(0\) on reflections. Adding \(2\varepsilon_s\) gives the stated character. For even \(n\), the sum of the two-dimensional characters is \(n-2\) at the identity and \(-1-(-1)^k\) at each nontrivial rotation \(r^k\); adding \(2\varepsilon_s+\varepsilon_r\) again gives the formula, including both kinds of reflection. Character orthogonality proves the complex decomposition. The elementary graph-cycle exact sequence gives \(\operatorname{tr}(g\mid H_1(W_{n+1};\mathbb Q))=1+\operatorname{tr}(g\mid C_1(W_{n+1}))-\operatorname{tr}(g\mid C_0(W_{n+1}))\). These traces are \(n\) at identity, \(0\) at nontrivial rotations, \(-1\) at odd-rim reflections, and \(0,-2\) at even-rim vertex-axis and edge-axis reflections, respectively. Their differences from \(\chi_n\) are exactly the sign character \(\varepsilon_s\), proving the rational-module formula. Averaging over rotations gives exactly two invariant dimensions, while averaging over \(D_n\) gives zero. An admissible barycentric subdivision of the finite cubical model lets finite-group rational homology transfer identify ordinary orbit-space homology with invariant homology. Since the model is connected and has no homology above degree one, the quotient conclusions follow.

## Verification
The standalone Python 3 standard-library program `verify.py` reconstructs the graph, all cubical cells, the mod-two boundary matrices, and every signed fixed-cell trace. For each rim length \(4\le n\le40\), it checks the exact cell counts, \(\partial_1\partial_2=0\), the full ranks of both differentials over \(\mathbb F_2\), all \(2n\) dihedral elements (1,628 group elements in total), the six symbolic trace cases, and invariant-character averages. Run `python3 verify.py` in the directory containing the source file. The recorded output is in `verification_output.txt`. These finite tests independently detect formula, orientation, and low-order mistakes but are **not** a replacement for the general argument in the proof.

## Relationship to prior work
Barnett and Farber [1] study the ordered two-particle graph configuration space and its graph-pair model, giving fundamental nonequivariant information; they do not state the wheel's complete unordered dihedral character. Harrison, Keating, Robbins, and Sawicki [2], particularly their Theorem 4, give the first-homology group for every three-connected planar graph as an abstract abelian group and use wheel graphs to prove equality of exchange phases up to sign. These results yield the **rank** here, but not the actual graph-automorphism character: determining the signs of reflections and the distinction between the two even-rim reflection classes requires an equivariant computation. Maciążek and Sawicki [4, §5.3] compute wheel configuration homology and in particular zero second homology, without providing this dihedral representation. A published study of the wheel graph's discrete-Morse complex [5] concerns a different simplicial complex; its character does not imply the character of the collision-free two-particle space. Another published two-point graph result [6] concerns exchange-sign **Borel–Moore** homology, not ordinary homology. Ko and Park [3] likewise classify the abstract first homology by graph-theoretic invariants without recording this automorphism module. The present result is an equivariant refinement, not a new nonequivariant Betti-number calculation.

## Limitations
The finding concerns exactly two unordered, collision-free points on wheels with at least four rim vertices. Its complex irreducible splitting should not be interpreted as a splitting into rank-two rational irreducibles or as an integral group-lattice decomposition. Vanishing rational homology of a quotient does not imply that its fundamental group is trivial or that it is contractible. No higher-particle theorem, integral quotient classification, or Borel-equivariant claim is asserted. A previously unpublished or unindexed equivalent character calculation remains possible; the claimed originality is relative to inspected sources, not definitive priority certification.

## References
1. Kathryn Barnett and Michael Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180v1, first public 2009-03-12, especially the discrete graph-pair model; https://arxiv.org/abs/0903.2180.
2. J. M. Harrison, J. P. Keating, J. M. Robbins, and A. Sawicki, *n-Particle Quantum Statistics on Graphs*, arXiv:1304.5781v1, first public 2013-04-21; Communications in Mathematical Physics 330 (2014), 1293–1326, especially §4.2, Lemma 1 and Theorem 4; https://doi.org/10.1007/s00220-014-2091-0.
3. Ki Hyoung Ko and Hyo Won Park, *Characteristics of Graph Braid Groups*, arXiv:1101.2648v1, first public 2011-01-13, especially Theorem 3.16 on abstract first-homology groups; https://arxiv.org/abs/1101.2648.
4. Tomasz Maciążek and Adam Sawicki, *Non-abelian Quantum Statistics on Graphs*, arXiv:1806.02846v1, first public 2018-06-07, Communications in Mathematical Physics 371 (2019), 921–973, especially §5.3; https://doi.org/10.1007/s00220-019-03583-5.
5. *Dihedral top homology of wheel discrete-Morse complexes*, published record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-dihedral-top-homology-of-wheel-discrete-morse-complexes--07726f70cc8e.
6. *Exchange-sign Borel–Moore homology of two-point graph configurations*, published record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exchange-sign-borel-moore-homology-of-two-point-graph-configurat--68e49e70a285.
