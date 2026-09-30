# Independent audit — 2026-09-29

Record: `2026/09/17/fifth-power-reciprocal-fibonacci-floor--e607dd8db2c7`  
Assigned and audited source tree: `7ed8891e6682d6c7588ddcfa114cfb1de5318958`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_reproduced**. The explicit floor formula was independently checked with exact Fibonacci/Lucas arithmetic and high-precision tail summation for n=4 through 30, with complete agreement. The modular obstruction also checks: 4F_n-3F_{n-1} mod 19 repeats the nonzero block [4,1,5,6,11,17,9,7,16], so the rational approximant cannot be integral. Direct modular iteration reproduces the claimed 3654 period of A_n mod 31958. The analytic tail step is consistent: the record obtains |S_n^{-1}-G_n|<10 alpha^{-n}, and alpha^27>10*31958 puts the error below one denominator spacing for n>=27; the remaining finite range is covered by a rigorous rational tail majorant.

## Originality

**supported_narrow**. The closest current exact-floor paper located treats the cubic tail, while the general Wan-Liang-Liao framework supplies arbitrary-exponent asymptotics rather than this d=5 floor identity. Searches did not locate a prior exact fifth-power formula of the stated form. The originality claim is therefore accepted narrowly for this exact exponent-5 floor determination, not for Binet-series asymptotics.

## Scientific value

**useful_exact_number_theory_result**. The theorem extends the small-power reciprocal-Fibonacci floor literature to the first stated higher-power case with a fully explicit modular correction and finite certificate. It is specialized, but the exact all-n>=4 identity is mathematically stronger than a numerical or asymptotic observation.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/17/fifth-power-reciprocal-fibonacci-floor--e607dd8db2c7
- https://arxiv.org/abs/2609.18179
- https://arxiv.org/abs/2510.13472
- https://doi.org/10.1515/math-2022-0525
- https://doi.org/10.3934/era.2025020

## Limitations

- The result is for the ordinary Fibonacci sequence and exponent 5; no all-higher-powers theorem is established.
- The originality search cannot exclude unpublished or very recent contemporaneous work.
- The general asymptotic method is prior art and is not credited as part of the new contribution.
