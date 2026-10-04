# Same-model review

## Correctness
PASS. Arbitrary one-variable antiderivative tests give
\[
\mathbb E[y\mid x]=x,\qquad
\mathbb E[xz\mid y]=cy,\qquad
\mathbb E[xy\mid z]=bz.
\]
Their integrated and weighted consequences yield
\[
\mathbb E[z(z-c)]
=
\frac cb\,\mathbb E[(y-x)^2].
\]
Zero defect places the invariant support in \(y=x\); tangency and bounded completeness reduce it exactly to the three equilibria. The slab obstruction then follows from the pointwise sign of \(z(z-c)\) on \(0\le z\le c\). The packaged checker verifies the polynomial certificates exactly.

Risk: the equality proof uses the standard invariance of the support of a compactly supported invariant probability measure.

## Originality
PASS. The foundational full text, the unified Lorenz–Chen transition paper, and a detailed full Lorenz–Chen–Lü comparison were inspected. The latter explicitly treats coordinate/time scalings and generalized-Lorenz equivalence, so normalization aliases were included in the comparison. Exact-object semantic searches found no statement implying the three conditional laws or the equality-rigid slab defect.

Risk: complete text of the 2016 global-boundedness paper was unavailable after bounded lawful-access attempts; possible differently phrased overlap there remains explicit.

## Value
PASS. The theorem upgrades the Lü system's familiar equilibrium geometry into a universal stationary restriction: equilibrium mixtures are exactly the zero-defect states, while every genuinely recurrent compact state must leave the whole equilibrium-height interval in measure. The coordinate-wise conditional laws are exact binwise constraints and are materially finer than ordinary numerical averages or Lyapunov-exponent data.

Same-model review: passed. Independent audit: not yet performed.
