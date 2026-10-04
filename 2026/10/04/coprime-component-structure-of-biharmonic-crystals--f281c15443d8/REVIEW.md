# Review

## Correctness
PASS. The claim is derived from the source's exact crystal criterion. For a crystal,
\(Q(a,b)\) is integral and the half-shifted components
\(x=(a+1)/2\), \(y=(b+1)/2\) satisfy \((x+y-1)^2=wxy\). A common divisor
of \(x\) and \(y\) immediately contradicts this equation, proving
\(\gcd(a+1,b+1)=2\). For \(\gcd(a,b)\), the published recurrence for all positive
integer solutions is used backwards modulo a hypothetical common divisor; it forces
the fixed initial value \(u_1=1\) to be congruent to the inverse of \(2\), which is
impossible unless the divisor is \(1\). The two-prime-support uniqueness corollary
then follows from unique prime-power allocation in a coprime factorization.

The main scientific risk is copying of the source recurrence or equivalence.
Those statements were checked in the primary full text, and the packaged checker
also validates thousands of generated instances.

## Originality
PASS. published-finding corpus searches for biharmonic crystals, component gcds, unitary
factorizations and two-prime-support uniqueness returned no result about this object.
The current ledger contains no biharmonic/crystal finding. The primary paper
classifies crystals and explicitly poses component uniqueness as a conjecture, but
does not state the two coprimality identities; full-text searches for "gcd" and
"coprime" were negative. OEIS A210494 records biharmonic integers, not component
factorizations. The closest published-finding corpus hits concern other divisor notions or unrelated
uniqueness problems and do not imply this claim.

Residual risk: a later or poorly indexed paper could have noticed the same elementary
structural consequence without using searchable terminology.

## Value
PASS. The result is not a parameter substitution or bounded census. It gives a global
structural invariant for every crystal factorization and converts arbitrary component
splits into unitary splits. This directly reduces the open uniqueness problem and
settles it for the natural first nontrivial support stratum \(\omega(N)=2\), while
showing that any counterexample must have at least three distinct prime divisors.

Same-model review: passed. Independent audit: not yet performed.
