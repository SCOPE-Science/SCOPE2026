# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.** The key step is a tangent-space rescaling at a point of \(X\). The
normal-coordinate expansions
\[
d(\exp_o(\varepsilon x),\exp_o(\varepsilon y))^2
=\varepsilon^2|x-y|^2+O(\varepsilon^4)
\]
and \(d\sigma=\varepsilon^d(1+O(\varepsilon^2))dy\), together with the explicit
Dakshi--Pusti normalization, give the nonzero limit factor \(2^{\mu+1}\) and the
standard Euclidean complex spherical mean. The powers of \(\varepsilon\) cancel
exactly:
\[
-(d-2+2\mu)+(2\mu-2)+d=0.
\]
For nonpositive real part, the normalized distribution
\(s_+^{\mu-1}/\Gamma(\mu)\) and the identity
\(\partial_s^k u_{\mu+k}=u_\mu\) justify the same limit after analytic
continuation.

A global \(L^p(X)\) maximal bound controls every finite collection of radii
\(\varepsilon t\). Fatou's lemma after rescaling transfers this to every finite
set of Euclidean radii in \([1,2]\); density in \(t\) then gives the full local
Euclidean maximal bound. Applying the published Liu--Shen--Song--Yan necessary
condition with \(q=p\) yields the claimed formula.

The formula was checked algebraically:
\[
\sigma_d(p,p)=
\max\left\{
-(d-1)/p,\ 1/p-(d-1)/2,\ 1-d+d/p
\right\}.
\]
For \(p>2\), the third term is strictly smaller than the second by
\((d-1)(1/2-1/p)\). The remaining two terms cross at
\(p=2d/(d-1)\). For real hyperbolic space the result agrees with the previously
published Chen--Shen--Wang--Yan necessary condition, providing an external
consistency check.

## Originality

**PASS, to the best of our knowledge.** The most relevant source is the
September 2026 Dakshi--Pusti preprint introducing the generalized complex-order
operator on arbitrary rank-one noncompact symmetric spaces. Its Theorem 1.6 gives
only \(\mu>1-d+d/p\) for real \(\mu\), and Remark 3.7 explicitly leaves the
\(p>2\) range for further investigation. The sharper two-term \(p>2\) boundary is
known on real hyperbolic space from Chen--Shen--Wang--Yan, but searches found no
statement extending it to all rank-one spaces or to complex \(\mu\).

The January 2026 Liu--Shen--Song--Yan theorem supplies the Euclidean single-scale
necessary condition used here. Ghosh--Liu--Rozendaal--Song treat local
Fourier-integral maximal estimates, complex Euclidean means and ordinary
geodesic spheres on compact manifolds, but no located statement gives the present
\(L^p\) necessary region for the Dakshi--Pusti family on arbitrary rank-one
noncompact spaces.

The tangent-space/blow-up idea itself is classical in spirit and is not claimed
as an independently new general technique. The claimed contribution is the
specific transfer theorem for the newly introduced family and the consequent
all-rank-one, complex-order necessary region.

Residual originality risk remains because the Dakshi--Pusti paper is only days
old and contemporaneous comments or revisions may not yet be indexed. No
inaccessible paper was identified whose known title or abstract specifically
suggests the same all-rank-one theorem.

## Value

**PASS.** The result immediately strengthens the necessary side of a very recent
general theorem in the entire \(p>2\) regime and shows that the two
real-hyperbolic obstructions are actually universal local obstructions depending
only on dimension. It also removes the real-parameter restriction from those
local necessary conditions. This materially narrows the permissible region for
any future improvement of the sufficient \(p>2\) theory.

## Limitations checked

- Necessity only; no matching sufficiency is claimed.
- The complex endpoint for \(p\le2\) is not resolved.
- No \(p=\infty\), weak-endpoint, lacunary, or higher-rank claim is made.
- Review is not independent validation, peer review, or formal verification.
