# A one-switch dependence law for nested Dirichlet exceedance counts

## Finding

Let \(d\ge2\), \(2\le k\le d\), \(\alpha>0\), and \(X=(X_1,\ldots,X_d)\sim\operatorname{Dirichlet}(\alpha,\ldots,\alpha)\). For \(0<t<1\), count the exceedances among any fixed \(k\) coordinates:
\[
N(t)=\sum_{i=1}^{k}\mathbf1\{X_i>t\},\qquad p(t)=\Pr(X_1>t).
\]
There is exactly one low-threshold critical value \(r_0\in(0,1/2]\), characterized by \(kp(r_0)=1\). For \(0<r\le s<1\):

- If \(r>r_0\), then \(\operatorname{Cov}(N(r),N(s))>0\) for every \(s\ge r\).
- If \(r=r_0\), the covariance is positive for \(r\le s<1-r\), and zero for \(1-r\le s<1\). The former interval is empty when \(d=k=2\) and \(r=r_0=1/2\).
- If \(0<r<r_0\), a **unique** \(s_*(r)\in(r,1-r)\) separates strictly positive covariance for \(r\le s<s_*(r)\) from strictly negative covariance for \(s_*(r)<s<1\), with covariance zero at \(s=s_*(r)\).

In particular, even though \(N(s)\le N(r)\) on every sample path, the two counts can have strictly negative covariance. The necessary and sufficient criterion for such a higher-threshold reversal is \(\mathbb E N(r)=kp(r)>1\).

For the **uniform simplex** case \(\alpha=1\), write \(m=d-1\). The exact covariance and critical threshold are
\[
\operatorname{Cov}(N(r),N(s))=
 k(1-s)^m+k(k-1)(1-r-s)_+^m-k^2(1-r)^m(1-s)^m,
\quad r_0=1-k^{-1/m}.
\]
If \(r<r_0\), the unique sign-switch point has the closed form
\[
b=\left(\frac{k(1-r)^m-1}{k-1}\right)^{1/m},\qquad
s_*(r)=1-\frac{r}{1-b}.
\]

**Geometric-graph consequence.** For \(n\ge3\) independent uniform points in \([0,1]\), let \(K_n(t)\) be the number of connected components of the graph connecting points at distance at most \(t\). Then the same complete trichotomy applies to \(K_n(r),K_n(s)\), with \(d=n+1\), \(k=n-1\), and
\[
r_{0,n}=1-(n-1)^{-1/n}.
\]
At \(n=3\), \(r=1/10\), and \(s=7/10\), the covariance is exactly \(-2183/250000\), exhibiting negative dependence for nested graphs with only three vertices.
For each fixed \(0<c\le \beta\), the thermodynamic-scale limit is
\[
\lim_{n\to\infty}\frac1n\operatorname{Cov}\bigl(K_n(c/n),K_n(\beta/n)\bigr)
=e^{-\beta}\left[1-(1+c\beta)e^{-c}\right].
\]
It switches sign at \(\beta_*(c)=(e^c-1)/c>c\).

## Assumptions and scope

All inequalities between threshold variables refer to real \(0<r\le s<1\); the Dirichlet law has strictly positive equal parameters, and the coordinates counted are a fixed subset of at least two. Strict exceedance is used, but Dirichlet boundary events have probability zero. The graph has a deterministic number of uniform vertices (not Poisson-distributed vertices); its gaps include two uncounted boundary spacings. The scaling limit fixes \(c\) and \(\beta\) independently of \(n\), with \(\beta\ge c>0\).

## Proof

**Step 1: covariance reduction.** Let \(p(t)=\Pr(X_1>t)\), and for \(0<r,s<1\) put \(q_r(s)=\Pr(X_1>r\mid X_2>s)\). Exchangeability gives \(\mathbb E N(t)=kp(t)\). Because the same-coordinate joint exceedance event for \(r\le s\) has probability \(p(s)\), while each of the \(k(k-1)\) different-coordinate pairs contributes \(p(s)q_r(s)\),
\[
\operatorname{Cov}(N(r),N(s))
=k p(s)\bigl[1-kp(r)+(k-1)q_r(s)\bigr].\tag{1}
\]
Here \(p(s)>0\) for \(s<1\); only the bracket determines the sign.

**Step 2: strict conditional-tail monotonicity.** Dirichlet neutrality gives, conditionally on \(X_2=z\),
\[
X_1=(1-z)Y,\quad Y\sim\operatorname{Beta}(\alpha,(d-2)\alpha),
\]
with \(Y\) independent of \(X_2\) when \(d\ge3\). Hence
\[
h_r(z)=\Pr(X_1>r\mid X_2=z)
=\Pr\left(Y>\frac{r}{1-z}\right)
\]
is strictly decreasing on \((0,1-r)\) and zero when \(z\ge1-r\). For \(d=2\), interpret \(Y=1\) deterministically, so \(h_r(z)=\mathbf1\{z<1-r\}\). Since \(X_2\) has a strictly positive beta density \(f\) on \((0,1)\), the conditional average
\[
q_r(s)=\frac{\int_s^1h_r(z)f(z)\,dz}{\int_s^1 f(z)\,dz}
\]
is continuous, strictly decreasing as \(s\) traverses \((0,1-r)\), and identically zero when \(s\ge1-r\). Indeed, on \((0,1-r)\), differentiation yields
\[
q'_r(s)=\frac{f(s)}{p(s)}\bigl(q_r(s)-h_r(s)\bigr)<0,
\]
because the conditional mean to the right is strictly below the value at the lower endpoint. This proof also holds in the \(d=2\) case.

**Step 3: complete sign classification.** The continuous strictly decreasing marginal tail \(p(r)\) runs from one to zero. There is a unique \(r_0\) with \(kp(r_0)=1\). At \(r=1/2\), almost surely at most one coordinate exceeds \(r\), so \(kp(1/2)\le1\) and \(r_0\le1/2\). If \(kp(r)<1\), the bracket in (1) is strictly positive for all \(s\). If \(kp(r)=1\), it is \((k-1)q_r(s)\), strictly positive precisely when \(s<1-r\). If \(kp(r)>1\), then \(r<r_0\le1/2\), so \((r,1-r)\) is nonempty. The bracket is positive at \(s=r\), because (1) there becomes the strictly positive variance of \(N(r)\). This variance is strictly positive: a neighborhood of a simplex vertex indexed among the selected coordinates has exactly one exceedance and has positive probability, while \(\mathbb E N(r)=kp(r)>1\) forces positive probability of at least two exceedances. At \(s=1-r\) the bracket is \(1-kp(r)<0\). By Step 2 it crosses zero exactly once, proving the trichotomy.

**Step 4: uniform-simplex and geometric formulas.** When \(\alpha=1\), translation of the standard simplex gives
\[
\Pr(X_1>r)=(1-r)^{d-1},\quad
\Pr(X_1>r,X_2>s)=(1-r-s)_+^{d-1}.
\]
Substitute in Step 1 and solve its vanishing bracket to obtain the displayed closed forms. For \(n\) uniform ordered points the \(n+1\) boundary-and-interior spacings have symmetric \(\operatorname{Dirichlet}(1,\ldots,1)\) law. Every interior spacing above \(t\) separates two components, hence \(K_n(t)=1+N(t)\) with \(d=n+1\) and \(k=n-1\). The explicit three-point covariance follows by rational substitution. Finally, expand \((1-z/n)^n=e^{-z}(1-z^2/(2n)+O(n^{-2}))\) for fixed \(z\), in the exact graph covariance with \(k=n-1\), to obtain the stated limit.

## Verification

The accompanying standalone `verify.py` uses exact rational arithmetic to check 139,672 finite uniform-simplex sign cases, a three-point counterintuitive negative-covariance example, and numeric brackets around ten closed-form transitions. It also performs deterministic-seed Dirichlet Monte Carlo checks at five parameter settings to corroborate sign changes outside \(\alpha=1\). The stored `verification_results.txt` records the execution. The finite checks are independent diagnostics and **not** a substitute for the analytic quantifier proof in Steps 1–4.

## Relationship to prior work

Joag-Dev and Proschan (1983) establish negative association for Dirichlet coordinates, yielding negative cross-coordinate contributions. Negative association does not by itself determine the sign of \(\operatorname{Cov}(N(r),N(s))\) because the two counts share coordinates. Decreusefond and Ferraz (2010 preprint; 2011 publication) compute one-radius component-count distributions in a Poisson-input interval graph; their inspected theorems are not a two-radius fixed-sample sign classification. The present theorem isolates the sharp, distributional one-switch criterion and converts it to a finite-size geometric graph boundary. It does not claim originality for standard Dirichlet neutrality, beta tails, or the elementary simplex exceedance probabilities.

## Limitations

The exact algebraic crossing formula is restricted to \(\alpha=1\); for general \(\alpha\), the crossing is uniquely defined but implicit. The asymptotic limit is for one-dimensional fixed-size uniform geometric graphs at radii of order \(1/n\), not higher-dimensional models. General empirical-spacing process literature may contain an equivalent formulation of some covariance limits; priority is not established by unsuccessful searching. Certain older full texts were inaccessible, and this is a residual literature risk. No independent scientific audit has been conducted.

## References

1. K. Joag-Dev and F. Proschan, “Negative Association of Random Variables with Applications,” *Annals of Statistics* **11** (1983), 286–295. DOI: 10.1214/aos/1176346079.
2. L. Decreusefond and E. Ferraz, “On the One dimensional Poisson Random Geometric Graph,” arXiv:1008.5140v1 (first public 2010-08-30); *Journal of Probability and Statistics* (2011), article 350382, DOI: 10.1155/2011/350382.
3. R. Pyke, “Spacings,” *Journal of the Royal Statistical Society: Series B* **27** (1965), 395–436. Historical background; full text was not available for inspection.
