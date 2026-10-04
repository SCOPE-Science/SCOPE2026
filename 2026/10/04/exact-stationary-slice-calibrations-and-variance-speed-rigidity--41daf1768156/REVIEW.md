# Same-model review

## Correctness
PASS. Stationarity against arbitrary antiderivatives of \(s=x+y\) gives
\[
\mathbb E[x\mid s]=A.
\]
Stationarity against arbitrary antiderivatives of \(y\) gives
\[
B\mathbb E[x\mid y]=y\mathbb E[x^2\mid y].
\]
These imply the conditional-variance and activator-size-biased nullcline formulas. A backward-time differential inequality rules out \(s\le A\) on any bounded complete positive orbit. Orthogonality of \(x-A\) to functions of \(s\), together with \(\dot s=A-x\), gives the covariance-speed identity. Zero defect forces the unique positive equilibrium.

Risk: compact support in the strictly positive quadrant is used to avoid integrability and boundary issues in the conditional formulas.

## Originality
PASS. The complete 1971 same-object article is the decisive prior comparison: it explicitly derives
\[
\frac{d}{dt}(X+Y)=A-X
\]
and, after one-period averaging, obtains
\[
\langle X\rangle=A.
\]
That global result is treated as prior and excluded from the originality claim. The surviving theorem keeps arbitrary slice test functions and obtains the stronger conditional law, an independent inhibitor-fiber relation, a size-biased nullcline calibration, the recurrent barrier, and an equality-rigid covariance-speed defect. Complete classical and modern same-object sources inspected did not state those surviving assertions.

Risk: the generator calculations are short, so an equivalent observation could remain in unindexed chemical-oscillation literature.

## Value
PASS. The result turns two natural Brusselator coordinates—the total concentration and inhibitor level—into exact stationary calibration variables. It gives a direct nullcline-based diagnostic for stationary data, a strict recurrent geometry \(x+y>A\), and a fluctuation identity that vanishes only at equilibrium. These statements remain meaningful on the classical stable limit cycle and refine the known global average rather than repeating it.

Same-model review: passed. Independent audit: not yet performed.
