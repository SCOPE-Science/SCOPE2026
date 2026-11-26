# Independent mathematical audit

## correctness

PASS

The repeated-root formula follows by substitution and includes index zero in the form x_n=a^n(x_0+nD/a) when a is nonzero. If a=0 the quotient set is finite; if D=0 the sequence is zero or geometric, which misses an open valuation class (unit root) or an open subset of units excluding 1 (nonunit root). For aD nonzero and c=ax_0/D of negative valuation, every n+c has precisely that valuation, so v_p(x_n)=v_p(x_0)+n v_p(a); the same open-set obstructions apply. For integral c, the fixed positive lag d gives a^d+da^d/(n+c). Since positive integers shifted by c are dense in Z_p, for each target z with (da^d)/(z-a^d) a nonzero p-adic integer the ratio can approach z along positive n. If a is a unit, d=(p-1)p^j gives a^d→1 and da^d→0 by Euler's theorem, including at p=2, so every target except 1 eventually meets this condition; 1 is itself a ratio. For p|a, take d→infinity, so both terms tend to zero and every nonzero target meets the condition; zero is the limit of x_n divided by a fixed nonzero term. Denominators along the approximating subsequence can be kept nonzero since their shifted-index limit for that fixed lag is nonzero. The cited dyadic examples have c=1 and c=1/2, respectively. The replay script and recorded numeric log were inspected, not executed; those cases do not prove the all-primes statement.

## originality

PASS

Credit the established good-prime theorem and the broader simple-zero analytic theorem, which already implies density for unit a and integral shift. The supported contribution is the complete necessity-and-sufficiency decision for arbitrary data at every prime, in particular the nonunit-root branch and the nonintegral-shift obstruction. The strongest same-family indexed record classifies a different property, not ratio density.

## value

PASS

The rule completes a density question already posed for the identical recurrence, not a newly chosen test family. It decides exactly which excluded primes yield density, and the obstruction distinguishes two behaviors even when both recurrence coefficients vanish modulo the prime. The nonunit proof is not supplied by the usual analytic interpolation; the fixed-lag ratio argument explains why arbitrarily high valuations of the common exponential factor do not prevent density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
