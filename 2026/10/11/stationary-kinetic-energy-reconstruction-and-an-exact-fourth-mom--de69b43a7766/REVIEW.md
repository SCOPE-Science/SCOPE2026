# Same-model review

## Correctness
PASS. Stationarity of arbitrary antiderivatives of \(x\) gives \(\mathbb E[v\mid x]=0\). The generator of \(\phi(x)v\) then yields
\[
\mathbb E[\phi'(x)v^2]=\mathbb E[x\phi(x)].
\]
Its distributional form reconstructs the kinetic-energy projection exactly from the position marginal. Monomial tests give the full moment hierarchy, and the mechanical-energy derivative gives the damping balance; together they imply
\[
\mathbb E[x^4]=3\mathbb E[x^2].
\]
The endpoint \(\mathbb E[x^2]=3\) is excluded by equality rigidity and invariance.

Risk: compact support is used to justify unrestricted antiderivative tests and the finite-measure distribution argument.

## Originality
PASS. The strongest inspected same-object prior work is a complete article devoted to rigorous van der Pol long-time averages. It writes the exact system and bounds the average of \(x^2+v^2\), but targeted complete-text searches found no moment, variance, conditional, virial, or fourth-moment formulation matching the accepted theorem. Direct semantic and exact-phrase searches likewise found no same-object implication.

Risk: the original 1920 article was not used for whole-document noncoverage, and an equivalent historical virial identity could remain unindexed.

## Value
PASS. The theorem reconstructs an entire stationary kinetic-energy marginal, not just one scalar average, and it produces an infinite exact moment hierarchy. The parameter-independent fourth-moment law and strict RMS ceiling provide immediate reproducibility checks for numerical or experimental stationary data and tie recurrent motion to both signs of the nonlinear damping.

Same-model review: passed. Independent audit: not yet performed.
