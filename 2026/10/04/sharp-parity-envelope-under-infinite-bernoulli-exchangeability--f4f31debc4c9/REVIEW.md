# Review

## Correctness

PASS. Infinite exchangeability reduces the problem exactly to a random
\(P\in[0,1]\) with fixed mean. The parity bias is
\[
\mathbb E(1-2P)^n.
\]
After the affine change \(M=1-2P\), this is a one-moment extremal problem for
\(x^n\) on \([-1,1]\). For even \(n\), Jensen and the endpoint mixture give
the exact interval. For odd \(n\), the stated tangent line is proved to be the
least concave majorant, and odd symmetry gives the greatest convex minorant.
The one- and two-atom extremizers attain every boundary piece, and convex
mixing fills the interval.

The fair-marginal asymptotic follows directly from the defining equation for
\(c_n\), not from numerical extrapolation.

## Originality

PASS, with a residual historical-literature risk. The full Rougier preprint
was inspected at its representation theorem and extendability discussion. It
provides the exchangeability framework but no parity optimization. The full
Zaigraev--Kaniovski preprint was inspected at its setup and main theorem; it
optimizes monotone tail events for finite exchangeable Bernoulli trials, not
parity under infinite extendibility.

The closest published semantic record concerns exact tail envelopes for
infinitely extendible Bernoulli trials. It uses the same de Finetti
one-moment reduction, but its objective is a binomial tail. It does not state
the power-envelope parity theorem, the odd tangent root, or the fair-marginal
\([1/4,3/4]\) limit.

Targeted searches for parity, XOR, exchangeable Bernoulli sums, binomial
mixtures, and de Finetti parity did not locate an equivalent statement.

## Value

PASS. Parity is a canonical nonmonotone statistic that is invisible to the
single marginal mean but highly sensitive to higher-order dependence. The
theorem gives its complete finite-\(n\) feasible interval under the important
extendibility constraint, identifies explicit extremal mixing laws, and
exhibits a qualitative even/odd phase split. The fair-marginal limit shows
that infinite exchangeability still permits persistent parity bias, but only
inside a sharp asymptotic interval.

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK odd_envelope_checks=300150 endpoint_atom_checks=187884 even_envelope_checks=300150 root_checks=50 fair_asymptotic_checks=5`.
