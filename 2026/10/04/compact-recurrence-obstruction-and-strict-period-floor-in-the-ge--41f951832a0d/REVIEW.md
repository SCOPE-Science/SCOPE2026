# Same-model review

## Correctness
PASS. Coordinate stationarity yields \(\mathbb E[z]=0\), \(\mathbb E[y]=-\mathbb E[x^2]\), and \(\mathbb E[x^2]=a+b\mathbb E[x]\), hence the exact mean–variance parabola. Variation of constants proves \(y<0\) on every bounded complete trajectory. Three exact generator identities give \(\mathbb E[(a+bx+y)^2]=b\mathbb E[z^2]\); their equality cases force equilibrium support when \(b\le0\). For \(b>0\), the sign changes follow from zero integrals of \(p(x)\) and \(z\). The period floor follows from the energy law plus Wirtinger, and the equality case is excluded by the second harmonic created by \(x^2\) in the exact jerk equation. The packaged exact checker returns `VERIFY_OK`.

## Originality
PASS. Targeted semantic database and web searches for Sprott M, its exact equations, invariant measures, the jerk reduction, recurrence balance, and period bounds returned no same-object theorem. The full substantive 1994 article gives Case M, critical points, Lyapunov data, dimension, and numerical parameter behavior. The generalized parameter-space note gives the \(a,b\) family and numerical dynamic-region maps. The ABS-M source studies a different absolute-value nonlinearity. None of the inspected statements implies the invariant-measure energy law, the \(b\le0\) compact-recurrence obstruction, or the strict period floor. Residual indexing risks are recorded in `AUDIT.json`.

## Value
PASS. Case M is one of the classical algebraically minimal chaotic flows, and its two-parameter normalization has documented stable, periodic, chaotic, and unbounded regions. The theorem converts the coefficient sign \(b\) into a rigorous global recurrence obstruction, supplies exact stationary geometry for all compact invariant measures, and gives a universal strict period floor for every nonconstant cycle. This is structural information rather than a parameter scan or numerical recomputation.

## Closest literature and limitations
Sprott (1994) is the foundational source and Sprott's 2013/2014 note gives the exact two-parameter Case M normalization. The 1999 ABS variant is a nearby but inequivalent nonlinear system. The 1997/2008 jerk literature concerns algebraically simple jerk systems and nonchaotic parameter regions; the inspected material does not state the theorem here. The result does not establish existence of non-equilibrium compact recurrence for arbitrary positive \(b\).

Same-model review: passed. Independent audit: not yet performed.
