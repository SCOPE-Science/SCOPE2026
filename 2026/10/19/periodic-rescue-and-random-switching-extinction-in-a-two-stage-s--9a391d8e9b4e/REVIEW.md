# Independent mathematical audit

## correctness

PASS

Two updates give the diagonal product with entries b_j s_i and s_j b_i. For every 0<q<1, each parity subsequence has transition matrix P² with off-diagonal entry 2q(1−q)>0, equal stationary weights, and aperiodicity. Applying the finite-state ergodic theorem to the two parity logs gives (b₁b₂s₁s₂)^(1/4) for both positive stage components. A last odd update changes the log total by a bounded amount. At q=0 the two positive components retain both diagonal branches, giving √max(b₁s₂,b₂s₁); strict separation is exactly the unequal-cross-product case. At q=1 the environment stays fixed, outside the interior formula. The example has both squares I/4 and alternating two-step diagonal entries 1/64 and 4, confirming 1/2, 2 and 1/2 for the three respective modes. For the mean, condition on the Markov state and regroup the resulting four coordinates by stage; the expected-state matrix then has off-diagonal blocks diag(b)P and diag(s)P. This yields the two quadratic factors and the stated radical expression for its Perron root. Irreducibility suffices despite period two, because the strictly positive left Perron vector bounds the sum of expected coordinates above and below by constant multiples of μ(q)^t, even from a fixed starting environment. The smaller root of 8x²−17(1−q)x+2−4q is at most 1/2 for q≤1/2 (nonnegative roots with product at most 1/4), and negative for q>1/2. The sign of this polynomial at x=1 is that of 13q−7, giving exactly the stated mean threshold. Critical means exponential rate one, not survival. The strict modal comparisons persist by continuity within the admissible demographic region; a strict mean comparison is locally stable at any fixed q away from criticality, not a universal unchanged threshold under perturbation. A separate exact symbolic replay at branches/92cfc60a-415e-4304-81cb-edefcf2af840/reproduce_expected_multiplier.py confirmed the characteristic factorization, P(1)=13q−7 and μ(7/13)=1. The uploaded verifier was inspected, not run; its path enumerations and simulations were not needed for the infinite-time proof.

## originality

PASS

The supported distinct contribution, to the best of the statement-level evidence checked, is the exact parity-dependent boundary law for this semelparous class and its joint comparison with the exact ensemble threshold in a single witness. The general distinction between typical and mean growth, deterministic versus probabilistic matrix-product gaps, and the use of Markov-conditioned expectation matrices are not new. No inspected stronger result supplies this boundary calculation or the combined rescue and extinction regimes.

## value

PASS

The completely semelparous model is a natural demographic boundary. The exact q-independent almost-sure extinction rate despite arbitrarily rare departures from deterministic rescue identifies a meaningful singular limit, and the mean calculation gives a precise regime where expected growth misdiagnoses typical behavior. The contribution is the controlled boundary example and class-level mechanism, not the threshold number in isolation or a claim about populations with nonzero stage retention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
