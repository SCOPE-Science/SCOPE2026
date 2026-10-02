---
audit_date_utc: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For entropic optimal transport between Gaussian marginals whose covariance matrices are simultaneously diagonalizable and have spectra in (0,M], the optimal Gaussian plans satisfy a dimension-free one-sided W2 stability bound with \(C_1(r)=1+(1+4F_*^2)\(r^2\)\), \(F_*=0.133529881\)..., r=M/eps, and a two-sided bound with constant 2C1(r).

## Correctness — PASS

The scalar Gaussian EOT cross-covariance c=(sqrt(\(\varepsilon^2+4ab\))-eps)/2 was reconstructed. Writing a=\(u^2\), the regression contribution g(u)=c/u has derivative bounded by r=M/eps, while the residual standard deviation has derivative bounded by 2F*r. Maximizing F(s)=sqrt(s-1)/(sqrt(2)s(s+1)) gives \(s_*=(3+\sqrt{33})/6\) and \(F_*=0.133529881\)..., hence \(1+4F_*^2=1.071320916\).... A common-Gaussian coupling in each simultaneous eigen-coordinate gives the stated one-sided factor, and the squared triangle inequality gives 2C1 for the two-sided change. The supplied randomized Bures-Wasserstein script is consistent with, but not substituted for, this proof.

**Evidence inspected:** artifacts/numeric_check.py; https://arxiv.org/abs/2006.02572; https://arxiv.org/abs/2412.09235

**Residual risk:** The result requires one common diagonalizing basis for the covariance family and does not extend as stated to noncommuting covariances.

## Originality — PASS

Gaussian EOT closed forms are prior. Eckstein-Nutz give general quantitative plan stability of Hölder type, and Chiarini-Conforti-Greco-Tamanini give KL stability under semiconcavity. The inspected Theorem 1.1 controls relative entropy by a marginal KL term plus a semiconcavity multiple of \(W_2^2\); it does not state or imply the package's explicit commuting-Gaussian W2-Lipschitz coefficient C1(r). No primary source located contained that coefficient or the same one-sided/two-sided formulas.

**Equivalent formulations:** Checked Gaussian Schrödinger-bridge covariance formulas, W2 stability of plans, entropic-potential stability, and KL stability formulations.

**Broader coverage:** General stability theorems cover wider classes but with different metrics, hypotheses, or Hölder-type dependence; they do not dominate the explicit C1(r) inequality.

**Exact database or table:** No exact constant table containing F* or C1(r) was located.

**Claim versus prior implication:** Prior Gaussian closed forms provide ingredients, not the derived dimension-free perturbation coefficient; the general KL/Hölder results do not mechanically yield this exact W2 bound.

**Primary/technical sources inspected:** https://arxiv.org/abs/2006.02572; https://doi.org/10.1137/21M1448159; https://arxiv.org/abs/2412.09235

**Residual risk:** A Gaussian-specialized stability estimate under different notation could have been missed.

## Value — PASS

An explicit dimension-free stability constant in a tractable Gaussian benchmark is useful for calibrating general entropic-transport stability theory, and the r->0 limit records the correct unit baseline. This is a motivated exact special case, not merely a numerical test.

**Context inspected:** General entropic-plan stability literature and Gaussian EOT closed forms.

**Residual risk:** The factor 2 in the two-sided bound is deliberately non-sharp and the result does not solve the noncommuting case.

## Disposition

PASS. The final claim clears correctness, originality, and value as stated. No change to `RESULT.md` or `SLOGAN.txt` is required.
