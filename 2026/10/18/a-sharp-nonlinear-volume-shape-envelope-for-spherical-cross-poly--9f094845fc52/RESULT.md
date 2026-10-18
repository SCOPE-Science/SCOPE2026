# A sharp nonlinear volume–shape envelope for spherical cross-polytopes

## Finding
For every integer \(d\ge2\) and every labelled inscribed combinatorial cross-polytope specified below, define the squared orthogonal vertex discrepancy \(\Delta^2\). The exact dimension-dependent envelope is
\[
\boxed{\operatorname{Vol}_d(P)\le\frac{2^d}{d!}\left(1-\frac{\Delta^2}{4d}\right)^d.}
\]
Equality is characterized by the opposite half-chord matrix being a positive scalar multiple of an orthogonal matrix. The bound is genuinely sharp on a nonzero interval of discrepancies in every dimension, and its optimal quadratic deficit coefficient at the regular cross-polytope is \(2^{d-2}/d!\).

## Assumptions and scope
Let \(d\ge2\). Let \(P\subset\mathbb R^d\) be a full-dimensional convex polytope combinatorially equivalent to the regular \(d\)-cross-polytope, with exactly \(2d\) distinct vertices \(p_{i,+},p_{i,-}\in S^{d-1}\), indexed so that each pair \(p_{i,+},p_{i,-}\) consists of *nonadjacent* vertices. Thus every facet is the simplex spanned by exactly one point from each pair. Define
\[
 a_i=(p_{i,+}-p_{i,-})/2,\qquad A=[a_1\ \cdots\ a_d],\qquad V_0=2^d/d!.
\]
Use the labelled orthogonal Procrustes discrepancy
\[
 \Delta(P)^2=\min_{U\in O(d)}\sum_{i=1}^d\big(\|p_{i,+}-Ue_i\|_2^2+\|p_{i,-}+Ue_i\|_2^2\big).
\]
The orthogonal group includes reflections; the vertex labels and the opposite pairing are fixed in this minimization. No central symmetry of \(P\) is assumed. The small-discrepancy sharpness statement includes noncentrally symmetric polytope examples.

## Proof
**1. Exact volume identity.** The boundary facets are indexed by sign vectors \(\sigma\in\{-1,+1\}^d\). Give them the boundary orientations induced by the reference cross-polytope; relative to the vertex order \(i=1,\dots,d\), their orientation signs differ by \(\prod_i\sigma_i\). The signed cone formula for volume (valid with any apex, including the origin outside the polytope) gives, up to one common orientation sign,
\[
 d!\operatorname{Vol}_d(P)=\left|\sum_{\sigma\in\{\pm1\}^d}\left(\prod_i\sigma_i\right)\det(p_{1,\sigma_1},\ldots,p_{d,\sigma_d})\right|
 =\left|\det(p_{1,+}-p_{1,-},\ldots,p_{d,+}-p_{d,-})\right|.
\]
The last equality is pure determinant multilinearity. Hence \(\operatorname{Vol}_d(P)=V_0|\det A|\). The unquantified determinant identity is already familiar in low dimensions; the new claim concerns its sharp connection to a precise vertex-distance stability statistic.

**2. Exact discrepancy identity.** Expanding squares using \(\|p_{i,\pm}\|=\|e_i\|=1\),
\[
 \sum_i\big(\|p_{i,+}-Ue_i\|^2+\|p_{i,-}+Ue_i\|^2\big)=4d-4\operatorname{tr}(U^{\mathsf T}A).
\]
The polar decomposition or singular-value decomposition of \(A\) gives
\[
 \max_{U\in O(d)}\operatorname{tr}(U^{\mathsf T}A)=\|A\|_* =\sum_{j=1}^d s_j,
 \qquad \Delta^2=4\left(d-\sum_{j=1}^d s_j\right),
\]
where \(s_j>0\) are the singular values of the invertible matrix \(A\). Each half-chord satisfies \(\|a_i\|\le1\), so \(0<\|A\|_*\le\sum_i\|a_i\|\le d\). In particular \(0\le\Delta^2<4d\).

**3. The sharp global envelope and equality.** The geometric-arithmetic mean inequality applied to positive singular values implies
\[
 \frac{\operatorname{Vol}_d(P)}{V_0}=\prod_{j=1}^d s_j
 \le\left(\frac{\sum_js_j}{d}\right)^d
 =\left(1-\frac{\Delta^2}{4d}\right)^d.
\]
Equality in this step holds exactly when all singular values are equal, equivalently \(A=sU\) with some \(s>0\) and \(U\in O(d)\). With \(m_i=(p_{i,+}+p_{i,-})/2\), the unit-sphere constraints then force \(m_i\perp Ue_i\) and \(\|m_i\|^2+s^2=1\), which gives an explicit geometric description of all equality cases subject to the stated polytope combinatorics. Conversely every such configuration is an equality case.

**4. Non-antipodal sharpness at every small discrepancy.** Fix \(d\) and let \(s\in(0,1]\) approach \(1\). Put \(q=\sqrt{1-s^2}\), and read coordinate subscripts cyclically. Set
\[
 p_{i,\pm}=q e_{i+1}\pm s e_i,\qquad i=1,\ldots,d,
\]
with \(e_{d+1}=e_1\). Each vertex is on the unit sphere. When \(s\) is sufficiently close to \(1\), all signed facet-support inequalities at the reference regular cross-polytope remain strict at nonincident vertices. Therefore the perturbed convex hull has exactly the same combinatorial face lattice and the displayed labels remain opposite. For this family, \(A=sI\), whence \(\Delta^2=4d(1-s)\) and \(\operatorname{Vol}_d(P)=V_0s^d\), proving exact equality in the envelope at every \(\Delta^2\) in some interval \([0,\varepsilon_d)\). All members with \(s<1\) have nonzero pair midpoints, so are not centrally symmetric about the origin; for sufficiently small \(q>0\) they are not centrally symmetric about any point because their distinct pair midpoints \(q e_{i+1}\) differ.

**5. Optimal leading deficit.** The binomial expansion gives
\[
 V_0-\operatorname{Vol}_d(P)\ge V_0\left[\frac{\Delta^2}4-\frac{d-1}{32d}\Delta^4+O_d(\Delta^6)\right].
\]
Equality constructions from step 4 make the leading coefficient \(V_0/4=2^{d-2}/d!\) optimal. The exact nonlinear formula is stronger than just this leading term.

## Verification
The standalone file `verify_crosspolytope.py` constructs random near-regular inscribed cross-polytopes and equality configurations in dimensions \(2\) through \(6\), calculates their independent convex-hull volumes with SciPy, and compares them against the determinant identity and the proposed envelope. Running `python verify_crosspolytope.py` reports a PASS for each dimension. These finite tests are supplementary: the all-dimensional proof is Steps 1–5 above, not numerical enumeration.

## Relationship to prior work
Horváth and Lángi, *Maximum volume polytopes inscribed in the unit sphere* (first publicly posted 26 February 2014, arXiv:1402.6496v1), proved in Corollary 3 that the regular cross-polytope uniquely maximizes inscribed volume within its combinatorial class; their work provides the qualitative extremal setting. Their quantitative necessary conditions do not give the exact vertex-Procrustes envelope or the non-antipodal equality curves. A 2025 mathematical discussion on cross-polytope volume and opposite-vertex diagonals records the determinant identity in dimensions \(2\) and \(3\) and asks about the general form; hence the determinant reduction itself is not asserted to be original here. The claimed contribution is the globally valid, locally attained nonlinear volume–shape envelope and its exact equality characterization.

## Limitations
The functional upper bound applies only to cross-polytope combinatorial type with the specified opposite pairing and all vertices on the unit sphere; it is not a theorem for arbitrary \(2d\)-vertex polytopes. The equality family is proved to realize every sufficiently small discrepancy, not every feasible global discrepancy. The distance is a labelled orthogonal Procrustes distance, not Banach–Mazur or Hausdorff distance. The analysis is not independently audited. Older three-dimensional source material may contain related local inequalities not accessible in this investigation, although no source inspected gives the full stated all-dimensional envelope.

## References
1. Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496v1 (26 February 2014), Corollary 3 and Section 2; https://arxiv.org/abs/1402.6496 and https://arxiv.org/html/1402.6496v3.
2. *Volume of polytope spanned by vertex pairs is invariant under translation of diagonals*, Mathematics Stack Exchange question 5100009 (5 October 2025); https://math.stackexchange.com/questions/5100009/volume-of-polytope-spanned-by-vertex-pairs-a-i-a-i-is-invariant-under-trans.
3. M. Berman and D. Hanes, *Volumes of polyhedra inscribed in the unit sphere in \(E^3\)*, Mathematische Annalen 188 (1970), 78–84; cited as prior three-dimensional extremal research in reference 1.
