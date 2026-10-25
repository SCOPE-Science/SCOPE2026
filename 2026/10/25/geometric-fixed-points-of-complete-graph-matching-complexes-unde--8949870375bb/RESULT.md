# Geometric fixed points of complete-graph matching complexes under every involution

## Finding

Let \(M_n\) be the simplicial complex whose vertices are the two-element subsets of \([n]\), and whose simplices are collections of pairwise disjoint two-element subsets. An involution \(\tau\in S_n\) with \(m\) transpositions and \(r\) fixed ground vertices (so \(n=2m+r\)) acts naturally on its geometric realization. For \(m\ge1\), its **geometric fixed-point space** is classified by

\[
|M_n|^{\langle\tau\rangle}\simeq
\begin{cases}
\text{contractible},&m\text{ odd},\\
\bigvee^{(2k)!/k!} S^{k-1},&m=2k,\ r=0\text{ or }1,\\
\text{contractible},&m=2k,\ r=2,\\
\bigvee^{(2k)!/k!}\Sigma^k|M_r|,&m=2k,\ r\ge3.
\end{cases}
\]

The homotopy equivalence is not merely a calculation of the invariant part of the ambient homology representation: it concerns the space of points actually fixed by \(\tau\). The \(m=0\) case is tautologically \(|M_r|\).

One specific consequence uses the established calculation \(\widetilde H_1(M_7;\mathbb Z)\cong\mathbb Z/3\) and \(\widetilde H_2(M_7;\mathbb Z)\cong\mathbb Z^{20}\) [1,2]. For an involution in \(S_{11}\) with two disjoint transpositions and seven fixed ground vertices, the geometric fixed space has

\[
\widetilde H_2\cong(\mathbb Z/3)^2,\qquad
\widetilde H_3\cong\mathbb Z^{40},
\]
with other reduced integral homology groups zero. This is a naturally occurring fixed-point space with torsion.

## Assumptions and scope

All complexes are finite, geometric realizations carry their usual linear simplicial actions, homotopy equivalences are of ordinary unbased spaces, and homology is integral unless specified. A contractible complex is nonempty. For \(r=0,1\), \(M_r=\{\emptyset\}\) is the void-vertex complex, which contributes the identity factor in a *simplicial join*. The symbol \(\Sigma X\) means ordinary unreduced suspension of a nonempty space \(X\); \(\Sigma^k\) denotes iteration. The wedge has the indicated number of components identified at chosen basepoints. The classification applies for all integers \(m\ge1\) and \(r\ge0\), without restrictions on the size of \(n=2m+r\) beyond these.

## Proof

**Fixed-point triangulation.** Each vertex of \(M_n\) is an edge of \(K_n\). A point in a simplex has unique nonnegative barycentric coordinates on its incident vertices. It is fixed by the involution precisely when its nonzero coordinates are constant on each orbit of graph edges, and each orbit with positive coordinate is a matching by itself. Therefore \(|M_n|^{\langle\tau\rangle}\) is canonically homeomorphic to the realization of the simplicial *orbit complex*: its vertices are graph-edge orbits whose union is a matching, and its faces are collections of orbits whose union is still a matching. The vertex mapping sends each orbit to its barycenter.

**Complete list of admissible orbits.** Label the transposed ground vertices \(i^+,i^-\) for \(1\le i\le m\). One has the singleton orbit \(L_i=\{\{i^+,i^-\}\}\), and for \(i<j\) exactly two admissible length-two orbits:

\[
E^+_{ij}=\big\{\{i^+,j^+\},\{i^-,j^-\}\big\},\qquad
E^-_{ij}=\big\{\{i^+,j^-\},\{i^-,j^+\}\big\}.
\]

Each such orbit consumes precisely the indicated one or two *whole transposition blocks*. An edge joining a transposed ground vertex to a fixed ground vertex has a two-element orbit whose two edges share that fixed vertex; hence it cannot appear in any fixed simplex. All ground edges joining two fixed vertices are singleton admissible orbits, and they form \(M_r\). Consequently, writing \(O_m\) for the simplicial complex on the \(L_i\) and \(E^\pm_{ij}\), with simplices exactly those with pairwise disjoint consumed blocks, there is an actual simplicial isomorphism

\[
\operatorname{FixOrbit}_\tau(M_n)\cong O_m*M_r.
\]

**Homotopy recurrence.** The complex \(O_1\) consists of a single vertex and is contractible. The complex \(O_2\) consists of the edge \(L_1L_2\) and the two isolated vertices \(E^+_{12},E^-_{12}\), so \(|O_2|\simeq S^0\vee S^0\). For \(m\ge3\), the subcomplex \(A=L_m*O_{m-1}\) is a cone. The remaining simplices are covered by \(2(m-1)\) cones \(E^\epsilon_{im}*O_{m-2}^{\widehat{i,m}}\), one for each \(i<m\) and sign \(\epsilon\). Here the superscript identifies the canonical copy using the blocks other than \(i,m\). Each such cone meets \(A\) exactly in its base, and any two of the newly attached cones intersect only inside \(A\), since their apex vertices both consume block \(m\). Thus \(O_m\) is a union formed by attaching these cones to a contractible simplicial subcomplex along their full bases.

Inclusion of subcomplexes is a cofibration, and collapse of the contractible subcomplex \(A\) is a homotopy equivalence. Each attached cone becomes the unreduced suspension of its base when the base is identified to the common point. Since \(O_{m-2}\) is nonempty for \(m\ge3\), this yields

\[
|O_m|\simeq\bigvee^{2(m-1)}\Sigma|O_{m-2}|\qquad(m\ge3).
\]

By the two base cases, odd \(m\) give contractible spaces. If \(m=2k\), induction yields a wedge of \(a_k\) spheres of dimension \(k-1\), where \(a_1=2\), \(a_k=2(2k-1)a_{k-1}\), and therefore \(a_k=(2k)!/k!\).

**Reassembling fixed ground vertices.** For \(r=0,1\), the abstract complexes \(M_r\) have no vertices, so the simplicial join changes nothing. For \(r=2\), \(M_2\) has a vertex and the entire join is a cone. For \(r\ge3\), \(M_r\) is nonempty. To avoid any pointed/unpointed ambiguity, apply the same cone-attachment argument *directly to the joins*: the contractible cone \(A*M_r\) is augmented by \(2(m-1)\) cones, each based along the full copy of \(O_{m-2}*M_r\). Consequently \( |O_m*M_r|\simeq\bigvee^{2(m-1)}\Sigma|O_{m-2}*M_r|\) for \(m\ge3\). At \(m=2\), the complex \(O_2*M_r\) consists of three cones on \(|M_r|\) identified along their shared base, so it is homotopy equivalent to a wedge of two copies of \(\Sigma|M_r|\). Induction using the recurrence above proves the claimed \(a_k\) copies of \(\Sigma^k|M_r|\) for even \(m=2k\). When \(m\) is odd, the join of the contractible \(O_m\) with \(M_r\) is contractible. This proves all quantified cases.

## Verification

The standalone standard-library script `verify_involution_matching.py` rebuilds the full edge-orbit complex directly from the original graph involution. It checks orbit admissibility and the complete finite simplicial boundary matrices over \(\mathbb F_2\) for fourteen independent parameter pairs; their homology agrees with the asserted wedge/suspension ranks. Further tests compute reduced Euler characteristics for \(m=5,6,7,8\), agreeing with \(0,120,0,-1680\), respectively. Running the script prints `MATCHING_INVOLUTION_FIXED_COMPLEX_VERIFIED` after all assertions succeed. These finite tests complement, but do not replace, the proof by cone attachments and cofibrations.

## Relationship to prior work

Mondal–Mukherjee–Saha [1] study ordinary matching complexes of complete graphs by discrete Morse theory, including the established integral homology of \(M_7\); their results are used only for the torsion corollary, not as a fixed-point theorem. Wachs [2] surveys \(S_n\)-homology representations of matching complexes and, in Section 8, homotopy formulas for uniformly colored multigraph matching complexes via simplicial inflations. Those are closely related techniques but concern **different simplicial complexes** from the orbit complexes above, which have one singleton edge at every paired block as well as two alternatives for every inter-block edge. None of those reviewed statements specifies the geometric fixed-point spaces here, or implies the result without identifying the orbit complex and proving the loop-augmented cone recurrence.

## Limitations

The theorem classifies the fixed-point spaces of individual order-two permutations, not fixed points of arbitrary subgroups or the full equivariant stable homotopy type. For \(r\ge3\) it expresses the answer in terms of suspensions of the ordinary matching complex \(M_r\), whose general integral homotopy type is not known; the formula does **not** claim to solve that separate problem. The torsion example relies on known integral homology [1,2]. Distinctly phrased or unindexed equivalent prior literature remains a possibility. Computations in the verifier are finite, while the unbounded statement is supported by the inductive homotopy argument.

## References

[1] A. Mondal, S. Mukherjee, K. Saha, *Discrete Morse theory and the topology of matching complexes of complete graphs*, arXiv:2303.07054, first public 13 March 2023; merged into *Topology of matching complexes of complete graphs via discrete Morse theory*, arXiv:2305.02973, https://arxiv.org/html/2305.02973v5 .

[2] M. L. Wachs, *Topology of matching, chessboard, and general bounded degree graph complexes*, Algebra Universalis 49 (2003), 345–385; author manuscript dated 2001, revised 2002, https://www.math.miami.edu/~wachs/papers/tmc.pdf , especially Sections 3, 6 and 8.
