# Same-model review

## Correctness
PASS. Three arbitrary antiderivative test families give
\[
\mathbb E[y\mid x]=0,\qquad
\mathbb E[x+z^2\mid y]=0,\qquad
\mathbb E[y\mid z]=2z-1.
\]
Coordinate stationarity and the exact generator identities for \(y^2/2\), \(xz\), and \(yz\) then give
\[
\mathbb E[z]=\frac12,\qquad
\mathbb E[x]=-\frac14-V,
\]
\[
\mathbb E[y^2]=6V,\qquad
\operatorname{Cov}(y,z)=2V,
\]
and
\[
\mathbb E[(z-\tfrac12)^3]=-V.
\]
The zero-variance support is the unique equilibrium. The factorized third-moment law forces every other invariant measure to place positive mass below \(z=-1/2\), and its fixed mean then forces positive mass above \(z=1/2\).

Risk: the equality and excursion arguments use standard invariance of the support of a compactly supported invariant probability measure.

## Originality
PASS. The full foundational article was inspected and contains the exact equations, equilibrium, Lyapunov data, and numerical Case N attractor but no invariant-measure theorem. Exact-object semantic searches found no conditional, correlation, skewness, or all-measures excursion statement.

Risk: complete text of Panchev's 2004 all-systems analytical paper and the Case N section of Starkov–Coria's 2005 periodic-localization paper was unavailable. To avoid a decisive unresolved comparison, no periodic-orbit localization corollary is included in the accepted claim.

## Value
PASS. The result gives a universal non-equilibrium correlation
\[
\sqrt{\frac23},
\]
an exact central skewness law, and a sharp forced excursion below a natural height boundary one unit below the unique equilibrium. These provide exact stationary diagnostics and geometric restrictions for a benchmark simple chaotic flow rather than a numerical recomputation of known Lyapunov data.

Same-model review: passed. Independent audit: not yet performed.
