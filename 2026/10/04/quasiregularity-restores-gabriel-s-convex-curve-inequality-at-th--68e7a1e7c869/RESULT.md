# Quasiregularity restores Gabriel's convex-curve inequality at the endpoint

## Finding

Let \(K\ge1\), and let
\[
f=h+\overline g
\]
be a sense-preserving harmonic \(K\)-quasiregular mapping of the unit disk \(\mathbb D\), normalized by \(g(0)=0\). Assume
\[
f\in\mathbf h^1,
\qquad
\sup_{0<r<1}\frac1{2\pi}\int_0^{2\pi}|f(re^{i\theta})|\,d\theta<\infty.
\]
Then the analytic components satisfy
\[
h,g\in H^1,
\]
so \(f\) has an \(L^1\) radial boundary trace
\[
f^*=h^*+\overline{g^*}.
\]
Moreover, every convex curve \(\Gamma\subset\mathbb D\) satisfies
\[
\int_\Gamma |f(z)|\,ds(z)
\le
4(K^2+1)
\int_{\mathbb T}|f^*(\zeta)|\,|d\zeta|.
\]
Here a convex curve means a simple rectifiable arc, or a closed rectifiable curve, contained in the boundary of a convex subset of \(\mathbb D\); line segments are allowed.

This supplies a full convex-curve Gabriel inequality at \(p=1\) for the natural harmonic quasiregular subclass. The constant is not asserted to be optimal. In the analytic case \(K=1\), Gabriel's classical sharp constant is \(2\).

## Assumptions and scope

Sense-preserving harmonic \(K\)-quasiregularity means that, for the canonical decomposition \(f=h+\overline g\),
\[
|g'(z)|\le k|h'(z)|,
\qquad
k=\frac{K-1}{K+1}<1.
\]
The normalization \(g(0)=0\) is the standard harmless normalization of the decomposition.

The conclusion is specific to \(p=1\). It does not assert a corresponding theorem for \(0<p<1\), and it does not determine the best dependence on \(K\). The theorem concerns harmonic quasiregular mappings; no claim is made for the unrestricted radial quasiregular Hardy class, where boundary values require additional hypotheses.

## Proof

Write
\[
a=|h'|,
\qquad
b=|g'|,
\qquad
S=a^2+b^2.
\]
The singular values of the real differential \(Df\) are
\[
\Lambda=a+b,
\qquad
\lambda=a-b.
\]
Since \(b/a\le k\), with the zero-derivative case understood by continuity,
\[
\frac{\lambda^2}{S}
=
\frac{(a-b)^2}{a^2+b^2}
\ge
\frac{(1-k)^2}{1+k^2}
=
\frac{2}{K^2+1}.
\tag{1}
\]

Fix \(\varepsilon>0\) and define the smooth positive functions
\[
U_\varepsilon
=
\sqrt{|f|^2+2\varepsilon^2},
\qquad
V_\varepsilon
=
\sqrt{|h|^2+|g|^2+\varepsilon^2}.
\]
For a harmonic vector-valued map \(F\) and \(W=\sqrt{|F|^2+c}\), direct differentiation gives
\[
\Delta W
=
\frac{|DF|_F^2}{W}
-
\frac{|DF^TF|^2}{W^3}.
\tag{2}
\]
Applying (2) to the planar harmonic map \(f\), using
\[
|Df|_F^2=\Lambda^2+\lambda^2,
\qquad
|Df^Tf|\le\Lambda|f|,
\]
gives
\[
\Delta U_\varepsilon
\ge
\frac{\lambda^2}{U_\varepsilon}.
\tag{3}
\]
For the four-real-dimensional harmonic map \((h,g)\), formula (2) gives
\[
\Delta V_\varepsilon
\le
\frac{2S}{V_\varepsilon}.
\tag{4}
\]
Also
\[
U_\varepsilon^2
\le
2V_\varepsilon^2.
\tag{5}
\]
Combining (1)--(5),
\[
\Delta U_\varepsilon
\ge
\frac{1}{\sqrt2(K^2+1)}
\Delta V_\varepsilon.
\tag{6}
\]

Let \(M_1(r,W)\) denote the normalized circular mean of a nonnegative function \(W\). Green's radial mean identity applied to (6) yields
\[
M_1(r,U_\varepsilon)-U_\varepsilon(0)
\ge
c_K\bigl(M_1(r,V_\varepsilon)-V_\varepsilon(0)\bigr),
\qquad
c_K=\frac1{\sqrt2(K^2+1)}.
\tag{7}
\]
Letting \(\varepsilon\downarrow0\), the normalization \(g(0)=0\) gives the same center value \(|f(0)|\) on both sides. Since \(c_K\le1\) and the mean of the subharmonic function \(|f|\) dominates \(|f(0)|\), (7) implies
\[
M_1\!\left(r,\sqrt{|h|^2+|g|^2}\right)
\le
c_K^{-1}M_1(r,|f|).
\tag{8}
\]
Therefore
\[
M_1(r,|h|+|g|)
\le
\sqrt2\,M_1\!\left(r,\sqrt{|h|^2+|g|^2}\right)
\le
2(K^2+1)M_1(r,|f|).
\tag{9}
\]
Because \(f\in\mathbf h^1\), equation (9) proves \(h,g\in H^1\). Their radial limits belong to \(L^1(\mathbb T)\), converge in \(L^1\), and satisfy
\[
\int_{\mathbb T}(|h^*|+|g^*|)\,|d\zeta|
\le
2(K^2+1)
\int_{\mathbb T}|f^*|\,|d\zeta|.
\tag{10}
\]

Gabriel's analytic theorem at \(p=1\), applied separately to \(h\) and \(g\), gives
\[
\int_\Gamma |h|\,ds
\le
2\int_{\mathbb T}|h^*|\,|d\zeta|,
\qquad
\int_\Gamma |g|\,ds
\le
2\int_{\mathbb T}|g^*|\,|d\zeta|.
\]
Using \(|f|\le|h|+|g|\) and then (10) proves
\[
\int_\Gamma |f|\,ds
\le
4(K^2+1)
\int_{\mathbb T}|f^*|\,|d\zeta|.
\]

## Verification

The critical nonstandard step is the regularized Laplacian comparison. Formula (2) follows by differentiating \(W=(|F|^2+c)^{1/2}\) and using \(\Delta F=0\). Inequality (3) uses the exact two singular values of a planar harmonic map, while (4) uses the exact Frobenius energy \(2(|h'|^2+|g'|^2)\) of the analytic pair \((h,g)\).

The distortion conversion was checked algebraically:
\[
\frac{(1-k)^2}{1+k^2}
=
\frac2{K^2+1}
\quad\text{when}\quad
k=\frac{K-1}{K+1}.
\]
The regularization removes any issue at zeros of \(f\), \(h\), or \(g\), and monotone convergence permits \(\varepsilon\downarrow0\). No finite experiment or numerical approximation is used.

## Relationship to prior work

Bajrami's 2026 paper proves a dilatation-dependent Gabriel inequality for harmonic \(K\)-quasiregular mappings at \(p=2\), and records the general \(p>1\) harmonic result as a corollary of Das. Its Problem 7.4 asks which additional quasiregular or harmonic quasiregular assumptions restore a Gabriel-type inequality at \(p=1\) or below. The theorem above answers the \(p=1\) existence part for the basic harmonic \(K\)-quasiregular subclass.

Das proved that the unrestricted harmonic convex-curve inequality fails for every \(0<p\le1\), so quasiregularity is a substantive hypothesis rather than a cosmetic restriction. Bajrami also proves a sharp constant-\(2\) theorem under the separate assumption that \(|f|\) is log-subharmonic; harmonic quasiregularity alone is not stated there to imply that hypothesis.

The quasiregular Hardy-space theory of Adamowicz and González obtains non-tangential maximal characterizations under additional growth and multiplicity hypotheses. Those conditions are not part of the present theorem. Related harmonic-quasiregular Riesz and Zygmund theorems compare real and imaginary components or impose one-sided growth assumptions; they do not state a convex-curve endpoint Gabriel inequality for every harmonic \(K\)-quasiregular \(\mathbf h^1\) map.

## Limitations

The factor \(4(K^2+1)\) is a sufficient constant furnished by the Laplacian comparison and is not claimed sharp. It is far from the sharp analytic value at \(K=1\), where the coanalytic component vanishes and Gabriel's constant is \(2\).

No statement is made for \(0<p<1\). The theorem also does not address arbitrary quasiregular mappings without harmonicity, nor does it supply a boundary maximal-function theorem for the full radial quasiregular Hardy class.

## References

1. E. Bajrami, *Gabriel-Type Estimates for Harmonic Quasiregular Mappings and Stoilow Classes*, arXiv:2606.22358v1, 2026.
2. S. Das, *Gabriel's problem for harmonic Hardy spaces*, Journal of Mathematical Analysis and Applications 552 (2025), Article 129816; arXiv:2408.06623v2.
3. S. Das, J. Huang, and A. Rasila, *Zygmund's theorem for harmonic quasiregular mappings*, Complex Analysis and Operator Theory 19 (2025), Article 91; arXiv:2501.01627v1.
4. T. Adamowicz and M. J. González, *Hardy spaces and quasiregular mappings*, Transactions of the American Mathematical Society 378 (2025), 6265--6290; arXiv:2309.12947.
5. R. M. Gabriel, *Some results concerning the integrals of moduli of regular functions along curves of certain types*, Proceedings of the London Mathematical Society (2) 28 (1928), 121--127.
