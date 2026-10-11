# Review of A unique minimum in the stretched-exponential Fock Korenblum radius

## Correctness

PASS. The source formula
\[
K(m)^2=\Gamma(4/m)/\Gamma(2/m)
\]
is exact for every \(m>0\). With \(x=2/m\), duplication gives
\[
K(2/x)^2
=
2^{2x-1}\Gamma(x+1/2)/\sqrt\pi.
\]
Therefore the logarithmic derivative is exactly
\[
2\log2+\psi(x+1/2),
\]
whose derivative is the positive trigamma function. Its value at \(x=0\) is \(-\gamma\), and it tends to infinity, so there is exactly one critical point and it is a strict global minimum. Reversing the variable \(x=2/m\) gives the stated sign pattern in \(m\).

The large-\(m\) expansion follows by subtracting the standard small-argument expansions of \(\log\Gamma(2x)\) and \(\log\Gamma(x)\). The coefficient after exponentiation is
\[
(\gamma^2+\pi^2)/(2m^2),
\]
which was checked independently. Stirling's formula proves divergence as \(m\downarrow0\).

## Originality

PASS. The fully inspected 2026 primary source records the exact gamma-ratio radius for \(e^{-|z|^m}\) but does not analyze its dependence on \(m\). It contains no stretched-exponential monotonicity theorem, critical exponent, or endpoint expansion.

The closest earlier weighted-Fock paper supplies upper bounds through special functions and is the source whose upper bounds the 2026 theorem makes sharp in the Hilbert setting. Its public abstract was inspectable, but full text was not available through the accessed endpoint; this is retained as a residual risk rather than treated as evidence of noncoverage.

A prior result on the same 2026 source classifies equality pairs at a fixed sharp radius. It does not compare the radii of different stretched-exponential weights and does not imply the unique parameter minimum without the gamma/digamma analysis carried out here.

Published-finding and web searches using the exact gamma ratio, the digamma critical equation, the weight family, and the numerical minimum did not locate an implication-equivalent theorem.

## Value

PASS. The stretched-exponential weights are a canonical one-parameter family singled out explicitly by the new sharp-radius theorem. Once exact radii are known, understanding how the geometric domination threshold changes with the decay exponent is a natural structural question.

The answer is not the naive monotonic one: stronger power decay lowers the radius only up to one finite exponent and then reverses direction. The unique minimum and the approach from below to \(1/\sqrt2\) provide a complete phase portrait for this canonical family and expose behavior that is invisible from the unspecialized moment formula alone.

Same-model review: passed. Independent audit: not yet performed.
