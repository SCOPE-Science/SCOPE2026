# Review of Exact finite-degree inradius of the roots-of-unity lemniscate

## Correctness

PASS. The source already proves that every inscribed disk can be rotated into one lobe and that the principal lobe lies in the strip
\[
|\operatorname{Im}z|<H_n,
\]
so
\[
\rho(z^n-1)\le H_n.
\]

The new direction constructs a matching disk. On the exact boundary
\[
r(\theta)=(2\cos(n\theta))^{1/n},
\]
the squared distance to
\[
c_n=q_n\cos\alpha_n
\]
has derivative whose sign is controlled by
\[
J(\theta)=
\frac{r(\theta)\sin(n\theta)}
{\sin((n+1)\theta)}.
\]
Direct differentiation shows
\[
\operatorname{sign}J'
=
\operatorname{sign}
\left(
n\tan\theta-\tan(n\theta)
\right),
\]
which is negative throughout the positive half-lobe. Since
\[
J(\alpha_n)=c_n,
\]
the distance decreases up to
\[
\alpha_n
\]
and increases afterwards. Its minimum is exactly
\[
H_n.
\]
This proves the disk inclusion for the full continuum boundary, including the cusp by endpoint continuity.

The first correction follows from the exact formula and standard Taylor expansion. The proof clearly separates exact finite-degree assertions from asymptotics.

## Originality

PASS. The 1958 primary source uses
\[
z^n-1
\]
only to obtain the asymptotic obstruction
\[
c\le\pi/2
\]
for the universal inverse-degree constant. The 2025 inradius literature still treats the roots-of-unity configuration as the conjectural extremal model without recording its exact finite-degree inradius.

The 2026 lead source derives the exact quantity
\[
H_n
\]
as an upper bound on the inradius of
\[
z^n-1
\]
and uses only its limit
\[
nH_n\to\pi/2.
\]
Full-text inspection of its model calculation finds no matching disk construction and no statement
\[
\rho(z^n-1)=H_n.
\]

Targeted searches using exact model names, largest-inscribed-disk language, the formula parameters, and equivalent roots-of-unity descriptions found no implication-equivalent published result. Semantic searches of published findings returned only adjacent polynomial-zero and radius problems.

A residual risk remains that an older classical treatment uses different notation for the same finite-degree disk geometry, but no such statement was found in the primary sources or searches inspected.

## Value

PASS. The roots-of-unity lemniscate is the canonical obstruction in the deterministic inradius problem: it appears already in the 1958 problem statement and is the model matching the 2026 sharp asymptotic theorem.

Determining its exact inradius is therefore a natural invariant, not an arbitrary slice. The result shows that the recent strip obstruction is geometrically sharp at every finite degree and identifies an explicit maximizing disk and its tangency points. This gives a complete finite-degree description of the model quantity that underlies the universal asymptotic constant.

The exact formula also exposes the finite-degree approach to
\[
\pi/(2n),
\]
including the logarithmically enhanced second-order deficit.

Same-model review: passed. Independent audit: not yet performed.
