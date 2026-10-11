# Exact pressure–activity law for recurrent QPP dynamics

## Finding
Consider the classical quasi-periodic plasma perturbations (QPP) system
\[
\dot x=(z-1)y-\delta x,\qquad \dot y=x,\qquad \dot z=\eta\bigl(h-z-y^2z\bigr),
\]
with \(h,\delta,\eta>0\). Let \(\mu\) be any compactly supported invariant Borel probability measure whose support lies in \(z>0\), and write
\[
\bar z=\int z\,d\mu.
\]
Then the pressure statistics determine the mean-square magnetic-field velocity exactly:
\[
\boxed{\int x^2\,d\mu=\bar z+h\int \frac1z\,d\mu-(h+1).}
\]
The displacement amplitude also satisfies
\[
\int y^2\,d\mu=h\int \frac1z\,d\mu-1.
\]
Equivalently, the activity law has the nonnegative pressure-fluctuation decomposition
\[
\int x^2\,d\mu
=\frac{(\bar z-1)(\bar z-h)}{\bar z}
+\frac{h}{\bar z^2}\int\frac{(z-\bar z)^2}{z}\,d\mu.
\]
Moreover, \(\int x^2\,d\mu=0\) holds exactly when \(\mu\) is supported on the equilibrium set. Hence every non-equilibrium ergodic recurrent state in \(z>0\) satisfies
\[
\bar z+h\int \frac1z\,d\mu>h+1.
\]
At the parameter value \(h=3\) used in the source's chaotic phase portraits, this becomes the exact diagnostic
\[
\int x^2\,d\mu=\bar z+3\int\frac1z\,d\mu-4>0
\]
for every non-equilibrium ergodic compact recurrent state.

## Assumptions and scope
The claim concerns the autonomous integer-order QPP model printed as system (6) in Zhang and Yang. The parameters satisfy \(h,\delta,\eta>0\), and the invariant measure is compactly supported in the physically relevant positive-pressure half-space \(z>0\). Compact support away from \(z=0\) makes \(\log z\) and all observables used below bounded with bounded derivatives on a neighborhood of the support.

No assertion is made about the delayed model, the fractional-order extension, existence of chaos, or existence of a compact invariant measure for any particular parameter set. The result is conditional on such a compact recurrent state and applies equally to periodic-orbit measures and to more general compact invariant probability measures.

## Proof
For any continuously differentiable observable \(\phi\), invariance gives \(\int L\phi\,d\mu=0\), where \(L\) is the Lie derivative along the QPP vector field.

First,
\[
L\!\left(\frac{y^2}{2}\right)=xy,
\]
so
\[
\int xy\,d\mu=0.
\]
Next,
\[
L(xy)=x^2+y^2(z-1)-\delta xy.
\]
After integration,
\[
\int x^2\,d\mu=\int y^2(1-z)\,d\mu.
\]
Stationarity of \(z\) gives
\[
0=\int Lz\,d\mu
=\eta\left(h-\int z\,d\mu-\int y^2z\,d\mu\right),
\]
therefore
\[
h=\bar z+\int y^2z\,d\mu.
\]
Combining the preceding two identities yields
\[
\int x^2\,d\mu=\bar z+\int y^2\,d\mu-h.
\]

Because \(z>0\) on the compact support,
\[
L(\log z)=\eta\left(\frac hz-1-y^2\right).
\]
Integrating gives
\[
\int y^2\,d\mu=h\int\frac1z\,d\mu-1.
\]
Substitution proves the boxed pressure–activity law.

For the equivalent decomposition, set \(Z=\bar z>0\). The pointwise identity
\[
\frac1z-\frac1Z+\frac{z-Z}{Z^2}=\frac{(z-Z)^2}{zZ^2}
\]
and \(\int(z-Z)\,d\mu=0\) imply
\[
\int\frac1z\,d\mu=\frac1Z+\frac1{Z^2}\int\frac{(z-Z)^2}{z}\,d\mu.
\]
Substitution into the boxed law gives the displayed fluctuation decomposition.

Finally, if \(\int x^2\,d\mu=0\), then \(x=0\) on the invariant support. Along such support \(\dot y=0\), while invariance of \(x=0\) requires \(y(z-1)=0\). If \(y\ne0\), invariance of \(z=1\) further requires \(h-1-y^2=0\), giving a nonzero equilibrium. If \(y=0\), the remaining scalar equation is \(\dot z=\eta(h-z)\), whose only invariant probability measure is supported at \(z=h\). Thus the measure is supported on equilibria. The converse is immediate because every equilibrium has \(x=0\). An ergodic invariant measure that is not an equilibrium point mass therefore has strictly positive \(\int x^2\,d\mu\).

## Verification
The accompanying `verify.py` reconstructs the four Lie derivatives used in the proof with exact symbolic algebra and verifies the reciprocal-pressure variance decomposition. Its recorded output ends with `VERIFY_OK`.

The proof itself is infinite-state: it uses invariance identities, not finite trajectory sampling. No numerical integration, Lyapunov-exponent estimate, or finite-time average is used as a substitute for the invariant-measure argument.

## Relationship to prior work
Zhang and Yang study the same QPP equations, including equilibrium stability, Hopf bifurcation, delayed feedback, non-integrability, numerical chaotic regimes, and dynamics at infinity. Their full text was inspected through the autonomous model, the delayed analysis, the numerical-chaos section, and the global-at-infinity discussion. Searches in that text for average, mean, invariant measure, and recurrence do not reveal the pressure–activity identity above.

The original QPP paper of Constantinescu et al. introduces the physical model and reports oscillatory regimes. Constantinescu et al. later analyze Hopf and fast-slow dynamics, and Elsadany, Elsonbaty, and Agiza analyze local/global bifurcations and chaos. Matouk and Khan study a fractional-order extension containing the same integer-order model at order one. These works motivate the recurrent regimes but do not imply the invariant-measure pressure–activity law: the new statement comes from simultaneously using stationarity of \(xy\), \(z\), and \(\log z\), and it applies to every compact recurrent statistical state of the classical flow rather than only to a local bifurcation branch or a sampled trajectory.

## Limitations
The logarithmic step requires the invariant support to lie in \(z>0\). The claim does not prove that a compact non-equilibrium invariant measure exists for a given parameter triple, nor does it classify periodic or chaotic states. It gives necessary exact statistics for any such state. The 2011 introducing paper was identifiable and its model/oscillation content was checked from public indexed material, but a direct full-text fetch was rate-limited during this review; this leaves a residual literature-access risk, not a gap in the proof.

## References
1. X. Zhang and S. Yang, “Complex dynamics in a quasi-periodic plasma perturbations model,” *Discrete and Continuous Dynamical Systems - B* 26 (2021), 4013–4043. DOI: 10.3934/dcdsb.2020272.
2. D. Constantinescu, O. Dumbrajs, V. Igochine, K. Lackner, R. Meyer-Spasche, and H. Zohm, “A low-dimensional model system for quasi-periodic plasma perturbations,” *Physics of Plasmas* 18 (2011), 062307. DOI: 10.1063/1.3600209.
3. D. Constantinescu et al., “Bifurcations and fast-slow dynamics in a low-dimensional model for quasi-periodic plasma perturbations,” *Romanian Reports in Physics* 67 (2015), 1049–1060.
4. A. A. Elsadany, A. Elsonbaty, and H. N. Agiza, “Qualitative dynamical analysis of chaotic plasma perturbations model,” *Communications in Nonlinear Science and Numerical Simulation* 59 (2018), 409–423. DOI: 10.1016/j.cnsns.2017.11.020.
5. A. E. Matouk and I. Khan, “Complex dynamics and control of a novel physical model using nonlocal fractional differential operator with singular kernel,” *Journal of Advanced Research* 24 (2020), 463–474. DOI: 10.1016/j.jare.2020.05.003.
