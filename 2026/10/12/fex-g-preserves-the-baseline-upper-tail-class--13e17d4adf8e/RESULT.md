# FEx-G preserves the baseline upper-tail class
## Finding
Let \(G\) be a proper baseline cumulative distribution function with survival function
\[
s(x)=\overline G(x)=1-G(x),
\]
and right endpoint \(x_G\), finite or infinite. The 2026 parsimonious FEx-G construction defines
\[
F(x)=p\left[1-\exp\left\{-\left(1-s(x)^{G(x)}\right)\right\}\right],
\qquad
p=\frac{e}{e-1}.
\]
Since \(G(x)=1-s(x)\), its survival function simplifies exactly to
\[
\boxed{
\overline F(x)
=
\frac{\exp\{s(x)^{1-s(x)}\}-1}{e-1}.
}
\]

As \(x\uparrow x_G\), one has \(s(x)\downarrow0\), and therefore
\[
\boxed{
\frac{\overline F(x)}{\overline G(x)}
\longrightarrow
\frac{1}{e-1}.
}
\]
More precisely, with \(s=s(x)\),
\[
\boxed{
\overline F(x)
=
\frac{1}{e-1}
\left[
s-s^2\log s+\frac12s^2
+O\!\left(s^3\log^2s\right)
\right].
}
\]

If the baseline is absolutely continuous with positive density near \(x_G\), then its hazard is
\[
h_G(x)=\frac{g(x)}{s(x)}.
\]
The FEx-G hazard satisfies
\[
\boxed{
\frac{h_F(x)}{h_G(x)}\longrightarrow1.
}
\]
Thus FEx-G may alter finite-range hazard shapes, but it is asymptotically hazard-equivalent to its baseline at the upper endpoint.

Two consequences follow immediately. First, if the baseline upper tail is regularly varying,
\[
\overline G(x)=x^{-\alpha}L(x),
\qquad \alpha>0,
\]
then
\[
\overline F(x)
\sim
\frac{x^{-\alpha}L(x)}{e-1},
\]
so the regular-variation index is unchanged.

Second, for a nonnegative unbounded baseline and every \(r>0\),
\[
\boxed{
\operatorname E_F[X^r]<\infty
\quad\Longleftrightarrow\quad
\operatorname E_G[X^r]<\infty.
}
\]
The transform therefore cannot create or remove a positive-moment threshold.

For a Pareto-type baseline with index \(\alpha\), the extreme-quantile index is likewise unchanged. If \(Q_F\) and \(Q_G\) are the respective quantile functions, then under the standard regular-variation inversion,
\[
\frac{Q_F(1-u)}{Q_G(1-u)}
\longrightarrow
\left(\frac{1}{e-1}\right)^{1/\alpha}
\]
when the slowly varying factor admits the usual quantile-ratio limit, and in particular this equality holds for an exact Pareto baseline.

The structural message is that the transformation can substantially change central shape and hazard geometry while its ultimate upper-tail order remains locked to the baseline.

## Assumptions and scope
The tail-equivalence statement needs only a proper baseline CDF satisfying
\[
\overline G(x)\to0
\]
at its right endpoint.

The hazard-ratio statement additionally assumes absolute continuity and a positive baseline density sufficiently near the endpoint so both hazards are defined.

The moment-equivalence statement is asserted for nonnegative unbounded baselines. It uses the standard tail-integral characterization of positive moments.

The regular-variation corollary concerns baselines whose survival functions are regularly varying. No claim is made that every other extreme-value normalization is literally unchanged; the proved primitive statement is the positive-constant survival equivalence.

## Proof
Write
\[
s=\overline G(x).
\]
The FEx-G CDF is
\[
F(x)
=
\frac{e}{e-1}
\left[
1-\exp\{-1+s^{1-s}\}
\right].
\]
Therefore
\[
\begin{aligned}
\overline F(x)
&=1-F(x)\\
&=1-\frac{e}{e-1}
+\frac{e}{e-1}e^{-1+s^{1-s}}\\
&=\frac{e^{s^{1-s}}-1}{e-1}.
\end{aligned}
\]

Now
\[
s^{1-s}
=
s\exp(-s\log s)
=
s-s^2\log s
+O\!\left(s^3\log^2s\right).
\]
Using
\[
e^t-1=t+\frac12t^2+O(t^3)
\]
gives
\[
\overline F(x)
=
\frac{1}{e-1}
\left[
s-s^2\log s+\frac12s^2
+O\!\left(s^3\log^2s\right)
\right].
\]
Dividing by \(s\) proves
\[
\overline F(x)/\overline G(x)\to1/(e-1).
\]

For the hazard statement, define
\[
\phi(s)=\frac{e^{s^{1-s}}-1}{e-1}.
\]
Since
\[
\overline F(x)=\phi(s(x)),
\]
we have
\[
f_F(x)=\phi'(s)g(x).
\]
If
\[
t=s^{1-s},
\]
then
\[
t'=t\left(\frac1s-1-\log s\right),
\]
and hence
\[
\frac{h_F}{h_G}
=
\frac{s\phi'(s)}{\phi(s)}
=
\left(1-s-s\log s\right)
\frac{t e^t}{e^t-1}.
\]
Both factors tend to one as \(s\downarrow0\), proving the hazard-ratio limit.

For moments, positive-constant tail equivalence implies that for sufficiently large \(x\) there are constants \(0<c_1<c_2<\infty\) such that
\[
c_1\overline G(x)
\le
\overline F(x)
\le
c_2\overline G(x).
\]
For \(r>0\),
\[
\operatorname E[X^r]
=
r\int_0^\infty x^{r-1}\Pr(X>x)\,dx.
\]
The two tail integrals therefore converge or diverge together.

Regular variation is preserved because multiplication by a positive asymptotic constant does not change its index.

## Verification
The accompanying checker evaluates the exact survival map
\[
\phi(s)=\frac{e^{s^{1-s}}-1}{e-1}
\]
for survival probabilities spanning several orders of magnitude.

It verifies numerically that
\[
\phi(s)/s\to1/(e-1)
\]
and that the normalized residual after subtracting
\[
\frac{1}{e-1}
\left(s-s^2\log s+s^2/2\right)
\]
vanishes at the predicted rate.

The checker also evaluates the exact hazard ratio
\[
\left(1-s-s\log s\right)
\frac{s^{1-s}e^{s^{1-s}}}{e^{s^{1-s}}-1}
\]
and confirms convergence to one.

For an exact Pareto baseline it numerically inverts the transformed survival and verifies the extreme-quantile constant
\[
(1/(e-1))^{1/\alpha}.
\]
These computations are reproducibility aids; the general result is analytic.

## Relationship to prior work
The primary article defines the FEx-G transformation and emphasizes its ability to change density, hazard, skewness, and tail behavior without adding parameters. It derives a power-series representation around the lower endpoint and studies five submodels.

For the bounded FEx-Kumaraswamy submodel, the article later proves the special endpoint relation
\[
h(t)\sim\frac{b}{1-t}
\]
as \(t\uparrow1\). The baseline Kumaraswamy hazard has the same asymptotic form. This is consistent with, but does not state, the general theorem
\[
h_F/h_G\to1
\]
for every absolutely continuous baseline.

A 2025 paper with the same family label uses a different construction,
\[
F(x)=1-\exp\left[-G_1(x)^\nu/\overline G_2(x)^\omega\right],
\]
with two baselines and additional shape parameters. Its tail properties therefore do not cover the parameter-free 2026 transformation studied here.

General T-X theory supplies the composition framework but does not determine the endpoint asymptotics of this particular nonlinear map. Focused literature searches using survival equivalence, hazard equivalence, regular variation, moment thresholds, and the exact DOI did not locate the present baseline-uniform theorem.

## Limitations
The theorem characterizes the ultimate upper endpoint. It does not prevent the transformation from producing substantial finite-range changes in hazard shape, skewness, or fit.

The hazard-ratio conclusion needs a differentiable baseline with positive density near the endpoint.

The quantile-ratio constant is automatic for exact Pareto tails; for general regular variation, the displayed simple quantile ratio requires the usual regularity on the slowly varying factor.

A recent unindexed source may contain an equivalent endpoint theorem.

## References
1. E. M. Eldemery, H. M. Almongy, K. M. Mahfouz, M. M. El Genidy, I. Elbatal, H. M. Aljohani, and A. Z. Afify, “A unified parsimonious exponential-G family for modeling real-world data: theory and statistical inference,” AIMS Mathematics 11 (2026), 13865–13912. DOI: 10.3934/math.2026571.
2. J. N. Al Abbasi, I. Elbatal, A. Z. Afify, and H. A. Mahran, “A novel flexible exponential-G family: Properties, estimation, and applications in environmental and engineering sciences,” Journal of King Saud University – Science 37 (2025), 8202025. DOI: 10.25259/JKSUS_820_2025.
3. M. Alzaatreh, C. Lee, and F. Famoye, “On generating T-X family of distributions using quantile functions,” Journal of Statistical Distributions and Applications 1 (2014), 2. DOI: 10.1186/2195-5832-1-2.
