# Independent audit — Two-prime rigidity for the multiplier-four iterate of the unitary divisor sum

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/20/iterated-unitary-sigma-multiplier-four-two-prime-rigidity--86dd6501721e`  
**Assigned and audited tree:** `543cdfde34610d73fbca07be53b733379beda2d7`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The record survives independent review without a substantive research-file edit.

## Correctness

PASS. Writing M=(2^a+1)(p^b+1)=2^sR forces the odd factor 2^s+1 to divide p^b, hence 2^s+1=p^c. If b is even then s=1 and p=3. If b is odd, LTE/parity and the factorization p^c-1=(p^{c/2}-1)(p^{c/2}+1) give the unique putative power-of-two factorization x-1=2, x+1=4, which contradicts s=v_2(p+1). For b=2, the reduction p=3 is followed by a correct split according to 5 | 2^a+1; the first case reduces to a power-of-two unitary divisor sum and a valid congruence argument forcing a=1, while the second case excludes the necessary 2-3-smooth value 5^{c+1}+1. Direct substitution confirms n=18.

## Originality

PASS, narrowly scoped. Sitaramaiah–Subbarao's 1998 work and OEIS coverage concern unitary-superperfect multiplier 2 and bounded tables that include the multiplier-4 example 18; the assigned record does not claim those data as new. Searches for sigma*^2(n)=4n, multiplier-four/unitary-superperfect terminology, and two-prime forms did not locate the infinite-range theorem p=3 with b even or the complete b=2 classification. Residual risk remains from alternate (m,k)-perfect or unitary-perfect terminology, so priority is asserted only for the stated structural slice.

## Scientific value

PASS. The record converts an isolated bounded-data observation into an infinite-range rigidity theorem for the natural two-prime-power family and completely closes the first even-exponent slice. It materially narrows any future classification of multiplier-four iterates by reducing all two-prime candidates to 2^a3^{2m} and proving uniqueness when m=1.

## Independent checks

- Re-derived the valuation reduction 2^s+1=p^c and checked every parity/LTE branch.
- Ran an independent exact-integer scan over 1<=a<=16, odd primes p<500, and 1<=b<=7; the only solution was (a,p,b,n)=(1,3,2,18).
- Checked that the current main-path tree is unchanged from the assignment snapshot.

## Literature and evidence

- https://www.math.ualberta.ca/~subbarao/documents/Sitaramaiah_Subbarao1998.pdf — Sitaramaiah and Subbarao (1998), principal earlier unitary-superperfect source and bounded computations.
- https://oeis.org/A038843 — OEIS A038843, unitary-superperfect multiplier-2 sequence and literature links.
- https://doi.org/10.3390/sym15122134 — Chehade, Miari and Alkhezi (2023), later unitary-superperfect literature context.

## Limitations

- The theorem does not classify the remaining family 2^a 3^{2m} for m>=2 and makes no claim for three or more distinct prime factors.
- The originality search may miss equivalent formulations under older (m,k)-perfect terminology.
- The bounded computation supports but does not replace the proof.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `543cdfde34610d73fbca07be53b733379beda2d7`. The publication plan changes only independent-audit materials and `VERIFICATION.md`; the Lean and expert-attestation channels are preserved exactly as `unknown` with null evidence.
