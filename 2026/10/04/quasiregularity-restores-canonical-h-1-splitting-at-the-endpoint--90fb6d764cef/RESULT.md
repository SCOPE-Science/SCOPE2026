# Quasiregularity restores canonical \(H^1\) splitting at the endpoint

## Finding

Let \(K\ge1\), \(K_0\ge0\), and let
\[
f=h+\overline g
\]
be a weak harmonic \((K,K_0)\)-quasiregular mapping of the unit disk, with the canonical normalization
\[
g(0)=0.
\]
Thus
\[
J_f\ge0,
\qquad
\Lambda_f^2\le KJ_f+K_0.
\]
If
\[
f\in\mathbf h^1,
\]
then
\[
h,g\in H^1.
\]

The endpoint statement has a quantitative radial form. Put
\[
c_K
=
\min\!\left\{\frac{2}{K^2+1},\frac12\right\},
\qquad
D_K
=
\frac{2^{3/2}}{c_K},
\qquad
\eta
=
\frac{4K_0}{K^2+1}.
\]
Then, for every \(0<r<1\),
\[
\int_{\mathbb T}
\left(
|h(r\zeta)|^2+|g(r\zeta)|^2+\eta r^2
\right)^{1/2}
d\sigma(\zeta)
\le
D_K
\int_{\mathbb T}
\left(
|f(r\zeta)|^2+\eta r^2
\right)^{1/2}
d\sigma(\zeta).
\]
Consequently,
\[
\max\{\|h\|_{H^1},\|g\|_{H^1}\}
\le
D_K
\left(
\|f\|_{\mathbf h^1}
+
2\sqrt{\frac{K_0}{K^2+1}}
\right).
\]

This is a genuine endpoint effect. For an arbitrary harmonic member of \(\mathbf h^1\), its analytic and co-analytic components need not lie in \(H^1\).

## Assumptions and scope

For a harmonic mapping
\[
f=h+\overline g,
\]
write
\[
\Lambda_f=|h'|+|g'|,
\qquad
\lambda_f=\bigl||h'|-|g'|\bigr|.
\]
Since \(J_f\ge0\),
\[
J_f=\Lambda_f\lambda_f.
\]
The weak quasiregular hypothesis is therefore
\[
\Lambda_f^2
\le
K\Lambda_f\lambda_f+K_0.
\]

The conclusion concerns the canonical analytic/co-analytic splitting. It does not assert an \(L^1\) Littlewood--Paley square-function estimate, and the displayed constant \(D_K\) is a valid explicit constant rather than a claim of optimality.

The normalization \(g(0)=0\) is the standard canonical normalization and is used only to match the two comparison functions at the origin.

## Proof

Set
\[
S=|h'|^2+|g'|^2.
\]
The elementary identity
\[
S=\frac{\Lambda_f^2+\lambda_f^2}{2}
\]
and the weak quasiregular inequality imply
\[
\Lambda_f^2
\le
\frac{2K^2}{K^2+1}S
+
\frac{2K_0}{K^2+1}.
\]
Indeed,
\[
\Lambda_f^2
-
\frac{2K^2}{K^2+1}S
=
\frac{
(\Lambda_f-K\lambda_f)
(\Lambda_f+K\lambda_f)
}{K^2+1}.
\]
If the first factor is nonpositive there is nothing to prove. Otherwise
\[
K\lambda_f<\Lambda_f,
\]
so
\[
(\Lambda_f-K\lambda_f)
(\Lambda_f+K\lambda_f)
\le
2\Lambda_f(\Lambda_f-K\lambda_f)
=
2(\Lambda_f^2-K\Lambda_f\lambda_f)
\le
2K_0.
\]

Put
\[
\eta=\frac{4K_0}{K^2+1}
\]
and, for \(\varepsilon>0\), define
\[
V_\varepsilon(z)
=
\left(
|f(z)|^2+\eta|z|^2+\varepsilon
\right)^{1/2},
\]
\[
U_\varepsilon(z)
=
\left(
|h(z)|^2+|g(z)|^2+\eta|z|^2+\varepsilon
\right)^{1/2}.
\]

The differential calculation in the recent Littlewood--Paley proof remains valid at the endpoint because the regularization \(\varepsilon>0\) removes the only singularity. For completeness, write
\[
\Phi(z)=(f(z),\sqrt{\eta}\,z).
\]
Then
\[
\Delta |\Phi|^2
=
4(S+\eta)
\]
and
\[
|\nabla |\Phi|^2|^2
\le
4V_\varepsilon^2(\Lambda_f^2+\eta).
\]
Therefore
\[
\Delta V_\varepsilon
\ge
V_\varepsilon^{-1}
\left(
2S-\Lambda_f^2+\eta
\right).
\]
Using the preceding bound for \(\Lambda_f^2\) gives
\[
\Delta V_\varepsilon
\ge
V_\varepsilon^{-1}
\left(
\frac{2}{K^2+1}S+\frac{\eta}{2}
\right)
\ge
c_K
V_\varepsilon^{-1}(S+\eta),
\]
where
\[
c_K
=
\min\!\left\{\frac{2}{K^2+1},\frac12\right\}.
\]

Direct differentiation of \(U_\varepsilon\) gives
\[
\Delta U_\varepsilon
\le
2U_\varepsilon^{-1}(S+\eta).
\]
Since
\[
|f|^2
\le
2(|h|^2+|g|^2),
\]
we have
\[
V_\varepsilon^2\le2U_\varepsilon^2
\]
and hence
\[
U_\varepsilon^{-1}
\le
\sqrt2\,V_\varepsilon^{-1}.
\]
Thus
\[
\Delta U_\varepsilon
\le
D_K\,\Delta V_\varepsilon,
\qquad
D_K=\frac{2^{3/2}}{c_K}.
\]

Green's mean identity yields, for \(0<r<1\),
\[
\int_{\mathbb T}U_\varepsilon(r\zeta)\,d\sigma(\zeta)
-
U_\varepsilon(0)
\le
D_K
\left[
\int_{\mathbb T}V_\varepsilon(r\zeta)\,d\sigma(\zeta)
-
V_\varepsilon(0)
\right].
\]
Because \(g(0)=0\),
\[
U_\varepsilon(0)=V_\varepsilon(0).
\]
Also \(D_K\ge1\), so
\[
\int_{\mathbb T}U_\varepsilon(r\zeta)\,d\sigma(\zeta)
\le
D_K
\int_{\mathbb T}V_\varepsilon(r\zeta)\,d\sigma(\zeta).
\]
Letting \(\varepsilon\downarrow0\) gives the displayed radial estimate.

Finally,
\[
\left(
|f|^2+\eta r^2
\right)^{1/2}
\le
|f|+r\sqrt{\eta},
\]
so
\[
\sup_{0<r<1}
\int_{\mathbb T}
\left(
|h|^2+|g|^2
\right)^{1/2}
d\sigma
\le
D_K
\left(
\|f\|_{\mathbf h^1}+\sqrt{\eta}
\right).
\]
Since each of \(|h|\) and \(|g|\) is bounded by the vector norm on the left,
\[
h,g\in H^1
\]
with the claimed quantitative bound.

To see why the quasiregular hypothesis matters, consider
\[
F(z)=\frac{1+z}{1-z}
\]
and
\[
f(z)=\operatorname{Re}F(z).
\]
This is the positive Poisson kernel with
\[
\|f\|_{\mathbf h^1}=1.
\]
Its canonical splitting is
\[
h(z)=\frac1{1-z},
\qquad
g(z)=\frac z{1-z}.
\]
The integral means of \(|h|\) and \(|g|\) diverge logarithmically as the radius tends to one, so neither component belongs to \(H^1\).

## Verification

The endpoint calculation was reconstructed from the exact regularized functions and differential identities used in the primary source, rather than by taking a limit of its \(p>1\) theorem.

At the critical exponent, the lower Laplacian coefficient is
\[
\min\!\left\{\frac{2}{K^2+1},\frac12\right\}>0.
\]
All comparison functions are smooth for \(\varepsilon>0\), so Green's identity applies without an endpoint singularity. The passage \(\varepsilon\downarrow0\) is justified by Fatou's lemma on the left and dominated convergence on the right for each fixed radius.

The counterexample without quasiregularity is exact: the positive Poisson kernel has circle mean one, while
\[
\int_{\mathbb T}\frac{d\sigma(\zeta)}{|1-r\zeta|}
\]
diverges like a logarithm as \(r\uparrow1\).

No finite experiment, truncation, or numerical evidence is used.

## Relationship to prior work

Chen, Huang, Jin, and Li prove a Littlewood--Paley estimate for weak harmonic \((K,K_0)\)-quasiregular mappings when \(1<p\le2\). Their proof first obtains an \(H^p\) bound for the analytic and co-analytic components and then invokes the analytic Littlewood--Paley theorem. The endpoint \(p=1\) is not stated. The finding above isolates the component-comparison part of their proof and shows that this part survives exactly at \(p=1\), even though the square-function theorem itself is not being extended here.

Das, Huang, and Rasila analyze the ordinary harmonic \(h^1\) endpoint. Their Theorem 3(ii) gives, for a general harmonic \(f\in h^1\), only
\[
h,g\in H^p
\qquad(0<p<1).
\]
They also obtain \(H^1\) membership for the single combination \(h+g\) under an additional nonvanishing hypothesis. Neither statement gives \(h,g\in H^1\) from \(f\in h^1\). The Poisson-kernel example above shows that such a general endpoint splitting is false.

The new point is therefore structural: the weak quasiregular differential inequality restores the canonical analytic/co-analytic splitting precisely at the endpoint where ordinary harmonic \(h^1\) loses it.

## Limitations

The displayed \(D_K\) is an explicit proof constant, not asserted to be optimal.

The theorem does not prove an \(L^1\) bound for the sharp-cutoff Littlewood--Paley square function from the recent source. It only identifies the canonical splitting step as endpoint-stable.

The result is stated in the disk and uses the weak harmonic \((K,K_0)\)-quasiregular differential inequality. No corresponding endpoint statement is claimed for arbitrary harmonic mappings, for nonharmonic quasiregular mappings, or for unrelated Hardy-space decompositions.

## References

1. S. Chen, M. Huang, L. Jin, and Q. Li, *Sharp constant problems for harmonic mappings*, arXiv:2609.33159v1, 2026.
2. S. Das, J. Huang, and A. Rasila, *Zygmund's theorem for harmonic quasiregular mappings*, Complex Analysis and Operator Theory 19 (2025), Article 91; arXiv:2501.01627v1.
3. D. Kalaj, *Riesz and Kolmogorov inequality for harmonic quasiregular mappings*, Journal of Mathematical Analysis and Applications 542 (2025), Article 128767; arXiv:2310.12643.
