# Diagonal collapse of the oscillation-exponent gap for bilinear rough commutators

## Finding

Let \(d\ge1\), let
\[
\Omega\in L^\infty(S^{2d-1}),
\qquad
\int_{S^{2d-1}}\Omega\,d\sigma=0,
\]
and extend \(\Omega\) homogeneously to \(\mathbb R^{2d}\setminus\{0\}\). Assume there exist a measurable set
\[
F\subset S^{d-1},
\qquad
\sigma(F)>0,
\]
constants \(\delta,\kappa>0\), and a unimodular number \(\lambda\) such that
\[
\operatorname{Re}\!\left[\lambda\Omega(\theta+h,\theta-h)\right]\ge\kappa
\]
for almost every
\[
(\theta,h)\in F\times B(0,\delta).
\]

Let
\[
T_\Omega(f_1,f_2)(x)
=
\operatorname{p.v.}
\iint_{\mathbb R^d\times\mathbb R^d}
\frac{\Omega((y_1,y_2)/|(y_1,y_2)|)}
{|(y_1,y_2)|^{2d}}
f_1(x-y_1)f_2(x-y_2)\,dy_1\,dy_2.
\]
For a bilinear operator \(T\), write
\[
[b,T]_1(f_1,f_2)=bT(f_1,f_2)-T(bf_1,f_2)
\]
and
\[
[b,T]_2(f_1,f_2)=bT(f_1,f_2)-T(f_1,bf_2).
\]

If \(b\in L^4_{\mathrm{loc}}(\mathbb R^d)\) is complex-valued, then
\[
\bigl\|[b,[b,T_\Omega]_2]_1\bigr\|_{L^2\times L^2\to L^1}
\asymp_{d,\Omega}
\|b\|_{\mathrm{BMO}}^2.
\]
Moreover, for the two partial transposes appearing in the recent lower-bound theorem,
\[
\bigl\|[b,[b,T_\Omega^{*2}]_1]_1\bigr\|_{L^2\times L^\infty\to L^2}
=
\bigl\|[b,[b,T_\Omega^{*1}]_2]_2\bigr\|_{L^\infty\times L^2\to L^2}
\asymp_{d,\Omega}
\|b\|_{\mathrm{BMO}}^2.
\]

Thus the small exponent bump in the two-symbol theorem disappears completely on the natural diagonal
\[
b_1=b_2=b.
\]
For these natural exponent triples, boundedness of any one of the displayed diagonal second-order commutators is equivalent to
\[
b\in\mathrm{BMO},
\]
with no reality assumption on the symbol.

## Assumptions and scope

For \(1\le r<\infty\), define
\[
\|b\|_{\mathrm{BMO}_r}
=
\sup_Q
\left(
\frac1{|Q|}
\int_Q
|b-\langle b\rangle_Q|^r
\right)^{1/r}.
\]
The standard seminorm is
\[
\|b\|_{\mathrm{BMO}}=\|b\|_{\mathrm{BMO}_1}.
\]
By the John--Nirenberg theorem,
\[
\|b\|_{\mathrm{BMO}_r}\asymp_{d,r}\|b\|_{\mathrm{BMO}}
\]
for every finite \(r\).

The recent paper defines, for two symbols \(b_1,b_2\),
\[
S_{r,t}(b_1,b_2)
=
\sup_Q
\langle|b_1-\langle b_1\rangle_Q|\rangle_{r,Q}
\langle|b_2-\langle b_2\rangle_Q|\rangle_{t,Q},
\]
and
\[
T_u(b_1,b_2)
=
\sup_Q
\left\langle
|b_1-\langle b_1\rangle_Q|
|b_2-\langle b_2\rangle_Q|
\right\rangle_{u,Q}.
\]

The local \(L^4\) assumption guarantees that all repeated-position forms used in the lower theorem are defined under its stated hypotheses. In the forward direction, \(b\in\mathrm{BMO}\) itself implies all finite local integrability needed by the upper estimates.

No sharp numerical comparison constants are claimed.

## Proof

On the diagonal \(b_1=b_2=b\), the joint quantities collapse exactly to ordinary \(\mathrm{BMO}\) moments:
\[
S_{r,r}(b,b)
=
\|b\|_{\mathrm{BMO}_r}^2
\]
and
\[
T_u(b,b)
=
\sup_Q
\left(
\frac1{|Q|}
\int_Q
|b-\langle b\rangle_Q|^{2u}
\right)^{1/u}
=
\|b\|_{\mathrm{BMO}_{2u}}^2.
\]

For the mixed commutator, the recent lower theorem gives
\[
S_{2,2}(b,b)+T_1(b,b)
\lesssim_\Omega
\bigl\|[b,[b,T_\Omega]_2]_1\bigr\|_{L^2\times L^2\to L^1}.
\]
The diagonal identities make the left side
\[
2\|b\|_{\mathrm{BMO}_2}^2.
\]
Hence
\[
\|b\|_{\mathrm{BMO}}^2
\lesssim_{d,\Omega}
\bigl\|[b,[b,T_\Omega]_2]_1\bigr\|_{L^2\times L^2\to L^1}.
\]

For the reverse inequality, fix one exponent bump, for example \(\varepsilon=1\), in the source upper theorem:
\[
\bigl\|[b,[b,T_\Omega]_2]_1\bigr\|_{L^2\times L^2\to L^1}
\lesssim_d
\|\Omega\|_\infty
\left(
S_{3,3}(b,b)+T_2(b,b)
\right).
\]
The diagonal identities give
\[
S_{3,3}(b,b)=\|b\|_{\mathrm{BMO}_3}^2,
\qquad
T_2(b,b)=\|b\|_{\mathrm{BMO}_4}^2.
\]
John--Nirenberg therefore yields
\[
\bigl\|[b,[b,T_\Omega]_2]_1\bigr\|_{L^2\times L^2\to L^1}
\lesssim_{d,\Omega}
\|b\|_{\mathrm{BMO}}^2.
\]

For the repeated-position commutators of the partial transposes, the source lower theorem gives
\[
S_{2,2}(b,b)+T_2(b,b)
\lesssim_\Omega
\bigl\|[b,[b,T_\Omega^{*2}]_1]_1\bigr\|_{L^2\times L^\infty\to L^2},
\]
and identifies this norm with
\[
\bigl\|[b,[b,T_\Omega^{*1}]_2]_2\bigr\|_{L^\infty\times L^2\to L^2}.
\]
Here
\[
S_{2,2}(b,b)=\|b\|_{\mathrm{BMO}_2}^2,
\qquad
T_2(b,b)=\|b\|_{\mathrm{BMO}_4}^2.
\]
Thus either repeated-position norm controls \(\|b\|_{\mathrm{BMO}}^2\).

For the reverse repeated-position estimate, again choose \(\varepsilon=1\) in the source upper bound:
\[
\|C\|
\lesssim_d
\|\Omega\|_\infty
\left(
S_{3,3}(b,b)+T_3(b,b)
\right)
=
\|\Omega\|_\infty
\left(
\|b\|_{\mathrm{BMO}_3}^2+
\|b\|_{\mathrm{BMO}_6}^2
\right).
\]
John--Nirenberg bounds this by a constant times
\[
\|b\|_{\mathrm{BMO}}^2.
\]
This completes all three equivalences.

## Verification

The proof uses exact algebraic identities and standard \(\mathrm{BMO}\) moment equivalence; no numerical experiment is involved.

The critical diagonal reductions were checked directly from the definitions:
\[
S_{r,r}(b,b)=\|b\|_{\mathrm{BMO}_r}^2
\]
and
\[
T_u(b,b)=\|b\|_{\mathrm{BMO}_{2u}}^2.
\]
The source lower bounds at the natural exponent triples were checked in its Corollary 1.4 and Theorem 1.10. The source upper bounds were checked in Theorems 1.13 and 1.14. Choosing a fixed \(\varepsilon=1\) is sufficient; no limiting argument as \(\varepsilon\downarrow0\) is used.

The geometric non-degeneracy condition was checked against the source's Assumption 2.5. It is the only extra hypothesis needed for the lower estimates. The upper estimates require only a bounded mean-zero angular kernel.

The repeated-position local-integrability requirement is satisfied under the stated \(L^4_{\mathrm{loc}}\) hypothesis, and automatically under \(\mathrm{BMO}\) in the forward direction.

## Relationship to prior work

The motivating 2026 paper develops joint oscillation conditions for two possibly distinct complex-valued symbols. At the natural exponent triples it obtains necessary conditions at exponents \(2\) and sufficient conditions with an arbitrary positive exponent bump, and explicitly leaves removal of that bump open in the general two-symbol problem.

On the diagonal \(b_1=b_2\), the two joint oscillation scales cease to be genuinely independent: they become ordinary finite \(\mathrm{BMO}\) moments. John--Nirenberg then removes the bump at once and yields a complete same-symbol characterization for the rough bilinear operator, including complex-valued symbols.

Zeng's 2025 bilinear iterated-commutator theorem gives single-symbol lower bounds for real-valued symbols in a non-degenerate bilinear Calderón--Zygmund setting, whose kernels have smoothness assumptions absent from the rough homogeneous operator here. The present consequence therefore uses the new complex-valued rough-kernel lower theorem rather than following from that earlier result.

The 2020 Hytönen--Li--Oikari joint-oscillation theorem concerns iterated commutators of linear Calderón--Zygmund operators. Chaffee's bilinear BMO characterization concerns first-order commutators. Neither supplies the displayed second-order characterization for bounded rough bilinear angular kernels.

## Limitations

The exponent-gap collapse proved here is restricted to the diagonal tuple
\[
b_1=b_2.
\]
It does not solve the motivating paper's open problem for genuinely distinct symbols.

No sharp comparison constants are obtained. The constants in the equivalences inherit the geometric non-degeneracy data, dimension, kernel size, and John--Nirenberg constants.

The lower implication depends on the source's geometric non-degeneracy condition. For a bounded mean-zero angular kernel that fails that condition, no necessity statement is asserted here.

## References

1. Y. Wu, *Sparse bounds and joint oscillation for bilinear rough commutators*, arXiv:2609.27591v1, 2026.
2. Y. Zeng, *Off-diagonal Bloom weighted estimates for bilinear commutators*, arXiv:2505.19007v1, 2025.
3. T. Hytönen, K. Li, and T. Oikari, *Iterated commutators under a joint condition on the tuple of multiplying functions*, Proceedings of the American Mathematical Society 148 (2020), 4797--4815.
4. L. Chaffee, *Characterizations of bounded mean oscillation through commutators of bilinear singular integral operators*, Proceedings of the Royal Society of Edinburgh Section A 146 (2016), 1159--1166.
