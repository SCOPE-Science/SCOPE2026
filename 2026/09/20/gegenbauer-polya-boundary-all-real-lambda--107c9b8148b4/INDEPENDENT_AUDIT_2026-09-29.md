# Independent audit — 2026-09-29 UTC

Record: `2026/09/20/gegenbauer-polya-boundary-all-real-lambda--107c9b8148b4`  
Assigned source tree: `b53b64bae01c4474a65b504bc4e8ac3f15ddbdf6`  
Audited current source tree: `b53b64bae01c4474a65b504bc4e8ac3f15ddbdf6`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `b2e47b54447225c5e3328af2834d2b18c7f0340a`  
Disposition: **passed**

## Correctness

**independently_supported**. The continuous-parameter sufficiency proof checks. In the Gegenbauer product formula the cap self-convolution calculation has the stated discriminant and Jacobian, and the normalizations satisfy a_lambda*kappa_lambda/lambda=1/pi. Its nth transform is the square of the cap transform; for n>0 the latter is proportional to (sin beta)^(2lambda+1) C_{n-1}^{lambda+1}(cos beta), so it has only finitely many zeros in any beta interval, while n=0 is strictly positive. Lu's full-support positive-mixture lemmas are stated for arbitrary real positive exponents: Lemma 3.3(iii) supplies the tan^2 mixture, Lemma 3.4 with nu=1/2 supplies the linear-to-quadratic truncated-power mixture, and Lemma 3.3(iv) plus the Laplace representation handles beta=pi/2 without a limiting loss of strictness. These ingredients therefore transfer strict Gegenbauer-coefficient positivity to (t-r)_+^(lambda+1) for every lambda>0 and 0<t<=pi. The beta-kernel identity then preserves strict positivity for every delta>lambda+1.

## Originality

**qualified_supported_continuous_parameter_extension**. Beatson--zu Castell--Xu state the Polya integral conjecture for arbitrary real lambda>0, whereas Xu's later Jacobi theorem is stated on an integer-parameter family and Lu's 2025 truncated-power theorem is formulated on ordinary spheres, hence at discrete dimension-linked Gegenbauer parameters. Lu's paper does provide the real-exponent positive-mixture machinery used here but does not state the all-real Gegenbauer spectral theorem. Searches did not locate an equivalent continuous-lambda sufficiency result. The claim is therefore supported only for this continuous-parameter extension; the sphere-relevant discrete cases and the analytic mixture lemmas are prior art, and a differently indexed hypergroup formulation remains a residual priority risk.

## Scientific value

**meaningful_extension_of_literal_conjecture**. The result closes the sufficiency half of the literal all-real parameter range of the published conjecture and isolates an explicit cap self-convolution identity on the Gegenbauer hypergroup. It is useful beyond integer-dimensional spheres, while the unproved necessity direction keeps the scope appropriately limited.

## Independent checks

- Verified symbolically that the cap normalization a_lambda*kappa_lambda/lambda equals 1/pi.
- Inspected Lu's open full text, including Lemmas 3.3 and 3.4 and the beta>=pi/2 Laplace-mixture step.
- Checked the finite-zero strictness argument from the Gegenbauer antiderivative formula.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/gegenbauer-polya-boundary-all-real-lambda--107c9b8148b4
- https://arxiv.org/abs/1110.2437
- https://arxiv.org/abs/1510.08658
- https://arxiv.org/abs/1701.00787
- https://www.math.wichita.edu/~lu/resume/power.pdf
- https://doi.org/10.1016/j.jat.2024.106120

## Limitations

- The necessity direction delta<lambda+1 for arbitrary real lambda is not proved.
- Lu's positive-mixture and complete-monotonicity lemmas are imported rather than reproved.
- The integer-dimensional spherical cases are prior work and are not part of the novelty claim.
- A differently formulated continuous-parameter hypergroup result could remain unindexed.
