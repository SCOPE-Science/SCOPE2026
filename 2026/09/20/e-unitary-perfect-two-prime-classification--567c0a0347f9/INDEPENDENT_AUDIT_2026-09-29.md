# Independent audit — Two-prime classification of exponential unitary perfect numbers

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Source path:** `2026/09/20/e-unitary-perfect-two-prime-classification--567c0a0347f9`  
**Assigned and audited tree:** `1a21ae5073a0254d168a0c1b6d72a333ce3888b5`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The claim survives independent review without a substantive research-file edit.

## Correctness

PASS. Using the published fact that no odd e-unitary perfect number exists, write n=2^a q^b. Dividing the perfectness equation by 2q gives AB=2^a q^(b-1), where A=σ^{(e)*}(2^a)/2 is odd and B=σ^{(e)*}(q^b)/q is 1 mod q. Unique prime support therefore forces A=q^(b-1) and B=2^a. Normalizing gives S_a R_b=2. Since every proper unitary divisor of b is at most b-1, R_b<1+1/(q-1)≤3/2, so S_a>4/3. Bounding proper unitary divisors of a by floor(a/2) rules out all odd a and all even a≥6, leaving a=2 or 4. These yield respectively n=36 and a contradiction. An independent brute-force search over two distinct primes below 100 and exponents 1,…,9 finds only 36.

## Originality

PASS with an older-terminology caveat. Minculete–Tóth (2011) develop exponential unitary divisors, prove the odd-number exclusion, and discuss known examples/open questions. The older two-prime theorem located in the literature is for e-perfect numbers, a logically different notion because whether every e-unitary perfect number is e-perfect remains open. Targeted searches for the exact e-unitary two-prime classification and current OEIS data did not locate a prior theorem, and no obvious SCOPE duplicate was found. An older statement under variant terminology remains residual risk.

## Scientific value

PASS. The theorem gives the minimal-support classification for e-unitary perfect numbers and strengthens the open-problem landscape by proving that any e-unitary-perfect but non-e-perfect counterexample must involve at least three distinct primes.

## Independent checks

- Reconstructed the parity/congruence factor split A=q^(b-1), B=2^a and the normalized product S_aR_b=2.
- Rechecked the geometric-series bounds that reduce a to 2 or 4 and the two terminal cases.
- Brute-force searched all pairs of distinct primes below 100 with exponents 1,…,9 using exact unitary-divisor sums; the only solution is 2^2·3^2=36.
- Checked current main-path tree identity against the assignment snapshot.

## Literature and evidence

- https://doi.org/10.71352/ac.35.205 — Minculete and Tóth (2011), systematic source on exponential unitary divisors and the no-odd-e-unitary-perfect theorem.
- https://ac.inf.elte.hu/Vol_035_2011/doi/205_35.pdf — Lawful open-access full text used to inspect the e-unitary-perfect section and Theorem 6.
- https://oeis.org/A391281 — Current primitive e-unitary perfect sequence; lists 36 first and records known-example context.
- https://link.springer.com/book/10.1007/1-4020-2547-9 — Standard handbook source summarizing the distinct older two-prime classification for e-perfect numbers.

## Limitations

- The result classifies only support size one/two and does not classify e-unitary perfect integers with three or more distinct prime factors.
- It does not resolve whether every e-unitary perfect number is e-perfect.
- Originality is bounded by accessible/indexed literature; older work under variant terminology remains the main priority uncertainty.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `1a21ae5073a0254d168a0c1b6d72a333ce3888b5`. This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels remain byte-for-byte semantically identical to the pre-audit file.
