# Self-review

## Correctness

PASS. The source's exact rational recurrence was reconstructed from Eq. (36). Exact factorization reduces its only interior physical fixed point to the unique \(z_*>2\) solving \(z^3+z^2-2z-16=0\). Strict monotonicity of the cubic on \([2,\infty)\), together with the reciprocal substitution, proves uniqueness. The sign of the same factorization proves strict decrease below the threshold and strict increase above it. Invariance of \([0,1/2]\), continuity, and the complete fixed-point classification prove the limiting basins. The packaged symbolic replay returned `VERIFY_OK`.

Risk: the theorem is restricted to the source's twirled independent-noise one-dimensional recurrence.

## Originality

PASS. The anchor reports only a numerical H-type threshold \(\epsilon_0\approx0.141\), although its separate T-type protocol is treated exactly. A later primary comparison still quotes \(0.141\) for the 15-to-1 H-state routine and distinguishes broader H-state protocols. Focused published-finding and literature searches for source identifiers, Reed–Muller/15-to-1 aliases, the high-precision value, the reciprocal polynomial/cubic, and basin terminology found no implication-equivalent statement.

Residual risk: an unindexed note, thesis, or software derivation may contain the same algebraic reduction.

## Value

PASS. The 15-to-1 routine is a canonical benchmark in magic-state distillation. A low-degree exact threshold is a natural protocol invariant, and the factorization simultaneously supplies the complete global one-dimensional dynamics rather than only a decimal crossing estimate. The result cleanly separates failure of this routine above threshold from nondistillability by all routines.

Self-review: passed. Independent audit: not yet performed.
