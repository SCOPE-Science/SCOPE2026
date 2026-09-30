# Independent audit — 2026-09-30

**Record:** `2026/09/21/polylogarithmic-reciprocal-smoothing-u-threshold--6f7ea490d72a`  
**Repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `4563608c753bb7e38c73b90816fb1ab30983ddc2`  
**Disposition:** **PASSED**

## Correctness

**PASS.** The upper bound follows correctly from |b_1|<=2, the area theorem sum_{n>=2}(n-1)|b_n|^2<=1, and two separate Cauchy--Schwarz estimates: H(sigma)<=1 makes the smoothed reciprocal zero-free, while the U-functional is bounded by the square root of sum_{n>=2}(n-1)/(n+1)^{2sigma}. For sigma>=sigma_*>7/5 the latter is below the stated 9/5-series majorant 0.945. Independent high-precision evaluation gives H(1.413519)>1 and H(1.413520)<1. The lower obstruction using f_alpha=z/(1-z)^alpha is sound because its reciprocal coefficients are negative with |b_n|~c n^{-alpha-1}, so the positive U-series diverges whenever alpha+sigma<1.

## Originality

**PASS (literature-bounded).** Ali--Obradovic--Ponnusamy (2013) give the published universal upper bound 3/2 and pose the smallest-parameter problem. The 1996 Ponnusamy--Sabapathy paper was first sought through open routes and then obtained through authorized institutional access; all 15 pages were inspected. Its theorem statements and convolution results concern geometric mapping properties of generalized polylogarithms and do not state this arbitrary-f reciprocal-smoothing threshold or the 1.413520 bracket. Targeted searches and repository code search found no equivalent result.

## Scientific value

**PASS.** The result narrows a concrete published universal threshold from sigma_U<=3/2 to 1<=sigma_U<1.413520, while identifying different mechanisms for the upper and lower bounds. It leaves a substantially smaller, analytically defined interval for the true threshold.

## Literature and evidence

- Ali, Obradovic and Ponnusamy, Necessary and sufficient conditions for univalent functions: https://doi.org/10.1080/17476933.2011.599116
- Ponnusamy and Sabapathy, Polylogarithms in the Theory of Univalent Functions: https://doi.org/10.1007/BF03322186
- Obradovic and Ponnusamy, Univalence and starlikeness of certain transforms defined by convolution of analytic functions: https://doi.org/10.1016/j.jmaa.2007.03.020

## Limitations

- The exact universal U-threshold remains unresolved in [1,sigma_*].
- The lower construction rules out membership in U but does not by itself prove failure of univalence.
- The 1996 comparison is fully inspected, but differently indexed later work on reciprocal/Hadamard smoothing remains a residual priority risk.


This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
