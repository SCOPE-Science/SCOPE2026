# Independent Audit — 2026/09/18/fekete-szego-analytic-lipschitz-constant--250a4af644f8

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `e401d8d37af7ffce985ea8668ab5a8d4d3cbea47`
- Disposition: **PASSED**

## Correctness

**PASS** — The quantitative refinement is correct. For the unit-disk normalization phi(z)=z+a_2 z^2+a_3 z^3+..., (log phi')''(0)=6a_3-4a_2^2=6(a_3-(2/3)a_2^2), so the sharp Fekete-Szego inequality at mu=2/3 gives |g''|<=6(1+2e^{-4}). The centered Gaussian Taylor remainder is bounded by 3(1+2e^{-4})sigma^2. Using |B'|<=4 and the exact imaginary part of the complex Gaussian, Cauchy-Schwarz gives |Im G|<=4 sigma sqrt(sinh(sigma^{-2})). These bounds make h=psi' exp(-lambda-iG) satisfy |h|<=|psi'| on the strip and keep the real-axis argument within E_sigma, giving c(sigma)=cos(E_sigma)e^{-lambda_sigma}. At sigma=9/14, E=1.285211227040433, lambda=6.072639494094411 and c=0.0006493848651431162, so the stated c_0>6.49e-4 follows. The identified source slips in the Taylor sign and Gaussian second moment are also correctly diagnosed; at sigma=1/3 the corrected 8/9 error remains below pi/3.

## Originality

**PASS** — MacMahon's September 2026 preprint supplies the underlying analytic-Lipschitz/inner-metric comparison and Gaussian-straightening idea, while the Fekete-Szego coefficient bound is classical. The audited contribution is the nontrivial quantitative synthesis: recognizing the second logarithmic-derivative coefficient as the sharp mu=2/3 Fekete-Szego functional and coupling it to a sharper oscillatory Gaussian strip estimate. Targeted searches located no prior statement of this improved universal constant or this exact refinement. Because the source theorem is extremely recent, an unindexed parallel observation remains a residual risk.

## Scientific value

**PASS** — The result strengthens a newly introduced universal comparison by roughly thirty-nine orders of magnitude in the explicit lower constant, while also repairing two quantitative slips in the source proof without changing its qualitative conclusion. The bridge between a sharp classical univalent-function coefficient theorem and the new metric estimate is reusable and materially improves the quantitative content of the source theorem.

## Sources

- On Simply Connected Domains Supporting an Unbounded Analytic Function with Bounded Derivative (C. MacMahon): https://arxiv.org/abs/2609.20607 — Source analytic-Lipschitz/inner-metric theorem and Gaussian straightening argument.
- A general approach to the Fekete-Szego problem (J. H. Choi; Y. C. Kim; T. Sugawa): https://doi.org/10.2969/jmsj/05930707 — Modern source recording the classical sharp Fekete-Szego inequality used at mu=2/3.

## Limitations

- No optimality is claimed for c_0 or for the Gaussian kernel method.
- The originality conclusion is necessarily qualified because the motivating preprint is very recent.
- The theorem remains restricted to simply connected planar domains.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository write was performed. Open-access/preprint sources were checked first; Oxford Download was not needed for this record.
