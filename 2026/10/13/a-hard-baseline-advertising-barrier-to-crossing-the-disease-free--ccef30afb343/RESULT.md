# A hard baseline-advertising barrier to crossing the disease-free threshold

## Finding

In the epidemic-awareness model, define
\[
\mathcal R_0=
\frac{\beta\Lambda}{d(\nu+\alpha+d)}
\]
and
\[
c=\lambda_0+d.
\]
The source gives the media-modified reproduction number
\[
\mathcal R_1(M_0)
=
\mathcal R_0
\frac{c(p+M_0)}
{\lambda M_0+c(p+M_0)}.
\]

Although \(\mathcal R_1\) decreases strictly as the maintained baseline number of advertisements \(M_0\) increases, it cannot be reduced arbitrarily far. Its exact floor is
\[
\lim_{M_0\to\infty}\mathcal R_1(M_0)
=
\mathcal R_0\frac{c}{\lambda+c}.
\]

Suppose
\[
\mathcal R_0>1.
\]
A finite \(M_0\) with
\[
\mathcal R_1<1
\]
exists if and only if
\[
\lambda>(\mathcal R_0-1)c.
\]
When this strict inequality holds, the unique crossing is
\[
M_{0,c}
=
\frac{(\mathcal R_0-1)cp}
{\lambda-(\mathcal R_0-1)c},
\]
and
\[
\mathcal R_1<1
\quad\Longleftrightarrow\quad
M_0>M_{0,c}.
\]

If instead
\[
\lambda<(\mathcal R_0-1)c,
\]
even an arbitrarily large baseline cannot reach the subunit threshold. At equality, every finite \(M_0\) still has \(\mathcal R_1>1\), with \(\mathcal R_1\downarrow1\) only in the infinite-baseline limit.

For the source's Table 1 values,
\[
\mathcal R_0\approx1.8745313672,
\qquad
(\mathcal R_0-1)c\approx0.0070312322.
\]
The source uses
\[
\lambda=0.012,
\]
so crossing is possible in principle, but requires
\[
M_0>1698.1028207.
\]
At the printed value
\[
M_0=500,
\]
one obtains
\[
\mathcal R_1\approx1.3026792112.
\]
Equivalently, if \(M_0=500\) is fixed, the dissemination rate must satisfy
\[
\lambda>0.0239061895
\]
to cross \(\mathcal R_1=1\).

## Assumptions and scope

All demographic and media parameters in the source model are positive. The main classification assumes
\[
\mathcal R_0>1,
\]
because if \(\mathcal R_0\le1\), the disease-free threshold is already subunit without baseline advertising.

The source proves local asymptotic stability of its disease-free equilibrium for
\[
\mathcal R_1<1
\]
and instability for
\[
\mathcal R_1>1.
\]
The finding therefore classifies reachability of that local threshold. It does not independently assert global attraction of the disease-free equilibrium.

The maintained baseline \(M_0\) is treated as the source defines it: a nonnegative number of advertisements continuously present in the region.

## Proof

At the disease-free equilibrium,
\[
I=0,\qquad
N=\frac{\Lambda}{d},\qquad
M=M_0.
\]
The aware-population balance is
\[
\lambda\frac{M_0}{p+M_0}(N-A)-cA=0.
\]
Hence
\[
A_0
=
\frac{\Lambda}{d}
\frac{\lambda M_0}
{\lambda M_0+c(p+M_0)},
\]
and the susceptible population is
\[
S_0
=
\frac{\Lambda}{d}
\frac{c(p+M_0)}
{\lambda M_0+c(p+M_0)}.
\]
Therefore
\[
\mathcal R_1
=
\frac{\beta S_0}{\nu+\alpha+d}
=
\mathcal R_0
\frac{c(p+M_0)}
{\lambda M_0+c(p+M_0)}.
\]

Differentiate with respect to \(M_0\):
\[
\frac{d\mathcal R_1}{dM_0}
=
-\frac{
\mathcal R_0c\lambda p
}{
\left(cp+(\lambda+c)M_0\right)^2
}
<0.
\]
Thus \(\mathcal R_1\) is strictly decreasing, and
\[
\lim_{M_0\to\infty}\mathcal R_1
=
\mathcal R_0\frac{c}{\lambda+c}.
\]

For \(\mathcal R_0>1\), the limiting value is below one exactly when
\[
\mathcal R_0c<\lambda+c,
\]
or
\[
\lambda>(\mathcal R_0-1)c.
\]
This proves the reachability condition.

When the strict inequality holds, solving
\[
\mathcal R_1=1
\]
gives
\[
(\mathcal R_0-1)cp
=
\left(\lambda-(\mathcal R_0-1)c\right)M_0,
\]
hence
\[
M_{0,c}
=
\frac{(\mathcal R_0-1)cp}
{\lambda-(\mathcal R_0-1)c}.
\]
Strict monotonicity then gives the complete side-of-threshold classification.

For fixed \(M_0>0\), the same inequality rearranges to
\[
\lambda>
(\mathcal R_0-1)c
\left(1+\frac{p}{M_0}\right).
\]

The limiting susceptible fraction follows directly from the disease-free balance:
\[
\lim_{M_0\to\infty}\frac{S_0}{N_0}
=
\frac{c}{\lambda+c}.
\]
Thus the reproduction-number floor is the epidemiological reflection of saturation in the awareness-transfer rate.

## Verification

The bundled `verify.py` uses exact rational arithmetic for the source's Table 1 values.

It reconstructs
\[
\mathcal R_0=\frac{7500}{4001},
\]
verifies the derivative sign symbolically through the closed form, and checks the exact equivalence between the finite-baseline crossing and the awareness-rate condition.

It also evaluates
\[
M_{0,c}\approx1698.1028207,
\qquad
\mathcal R_1(500)\approx1.3026792112,
\]
and
\[
\lambda_c(500)\approx0.0239061895.
\]

No finite parameter scan is used to prove the classification.

## Relationship to prior work

The motivating article derives the disease-free equilibrium and the modified reproduction number \(\mathcal R_1\), then explores the joint effect of \(\lambda\) and \(M_0\) with a contour plot. It states that larger dissemination and baseline advertising can push \(\mathcal R_1\) below one, but it does not give the exact condition determining whether increasing \(M_0\) can ever cross the threshold.

Agaba, Kyrychko, and Blyuss analyze a different awareness-coupled epidemic model with private and public awareness and derive awareness-dependent epidemic thresholds. Their model supports the broader principle that awareness changes invasion thresholds, but it does not contain the source's saturating baseline-advertising balance or imply the barrier above.

A later model by Rai, Tiwari, Kang, and Misra also includes a maintained baseline of social-media advertisements and numerically identifies baseline levels associated with disease-free dynamics in a richer literacy-structured system. That later result establishes the relevance of baseline-advertising thresholds but does not imply the exact closed-form reachability classification for the simpler 2018 model.

Targeted searches by source identity, the \(\mathcal R_1\) formula, baseline-advertising threshold language, infinite-baseline limits, and equivalent awareness-rate conditions did not locate this source-specific classification.

## Limitations

The result is a threshold-reachability statement for the deterministic model and its disease-free linearization.

It does not optimize the economic cost of advertisements, model message fatigue beyond the source equations, or compare baseline advertising with treatment or vaccination.

It does not assert that \(\mathcal R_1<1\) is sufficient for global eradication from every initial condition unless an additional global-stability result is supplied.

## References

1. A. K. Misra, R. K. Rai, Y. Takeuchi, “Modeling the control of infectious diseases: Effects of TV and social media advertisements,” Mathematical Biosciences and Engineering 15 (2018), 1315–1343. DOI: 10.3934/mbe.2018061.
2. G. O. Agaba, Y. N. Kyrychko, K. B. Blyuss, “Mathematical model for the impact of awareness on the dynamics of infectious diseases,” Mathematical Biosciences 286 (2017), 22–30. DOI: 10.1016/j.mbs.2017.01.009.
3. R. K. Rai, P. K. Tiwari, Y. Kang, A. K. Misra, “Modeling the effect of literacy and social media advertisements on the dynamics of infectious diseases,” Mathematical Biosciences and Engineering 17 (2020), 5812–5848. DOI: 10.3934/mbe.2020311.
