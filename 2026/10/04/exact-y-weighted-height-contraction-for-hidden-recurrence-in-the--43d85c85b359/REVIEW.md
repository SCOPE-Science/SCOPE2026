# Same-model review

## Correctness
PASS. Bounded completeness gives
\[
y(t)=\int_{-\infty}^{t}e^{-(t-u)}x(u)^2\,du>0.
\]
Arbitrary antiderivative tests in \(x\) give
\[
\mathbb E[yz\mid x]=-a.
\]
Using the two stationary identities inherited from the unchanged \(y\)- and \(z\)-equations yields
\[
\mathbb E[y]=\frac{1+\mathbb E[\dot z^2]}{16}.
\]
Therefore the \(y\)-weighted height is exactly
\[
\mathbb E_\nu[z]
=
-\frac{16a}{1+\mathbb E[\dot z^2]}.
\]
Zero defect forces the unique equilibrium by invariant-support tangency; positive defect gives the two strict mass consequences.

Risk: the proof uses standard disintegration and invariance of the support of a compactly supported invariant probability measure.

## Originality
PASS. The full foundational paper, full coexistence paper, and full generalized Sprott-E paper were compared. Previously known zero-forcing Sprott-E stationary identities were treated as prior coverage and are not claimed as new. The surviving positive-forcing theorem
\[
\mathbb E[yz\mid x]=-a,
\qquad
\mathbb E_\nu[z]
=
-\frac{16a}{1+D}
\]
and its rigidity and excursion consequences were not found in the inspected same-object sources or targeted semantic searches.

Risk: the complete 2020 global-geometry article was not securely available, so a differently phrased stationary identity there remains a specific residual risk.

## Value
PASS. The result constrains exactly the phenomenon that motivates the model: nontrivial recurrent dynamics coexisting with a stable equilibrium. At the published coexistence value \(a=0.01\), any periodic or strange invariant measure must have \(y\)-weighted mean height strictly between \(-0.16\) and zero and must place mass above the equilibrium height while retaining negative-height mass. This is a reusable invariant-measure diagnostic rather than a re-estimation of Lyapunov exponents.

Same-model review: passed. Independent audit: not yet performed.
