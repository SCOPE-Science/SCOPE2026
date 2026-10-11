# Review of Exact centered univalence radius of the Borovikov shear

## Correctness

PASS. The full Jacobian was reconstructed from the analytic identity
\[
W'(z)=-4z/(1-z^4)
\]
for
\[
W(z)=\log((1-z^2)/(1+z^2)).
\]
The Cauchy--Riemann equations give
\[
(u_*)_y=-(8/\pi)\operatorname{Re}(z/(1-z^4)),
\]
so the source real-axis derivative is a special case rather than an extrapolation.

For
\[
|z|\le r,
\]
the chain
\[
\operatorname{Re}(z/(1-z^4))
\le
|z|/|1-z^4|
\le
r/(1-r^4)
\]
is sharp uniquely at
\[
z=r>0.
\]
This gives the exact Jacobian minimum and proves strict positivity throughout
\[
\mathbb D_{r_M}.
\]

Global injectivity is then exact: equality of images forces equality of real coordinates, and on each connected vertical slice the imaginary coordinate has derivative equal to the positive Jacobian. Any larger centered disk contains the Jacobian-zero point, so Lewy's theorem rules out univalence there.

## Originality

PASS. The fully inspected 2026 source proves that the Jacobian vanishes at a unique positive real point
\[
r_M
\]
on the real axis and uses that point to disprove a Landau-radius conjecture. It does not state the full-disk Jacobian minimum, absence of earlier off-axis collapse, or global injectivity on
\[
\mathbb D_{r_M}.
\]

The original Landau--Bloch conjecture paper concerns universal radius guarantees rather than the geometry of this later explicit shear. Classical harmonic-shear and Lewy theory provide general tools but do not imply the exact radius without the source-specific Jacobian maximization and vertical-fiber analysis.

Searches using the source identifier, the fold equation, off-axis Jacobian language, and exact centered-univalence formulations did not locate an implication-equivalent published theorem.

## Value

PASS. The explicit map is the mechanism behind the new counterexample to the harmonic Landau-radius conjecture. Knowing only one real-axis fold leaves open whether the model already loses local or global injectivity earlier elsewhere in the disk.

The theorem resolves that natural ambiguity completely. It identifies the exact centered univalence radius, proves the real-axis fold is globally first, and shows that the source's obstruction is not preceded by hidden off-axis or global collisions. This gives a complete geometric classification of the counterexample's centered univalence regime rather than another numerical threshold.

Same-model review: passed. Independent audit: not yet performed.
