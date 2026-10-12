# The patchwise persistence lower bound omits pollution and outward migration

## Finding

For the stochastic two-patch model, the source defines
\[
R_1(t)
=
r_1-r_0c_0(t)
-d_{12}\left(
1+\frac{\lambda_1c_e(t)}{1+\alpha c_e(t)^2}
\right)
\]
and
\[
R_2(t)
=
r_2
-d_{21}\left(
1-\frac{\lambda_2c_e(t)}{1+\alpha c_e(t)^2}
\right).
\]

Theorem 4.10 assumes
\[
\langle R_i(t)\rangle^{l}
-
\frac{\sigma_i^2}{2}
>0
\]
for both patches, but its displayed conclusion replaces the effective patch growth by the intrinsic rate:
\[
\liminf_{t\to\infty}\langle x_i(t)\rangle
\ge
\frac{\bar r_i-\sigma_i^2/2}{a_i}.
\]
The source defines
\[
\bar f=\lim_{t\to\infty}f(t).
\]
Since each \(r_i\) is a constant model parameter,
\[
\bar r_i=r_i.
\]

The displayed quantitative bound is false. The proof immediately below the theorem instead derives
\[
\liminf_{t\to\infty}\langle x_i(t)\rangle
\ge
\frac{\langle R_i(t)\rangle^l-\sigma_i^2/2}{a_i}.
\]

A source-admissible exact example makes the distinction strict. Choose
\[
r_1=3,\quad
r_2=2,\quad
r_0=1,\quad
a_1=a_2=1,\quad
d_{12}=1,\quad
d_{21}=0,
\]
\[
\sigma_1=\sigma_2=1,\quad
\lambda_1=\lambda_2=0,\quad
\alpha=1,
\]
and
\[
f=g=m=1,\qquad
h=2,\qquad
u_e(t)=1,
\]
with
\[
c_e(0)=\frac12,\qquad
c_0(0)=\frac14.
\]
Then the toxicant concentrations remain constant,
\[
c_e(t)=\frac12,\qquad
c_0(t)=\frac14,
\]
and
\[
R_1=\frac74,\qquad
R_2=2.
\]
Both hypotheses of Theorem 4.10 hold.

Because \(d_{21}=0\), patch 1 is exactly the scalar stochastic logistic equation
\[
dx_1
=
x_1\left(\frac74-x_1\right)dt
+
x_1\,dB_1(t).
\]
The source's own Lemma 2.3 gives
\[
\lim_{t\to\infty}\langle x_1(t)\rangle
=
\frac54
\qquad\text{a.s.}
\]
The theorem statement instead requires a lower bound of
\[
\frac52.
\]
Thus the statement's quantitative estimate is false, while the proof-derived estimate is exact on this witness.

## Assumptions and scope

The example uses the parameter domain printed in the source. In particular,
\[
0\le\lambda_i\le1,
\]
the toxicant concentrations are in
\[
[0,1],
\]
the input obeys
\[
u_e(t)<h,
\]
and
\[
f\le g+m.
\]
The source itself also uses zero migration coefficients in its numerical Example 3, so \(d_{21}=0\) is within its implemented parameter domain.

The finding concerns the numerical lower-bound clause of Theorem 4.10. It does not refute the theorem's qualitative conclusion that both patches are strongly persistent in the mean under its hypotheses.

No claim is made that the proof-derived bound is globally sharp for every coupled parameter set. It is sharp for the exact decoupled-outflow witness above.

## Proof

The environmental equations are
\[
dc_0
=
\bigl(fc_e-(g+m)c_0\bigr)dt,
\qquad
dc_e
=
\bigl(-hc_e+u_e\bigr)dt.
\]
At the stated values,
\[
fc_e-(g+m)c_0
=
\frac12-2\cdot\frac14
=
0
\]
and
\[
-hc_e+u_e
=
-2\cdot\frac12+1
=
0.
\]
Therefore
\[
c_e(t)=\frac12,\qquad
c_0(t)=\frac14
\]
for all \(t\).

With
\[
\lambda_1=\lambda_2=0,
\]
the effective rates become
\[
R_1
=
3-\frac14-1
=
\frac74
\]
and
\[
R_2
=
2.
\]
Thus
\[
R_1-\frac{\sigma_1^2}{2}
=
\frac54>0,
\qquad
R_2-\frac{\sigma_2^2}{2}
=
\frac32>0.
\]

Because
\[
d_{21}=0,
\]
the first population equation contains no immigration from patch 2. Its outgoing migration remains
\[
-d_{12}x_1=-x_1.
\]
Hence
\[
dx_1
=
x_1\left(
3-\frac14-1-x_1
\right)dt
+
x_1\,dB_1(t),
\]
which simplifies to
\[
dx_1
=
x_1\left(\frac74-x_1\right)dt
+
x_1\,dB_1(t).
\]

The source's Lemma 2.3 states that for
\[
dx=x(r-ax)dt+\sigma x\,dB,
\]
if
\[
r-\frac{\sigma^2}{2}>0,
\]
then
\[
\lim_{t\to\infty}\langle x(t)\rangle
=
\frac{r-\sigma^2/2}{a}
\qquad\text{a.s.}
\]
Applying it with
\[
r=\frac74,\qquad
a=1,\qquad
\sigma=1
\]
gives
\[
\lim_{t\to\infty}\langle x_1(t)\rangle
=
\frac54.
\]

The displayed Theorem 4.10 estimate uses
\[
\bar r_1=r_1=3
\]
and would require
\[
\liminf_{t\to\infty}\langle x_1(t)\rangle
\ge
\frac{3-1/2}{1}
=
\frac52.
\]
Since
\[
\frac54<\frac52,
\]
the displayed bound is false.

The final lines of the source proof instead give
\[
\liminf_{t\to\infty}\langle x_1(t)\rangle
\ge
\frac{\langle R_1(t)\rangle^l-1/2}{1}
=
\frac54,
\]
which agrees exactly with the scalar stochastic-logistic limit.

## Verification

The bundled `verify.py` checks the environmental equilibrium, the effective growth rates, both Theorem 4.10 hypotheses, the scalar-logistic reduction, and the two competing lower bounds using exact rational arithmetic.

The checker confirms
\[
\text{actual time mean}=\frac54,
\qquad
\text{proof-derived bound}=\frac54,
\qquad
\text{displayed theorem bound}=\frac52.
\]

No finite simulation is used to establish the contradiction.

## Relationship to prior work

Stochastic-logistic persistence and extinction criteria are established prior theory. The motivating source itself states the exact scalar time-mean formula as Lemma 2.3, citing earlier stochastic population work. Liu and Wang study persistence and extinction in stochastic non-autonomous logistic systems, while Liu, Wang, and Wu study stochastic competitive populations in polluted environments.

Those general results are not claimed as new. The source-specific contribution here is the exact counterexample showing that Theorem 4.10's displayed patchwise abundance bound drops the pollution and outward-migration terms already present in \(R_i(t)\), together with the observation that the proof immediately below the theorem retains those terms and yields the correct value on the witness.

Searches by the source DOI, exact title, theorem number, lower-bound language, migration terminology, and correction or erratum terminology did not locate a published correction of Theorem 4.10.

## Limitations

The qualitative strong-persistence conclusion is not disproved by this example.

The source's proof-derived bound is shown to be correct and sharp on the exact witness, but no universal optimality claim for that bound is made.

A non-indexed author correction could exist outside the checked records.

## References

1. X. Dai, S. Wang, B. Yan, Z. Mao, W. Xiong, “Survival analysis of single-species population diffusion models with chemotaxis in polluted environment,” AIMS Mathematics 5 (2020), 6749–6765. DOI: 10.3934/math.2020434.
2. M. Liu, K. Wang, “Persistence and extinction in stochastic non-autonomous logistic systems,” Journal of Mathematical Analysis and Applications 375 (2011), 443–457. DOI: 10.1016/j.jmaa.2010.09.058.
3. M. Liu, K. Wang, Q. Wu, “Survival analysis of stochastic competitive models in a polluted environment and stochastic competitive exclusion principle,” Bulletin of Mathematical Biology 73 (2011), 1969–2012. DOI: 10.1007/s11538-010-9569-5.
