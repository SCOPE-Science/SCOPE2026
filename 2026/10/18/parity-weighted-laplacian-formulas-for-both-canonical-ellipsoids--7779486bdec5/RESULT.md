# Parity-weighted Laplacian formulas for both canonical ellipsoids of cactus symmetric edge polytopes

## Finding

**Theorem.** Let \(G=(V,E)\) be a connected finite simple cactus graph with \(|E|\geq1\): each edge belongs to at most one simple cycle. Put \(n=|V|\) and \(d=n-1\). For each unoriented edge \(e=\{u,v\}\), choose either incidence vector \(b_e=\mathbf e_v-\mathbf e_u\). The choices of orientations do not affect the answers. In the Euclidean subspace
\[
H=\{x\in\mathbb R^V:\textstyle\sum_{v\in V}x_v=0\},
\qquad P_G=\operatorname{conv}\{\pm b_e:e\in E\},
\]
consider the unique maximum-volume inscribed (John) ellipsoid and unique minimum-volume enclosing (Löwner) ellipsoid. Both centers are zero. Write \(B\) for the bridges and \(\mathcal C\) for the cycles; distinct cycles have disjoint edge sets. For \(C\in\mathcal C\), put \(\ell_C=|E(C)|\) and
\[
k_C=\begin{cases}\ell_C,&\ell_C\text{ even},\\\ell_C-1,&\ell_C\text{ odd}.\end{cases}
\]
Define the positive-definite-on-\(H\) shape matrices
\[
\boxed{\displaystyle
\Sigma_J=\frac1d\sum_{e\in B}b_eb_e^{\mathsf T}+
\sum_{C\in\mathcal C}\frac{\ell_C-1}{d k_C}\sum_{e\in C}b_eb_e^{\mathsf T},}
\]
\[
\boxed{\displaystyle
\Sigma_L=\sum_{e\in B}b_eb_e^{\mathsf T}+
\sum_{C\in\mathcal C}\frac{\ell_C-1}{\ell_C}\sum_{e\in C}b_eb_e^{\mathsf T}.}
\]
For either shape \(\Sigma\), its ellipsoid is \(\mathcal E_\Sigma=\{x\in H:x^{\mathsf T}(\Sigma|_H)^{-1}x\le1\}\). The following conclusions hold simultaneously.

1. **Exact contacts:** Every facet-supporting hyperplane of \(P_G\) touches \(\mathcal E_{\Sigma_J}\) at a point in the facet, and every vertex \(\pm b_e\) touches \(\mathcal E_{\Sigma_L}\). There are no other Löwner boundary points of \(P_G\).
2. **Exact volume ratio:**
\[
\boxed{\displaystyle\frac{\operatorname{Vol}_d(\mathcal E_{\Sigma_L})}{\operatorname{Vol}_d(\mathcal E_{\Sigma_J})}
=d^{d/2}\prod_{C\in\mathcal C}\left(\frac{k_C}{\ell_C}\right)^{(\ell_C-1)/2}.}
\]
3. **Homothety classification:** The John and Löwner ellipsoids are homothetic if and only if either (a) every cycle is even, with any number of bridges permitted; or (b) there are no bridges and all cycles are odd and have one common length. A graph with an odd cycle and a bridge, or with cycles of unequal parity, never has homothetic canonical ellipsoids.
4. **Facet enumeration:** The number of facets of \(P_G\) is
\[
2^{|B|}\prod_{\substack{C\in\mathcal C\\\ell_C\,\mathrm{even}}}\binom{\ell_C}{\ell_C/2}
\prod_{\substack{C\in\mathcal C\\\ell_C\,\mathrm{odd}}}
\ell_C\binom{\ell_C-1}{(\ell_C-1)/2}.
\]
This enumeration is included to specify the scope of the facet-contact assertion; the metric ellipsoid classification and parity-dependent homothety criterion are the main new claims.

## Assumptions and scope

All graphs are simple, finite, connected, and have at least one edge. A cactus is permitted to have bridges, articulation vertices, cycles of different lengths, or just one edge. The dimension \(d\) is the intrinsic dimension in the zero-sum hyperplane, not the ambient dimension \(n\). Euclidean volumes and shape operators are calculated in the standard vertex-coordinate inner product restricted to \(H\); no choice of graph orientation or labeling enters either invariant. Both matrices annihilate the all-ones vector and are positive definite after restriction to \(H\). An empty product equals \(1\). The displayed formulas are exact, and involve neither generic-position assumptions nor numerical limits.

For an explicit absolute volume, let \(w_e\) denote the coefficient of \(b_eb_e^{\mathsf T}\) in either shape matrix. If \(\omega_d\) is the Euclidean volume of the unit \(d\)-ball, then the weighted matrix-tree identity yields
\[
\operatorname{Vol}_d(\mathcal E_\Sigma)=\omega_d
\sqrt{\,n\left(\prod_{e\in B}w_e\right)
\prod_{C\in\mathcal C}\ell_C\,w_C^{\ell_C-1}},
\]
where all edges of each cycle \(C\) share the weight \(w_C\). This also gives exact individual volumes and specializes correctly to a tree and to an isolated cycle.

## Proof

**1. Orthogonal abstract model.** Direct each cycle cyclically, adjusting signs of its edge generators. Let \(H_\ell=\{z\in\mathbb R^\ell:\sum_i z_i=0\}\), and \(u_i=\mathbf e_i-\mathbf1/\ell\in H_\ell\). For each bridge introduce a unit coordinate \(f_e\). Set
\[
W=\bigoplus_{C\in\mathcal C}H_{\ell_C}\ \oplus\ \mathbb R^{|B|}.
\]
The linear map \(T:W\to H\) taking \(u_i\) in the cycle indexed by \(C\) to the corresponding oriented incidence vector \(b_e\), and each \(f_e\) to its bridge incidence vector, is a linear isomorphism. Indeed, the incidence map's cycle space has one independent relation for each cactus cycle, with disjoint edge supports; on \(H_{\ell_C}\) the unique cyclic sum relation has already been factored out. Thus its dimension and rank both equal \(d=\sum_C(\ell_C-1)+|B|\). Consequently,
\[
T^{-1}(P_G)=\operatorname{conv}\left(\bigcup_C\{\pm u_i:i\in C\}\ \cup\ \{\pm f_e:e\in B\}\right),
\]
a centrally symmetric free sum of cycle factors and line-segment factors.

**2. Exact polar vertices.** The polar in \(W\) is the Cartesian product of the cube sections
\[
Q_\ell=\{y\in H_\ell:|y_i|\le1\}\qquad (C\text{ of length }\ell)
\]
and one interval \([-1,1]\) for each bridge. Every vertex of \(Q_\ell\) has at least \(\ell-1\) saturated coordinate constraints. For even \(\ell\), zero sum requires precisely \(\ell/2\) entries \(+1\) and \(\ell/2\) entries \(-1\), so every vertex has squared norm \(\ell\). For odd \(\ell\), exactly one coordinate vanishes and the others split evenly into \(+1\) and \(-1\); its squared norm is \(\ell-1\). These are all the vertices because the displayed active constraints have rank \(\ell-1\) in \(H_\ell\). Thus the cycle squared norms are the constants \(k_C\). Cartesian-product vertices independently choose one such cycle vertex and one sign for each bridge. This proves the stated facet count because vertices of the polar correspond to facets of the full-dimensional original polytope.

**3. The inscribed extremal ellipsoid.** The John ellipsoid exists and is unique. The product of independent sign-inversions of the component subspaces fixes the polar and original bodies; invariance and uniqueness force the extremal center to be zero and all cross-block shape terms to vanish. Permutations of the \(\ell\) coordinates within each cycle preserve \(\{\pm u_i\}\); their action on the zero-sum representation \(H_\ell\) has only scalar invariant symmetric operators. Likewise, bridge sign changes force diagonal bridge covariance. Therefore any John shape in \(W\) has scalar cycle blocks \(a_C I_{H_{\ell_C}}\) and individual bridge variances \(t_e>0\).

The ellipsoid \(\mathcal E_\Sigma\) lies in the original body exactly when its support function obeys \(y^{\mathsf T}\Sigma y\le1\) for all polar vertices \(y\). By Step 2 this is a **single exact inequality**:
\[
\sum_{C\in\mathcal C}k_Ca_C+\sum_{e\in B}t_e\le1.
\]
Maximizing ellipsoid volume amounts to maximizing
\[
\sum_{C\in\mathcal C}(\ell_C-1)\log a_C+\sum_{e\in B}\log t_e
\]
subject to that inequality. Its strictly concave optimum is interior in every positive coordinate and saturates the bound. A Lagrange multiplier gives \(a_C=(\ell_C-1)/(d k_C)\), \(t_e=1/d\), since the sum of the dimensions of the components equals \(d\). It follows directly from the single-inequality representation that **every** polar vertex has \(y^{\mathsf T}\Sigma_J y=1\), hence every corresponding facet is supporting and tangent. For a polar vertex \(y\), the tangent point is \(\Sigma_Jy\) in abstract coordinates, pushed forward by \(T\), and the equality of the unique supporting hyperplane ensures it belongs to that facet. (Under \(T\), the polar covector transforms contragrediently.)

**4. The enclosing extremal ellipsoid.** The same uniqueness and symmetries force scalar blocks in the centered Löwner shape. Its containment of \(\pm u_i\) is equivalent to \(\|u_i\|^2/a_C=(\ell_C-1)/(\ell_Ca_C)\le1\), while containment of \(\pm f_e\) is \(1/t_e\le1\). These independent inequalities say \(a_C\ge(\ell_C-1)/\ell_C\) and \(t_e\ge1\). The determinant strictly increases in every block variable, so every lower bound is attained. Accordingly all generating vertices are on the ellipsoid. Distinct generating vertices are genuine vertices, since each has the same Euclidean norm within its cycle factor and the free-sum construction preserves vertices. Strict convexity of the ellipsoid means a nonvertex convex combination of distinct generators lies in its interior.

**5. Return to vertex coordinates and evaluate volumes.** The identity
\[
\sum_{i=1}^\ell u_iu_i^{\mathsf T}=I_{H_\ell}
\]
shows that transporting the abstract covariance by \(T\) replaces \(a_C I_{H_{\ell_C}}\) with \(a_C\sum_{e\in C}b_eb_e^{\mathsf T}\), and \(t_e f_ef_e^{\mathsf T}\) with \(t_eb_eb_e^{\mathsf T}\). This proves both displayed parity-weighted Laplacian formulas. An invertible linear transformation scales both ellipsoid volumes by the same factor, so the ratio is the square root of the determinant ratio of their abstract block matrices. The bridge blocks contribute \(d^{1/2}\) each; a cycle block contributes \([d k_C/\ell_C]^{(\ell_C-1)/2}\). Multiplication gives the formula. For absolute volume, the weighted Laplacian nonzero-eigenvalue product is \(n\) times its weighted spanning-tree sum. In a cactus every spanning tree contains all bridges and deletes exactly one edge of each cycle; with constant cycle weights this sum factors as stated.

**6. Characterize homothety.** Homothetic centered ellipsoids have proportional shape matrices. Pulling back under \(T\), the ratio of Löwner to John block variances equals \(d\) for every bridge and every even cycle, and \(d(\ell_C-1)/\ell_C\) for an odd cycle. Since \((\ell-1)/\ell\) is strictly increasing with odd \(\ell\), all ratios are identical precisely in the two listed cases. This completes the proof.

## Verification

The accompanying stand-alone, standard-library-only program `verify.py` uses exact `fractions.Fraction` arithmetic. It builds and checks \(61\) connected cactus instances (trees; cycles of lengths \(3\) through \(8\), with and without bridges; and multiply-cyclic mixed-parity cacti). In these instances it enumerates \(26{,}006\) polar vertices/facet-supporting normals, checks the exact John identity \(y^{\mathsf T}\Sigma_Jy=1\) for every one, and checks the active-edge incidence rank \(d\). It also checks the exact Löwner contact identity \(b_e^{\mathsf T}(\Sigma_L|_H)^{-1}b_e=1\) for \(998\) signed generating vertices, and reconstructs consistent graph potentials for all polar corners. Command: `python3 verify.py`; expected final line: `VERIFY_OK cases 61 facet_contacts 26006 vertex_contacts 998`. The argument above, not the finite tests, establishes the theorem for all cactus graphs.

## Relationship to prior work

D’Alì, Juhnke-Kubitzke and Koch (2023), *On a generalization of symmetric edge polytopes to regular matroids*, establishes symmetric-edge-polytope definitions, polar/facet frameworks, and matroidal structure; its original July 10, 2023 preprint is the dated primary source. D’Alì, Delucchi and Michałek (2019), *Many faces of symmetric edge polytopes*, studies facet combinatorics, joins and graph structure, not the claimed pair of canonical metric ellipsoids. Chen, Davis and Korchevskaia (2021), *Facets and facet subgraphs of symmetric edge polytopes*, gives a facet-subgraph account, without this John/Löwner determination. Ivanov (2017), *On the volume of the John–Löwner ellipsoid*, supplies general ellipsoid methods and bounds, but does not state the parity-weighted cactus Laplacian identities or simultaneous complete contact classification. These sources are ingredients and neighboring results, not priority proofs of absence. An earlier equivalent theorem under graphical optimal-design, cube-section, or convex-body terminology remains possible.

## Limitations

The theorem is restricted to connected cactus graphs; overlapping cycles introduce coupled incidence relations, and the product-of-cube-sections polar reduction need not hold. It is not a classification for all graphs, arbitrary weighted edge-root configurations, or an assertion about affine center uniqueness beyond the established canonical ellipsoids. The exact facet enumeration is a structural aid and should not be read as a new combinatorial enumeration. The numerical verification is finite and does not replace the symbolic all-dimensions proof. No independently performed mathematical audit or definitive publication-priority determination is claimed.

## References

1. A. D’Alì, M. Juhnke-Kubitzke and M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933, first version publicly posted 2023-07-10, https://arxiv.org/abs/2307.04933.
2. A. D’Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, original 2019 preprint; final publication in *Journal of Combinatorics* (2022), DOI:10.37236/10387.
3. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, 2021, https://arxiv.org/abs/2107.12315.
4. G. Ivanov, *On the volume of the John–Löwner ellipsoid*, arXiv:1707.04442, 2017, https://arxiv.org/abs/1707.04442.
