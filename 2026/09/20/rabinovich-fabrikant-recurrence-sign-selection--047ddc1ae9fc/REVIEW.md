# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The core identities are exact. For
\(W=x^2+y^2+4z\), direct differentiation gives
\(\dot W=2\gamma(x^2+y^2)-8\alpha z\). The third equation integrates to
the exact logarithmic relation for every orbit with \(z\ne0\).

For a compactly supported ergodic invariant measure off \(z=0\), the proof
of \(\int xy=-\alpha\) does not assume that \(\log|z|\) is integrable.
Instead it uses a point that is simultaneously Birkhoff-generic for the
bounded continuous observable \(xy\) and Poincare recurrent; recurrence
makes the logarithmic endpoint term sublinear along a subsequence. The
generator identity for the smooth bounded-on-support observable \(W\) then
gives the mean-height law. This avoids a hidden regularity assumption near
the invariant plane.

The invariant-plane statement follows from the exact identity
\(\dot q=2\gamma q\). The gamma-zero periodic classification follows from
the exact polar equation \(\dot\theta=1-r^2\cos^2\theta\). The period
integral is the standard elementary integral
\(\int_0^{2\pi}(1-r^2\cos^2\theta)^{-1}d\theta
=2\pi/\sqrt{1-r^2}\) for \(r<1\).

For \(\gamma<0,z\ge0\), \(W\ge0\) and
\[
\dot W\le-\min(2|\gamma|,2\alpha)W,
\]
so Gronwall gives global boundedness and exponential convergence. The
symbolic verification artifact returns zero residual for every algebraic
identity it checks.

Potential failure modes were examined: an ergodic off-plane measure cannot
mix signs of \(z\); equality in the periodic mean-height inequality forces
\(x+y\equiv0\), whose largest periodic invariant subset consists only of
equilibria; and the global convergence statement is restricted to the
half-space where \(W\) is positive definite.

## Originality — PASS

The 1979 Rabinovich--Fabrikant paper was inspected and already contains
the conservative energy \(x^2+y^2+4z\) for \(\gamma=\alpha=0\), so no
originality is claimed for that polynomial itself. It also identifies
\(z=0\) as the boundary of the physical half-space.

The accessible full text of Danca and Chen (2004) concentrates on
equilibria, dissipativity, bifurcation diagrams and numerical attractors.
The accessible full arXiv text corresponding to Danca, Feckan, Kuznetsov
and Chen (2016) records the invariant plane and the reduced-plane relation
\(\dot q=2\gamma q\), then largely studies invariant manifolds and unusual
attractors numerically. Diab, Guirao and Vera (2015) use first- and
second-order averaging to establish periodic orbits near zero-Hopf
equilibria. Turukina (2022), including its accessible full paper, explicitly
uses numerical integration and MatCont to study negative dissipation
parameters. Sajjad et al. (2026) use grid scans, time series, spectra and
empirical statistical diagnostics.

Searches also included synonymous formulations involving invariant
measures, ergodic averages, balance laws, mean z, global stability,
periodic-orbit averages, and the expression \(x^2+y^2+4z\). No inspected
source states the compact-ergodic identities
\(\int xy=-\alpha\) and
\(\int z=\gamma/2+(\gamma/(4\alpha))\int(x+y)^2\), their recurrence
half-space selection consequence, the exact gamma-zero periodic
classification with period formula, or the \(\gamma<0,z\ge0\) exponential
collapse theorem.

The principal residual originality risk is older or non-indexed RF
literature phrased in the original wave-amplitude variables rather than
the standard three-dimensional coordinates. The original 1979 article,
the major 2004/2016 RF analyses, and the 2022 negative-parameter paper
substantially reduce this risk. Originality remains "to the best of our
knowledge", not an exhaustive literature guarantee.

## Value — PASS

The result supplies exact constraints on recurrent statistics rather than
another numerical parameter scan. In particular, the mean-height formula
and anisotropy gap apply to periodic, quasiperiodic and chaotic ergodic
states with compact support and immediately forbid compact recurrent
states in the wrong sign half-space. The gamma-zero slice is classified
exactly at the level of all periodic orbits, including their periods.
The negative-growth theorem gives a simple global region in which the
physical half-space cannot support any nontrivial compact invariant set.
These statements complement a literature dominated by numerical
bifurcation and attractor studies.

## Scientific limitations

The measure statement is componentwise ergodic and assumes compact support.
The global convergence theorem does not cover \(z<0\), \(\alpha\le0\), or
all negative-parameter combinations studied numerically in the literature.
The result does not claim a complete classification of RF dynamics.
