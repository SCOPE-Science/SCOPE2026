# The printed stochastic patch model and its extinction proof use different noise correlations

## Finding

The stochastic two-patch population model prints
\[
dx_1=\cdots+\sigma_1x_1\,dB_1,
\qquad
dx_2=\cdots+\sigma_2x_2\,dB_1.
\]
Thus both patches are driven by the same Brownian motion.

The later extinction proof instead uses
\[
\sigma_1x_1\,dB_1+\sigma_2\theta x_2\,dB_2
\]
and computes its quadratic variation as the sum of two squares, with no covariance term. This is the calculation for independent Brownian motions.

The two models have different sharp uniform Itô corrections. Let
\[
Y=x_1+\theta x_2,
\qquad
p=\frac{x_1}{Y}.
\]
Then
\[
1-p=\frac{\theta x_2}{Y}.
\]

For independent patch noise,
\[
\frac{d\langle Y\rangle}{Y^2\,dt}
=
\sigma_1^2p^2+\sigma_2^2(1-p)^2.
\]
Its sharp lower bound over \(0\le p\le1\) is
\[
v_{\mathrm{ind}}
=
\frac{\sigma_1^2\sigma_2^2}
{\sigma_1^2+\sigma_2^2}.
\]

For the common noise printed in the model,
\[
\frac{d\langle Y\rangle}{Y^2\,dt}
=
\left[
\sigma_1p+\sigma_2(1-p)
\right]^2,
\]
whose sharp lower bound is
\[
v_{\mathrm{com}}
=
\min\{\sigma_1^2,\sigma_2^2\}.
\]

Therefore the same comparison argument used in Theorem 4.4 gives the following sufficient extinction condition for the printed common-noise system:
\[
(R_1^u+R_2^u)
+
\sqrt{
(R_1^u-R_2^u)^2
+
4D_{12}^uD_{21}^u
}
<
\min\{\sigma_1^2,\sigma_2^2\}.
\]

The source instead places
\[
\frac{\sigma_1^2\sigma_2^2}
{\sigma_1^2+\sigma_2^2}
\]
on the right-hand side, which is the independent-noise bound used by its proof.

For equal noise intensities,
\[
\sigma_1=\sigma_2=\sigma,
\]
the distinction is a factor of two:
\[
v_{\mathrm{ind}}=\frac{\sigma^2}{2},
\qquad
v_{\mathrm{com}}=\sigma^2.
\]

This difference is attained in a simple admissible submodel. Set pollution and chemotaxis to zero and choose
\[
r_1=r_2=\frac38,
\qquad
a_1=a_2=1,
\qquad
d_{12}=d_{21}=d>0,
\qquad
\sigma_1=\sigma_2=1.
\]
For
\[
Y=x_1+x_2,
\]
the migration terms cancel and the printed common-noise system gives
\[
dY
=
\left[
\frac38Y-x_1^2-x_2^2
\right]dt
+
Y\,dB_1.
\]
Hence
\[
d\log Y
=
\left[
-\frac18
-
\frac{x_1^2+x_2^2}{Y}
\right]dt
+
dB_1.
\]
Since
\[
\frac{B_1(t)}{t}\to0
\]
almost surely,
\[
\limsup_{t\to\infty}
\frac{\log Y(t)}{t}
\le
-\frac18.
\]
Thus both patch populations become extinct exponentially almost surely.

For these same parameters the source's spectral left-hand side is
\[
2r=\frac34.
\]
Its independent-noise extinction condition requires
\[
\frac34<\frac12,
\]
which fails, whereas the corrected common-noise condition is
\[
\frac34<1,
\]
which holds.

## Assumptions and scope

The noise intensities satisfy
\[
\sigma_1,\sigma_2>0,
\]
as in the source's stochastic analysis. The population state is positive.

The correction concerns the covariance structure of the environmental noise. It does not alter the deterministic chemotaxis model.

If equations (1.4)-(1.5) were intended to contain two independent Brownian motions and the repeated \(B_1\) is merely a transcription error, then the source's independent-noise calculation is the relevant one after that model correction. If the printed equations are taken literally, the common-noise correction above is the relevant one.

The extinction inequality is sufficient, not necessary.

## Proof

For a weighted total population
\[
Y=x_1+\theta x_2,
\]
write
\[
p=\frac{x_1}{Y},
\qquad
q=\frac{\theta x_2}{Y}.
\]
Then
\[
p,q>0,
\qquad
p+q=1.
\]

With independent Brownian motions,
\[
dY=\cdots+\sigma_1x_1\,dB_1+\sigma_2\theta x_2\,dB_2,
\]
so
\[
\frac{d\langle Y\rangle}{Y^2dt}
=
\sigma_1^2p^2+\sigma_2^2q^2.
\]
Completing the square gives
\[
\sigma_1^2p^2+\sigma_2^2(1-p)^2
\ge
\frac{\sigma_1^2\sigma_2^2}
{\sigma_1^2+\sigma_2^2},
\]
with equality at
\[
p=
\frac{\sigma_2^2}
{\sigma_1^2+\sigma_2^2}.
\]

With the single Brownian motion printed in both patch equations,
\[
dY
=
\cdots+
\left(
\sigma_1x_1+\sigma_2\theta x_2
\right)dB_1.
\]
Therefore
\[
\frac{d\langle Y\rangle}{Y^2dt}
=
\left[
\sigma_1p+\sigma_2(1-p)
\right]^2.
\]
The expression inside the square is a convex combination of the two positive noise intensities, so its minimum is
\[
\min\{\sigma_1,\sigma_2\}.
\]
Squaring proves
\[
v_{\mathrm{com}}
=
\min\{\sigma_1^2,\sigma_2^2\}.
\]

The deterministic part of the source's comparison argument is unchanged. If
\[
\Lambda
=
(R_1^u+R_2^u)
+
\sqrt{
(R_1^u-R_2^u)^2+4D_{12}^uD_{21}^u
},
\]
then the Perron comparison rate used in the proof is
\[
\frac{\Lambda}{2}.
\]
Itô's formula gives
\[
d\log Y
\le
\frac12
\left(
\Lambda-v_{\mathrm{com}}
\right)dt
+
dM_t
\]
up to the same asymptotically vanishing comparison slack used by the source. Thus
\[
\Lambda<v_{\mathrm{com}}
\]
implies exponential extinction.

The explicit symmetric witness follows by summing the two printed equations. Symmetric migration cancels exactly, and common equal noise factors as
\[
x_1\,dB_1+x_2\,dB_1=Y\,dB_1.
\]
The displayed logarithmic inequality then follows immediately from Itô's formula.

## Verification

The bundled `verify.py` symbolically minimizes both quadratic-variation expressions.

It verifies
\[
\min_{0\le p\le1}
\left[
\sigma_1^2p^2+\sigma_2^2(1-p)^2
\right]
=
\frac{\sigma_1^2\sigma_2^2}
{\sigma_1^2+\sigma_2^2},
\]
and, for positive \(\sigma_1,\sigma_2\),
\[
\min_{0\le p\le1}
\left[
\sigma_1p+\sigma_2(1-p)
\right]^2
=
\min\{\sigma_1^2,\sigma_2^2\}.
\]

For the exact witness
\[
r=\frac38,
\qquad
\sigma_1=\sigma_2=1,
\]
it verifies
\[
\Lambda=\frac34,
\qquad
v_{\mathrm{ind}}=\frac12,
\qquad
v_{\mathrm{com}}=1.
\]
Hence the independent sufficient condition fails and the common-noise condition holds.

The exponential extinction statement for the witness is analytic and uses the strong law
\[
B_1(t)/t\to0
\]
almost surely.

## Relationship to prior work

Dai, Wang, Yan, Mao, and Xiong print the same Brownian motion in both stochastic patch equations. Their subsequent proofs repeatedly use \(B_1\) and \(B_2\), and Theorem 4.4 computes a quadratic variation equal to the sum of two squared patch contributions. The effective variance defined in their preliminaries is exactly the sharp independent-noise lower bound.

Zou, Fan, and Wang's earlier two-patch stochastic diffusion paper, which is cited by the motivating source, explicitly declares \(B_1\) and \(B_2\) to be mutually independent Brownian motions. Its stochastic model therefore matches the covariance structure used in the motivating source's proofs rather than the covariance structure printed in equations (1.4)-(1.5).

Hening, Nguyen, and Yin study stochastic populations dispersed across patches with a general environmental covariance matrix. They emphasize that perfectly correlated, degenerate noise is biologically meaningful and can have qualitatively different persistence and extinction behavior from nondegenerate noise. This supports treating the covariance choice as part of the mathematical model rather than as inert notation.

No located source-specific correction or erratum resolves which covariance structure was intended in the 2020 article.

## Limitations

The result does not claim that every theorem in the source becomes false under common noise. Several one-coordinate estimates remain valid, and the common-noise extinction condition is in fact stronger than the independent-noise condition.

The explicit witness shows a strict gap between the two sufficient extinction criteria; it is not a claim that the corresponding independent-noise system necessarily persists.

The result does not infer which stochastic covariance structure was used to generate the numerical figures because simulation code is unavailable.

## References

1. X. Dai, S. Wang, B. Yan, Z. Mao, W. Xiong, “Survival analysis of single-species population diffusion models with chemotaxis in polluted environment,” AIMS Mathematics 5 (2020), 6749–6765. DOI: 10.3934/math.2020434.
2. X. Zou, D. Fan, K. Wang, “Effects of Dispersal for a Logistic Growth Population in Random Environments,” Abstract and Applied Analysis 2013 (2013), 912579. DOI: 10.1155/2013/912579.
3. A. Hening, D. H. Nguyen, G. Yin, “Stochastic population growth in spatially heterogeneous environments: the density-dependent case,” Journal of Mathematical Biology 76 (2018), 697–754. DOI: 10.1007/s00285-017-1153-2.
