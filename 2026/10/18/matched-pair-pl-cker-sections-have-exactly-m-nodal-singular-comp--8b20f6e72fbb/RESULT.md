# Matched-pair Plücker sections have exactly \(m\) nodal singular components

## Finding
For an integer \(m\ge3\), write \(V=k^{2m}=V_1\oplus\cdots\oplus V_m\), where each \(V_i\cong k^2\) has an ordered basis and \(k\) is algebraically closed of arbitrary characteristic. Consider the **scheme-theoretic** coordinate-hyperplane section
\[
X_m=\{W\in\operatorname{Gr}(2,V):p_{2i-1,2i}(W)=0\quad(1\le i\le m)\}.
\]
It is the variety of rank-two representations in which each prescribed coordinate pair is parallel or zero. The \(m\) Plücker equations form a complete intersection on the Grassmannian. The scheme \(X_m\) is integral, normal and a local complete intersection of dimension \(3m-4\), with Plücker degree
\[
\deg X_m=\frac{1}{2m-1}\binom{4m-4}{2m-2}.
\]
Its **entire reduced singular locus** is
\[
\operatorname{Sing}(X_m)_{\mathrm{red}}=\bigcup_{i=1}^m Y_i,
\qquad
Y_i=\{W\in X_m:\operatorname{pr}_{V_i}(W)=0\}.
\]
The \(m\) varieties \(Y_i\) are distinct irreducible components, and each is naturally isomorphic to \(X_{m-1}\) in \(\operatorname{Gr}(2,k^{2m-2})\). Thus every component has codimension three in \(X_m\), dimension \(3m-7\), and degree
\[
\deg Y_i=\frac{1}{2m-3}\binom{4m-8}{2m-4},\qquad
\deg\operatorname{Sing}(X_m)_{\mathrm{red}}=
\frac{m}{2m-3}\binom{4m-8}{2m-4}.
\]
For each set of indices \(S\subseteq\{1,\dots,m\}\), intersections of components obey
\[
\bigcap_{i\in S}Y_i\cong X_{m-|S|}\quad\text{if }|S|\le m-2,
\]
and are empty for \(|S|>m-2\). In these formulas the boundary case \(X_2\) is \(\mathbb P^1\times\mathbb P^1\).

At a closed point where exactly \(z\) coordinate-pair projections vanish, \(0\le z\le m-2\), the completed local ring has the **exact formal normal form**
\[
\widehat{\mathcal O}_{X_m,x}\cong
k[[t_1,\ldots,t_{3m-4-3z},a_1,b_1,c_1,d_1,\ldots,a_z,b_z,c_z,d_z]]
/(a_1d_1-b_1c_1,\ldots,a_zd_z-b_zc_z).
\]
In particular each singular component has an ordinary three-dimensional node as its generic transverse singularity; at multiple component intersections the nodes occur in independent factors. The conclusion is valid in characteristic two as well as in other characteristics.

## Assumptions and scope
The ideal is generated **inside the homogeneous coordinate ring of the Plücker Grassmannian**, not in the polynomial ring on unrestricted Plücker coordinates. All assertions are scheme-theoretic for \(X_m\) and set-theoretic/reduced-scheme assertions for \(\operatorname{Sing}(X_m)_{\mathrm{red}}\); the unreduced Jacobian singular scheme is not being identified. Coordinate-pair labels may be simultaneously relabeled, but the paired-block structure is fixed. The normal form is at closed \(k\)-points, over an algebraically closed field.

## Proof
**1. Exact affine equations.** Every rank-two \(2\times2m\) matrix representing \(W\) has two linearly independent columns. If each pair determinant vanishes, these independent columns must belong to **different** paired blocks. The open Grassmannian charts indexed by a choice of one pivot column from each of two distinct blocks therefore cover \(X_m\). After the usual invertible left row operation, the chosen pivot columns are \((1,0)^T\) and \((0,1)^T\). The second column in each pivot block is constrained by a single **linear** equation, and every other block has matrix
\[
B_j=\begin{pmatrix}a_j&c_j\\b_j&d_j\end{pmatrix},\qquad\det B_j=a_jd_j-b_jc_j=0.
\]
Consequently, **on each such full open chart**, not merely to first order,
\[
X_m\cap U\cong\mathbb A^2\times\prod_{j=1}^{m-2}
\operatorname{Spec}k[a_j,b_j,c_j,d_j]/(a_jd_j-b_jc_j).
\tag{1}
\]
This proves the local complete-intersection claim and the dimension \(2+3(m-2)=3m-4\). The equation is an irreducible hypersurface, smooth precisely away from its origin over every field.

**2. Irreducibility and normality.** Let \(B=(\mathbb P^1)^m\) parameterize one line \(L_i\subset V_i\) for each block. The incidence variety \(\operatorname{Gr}_B(2,\bigoplus_iL_i)\) is smooth and irreducible, with dimension \(m+2(m-2)=3m-4\), and its proper image equals the set underlying \(X_m\). Indeed the projection of a two-plane to each \(V_i\) has rank at most one, and one may choose \(L_i\) containing its image. Hence \(X_m\) has irreducible support. The charts (1) are reduced (each factor is geometrically integral), so \(X_m\) is integral. Each chart is Cohen–Macaulay (complete intersection), and the singular locus of a determinant factor has codimension three; by Serre's \(R_1+S_2\) criterion, every chart, hence \(X_m\), is normal. The \(m\) imposed hyperplanes have their expected codimension and form a regular sequence on the smooth Grassmannian.

**3. Complete singular classification and germs.** The Jacobian of \(a_jd_j-b_jc_j\) is \((d_j,-c_j,-b_j,a_j)\). It vanishes exactly where the full \(2\times2\) block \(B_j\) is zero, including in characteristic two. Because the determinant equations involve pairwise disjoint variables, (1) is smooth exactly when none of its nonpivot blocks is zero. Intrinsically this says \(\operatorname{pr}_{V_i}(W)\ne0\) for every \(i\). Each zero-block locus \(Y_i\) is the corresponding paired-coordinate section in the complementary \(2m-2\) coordinates, namely \(X_{m-1}\). It is irreducible by step 2 (including \(m-1=2\), when the section is the Segre quadric). There are points with only block \(i\) zero and all other blocks nonzero, so the \(Y_i\) are distinct inclusion-maximal components. For a point with \(z\) zero blocks, choose both pivot columns from nonzero blocks; every remaining nonzero rank-one block is smooth, so formal implicit-function coordinates turn its determinant equation into one smooth coordinate. Each zero block contributes the independent node \(a_id_i-b_ic_i\). Counting smooth coordinates yields \(3m-4-3z\), proving the displayed completed-local-ring isomorphism and all component intersections.

**4. Degrees.** The hyperplane equations form a regular sequence of length \(m\), so the Plücker degree of \(X_m\) equals the degree of \(\operatorname{Gr}(2,2m)\), which the two-row hook-length formula identifies with Catalan number \(\frac1{2m-1}\binom{4m-4}{2m-2}\). Each \(Y_i\) is the same construction with \(m-1\) pairs; hence its degree is the corresponding Catalan number. All \(Y_i\) have equal dimension, and their pairwise intersections have smaller dimension. The degree of their reduced union is consequently the sum of their individual degrees, giving the formula stated above. All steps are valid in every characteristic.

## Verification
The included standalone `verify_matching.py` checks the exact Plücker big-chart determinant equations by symbolic arithmetic for \(2\le m\le8\), the Catalan and singular-support degree formulas, and the predicted Jacobian rank on coordinate samples. It then exhaustively enumerates all points of the relevant Grassmannian over \(\mathbb F_2\) and \(\mathbb F_3\) for \(m=3\), and over \(\mathbb F_2\) for \(m=4\). In each case it computes the Jacobian in the full Grassmannian big cell and verifies that its rank defect is exactly the number of zero paired blocks. Executing the checker returns `VERIFY_OK`. These finite checks corroborate, but are not used in place of, the all-parameter proof above.

In particular \(X_3\) is a normal fivefold of degree \(14\), and its singular support is the disjoint union of three Segre quadrics \(\mathbb P^1\times\mathbb P^1\), of total degree \(6\).

## Relationship to prior work
The prescribed parallel-pair conditions identify a natural rank-two positroid/partition-matroid stratum. Knutson–Lam–Speyer establish **general** positroid-variety facts, notably scheme-theoretic Plücker descriptions, normality and Cohen–Macaulayness; none of those general facts is claimed as a new discovery here. Billey–Weaver and Fluegemann give **general** smoothness tests for positroid varieties at distinguished points. Mohammadi–Zaffalon and collaborators study rank-two positroid cells and their boundaries. The contribution here is the **explicit uniform complete singular-component decomposition, full formal local models, component-intersection pattern and degrees for this matched-pair family**, obtained from a transparent chart product. None of the reviewed passages explicitly supplies this combination or a theorem with a direct matching statement. General background results may in principle provide alternative deductions, and equivalent coverage in unlocated literature remains possible.

## Limitations
No independent audit has been performed. This is not a classification of arbitrary rank-two positroid varieties or of arbitrary matching-derived **other** degeneracy constructions. The theorem identifies the reduced singular locus and completed local rings of \(X_m\); it makes no assertion about embedded/nonreduced structure of the Jacobian singular scheme. The degree formula is standard Grassmannian enumerative theory applied here, not a new degree formula for the Grassmannian. The exact same result may be derivable from broader prior positroid local-geometry literature not identified in the accessible comparison.

## References
1. A. Knutson, T. Lam, D. Speyer, *Positroid varieties I: juggling and geometry*, arXiv:0903.3694 (first public 2009-03-21); related revised *Positroid varieties: juggling and geometry*, arXiv:1111.3660.
2. S. Billey and J. E. Weaver, *A pattern avoidance characterization for smoothness of positroid varieties*, arXiv:2204.09013; Séminaire Lotharingien de Combinatoire 86B.57 (2022).
3. J. Fluegemann, *Smooth points on positroid varieties*, arXiv:2407.21116 (2024).
4. F. Mohammadi and F. Zaffalon, *Computing positroid cells in the Grassmannian of lines, their boundaries and their intersections*, arXiv:2206.14001 (2022; later versions add S. Agarwala).
