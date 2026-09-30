# Independent audit — 2026-09-30

**Record:** `2026/09/21/power-exponential-product-local-instability--348ea42cbf67`  
**Repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `ca0612867de2c01db388edda4609898b6faf08d8`  
**Disposition:** **PASSED**

## Correctness

**PASS.** Direct Taylor expansion of D_{n,r} at t*1 cancels the constant and linear terms and gives the stated scalar Hessian coefficient times n sum y_i^2-(sum y_i)^2. Maximizing t(log t)^2 on (0,1] gives 4/e^2 at t=e^{-2}, hence the exact transverse-instability condition r>e^2/(2n). For r=1 this yields nearby counterexamples for all n>=4. The one-coordinate critical expansion at r=e^2/(2n) gives the stated negative cubic coefficient for n>=3; independent 80-digit evaluations for n=3,4,5 converge to that coefficient and reproduce the sign.

## Originality

**PASS (literature-bounded).** Coronel--Huancas (2014) state the all-n Theorem 1.4 and Conjecture 3.3. Matejicka (2016) explicitly lists neighboring Theorems 1.2 and 1.3, Lemma 3.1, and Conjectures 3.1 and 3.2 as invalid, but not Theorem 1.4 or Conjecture 3.3. Targeted searches for the product inequality, correction language, and the e^2/(2n) threshold found no prior version of this diagonal second-variation obstruction; repository code search found no duplicate. An unindexed correction or differently notated calculation remains possible.

## Scientific value

**PASS.** The result identifies an analytic family of counterexamples to a published theorem in every dimension n>=4 and quantifies the exact onset of local diagonal instability for the associated parameter conjecture, including the critical cubic failure for n>=3.

## Literature and evidence

- Coronel and Huancas, The proof of three power-exponential inequalities: https://doi.org/10.1186/1029-242X-2014-509
- Matejicka, On the Cirtoaje conjecture: https://doi.org/10.1186/s13660-016-1092-2

## Limitations

- The condition r<=e^2/(2n) is only local second-variation stability and does not prove the global inequality.
- The critical case n=2, r=e^2/4 remains unresolved by this expansion.
- The global r=1 cases n=2,3 are not classified here.


This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
