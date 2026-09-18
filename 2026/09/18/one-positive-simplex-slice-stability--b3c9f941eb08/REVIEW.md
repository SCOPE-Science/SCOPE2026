# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The proof reduces the one-positive-coordinate chamber to an exact elementary density formula. If
\(a=(x,-y_2,\ldots,-y_n)\), \(r_j=y_j/x\), and \(\sum r_j=1\), independence of exponential variables gives
\[
\sigma(a)=x^{-1}\prod_{j=2}^n(1+r_j)^{-1}.
\]
AM-GM then yields the stated ratio bound. The identity
\(\langle a,a_*\rangle=x/A\) follows from \(\sum y_j=x\) and \(A+B=1/A\). Equality forces the balanced vector.

The Hessian calculation was checked directly along arbitrary geodesics through \(a_*\). The tangent-space constraints force the first variation to vanish, while the second logarithmic variation is
\[
-(n-2)+(n-1)+\frac{n-1}{n}=\frac{2n-1}{n}.
\]
Because the first derivative vanishes, this is also the normalized second variation of \(V\). The coefficient is independent of tangent direction, giving the claimed isotropic Hessian.

## Originality

The closest sources inspected were:

- Ambrus–Gárgyán, arXiv:2609.12714, which proves the global minimum and explicitly discusses the gap in Dirksen's balancing proposition. Searches within the accessible text found no stability theorem, Hessian calculation, or second-variation statement.
- Dirksen (2017), which gives volume formulas and a partial minimum result. The new 2026 paper identifies a gap in the balancing proposition used in that route. The present proof uses instead the exact one-positive-sign density factorization and AM-GM.
- Myroshnychenko–Tang–Tatarko–Tkocz, *Stability of Simplex Slicing*, which is a quantitative stability theorem for Webb's maximal-volume section, not for facet-parallel minimal sections.

Targeted searches for quantitative stability of the minimum, second variation/Hessian at a facet-parallel minimum, and angular deficit formulations did not locate a prior equivalent statement. To the best of our knowledge, the explicit bound
\[
V(a)/V_{\min}\ge\sec\theta
\]
in the one-positive chamber, its imbalance form, and the complete Hessian formula are not covered by these sources.

Residual originality risk is non-negligible because the global-minimum preprint appeared only in September 2026, and very recent parallel work may not yet be indexed.

## Value

The result supplies a quantitative strengthening exactly on a natural sign chamber where an older qualitative proof route has a documented gap. It gives a short independent proof of that chamber statement, an explicit deficit in geometric and coordinate terms, and the full local curvature of the section-volume functional at the newly established global minimizer. The Hessian also shows nondegeneracy and identifies the same second-order stiffness in every tangent direction.

The result is deliberately not presented as global stability: normals with multiple positive and multiple negative coordinates remain outside the quantitative estimate.
