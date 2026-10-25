# Twisted incidence-cycle homology in projective-plane Vietoris–Rips filtrations

## Finding
Let \(\Pi\) be a finite projective plane of order \(q\ge2\), let \(\Gamma\) be its point–line incidence graph with the unweighted shortest-path metric, and let \(K_r=\operatorname{VR}_{\le r}(V(\Gamma))\). The full graph automorphism group \(G=\operatorname{Aut}(\Gamma)\) either preserves or exchanges its point and line classes. Let \(\varepsilon:G\to\{\pm1\}\) be the class-exchange sign. Give each flag (incidence edge) the orientation point-to-line, and let \(Z_1(\Gamma;\mathbb Z)=\ker[\partial:\mathbb Z^{E(\Gamma)}\to\mathbb Z^{V(\Gamma)}]\) be the integral cycle lattice with its natural oriented-edge action.

There are **natural integral \(G\)-module isomorphisms**
\[
H_1(K_1;\mathbb Z)\cong Z_1(\Gamma;\mathbb Z),\qquad
\widetilde H_2(K_2;\mathbb Z)\cong\varepsilon\otimes_{\mathbb Z} Z_1(\Gamma;\mathbb Z).
\]
Both groups are free of rank \(q^3\). In degrees other than those displayed, positive-dimensional homology vanishes at these respective scales. Equivalently, \(H_2(K_2;\mathbb Z)\) is the integral flag-cycle lattice with **unsigned** permutation of flags by every automorphism; the sign introduced by a point–line exchange cancels the ordinary orientation reversal of graph edges.

Write \(F(g)\) for the number of incidence edges fixed *setwise* by \(g\), and \(V(g)\) for the number of fixed incidence-graph vertices. For the rational trace \(\chi_2(g)\) on \(\widetilde H_2(K_2;\mathbb Q)\),
\[
\chi_2(g)=\begin{cases}
F(g)-V(g)+1,&g\text{ preserves the two classes},\\
F(g)-1,&g\text{ exchanges them}.
\end{cases}
\]
At scale one the trace in degree one is \(\chi_1(g)=\varepsilon(g)\chi_2(g)\). Thus the two consecutive homology groups have equal ranks and agree on every point–line-preserving symmetry, but **differ by a sign on every duality**.

For the Fano plane, \(G\) has order \(336\). The complete character of its eight-dimensional scale-two homology is as follows; the last column is \(\chi_2\):

| Part action | Element order | Number of elements | Trace |
|---|---:|---:|---:|
| Preserves | 1 | 1 | 8 |
| Preserves | 2 | 21 | 0 |
| Preserves | 3 | 56 | -1 |
| Preserves | 4 | 42 | 0 |
| Preserves | 7 | 48 | 1 |
| Exchanges | 2 | 28 | 2 |
| Exchanges | 6 | 56 | -1 |
| Exchanges | 8 | 84 | 0 |

Its character has squared norm \(1\), hence the rational representation is absolutely irreducible, and its fixed subspace under the full group is zero. The polarity induced by the ordinary dot product on \(\mathbb F_2^3\) has trace \(-2\) on \(H_1(K_1;\mathbb Q)\) and \(+2\) on \(H_2(K_2;\mathbb Q)\). Moreover, this eight-dimensional scale-two representation is rationally isomorphic to the irreducible constituent denoted \(W\) in the published full-automorphism classification of the **different** simplicial matching complex of the Heawood graph: their complete eight-type character tables agree. No canonical cross-complex map is asserted.

## Assumptions and scope
A finite projective plane of order \(q\) has \(N=q^2+q+1\) points and equally many lines, exactly \(q+1\) flags at each point and each line, and unique connecting lines and intersection points. This includes every existing finite plane, not only Desarguesian ones; no plane existence at unestablished orders is assumed. \(\Gamma\) is the bipartite graph on points and lines, with one edge for each incident pair. Its graph-distance Vietoris–Rips complex includes any vertex subset of pairwise distance at most the indicated real scale, inclusive at the boundary. The action is the full graph automorphism action, including any dualities actually possessed by the plane. The Fano computation concerns the unique plane of order two and its entire \(336\)-element graph automorphism group.

## Proof
**1. Metric and clique classification.** Two distinct points of \(\Pi\) are at graph distance two via their unique joining line. The dual statement holds for lines. An incident point and line are at distance one, and a nonincident point and line are at distance three. Therefore \(K_1=\Gamma\), while \(K_2\) consists of all subsets of points, all subsets of lines, and mixed simplices in which every selected point is incident to every selected line. No mixed simplex can have two distinct points and two distinct lines, because two points have only one common line.

**2. Contractible two-piece cover.** Let \(U\) be the simplex on the entire point set together with the simplices \(\{\ell\}\cup P(\ell)\), one for each line \(\ell\); here \(P(\ell)\) is the set of points on \(\ell\). Dually let \(V\) be the simplex on all lines together with the simplices \(\{p\}\cup L(p)\). Then \(K_2=U\cup V\), and \(U\cap V=\Gamma\) exactly. A line vertex occurs in only one maximal simplex of \(U\); its link there is the simplex on \(P(\ell)\), so it can be eliminated by an elementary dominated-vertex collapse. Eliminating all line vertices collapses \(U\) to the point simplex, hence \(U\) is contractible. Dually \(V\) is contractible. This argument uses no choice of coordinates.

**3. Integral and equivariant Mayer–Vietoris.** Since the cover is simplicial, there is an exact sequence of chain complexes
\[
0\longrightarrow C_*(\Gamma)
\xrightarrow{\;(i_U,-i_V)\;}
C_*(U)\oplus C_*(V)
\xrightarrow{\;\,+\,\;}
C_*(K_2)\longrightarrow0.
\]
Its connecting homomorphism is an integral isomorphism \(\delta:\widetilde H_2(K_2;\mathbb Z)\xrightarrow{\sim}H_1(\Gamma;\mathbb Z)\), because both \(U\) and \(V\) are contractible. A graph automorphism preserving the two classes preserves the ordered cover and commutes with \(\delta\). An automorphism exchanging the classes exchanges the two cover summands, carrying \((a,-a)\) to \((-ga,ga)\); hence \(\delta\circ g_*=-g_*\circ\delta\) for such an automorphism. This proves the \(\varepsilon\)-twisted integral module isomorphism, not only equality of Betti numbers. The first-scale identification is immediate from \(K_1=\Gamma\). The cycle rank is
\[
|E(\Gamma)|-|V(\Gamma)|+1
=(q+1)N-2N+1=q^3.
\]
All remaining positive homology at the two scales vanishes by the graph and Mayer–Vietoris chain calculations.

**4. Explicit character.** Orient every flag edge from point to line. On the graph chain groups, the usual cellular Lefschetz identity reads
\[\chi_{H_1(\Gamma)}(g)=\operatorname{tr}(g\mid C_1)-\operatorname{tr}(g\mid C_0)+1.\]
For class-preserving \(g\), the two chain traces are \(F(g)\) and \(V(g)\). For class-exchanging \(g\), no vertex is fixed, and any setwise-fixed incidence edge has its orientation reversed, so the chain traces are \(-F(g)\) and zero. Multiplication by \(\varepsilon(g)\) yields the claimed formula at scale two. This formula applies to all collineations and dualities, including dualities of order greater than two.

**5. Complete Fano calculation and irreducibility.** Identify both Fano points and line normals with the seven nonzero vectors in \(\mathbb F_2^3\), with incidence \(p\cdot\ell=0\). Every invertible \(3\times3\) binary matrix acts on points by \(p\mapsto Ap\) and on lines by \(\ell\mapsto(A^{-1})^T\ell\); there are exactly \(168\) such transformations. The polarity interchanging a point \(p\) with line normal \(p\) yields the second coset, giving all \(336\) automorphisms. Enumerating the \(7^3\) potential ordered nonzero matrix columns and keeping the invertible triples gives a complete elementary group enumeration. Counting fixed vertices and oriented incidence edges by the preceding formula produces the eight rows displayed above. Their weighted squared character sum is \(336\), and their weighted ordinary sum is zero:
\[
\frac1{336}\sum_{g\in G}\chi_2(g)^2=1,
\qquad \frac1{336}\sum_{g\in G}\chi_2(g)=0.
\]
Consequently the complex rational character is irreducible (in fact absolutely irreducible) and contains no trivial constituent. The polarity has exactly three setwise-fixed flags, yielding its scale-two trace \(3-1=2\); the scale-one trace is the negative.

**6. Representation bridge.** The published Heawood matching-complex classification gives a distinct eight-dimensional irreducible constituent \(W\) with character values, in precisely the same eight group types, \((8,0,-1,0,1,2,-1,0)\). Equality of character values on all conjugacy types over characteristic zero implies \(\widetilde H_2(K_2;\mathbb Q)\cong_G W\). This is a rational module isomorphism, not an integral comparison of the two simplicial complexes.

## Verification
The included standard-library executable `verify_fano_rips.py` constructs all \(331\) nonempty faces of \(K_2\) directly from the incidence relation, verifies the \(14\)-vertex Fano projective-plane axioms, and computes the six nontrivial mod-two boundary ranks \((13,50,54,30,12,2)\), giving Betti ranks \((1,0,8,0,0,0,0)\). It enumerates every one of the \(336\) graph automorphisms from all invertible binary matrices and the dot-product polarity. For each automorphism it independently compares (i) the signed fixed-simplex Lefschetz trace with (ii) the twisted graph-chain trace from the theorem. It checks all eight group-type counts, both group character norms, zero full-group invariant multiplicity, and the polarity signs. Run `python3 verify_fano_rips.py`. Successful execution prints `FANO_RIPS_EQUIVARIANT_CHECKS_OK` followed by counts. A second standalone `verify_matching_bridge.py` independently enumerates the published matching-complex chain complex, checks its full mod-two boundary ranks and all \(336\) matching-character Lefschetz sums, constructs its eight Sylow-seven subgroups, and verifies element by element that the residual character \(W\) agrees with the new Rips character. Run `python3 verify_matching_bridge.py`; successful execution prints `HEAWOOD_RIPS_MATCHING_CHARACTER_BRIDGE_OK`. Both programs are independent calculations supporting only the finite Fano specialization; the theorem for arbitrary finite planes follows from the structural proof, not finite testing.

## Relationship to prior work
Adams and Coskunuzer (first public 2021-03-11) study geometric and persistent homology of graph powers; their general lifetime bounds do not calculate an equivariant plane-incidence cycle lattice. A published exact scale-two Rips computation for finite projective-plane incidence graphs establishes the **nonequivariant** suspension and rank \(q^3\) but contains no point–line-exchange module isomorphism, no duality character and no Fano full-automorphism character table. Thus its existing sphere count is acknowledged and not claimed here.

A separate published Heawood matching-complex report gives \(\widetilde H_4(\mathcal M(\Gamma);\mathbb Q)\cong\mathbf1\oplus T\oplus W\) and an eight-class table for \(W\). Its complex is defined on *edges* and has homology in degree four, whereas the scale-two graph-metric Rips complex here is defined on *vertices* and has homology in degree two. That matching result does not imply the Rips character or the general integral duality-twist theorem; the newly established comparison is equality of the complete rational characters. Related graph-power persistence bounds by Parks and Marchette likewise do not determine symmetry representations.

## Limitations
No new claim is made about the nonequivariant sphere-wedge classification of the projective-plane scale-two Rips complex. The theorem computes integral homology **modules**, not an integral equivariant wedge decomposition or an equivariant homotopy equivalence. Equality with the matching-complex constituent \(W\) is over \(\mathbb Q\) only and does not assert a canonical geometric map or integral lattice isomorphism between the different complexes. The Fano eight-row enumeration is complete only for order two; the general theorem gives a formula requiring fixed-flag and fixed-vertex information for whatever finite plane and symmetries are at hand. Unindexed equivariant incidence-geometry literature remains an originality risk; failed searches do not certify universal novelty.

## References
1. Adams, H.; Coskunuzer, B. *Geometric Approaches on Persistent Homology*. arXiv:2103.06408 (first public 2021-03-11); especially Sections 2.2 and 4. MSC2020 55N31, 55U10.
2. *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*. Public report (2026-10-04), https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3/RESULT.md .
3. *Full Aut(H)-module of the Heawood matching complex*. Public report (2026-10-11), https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-full-operatorname-aut-h-module-of-the-heawood-matching-complex--d7a042784870/RESULT.md .
4. Parks, A. D.; Marchette, D. J. *Persistent homology in graph power filtrations*. Royal Society Open Science 3 (2016), 160228. DOI: 10.1098/rsos.160228 (background only).
