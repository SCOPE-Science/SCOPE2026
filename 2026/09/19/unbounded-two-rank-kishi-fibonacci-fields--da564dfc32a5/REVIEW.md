# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The construction is internally consistent and uses four standard inputs in a compatible way.

First, Carmichael's theorem supplies a primitive prime divisor of each chosen Fibonacci number F_(25 r_i), because 25 r_i > 12. Primitive divisors attached to distinct indices are distinct, and none can be 2 or 5. Second, because the rank of apparition of q_i is exactly 25 r_i, every chosen index n=25 U_R Q is a multiple of z(q_i). Lengyel's valuation formula then makes v_(q_i)(F_n) an affine function of v_(q_i)(n), so multiplying U_R by q_i zero or one extra time independently fixes the desired odd parity. The separate formula v_5(F_n)=v_5(n) makes 5 survive as an additional odd-exponent factor.

Third, the squarefree part therefore contains at least R+1 distinct odd primes. Gauss genus theory gives 2-rank at least R for the imaginary quadratic class group, hence 2^R divides its class number. Kishi's universal factor 5 is coprime to 2^R, producing 5*2^R divisibility.

Fourth, the infinitude argument was checked for the two possible parity subtleties at p=2 and p=5. Under a hypothetical finite set of fields, the Fibonacci gcd identity forces every prime in a sufficiently late squarefree part back into F_m. Lengyel's formula (and its explicit p=2,5 cases) then fixes all valuation parities, so the squarefree part becomes constant. The Fibonacci--Lucas identity places infinitely many strictly increasing Lucas values on one nonsingular quartic Y^2=5D^2X^4-4, contradicting Siegel finiteness.

Potential hidden-hypothesis checks included: U_R is odd, so s=(U_R Q-1)/2 is an integer; v_5(U_R)=1; each 25 r_i divides 25 U_R Q; variable Q is excluded from the finite set of fixed primes; the quadratic field depends only on the squarefree part; and the fundamental discriminant retains all odd primes exhibited in that squarefree part.

## Originality

**PASS, to the best of our knowledge.** The recent Chakraborty--Rao--Dabhole preprint was inspected at the theorem statements, Fibonacci valuation proposition, proof of its 10-divisibility theorem, and proof of its infinitude theorem. It gives a two-prime squarefree-kernel argument (5 and 3001) yielding one genus-theoretic factor of 2, not an arbitrary-rank construction. Its infinitude proof treats a different restricted family and does not state unbounded 2-rank in Kishi's family.

Searches were made around the exact family Q(sqrt(-F_(50s+25))) and synonymous formulations involving unbounded 2-rank, powers of 2 in class numbers, squarefree parts of Fibonacci values, primitive divisors, and genus theory. No prior theorem matching the arbitrary-R statement was found. General theorems constructing quadratic fields with prescribed class-number divisibility do not by themselves imply the result inside this fixed Fibonacci-parametrized family.

The most important access limitation is Yasuhiro Kishi's 2008 J. Number Theory paper (DOI 10.1016/j.jnt.2008.02.016). Its abstract was inspected, and its principal family theorem and infinitude argument are explicitly restated and used in the 2026 preprint, but the complete 2008 text was not inspected. Because it studies exactly this Fibonacci family, it is the source most plausibly capable of containing an unadvertised stronger 2-rank observation. Nothing in the accessible abstract, citation descriptions, or the 2026 paper's account indicates such a result, so this is residual rather than concrete evidence of prior coverage.

The primitive-divisor theorem itself is classical (Carmichael; a modern simple proof is Yabuta 2001), Lengyel's valuation formulas are classical, and Gauss genus theory is classical. Originality is claimed only for their use to obtain the stated infinite arbitrary-2-rank subfamilies of Kishi fields.

## Value

**PASS.** The recent theorem improves Kishi's factor 5 to a factor 10 on a valuation-defined subfamily. The present result shows that this is the first level of an unbounded phenomenon: every prescribed 2-rank occurs as a lower bound on an infinite subfamily, while the original factor 5 persists. It also supplies an explicit constructive recipe for the subfamily and a proof that the construction produces infinitely many distinct fields rather than repeated parametrizations.

## Scope and limitations

The result does not determine the full 2-primary class group, does not produce elements of exact order 2^R, and gives no density or optimized size for U_R. The motivating preprint is very recent, so unindexed contemporaneous work remains a residual originality risk. No independent validation or formal proof-assistant verification is asserted.
