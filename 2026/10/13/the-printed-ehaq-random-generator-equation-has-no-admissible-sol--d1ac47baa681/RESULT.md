# The printed EHaq random-generator equation has no admissible solution
## Finding
Let
\[
A_\tau(x)
=
\frac{(1+\tau)^2+\tau x+\tfrac12(\tau x)^2}{(1+\tau)^2}e^{-\tau x},
\qquad
x\ge0,
\]
for
\[
\delta>0,\qquad \tau>0.
\]
The published exponentiated Haq cumulative distribution function is
\[
F(x)=[1-A_\tau(x)]^\delta.
\]

For a probability level
\[
0<z<1,
\]
the equation
\[
F(x)=z
\]
is equivalent to
\[
\boxed{
A_\tau(x)=1-z^{1/\delta}.
}
\]
Thus the correct numerical quantile equation is
\[
\boxed{
\left((1+\tau)^2+\tau x+\frac12(\tau x)^2\right)e^{-\tau x}
=
(1+\tau)^2(1-z^{1/\delta}).
}
\]

Equation (10) of the source instead prints a plus sign:
\[
\left((1+\tau)^2+\tau x+\frac12(\tau x)^2\right)e^{-\tau x}
=
(1+\tau)^2(1+z^{1/\delta}).
\]
For every admissible \(z,\delta,\tau\), this printed equation has no solution with \(x\ge0\).

The corrected equation has exactly one solution. At
\[
(\delta,\tau,z)=(0.5,0.5,0.25),
\]
it gives
\[
\boxed{
Q(0.25)=0.238229040340517\ldots,
}
\]
which agrees with the source's Table 1 value \(0.2382\).

The same corrected inversion reproduces the first three Table 1 quantiles for \(\delta=0.5\):
\[
\begin{array}{c|ccc}
\tau & Q(0.25)&Q(0.50)&Q(0.75)\\
\hline
0.5&0.2382290403&1.1378757848&3.4048875745\\
1.0&0.0869740168&0.4014703904&1.2298132161\\
1.5&0.0515355298&0.2345105321&0.7043047116\\
2.0&0.0364492754&0.1647154606&0.4881694932\\
3.0&0.0229963864&0.1032657483&0.3019044576
\end{array}
\]

The article later says that Monte Carlo samples are selected from the EHaq distribution using the quantile function in Eq. (10). Since the printed equation has no admissible root, the simulation algorithm described in the article cannot be executed as written. The Table 1 agreement shows that at least some reported numerics are consistent with the corrected inversion, so this result does not claim that the unpublished simulation code used the wrong sign.

## Assumptions and scope
The support is
\[
x\ge0,
\]
with
\[
\delta,\tau>0
\]
and
\[
0<z<1.
\]

The finding concerns the algebraic inversion of the published CDF and the equation presented as the quantile/random-number generator.

It does not reassess the model's parameter estimators, empirical fits, or every simulation output. The article does not expose the implementation needed to determine which sign was used in its numerical code.

## Proof
Set
\[
L_\tau(x)
=
\left((1+\tau)^2+\tau x+\frac12\tau^2x^2\right)e^{-\tau x}.
\]
Direct differentiation gives
\[
L_\tau'(x)
=
-\tau^2
\left(
2+\tau+\frac{\tau x^2}{2}
\right)e^{-\tau x}.
\]
Hence
\[
L_\tau'(x)<0
\]
for every \(x\ge0\) and \(\tau>0\).

Also,
\[
L_\tau(0)=(1+\tau)^2
\]
and
\[
L_\tau(x)\to0
\qquad(x\to\infty).
\]
Therefore the range of \(L_\tau\) is
\[
(0,(1+\tau)^2].
\]

The right side printed in Eq. (10) is
\[
(1+\tau)^2(1+z^{1/\delta}),
\]
which is strictly larger than \((1+\tau)^2\). Thus it lies outside the range of \(L_\tau\), proving that the printed equation has no solution.

Starting from the CDF instead gives
\[
[1-A_\tau(x)]^\delta=z
\]
and therefore
\[
L_\tau(x)=(1+\tau)^2(1-z^{1/\delta}).
\]
This corrected right side lies strictly between \(0\) and \((1+\tau)^2\). Continuity and strict monotonicity of \(L_\tau\) then give existence and uniqueness.

## Verification
The accompanying checker implements the published CDF and the two competing inversion equations.

It verifies the exact derivative sign, confirms that the printed plus-sign right side exceeds the maximum left-side value for a grid of admissible parameters, and solves only the corrected minus-sign equation.

Each computed root is substituted back into the published CDF and returns the requested probability to high precision.

The checker also reproduces the Table 1 quartiles shown above. This is useful evidence that the displayed table is consistent with the corrected equation even though Eq. (10) itself is not executable.

## Relationship to prior work
The EHaq construction uses the classical exponentiated-distribution mechanism
\[
F(x)=G(x)^\delta.
\]
For any such model,
\[
F(x)=z
\]
forces
\[
G(x)=z^{1/\delta}.
\]
Here the Haq baseline CDF is
\[
G(x)=1-A_\tau(x),
\]
so the corrected minus sign follows immediately.

The classical Lehmann-alternative literature studies the general model \(F_*(x)=F(x)^\theta\). It supports this exponentiation mechanism but does not discuss the source-specific EHaq equation.

Focused searches using the exact DOI, model name, quantile and random-generator terminology, Eq. (10), and correction terminology did not locate a published correction of the EHaq equation.

## Limitations
The unpublished simulation implementation is unavailable, so the sign actually used in code is not determined here.

The source's displayed quantiles agree with the corrected equation and are not contradicted by this result.

A very recent or unindexed correction could exist outside the sources examined.

## References
1. A. S. Alharthi, “An exponentiated Haq distribution: Theoretical aspects, estimation, and modeling of radiation and COVID-19 datasets,” AIMS Mathematics 10 (2025), 22497–22530. DOI: 10.3934/math.20251002.
2. R. C. Gupta, P. L. Gupta, and R. D. Gupta, “Modeling failure time data by Lehman alternatives,” Communications in Statistics—Theory and Methods 27 (1998), 887–904. DOI: 10.1080/03610929808832134.
