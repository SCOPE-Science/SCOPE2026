# A finite-rank hub correction for wheel partial-isometry monoids

## Finding

For every integer \(n\ge5\), let \(W_n=K_1\vee C_n\) be the simple wheel with one hub and \(n\) rim vertices. Let \(\mathcal D(W_n)\) be the inverse monoid of *all* partial isometries of its shortest-path metric, including the empty map. Here a partial isometry is an injective map between arbitrary vertex subsets that preserves every pairwise ambient-graph distance. Let \(\mathcal P(C_n)\) be the inverse monoid of all isomorphisms between vertex-induced subgraphs of the rim cycle (which is generally **larger** than the metric partial-isometry monoid of the cycle). Define domain-rank polynomials
\[
R_n(z)=\sum_{\alpha\in\mathcal D(W_n)}z^{|\operatorname{dom}\alpha|},\qquad
Q_n(z)=\sum_{\beta\in\mathcal P(C_n)}z^{|\operatorname{dom}\beta|}.
\]
Then the following identity holds, with no parity restriction:
\[
\boxed{R_n(z)=(1+z)Q_n(z)+2nz+5n^2z^2+2n^2(n-1)z^3+2n^2z^4.}
\]
In particular, the partial isometries that neither avoid the hub in both domain and image nor fix the hub have the *exact* rank polynomial
\[
\boxed{E_n(z)=2nz+5n^2z^2+2n^2(n-1)z^3+2n^2z^4.}
\]
Thus hub-moving partial isometries occur only in ranks \(1,2,3,4\), and their total number is \(2n+5n^2+2n^3\).

The formula is completely explicit. For a partition \(\lambda=(1^{m_1}2^{m_2}\cdots)\vdash k\), let \(t=\sum_jm_j\) be its number of parts and put
\[
B_{n,\lambda}=\begin{cases}
\displaystyle\frac{n(t-1)!}{\prod_jm_j!}\binom{n-k-1}{t-1},&1\le t\le n-k,\\
0,&\text{otherwise},
\end{cases}\quad
A_\lambda=2^{t-m_1}\prod_jm_j!.
\]
For \(n\ge5\),
\[
\boxed{Q_n(z)=1+2nz^n+
\sum_{k=1}^{n-1}\left(\sum_{\lambda\vdash k}B_{n,\lambda}^{\,2}A_\lambda\right)z^k.}
\]
Therefore these two displayed formulas determine every coefficient of \(R_n(z)\) by integer arithmetic for all \(n\ge5\). In particular,
\[
|\mathcal D(W_n)|=2|\mathcal P(C_n)|+2n+5n^2+2n^3.
\]

## Assumptions and scope

The graph \(C_n\) has rim vertices \(1,\ldots,n\) and edges between cyclic neighbors. The hub \(0\) is adjacent to every rim vertex. Distances are those in the *entire* wheel, not distances in an induced subgraph. Domain rank means the number of points on which a partial map is defined, not the minimum size of a generating set of a monoid. A vertex-induced graph isomorphism preserves both adjacency and nonadjacency. All maps and subsets are distinctly labeled; no quotient by graph automorphism is taken.

The restriction \(n\ge5\) is essential to this statement's precise correction: the rim then has no triangles, and induced proper rim subgraphs are disjoint unions of paths. No assertion is made here about smaller wheels, arbitrary joins, or the cycle's *metric* partial-isometry monoid.

## Proof

**1. Reduction to induced graph isomorphisms.** The wheel has diameter two. For any distinct vertices, ambient distance equals one exactly for adjacent pairs and equals two otherwise. Consequently, a partial map preserves wheel distances if and only if it is a bijection between two vertex subsets that preserves adjacency and nonadjacency. Hence \(\mathcal D(W_n)=\operatorname{PAut}(W_n)\) as sets and monoids.

**2. The rim polynomial.** A proper nonempty vertex-induced subgraph of \(C_n\) is a forest of paths. Let its component sizes form \(\lambda=(1^{m_1}2^{m_2}\cdots)\), with \(k\) selected vertices and \(t\) path components. In cyclic order these paths are separated by \(t\) positive gaps with total length \(n-k\). Counting a distinguished initial path gives \(n\) choices of its initial vertex, \(t!/\prod m_j!\) distinct orders of path sizes, and \(\binom{n-k-1}{t-1}\) positive gap compositions. Every subset is counted \(t\) times, giving exactly \(B_{n,\lambda}\). Each component of size at least two has two reflections, and components of equal size can be permuted; therefore the induced forest has exactly \(A_\lambda=2^{t-m_1}\prod m_j!\) automorphisms.

If an isomorphism type \(H\) occurs on \(b\) different vertex subsets, exactly \(b^2|\operatorname{Aut}(H)|\) partial automorphisms have domain and image of type \(H\). This counts ordered domains and images, not unordered pairs. The empty map contributes one; the complete rim cycle has automorphism group of size \(2n\). Summing establishes the displayed explicit formula for \(Q_n(z)\).

**3. Two disjoint canonical families.** A wheel partial isometry can avoid the hub in both domain and image: these maps are precisely \(\mathcal P(C_n)\) because the ambient wheel metric on rim pairs records precisely adjacency in \(C_n\). Their rank polynomial is \(Q_n(z)\). Alternatively, it may contain the hub in both domain and image and fix it. Deleting the fixed hub establishes a bijection with \(\mathcal P(C_n)\), increasing the domain rank by one; the polynomial for this second, disjoint family is \(zQ_n(z)\). We count all remaining maps next, without assuming they are restrictions of whole-wheel automorphisms.

**4. Distinguishing cones.** For a rim subset \(S\), write \(H_S=C_n[S]\) and \(\widehat H_S=K_1\vee H_S\), the graph induced by \(S\cup\{0\}\). If \(|S|\ge4\), the hub has degree at least four and every rim vertex has degree at most three, so the hub is the unique possible image of itself under an isomorphism between such cones. If \(|S|=3\), the hub remains unique except when \(H_S\) is a three-vertex path, in which case \(\widehat H_S\) is the diamond \(K_4\) minus one edge and has two interchangeable universal vertices. For \(|S|=2\), the cone is a triangle when \(S\) is an edge, or a three-vertex path when the two rim vertices are nonadjacent. For \(|S|=1\), the cone is an edge; for \(|S|=0\), a singleton.

These observations exhaust cone-to-cone maps that fail to fix the hub. Exactly \(n\) rim subsets induce a singleton, \(n\) induce an edge, and \(n\) induce a three-vertex path. Relative to the counts of hub-fixing maps, the extra cone-to-cone isomorphisms are:
\[
\begin{array}{c|c|c}
\text{cone type}&\text{extra automorphisms per domain/image pair}&\text{rank-polynomial contribution}\\\hline
K_2&2-1=1&n^2z^2\\
K_3&6-2=4&4n^2z^3\\
K_4\setminus\{\text{one edge}\}&4-2=2&2n^2z^4.
\end{array}
\]
All other cone types have the hub distinguished and contribute no additional maps.

**5. Cone-to-rim maps.** Every induced rim graph has maximum degree two. Every cone on at least three rim vertices has a degree-three-or-higher hub. Thus no such cone is isomorphic to a rim-only induced graph. The possible cone/rim coincidences are exactly \(K_1\), \(K_2\), and the path \(P_3\); the triangle cone has no rim-only counterpart because \(n\ge5\). There are \(n\) rim singletons and one singleton cone, \(n\) rim edges and \(n\) edge cones, \(n\) rim induced three-vertex paths and \(\binom n2-n=n(n-3)/2\) cone paths (each from a nonadjacent rim pair). For each isomorphism type, the number of maps in either direction is twice the product of subset counts and the automorphism-group order. Therefore these cross-type maps contribute respectively
\[
2nz,\qquad 2\cdot n\cdot n\cdot2\,z^2=4n^2z^2,\qquad
2\cdot n\cdot\frac{n(n-3)}2\cdot2\,z^3=2n^2(n-3)z^3.
\]

**6. Summation and exhaustiveness.** Every map has a rim-only domain or a cone domain, and similarly for its image. Rim-to-rim, hub-fixing cone-to-cone, exceptional cone-to-cone, and cone-to-rim maps (in either direction) are mutually disjoint and exhaustive. Adding the extras from Steps 4 and 5 gives
\[
\begin{aligned}
E_n(z)&=2nz+(n^2+4n^2)z^2
 +(4n^2+2n^2(n-3))z^3+2n^2z^4\\
&=2nz+5n^2z^2+2n^2(n-1)z^3+2n^2z^4.
\end{aligned}
\]
Together with the two canonical families from Step 3 this proves the rank-polynomial identity and, on setting \(z=1\), the claimed total cardinality. In particular the exact exceptional set is supported in domain ranks at most four. \(\square\)

## Verification

The included `verify.py` uses only the Python standard library. Run `python3 verify.py` in the directory containing that file. It reconstructs the cyclic run-subset multiplicities directly for \(5\le n\le11\); exhaustively tests **all injective partial maps** of both \(C_n\) and \(W_n\) for \(n=5,6,7\), checking the actual edge/nonedge relation (equivalently the ambient wheel distances), and compares every coefficient with the two formulas. It separately counts the exceptional hub-moving maps at each rank, without using their predicted formulas for classification. Further arithmetic consistency checks cover \(8\le n\le13\).

The checked total sizes of \(\mathcal D(W_n)\) are \(957\), \(2534\), \(7737\), and \(26866\) for \(n=5,6,7,8\), respectively. The corresponding polynomials begin
\[
\begin{aligned}
R_5(z)&=1+36z+250z^2+400z^3+200z^4+60z^5+10z^6,\\
R_6(z)&=1+49z+450z^2+978z^3+672z^4+288z^5+84z^6+12z^7.
\end{aligned}
\]
The computations test finitely many parameters only; the all-\(n\) result follows from the proof above.

## Relationship to prior work

Fernandes, *On the monoid of partial isometries of a wheel graph*, arXiv:2307.16257 (first public version July 30, 2023), studies precisely \(\mathcal D(W_n)\). In particular its Lemma 1.1 establishes that a noncanonical hub interaction has rank at most four, and Theorem 2.4 describes Green's classes. Those structural findings are prior work and are **not** claimed here. The paper culminates in generating-set rank formulas (Theorem 4.4); it does not state the present domain-rank polynomial or the exact numbers of noncanonical maps in each of the four ranks.

Jajcay, Jajcayová, Szakács and Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422, establishes the general induced-subgraph inverse-monoid viewpoint and the correspondence of Green classes with induced-subgraph isomorphism classes (Proposition 3.1). The elementary \(b^2|\operatorname{Aut}(H)|\) principle is acknowledged here, not new. The new result is the explicit all-wheel polynomial identity and its universally supported correction, using a complete multiplicity analysis of the exceptional small induced subgraphs.

Fernandes and Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196, analyzes the cycle's **ambient metric** partial isometries, which are restrictions of dihedral permutations. In contrast, \(Q_n\) here counts all induced-subgraph partial graph automorphisms of the rim; these notions differ for sufficiently large cycles. The explicit run formula for \(Q_n\) is proved in Step 2 rather than inferred from the metric-cycle cardinality.

## Limitations

This theorem concerns the full metric partial-isometry monoid of the simple \(n\)-rim wheel for \(n\ge5\), and does not claim a formula for arbitrary diameter-two graphs, smaller wheels, noninjective partial homomorphisms, or induced-subgraph distance metrics. The cited prior structural theorems are acknowledged, and no claim is made that all general counting principles used are new. No independent mathematical audit or independent exhaustive publication-priority determination has been performed; a broader unlocated wheel/cone enumeration result could subsume the formula.

## References

1. V. H. Fernandes, *On the monoid of partial isometries of a wheel graph*, arXiv:2307.16257, first posted 2023-07-30; journal version, *Asian-European Journal of Mathematics* 17 (2024), 2350238. https://arxiv.org/pdf/2307.16257
2. R. Jajcay, T. Jajcayová, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422 (2018); *Journal of Algebraic Combinatorics* 53 (2021), 829–849. https://arxiv.org/pdf/1809.04422
3. V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196 (2022); *Turkish Journal of Mathematics* 47 (2023), 1746–1760. https://arxiv.org/pdf/2205.02196
