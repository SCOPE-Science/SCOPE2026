# Review: A forty-term obstruction for distinct semiprime Egyptian fractions

## Correctness — PASS

The assumption of an **integer** sum forces each prime-local residue to vanish when all denominators are included. A nonzero residue among head denominators must be repaired by a tail denominator incident with that prime; since each semiprime has two prime factors, at most twice the number of tail terms require repair. The weighted dual exactly compensates the uniform tail bound. The finite computation checks the entire prime-pair head up to \(2000\) using an integer-only residue dynamic program with proved outward rounding. The exact upper rational \(7767730087/7812500000\) is less than one, so the contradiction is rigorous and independent of solver tolerances. A known \(48\)-term representation validates the local residue criterion on a genuine positive example.

## Originality — PASS

The closest same-invariant paper is Watanabe, arXiv:2009.03275v2; it presents \(47\)-term representations and **conjectures**, without proving, that they are minimal. Its constructive search begins with prime factors at most \(53\), and its Section 4.1 rules out exactly \(46\)-term examples when every prime factor is at most \(101\); neither result covers arbitrary primes. Li, arXiv:2606.15159v2, proves universal existence but no short-rank lower bound. The separate published bound for fixed two-prime support \(\{2,p\}\) does not cover arbitrary distinct semiprimes. Searches of exact formulation, aliases, near-neighbor statements and prior current claims found no equivalent unrestricted \(r\ge41\) proof. A later same-object paper on rational existence was accessible only at abstract level; that material does not assert this lower bound and remains a documented access risk.

## Value — PASS

This is a motivated quantitative step toward Watanabe's explicit conjecture that the true minimum is \(47\). The elementary reciprocal-sum obstruction gives only \(38\), so the new lower bound \(41\) eliminates three additional candidate ranks. More importantly, the proof combines a global prime-local congruence with a tail-independent finite dual, addressing the genuine challenge that a search restricted to small prime factors cannot rule out arbitrary large primes. No exact-rank classification is claimed.

## Limitations

The exact value of \(r\) remains unknown in the interval \(41\) through \(47\). The proof does not establish the conjectural upper endpoint as minimal, and its numerical certificate applies only to the particular exact dual, not to a full unrestricted enumeration of representations.

Self-review: passed. Independent audit: not yet performed.
