# Self-review

## Correctness
PASS. The exact Newton error identity
\[
Z_{k+1}
=
\frac12Z_k^2(I+Z_k)^{-1}
\]
shows that the lowest nonzero nilpotent degree doubles at each step. Its coefficient obeys
\[
c_{k+1}=\frac{c_k^2}{2},
\qquad
c_0=1,
\]
so
\[
c_k=2^{\,1-2^k}.
\]
For a size-\(n\) Jordan shift this proves exact termination precisely when
\[
2^k\ge n.
\]

For \(n\ge3\), the first step maps \(e_3\) to an error vector of norm \(M^2/2\), while the initial spectral error is \(M\). The \(3\times3\) family makes the factor \(M/2\) exact and terminates on the next step. The embedded checker replays the identities in exact rational arithmetic.

## Originality
PASS with stated residual risks. Newton's matrix-sign iteration, its global convergence theory, and generic nonnormal transient growth are prior work.

The closest full source explicitly says that matrix-sign Newton errors are not determined solely by eigenvalues because the iterates are generally nonnormal. It does not state the unipotent Jordan family, the exact dyadic termination law, the minimal dimension-three obstruction, or the exact amplification factor.

Targeted published-record and literature searches did not locate an implication-equivalent theorem. The main residual risk is older matrix-function literature expressing the same Jordan calculation under different terminology.

## Value
PASS. The matrix-sign literature itself identifies eigenvalue-insensitive nonnormal error as a practical complication. The theorem gives an exact, dimension-minimal model of that complication: every eigenvalue is already at the correct sign value, yet the matrix error can grow without bound before exact finite termination. The dyadic termination count and equality family make the phenomenon structurally informative rather than a generic numerical counterexample.

## Closest literature and limitations
The closest inspected primary source is Higham–Mackey–Mackey–Tisseur's full treatment of polar and matrix-sign iterations. Kenney–Laub provides broader rational-iteration background but was access-limited through the inspected route. The theorem concerns unscaled Newton, exact arithmetic, and a structured unipotent family; scaling, fixed-condition-number extremals, and floating-point behavior are outside scope.

Self-review: passed. Independent audit: not yet performed.
