# Independent audit — 2026-09-29

Record: `2026/09/19/exact-largest-gegenbauer-cbf-thresholds-degrees-four-five--08c02c582cdc`  
Assigned and audited source tree: `1ee99b17186113461b13fd4fc4b04b522ad0e495`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `348299a6998f57ffa02bab2fc51e55bfefed443a`  
Disposition: **passed**

## Correctness

**independently_supported**. The degree-four and degree-five algebra, Pick-function argument, and endpoint measures check. Independent symbolic factorization reproduces the displayed C_4^lambda and C_5^lambda quartics and their largest-zero formulas. After s=lambda+1/2, each F^2 factors as A(s)B_d(s), where A is a positive affine combination of a square root of a complete Bernstein Möbius map and B_d=(s+c)/(s+b). For 0≤c≤b, closure under powers/geometric means gives the claimed sufficiency. If c>b, choosing x in (-c,-b) makes B approach the negative real axis from below while A approaches a positive value from above, so the positive-axis square-root branch has negative imaginary part and fails the Pick criterion. At d=3 and d=4, independent numerical Stieltjes integration of the stated rho_4 and rho_5 densities at s=0.1,1,10 agrees with the closed forms to about 10^-17, corroborating the inversion formulas.

## Originality

**qualified_low_degree_sharpening**. Castillo's September 2026 preprint publicly proves broad complete-Bernstein results for scaled ultraspherical zeros, including a general largest-zero scale, but the public record does not advertise exact optimal largest-zero thresholds in degrees four and five. Targeted searches by the explicit degree formulas, candidate endpoints, and Pick/complete-Bernstein terminology found no equivalent d_max=3 and d_max=4 theorem or the displayed compact endpoint measures. The contribution is therefore supported as an elementary but exact low-degree sharpening of a very recent source, with substantial concurrency risk.

## Scientific value

**meaningful_exact_threshold_result**. The result determines the first two unresolved optimal largest-zero scale intervals and shows the previously sufficient ranges are not sharp. The explicit endpoint representing measures also explain the sharp boundary analytically. It does not establish the apparent d_max=n-1 pattern beyond n=5.

## Literature and evidence checked

- https://arxiv.org/abs/2609.19186
- https://doi.org/10.1515/9783110269338

## Limitations

- Only degrees four and five are settled.
- The source preprint is extremely recent, so parallel low-degree calculations may be unindexed.
- No general optimal threshold for n≥6 is proved.
- The originality assessment rests on targeted current searches plus the public source statement; no priority claim is made beyond these explicit low-degree formulas.
