# Integral wheel forest-filtration persistence and dihedral symmetry cancellation

## Finding
For every integer \(m\ge 8\), let \(W_{m+1}=K_1*C_m\) be the wheel with rim \(\mathbb Z/m\mathbb Z\) and hub \(h\). Let \(\mathcal F_d(W_{m+1})\) consist of the vertex sets inducing a forest of maximum degree at most \(d\). The following describes **the complete reduced integral persistent homology of the restricted filtration \(d=2,3,\ldots,\infty\)**, and its degree-two dihedral symmetry.

Set \(a=\lfloor m/2\rfloor\). Define \((r,\beta)\) by
\[
(r,\beta)=\begin{cases}(q-1,2)&m=3q,\\(q-1,1)&m=3q+1,\\(q,1)&m=3q+2.\end{cases}
\]
For \(1\le j\le a\), put
\[
c_{m,j}=\frac{m}{m-j}\binom{m-j}{j},\quad
Q_{m,d}=-1+\sum_{j=1}^{d}(-1)^{j-1}c_{m,j},\quad
B_{m,d}=(-1)^{d-1}\left(Q_{m,d}-\mathbf 1_{d\ge r+2}(-1)^r\beta\right),
\]
where \(2\le d\le a\). Each \(B_{m,d}\) is a nonnegative integer. Define \(E_{m,d}=B_{m,d}-\beta\mathbf 1_{d=r+1}\).

Write \(I_{[b,e)}^{(k)}\) for the persistence module having one copy of \(\mathbb Z\) in reduced homological degree \(k\) at each integral filtration index \(d\in[b,e)\), with identity transition maps while present and zero elsewhere. Then, as a persistence module over \(\mathbb Z\),
\[
\widetilde H_*(\mathcal F_{\bullet}(W_{m+1});\mathbb Z)\big|_{d\ge2}
\cong I_{[2,\infty)}^{(m-2)}
\oplus \left(I_{[r+1,\infty)}^{(r+1)}\right)^{\oplus\beta}
\oplus\bigoplus_{d=2}^{a}\left(I_{[d,d+1)}^{(d)}\right)^{\oplus E_{m,d}}.
\]
In particular, **no integral torsion occurs at any stage**, and the only classes surviving indefinitely are one rim class and \(\beta\) cycle-independence classes. The restricted filtration is constant for \(d\ge a\). For \(2\le d\le r+1\) there is additionally a nonequivariant homotopy classification
\[
\mathcal F_d(W_{m+1})\simeq S^{m-2}\vee\bigvee^{B_{m,d}}S^d.
\]

Let \(D_m\) act on the rim by rotations \(\rho(i)=i+1\) and reflections \(\sigma_b(i)=b-i\), fixing the hub. Its rational character \(\chi_m\) on \(\widetilde H_2(\mathcal F_2(W_{m+1});\mathbb Q)\), a space of dimension \(B_{m,2}=m(m-5)/2+1\), is **exactly**
\[
\chi_m(g)=\begin{cases}
 m(m-5)/2+1,&g=1,\\
 1-m/2,&m\text{ even},\ g=\rho^{m/2},\\
 1,&g=\rho^k\ne1\text{ and }(m\text{ odd or }k\ne m/2),\\
 -(m-3)/2,&m\text{ odd},\ g=\sigma_b,\\
 1-m/2,&m\text{ even},\ g=\sigma_b,\ b\text{ even},\\
 3-m/2,&m\text{ even},\ g=\sigma_b,\ b\text{ odd}.
\end{cases}
\]
The \(D_m\)-invariants of that degree-two rational homology always vanish. Moreover,
\[
\widetilde H_k\bigl(|\mathcal F_2(W_{m+1})|/D_m;\mathbb Q\bigr)
\cong\begin{cases}
\mathbb Q,&m\equiv1\pmod 4\text{ and }k=m-2,\\
0,&\text{otherwise}.
\end{cases}
\]

## Assumptions and scope
All graphs are finite simple undirected graphs, and forest means vertex-induced acyclic subgraph. The complete integral persistence assertion begins at \(d=2\): it makes **no** statement about bars born at \(d=0\) or \(d=1\), even though those stages were studied previously. The dihedral character is for the ordinary action on rational homology, not an equivariant wedge decomposition. The quotient conclusion is rational, and makes no assertion about integral torsion in the quotient. The integer \(m\) is always at least eight; the wheel has \(m+1\) vertices.

## Proof
**1. Exact simplicial description and naturality.** Write \(K=\operatorname{Ind}(C_m)\), the complex of independent rim sets, and \(L_d=\operatorname{sk}_{d-1}K\). Any proper subset of the rim induces a disjoint union of paths, of maximum degree at most two; the full rim contains a cycle. If a forest contains the hub, it cannot contain adjacent rim vertices, since they would form a triangle with the hub. Its hub degree equals the number of selected rim vertices. Thus for every \(d\ge2\), as an equality of simplicial complexes,
\[
\mathcal F_d(W_{m+1})=\partial\Delta^{m-1}\ \cup_{L_d}\ (h*L_d).
\]
This equality respects all filtration inclusions and the \(D_m\)-action. For \(d\ge a\), the link \(L_d=K\), so the filtration stops changing.

**2. Homology reduction.** Put \(A=\partial\Delta^{m-1}\simeq S^{m-2}\). Because \(\dim L_d\le a-1<m-3\), the long exact sequence of \((\mathcal F_d,A)\), with \(\mathcal F_d/A\cong\Sigma L_d\), identifies naturally
\[
\widetilde H_{m-2}(\mathcal F_d;\mathbb Z)\cong\mathbb Z,
\quad\widetilde H_i(\mathcal F_d;\mathbb Z)\cong\widetilde H_{i-1}(L_d;\mathbb Z)\quad(1\le i\le a),
\]
and gives no other nonzero groups. The rim generator is unchanged by inclusions; all other maps are induced by the skeletal inclusions \(L_d\hookrightarrow L_{d+1}\). The dimensions are disjoint since \(a<m-2\).

**3. Skeletal chain calculation.** The established cycle-independence classification states \(K\simeq\bigvee^{\beta}S^r\), with the displayed \((r,\beta)\). There are \(c_{m,j}\) independent rim sets of size \(j\): after choosing \(j\) marked vertices with at least one unmarked vertex between consecutive marks around a cycle, cyclic gap composition gives \(\frac m{m-j}\binom{m-j}{j}\). Consequently the reduced Euler characteristic of \(L_d\) is \(Q_{m,d}\).

For each skeleton \(L_d\), the homology in degrees strictly below its top dimension \(d-1\) equals that of \(K\): the boundary maps in those degrees are already present. Thus, if \(d\le r+1\), all reduced homology below degree \(d-1\) vanishes, while if \(d\ge r+2\), the only such group is \(\mathbb Z^\beta\) in degree \(r\). Top-dimensional homology is a kernel between finitely generated free abelian groups, hence free. Euler characteristic therefore gives its rank \(B_{m,d}\). This proves every rank formula and integral torsion-freeness. For \(d\le r+1\), the skeleton is \((d-2)\)-connected by the homotopy-type theorem for \(K\) and the cellular skeletal connectivity lemma. A \((d-2)\)-connected finite \((d-1)\)-dimensional CW complex is a wedge of \((d-1)\)-spheres (including an empty wedge for the contractible case). The inclusion \(L_d\to A\) is nullhomotopic because \(\dim L_d<m-2\). The homotopy cofiber of this null map is \(A\vee\Sigma L_d\), proving the early-stage wedge claim.

**4. Integral transition maps and barcodes.** Fix an integer homological degree in the skeletal filtration. A class in the top degree \(d-1\) of \(L_d\) is killed upon including the next skeleton unless \(d=r+1\), because all reduced homology of \(K\) below degree \(r\) and above degree \(r\) is zero. Precisely at \(d=r+1\), the inclusion \(H_r(L_{r+1};\mathbb Z)\to H_r(L_{r+2};\mathbb Z)=H_r(K;\mathbb Z)\cong\mathbb Z^\beta\) is surjective: its target is obtained by adding the \((r+1)\)-cell boundary relations, and later cells have no effect on \(H_r\). The kernel is primitive because the target is free; hence the map splits as a map of free abelian groups. At all later stages this \(\mathbb Z^\beta\) is preserved. Every other top group dies at the next stage, and the rim class persists independently. Suspending the skeleton persistence by one degree yields exactly the asserted integral interval decomposition. All assertions hold for every \(m\ge8\), not merely for checked finite examples.

**5. Dihedral character and quotient.** At \(d=2\), \(L_2\) is the connected complement graph of the rim cycle. Its graph cycle space \(H_1(L_2;\mathbb Z)\) is identified, equivariantly, with \(\widetilde H_2(\mathcal F_2;\mathbb Z)\). The augmented oriented graph chain complex gives, for any \(g\in D_m\),
\[
\operatorname{tr}(g\mid H_1(L_2;\mathbb Q))
=\operatorname{tr}(g\mid C_1(L_2;\mathbb Q))
-\operatorname{tr}(g\mid C_0(L_2;\mathbb Q))+1.
\]
On oriented edges, a fixed unordered edge contributes \(+1\) if its endpoints are individually fixed and \(-1\) if they are exchanged. Nontrivial rotations fix no vertices; only the half-turn (if it exists) exchanges opposite independent pairs, yielding \(-m/2\) on \(C_1\). An odd-rim reflection fixes one vertex and exchanges \((m-3)/2\) independent pairs; an even-rim reflection through two opposite vertices fixes their connecting independent edge and exchanges \((m-2)/2\) independent pairs, while a reflection through two edges exchanges \(m/2-2\) independent pairs. This gives the six displayed character cases. Their sum over all \(2m\) dihedral elements is zero, so the invariant degree-two subspace vanishes.

The rim-sphere class transforms under a rim permutation by its sign. For even \(m\), a one-step rotation is odd, so this character is nontrivial. For odd \(m\), all rotations are even and a reflection acts by \((-1)^{(m-1)/2}\); the rim class is invariant exactly when \(m\equiv1\pmod4\). For a finite group acting simplicially, barycentric subdivision makes the cellular action admissible, and rational homology of the orbit space equals the invariant rational homology of the original complex. This proves the quotient statement.

## Verification
The standalone standard-library program `check_wheel.py` exhaustively enumerates all vertex subsets of the wheel and computes exact \(\mathbb F_2\)-chain ranks for every \(2\le d\le\lfloor m/2\rfloor\) and every \(8\le m\le12\). It independently enumerates all dihedral elements and checks the character formula. The separate program `check_persistence.py` performs full boundary-matrix persistence reduction over \(\mathbb F_2\) for \(m=8,9,10\), including transition ranks. Both programs passed, and their complete outputs are included. These finite verifications corroborate, but do not substitute for, the proof above. Integral freeness and infinite parameter coverage follow from the skeletal chain argument, not from modular experiments.

For example, \(m=10\) yields the intervals \(26\) in degree two on \([2,3)\), \(23\) in degree three on \([3,4)\), \(2\) in degree four on \([4,5)\), one in degree three on \([3,\infty)\), and one in degree eight on \([2,\infty)\). The diagram is the same over every field.

## Relationship to prior work
Carnero Bravo introduced the maximum-degree induced-forest filtration and, in the wheel proposition of *The Forest Filtration of a Graph*, gave the first-degree stage and the stabilized high-degree homotopy type for \(d\ge\lfloor m/2\rfloor\). The source's general hub-join lemma already gives the underlying cone attachment; that lemma is **not** claimed here as new. Kozlov's cycle-independence homotopy classification, recalled in the same source, supplies the input \((r,\beta)\). The present contribution is the all-stage **integral persistence and inclusion-map classification for \(d\ge2\)**, the omitted intermediate stage wedge types in the specified range, the complete degree-two dihedral character, and the rational quotient consequence. Neither static stabilized homotopy groups nor the known cone decomposition alone reports these explicit maps and symmetry cancellations. Comparison searches found no published equivalent theorem or dominating character/barcode statement; an unindexed equivalent derivation remains possible.

## Limitations
No assertion is made about interval decompositions involving the \(d=0,1\) stages, the full equivariant homotopy type, homotopy types for every degree after the early wedge range, integral homology of the orbit quotient, or non-wheel graph families. The literature search may miss unpublished or unindexed equivalent calculations. The result has not undergone independent mathematical audit.

## References
1. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271 (first public version July 25, 2023), particularly the induced-forest definition, hub-join lemma, and wheel proposition. https://arxiv.org/abs/2307.13271
2. D. N. Kozlov, *Complexes of Directed Trees*, Journal of Combinatorial Theory, Series A 88 (1999), 112–122, DOI:10.1006/jcta.1999.2984. The cycle independence homotopy theorem is reproduced in reference 1.
3. M. Berghoff, *On the Homology of Independence Complexes*, Combinatorial Theory 2(1) (2022), DOI:10.5070/C62156880 (context for cycle independence complexes and their homology).
