# Scientific review: sharp binary eventual periods for A158690

## Correctness — PASS
The claimed minimal eventual period is \(2^{r-3}\) modulo \(2^r\) for every \(r\ge4\), and the stronger exact valuation law is for all \(k\ge0\) and all even \(n\ge k+5\). The proof begins from the integral Stirling-series representation, uses a genuinely finite power-sum expansion for each modulus, and recovers \(B\equiv2\pmod4\) from the exactly evaluated coefficients \(a(6)\) and \(a(8)\). Binomial expansion of odd squares yields both the upper period and a nonzero half-period difference at every sufficiently large even index. The base cases modulo \(2\), \(4\), and \(8\) are handled separately. Independent integer-arithmetic tests cover a finite range; the proof covers the infinite range.

## Originality — PASS, with residual risks
Kallat's 2026 general theorem guarantees only \(\lambda(2^r)=2^{r-2}\) as an eventual period, not the strict half-period or its optimality. The A158690 database entry displays the isolated modulo-\(16\) period-\(2\) example but not an all-exponent law. Straub's different Fishburn coefficient congruences do not address this exponential-series least-period invariant. Targeted searches of the relevant literature, mathematical result records, and previously accessible result claims found no equivalent or dominating statement. A hidden generalization or unpublished treatment is still possible.

## Mathematical value — PASS
The existing problem is to understand eventual periodicity modulo every integer, and the available universal bound is demonstrably nonsharp at a natural modulus. The theorem determines the entire dyadic least-period hierarchy and proves sharpness by an exact infinite family of 2-adic valuations, rather than merely exhibiting one smaller period at a sample modulus. This supplies a precise arithmetic refinement of an established sequence congruence phenomenon.

## Closest literature and limitations
The closest source is A. Kallat, *A Proof of Bala's Congruence Conjectures for A158690* (arXiv:2609.07238v1, September 7, 2026), especially Proposition 2.1, Remark 2.2, and Theorem 2.6. The OEIS A158690 entry documents the low-power example. Related but noncovering material is A. Straub, *Congruences for Fishburn numbers modulo prime powers* (arXiv:1407.7521). Neither a sharp preperiod classification nor periods for odd prime powers are claimed. No independent mathematical audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
