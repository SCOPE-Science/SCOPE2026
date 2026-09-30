# Independent audit — 2026-09-28

Record: `2026/09/10/024`  
Audited tree: `eba257d5c05021cfa3708543997c84d458251f53`  
Disposition: **passed**

## Correctness
I independently reconstructed the normalized adjacency spectra. For the contracted 7-vertex graph, the characteristic polynomial of `12P` is
`(y-12)(y-4)(y+4)(y^2+4y-16)(y^2+8y-16)`, so its second random-walk eigenvalue is `1/3`. The cube also has second eigenvalue `1/3`. The standard equilateral quantum-graph reduction therefore gives first positive wavenumbers `12 arccos(1/3)` and `11 arccos(1/3)`, respectively; the vertex-vanishing branch starts later at `pi/ell`. The stated strict inequality is correct.

## Originality
Band–Lévy and earlier equilateral spectral results provide the method and optimization context. I did not locate this exact two-point cube/contraction comparison in prior literature. Its originality, if any, is therefore in the explicit finite calculation rather than the spectral reduction.

## Scientific value
The result is a valid boundary-center benchmark and can serve as one stratum check. It is narrow: it does not compare non-equilateral points, eliminate the whole contraction boundary, or solve the cube optimization problem.

## Limitations
No full-stratum or global-maximizer statement should be inferred.

## Sources
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/024
- https://arxiv.org/abs/1608.00520
- https://doi.org/10.1002/mma.1670100404
