# Independent audit — 2026-09-26

Record: `2026/09/09/053`. Verdict: **correctness PASS; originality PASS (restricted certificate); scientific value PASS (narrow optimization data).** Disposition: retain accepted.

## Correctness
The A entries for s^m,s^n follow directly from the simplex sum density (31)!·vol(ds)=s^31/32, giving A_mn=1/(m+n+32); the x1 block follows conditional Dirichlet moments. The displayed B entries use the squared coordinate-integral Maynard functional; the package's independent Beta-moment rebuild matches the archived 8×8 matrices. I separately parsed the exact rational matrices and coefficient vector and recomputed cᵀBc/cᵀAc=7553888936545658/2485078816758705 (≈3.03969793). An independent rational LDL factorization of (61/20)A−B produced the eight archived strictly positive pivots exactly, so every nonzero vector in the declared cell has ratio <61/20. The 32 integers are distinct, span 200, and omit at least one residue modulo every prime ≤32 (which suffices for larger primes). Maynard Proposition 4.2 indeed uses ceil(θ M/2), so the claimed cell-only thresholds follow: at θ<1/2 no M≤3.05 reaches 4, and at θ<1 no M≤3.05 reaches 4 for three primes; the explicit lower vector gives two primes only conditionally for θ>2/L≈0.658.

## Prior work and originality
Maynard, arXiv:1311.4600v3, defines the ratio and prime-count criterion; Polymath optimizes broader weight spaces. The fixed 8-dimensional k=32 Gram cell and exact two-sided rational certificate are a bounded computational addition. They do not establish an upper bound for global M_32 or the full degree-six symmetric space.

## Scientific value and limits
The certificate precisely excludes this particular restricted family from the unconditional two-prime and conditional three-prime thresholds, and gives a reproducible lower weight for stronger distribution hypotheses. The cell is small and chosen in advance; the result says nothing about better weights outside it or unconditional prime gaps.

Sources: RESULT.md and artifacts/gram_final.json, ratio_bound.json, tuple.json, verify.py; https://arxiv.org/html/1311.4600v3, Proposition 4.2; https://arxiv.org/abs/1407.4897.
