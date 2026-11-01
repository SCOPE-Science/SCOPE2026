# Sharp nonlinear volume stability for inscribed cross-polytopes

## Finding

For each integer \(n\ge2\), write \(V_n=2^n/n!\). Let \(P\) be a full-dimensional convex polytope whose vertices \(v_i^+,v_i^-\in\mathbb S^{n-1}\), indexed by \(1\le i\le n\), form the combinatorial type of the regular cross-polytope. Each pair is determined by the unique nonadjacent vertex of the corresponding vertex in the edge graph. Define the squared orthogonal matching displacement
\[
D(P)=\min_{Q\in O(n)}\sum_{i=1}^n\bigl(\|v_i^+-Qe_i\|^2+\|v_i^-+Qe_i\|^2\bigr).
\]
Then
\[
\boxed{V_n-\operatorname{vol}_n(P)\ge V_n\left[1-\left(1-\frac{D(P)}{4n}\right)^n\right].}
\]
Equality holds if and only if the half-chords \(w_i=(v_i^+-v_i^-)/2\) are mutually orthogonal and all have the same norm. This is a complete geometric equality criterion, and it permits non-antipodal vertex pairs.

The inequality is **exactly sharp at every prescribed squared displacement**
\[
0\le D<4n\left(1-\frac{2}{\sqrt5}\right).
\]
There is a one-parameter family attaining equality at each such \(D\). Consequently the optimal coefficient in \(V_n-\operatorname{vol}_n(P)\ge C_n D(P)+o(D(P))\), near the regular orbit, is \(C_n=V_n/4\). For \(n=4\), \(V_4=2/3\) and \(C_4=1/6\). The full four-dimensional profile is
\[
\frac23-\operatorname{vol}_4(P)\ge \frac23\left[1-\left(1-\frac{D(P)}{16}\right)^4\right].
\]

## Assumptions and scope

The Euclidean metric and unit sphere are fixed. The pairing consists of the unique pairs of nonadjacent vertices in the cross-polytope graph, so different choices of signed pair order are absorbed by the orthogonal minimization. All vertices have Euclidean norm one. No central symmetry, common midpoint, or regularity assumption is imposed. The inequality applies globally in this combinatorial class; exact attainability is asserted on the explicit displacement interval above, not for all possible displacements.

## Proof

**1. The signed-facet determinant identity.** A combinatorial \(n\)-cross-polytope has exactly the \(2^n\) simplicial facets with one vertex from each opposite pair. Their consistently oriented boundary coefficients, with the vertices ordered by pair index, are \(\prod_i\varepsilon_i\) up to an overall sign, for \(\varepsilon_i\in\{-1,1\}\). The signed cone-volume formula is valid even if the origin is exterior to \(P\):
\[
\operatorname{vol}_n(P)=\frac1{n!}\left|\sum_{\varepsilon\in\{-1,1\}^n}\Bigl(\prod_i\varepsilon_i\Bigr)\det(v_1^{\varepsilon_1},\dots,v_n^{\varepsilon_n})\right|.
\]
Multilinearity reduces this boundary sum to the single determinant
\[
\operatorname{vol}_n(P)=\frac1{n!}\bigl|\det(v_1^+-v_1^-,\dots,v_n^+-v_n^-)\bigr|=V_n|\det W|,
\]
where \(W=[w_1\ \cdots\ w_n]\). The orientation coefficient is inherited from the abstract cross-polytope boundary sphere, independently of the particular realization.

**2. Exact alignment formula.** Expansion of the \(2n\) unit-vector squared distances gives
\[
D(P)=4n-4\max_{Q\in O(n)}\operatorname{tr}(Q^{\mathsf T}W)=4n-4\|W\|_*,
\]
where \(\|W\|_*\) is the sum of its singular values. The last equality follows from a singular-value decomposition: \(W=U\operatorname{diag}(\sigma_i)V^{\mathsf T}\), and the trace is maximized by \(Q=UV^{\mathsf T}\). In particular \(0\le D(P)<4n\), since the determinant above is nonzero for full-dimensional \(P\).

**3. Sharp product-versus-sum inequality.** Arithmetic–geometric mean applied to the nonnegative singular values gives
\[
|\det W|=\prod_i\sigma_i\le\left(\frac1n\sum_i\sigma_i\right)^n=\left(1-\frac{D(P)}{4n}\right)^n.
\]
Combining with step 1 proves the asserted global nonlinear inequality. Equality occurs precisely when all singular values are equal, equivalently \(W=cQ\) for some \(c>0\) and \(Q\in O(n)\), which is the stated orthogonal equal-half-chord condition.

**4. Actual attainability, not merely formal matrix equality.** For a parameter \(2/\sqrt5<c\le1\), put \(s=\sqrt{1-c^2}\), so \(c>2s\). Indices are cyclic, and define
\[
v_i^\pm=s e_{i+1}\pm c e_i\qquad(1\le i\le n).
\]
All \(2n\) vertices lie on the unit sphere and \(W=cI\). It remains to check that the convex hull retains the required combinatorial type. Fix signs \(\varepsilon_i\in\{-1,1\}\). The selected points \(v_i^{\varepsilon_i}\) form a nonsingular square row matrix, since each diagonal entry has magnitude \(c>s\) and every row has just one off-diagonal entry of magnitude \(s\). Thus a unique vector \(a\) solves \(a\cdot v_i^{\varepsilon_i}=1\) for all \(i\). Its coordinates obey
\[
c\varepsilon_i a_i+s a_{i+1}=1.
\]
Writing \(T=\max_i|a_i|\), this gives \(T\le1/(c-s)\) and therefore
\[
\varepsilon_i a_i\ge\frac{c-2s}{c(c-s)}>0.
\]
Every unselected vertex lies strictly behind that hyperplane, because
\[
a\cdot v_i^{-\varepsilon_i}=1-2c\varepsilon_i a_i<1.
\]
Hence each of the \(2^n\) prescribed sign-selected simplices is an exposed facet. They constitute the closed simplicial boundary complex of the cross-polytope, so no additional facets can occur. Thus this is indeed a convex cross-polytope of the required combinatorial type.

For the family, \(D(P)=4n(1-c)\) and \(\operatorname{vol}_n(P)=V_nc^n\), proving equality at every \(D\) in the stated interval. Expansion as \(D\downarrow0\) yields
\[
V_n-\operatorname{vol}_n(P)\ge \frac{V_n}{4}D-\frac{V_n(n-1)}{32n}D^2+O_n(D^3),
\]
with equality all along the family, so the first and subsequent explicit profile coefficients are best possible in the near-orbit sense.

## Verification

The standalone script `verify.py` uses only the Python standard library. It checks in exact rational arithmetic, in dimensions \(2,3,4,5,6\), that every sign-chosen facet of the rational construction with \(c=899/901\), \(s=60/901\) is supporting and that all excluded vertices satisfy strict supporting inequalities. It also checks the exact volume, Procrustes displacement, and nonlinear profile identity. Running `python verify.py` must terminate successfully and prints a short summary. These finite checks supplement the analytic proof of every-dimensional validity; they do not certify the continuum by sampling.

## Relationship to prior work

Horváth and Lángi, *Maximum volume polytopes inscribed in the unit sphere* (arXiv:1402.6496, 2014), Corollary 3, already prove that the regular cross-polytope maximizes volume in its combinatorial class. Medgyes, *Inscribed 4-polytopes of maximal volume with seven and eight vertices* (arXiv:2610.26886v1, first public October 12, 2026), proves the regular four-dimensional cross-polytope is the unique maximizer across all eight-vertex types and bounds the other simplicial types. Neither paper claims the present exact volume-deficit profile in the squared orthogonal matching metric or its non-antipodal equality family. The matrix ingredients—the nuclear-norm trace maximization and arithmetic–geometric mean—are standard; their inequalities by themselves are not claimed as discoveries.

## Limitations

The bound applies only to polytopes with cross-polytope combinatorics, not arbitrary \(2n\)-vertex inscribed polytopes. The exact sharpness construction is established only for \(0\le D<4n(1-2/\sqrt5)\); the inequality remains valid outside this range but global best-attainability there is not asserted. The analytical proof establishes the mathematical statement, not historical priority. Searches cannot exclude equivalent historical formulations, and an independent audit has not been performed.

## References

1. Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496v3 (2014), especially Corollary 3. https://arxiv.org/html/1402.6496v3
2. C. Medgyes, *Inscribed 4-polytopes of maximal volume with seven and eight vertices*, arXiv:2610.26886v1 (first public 2026-10-12), especially Introduction and Section 2.4. https://arxiv.org/html/2610.26886v1
