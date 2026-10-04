# Same-model review

## Correctness
PASS. Stationarity against arbitrary antiderivatives of \(x\) gives
\[
\mathbb E[y\mid x]=\frac{C}{B}(x+p).
\]
The regression residual is exactly \(\dot x/B\), so conditional-expectation orthogonality gives
\[
\operatorname{Var}(y)-\left(\frac{C}{B}\right)^2\operatorname{Var}(x)
=
\frac1{B^2}\mathbb E[\dot x^2].
\]
Zero residual makes \(x\) and then \(y\) constant on each support trajectory; bounded completeness reduces the remaining cases to equilibria. The quadratic temperature generator and the \((x+p)^2/2\) generator then give the three-term budget.

Risk: the equality classification uses standard invariance of the support of a compactly supported invariant probability measure.

## Originality
PASS. The strongest prior source was inspected in full and already contains the quadratic Lie derivative implying
\[
\mathbb E[y^2+z^2-z]=0.
\]
That temperature-circle balance is therefore treated as prior, not as a new result. The inspected localization, rigorous-chaos, periodic-orbit, bifurcation, and invariant-surface sources do not state the conditional current regression, the exact current-speed variance defect, or its equilibrium-only equality classification. Targeted equivalent-form and Lorenz-equivalence searches returned no same-object implication of that surviving claim.

Risk: a differently phrased derivative-energy identity may remain in unindexed ENSO or Lorenz literature.

## Value
PASS. The result turns a physically meaningful stationary regression into an exact dynamical diagnostic: the variance gap is precisely mean-square current speed. It is strict for every genuinely time-dependent compact stationary state, and it refines the known temperature localization into a current-displacement/current-acceleration/mean-temperature budget at the standard asymmetric parameters as well as for arbitrary constant asymmetry.

Same-model review: passed. Independent audit: not yet performed.
