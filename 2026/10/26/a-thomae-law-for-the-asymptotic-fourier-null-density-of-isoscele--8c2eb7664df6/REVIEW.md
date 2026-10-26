# Scientific review of the trapezoid Fourier-null density theorem

## Correctness

**PASS.** Direct integration yields the continuous sinc formula including the separately evaluated zero-frequency axis. Simultaneously taking real and imaginary parts splits the complete zero set into two exceptional vertical families and one reciprocal lattice. The monotonicities of \(\tan v/v\) and \(v\tan v\) give a frequency-counting estimate uniform over the offset of each vertical line. A planar lattice covolume count and a semicircle Riemann sum give the two individual densities. Rational-slope coincidence occurs precisely when the vertical-line index is divisible by the denominator, at which the two descriptions agree except for bounded per-line exclusions. This produces the exact overlap correction and therefore the stated \(O_\alpha(R)\) remainder. No finite diagnostic is used in place of this argument.

A reproducible numerical checker independently integrates the Fourier formula, tests specified lattice zeros, and compares distinct-zero counts with the theoretical leading terms. It is supplementary evidence only.

## Originality

**PASS, with publication-priority risk.** The directly inspected 2016 Diaz–Le–Robins source proves general Fourier-transform and solid-angle formulas for polytopes; the 2017 Wuttke source gives analytic polygon form factors and removable-singularity handling. Neither states a real-zero lattice-plus-line classification or counts zeros of isosceles trapezoids. The 2024 Kolountzakis–Spyridakis results forbid complete analytic curves contained in the complex zero variety but do not provide an isolated-real-zero census or arithmetic density. Comparisons with accessible prior Fourier-zero studies of triangles, hexagons, and annuli show differences of object and count statement; none logically covers this fixed-area trapezoid result. A previously unindexed exact calculation in diffraction or shape-transform literature remains a genuine risk; independent literature review is needed for publication.

## Mathematical value

**PASS.** The Fourier-null set of a polygonal aperture is a natural diffraction invariant, not an arbitrary numerical slice. A fixed-area family has an exactly computable quadratic density that changes with the shape and suffers dense rational discontinuities; the jump size is arithmetic (the reduced denominator), not merely geometric. The complete global zero-set decomposition explains the mechanism and offers a reproducible benchmark for zero-finding schemes. It also exposes a distinction between finite-radius pattern stability and limiting zero-density stability. The theorem's limits are real frequencies, isosceles geometry, and strict nondegeneracy.

## Closest source comparisons and limits

- Diaz, Le, and Robins, *Fourier transforms of polytopes, solid angle sums, and discrete volume*, arXiv:1602.08593 (2016): general transform formulas and lattice sums; no trapezoid real-zero asymptotics in the inspected statements.
- Wuttke, *Form factor (Fourier shape transform) of polygon and polyhedron*, arXiv:1703.00255 (2017): polygon form factors and numerical singularity handling; no count or arithmetic resonance theorem in the inspected statements.
- Kolountzakis and Spyridakis, *Curves in the Fourier zeros of polytopal regions and the Pompeiu problem*, arXiv:2404.03405 (2024): exclusion of analytic curves in Fourier-null varieties; not a distinct-zero enumeration for trapezoidal apertures.

The possible presence of an indexed or unindexed exact trapezoid formula with the same quadratic-density consequence cannot be ruled out by search absence alone.

Self-review: passed. Independent audit: not yet performed.
