# Scientific review: Complete prime-power congruence law for digit reversal

## Correctness — PASS

The statement quantifies over all fixed integer bases \(b\ge2\), primes \(p\), exponents \(a\ge1\), and exact digit lengths \(\ell\). For \(p\nmid b\), the normalized reversal is a sum of independent digit steps \((b^j,b^{-j})\); the first two vectors generate precisely the claimed congruence subgroup because their determinant has \(p\)-valuation \(\nu_p(b^2-1)\). Finite Fourier convergence holds since each cyclic generator recurs and the digit distribution includes zero and one. For \(p\mid b\), nonoverlapping leading and trailing digit blocks are independent at the claimed cutoff, giving the exact finite-length formula. Subtraction of successive prime-power tails gives the valuation law. Twelve exact modular-image tests, ten brute-force divisibility comparisons, and four modular-dynamic-program convergence tests passed; none substitute for the proof of convergence at unbounded length.

## Originality — PASS, with residual risk

OEIS A055483 already defines and tabulates the decimal gcd of a number and its digit reversal (original entry dated 2000-06-27); OEIS A161825 tabulates its binary counterpart. The OEIS entry also records the decimal \(3\)- and \(9\)-divisibility implications. Neither checked entry provides the all-base, all-prime-power limiting distribution, subgroup classification, or sharp stabilization at primes dividing the base. Banks, Hart, and Sakata (2004) study *palindromic* integers in residue classes; the present theorem counts joint congruences of unrestricted integers and their reversals. Dartyge and colleagues (2023), in their analysis of reversible primes and squarefree pairs, cover some local squarefree factors in base two, including the \(3^2\) correlation reflected in their \(22/27\) factor. Their stated results do not dominate the complete prime-power and arbitrary-base theorem. A hidden earlier proof or an unstated consequence of the later Fourier estimates remains possible, so novelty is not independently certified.

## Mathematical value — PASS

The invariant \(\gcd(n,R_b(n))\) is explicitly cataloged, and joint divisibility is important in arithmetic sieve questions about digit reversal. A complete law reveals non-independent prime-power events exactly at the exceptional primes dividing \(b^2-1\), with a provably sharp transition between \(p^{-1}\) and \(p^{-2}\) valuation ratios. Primes dividing the base obey a different finite-length exact law. These are natural structural divisions, not an arbitrary numerical slice or a recurrence copied from an existing table. The theorem deliberately does not claim a global density for coprime reversal pairs.

## Primary sources and limits

- OEIS A055483, https://oeis.org/A055483, table and formula/comment sections, original entry 2000-06-27.
- OEIS A161825, https://oeis.org/A161825, binary gcd sequence and description, original entry 2009-06-20.
- Banks, Hart, and Sakata, *Almost All Palindromes Are Composite*, arXiv:math/0405056v1, 2004; PDF introduction and principal theorem statements compared.
- Dartyge, Martin, Rivat, Shparlinski, and Swaenepoel, *Reversible primes*, arXiv:2309.11380v1, 2023; Sections 1.2–1.3, Theorem 1.4, Section 5 and squarefree-modulus lemma compared.

Self-review: passed. Independent audit: not yet performed.
