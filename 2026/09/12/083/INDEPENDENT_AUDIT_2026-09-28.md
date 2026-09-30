# Independent audit — 2026-09-29

**Record:** `2026/09/12/083`  
**Disposition:** **repaired**  
**Audited tree:** `8d0e9a35f5f0d31070e168ce4b6bc52e8ca625d7`

## Correctness
The 48 labels follow the standard parafermion classification. Independent recomputation with a larger B=20 weight box and grades through 7 reproduced every one of the 48 filed (F,t) minima and dim A=149. Independently convolving the vacuum string coefficients with prod(1-q^n)^2 gives 1,0,6,13,38,80,182. The filed sentence saying equal-F theta-translated minimizers should be summed was inconsistent with the data and parafermion string-function decomposition; the top multiplicity is the common string coefficient, and that wording is corrected.

## Originality
Published work already supplies the rationality, module parametrization, fusion rules and quantum-dimension framework. The exact G2 level-2 table was not located in the checked sources, but an unsuccessful search alone cannot establish priority; the repaired record therefore presents it as a computational table without a first/new claim.

## Scientific value
A compact numerical table of conformal weights, top multiplicities, Zhu dimension, and low vacuum character for K(G2,2) is useful for subsequent Zhu/C2 and classically-free calculations.

## Findings
- All 48 (F,t) minima were stable under an independent larger-window computation.
- The former “sum all minimizers” wording was wrong; theta-translated representatives share one string coefficient.
- Repository artifact paths corrected from `output/artifacts/...` to `artifacts/...`.

## Independent checks
- Reimplemented Freudenthal-Kac recursion independently with B=20/N=7 for all four affine modules; all 48 minima matched B=14/N=5.
- Recomputed sum of squared top multiplicities as 149.
- Recomputed vacuum character through grade 6 from the archived string coefficients.

## Limitations
- Finite computational stabilization does not substitute for a separately formalized all-grades truncation theorem; no priority claim is certified.

## Sources
- https://doi.org/10.1090/tran/7547
- https://doi.org/10.1016/j.jalgebra.2009.08.003
- https://arxiv.org/abs/1207.3909
- repository:2026/09/12/083/artifacts/sectors.json
- repository:2026/09/12/083/artifacts/stringQL.json
