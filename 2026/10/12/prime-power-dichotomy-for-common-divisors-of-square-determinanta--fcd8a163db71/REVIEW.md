# Self-review

## Correctness
PASS. The degree formula is used in two independently checkable forms: the classical product and the rectangular Schur determinant
\[
D_{n,n-c}=\det\!\left[\binom{n}{c-i+j}\right].
\]
For \(n=p^e\), Lucas's theorem makes this matrix strictly upper triangular modulo \(p\), so every proper rank-stratum degree is divisible by \(p\). If \(n=p^e m\) with \(m>1\) and \(p\nmid m\), the corank \(c=p^e\) makes every factor in the localized degree product a \(p\)-adic unit. Since the determinant hypersurface has degree \(n\), these two observations prove the full common-prime dichotomy.

The exact checker independently matches the determinant and product formulas and verifies the theorem over a finite range. Those computations are regression evidence only.

## Originality
PASS. The closest arithmetic source reproduces the determinantal degree product and studies parity of individual rectangular-matrix degrees. The closest primary algebraic-geometry source studies the same bounded-rank matrix varieties and their nested rank loci. Targeted searches did not locate the all-ranks statement that a common prime exists exactly at prime-power matrix size, nor the explicit corank \(p^{\nu_p(n)}\) witness in the non-prime-power case.

Residual risk remains from older plane-partition, Schur-function, and foundational determinantal literature, especially the original Harris--Tu article, which was not fully inspected.

## Value
PASS. The result classifies a natural arithmetic invariant of the entire singular-rank tower rather than one isolated degree. It sharply separates prime-power matrix sizes from all others and supplies an explicit rank stratum that destroys each candidate common prime in the composite case.

Self-review: passed. Independent audit: not yet performed.
