# Stress increases force upward hazard jumps in the IZL cumulative-exposure model
## Finding
Let the inverted Z–Lindley distribution have cumulative distribution function
\[
F(t;\alpha)
=
\left(
1+\frac{\alpha}{2(1+\alpha)t}
\right)e^{-\alpha/t},
\qquad
t>0,\quad \alpha>0,
\]
and let
\[
h(t;\alpha)
=
\frac{f(t;\alpha)}{1-F(t;\alpha)}
\]
be its hazard rate.

For each
\[
0<p<1,
\]
write
\[
Q_p(\alpha)=F^{-1}(p;\alpha)
\]
and define the hazard evaluated at a fixed cumulative-failure level,
\[
H_p(\alpha)
=
h(Q_p(\alpha);\alpha).
\]

Then
\[
\boxed{
\frac{d}{d\alpha}H_p(\alpha)<0
\qquad
\text{for every }\alpha>0,\ 0<p<1.
}
\]
Thus, at a common cumulative exposure level, the instantaneous failure rate is strictly larger for the smaller IZL parameter.

This gives an exact direction theorem for the step-stress cumulative-exposure model. Suppose the first stage has parameter \(\alpha_1\), the second stage has parameter \(\alpha_2\), the stress changes at time \(\tau\), and the equivalent stage-two age \(e\) is chosen by
\[
F(e;\alpha_2)
=
F(\tau;\alpha_1)
=
p.
\]
Then
\[
h_G(\tau^-)=H_p(\alpha_1),
\qquad
h_G(\tau^+)=H_p(\alpha_2).
\]
Therefore
\[
\boxed{
\alpha_1>\alpha_2
\quad\Longrightarrow\quad
h_G(\tau^+)>h_G(\tau^-).
}
\]

Because the cumulative-exposure construction makes the survival probability continuous at the switch,
\[
1-F(e;\alpha_2)
=
1-F(\tau;\alpha_1),
\]
the density jump has the same sign:
\[
\boxed{
\alpha_1>\alpha_2
\quad\Longrightarrow\quad
f(e;\alpha_2)>f(\tau;\alpha_1).
}
\]

The direction is independent of the chosen change time. More generally, at any matched-exposure boundary in a multi-step model:

\[
\boxed{
\begin{array}{ll}
\alpha_{\mathrm{after}}<\alpha_{\mathrm{before}}
&\Longrightarrow\text{ upward hazard and density jump},\\[4pt]
\alpha_{\mathrm{after}}>\alpha_{\mathrm{before}}
&\Longrightarrow\text{ downward hazard and density jump},\\[4pt]
\alpha_{\mathrm{after}}=\alpha_{\mathrm{before}}
&\Longleftrightarrow\text{ continuous hazard and density}.
\end{array}
}
\]

For the parameter values displayed in Figure 1 of the 2026 step-stress paper,
\[
\alpha_1=1.5,
\qquad
\alpha_2=0.7,
\qquad
p=0.4,
\]
the matched ages are approximately
\[
Q_p(1.5)=1.3415552521,
\qquad
Q_p(0.7)=0.5720293366.
\]
The corresponding hazards are
\[
h(Q_p(1.5);1.5)=0.4648096557\ldots
\]
and
\[
h(Q_p(0.7);0.7)=1.1177202352\ldots.
\]
Thus the rate jumps upward by the factor
\[
\boxed{
2.404683\ldots.
}
\]

## Assumptions and scope
The parameter domain is
\[
\alpha>0,
\]
and the lifetime support is
\[
t>0.
\]
The cumulative level satisfies
\[
0<p<1.
\]

The result concerns the instantaneous hazard evaluated at ages having the same IZL cumulative probability. That is exactly the comparison required by the cumulative-exposure matching rule at a stress boundary.

The result does not claim that the ordinary hazard
\[
h(t;\alpha)
\]
is monotone in \(\alpha\) at a fixed chronological age \(t\). The matched-exposure age changes with \(\alpha\), and that change is essential.

The parent IZL hazard is itself upside-down-bathtub shaped as a function of age. The new statement is different: it is monotonicity in the distribution parameter after reparameterizing age by cumulative exposure.

## Proof
Fix
\[
0<p<1.
\]
Set
\[
b=1+\alpha>1
\]
and
\[
x=\frac{\alpha}{Q_p(\alpha)}>0.
\]
The quantile equation becomes
\[
p
=
\left(
1+\frac{x}{2b}
\right)e^{-x}.
\]

Differentiate implicitly with respect to \(b\). Since \(p\) is fixed,
\[
\frac{dx}{db}
=
-\frac{x}{b(2b+x-1)}.
\]

At the quantile, the density can be simplified using the same fixed-\(p\) equation. Starting from
\[
f(t;\alpha)
=
\frac{\alpha}{2(1+\alpha)t^2}
\left(
1+2\alpha+\frac{\alpha}{t}
\right)e^{-\alpha/t},
\]
substitute
\[
t=\frac{\alpha}{x}
\]
and
\[
e^{-x}
=
\frac{2bp}{2b+x}.
\]
This yields
\[
f(Q_p(\alpha);\alpha)
=
p\,
\frac{x^2(2b+x-1)}
{(b-1)(2b+x)}.
\]
Therefore
\[
H_p(\alpha)
=
\frac{p}{1-p}
\frac{x^2(2b+x-1)}
{(b-1)(2b+x)}.
\]

Differentiate its logarithm and substitute the formula for \(dx/db\):
\[
\frac{d}{db}\log H_p
=
-
\frac{
4b^3+4b^2x-2b^2+bx^2-2b-2x+1
}{
b(b-1)(2b+x-1)^2
}.
\]

It remains to prove positivity of the numerator
\[
N(b,x)
=
4b^3+4b^2x-2b^2+bx^2-2b-2x+1.
\]
At
\[
b=1,
\]
one has
\[
N(1,x)=(x+1)^2>0.
\]
Moreover,
\[
\frac{\partial N}{\partial b}
=
12b^2+8bx-4b+x^2-2.
\]
At \(b=1\),
\[
\frac{\partial N}{\partial b}(1,x)
=
x^2+8x+6>0,
\]
and
\[
\frac{\partial^2 N}{\partial b^2}
=
24b+8x-4>0
\]
for \(b\ge1\) and \(x>0\). Hence \(N(b,x)>0\) for every \(b>1\), so
\[
\frac{d}{db}\log H_p<0.
\]
Since \(db/d\alpha=1\),
\[
\frac{d}{d\alpha}H_p(\alpha)<0.
\]

At a cumulative-exposure switch, both sides have the same CDF value \(p\), hence the same survival \(1-p\). The sign of the density jump is therefore the sign of the hazard jump. This proves all three boundary cases.

## Verification
The included checker independently evaluates the IZL CDF, PDF, hazard, and quantiles.

It verifies the implicit derivative
\[
\frac{dx}{db}
=
-\frac{x}{b(2b+x-1)}
\]
against finite differences over a grid of parameter and quantile values.

It also checks the closed logarithmic derivative of \(H_p\) against numerical differentiation and confirms that it is negative throughout the test grid.

For the source's Figure 1 values
\[
(\alpha_1,\alpha_2,p)=(1.5,0.7,0.4),
\]
the checker obtains
\[
Q_p(1.5)=1.3415552521\ldots,
\qquad
Q_p(0.7)=0.5720293366\ldots,
\]
and
\[
H_p(1.5)=0.4648096557\ldots,
\qquad
H_p(0.7)=1.1177202352\ldots.
\]

Finally, random matched-exposure pairs are checked numerically to confirm the analytic sign classification. These numerical checks are reproducibility aids; the strict inequality is proved symbolically above.

## Relationship to prior work
The 2026 step-stress paper defines the two-stage cumulative-exposure model with
\[
\alpha_1>\alpha_2
\]
when stress is raised. Its Proposition 2 proves continuity of the cumulative exposure and writes the hazard jump as
\[
\frac{f(e;\alpha_2)-f(\tau;\alpha_1)}{1-p}.
\]
The paper describes this jump as the signature of the harsher stage and illustrates it numerically in Figure 1, but the displayed proposition does not determine the sign of the difference for all admissible parameters and all change times.

The parent 2026 IZL paper proves the upside-down-bathtub age shape of the hazard and gives a closed-form Lambert-\(W\) quantile. It does not state monotonicity of the hazard at a fixed quantile with respect to \(\alpha\).

General cumulative-exposure literature explains equivalent-age matching across stress stages, but it does not supply the IZL-specific parameter-ordering theorem above.

Focused searches using the exact step-stress DOI, the IZL model name, quantile-hazard terminology, cumulative-exposure hazard jumps, and parameter-ordering aliases did not locate a published theorem equivalent to the result stated here.

## Limitations
The theorem is specific to the one-parameter IZL family and its cumulative-exposure matching rule.

It classifies the instantaneous jump at a stress boundary; it does not compare complete post-switch hazard trajectories at unequal cumulative exposure levels.

The result validates the direction of the jump implied by the source's parameter ordering but does not by itself establish the correctness of any particular stress-to-parameter link outside the fitted test levels.

A very recent unindexed result could exist outside the sources examined.

## References
1. A. H. Alenezy, L. S. Diab, K. A. Rashedi, and G. A. Marei, “Inference for a step-stress model under the inverted Z-Lindley distribution with progressive Type-II censoring,” AIMS Mathematics 11 (2026), 31919–31962. DOI: 10.3934/math.20261256.
2. O. A. Alqasem and A. Elshahhat, “A New One-Parameter Model Supports an Upside-Down Bathtub Failure Rate: Theory, Inference, and Real-World Applications,” Mathematics 14 (2026), 1566. DOI: 10.3390/math14091566.
3. E. Cramer, “Ordered and censored lifetime data in reliability: An illustrative review,” WIREs Computational Statistics 15 (2023), e1571. DOI: 10.1002/wics.1571.
