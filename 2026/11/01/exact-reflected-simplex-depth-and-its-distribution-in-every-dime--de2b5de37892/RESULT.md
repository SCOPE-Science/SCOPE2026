# Exact reflected-simplex depth and its distribution in every dimension

## Finding
Let \(d\ge3\), let \(S\subset\mathbb R^d\) be any nondegenerate simplex with affine barycentric coordinates \(\lambda_1,\ldots,\lambda_m\), where \(m=d+1\), and let \(\mu\) be uniform volume measure on \(S\). The testing body is the **reflected**, equal-size simplex \(K=-S\), not \(S\) itself. Set \(c=2/m\), \(g\) equal to the centroid, and \(q_+=\max\{q,0\}\). Define, for \(0\le a\le c\),
\[
b(a)=\frac{2-a}{d},\qquad
V_d(a)=\sum_{k=0}^{d}(-1)^k\binom dk\left[(1-kb(a))_+^d-(1-a-kb(a))_+^d\right],
\]
and for \(u\in\mathbb R\),
\[
H_d(u)=\sum_{j=0}^{m}(-1)^j\binom mj(1-ju)_+^d.
\]
Here \(H_d\) on \([1/m,1]\) is the established distribution function of the largest coordinate of a uniform Dirichlet vector. Write \(L(y)=\max_i\lambda_i(y)\); the maximum is at least \(1/m\) even for points outside \(S\).

**Exact pointwise depth, on the entire ambient space:**
\[
\boxed{\mathsf d_{-S}(y;\mu)=1-V_d(\min\{L(y),c\}),\qquad y\in\mathbb R^d.}
\]
The function \(V_d\) is continuous and strictly increasing from \(V_d(0)=0\) to \(V_d(c)=H_d(c)\). Put \(\beta_d=1-H_d(c)\) and \(\gamma_d=1-V_d(1/m)\). Then \(0<\beta_d<\gamma_d<1\), the global minimum depth is \(\beta_d\), and the **unique** depth maximizer is the centroid, with depth \(\gamma_d\).

For every \(\beta_d<\alpha\le\gamma_d\), there is a unique \(u_\alpha\in[1/m,c)\) such that \(V_d(u_\alpha)=1-\alpha\). All the nontrivial upper depth regions are **reflected homothetic simplices**:
\[
\boxed{D_\alpha=\{y:\lambda_i(y)\le u_\alpha\text{ for every }i\}
=g-(m u_\alpha-1)(S-g).}
\]
For \(\alpha\le\beta_d\), \(D_\alpha=\mathbb R^d\); for \(\alpha>\gamma_d\), \(D_\alpha=\varnothing\). The region is contained in the original support \(S\) precisely when \(u_\alpha\le1/d\), equivalently \(\alpha\ge1-V_d(1/d)\); equality is the exact support-contact threshold.

For \(X\sim\mu\), the depth survival function throughout its nontrivial interval is
\[
\boxed{\Pr\{\mathsf d_{-S}(X;\mu)\ge\alpha\}=H_d(u_\alpha),
\qquad\beta_d<\alpha\le\gamma_d.}
\]
There is an **exact baseline atom equal to its own depth value**:
\[
\boxed{\Pr\{\mathsf d_{-S}(X;\mu)=\beta_d\}=\beta_d.}
\]
The survival function is one for \(\alpha\le\beta_d\) and zero for \(\alpha>\gamma_d\). In particular, for \(d=3\),
\[
V_3(a)=2a(1-a),\quad\beta_3=\frac12,\quad\gamma_3=\frac58,\quad
\alpha_{\mathrm{contact}}=\frac59,
\quad u_\alpha=\frac{1-\sqrt{2\alpha-1}}2.
\]
The general formulas remain valid for \(d=2\), recovering the previously established planar result; the assertion here is the higher-dimensional classification.

The baseline atom tends exponentially to one with dimension. For \(m=d+1\), a concrete estimate is
\[
0\le 1-\beta_d=H_d(2/m)\le
\exp[-m(1/4-\log(5/4))]+(1-e^{-5/2})^m.
\]

## Assumptions and scope
A simplex is the convex hull of \(d+1\) affinely independent points, and \(\lambda_i\) are its unique affine coordinate functions satisfying \(\sum_i\lambda_i(y)=1\) and \(S=\{\lambda_i\ge0\ \forall i\}\). The depth uses the exact definition
\[
\mathsf d_{K}(y;\mu)=1-\sup_{z:\,y\notin K+z}\mu(K+z),
\]
with all translates in \(\mathbb R^d\). The suprema over excluded closed translates agree with their boundary-relaxed analogues by continuity of translation mass; no pointwise support restriction on \(y\) is imposed. All volumes are normalized by \(|S|\). Every dimension \(d\ge3\) and every affine realization of \(S\) are covered.

## Proof
**1. Reduce translations to capped Dirichlet volumes.** By affine invariance, work in the barycentric hyperplane \(\sum_i x_i=1\). A translate of \(-S\) is exactly the polytope \(\{x_i\le z_i\ \forall i\}\) for a vector \(z\) with \(\sum_i z_i=2\). Its intersection with \(S\) is
\[
A(z)=\{x_i\ge0,\ x_i\le z_i,\ \sum_i x_i=1\}.
\]
Let \(F(z)=|A(z)|/|S|\). This is zero if a cap is nonpositive. For nonnegative caps, inclusion–exclusion gives
\[
F(z)=\sum_{I\subseteq\{1,\ldots,m\}}(-1)^{|I|}
\left(1-\sum_{i\in I}z_i\right)_+^d.
\]
Indeed, the region in which \(x_i>z_i\) for each \(i\in I\) is a shifted simplex of relative volume \((1-\sum_{i\in I}z_i)_+^d\). A point \(y\) is excluded exactly when some cap \(z_i\) is strictly less than \(\lambda_i(y)\). By continuity the supremum is unchanged if the strict inequality is replaced with \(z_i\le\lambda_i(y)\).

**2. A genuinely dimension-independent cap-optimization lemma.** For nonnegative \(z,w\) of coordinate sum two, convex combinations of points in \(A(z)\) and \(A(w)\) belong to \(A((1-t)z+tw)\). Brunn–Minkowski therefore makes \(F^{1/d}\) concave on this cap simplex. Since \(F\) is permutation invariant, averaging the last \(d\) coordinates at fixed first coordinate \(a\) cannot decrease \(F\). Hence a maximizing vector with \(z_1=a\) is \((a,b(a),\ldots,b(a))\).

For \(0<a<c\), all coordinates of this vector lie strictly between zero and one. Every constraint \(x_i=0\) and \(x_i=z_i\) then supports a genuine facet of \(A(z)\): for the lower facet choose the remaining coordinates proportional to their caps, and for the upper facet choose their sum to be \(1-z_i\). Two such polytopes with distinct cap vectors cannot be positively homothetic, since their complete set of lower facets \(x_i=0\) forces any homothety to have scale one and zero translation, and then the upper facets determine the same caps. Equality in Brunn–Minkowski is therefore excluded between distinct interior cap vectors. Averaging all coordinate permutations strictly increases \(F\) unless the cap vector is constant. Thus the unique maximal overlap is at \(z=(c,\ldots,c)\). Along \(z(a)=(a,b(a),\ldots,b(a))\), the vector at any \(a_2\in(a_1,c)\) is a convex combination of \(z(a_1)\) and \(z(c)\); concavity and the strict endpoint inequality imply \(F(z(a_2))>F(z(a_1))\). Consequently, the maximum subject to \(z_1\le a\le c\) occurs at equality, and for \(a\ge c\) it is the global maximum. Repeating for each coordinate gives the single controlling parameter \(\min\{L(y),c\}\).

**3. Evaluate the one-parameter maximum.** With one cap \(a\) and \(d\) equal caps \(b=(2-a)/d\), split the subsets in the inclusion–exclusion formula by whether they contain the exceptional index. This is exactly the displayed finite formula \(V_d(a)\). Its value at \(a=c\) is \(H_d(c)\). Taking the complement proves the pointwise formula and the strict uniqueness of the centroid maximizer, since \(L(y)=1/m\) only at \(g\).

**4. Identify regions, law, and baseline atom.** For \(\alpha>\beta_d\), strict monotonicity gives \(\mathsf d_{-S}(y;\mu)\ge\alpha\) if and only if \(L(y)\le u_\alpha\). The upper-cap region is the reflected homothetic simplex stated above. Its vertex opposite the \(i\)-th facet has barycentric coordinates \(1-du_\alpha\) in position \(i\) and \(u_\alpha\) elsewhere; it lies in \(S\) exactly when \(u_\alpha\le1/d\). Uniform barycentric coordinates have the \(\operatorname{Dirichlet}(1,\ldots,1)\) law, so inclusion–exclusion gives \(\Pr\{L(X)\le u\}=H_d(u)\). The event of baseline depth is \(\{L(X)\ge c\}\), which has probability \(1-H_d(c)=\beta_d\). Boundaries have \(\mu\)-measure zero, and the remaining survival assertions follow.

**5. Exponential baseline concentration.** Let \(E_i\) be independent rate-one exponential variables, \(T=\sum_{i=1}^m E_i\), and \(X_i=E_i/T\). On \(\{T\le5m/4,\ \max_iX_i\le2/m\}\) all \(E_i\le5/2\). Consequently
\[
H_d(2/m)\le \Pr\{T>5m/4\}+\Pr\{\max_iE_i\le5/2\}.
\]
The exponential-moment Chernoff bound for the \(\operatorname{Gamma}(m,1)\) variable \(T\) yields the first displayed term, and independence yields the second.

## Verification
The accompanying standard-library Python program `verify_reflected_simplex.py` checks the general two-level inclusion–exclusion formula against independently enumerated subset caps using exact rational arithmetic through dimension twelve; strict growth at rational samples; exact three-dimensional specialization, endpoint identities, and equality of baseline and baseline atom; plus independently generated Dirichlet samples and randomized excluded-translate comparisons in dimensions two through five. Running `python3 verify_reflected_simplex.py` produced `PASS 68437 exact or independently sampled checks`. These computations are finite diagnostics. Steps 1–5 above provide the universal proof.

## Relationship to prior work
Molchanov and Nagy (2026, arXiv:2610.26108) introduced the translate-depth framework and established general convexity, affine equivariance, baseline, and erosion identities. Their inspected Sections 2–4 and 7 do not state the present explicit all-dimensional equal-size reflected-simplex optimization. An earlier planar reflected-triangle calculation gives the \(d=2\) specialization, and a distinct same-orientation simplex calculation tests translates of \(tS\), not \(-S\); neither statement covers \(d\ge3\). The maximum-coordinate Dirichlet distribution \(H_d\) is classical (for example, recorded in Schlemm, 2014, Section 2); that distribution is **not** claimed as new. The contribution is the opposite-orientation cap optimization and the resulting higher-dimensional depth classification, support-contact threshold, and exact identification of the baseline atom with its depth level.

## Limitations
No claim is made about arbitrary testing dilations \(-tS\), nonuniform probability laws, arbitrary convex testing bodies, or an empirical finite-sample depth law. The known Dirichlet maximum formula and the prior planar case are explicitly excluded from novelty claims. The high-dimensional exponential upper bound is not a sharp asymptotic rate. The present same mathematical model proof review does not constitute independent validation or definitive historical priority; older multivariate spacing and simplex-overlap literature remains a residual priority risk.

## References
1. I. Molchanov and S. Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, arXiv:2610.26108, first public version October 19, 2026; https://arxiv.org/html/2610.26108v1.
2. E. Schlemm, *Limiting distribution of the maximal distance between random points on a circle: A moments approach*, arXiv:1405.6114, 2014, especially Section 2; https://arxiv.org/html/1405.6114v1.
3. H. Brunn, H. Minkowski, the classical Brunn–Minkowski inequality with its homothety equality condition (standard convex-geometric result).
