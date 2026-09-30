# Independent audit — 2026-09-29

Record: `2026/09/19/almost-bcd-banach-mazur-tangent-rigidity--2a7315b9e68f`  
Assigned and audited source tree: `831b8439f6a0f5d27264c38692214f25cbd5a7d9`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `4491a31be7852d3b32116b655efda872c5fdcd55`  
Disposition: **passed**

## Correctness

**independently_supported**. The quantitative transfer is correct. Han-Liu's Theorem B gives p_par(T_x^*X)<=8 sqrt(delta) under the stated local doubling and weak (1,1)-Poincare assumptions. If R is the von Neumann-Jordan ratio, the maximum in p_par is at most its denominator, giving R<=1+p_par; applying the same inequality after (p,q)->(p+q,p-q) gives 1/R<=1+p_par, hence C_NJ<=1+8 sqrt(delta). Passer's Theorems 1.2/3.4 give K_k(epsilon)=1+(18k^2-17k+14)epsilon+O_k(epsilon^2), and his two-dimensional theorem gives exactly sqrt((1+15epsilon+13.5epsilon^2)/(1-15epsilon-13.5epsilon^2)); substituting epsilon=8 sqrt(delta) reproduces the record. The lower lemma p_par(E)<=4(d_BM(E,l2)^2-1) follows directly from an almost-optimal Euclidean comparison norm and the exact Euclidean parallelogram identity. Han-Liu's perturbative lower parallelogram defect and Theorem 4.11, which gives Delta_BCD(F_tau) asymptotic to a positive constant times tau^2 for nonquadratic perturbations, then force d_BM-1 of order |tau| and prove the square-root exponent sharp.

## Originality

**qualified_synthesis**. Han-Liu supply the almost-BCD parallelogram estimate and the quadratic entropy scale; Passer supplies the finite-dimensional quantitative Jordan-von Neumann theorem. Neither inspected source states the combined BCD-to-Banach-Mazur cotangent estimate or its sharp entropy exponent. The result is therefore a useful new synthesis/corollary rather than an independent new rigidity mechanism.

## Scientific value

**meaningful_quantitative_translation**. Banach-Mazur distance gives a standard affine-geometric interpretation of almost-Riemannian cotangent fibers, and the perturbation examples show the square-root loss is intrinsic. The statement is useful especially because it includes an explicit two-dimensional bound, while remaining strictly fiberwise.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/almost-bcd-banach-mazur-tangent-rigidity--2a7315b9e68f
- https://arxiv.org/abs/2609.19564
- https://arxiv.org/abs/1305.3546
- https://doi.org/10.1007/s00010-013-0193-y
## Limitations

- The constants and smallness threshold depend on the finite fiber dimension.
- The conclusion is almost-everywhere and infinitesimal, not a global metric-measure closeness theorem.
- No optimal Banach-Mazur constant or dimension-free infinite-dimensional analogue is established.
- Most of the proof is a direct composition of two prior quantitative theorems, and the BCD source is only weeks old.
