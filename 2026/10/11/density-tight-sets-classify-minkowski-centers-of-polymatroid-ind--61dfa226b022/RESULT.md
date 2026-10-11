# Density-tight sets classify Minkowski centers of polymatroid independence polytopes

## Finding

**Theorem.** Let \(E\) be a finite nonempty set and let \(f:2^E\longrightarrow\mathbb R_{\ge0}\) be normalized, nondecreasing, and submodular:
\[
 f(\varnothing)=0,\quad f(A)\le f(B)\ (A\subseteq B),\quad
 f(A)+f(B)\ge f(A\cup B)+f(A\cap B).
\]
Assume \(w_e=f(\{e\})>0\) for every \(e\in E\), and write \(w(S)=\sum_{e\in S}w_e\). Consider the full-dimensional *independence polytope*
\[
 P_f=\bigl\{x\in\mathbb R_{\ge0}^E:x(S):=\sum_{e\in S}x_e\le f(S)\quad\text{for all }S\subseteq E\bigr\}.
\]
For a compact full-dimensional convex body \(K\), its Minkowski asymmetry and minimizing-center locus are
\[
 s(K)=\min_c\inf\{s\ge1:-(K-c)\subseteq s(K-c)\},\qquad
 \mathcal M(K)=\{c:-(K-c)\subseteq s(K)(K-c)\}.
\]
Define the *maximum singleton density*, its family of tight subsets, and the maximal tight set by
\[
 \rho=\max_{\varnothing\ne S\subseteq E}\frac{w(S)}{f(S)},\qquad
 \mathcal T=\{S\subseteq E:\rho f(S)=w(S)\},\qquad T=\bigcup_{S\in\mathcal T}S.
\]
Then \(\rho\ge1\), the family \(\mathcal T\) is closed under union and intersection (and contains the empty set), and
\[
 \boxed{s(P_f)=\rho},\qquad
 \boxed{\mathcal M(P_f)=\left\{c:\begin{array}{l}(\rho+1)c_e\ge w_e\ (e\in E),\\
 (\rho+1)c(S)\le\rho f(S)\ (S\subseteq E)\end{array}\right\}}.
\]
Every minimizing center has \(c_e=w_e/(\rho+1)\) for all \(e\in T\), while each other coordinate admits an independent small positive perturbation from the center \(w/(\rho+1)\). Precisely,
\[
 \boxed{\dim\operatorname{aff}\mathcal M(P_f)=|E\setminus T|},\qquad
 \boxed{\mathcal M(P_f)\text{ is a singleton}\iff\frac{w(E)}{f(E)}=\rho}.
\]
The entire center polytope has the following *residual submodular packing* representation. Put \(R=E\setminus T\) and, for \(S\subseteq R\),
\[
 g(S)=\rho\bigl(f(T\cup S)-f(T)\bigr)-w(S).
\]
Then \(g(\varnothing)=0\), \(g\) is submodular and \(g(S)>0\) for all nonempty \(S\subseteq R\). All centers are exactly
\[
 \boxed{\mathcal M(P_f)=\left\{\frac{w+z}{\rho+1}:
 z_e=0\ (e\in T),\quad z_e\ge0\ (e\in R),\quad z(S)\le g(S)\ (S\subseteq R)\right\}}.
\]
The residual \(g\) need not be nondecreasing; its *nonnegative packing polytope* rather than a new polymatroid independence polytope is asserted.

**Matroid specialization.** For every finite loopless matroid \(M\), take \(f=r_M\), the rank function, so that \(w_e=1\). Then
\[
 s(P_I(M))=\max_{\varnothing\ne S\subseteq E(M)}\frac{|S|}{r_M(S)}=\Upsilon_f(M),
\]
where the last equality is the **known** maximal-density/fractional-arboricity theorem, not a new statement about arboricity. The centers are unique if and only if \(M\) is uniformly dense, meaning \(|S|/r_M(S)\le|E(M)|/r_M(E(M))\) for all nonempty \(S\). Otherwise, their affine dimension is the number of elements outside the unique maximal maximum-density subset.

## Assumptions and scope

There are no integrality, representability, rationality, connectedness, or graph-theoretic hypotheses on \(f\); only finite normalized nondecreasing submodularity and positive singleton values. The condition \(w_e>0\) ensures that every nonempty set has positive capacity, that the polytope is full-dimensional, and that the displayed density ratios are defined. Loops of a matroid are excluded; they could instead be deleted before applying the statement in the intrinsic affine span. The normal form is the coordinatewise nonnegative independence polytope, *not* its base polytope \(x(E)=f(E)\).

Minkowski asymmetry is independent of the Euclidean metric. The center-space dimension is its affine dimension, not a Euclidean Hausdorff dimension. The formula determines an entire (possibly positive-dimensional) polytope, not only its center of mass or a selected center.

## Proof

**1. Exact feasibility of a proposed asymmetry factor.** Let \(s\ge1\) and \(q=(s+1)c\). By translation and positive homothety,
\[
 -(P_f-c)\subseteq s(P_f-c)\iff q-x\in sP_f\quad\text{for every }x\in P_f.
\]
Since \(0\in P_f\), necessarily \(q\in sP_f\), hence \(q(S)\le s f(S)\) for all \(S\). For each \(e\), the axis point \(w_e\mathbf e_e\) belongs to \(P_f\): every set containing \(e\) has capacity at least \(f(\{e\})=w_e\) by monotonicity. The nonnegativity of \(q-w_e\mathbf e_e\in sP_f\) therefore forces \(q_e\ge w_e\).

Conversely suppose \(q_e\ge w_e\) for all \(e\) and \(q\in sP_f\). Any \(x\in P_f\) satisfies \(0\le x_e\le w_e\), so \(q-x\ge0\). For every \(S\), since \(x(S)\ge0\),
\[
 (q-x)(S)=q(S)-x(S)\le q(S)\le s f(S),
\]
thus \(q-x\in sP_f\). We have proved, with both directions and no unmentioned assumptions,
\[
 -(P_f-c)\subseteq s(P_f-c)
 \iff q\ge w\ \text{coordinatewise and }q(S)\le s f(S)\text{ for all }S.
\]

**2. Optimal value and all centers.** From the necessary inequalities, for every nonempty \(S\),
\(w(S)\le q(S)\le s f(S)\), so \(s\ge\rho\). Since the singleton choice gives ratio one, \(\rho\ge1\). Conversely the vector \(q=w\) satisfies \(q\ge w\) and \(q(S)=w(S)\le\rho f(S)\) by definition of \(\rho\). Therefore \(s(P_f)=\rho\), realized at \(c=w/(\rho+1)\). Applying Step 1 at \(s=\rho\) gives exactly the full center inequalities in the Finding.

**3. Tight-set lattice and fixed coordinates.** Set \(h(S)=\rho f(S)-w(S)\), a nonnegative normalized submodular set function (the subtraction is modular). Whenever \(A,B\in\mathcal T\), submodularity gives
\[
 0=h(A)+h(B)\ge h(A\cup B)+h(A\cap B)\ge0.
\]
Hence both the union and intersection belong to \(\mathcal T\); by finiteness, \(T\) is tight and contains every tight set. For a minimizing center, let \(z=(\rho+1)c-w\). The exact center inequalities give \(z_e\ge0\) and \(z(S)\le h(S)\) for all subsets. As \(h(T)=0\), we get \(z(T)=0\), forcing \(z_e=0\) for each \(e\in T\).

**4. Residual formula, positivity, and affine dimension.** Let \(R=E\setminus T\). Every subset \(A\subseteq E\) has the unique decomposition \(A=S\cup U\) with \(S\subseteq R\), \(U\subseteq T\). Submodularity applied to \(S\cup U\) and \(T\), together with \(h(T)=0\), gives
\[
 h(S\cup U)+h(T)\ge h(S\cup T)+h(U),\qquad
 h(S\cup U)\ge h(S\cup T).
\]
Since \(z(U)=0\), the family of inequalities \(z(S)\le h(S\cup U)\) over all \(U\subseteq T\) is exactly equivalent to its strongest member \(z(S)\le h(S\cup T)=g(S)\). The residual representation follows. Its capacity \(g\) is a contraction of the submodular \(h\), so is submodular and normalized. If \(\varnothing\ne S\subseteq R\), then \(T\cup S\) properly contains the maximal tight set \(T\), and therefore
\(g(S)=h(T\cup S)>0\).

For finite \(R\), take
\[
 0<\varepsilon<\min_{\varnothing\ne S\subseteq R}\frac{g(S)}{|S|}.
\]
Every \(z\in[0,\varepsilon]^R\) extended by zero on \(T\) satisfies all residual inequalities, proving that the affine span contains an \(|R|\)-dimensional box. Step 3 fixed all coordinates in \(T\), proving exactly \(\dim\operatorname{aff}\mathcal M(P_f)=|R|\). In particular the center is unique iff \(R=\varnothing\), iff \(T=E\), iff \(h(E)=0\), i.e. iff \(w(E)/f(E)=\rho\).

**5. Matroids and an explicit nonunique example.** If \(f=r_M\) for a loopless matroid, \(w_e=r_M(\{e\})=1\), and the theorem identifies asymmetry with \(\max_{S\ne\varnothing}|S|/r_M(S)\). The independent-set polytope is the convex hull of independent-set indicators; by the established fractional-arboricity theorem this maximum is \(\Upsilon_f(M)\). The uniqueness criterion specializes to matroid uniform density.

For the graphic matroid of a triangle with one pendant bridge, \(|E|=4\), the triangle's three edges form the unique maximal density-tight set \(T\), and \(\rho=3/2\). All minimizing centers have triangle-edge coordinates \(2/5\); the bridge coordinate runs through the entire interval \([2/5,3/5]\). In contrast, the uniform matroid \(U_{2,4}\) has \(\rho=2\) with \(T=E\) and unique center \((1/3,1/3,1/3,1/3)\). Since all pairs are independent in \(U_{2,4}\) but no triple is, its independence complex cannot be the stable sets of any graph: it is not a graph-flag independence system. Thus the theorem has instances not covered by a stable-set-polytope result.

## Verification

The accompanying single-file Python verifier `verify.py` uses exact fractions and checks 110 seeded normalized nondecreasing submodular functions made from weighted sums of binary-representable matroid ranks and modular functions, in dimensions \(1\) through \(5\). It recomputes all density-tight subsets and their union/intersection lattice, checks the residual positive submodular capacities and uniform-density equivalence, and explicitly verifies the reflected-point inclusion inequalities for 2,348 greedy-generated polymatroid vertices at 178 proposed feasible centers. A separate graphic example checks the density \(3/2\) and exactly one free coordinate. The actual run printed:

`EXACT_VERIFY_PASS polymatroids 110 greedy_vertices_checked 2348 centers_checked 178 triangle_bridge_density 3/2 triangle_bridge_free_coordinates 1`

Execute `python3 verify.py` in a directory containing that embedded file; no external Python dependencies are needed. These finite checks are corroboration only: the infinite family follows from Steps 1--5, which use no enumeration assumptions.

## Relationship to prior work

Ferroni [1, Definitions 3.6 and 3.8] states the polymatroid submodular axioms and the independence-polytope inequalities, studying Ehrhart rather than asymmetry. The general theory of Minkowski asymmetry of convex bodies predates this work [5]. The maximum-density expression and its interpretation as fractional matroid arboricity are also established results, documented explicitly by van den Heuvel and Thomassé [2, Section 1.2, Proposition 1.7] and studied alongside principal partitions by Catlin et al. [3]. Truong and Poggi-Corradini [4] study matroid-base modulus and density profiles; their optimization is over the base polytope, not the reflected-containment center polytope above. Jochemko and Ravichandran [6] study generalized permutohedra and Minkowski-*linear* functionals, a different use of 'Minkowski'.

The asserted addition is the exact **Minkowski-asymmetry interpretation for arbitrary finite polymatroid independence polytopes**, their **complete minimizing-center polytope**, and the **maximal-density-tight residual affine-dimension/uniqueness classification**. The density maximization and the concept of tight sets are not claimed new independently. A related stable-set-polytope identity for fractional graph coloring applies to independence systems defined by forbidden edges; the rank-two uniform matroid example above shows that not every matroid independence system is such a graph stable-set system, so that identity does not imply this theorem without additional submodular reasoning. Related order-polytope asymmetry formulas concern a different realization and likewise do not imply the new claim.

## Limitations

The theorem requires finite, monotone, normalized submodularity and strictly positive singleton capacities, with all inequalities in the **independence-polytope** realization. The result gives no asymmetry formula for arbitrary affine sections, base polytopes, or polytopes with loops without first passing to their intrinsic affine span. The residual \(g\) is nonnegative and submodular but not asserted monotone. Although the proof is direct, no claim is made that general asymmetry or fractional arboricity or the principal partition are new. The earlier principal-partition paper by Catlin et al. [3] was identified through its indexed text but its full PDF was not retrievable via available lawful access, leaving some possibility of an unrecognized equivalent geometric formulation; equivalent statements under convex-corner/antiblocking terminology are also a literature risk. Scientific novelty is not independently certified.

## References

[1] Luis Ferroni, *Matroids are not Ehrhart positive*, arXiv:2105.04465 (first posted 2021-05-10; v3 inspected), Section 3, especially Definitions 3.6 and 3.8. Primary MSC 52B40, secondary 05B35 and 52B20. https://arxiv.org/abs/2105.04465

[2] Jan van den Heuvel and Stéphan Thomassé, *Cyclic Orderings and Cyclic Arboricity of Matroids*, arXiv:0912.2929 (first posted 2009-12-15), Section 1.2, Proposition 1.7. https://arxiv.org/abs/0912.2929

[3] Paul A. Catlin, Jerrold W. Grossman, Arthur M. Hobbs, and Hong-Jian Lai, *Fractional arboricity, strength, and principal partitions in graphs and matroids*, Discrete Applied Mathematics 40 (1992), 285–302, DOI:10.1016/0166-218X(92)90002-R. Public indexed copy: https://math.wvu.edu/~hlai2/Pdf/Catlin_Pdf/Catlin41.pdf (full text unavailable during comparison).

[4] Huy Truong and Pietro Poggi-Corradini, *Base Modulus for Matroid Truncation, Strength, and Fractional Arboricity*, arXiv:2604.11946 (first posted 2026-04-13), Sections 1–2. https://arxiv.org/abs/2604.11946

[5] René Brandenberg and Florian Grundbacher, *Tightening inequalities on volume-extremal k-ellipsoids using asymmetry measures*, Mathematika (2025), DOI:10.1112/mtk.70051. https://doi.org/10.1112/mtk.70051

[6] Katharina Jochemko and Mohan Ravichandran, *Generalized permutahedra: Minkowski linear functionals and Ehrhart positivity*, arXiv:1909.08448 (first posted 2019-09-18), especially Introduction and discussion of matroid polytopes. https://arxiv.org/abs/1909.08448
