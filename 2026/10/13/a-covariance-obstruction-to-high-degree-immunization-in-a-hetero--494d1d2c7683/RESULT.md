# A covariance obstruction to high-degree immunization in a heterogeneous network SIS model

## Finding

For the finite-degree heterogeneous SIS model of Huang and Jiang, define the epidemic weight of degree class \(k\) by
\[
w_k=\phi(k)f_k'(0).
\]
If susceptible degree class \(k\) is immunized at fraction \(\sigma_k\), the source's threshold formula is
\[
\mathcal R_0^{\mathrm{prof}}
=
\frac{\langle (1-\sigma_k)w_k\rangle}
{(\mu+\gamma)\langle k\rangle}.
\]
Let
\[
\bar\sigma=\langle\sigma_k\rangle.
\]
Uniform immunization at the same average coverage has
\[
\mathcal R_0^{\mathrm U}
=
\frac{(1-\bar\sigma)\langle w\rangle}
{(\mu+\gamma)\langle k\rangle}.
\]
The exact difference is therefore
\[
\boxed{
\mathcal R_0^{\mathrm{prof}}-\mathcal R_0^{\mathrm U}
=-\frac{\operatorname{Cov}_P(\sigma_k,w_k)}{(\mu+\gamma)\langle k\rangle}
}.
\]
Hence equal-budget targeting beats uniform immunization if and only if
\[
\operatorname{Cov}_P(\sigma_k,w_k)>0.
\]

The source's assumptions do not imply this sign. They require \(\phi(k)\le k\) and, for each degree, a nonnegative increasing concave infection-rate function \(f_k\), but they impose no monotonicity in \(k\) on the product \(\phi(k)f_k'(0)\). Consequently, high-degree targeting can put more vaccine on classes with *smaller* epidemic weight.

An exact two-degree example reverses the source's equal-budget comparison. Let
\[
P(1)=P(2)=\frac12,
\qquad
\phi(1)=\phi(2)=1,
\qquad
\mu=\gamma=\frac2{15},
\]
and
\[
f_1(\Theta)=\frac45\frac{\Theta}{1+\Theta},
\qquad
f_2(\Theta)=\frac15\frac{\Theta}{1+\Theta}.
\]
Then
\[
w_1=\frac45,
\qquad
w_2=\frac15,
\qquad
\langle k\rangle=\frac32,
\]
and
\[
\mathcal R_0
=
\frac{1/2}{(4/15)(3/2)}
=
\frac54>1.
\]

Apply the source's targeted rule with \(k_c=2\) and \(c=1/2\). Thus
\[
(\sigma_1,\sigma_2)=\left(0,\frac12\right),
\qquad
\bar\sigma=\frac14.
\]
The covariance is
\[
\operatorname{Cov}_P(\sigma_k,w_k)
=
\frac1{20}-\frac14\frac12
=-\frac3{40}.
\]
The targeted threshold is
\[
\mathcal R_0^{\mathrm T}
=
\frac{1/2-1/20}{2/5}
=
\frac98>1,
\]
whereas uniform immunization at the same average coverage gives
\[
\mathcal R_0^{\mathrm U}
=
\left(1-\frac14\right)\frac54
=
\frac{15}{16}<1.
\]
So the uniform scheme is subcritical while the high-degree targeted scheme is supercritical at the same average vaccination coverage.

For two degree classes, if \(w_1>w_2\) and \(\sigma_1\le\sigma_2\), then
\[
\operatorname{Cov}_P(\sigma_k,w_k)
=
P(1)P(2)(\sigma_2-\sigma_1)(w_2-w_1)\le0.
\]
Thus in this admissible example no nonconstant high-degree threshold profile can satisfy the positive-covariance premise used in the source's comparison argument.

## Assumptions and scope

The model has a finite maximum degree \(n\), positive degree probabilities \(P(k)\), and infection pressure
\[
\Theta(t)=\frac1{\langle k\rangle}\sum_k\phi(k)P(k)I_k(t).
\]
The source assumes \(\phi(k)\le k\) and, for every degree class,
\[
f_k(\Theta)\ge0,
\qquad
f_k(\Theta)=0\ \text{only at}\ \Theta=0,
\qquad
f_k'(\Theta)>0,
\qquad
f_k''(\Theta)\le0.
\]
The counterexample uses \(n=2\), positive probabilities, positive demographic rates, and \(\phi(k)\le k\). For \(a>0\), the function
\[
f(\Theta)=a\frac{\Theta}{1+\Theta}
\]
has
\[
f'(\Theta)=\frac{a}{(1+\Theta)^2}>0,
\qquad
f''(\Theta)=-\frac{2a}{(1+\Theta)^3}<0,
\]
so both chosen infection-rate functions satisfy the source's hypotheses throughout the biologically relevant interval.

The finding does not say high-degree targeting is generally inferior. It identifies the exact missing condition: at equal average coverage, efficiency is ordered by the covariance between immunization intensity and the epidemic weight \(w_k\).

## Proof

Write
\[
D=(\mu+\gamma)\langle k\rangle.
\]
The source's degree-dependent immunization threshold is
\[
\mathcal R_0^{\mathrm{prof}}
=
\frac{\langle w\rangle-\langle\sigma w\rangle}D.
\]
By the definition of covariance,
\[
\langle\sigma w\rangle
=
\bar\sigma\langle w\rangle
+
\operatorname{Cov}_P(\sigma,w).
\]
Therefore
\[
\mathcal R_0^{\mathrm{prof}}
=
\frac{(1-\bar\sigma)\langle w\rangle}D
-
\frac{\operatorname{Cov}_P(\sigma,w)}D
=
\mathcal R_0^{\mathrm U}
-
\frac{\operatorname{Cov}_P(\sigma,w)}D.
\]
This proves the if-and-only-if comparison.

For the exact example,
\[
\langle w\rangle
=
\frac12\left(\frac45+\frac15\right)
=
\frac12,
\qquad
D
=
\left(\frac4{15}\right)\left(\frac32\right)
=
\frac25.
\]
Thus \(\mathcal R_0=(1/2)/(2/5)=5/4\).

For the targeted profile,
\[
\langle\sigma w\rangle
=
\frac12\left(0\cdot\frac45+\frac12\cdot\frac15\right)
=
\frac1{20},
\]
so
\[
\mathcal R_0^{\mathrm T}
=
\frac{1/2-1/20}{2/5}
=
\frac98.
\]
Uniform coverage \(\bar\sigma=1/4\) gives
\[
\mathcal R_0^{\mathrm U}
=
\frac34\frac54
=
\frac{15}{16}.
\]
The same arithmetic gives
\[
\operatorname{Cov}_P(\sigma,w)
=
-\frac3{40},
\]
and verifies
\[
\mathcal R_0^{\mathrm T}-\mathcal R_0^{\mathrm U}
=
\frac3{16}
=
-\frac{-3/40}{2/5}.
\]

Finally, for two classes a direct expansion gives
\[
\operatorname{Cov}_P(\sigma,w)
=
P(1)P(2)(\sigma_2-\sigma_1)(w_2-w_1).
\]
Since the example has \(w_1>w_2\), every nonconstant immunization profile increasing with degree has negative covariance.

## Verification

The bundled `verify.py` uses exact rational arithmetic to reproduce
\[
\mathcal R_0=\frac54,
\qquad
\mathcal R_0^{\mathrm U}=\frac{15}{16},
\qquad
\mathcal R_0^{\mathrm T}=\frac98,
\qquad
\operatorname{Cov}_P(\sigma,w)=-\frac3{40}.
\]
It also checks the exact covariance-difference identity and the two-class covariance factorization for representative monotone targeted profiles.

The sign conditions on the infection-rate derivatives are proved analytically from their displayed formulas; no finite sample or trajectory simulation is used to infer the threshold reversal.

## Relationship to prior work

Huang and Jiang derive the degree-dependent threshold
\[
\mathcal R_0^{\mathrm T}
=
\frac{\langle w\rangle-\langle\sigma w\rangle}
{(\mu+\gamma)\langle k\rangle}
\]
and explicitly introduce the covariance between \(\sigma_k\) and \(w_k\). They then assert that an appropriate high-degree cutoff makes this covariance positive and conclude in Theorem 4.2(3) that targeted immunization is strictly more efficient than uniform immunization at the same average coverage. Their stated model hypotheses do not impose the cross-degree monotonicity needed for that sign.

Fu, Small, Walker, and Zhang study targeted immunization in a more restricted scale-free SIS model with piecewise-linear degree infectivity. In that setting the threshold weight is tied monotonically to degree, and their covariance argument supports the favorable targeted comparison. That restricted result does not imply the same sign for the later model's arbitrary degree-dependent functions \(f_k\).

Targeted large-degree immunization is also known to be optimal in several standard random-network SIS settings. Those results assume epidemic contribution increases with degree in the relevant threshold expression and therefore do not cover a model where \(w_k=\phi(k)f_k'(0)\) is allowed to decrease with degree.

Targeted searches by the exact article DOI and title, by Theorem 4.2's equal-average comparison, by covariance terminology, and by correction/erratum terminology did not locate a published correction of this source-specific claim.

## Limitations

The result concerns the comparison between uniform and degree-targeted immunization under the general heterogeneous-infection assumptions stated in the source. It does not contradict the source's numerical examples, where the selected functions may yield positively correlated epidemic weights.

The counterexample uses a deliberately small two-degree network to isolate the missing hypothesis. It is mathematically admissible under the stated model assumptions but is not offered as a calibrated empirical contact network.

The finding does not optimize over all possible immunization profiles. It gives the exact pairwise comparison with uniform coverage and shows that degree alone is insufficient to guarantee superiority when epidemic weights are allowed to vary independently across degree classes.

## References

1. S. Huang and J. Jiang, “Epidemic dynamics on complex networks with general infection rate and immune strategies,” Discrete and Continuous Dynamical Systems - B 23 (2018), 2071–2090. DOI: 10.3934/dcdsb.2018226.
2. X. Fu, M. Small, D. M. Walker, H. Zhang, “Epidemic dynamics on scale-free networks with piecewise linear infectivity and immunization,” Physical Review E 77 (2008), 036113. DOI: 10.1103/PhysRevE.77.036113.
3. M.-Y. Zhou, W.-M. Xiong, H. Liao, T. Wang, Z.-W. Wei, Z.-Q. Fu, “Analytical connection between thresholds and immunization strategies of SIS model in random networks,” Chaos 28 (2018), 051101. DOI: 10.1063/1.5030908.
