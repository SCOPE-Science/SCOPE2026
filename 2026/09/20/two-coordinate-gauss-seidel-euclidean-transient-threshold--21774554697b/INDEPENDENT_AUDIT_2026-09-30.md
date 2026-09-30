# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/two-coordinate-gauss-seidel-euclidean-transient-threshold--21774554697b`  
Assigned and audited source tree: `dccf43e1a16465bd1b9bb02dd821de8a2c2d714a`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `c533cc67393097d37117a9afd2b0ac63fd0e8b99`  
Disposition: **passed**

## Correctness

**independently_supported**. The two-coordinate Gauss-Seidel formulas and minimax threshold are correct. Exact coordinate minimization gives T_12=[[0,-c/a],[0,q]] and T_21=[[q,0],[-c/d,0]], q=c^2/(ad); since each has one nonzero column, the displayed Euclidean operator norms follow and larger-diagonal-first is the better static order. For fixed eigenvalues lambda<=Lambda, |c|<= (Lambda-lambda)/2, max(a,d)>=(Lambda+lambda)/2 and q=c^2/(Lambda*lambda+c^2)<=delta^2, delta=(Lambda-lambda)/(Lambda+lambda). These two bounds are attained simultaneously by the balanced-diagonal matrix, proving the exact minimax value delta*sqrt(1+delta^2). Solving delta^2+delta^4<=1 gives the stated kappa threshold, equivalently 2+sqrt(5)+2sqrt(2+sqrt(5))=8.352410032... and the displayed reciprocal quartic. Direct multiplication gives T^2=qT, so every fixed-order Euclidean ordering effect after the first sweep is exhausted by the startup transient.

## Originality

**qualified_supported_elementary_special_case**. Ordering effects in SOR/Gauss-Seidel and cyclic coordinate descent are classical. Varga's ordering work and Oswald-Zhou's random-reordering theory concern spectral/asymptotic or randomized behavior, while later coordinate-descent work studies broader worst cases. Targeted searches did not locate the exact 2x2 Euclidean one-sweep minimax, the larger-diagonal-first rule in this operator-norm form, the factor delta*sqrt(1+delta^2), or the condition-number threshold 8.352410032.... The contribution is therefore credible as a sharp elementary finite-dimensional transient calculation, not as a new general ordering theory. Because an equivalent 2x2 exercise could exist in older monographs under different terminology, prior-art risk remains material.

## Scientific value

**meaningful_sharp_transient_model**. The theorem cleanly separates asymptotic convergence from nonnormal Euclidean startup amplification, gives a closed optimal order and exact condition-number boundary, and supplies a family where the wrong order grows like sqrt(kappa) while the good order stays bounded. Its value is conceptual and exact rather than broad in dimension.

## Independent checks

- Re-derived both sweep matrices directly from the coordinate minimizers and their exact singular norms.
- Verified that the balanced-diagonal matrix simultaneously saturates the coupling and q bounds.
- Solved the nonexpansion inequality independently and recovered kappa*=8.35241003204277 and the quartic.
- Checked T_pi^2=q T_pi and the unbounded bad-order family with eigenvalues exactly 1 and kappa.

## Literature and evidence checked

- https://doi.org/10.2140/pjm.1959.9.925
- https://doi.org/10.1007/s10107-015-0892-3
- https://doi.org/10.1007/s00211-016-0829-7
- https://doi.org/10.1093/imanum/dry040
- https://www.math.ualberta.ca/ijnam/Volume-17-2020/No-4-20/2020-04-06.pdf
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/two-coordinate-gauss-seidel-euclidean-transient-threshold--21774554697b

## Limitations

- Only real two-dimensional SPD systems and exact point Gauss-Seidel are covered.
- The norm is Euclidean error, not the classical SPD energy norm.
- No higher-dimensional ordering rule or finite-precision result is implied.
- The theorem is elementary enough that differently indexed textbook or exercise-level prior art remains a real originality risk.
