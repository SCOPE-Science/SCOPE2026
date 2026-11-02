# Review of ternary-power Catalan residue coverage

## Correctness — PASS

The theorem quantifies over every integer \(k\ge1\), every class modulo \(3^k\), and infinitely many Catalan indices. The finite factorial-unit identity follows recursively by stripping multiples of three from factorials. Sparse base-three digits, separated by at least \(k+2\) positions, give independent length-\(k\) windows in both \(n\) and \(2n\), and their carry counts exactly recover the power \(3^v\). The remaining Catalan denominator is congruent to one. The central binomial coefficient \(\binom{2\cdot3^{k+2}}{3^{k+2}}\equiv2\pmod9\), yielding a generator of units modulo every \(3^k\) by the standard lifting-the-exponent argument. These steps prove explicit congruences for arbitrary \(k,v,t\), not just tested parameters.

The supplied standard-library verifier independently evaluates factorial units and direct Catalan integers, and checks hundreds of sparse-block combinations and complete residue coverage for small powers. Its tests do not replace the unbounded proof.

## Originality — PASS, with historical-priority qualification

The direct source question is Rowland–Yassawi (2013), Open question 3.6, which asks whether Catalan numbers omit a residue modulo any \(3^\alpha\). The theorem gives a uniform negative answer with explicit infinitely repeated witnesses. Krattenthaler–Müller (2013) treat generating functions modulo fixed powers of three, especially \(9\) and \(27\); Chen–Jiang (2013) prove stabilization for sparse sequences of the form \(C_{p^j-a}\) rather than coverage by the full sequence. Deutsch–Sagan (2006) treat reduction modulo three; Burns (2017) proves coverage modulo primes \(p\ge5\), not prime powers. These are statement-and-implication distinctions, not merely differences in wording. No inspected theorem gives the present all-level constructive surjectivity. Specialist literature not identified by the searches could nonetheless overlap.

## Mathematical value — PASS

Resolving a plainly stated open question for every power of three is a natural and useful arithmetic result. The sparse-digit factorization gives explicit witness indices for all \(3\)-adic target neighborhoods and all valuations, not just a finite set of numerical observations. This provides an algebraic mechanism for surjectivity even though the occurrence density of nonzero residue classes can be zero.

## Closest literature and limitations

Rowland–Yassawi, arXiv:1310.8635, Open question 3.6; Krattenthaler–Müller, arXiv:1308.2856, Section 12; Chen–Jiang, *Integers* 13 (2013) #A36, Theorem 1; Deutsch–Sagan, *J. Number Theory* 117 (2006), Theorem 5.2; Burns, arXiv:1703.02705. Priority claims are bounded by actual available comparisons. The result does not quantify the first occurrence, prove positive frequency, or address other primes.

Self-review: passed. Independent audit: not yet performed.
