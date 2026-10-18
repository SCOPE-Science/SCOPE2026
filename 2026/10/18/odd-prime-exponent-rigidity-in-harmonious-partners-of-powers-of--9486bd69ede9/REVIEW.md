# Scientific review: Odd-prime exponent rigidity in harmonious partners of powers of two

## Correctness — PASS

The theorem quantifies over every positive exponent triple and every odd prime. The necessary direction has three logically exhaustive stages. For exponent \(k=1\), the second reciprocal-divisor-sum term is strictly greater than \(1/3\). For \(k\geq2\), denominator clearing forces \(2^k-1\mid p^s\); the elementary parity/factorization argument rules out proper odd-prime powers, hence \(2^k-1=p\). The residual equation reduces to \(2p+1=t(p^{s-1}+2\sum_{i=0}^{s-2}p^i)\), whose integer squeeze excludes all \(s\geq2\). The remaining \(s=1\) forces \(r=k\). Direct substitution proves sufficiency. The finite exact checker evaluated 256,512 independently computed cases and found four matching cases; 576 additional direct-divisor-sum enumerations corroborated the same classification. The general proof does not depend on those checks.

## Originality — PASS, with residual uncertainty

The primary 2015 paper of Kozek–Luca–Pollack–Pomerance gives the defining identity and general sparsity and discordance results, but not this odd-prime-power exponent exclusion. A publicly indexed exact finding titled *Powers of two in two-prime-support harmonious pairs* **already settles** the subfamily with the odd prime occurring once. Therefore the classification restricted to \(s=1\) is prior work, not a contribution here. The scientifically new part is the unconditional proof that no harmonious pair in the full two-prime-support family exists with \(s\geq2\); this rules out infinitely many additional exponent layers and is not a logical consequence of a theorem whose quantified domain fixes \(s=1\). Bishop et al. (2021) prove general recognition criteria and give examples but do not state this exclusion. Exact higher-exponent, alternate-name, and stronger-coverage searches did not identify an equivalent statement. No claim of exhaustive literature coverage is made; the closest indexed finding was accessible as a summary, not as a complete manuscript, and an unindexed general theorem remains possible.

## Value — PASS

The underlying problem is the established divisor-sum recognition problem for harmonious pairs. Holding one member at a prime power of two and limiting the other to exactly two prime supports is a natural minimal arithmetic-complexity stratum. Previous classifications treated only squarefree odd parts. The theorem completes the entire exponent dimension instead of incrementing a numerical bound: repeated odd-prime factors are intrinsically impossible, and precisely the Mersenne-prime family survives. This is a structural boundary rather than a normalization identity or a finite table computation. The proof uses a nontrivial interaction of denominator divisibility, perfect-power rigidity and an integer-factor squeeze. It is not claimed to solve the unrestricted harmonious-partner problem or the infinitude of Mersenne primes.

## Closest literature and limitations

- Kozek, Luca, Pollack, Pomerance, *Harmonious pairs*, Int. J. Number Theory 11 (2015), 1633–1651; author's 20-page paper inspected, including definitions, results, proof methods, discordance and examples. https://www.pollack-math.net/harmonious5.pdf
- *Powers of two in two-prime-support harmonious pairs*, indexed mathematical result `2026/10/4/SCOPE-powers-of-two-in-two-prime-support-harmonious-pairs--94f9b7228e53`; mathematical summary inspected, covering exactly the odd-prime-exponent-one case, but full manuscript not available through the result retrieval.
- Bishop et al., *The Abundancy Index and Feebly Amicable Numbers*, arXiv:2104.11366; 9-page preprint inspected, with alias “feebly amicable.” https://arxiv.org/pdf/2104.11366

An unseen earlier classification of all \(2^k\)-partners with prime-power odd part would dominate this theorem. The calculation is not an independent audit.

Self-review: passed. Independent audit: not yet performed.
