# The subthreshold endemic branch in a 2024 SVIR model is algebraically empty

## Finding

Consider the SVIR model
\[
\begin{aligned}
\dot V&=\gamma S-(1-\theta)\beta VI-(\delta+d)V,\\
\dot S&=\Lambda+\delta V-\beta SI-(\gamma+d)S,\\
\dot I&=\beta SI+(1-\theta)\beta VI-(d+\alpha+b)I,\\
\dot R&=bI-dR.
\end{aligned}
\]
Assume
\[
d>0,\quad \beta>0,\quad \Lambda>0,\quad
\gamma,\delta,\alpha,b\ge0,\quad 0\le\theta\le1.
\]
Write
\[
r=1-\theta,\qquad a=d+\delta,\qquad m=d+\alpha+b.
\]
From the disease-free state printed in the source,
\[
S_0=\frac{\Lambda a}{d(a+\gamma)},
\qquad
V_0=\frac{\Lambda\gamma}{d(a+\gamma)},
\]
the unambiguous next-generation expression
\[
R_{\mathrm{vac}}
=\frac{\beta}{m}\bigl(S_0+rV_0\bigr)
\]
becomes
\[
R_{\mathrm{vac}}
=\frac{\beta\Lambda(a+r\gamma)}{dm(a+\gamma)}.
\]

The source reduces a positive endemic equilibrium to a root \(I^*>0\) of
\[
P(I)=A_2I^2+B_1I+C_0,
\]
where
\[
A_2=-rm\beta^2,
\]
\[
B_1=\beta\left\{\Lambda\beta r-m\left[a+r(\gamma+d)\right]\right\},
\]
and
\[
C_0=dm(a+\gamma)\bigl(R_{\mathrm{vac}}-1\bigr).
\]

For every admissible parameter choice,
\[
R_{\mathrm{vac}}\le1
\quad\Longrightarrow\quad
B_1<0.
\]
It follows that the positive-endemic equilibrium count is exactly
\[
\#\{I^*>0:P(I^*)=0\}
=
\begin{cases}
0,&R_{\mathrm{vac}}\le1,\\
1,&R_{\mathrm{vac}}>1.
\end{cases}
\]

Thus the subthreshold alternatives in Theorem 3.3 of the source that require
\(R_{\mathrm{vac}}<1\) and \(B_1>0\), and the threshold alternative requiring
\(R_{\mathrm{vac}}=1\) and \(B_1>0\), cannot occur in the stated biological parameter
domain. In particular, the saddle-node/backward-bifurcation endemic branch described by those
cases is algebraically empty for this model.

## Assumptions and scope

The result concerns the autonomous SVIR model above and its regular nonnegative biological
parameter domain. The restrictions \(d>0\), \(\beta>0\), and \(\Lambda>0\) exclude
degenerate cases in which the disease-free formulas or endemic interpretation collapse.
The remaining rates may vanish, and the full vaccine-effectiveness boundary
\(\theta=1\) is included.

The statement is only about existence and multiplicity of positive endemic equilibria. It does
not re-prove the source's global-stability theorem, does not classify Hopf bifurcations on the
unique endemic branch, and does not assert that every vaccination model lacks backward
bifurcation.

## Proof

Suppose first that \(R_{\mathrm{vac}}\le1\). Then
\[
\frac{\Lambda\beta}{m}
\le
d\frac{a+\gamma}{a+r\gamma}.
\]
Multiplying by \(r\ge0\) gives
\[
\frac{\Lambda\beta r}{m}
\le
d\frac{r(a+\gamma)}{a+r\gamma}.
\]
Because \(0\le r\le1\),
\[
a+r\gamma-r(a+\gamma)=(1-r)a\ge0,
\]
so
\[
\frac{\Lambda\beta r}{m}\le d.
\]
Therefore
\[
\frac{B_1}{\beta m}
=
\frac{\Lambda\beta r}{m}
-a-r(\gamma+d)
\le
-\delta-r(\gamma+d).
\]
If \(\delta+r(\gamma+d)>0\), this is strictly negative. The only case in which
the displayed upper bound can vanish is \(r=0\) and \(\delta=0\); there the exact
coefficient is
\[
B_1=-\beta md<0.
\]
Hence \(B_1<0\) whenever \(R_{\mathrm{vac}}\le1\).

If \(R_{\mathrm{vac}}<1\), then \(C_0<0\), while \(A_2\le0\) and
\(B_1<0\). Thus \(P(I)<0\) for every \(I>0\). If
\(R_{\mathrm{vac}}=1\), then \(C_0=0\) and
\[
P(I)=I(A_2I+B_1)<0
\]
for every \(I>0\). No positive endemic root exists in either case.

Now suppose \(R_{\mathrm{vac}}>1\), so \(C_0>0\). If \(r>0\), then
\(A_2<0\), and
\[
B_1^2-4A_2C_0>B_1^2.
\]
The two roots are real and their product is
\[
\frac{C_0}{A_2}<0,
\]
so exactly one root is positive. If \(r=0\), then \(A_2=0\) and
\[
B_1=-\beta ma<0.
\]
The equation is linear with positive intercept \(C_0\), hence its unique root
\(-C_0/B_1\) is positive. This proves the complete classification.

## Verification

The bundled `verify.py` checks the source coefficient identities with exact rational
arithmetic over a grid that includes \(\theta=1\), \(\delta=0\), and threshold
choices with \(R_{\mathrm{vac}}=1\). It also checks that every sampled
subthreshold case has \(B_1<0\) and no positive endemic root, while sampled
superthreshold cases have exactly one positive root.

The script additionally evaluates the parameter set used by the source for its disease-free
simulation:
\[
b=0.008,\quad d=0.0518,\quad \theta=0.8125,\quad
\beta=0.0563,\quad \delta=0.111,\quad
\Lambda=1,\quad \alpha=0.35,\quad \gamma=0.99.
\]
The reconstructed next-generation value is approximately
\[
R_{\mathrm{vac}}=0.8016,
\]
agreeing with the source's reported simulation value and fixing the normalization used in the
proof above.

The finite checks support reproducibility; the general theorem itself is the analytic sign
argument in the preceding section.

## Relationship to prior work

Zhu, Liu, Lin, Zhang, and Wei (2024) derive the same quadratic endemic-equilibrium equation.
Their Theorem 3.3 lists two positive endemic equilibria when
\(R_{\mathrm{vac}}<1\), \(B_1>0\), and a discriminant condition holds, and one
positive endemic equilibrium at a subthreshold fold. The source does not test whether
\(B_1>0\) is compatible with \(R_{\mathrm{vac}}\le1\) under its own parameter
constraints. The inequality above shows it is not. The source's numerical bifurcation example is
forward, which is consistent with the corrected global equilibrium count.

Arino, McCluskey, and van den Driessche (2003) analyze a different vaccination model in which
the analogous conditions \(B>0\), \(C<0\), and positive discriminant can genuinely coexist,
producing a backward bifurcation. Their result therefore shows that the sign pattern used in the
2024 case is mathematically meaningful in other models, but it does not imply feasibility for the
2024 coefficients.

Liu, Takeuchi, and Iwami (2008) prove strict threshold dynamics for different continuous and
pulse SVIR vaccination models and identify a necessary condition for successful elimination.
Those models include an explicit delay-to-immunity mechanism and do not contain the coefficient
identity proved here.

## Limitations

The result does not establish global convergence of the endemic equilibrium for
\(R_{\mathrm{vac}}>1\), nor does it exclude Hopf bifurcation on that unique branch.
It only removes the purported subthreshold positive-equilibrium and saddle-node cases from the
admissible parameter domain of this specific model.

The originality comparison found no published correction or erratum for the source-specific
coefficient incompatibility. A later unindexed note could exist, so absence from the inspected
literature is not a proof of priority.

## References

1. X. Zhu, H. Liu, X. Lin, Q. Zhang, Y. Wei, “Global stability and optimal vaccination control of SVIR models,” *AIMS Mathematics* 9 (2024), 3453–3482. DOI: 10.3934/math.2024170.
2. J. Arino, C. C. McCluskey, P. van den Driessche, “Global results for an epidemic model with vaccination that exhibits backward bifurcation,” *SIAM Journal on Applied Mathematics* 64 (2003), 260–276. DOI: 10.1137/S0036139902413829.
3. X. Liu, Y. Takeuchi, S. Iwami, “SVIR epidemic models with vaccination strategies,” *Journal of Theoretical Biology* 253 (2008), 1–11. DOI: 10.1016/j.jtbi.2007.10.014.
