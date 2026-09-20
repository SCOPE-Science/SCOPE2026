# Review — prime-square local rigidity for the Lebesgue–Nagell equation

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The argument has a short analytic reduction and a finite exact check.
Modulo p, the Thue form reduces to the affine line
\(a+(2/p)b=1\). Every first partial derivative of the homogeneous Thue form is
divisible by p, so its value modulo \(p^2\) is constant on each residue class
modulo p. Hence testing the p points on that affine line is exhaustive for the
prime-square obstruction.

The finite check is performed by two exact formulas: direct evaluation of the
Thue polynomial and exponentiation in \((\mathbb Z/p^2\mathbb Z)[\sqrt2]\). The
program requires exact agreement between the two evaluations for every tested
pair and verifies that exactly the stated 31 primes have the unique compatible
class \((1,0)\).

For the passage back to the original Diophantine equation, the hypotheses of the
cited Katz–Pratt results match the stated exponent range. Their Theorem 5.3 gives
\(r=\pm1\), Section 3 normalizes to \(r=1\) after a possible sign change of x,
and Theorem 7.7 converts \(b\equiv0\pmod p\) to
\(x\equiv1\pmod p\) in the normalized sign. The original equation then gives
\(y\equiv-1\pmod p\), and their Theorem 2.3 upgrades x to
\(x\equiv\pm1\pmod{p^2}\).

## Originality

**PASS, to the best of our knowledge.** The 2020 survey of Le–Soydan records the
underlying \(x^2-2=y^n\) problem among unresolved Lebesgue–Nagell equations.
Katz–Pratt (current arXiv revision dated 5 September 2026, also published in The
Ramanujan Journal) reduce the remaining prime-exponent problem to 84 cases and
state Conjecture 8.1 asserting local triviality. Their Proposition 8.2 proves only
that x and y are nonzero modulo p. Their Theorem 10.1 counts Thue solutions modulo
prime powers in most cases but, when the local prime equals the exponent and the
power exceeds one, leaves an unspecified positive factor.

Searches by the original equation, the local-triviality formulation, the stronger
\(x\equiv\pm1\pmod{p^2}\) conclusion, the modulo-\(p^2\) Thue formulation, and the
relevant source titles did not locate a result establishing this 31-prime list or
the prime-square rigidity criterion. The current SCOPE archive was also checked
for the mathematical object, claim family, and synonymous formulations; an older
failed record for a different Lebesgue–Nagell parameter family is unrelated.

The principal residual originality risk is recency: Katz–Pratt's relevant version
was revised in September 2026, so very recent follow-up work may not yet be fully
indexed. No inaccessible source was identified whose available statement closely
suggests that it already proves the present claim.

## Value

**PASS.** Katz–Pratt explicitly isolate local triviality as a weaker conjecture
that already appears difficult. The present result proves that conjecture for 31
of the 84 prime exponents left by the known global reductions and obtains the
stronger congruence \(x\equiv\pm1\pmod{p^2}\). The reduction is reusable: for any
further exponent in the same Thue family, local triviality follows whenever the
single affine line modulo p has only the trivial class compatible modulo \(p^2\).

## Scientific limitations

The result does not exclude nontrivial global integer solutions for the 31 primes.
For the remaining 53 residual primes, multiple classes pass the \(p^2\) test, so a
stronger modulus or additional arithmetic input is required. The enumeration is
computer-assisted, though exact and independently cross-checked by two arithmetic
evaluations in the supplied verification program. No formal proof-assistant
verification is claimed.
