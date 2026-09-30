# Independent audit — 2026-09-30 UTC

Record: `2026/09/21/near-f-perfect-nonexistence--1f65c1c828f1`  
Assigned and audited source tree: `507694c399b528002c2436bc9e05770469859899`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `519f72a7ff815ee408b5bc05c13e7ad3d71a3936`  
Disposition: **passed**

## Correctness

**independently_supported**. The reciprocal-divisor reduction is exact: with q=n/d, the defining equation is equivalent to sum_{e|n,e>1,e!=q} e^{-2}=3/n. Every subsequent bound uses positivity only. For odd n, parity makes tau(n) odd and n a square; two-prime squares and all but the p^2,p^4 prime-power cases are immediately too large in a surviving reciprocal term, and the two residual exact equations are impossible. For n=2m with m odd, n>12 forces q=2; two distinct odd primes contradict 2(p^2+r^2)<=3pr, while a prime-power odd part has exponent at most two and both exact equations fail. For 4|n, either 1/4 survives and n<=12 or q=2 and 1/16 survives and n<=48, leaving exactly twelve multiples of four. Independent exact scanning through n=20000 found no solution, consistent with the finite proof core.

## Originality

**qualified_supported_after_open_full_text**. The full 2025 INTEGERS paper introducing near F-perfect and [k,l]-near-perfect numbers was inspected from its lawful open PDF. It proves many factorization-specific exclusions, including prime powers, 2p^a and selected 2^a p^b cases, but its concluding remarks explicitly suggest characterizing [k,l]-near/deficient-perfect numbers with more than two prime factors as further work. It does not state global nonexistence for [2,3]. Targeted searches for the exact equation and synonymous deletion formulations found no stronger result. Because the proof is elementary, an older divisor-sum observation under unrelated terminology remains a residual risk.

## Scientific value

**meaningful_complete_existence_resolution**. The theorem closes the entire existence problem for the newly defined near F-perfect ([2,3]-near-perfect) class and replaces multiple factorization-specific exclusions by a short reciprocal-divisor mechanism that also yields useful general [2,l] bounds.

## Independent checks

- Re-derived the reciprocal-divisor identity and each parity/size reduction.
- Checked all twelve 4|n<=48 residue cases algebraically and independently scanned all n<=20000 by exact integer arithmetic with zero hits.
- Inspected the 2025 INTEGERS full text, including its specific near-F theorems and concluding remarks.
- Confirmed that the paper itself leaves more-than-two-prime-factor characterization as further work.

## Literature and evidence checked

- https://math.colgate.edu/~integers/z86/z86.pdf
- https://doi.org/10.1142/S1793042115500098
- https://arxiv.org/abs/1310.0898
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/21/near-f-perfect-nonexistence--1f65c1c828f1
## Limitations

- The theorem is specific to the [2,3]-near-perfect specialization.
- It does not settle general near F_k-perfect or [k,l]-near-perfect numbers.
- An older differently named reciprocal-divisor observation remains possible.
