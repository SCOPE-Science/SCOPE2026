# Self-review

## Correctness
PASS. The positive-diagonal QR factorization of a \(2\times2\) SPD matrix can be written explicitly. Direct multiplication gives
\[
b^+
=
b\,\frac{\det A}{a^2+b^2}.
\]
Swapping coordinates changes only the denominator to
\[
d^2+b^2,
\]
so the larger column norm is exactly the better order.

At fixed eigenvalues \(\mu<L\), the two squared column norms sum to
\[
\mu^2+L^2.
\]
This yields the sharp best-order factor
\[
\frac{2\mu L}{\mu^2+L^2}
=
\frac{2\kappa}{\kappa^2+1},
\]
with equality at equal column norms. The spectral-angle formula independently gives the exact fixed-order growth region and the supremum \(\kappa\). The packaged exact checker replays all stated witnesses.

## Originality
PASS with stated residual risk. Classical QR iteration is prior work. The closest full primary source already proposes descending diagonal and descending column-norm permutations and reports improved convergence; those ideas are explicitly treated as prior.

The new statement is the exact \(2\times2\) off-diagonal map, proof that the proposed column ordering is the optimal one-step permutation for this metric, the sharp robust contraction factor, and the nearly-\(\kappa\) fixed-order transient. Targeted semantic and literature searches found no implication-equivalent theorem.

The principal residual risk is an older textbook or QR paper containing the same elementary two-dimensional identity under different terminology.

## Value
PASS. The prior permutation paper motivates ordering as a convergence accelerator but supports its low-cost rules largely through intuition and simulation. The theorem gives a precise mathematical safeguard for the same rule in the smallest nontrivial SPD case and quantifies both its benefit and the transient it prevents.

## Closest literature and limitations
The closest full source is the 2014 symmetric-QR-permutation paper, whose column ordering is exactly descending column norm. Watkins provides archive-era QR background and primary MSC \(65F15\). The theorem is one-step, unshifted, and two-dimensional; practical shifted QR and higher-dimensional behavior remain outside scope.

Self-review: passed. Independent audit: not yet performed.
