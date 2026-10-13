# Self-review

## Correctness
PASS. A generic one-parameter subgroup of the row-column scaling torus has exactly the \(mn\) coordinate matrices as fixed points in projective matrix space. Every such point has rank \(1\), so every nontrivial rank locus has that same fixed set and hence Euler characteristic \(mn\).

For the maximal-minor locus, Thom--Porteous applied to
\[
\mathcal O(-1)^{\oplus m}\to\mathcal O^{\oplus n}
\]
gives degree
\[
\binom{n}{m-1}.
\]
The quotient by \(mn\) has exact adjacent-\(n\) ratio
\[
\frac{n}{n-m+2},
\]
which is strictly greater than \(1\) for \(m\ge3\). The base values at \(n=m,m+1,m+2\) give the complete crossover and the two equality pairs.

The bundled checker independently verifies the general determinantal product, its maximal-minor specialization, and every comparison over a broad finite range. Finite computation is regression evidence only.

## Originality
PASS. The square all-rank Euler constancy is already explicit in Zhang and is treated as prior coverage. The inspected literature does not state the rectangular \(mn\) extension together with the maximal-minor degree comparison. Targeted searches did not locate the two equality formats \((3,7)\) and \((5,7)\), and nearby indexed determinantal results concern degree curvature or divisibility instead.

Residual risk remains because both ingredients are classical and the final inequality is elementary once they are combined.

## Value
PASS. The result compares two canonical invariants of a fundamental singular family: a rank-independent topological invariant and a rank-condition projective degree. The exact phase diagram explains how rectangular aspect ratio drives the maximal-minor degree through the fixed Euler baseline and isolates precisely two equality formats.

Self-review: passed. Independent audit: not yet performed.
