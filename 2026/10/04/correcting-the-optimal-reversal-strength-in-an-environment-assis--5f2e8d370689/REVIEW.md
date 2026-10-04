# Same-model review

## Correctness

**PASS.** The claim starts from the source's displayed equations
\[
C_3=\frac{2(1-d)\sqrt{1-q}}{(1-d)+(1-q)}
\]
and
\[
P_3=\frac{(1-q)+(1-d)}2.
\]
With \(r=1-d\) and \(y=1-q\), differentiation gives
\[
\frac{dC_3}{dy}
=
\frac{r(r-y)}{\sqrt y(r+y)^2},
\]
so the unique concurrence maximum is \(y=r\), or \(q=d\). Direct substitution proves the corrected concurrence and success probability, while exact factorization proves that both exceed the values at the source's \(q=2d-d^2\) for every \(0<d<1\). Monotonicity of \(C_3\) and \(P_3\) on the two sides of \(y=r\) gives the complete Pareto frontier. A standalone checker independently replays the formulas and representative-state concurrence.

## Originality

**PASS, narrowly scoped.** The primary paper explicitly states \(q^O=2d-d^2\) immediately after its equations for \(C_3\) and \(P_3\), and then uses the resulting quantities in later comparisons. The searched literature did not surface an erratum or later publication correcting that scalar optimum. The accepted originality claim is only the correction, strict domination statement, and Pareto characterization for this one scheme.

A later survey cites the source in its review of weak-measurement protection methods, but the inspected material did not surface the corrected \(q=d\) condition. Residual risk remains because a simple derivative correction may have been noticed in unindexed notes or under another parameter convention.

## Value

**PASS.** The corrected point is not merely a numerically better concurrence setting: it also has strictly higher success probability than the published point. Thus the value labeled optimal in the source lies on a dominated branch. The correction changes the quantitative benchmark used in the source's subsequent scheme-three comparisons and supplies the exact efficient tradeoff curve needed for future experimental or theoretical use of that protocol.

Same-model review: passed. Independent audit: not yet performed.
