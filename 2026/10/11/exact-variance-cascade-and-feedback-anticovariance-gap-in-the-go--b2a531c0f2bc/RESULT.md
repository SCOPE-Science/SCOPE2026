# Exact variance cascade and feedback anticovariance gap in the Goodwin oscillator
## Finding
Consider the classical Goodwin oscillator
\[
\dot X=\Phi(Z)-k_4X,
\qquad
\dot Y=k_2X-k_5Y,
\qquad
\dot Z=k_3Y-k_6Z,
\]
with
\[
k_i>0
\]
and the Hill repression
\[
\Phi(Z)=\frac{k_1}{1+Z^9}.
\]
Let \(\mu\) be any compactly supported invariant Borel probability measure in the nonnegative concentration orthant.

The three stages satisfy exact state-slice calibration laws:
\[
\boxed{
\mathbb E_\mu[\Phi(Z)\mid X]=k_4X
},
\]
\[
\boxed{
\mathbb E_\mu[X\mid Y]=\frac{k_5}{k_2}Y
},
\]
and
\[
\boxed{
\mathbb E_\mu[Y\mid Z]=\frac{k_6}{k_3}Z
}.
\]

Each calibration has an exact fluctuation budget:
\[
\boxed{
\operatorname{Var}_\mu(\Phi(Z))
=
k_4^2\operatorname{Var}_\mu(X)
+
\mathbb E_\mu[\dot X^2]
},
\]
\[
\boxed{
k_2^2\operatorname{Var}_\mu(X)
=
k_5^2\operatorname{Var}_\mu(Y)
+
\mathbb E_\mu[\dot Y^2]
},
\]
and
\[
\boxed{
k_3^2\operatorname{Var}_\mu(Y)
=
k_6^2\operatorname{Var}_\mu(Z)
+
\mathbb E_\mu[\dot Z^2]
}.
\]
Each speed defect vanishes exactly for the unique equilibrium atom.

The negative feedback supplies a further identity not contained in the stagewise cascade:
\[
\boxed{
k_2k_3\operatorname{Cov}_\mu(Z,\Phi(Z))
=
k_6(k_4+k_6)(k_5+k_6)\operatorname{Var}_\mu(Z)
-
k_3^2(k_4+k_5+k_6)\operatorname{Var}_\mu(Y)
}.
\]
The Hill function is strictly decreasing on
\[
Z\ge0.
\]
Thus every non-equilibrium compact stationary state has nonconstant \(Z\) and
\[
\operatorname{Cov}_\mu(Z,\Phi(Z))<0.
\]
Therefore
\[
\boxed{
\operatorname{Var}_\mu(Y)
>
\frac{
k_6(k_4+k_6)(k_5+k_6)
}{
k_3^2(k_4+k_5+k_6)
}
\operatorname{Var}_\mu(Z)
}.
\]
This is strictly stronger than the direct filter inequality
\[
\operatorname{Var}_\mu(Y)
>
\left(\frac{k_6}{k_3}\right)^2
\operatorname{Var}_\mu(Z),
\]
because the ratio between the two coefficients is
\[
1+
\frac{k_4k_5}
{k_6(k_4+k_5+k_6)}
>
1.
\]

For the equal-rate normalization
\[
k_2=k_3=k_4=k_5=k_6=1,
\]
the feedback identity becomes
\[
\boxed{
\operatorname{Cov}_\mu(Z,\Phi(Z))
=
4\operatorname{Var}_\mu(Z)
-
3\operatorname{Var}_\mu(Y)
}
\]
and every non-equilibrium stationary state satisfies
\[
\boxed{
\operatorname{Var}_\mu(Y)
>
\frac43\operatorname{Var}_\mu(Z)
}.
\]

For the temperature-compensated limit-cycle parameter set used in the 1996 source,
\[
k_1=k_2=k_3=1,
\qquad
k_4=k_5=\frac15,
\qquad
k_6=\frac1{10},
\]
the exact feedback identity is
\[
\operatorname{Cov}_\mu
\left(
Z,\frac1{1+Z^9}
\right)
=
\frac9{1000}\operatorname{Var}_\mu(Z)
-
\frac12\operatorname{Var}_\mu(Y),
\]
so every non-equilibrium compact stationary state at those rates obeys
\[
\boxed{
\operatorname{Var}_\mu(Y)
>
\frac9{500}\operatorname{Var}_\mu(Z)
}.
\]
The direct final-stage filter inequality alone gives only
\[
\operatorname{Var}_\mu(Y)
>
\frac1{100}\operatorname{Var}_\mu(Z).
\]

## Assumptions and scope
The theorem uses the three-variable Goodwin model printed in the 1996 circadian-clock study:
\[
\dot X=\frac{k_1}{1+Z^9}-k_4X,
\qquad
\dot Y=k_2X-k_5Y,
\qquad
\dot Z=k_3Y-k_6Z.
\]
All rate constants are positive, and the invariant probability measure is assumed compactly supported in the nonnegative concentration orthant.

No ergodicity assumption is required. The result applies to the equilibrium atom, periodic-orbit measures, and compact invariant mixtures.

The argument extends verbatim to any bounded strictly decreasing repression function in place of the ninth-power Hill law. The stated claim is kept on the classical printed Goodwin model.

Goodwin introduced the oscillator in 1965, but the checked foundational record resolves that source only to a year. The structured date therefore uses 21 April 1996, the earliest checked day-resolved same-model publication, rather than inventing a day in 1965.

A mathematical article explicitly using the Goodwin oscillator lists \(34C11\) first in its Mathematics Subject Classification, so that primary classification is used here.

## Proof
Let \(L\) denote the flow generator.

For an arbitrary continuous function \(f\) on the compact \(X\)-projection of the support, choose an antiderivative \(F\) satisfying
\[
F'(X)=f(X).
\]
Then
\[
LF
=
f(X)\bigl(\Phi(Z)-k_4X\bigr).
\]
Invariance gives
\[
\mathbb E_\mu[
f(X)(\Phi(Z)-k_4X)
]
=
0
\]
for every \(f\), hence
\[
\mathbb E_\mu[\Phi(Z)\mid X]=k_4X.
\]

Repeating the same argument with arbitrary one-variable antiderivatives in \(Y\) and \(Z\) gives
\[
\mathbb E_\mu[X\mid Y]=\frac{k_5}{k_2}Y,
\qquad
\mathbb E_\mu[Y\mid Z]=\frac{k_6}{k_3}Z.
\]

Each coordinate speed is therefore an orthogonal regression residual. For example,
\[
\Phi(Z)=k_4X+\dot X
\]
with
\[
\mathbb E_\mu[\dot X\mid X]=0.
\]
The law of total variance gives
\[
\operatorname{Var}(\Phi(Z))
=
k_4^2\operatorname{Var}(X)
+
\mathbb E[\dot X^2].
\]
The other two variance identities follow identically.

If
\[
\mathbb E[\dot X^2]=0,
\]
then \(\dot X=0\) on invariant support. Along each support trajectory \(X\) is constant and
\[
\Phi(Z)=k_4X.
\]
Since \(\Phi\) is strictly decreasing on the nonnegative axis, \(Z\) is constant. Then \(\dot Z=0\) forces \(Y\) constant, and \(\dot Y=0\) gives the equilibrium equations. Thus the support is the unique equilibrium. The same propagation works from \(\dot Y=0\) or \(\dot Z=0\). Conversely the equilibrium atom makes all three defects vanish.

It remains to derive the sharpened downstream gap. Center the coordinates and put
\[
U=\Phi(Z)-\mathbb E[\Phi(Z)].
\]
The conditional laws give
\[
\operatorname{Cov}(X,Y)
=
\frac{k_5}{k_2}\operatorname{Var}(Y)
\]
and
\[
\operatorname{Cov}(Y,Z)
=
\frac{k_6}{k_3}\operatorname{Var}(Z).
\]

Stationarity of the centered product \(YZ\) gives
\[
0
=
k_2\operatorname{Cov}(X,Z)
+
k_3\operatorname{Var}(Y)
-
(k_5+k_6)\operatorname{Cov}(Y,Z).
\]
Hence
\[
\operatorname{Cov}(X,Z)
=
\frac1{k_2}
\left[
\frac{k_6(k_5+k_6)}{k_3}\operatorname{Var}(Z)
-
k_3\operatorname{Var}(Y)
\right].
\]

Stationarity of the centered product \(XZ\) gives
\[
0
=
\operatorname{Cov}(U,Z)
-
(k_4+k_6)\operatorname{Cov}(X,Z)
+
k_3\operatorname{Cov}(X,Y).
\]
Substitution yields
\[
k_2k_3\operatorname{Cov}(Z,\Phi(Z))
=
k_6(k_4+k_6)(k_5+k_6)\operatorname{Var}(Z)
-
k_3^2(k_4+k_5+k_6)\operatorname{Var}(Y).
\]

For an independent copy \(\widetilde Z\) of \(Z\),
\[
2\operatorname{Cov}(Z,\Phi(Z))
=
\mathbb E[
(Z-\widetilde Z)
(\Phi(Z)-\Phi(\widetilde Z))
].
\]
Because \(\Phi\) is strictly decreasing, the integrand is nonpositive and is strictly negative whenever
\[
Z\ne\widetilde Z.
\]
A non-equilibrium invariant state cannot have constant \(Z\): constant \(Z\) forces constant \(Y\), then constant \(X\), hence the equilibrium. Therefore every non-equilibrium state has
\[
\operatorname{Cov}(Z,\Phi(Z))<0.
\]
Solving the exact covariance identity for \(\operatorname{Var}(Y)\) gives the sharpened strict inequality.

Finally,
\[
\frac{
k_6(k_4+k_6)(k_5+k_6)
}{
k_3^2(k_4+k_5+k_6)
}
\bigg/
\left(\frac{k_6}{k_3}\right)^2
=
\frac{(k_4+k_6)(k_5+k_6)}
{k_6(k_4+k_5+k_6)}
=
1+
\frac{k_4k_5}
{k_6(k_4+k_5+k_6)},
\]
so the feedback bound strictly improves the direct final-stage filter inequality.

## Verification
The packaged checker uses exact rational arithmetic from the Python standard library.

It verifies the centered covariance elimination leading to
\[
k_2k_3\operatorname{Cov}(Z,\Phi(Z))
=
k_6(k_4+k_6)(k_5+k_6)\operatorname{Var}(Z)
-
k_3^2(k_4+k_5+k_6)\operatorname{Var}(Y).
\]

It verifies algebraically that the sharpened coefficient exceeds the direct final-stage coefficient by the factor
\[
1+
\frac{k_4k_5}
{k_6(k_4+k_5+k_6)}.
\]

For the exact source parameter set
\[
k_1=k_2=k_3=1,
\qquad
k_4=k_5=\frac15,
\qquad
k_6=\frac1{10},
\]
the checker verifies
\[
\frac{
k_6(k_4+k_6)(k_5+k_6)
}{
k_3^2(k_4+k_5+k_6)
}
=
\frac9{500},
\]
whereas
\[
\left(\frac{k_6}{k_3}\right)^2
=
\frac1{100}.
\]

The stored checker output is `VERIFY_OK`.

The conditional-expectation quantifiers, equilibrium-only equality classification, and strict sign of the feedback covariance are analytic proofs, not finite experiments.

## Relationship to prior work
The 1996 temperature-compensated Goodwin paper prints the three equations used here and emphasizes the roles of the amplifying reactions and the three degradation reactions. It studies limit cycles, damped oscillations, temperature compensation, entrainment, and phase response. A document-wide search of its searchable text found no occurrence of `variance`, `covariance`, `conditional`, `invariant measure`, or `moment`.

A complete open 2013 same-model study explains the standard Goodwin oscillator as a delayed negative-feedback loop, interprets the three variables as mRNA, protein, and transcriptional inhibitor, and studies molecular mechanisms behind the Hill repression. Full-document searches found no `variance`, `covariance`, `invariant measure`, `average`, `stationary`, or `conditional` formulation matching the accepted theorem.

A 2013 strong-feedback study analyzes the asymptotic relaxation regime of the three-variable Goodwin oscillator, while a 2014 revisit derives the Hopf amplitude equation and periodic entrainment. Those results concern waveform and bifurcation structure rather than all-invariant-measures variance geometry.

A published mathematical result on the Goodwin oscillator gives a different global recurrence theorem: a derivative-energy-weighted feedback slope equals the third-order Hurwitz Hopf threshold, forcing nonlinear recurrent states to cross the local Hopf-slope surface. That statement does not determine any of the three conditional regressions above, the stagewise variance residuals, or the exact feedback anticovariance identity. Conversely, the present result does not re-claim that Hopf-slope theorem.

The accepted theorem therefore isolates a different structural consequence of the same negative-feedback architecture: the linear stages form an exact stationary variance cascade, and monotonic repression strengthens the final-stage attenuation beyond what the local filter equation alone forces.

## Limitations
The theorem assumes compact invariant support in the nonnegative concentration orthant and positive rate constants.

It constrains conditional means and second-order stationary fluctuations but does not determine the period, waveform, invariant density, phase response, or stability of a limit cycle.

The strict feedback inequality uses monotonicity of the Hill repression. It does not require the Hill exponent \(9\) specifically, but the public claim is stated for the printed classical form.

The original Goodwin work predates the 1996 source but was verified only at year resolution in the checked route; no historical day is invented.

The published Goodwin recurrence result compared for overlap concerns a derivative-energy-weighted slope identity rather than the variance geometry here.

Because the one-coordinate generator step is concise, an equivalent regression observation could remain in unindexed literature.

## References
1. P. Ruoff and L. Rensing, “The Temperature-Compensated Goodwin Model Simulates Many Circadian Clock Properties,” *Journal of Theoretical Biology* 179, 275–285 (1996), DOI 10.1006/jtbi.1996.0067.
2. P. Ruoff, M. Vinsjevik, C. Monnerjahn, and L. Rensing, “The Goodwin Oscillator: On the Importance of Degradation Reactions in the Circadian Clock,” *Journal of Biological Rhythms* 14, 469–479 (1999), DOI 10.1177/074873099129001037.
3. D. Gonze and W. Abou-Jaoudé, “The Goodwin Model: Behind the Hill Function,” *PLoS ONE* 8, e69573 (2013), DOI 10.1371/journal.pone.0069573.
4. A. Woller, D. Gonze, and T. Erneux, “Strong feedback limit of the Goodwin circadian oscillator,” *Physical Review E* 87, 032722 (2013), DOI 10.1103/PhysRevE.87.032722.
5. S. Yanchuk and K. R. Schneider, “Complete synchronization of symmetrically coupled autonomous systems,” *Applicable Analysis* (2004), DOI 10.1080/00036810310001620072.
