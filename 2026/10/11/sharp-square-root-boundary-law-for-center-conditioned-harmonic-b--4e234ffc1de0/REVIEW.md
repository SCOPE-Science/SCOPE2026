# Review of Sharp square-root boundary law for center-conditioned harmonic Bohr radii

## Correctness

PASS. For any bounded complex harmonic disk map, its \(L^\infty\) boundary trace has the same positive and negative Fourier coefficients as the harmonic expansion. Parseval bounds the combined nonconstant coefficient squares by \(1-a^2\). Cauchy--Schwarz, using both signs of each frequency, therefore yields
\[
B_f(r)\le a+\sqrt{2(1-a^2)}\frac r{\sqrt{1-r^2}}.
\]
Solving its exact inequality against one yields \(r^2\le(1-a)/(3+a)\). The smooth trace \(e^{i\varepsilon\cos t}\) is unimodular, its Poisson extension is admissible, and its mean and first two Fourier coefficients have rigorously controlled Taylor expansions \(a=1-\varepsilon^2/4+O(\varepsilon^4)\) and \(|c_1|+|c_{-1}|=\varepsilon+O(\varepsilon^3)\). Its first-coefficient majorant forces the matching limsup \(1/2\). For \(a=1\), the harmonic maximum principle gives only constant maps. The comparison with the previously claimed radius is strictly algebraic for every \(a<1\).

## Originality

PASS. Ahamed--Hossain (arXiv:2604.14217v1, Theorem 2.1) asserts that the smaller linear-scale formula \((1-a)/(1-a+4/\pi)\) is sharp. The inspected full proof uses individually sharp degreewise coefficient inequalities and does not exploit joint Fourier-energy constraints or determine a square-root boundary law.

The closely related Abu Muhanna 2010 paper was read in full in its bounded-harmonic section. Its no-uniform-radius phenomenon is distinct and does **not** imply the rate for radii conditioned on the center magnitude. The 2014 article and later harmonic subclass works similarly do not state the precise leading law. Multiple formulation-specific published-record and prior-finding searches detected no covering statement; an unindexed prior observation remains possible.

## Value

PASS. The new theorem changes both the quantitative scale and leading constant of the radius reported as best possible in a fresh published-preprint argument, using a natural energy conservation principle unavailable to one-coefficient saturation. It pairs a universal bound on the entire harmonic class with an exact near-constant witness, yielding a natural sharp asymptotic invariant rather than merely a numerical correction. The endpoint discontinuity is structurally relevant to fixed-center formulations and reconciles with the known absence of a radius uniform in the center value.

Same-model review: passed. Independent audit: not yet performed.
