# Independent Audit — 2026/09/17/hadamard-densification-kusner-critical-scaling--43b27c183a43

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `81777875ab2e8d1bcbb5541ea18ac2c12a5b8db1`
- Disposition: **PASSED**

## Correctness

**PASS** — The arbitrary-Hadamard substitution preserves every distance count used in Xiong's construction. After normalizing one column of an order-m Hadamard matrix, distinct rows agree/differ in m/2 positions, and in H_4 tensor H the four distinguished columns behave exactly as in the Sylvester case. Hence the same scalar equation Phi_p(a)=1+1/m is sufficient. Independently, the p=4 identity Phi_4(a)-1=-3(a^2-2)^2/[4(a^4+2)] has its unique maximum at a=sqrt(2), and differentiating in p gives c=sqrt(2)log(1+sqrt(2))-(7/4)log 2=0.0334429143005567..., so 8/c=239.213602262732.... Using Paley orders and primes in the progression 3 mod 4 supplies Hadamard orders m=(1+o(1))/Delta(p), which yields the stated O((p-4)^-1) dimension bound.

## Originality

**PASS** — Xiong's 2026 source constructs the p>4 counterexamples with a sufficiently large power-of-two order; Swanepoel-Villa use arbitrary Hadamard orders and density in a different p<2 maximal-equilateral-set problem. Targeted searches found no pre-existing extension of Xiong's new p>4 construction to arbitrary Hadamard orders or the resulting leading constant 8/c. Repository chronology also matters: this record's first public commit was 2026-09-17 14:31:30 UTC, before the overlapping refinement record committed at 17:00:42 UTC the same day.

## Scientific value

**PASS** — The result turns Xiong's qualitative near-threshold construction into a quantitative critical scaling law with an explicit leading constant and removes an avoidable factor-of-two loss from dyadic rounding. It also identifies the precise stationary endpoint controlling the p downarrow 4 singularity, making the construction easier to compare with lower bounds and with future improvements in Hadamard-order availability.

## Sources

- Kusner's conjecture is false for p>4 (Nathan Xiong): https://arxiv.org/abs/2609.14794 — Source p>4 construction; its abstract states 8m equilateral points in dimension 8m-2 for an m depending on p.
- Maximal Equilateral Sets (Konrad J. Swanepoel; Rafael Villa): https://doi.org/10.1007/s00454-013-9523-z — Earlier arbitrary-Hadamard/density technique in a different p<2 maximal-equilateral-set construction.
- Equilateral Sets and a Schütte Theorem for the 4-norm (Konrad J. Swanepoel): https://doi.org/10.4153/CMB-2013-031-0 — Background quantitative stability near p=4.

## Limitations

- The result is an upper-bound refinement of Xiong's construction, not a determination of the true first-failure dimension.
- Originality is narrow: arbitrary Hadamard densification itself is old; the new point is compatibility with Xiong's p>4 template and its critical constant.
- The availability of Hadamard orders is used asymptotically through Paley/PNT rather than an all-orders Hadamard conjecture.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first. Oxford Download was not needed for this record.
