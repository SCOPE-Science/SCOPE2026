# Right truncation forces a universal TEA hazard blow-up
## Finding
Consider the right-truncated exponentiated Ailamujia distribution on
\[
0<x<1
\]
with parameters
\[
\alpha>0,
\qquad
\theta>0.
\]
Write
\[
B_\theta(x)
=
1-(1+2\theta x)e^{-2\theta x}
\]
and
\[
A_\theta
=
B_\theta(1)
=
1-(1+2\theta)e^{-2\theta}.
\]
The published cumulative distribution function is
\[
F(x)
=
\left(
\frac{B_\theta(x)}{A_\theta}
\right)^\alpha.
\]

The upper endpoint has a parameter-independent hazard scale. Specifically,
\[
\boxed{
\overline F(x)
\sim
c_{\alpha,\theta}(1-x)
\qquad
(x\uparrow1),
}
\]
\[
\boxed{
f(x)
\longrightarrow
c_{\alpha,\theta}
=
\frac{
4\alpha\theta^2e^{-2\theta}
}{
1-(1+2\theta)e^{-2\theta}
}
>0,
}
\]
and therefore
\[
\boxed{
h(x)
\sim
\frac{1}{1-x}
\qquad
(x\uparrow1).
}
\]

In fact,
\[
\boxed{
h'(x)
\sim
\frac{1}{(1-x)^2},
}
\]
so for every admissible parameter pair the hazard is strictly increasing on some terminal interval immediately before the upper endpoint.

This rules out a globally decreasing hazard for the right-truncated model. A hazard curve may decrease over a substantial interior region, but it must eventually turn upward and diverge.

The 2025 source advertises increasing, decreasing, and bathtub-shaped hazard behavior for the TEA model. The increasing and bathtub possibilities are compatible with the endpoint theorem, but a globally decreasing hazard is not. A 2026 progressive-censoring follow-up reuses the same truncated distribution and again discusses decreasing or nonmonotone hazard flexibility; the same endpoint obstruction applies there.

For example, at
\[
(\alpha,\theta)=(0.2,1),
\]
direct evaluation of the published hazard gives
\[
h(0.1)
=
3.653160159826076\ldots,
\]
\[
h(0.4)
=
2.955266723834778\ldots,
\]
so the hazard decreases over this interior range. Yet
\[
h(0.99)
=
100.868370128441385\ldots.
\]
The decreasing branch therefore reverses before the endpoint, exactly as the theorem requires.

## Assumptions and scope
The result uses the TEA distribution exactly as defined by right truncation to the open unit interval
\[
(0,1).
\]
The parameters satisfy
\[
\alpha,\theta>0.
\]

The conclusion is an endpoint theorem. It does not classify every possible number of interior turning points.

The phrase “globally decreasing hazard” means a hazard that is nonincreasing throughout the whole support. Such a shape is impossible here because the hazard necessarily diverges and is eventually increasing at the right endpoint.

The theorem does not challenge the normalization, CDF, or PDF formulas used in its proof. It identifies a structural consequence of those formulas that constrains the admissible reliability shapes.

## Proof
Differentiate
\[
B_\theta(x)
=
1-(1+2\theta x)e^{-2\theta x}.
\]
This gives
\[
B_\theta'(x)
=
4\theta^2x e^{-2\theta x}.
\]
In particular,
\[
B_\theta'(1)
=
4\theta^2e^{-2\theta}
>0.
\]

Since
\[
A_\theta=B_\theta(1),
\]
Taylor expansion at the upper endpoint gives
\[
A_\theta-B_\theta(x)
=
B_\theta'(1)(1-x)
+
O\!\left((1-x)^2\right).
\]
Hence
\[
\frac{B_\theta(x)}{A_\theta}
=
1-
\frac{B_\theta'(1)}{A_\theta}(1-x)
+
O\!\left((1-x)^2\right).
\]
Raising to the positive power \(\alpha\),
\[
F(x)
=
1-
\frac{\alpha B_\theta'(1)}{A_\theta}(1-x)
+
O\!\left((1-x)^2\right).
\]
Therefore
\[
\overline F(x)
=
\frac{\alpha B_\theta'(1)}{A_\theta}(1-x)
+
O\!\left((1-x)^2\right).
\]
The leading constant is
\[
c_{\alpha,\theta}
=
\frac{\alpha B_\theta'(1)}{A_\theta}
=
\frac{
4\alpha\theta^2e^{-2\theta}
}{
1-(1+2\theta)e^{-2\theta}
}.
\]

The PDF is
\[
f(x)
=
\frac{
\alpha B_\theta(x)^{\alpha-1}B_\theta'(x)
}{
A_\theta^\alpha
},
\]
so continuity at the upper endpoint gives
\[
f(x)\to
\frac{\alpha B_\theta'(1)}{A_\theta}
=
c_{\alpha,\theta}.
\]
Dividing the two expansions yields
\[
h(x)
=
\frac{f(x)}{\overline F(x)}
=
\frac1{1-x}
+
O(1).
\]

Because \(f\) is smooth and strictly positive near \(x=1\), one more Taylor term gives
\[
\overline F(x)
=
f(1-)(1-x)
-
\frac{f'(1-)}{2}(1-x)^2
+
O\!\left((1-x)^3\right)
\]
and
\[
f(x)
=
f(1-)
-
f'(1-)(1-x)
+
O\!\left((1-x)^2\right).
\]
Consequently
\[
h(x)
=
\frac1{1-x}
-
\frac{f'(1-)}{2f(1-)}
+
O(1-x),
\]
so
\[
h'(x)
=
\frac1{(1-x)^2}
+
O(1).
\]
Thus \(h'(x)>0\) for all \(x\) sufficiently close to \(1\).

## Verification
The included checker implements the published TEA CDF, PDF, survival, and hazard directly.

For several positive values of \(\alpha\) and \(\theta\), it verifies numerically that
\[
(1-x)h(x)\to1
\]
as \(x\uparrow1\).

It also checks that
\[
f(x)\to c_{\alpha,\theta}
\]
and
\[
\frac{\overline F(x)}{1-x}\to c_{\alpha,\theta}.
\]

At
\[
(\alpha,\theta)=(0.2,1),
\]
the checker reproduces the interior decline
\[
h(0.1)>h(0.4)
\]
and the large endpoint value
\[
h(0.99)>100.
\]
This demonstrates why finite-range plots can look decreasing while the full-support hazard is not.

The proof of the endpoint law is analytic; the numerical checks are reproducibility aids.

## Relationship to prior work
Jabarah et al. define the distribution by right truncating the exponentiated Ailamujia law at one. Their abstract and introduction advertise increasing, decreasing, and bathtub hazard behavior, while their displayed CDF and hazard are exactly the formulas analyzed above.

The same article later emphasizes increasing and U-shaped examples. Those shapes are compatible with the endpoint theorem. The new point is that right truncation itself imposes a universal terminal blow-up, so any claim of a globally decreasing hazard is incompatible with the defining CDF.

Alamri et al. study the same parent distribution under progressive Type-II censoring. Their discussion again attributes decreasing or nonmonotone hazard flexibility to the model. The endpoint theorem applies unchanged because censoring changes the observation scheme, not the parent hazard.

Focused searches using the exact DOI, TEA and TUEA model names, decreasing-hazard terminology, bounded-support endpoint language, and the asymptotic form \((1-x)^{-1}\) did not locate a published model-specific correction.

## Limitations
The result does not provide a complete phase diagram for the number and locations of interior hazard turning points.

The theorem is specific to the right-truncated support endpoint at one. It does not describe the lower-endpoint behavior, which can depend strongly on \(\alpha\).

A very recent unindexed correction could exist outside the sources examined.

## References
1. H. S. Jabarah, A. H. Tolba, A. T. Ramadan, and A. I. El-Gohary, “A new truncated unit exponentiated Ailamujia distribution with ranked-based inference and engineering applications,” AIMS Mathematics 10 (2025), 20466–20504. DOI: 10.3934/math.2025914.
2. F. S. Alamri, A. H. Tolba, H. S. Jabarah, A. R. El-Saeed, and A. T. Ramadan, “Statistical analysis for the truncated unit exponentiated Ailamujia distribution under progressive Type-II censoring,” AIMS Mathematics 11 (2026), 14341–14373. DOI: 10.3934/math.2026589.
