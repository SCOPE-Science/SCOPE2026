# An averaged infinitesimal Morera theorem for locally integrable data

## Finding

Let \(D\subset\mathbb C\) be a domain and let
\[
f\in L^1_{\mathrm{loc}}(D).
\]
For a compact set \(K\Subset D\) and
\[
0<r<\operatorname{dist}(K,\partial D),
\]
define, for almost every \(a\in K\),
\[
J_r f(a)
=
\int_0^{2\pi}
f(a+re^{it})\,i r e^{it}\,dt.
\]
The circle integral exists for almost every center by Fubini's theorem.

Assume that for every compact \(K\Subset D\),
\[
\|J_r f\|_{L^1(K)}
=
o(r^2)
\qquad(r\downarrow0).
\]
Then \(f\) agrees almost everywhere on \(D\) with a holomorphic function.

More precisely,
\[
\frac{1}{2\pi i r^2}J_r f
\longrightarrow
\bar\partial f
\qquad
\text{in }\mathcal D'(D)
\]
as \(r\downarrow0\). Thus the hypothesis is exactly a strong local averaged version of the distributional equation
\[
\bar\partial f=0.
\]

The scale is sharp. For
\[
f(z)=\bar z,
\]
one has
\[
J_r f(a)=2\pi i r^2
\]
for every admissible center and radius, so replacing \(o(r^2)\) by \(O(r^2)\) would be false.

## Assumptions and scope

The conclusion is an almost-everywhere statement because the input is only locally integrable. After the proof identifies a holomorphic representative \(h\), one has
\[
f=h
\]
almost everywhere on \(D\).

The hypothesis is local in both the domain and the center variable. No uniform pointwise control in \(a\) is assumed. Instead, the normalized circular integral tends to zero in
\[
L^1_{\mathrm{loc}}(D).
\]

No boundary regularity of \(D\) is required.

## Proof

Fix a test function
\[
\varphi\in C_c^\infty(D).
\]
Choose a compact set \(K\Subset D\) containing a neighbourhood of
\[
\operatorname{supp}\varphi.
\]
For all sufficiently small \(r\), Fubini's theorem gives
\[
\int_K |J_r f(a)|\,dA(a)
\le
2\pi r
\int_{K_r}|f(z)|\,dA(z),
\]
where
\[
K_r=\{z:\operatorname{dist}(z,K)\le r\}.
\]
Hence \(J_r f\) is well defined as an \(L^1(K)\) function.

Pair \(J_r f\) with \(\varphi\). After the change of variables
\[
z=a+re^{it},
\]
one obtains
\[
\int_D J_r f(a)\varphi(a)\,dA(a)
=
\int_D f(z)
\left[
\int_0^{2\pi}
\varphi(z-re^{it})\,i r e^{it}\,dt
\right]dA(z).
\]

Taylor expansion on a fixed compact neighbourhood of the support gives, uniformly in \(z\),
\[
\varphi(z-re^{it})
=
\varphi(z)
-r e^{it}\partial\varphi(z)
-r e^{-it}\bar\partial\varphi(z)
+O_\varphi(r^2).
\]
After multiplication by
\[
i r e^{it}
\]
and integration in \(t\), the constant Fourier mode and the \(e^{2it}\) mode vanish, while the \(\bar\partial\varphi\) term contributes
\[
-2\pi i r^2\bar\partial\varphi(z).
\]
Therefore
\[
\int_0^{2\pi}
\varphi(z-re^{it})\,i r e^{it}\,dt
=
-2\pi i r^2\bar\partial\varphi(z)
+
O_\varphi(r^3).
\]

Because \(f\) is integrable on the fixed compact enlargement involved here,
\[
\frac{1}{2\pi i r^2}
\int_D J_r f(a)\varphi(a)\,dA(a)
\longrightarrow
-\int_D f(z)\bar\partial\varphi(z)\,dA(z).
\]
By the definition of distributional differentiation, the right-hand side is
\[
\langle\bar\partial f,\varphi\rangle.
\]
Thus
\[
\frac{1}{2\pi i r^2}J_r f
\longrightarrow
\bar\partial f
\]
in \(\mathcal D'(D)\).

Now use the assumed local \(L^1\) decay. If
\[
\operatorname{supp}\varphi\subset K,
\]
then
\[
\left|
\frac{1}{2\pi i r^2}
\int_D J_r f(a)\varphi(a)\,dA(a)
\right|
\le
\frac{\|\varphi\|_\infty}{2\pi r^2}
\|J_r f\|_{L^1(K)}
\longrightarrow0.
\]
Hence
\[
\bar\partial f=0
\]
in \(\mathcal D'(D)\).

For completeness, the passage from distributional holomorphy to an actual holomorphic representative can be proved by mollification. Choose
\[
V\Subset W\Subset D.
\]
For sufficiently small \(\varepsilon\), let
\[
f_\varepsilon=f*\rho_\varepsilon
\]
on \(W\). Distributional differentiation commutes with convolution, so
\[
\bar\partial f_\varepsilon=0
\]
and every \(f_\varepsilon\) is holomorphic on \(W\). Also
\[
f_\varepsilon\longrightarrow f
\]
in \(L^1(W)\). For \(V\Subset W\), the mean-value inequality for holomorphic functions gives
\[
\sup_V|f_\varepsilon-f_\delta|
\le
C_{V,W}
\|f_\varepsilon-f_\delta\|_{L^1(W)}.
\]
Thus \(f_\varepsilon\) converges uniformly on \(V\) to a holomorphic function \(h\), while the same sequence converges to \(f\) in \(L^1(W)\). Therefore
\[
h=f
\]
almost everywhere on \(V\). Since \(V\Subset D\) was arbitrary, these local representatives agree and give one holomorphic representative on \(D\).

Finally, direct parametrization gives, for \(f(z)=\bar z\),
\[
\int_0^{2\pi}
\overline{a+re^{it}}\,
i r e^{it}\,dt
=
2\pi i r^2,
\]
which proves sharpness of the order \(r^2\).

## Verification

The central identity was checked directly at the distribution level. Its sign and normalization agree with the smooth Green-formula normalization in the motivating paper:
\[
r^{-2}J_r f(a)\longrightarrow2\pi i\,\bar\partial f(a)
\]
when \(f\) is \(C^1\).

The Taylor remainder contributes \(O(r^3)\) before division by \(r^2\). Since \(f\) is locally integrable on a fixed compact enlargement, its contribution tends to zero after pairing with a test function.

No pointwise representative of \(f\) is used in the proof. No differentiation of \(f\) is assumed. No numerical experiment or finite computation is used as evidence.

## Relationship to prior work

Guo and Xiao prove the recent infinitesimal circular Morera theorem for continuous functions under the pointwise condition
\[
J_f(a,r)=o(r^2)
\]
at every center. Their theorem is genuinely pointwise and uses continuity to recover the original function after a distributional primitive argument.

The statement here changes both axes of the hypothesis: the function is only locally integrable, while the circular defect is controlled in the local \(L^1\) norm of the center variable. The new proof bypasses pointwise asymptotic mean-value theory and identifies the normalized circular operator itself as an approximation to \(\bar\partial\) in distributions.

Zalcman's classical mean-value theorem characterizes weak solutions of homogeneous constant-coefficient differential equations through exact convolution mean-value identities. That broad framework is closely related, but the accessible descriptions concern exact identities for all admissible centers and radii, not the local averaged little-oh asymptotic used here. The full 1973 article was not available for direct inspection during this comparison, so it remains an explicit literature risk.

Weit's generalized asymptotic mean-value work concerns continuous functions and convergence uniformly on compact sets for a different large-parameter mean-value regime. Recent nonlinear asymptotic characterizations of holomorphic functions likewise use pointwise or contact-type mean operators rather than the local \(L^1\)-in-center circular defect above.

## Limitations

The theorem does not assert pointwise convergence of normalized circular integrals for a merely \(L^1_{\mathrm{loc}}\) function.

The \(L^1\)-in-center hypothesis is sufficient for distributional holomorphy; no claim is made that it is the weakest possible topology. Distributional convergence of the normalized defects to zero would itself suffice, but that is a reformulation at the level of the proof rather than a quantitative function-space hypothesis.

The literature comparison leaves a residual risk from older general convolution-equation theory whose full text was not accessible in this review.

## References

1. Q. Guo and A. Xiao, *An Infinitesimal Circular Morera Theorem*, arXiv:2608.04540v1, 2026.
2. L. Zalcman, *Mean values and differential equations*, Israel Journal of Mathematics 14 (1973), 339--352.
3. Y. Weit, *On a generalized asymptotic mean value property*, Aequationes Mathematicae 41 (1991), 242--247.
4. R. Durastanti and R. Magnanini, *Nonlinear asymptotic mean value characterizations of holomorphic functions*, ESAIM: Control, Optimisation and Calculus of Variations 30 (2024), Article 46.
