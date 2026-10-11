# Review of Sharp real-zero phase transition for Gegenbauer partial sums

## Correctness

PASS. For fixed
\[
0<\alpha<1,
\]
the DLMF interior asymptotic writes \(C_k^{(\alpha)}(\cos\theta)\) as an oscillatory term with amplitude comparable to
\[
k^{\alpha-1}
\]
plus a summable
\[
O(k^{\alpha-2})
\]
remainder, uniformly away from the endpoints. The exact Pochhammer amplitude decreases because
\[
(k+2\alpha)/(k+\alpha+1)<1.
\]
Uniform Dirichlet summation therefore makes the tail of the Gegenbauer series
\[
O(n^{\alpha-1}),
\]
and its ordinary sum equals its Abel value
\[
(2-2x)^{-\alpha}.
\]
Hence the partial sums are eventually positive on every fixed compact interior interval.

The exact derivative identity raises the parameter to
\[
\alpha+1>1.
\]
The primary theorem therefore places all derivative zeros in
\[
(-1,1)
\]
for large degree and gives their arcsine limiting density. Rolle counting confines any real zeros of the original partial sum to arbitrarily thin endpoint layers, apart from at most one zero on the negative exterior ray. Taking the endpoint-layer width to zero yields
\[
R_n(\alpha)/n\to0.
\]

## Originality

PASS. The fresh paper proves eventual real-rootedness for
\[
\alpha\ge1
\]
and displays a Legendre counterexample, but it does not state a theorem for all
\[
0<\alpha<1
\]
or quantify the asymptotic real-zero count.

Searches for Gegenbauer partial sums, subcritical real-zero proportions, converse real-rootedness, and exact-source follow-ups found no implication-equivalent published result. Classical positivity papers concern differently weighted or normalized Jacobi/Gegenbauer sums and do not classify the real zeros of the unweighted polynomial in its spatial variable.

A residual risk is that an older orthogonal-polynomial source may contain the same subcritical consequence under a different partial-sum terminology, but the closest located results do not cover it.

## Value

PASS. The source theorem leaves open whether
\[
\alpha\ge1
\]
is a true geometric threshold or merely the range accessible to its proof. The new result gives the strongest possible qualitative converse: below \(1\), not just some but asymptotically almost all zeros are nonreal.

This produces a complete zero-geometry phase diagram for the real-zero fraction and identifies the derivative parameter shift
\[
\alpha\mapsto\alpha+1
\]
as the mechanism connecting the two phases.

Same-model review: passed. Independent audit: not yet performed.
