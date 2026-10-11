# Same-model review

## Correctness
PASS. Antiderivative tests in the three coordinates give
\[
\mathbb E[y\mid x]=0,
\qquad
\mathbb E[z\mid y]=0,
\qquad
\mathbb E[x^2-cx-by\mid z]=az.
\]
Averaging yields
\[
\mathbb E[x^2]=c\mathbb E[x],
\]
hence
\[
\operatorname{Var}(x)=m(c-m).
\]
Endpoint variance zero forces the corresponding equilibrium atom. The nonlinear forcing residual is exactly \(\dot z\), giving the stated variance defect, covariance, and correlation formula. Zero vertical-speed defect on compact invariant support forces \(z=y=0\) and then \(x\in\{0,c\}\).

Risk: compact support is used to make every generator test integrable and to justify bounded-complete-trajectory rigidity.

## Originality
PASS. The closest same-object indexed result already proves a different Genesio recurrence balance,
\[
\mathbb E[z^2]=b\mathbb E[y^2],
\]
and a sharp period floor; those are excluded from the originality claim. A complete open 2012 same-object article and a complete 2013 same-object PDF were inspected at statement and implication level and contain no matching invariant-measure moment theorem. The modern global-dynamics/integrability source has different stated results; its restricted full text is retained as a residual risk.

Risk: the invariant-measure proof is short enough that an unindexed equivalent observation remains possible.

## Value
PASS. The result links the model's two fixed points to the statistics of every compact invariant state through a sharp barycenter–variance parabola, and it supplies a fiberwise nonlinear-forcing calibration whose residual is exactly vertical-speed energy. These identities are directly testable on periodic and chaotic recurrent data and are structurally stronger than the known integrated recurrence balance.

Same-model review: passed. Independent audit: not yet performed.
