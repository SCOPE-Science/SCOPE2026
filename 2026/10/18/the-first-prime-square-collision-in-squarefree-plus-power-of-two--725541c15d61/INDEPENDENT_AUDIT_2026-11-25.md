# Independent mathematical audit

## correctness

PASS

For the repaired comparison, exact trial factorization gives only (difference, prime)=(20,5) for q≥5 and differences 1–20. The prime progression removes 2 and 3 obstructions at admissible exponents. At fixed cutoff Y, CRT and the prime number theorem in fixed progressions give uniform independent reduced choices at squares of primes 5≤q≤Y. For any fixed shift c, q>Y up to X^{1/4} contributes at most 4X/(φ(q²)log X) primes per q by Brun–Titchmarsh in the reduced class c mod q². Larger q up to √X are bounded by counting integers, O(X^{3/4}+√X) in total. Dividing by π(X;36,7) and letting Y→∞ proves the infinite model, since the same tail is summable in the model. This replaces the frozen proof’s moment argument, which used a squarefree-tuple count with a majorant allowing nonsquarefree divisors and described a modulus bound as a divisibility. At q=5 the two laws agree on the probability of covering zero or one missed labels; they differ only for U={0,20}, when the collision contributes 1/20. Forcing the ordinary labels at sixteen separate primes and avoiding the special classes elsewhere has a positive product probability. The signed sum follows from changing the q=5 factor only for subsets containing both special labels. Separate finite replay by state counting instead of inclusion–exclusion confirms the factor arithmetic and correction in truncated models with up to twenty other primes: python3 /workspace/branches/independent_replay.py 2. The asymptotic proof, not the finite replay, establishes the repaired sign in the infinite model.

## originality

PASS

Pass applies only to the corrected scope: the positive-event identity and strict direction of the first collision error relative to the all-distinct benchmark. The exact eighteen-exponent density as a purported new result fails the prior-implication check. Harman–Paquin explicitly gives the arbitrary finite-set distinct-residue law at p. 13, which mechanically yields that density and even the signed correction expression. The frozen comparison to Remark 4 alone materially understates coverage. The repair credits the exact formula and isolates what is not supplied by that law as stated: resolving the sign of a cancellation-heavy signed difference by identifying the lone uncovered-pair event and proving it has positive mass.

## value

PASS

At the first natural loss of local disjointness, even the direction of error of the prior extrapolation is not evident from its alternating terms. The revised result explains which event matters exactly: all other labels must already be covered, and both colliding labels must remain. Its positive mass proves a structural, strict underestimate without numerically resolving tiny differences. This is useful for interpreting the first collided window, distinct from copying the prior general law at one parameter. It does not estimate the numerical density, give a uniform sieve, or settle unrestricted representations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
