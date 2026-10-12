# The discrete Wiener-range paper confuses union exceedance with joint survival
## Finding
Let
\[
\mathbf R=(R_1,\ldots,R_n)
\]
be the independent discrete Wiener-range vector constructed in the 2026 source, and let
\[
F_i(r_i)=\Pr(R_i\le r_i).
\]
The paper correctly writes the joint CDF as
\[
F(\mathbf r)
=
\prod_{i=1}^n F_i(r_i).
\]

It then defines its “joint survival function” by
\[
S_{\mathrm{pub}}(\mathbf r)
=
1-F(\mathbf r)
=
1-\prod_{i=1}^nF_i(r_i).
\]
For more than one component, this is not the probability that all ranges exceed their thresholds. By De Morgan's law,
\[
\boxed{
S_{\mathrm{pub}}(\mathbf r)
=
\Pr\!\left(
\bigcup_{i=1}^n\{R_i>r_i\}
\right),
}
\]
the probability that at least one range exceeds its threshold.

The strict joint co-exceedance survival is instead
\[
\boxed{
S_{\cap}(\mathbf r)
=
\Pr(R_i>r_i\text{ for every }i)
=
\prod_{i=1}^n\{1-F_i(r_i)\}.
}
\]
For the inclusive conditioning used by the paper's discrete hazard,
\[
\boxed{
S_{\cap}^{\ge}(\mathbf r)
=
\Pr(R_i\ge r_i\text{ for every }i)
=
\prod_{i=1}^n\{1-F_i(r_i-1)\}.
}
\]

The distinction becomes asymptotically extreme. For two independent identically distributed margins, write
\[
s(r)=1-F(r).
\]
Then
\[
S_{\mathrm{pub}}(r,r)
=
2s(r)-s(r)^2,
\]
while
\[
S_{\cap}(r,r)
=
s(r)^2.
\]
Therefore
\[
\boxed{
\frac{S_{\mathrm{pub}}(r,r)}
{S_{\cap}(r,r)}
=
\frac{2}{s(r)}-1.
}
\]
Since
\[
s(r)\to0
\]
as
\[
r\to\infty,
\]
the ratio diverges to infinity. Thus the source's plotted “joint survival” can overstate simultaneous extreme-range probability by an arbitrarily large multiplicative factor in the far tail.

More generally, for \(n\) identical independent margins,
\[
S_{\mathrm{pub}}
=
1-\{1-s\}^n
\sim ns,
\qquad
S_{\cap}
=
s^n,
\]
so
\[
\boxed{
\frac{S_{\mathrm{pub}}}{S_{\cap}}
\sim
n s^{1-n}.
}
\]

The same event error survives the paper's componentwise double truncation. Its truncated joint PMF is a product of normalized marginal truncated PMFs, so independence is preserved. Hence the correct truncated co-survival is again a product of marginal truncated survivals, not
\[
1-\bar F_1\bar F_2.
\]

This also exposes an internal inconsistency in the hazard section. Proposition 1 correctly defines the bivariate discrete hazard as
\[
\Pr(
R_1=r_1,R_2=r_2
\mid
R_1\ge r_1,R_2\ge r_2
)
\]
and correctly states that its denominator factorizes into marginal survival probabilities. For componentwise truncation, the same conditional event gives
\[
\boxed{
\bar H(r_1,r_2)
=
\frac{
\bar p_1(r_1)\bar p_2(r_2)
}{
\{1-\bar F_1(r_1-1)\}
\{1-\bar F_2(r_2-1)\}
}.
}
\]
The paper's truncated Eq. (3.6), which uses
\[
\bar f(r_1,r_2)\{1-\bar F(r_1,r_2)\}^{-1},
\]
conditions on a different union-exceedance quantity and therefore is not the conditional hazard defined in Proposition 1.

Consequently, Figures 5 and 6 and the empirical Figure 16 do not represent the probability that all plotted range coordinates exceed the stated limits, despite the accompanying simultaneous-exceedance interpretation.

## Assumptions and scope
The claim uses only the independence structure explicitly assumed by the source and the standard event meanings of its displayed CDF and hazard conditioning.

There are two common lattice conventions for survival:
\[
\Pr(R_i>r_i)
\]
and
\[
\Pr(R_i\ge r_i).
\]
The correction states both. The source's Eq. (2.4) fails under either convention: \(1-\prod_iF_i(r_i)\) is a union event, whereas joint survival for simultaneous exceedance is an intersection event.

The result does not challenge the univariate Wiener-range discretization, its marginal PMF, or the product joint PMF. It corrects the multivariate tail event and the downstream co-exceedance interpretation.

The paper's untruncated Proposition 1 hazard is not rejected; its product-of-marginal-survivals denominator is the correct structure. The inconsistency arises because the paper's earlier “joint survival” and its later truncated hazard use \(1-F_{\mathrm{joint}}\) instead.

## Proof
For any events
\[
A_i=\{R_i\le r_i\},
\]
the joint CDF is
\[
F(\mathbf r)
=
\Pr\!\left(\bigcap_i A_i\right).
\]
Therefore
\[
1-F(\mathbf r)
=
\Pr\!\left(
\left(\bigcap_i A_i\right)^c
\right)
=
\Pr\!\left(
\bigcup_i A_i^c
\right)
=
\Pr\!\left(
\bigcup_i\{R_i>r_i\}
\right).
\]
This proves that the published complement is an at-least-one-exceedance probability.

By contrast, simultaneous strict exceedance is
\[
\Pr\!\left(
\bigcap_i\{R_i>r_i\}
\right).
\]
Independence gives
\[
\Pr\!\left(
\bigcap_i\{R_i>r_i\}
\right)
=
\prod_i\Pr(R_i>r_i)
=
\prod_i\{1-F_i(r_i)\}.
\]

The inclusive version is identical after shifting each discrete marginal CDF by one lattice point:
\[
\Pr(R_i\ge r_i)
=
1-F_i(r_i-1).
\]

For identical margins, set
\[
s=1-F(r).
\]
The published quantity is
\[
1-(1-s)^2
=
2s-s^2,
\]
while simultaneous exceedance is
\[
s^2.
\]
Their ratio is
\[
2/s-1,
\]
which diverges because every proper nonnegative range distribution satisfies
\[
s(r)\to0.
\]

Rectangular componentwise truncation preserves independence because the conditioning event factors by coordinate. The source's own Eq. (3.2) displays this factorization explicitly. Therefore the same product rule applies to the truncated marginal survivals.

Finally, the conditional hazard identity is immediate:
\[
\Pr(
\mathbf R=\mathbf r
\mid
R_i\ge r_i\text{ for every }i
)
=
\frac{
\prod_i p_i(r_i)
}{
\prod_i\Pr(R_i\ge r_i)
}.
\]
The corresponding formula remains true after componentwise truncation. Replacing the denominator by
\[
1-F_{\mathrm{joint}}(\mathbf r)
\]
changes the conditioning event from simultaneous survival to the union that at least one coordinate exceeds its threshold.

## Verification
The included checker verifies the event algebra for arbitrary marginal CDF values and then evaluates two diagnostic examples.

If
\[
F_1(r_1)=F_2(r_2)=\frac12,
\]
the paper's complement gives
\[
1-F_1F_2=\frac34,
\]
whereas simultaneous strict exceedance is
\[
(1-F_1)(1-F_2)=\frac14.
\]

For identical strict marginal tail \(s\), the checker confirms
\[
\frac{1-(1-s)^2}{s^2}
=
\frac2s-1
\]
and the divergence of this ratio as \(s\) decreases.

A separate geometric-lattice example checks the hazard inconsistency. For two independent geometric variables with cell hazard \(1/2\), the conditional joint hazard is \(1/4\) at every lattice point, while dividing the joint cell probability by \(1-F_{\mathrm{joint}}\) produces a different value. This check is distribution-independent evidence for the event mismatch; the analytic proof above is decisive.

## Relationship to prior work
The 2026 source assumes independent Wiener ranges, gives a product joint PMF and product joint CDF, and then labels
\[
1-F_{\mathrm{joint}}
\]
as “joint survival.” It explicitly says this function estimates probabilities of threshold exceedance, characterizes tail dependence, and detects co-excesses. Its Figure 16 caption similarly says the truncated joint survival represents the probability that both plotted range values exceed limits.

The same paper later supplies the correct event-level definition in Proposition 1:
\[
\Pr(
R_1=r_1,R_2=r_2
\mid
R_1\ge r_1,R_2\ge r_2
),
\]
and states that independence makes the joint survival probability in the denominator a product of marginal survivals. This directly conflicts with Eq. (2.4).

A closely related 2025 continuous Wiener-range paper by Alraddadi and El-Hadidy also writes a complement-of-joint-CDF quantity as a multivariate survival function while discussing simultaneous upper-tail movements. It therefore propagates the same convention rather than supplying a correction.

Standard bivariate discrete survival implementations define joint survival through simultaneous exceedance. For example, the documented Basu–Dhar bivariate geometric survival is
\[
\Pr(X\ge x,Y\ge y).
\]
Focused searches using the exact DOI, the paper title, joint-survival, co-exceedance, hazard, and truncation aliases did not locate a corrigendum or a published source already correcting the 2026 formulas.

## Limitations
The correction distinguishes simultaneous co-exceedance from at-least-one exceedance. The latter is itself a meaningful risk quantity: it is the survival of the coordinatewise maximum event. It should simply not be interpreted as the probability that all assets jointly exceed their thresholds.

The numerical figures in the source are not regenerated here. Their event interpretation follows directly from the formulas used to generate them.

No dependence model beyond the source's independence assumption is analyzed.

## References
1. S. A. Alharbi and M. A. A. El-Hadidy, “A multivariate discrete Wiener range distribution with truncation: Theory, reliability properties, and applications to constrained financial markets,” AIMS Mathematics 11 (2026), 3563–3593. DOI: 10.3934/math.2026146.
2. R. M. Alraddadi and M. A. A. El-Hadidy, “A multivariate model for the Wiener process range, with statistical properties under stochastic volatility,” AIMS Mathematics 10 (2025), 22023–22052. DOI: 10.3934/math.2025980.
3. R. P. de Oliveira and J. A. Achcar, documentation for bivariate geometric survival functions, referring to Roy's discrete bivariate reliability formulation.
