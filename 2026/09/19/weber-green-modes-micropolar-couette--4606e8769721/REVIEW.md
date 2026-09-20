# Same-model review

## Scientific claim reviewed

For the balanced-viscosity linearized micropolar Couette Green system in arXiv:2609.20109v1, the sheared Fourier \(2\times2\) ODE admits an exact reduction to Weber's equation. This produces a closed parabolic-cylinder fundamental matrix, an exact determinant, and sharp fixed-frequency singular-value asymptotics with cubic common damping and quadratic nonnormal splitting.

## Correctness

**PASS.**

The first-order system
\[
m'=-qm+q\omega,\qquad \omega'=m-(q+2)\omega
\]
is transformed by
\[
Q'=q+1,\qquad y=e^Q\omega
\]
into
\[
y''=(q+1)y,
\]
with exact reconstruction
\[
\omega=e^{-Q}y,\qquad m=e^{-Q}(y'+y).
\]
For the Couette symbol,
\[
q+1=|A\xi|^2(t-t_c)^2+\xi^2+1,
\]
and the stated scaling gives Weber's equation with
\[
\nu_W=-\frac12-\frac{\xi^2+1}{2|A\xi|}<0.
\]
The Wronskian
\[
\sqrt{2\pi}/\Gamma(-\nu_W)
\]
is nonzero, so the chosen two parabolic-cylinder solutions form a fundamental pair. Liouville's formula independently gives
\(\det\widehat G=e^{-2Q}\).

The main failure modes were checked explicitly:

- \(\xi=0\) is excluded from the Weber scaling and is treated separately by a constant-matrix exponential.
- The sign of \(A\xi\) does not affect the quadratic potential because \(\rho=|A\xi|\); the center \(t_c=\widetilde\eta/(A\xi)\) retains the correct sign.
- The growing asymptotic of \(D_{\nu_W}(-z)\) cannot lose its leading coefficient: \(-\nu_W>0\) and \(1/\Gamma(-\nu_W)\neq0\).
- The fixed normalization \(Y(0)^{-1}\) cannot remove the growing Weber direction from the operator norm because it is invertible.
- The smaller singular-value asymptotic is fixed by the exact determinant and therefore does not depend on an angle estimate between the two Weber basis columns.

Symbolic and numerical checks reproduce the reduction, matrix formula, zero-mode formula, and determinant to near machine precision. The computations are supportive evidence only.

## Originality

**PASS, to the best of our knowledge, with a stated residual risk.**

The primary source itself is highly relevant and was inspected at theorem/equation level. It explicitly writes the sheared Fourier coefficient matrix and later derives
\[
F''-(1+P')F=0,\qquad P'=q,
\]
but then uses an integral representation and Gronwall estimates. It does not identify this equation as Weber's equation, give a parabolic-cylinder fundamental matrix, or state the singular-value splitting above. The paper also motivates its method by the claimed lack of an explicit frequency-domain Green expression; the present formula is therefore a source-specific sharpening of that point for its balanced-viscosity case.

Searches were made for the source title/arXiv identifier together with `Weber`, `parabolic cylinder`, `explicit Green`, and synonymous Couette/micropolar formulations. No public correction or equivalent source-specific formula was found. The current SCOPE archive was also searched for the source identifier, `micropolar`, and equivalent special-function terminology; no overlapping accepted record was found.

Two prior micropolar-Couette papers are the principal residual risk:

- Y. Wang and L. Li, DOI 10.3934/dcdsb.2025124, studies linear and nonlinear enhanced dissipation using a Fourier-multiplier method. The accessible article material identifies that method and the main decay result, but the complete proof body was not fully available for inspection.
- K. Tao, DOI 10.1002/mma.70878, proves linear decay and nonlinear stability thresholds under several viscosity relations. The accessible text provided the abstract and bibliographic material but not enough of the proof body to exclude a hidden equivalent transformation.

No concrete evidence of coverage was found in either source. The standard theory of parabolic-cylinder functions is of course prior art and is excluded from the novelty claim. The novelty claim is the source-specific reduction and its dynamical consequences, not Weber theory itself.

## Value

**PASS.**

The result turns the source's unevaluated scalar ODE into an exact Green-symbol formula and exposes information unavailable from a scalar Gaussian upper bound: the determinant, the two singular directions, and an explicit condition-number growth law
\[
\log\kappa_2=
\frac{z^2}{2}-2\nu_W\log z+O(1).
\]
This gives a concrete measure of nonnormality while preserving the same cubic enhanced-dissipation exponent in both singular directions. The formula also provides an exact benchmark for testing future uniform frequency estimates or general-viscosity extensions.

## Limitations

The formula is tied to the balanced-viscosity coefficient matrix in the source paper and is a fixed sheared-frequency statement. It does not establish a better nonlinear threshold or a uniform physical-space Green estimate. The two related prior papers listed above were not fully inspected at proof level and remain the main originality uncertainty.

Same-model review: passed. Independent audit: not yet performed.
