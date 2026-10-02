# Independent scientific audit — SCOPE-20260919-80bd8eba23bd

Audited at: 2026-10-01T17:15:19.026518Z

Disposition: **passed**

## Correctness — PASS

For the mirror products, the density difference is twice the odd Walsh part of \(\prod_i(1+a_i x_i)\). Orthogonality bounds all odd degrees at least three in \(L^2\) by \(O(q^{3/2})\), while \(q(1-q/2)\le\Delta^2\le q\); this yields the uniform \(O(q)\) profile. Sorting normalized coefficients and taking a triangular-array limit gives a Rademacher series plus an independent Gaussian tail; uniform second moments justify convergence of absolute first moments. Sharp \(p=1\) Khintchine then gives the complete interval \([1/\sqrt2,1]\), and diffuse arrays give \(\sqrt{2/\pi}\). The general Bernoulli-product corollary follows from exact midpoint contrasts with variance \(v_i/(2-v_i)\), the same odd-product expansion, and Lindeberg.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_weak_signal_profiles.py
- Smirnov arXiv:2609.19222 full text

### Correctness risks

- The quantitative \(2q\) error is a convenient local bound rather than a globally optimal remainder constant.
- The Bernoulli-product corollary requires the stated diffuse Lindeberg condition.

## Originality — PASS

Fresh full-text inspection of Smirnov's paper, including its later revision, shows a constant-factor theorem \(d_{TV}\asymp E\min\{1,\sqrt G\}\) and a mirror-product lower bound with an unspecified absolute constant. It does not state the uniform weak-signal Rademacher profile, the complete subsequential Rademacher-Gaussian classification, or the exact local efficiency interval. A SCOPE record published on 2026-09-20 independently extends the same local result to a finite-signal diffuse curve; because it is later-dated than this 2026-09-19 record, it is corroborating later work rather than prior coverage.

### Equivalent formulations

No earlier equivalent exact profile theorem was located; the later SCOPE result is not treated as prior art.

### Broader coverage

These ingredients motivate the proof but do not by themselves state the uniform profile approximation or classify every subsequential efficiency.

### Exact database or table

This is not a known-table computation.

### Claim versus prior implication

The audited odd-Walsh remainder estimate is the additional step that converts the constant-factor theorem into an exact weak-signal profile.

### Sources inspected

- TV between Bernoulli products, up to constants — https://arxiv.org/abs/2609.19222. NOT_COVERING: The source proves a uniform constant-factor comparison and an unspecified mirror lower constant, not the exact weak-signal profile.
- Sharp local and diffuse distinguishability for Bernoulli mirror products — published SCOPE record 2026/09/20/sharp-local-diffuse-bernoulli-mirror-distinguishability--0e1e1f426bbd. LATER_CORROBORATION: It is dated one day later and extends the local result to a finite-signal diffuse curve; it corroborates rather than precedes the assigned record.

### Checked sources

- https://arxiv.org/abs/2609.19222
- published SCOPE 2026/09/20/sharp-local-diffuse-bernoulli-mirror-distinguishability--0e1e1f426bbd
- Resultary semantic search

### Residual risks

- Older binary-experiment, Riesz-product, or LAN literature may contain an equivalent local profile under different notation.
- No claim is made about the globally optimal all-signal constant in Smirnov's theorem.

## Value — PASS

The theorem resolves the local efficiency geometry of a newly studied product-measure comparison: it identifies exact sparse and diffuse constants, classifies every subsequential profile, and transfers the result to a natural diffuse Bernoulli-product regime. This is more than a routine constant tweak.

### Value sources

- https://arxiv.org/abs/2609.19222
- assigned RESULT.md

### Value risks

- The result is local in signal strength; finite-signal behavior requires additional hypotheses and is outside the assigned main theorem.

## Limitations

- The sharp profile theorem is a weak-signal statement.
- The direct Bernoulli-product asymptotic assumes vanishing total signal and a maximum-coordinate Lindeberg condition.
- No global optimal constant for arbitrary signal strength is claimed.
