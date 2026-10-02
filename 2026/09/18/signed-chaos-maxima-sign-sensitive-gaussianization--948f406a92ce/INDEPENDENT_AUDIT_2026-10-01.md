# Independent audit — 2026-10-01

**Disposition:** passed

## Correctness

The exact cumulant generating functions give \(K_+(t)=t^2/2+\sqrt2 t^3/(3\sqrt m)+t^4/(2m)+O(t^5/m^{3/2})\) and \(K_0(t)=t^2/2+t^4/(2m)+2t^6/(3m^2)+O(t^8/m^3)\). At \(x\sim\sqrt{2\log p}\), the positive cubic term yields the shift \(4(\log p)^{3/2}/(3\sqrt m)\); the balanced saddlepoint rate \(I_m(x)=x^2/2-x^4/(2m)+4x^6/(3m^2)+\cdots\) yields shift \(2(\log p)^2/m\). The remainder ratios are \(o(1)\) under \(m/\log p\to\infty\). The gamma triangular-array theorem covers the positive row normalization, and the balanced tilting argument gives the stated tail ratio and shifted-Gumbel limits.

## Originality

Cai and Hu provide the signed-chaos framework and an effective-rank phase transition, while Bose–Dasgupta–Maulik and Anderson–Coles–Hüsler provide triangular-array extreme-value machinery. None of the inspected statements gives the paired same-\(r_4\) positive-versus-balanced thresholds \((\log p)^3\) and \((\log p)^2\) with the explicit critical Kolmogorov profile. Resultary found closely matching SCOPE records only on 2026-09-19, after this record.

### Equivalent formulations

Compared the actual shift laws and threshold implications.

### Broader coverage

Neither source implies the balanced-versus-positive separation at fixed fourth-order effective rank.

### Exact database or table comparison

Those records postdate the audited publication date and are not prior coverage.

### Claim versus prior implication

The final theorem is not a direct corollary stated by the sources.

### Source inspections

- **Approximation Theorems for High-Dimensional Canonical U-Statistics: Gaussian Chaos and Phase Transition** — PRIOR_FRAMEWORK_NOT_COVERING. Material read: primary abstract and theorem-level description available through arXiv indexing. Evidence location: https://arxiv.org/abs/2609.20529.

- **Maxima of Dirichlet and triangular arrays of gamma variables** — PRIOR_POSITIVE_CASE_TOOL. Material read: primary full PDF text around Theorem 2.1 and its centering equation. Evidence location: https://arxiv.org/abs/0803.3518.

- **Maxima of Poisson-like variables and related triangular arrays** — RESIDUAL_RISK. Material read: bibliographic record and abstract; full text not obtained. Evidence location: https://doi.org/10.1214/aoap/1043862420.

## Value

The theorem identifies spectral sign balance as a sharp phase coordinate invisible to the fourth-order effective rank: the Gaussianization requirement changes by a full logarithmic power and the critical error is quantified by an explicit Gumbel-translation profile. This is a natural boundary question in the motivating high-dimensional approximation problem.

## Residual risks and limitations

Independent coordinates and flat equal-magnitude spectra only; exact balance is required for the log-squared threshold statement; the analysis assumes m/log p tends to infinity and excludes finite-sample U-statistic approximation error. Anderson–Coles–Hüsler (1997) was not inspected in full.
