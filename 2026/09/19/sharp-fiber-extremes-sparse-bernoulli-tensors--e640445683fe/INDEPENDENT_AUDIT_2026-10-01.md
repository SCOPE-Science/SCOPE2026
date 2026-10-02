# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-e640445683fe`

## Correctness — PASS

The full Zhou–Zhu primary paper was inspected through the main theorem, its optimality discussion, maximum-fiber lemma, and heavy-tuple proof. The source explicitly uses fiber norms as the unavoidable obstruction. For one fixed tensor mode the \(n^{k-1}\) fiber degrees are independent \(\mathrm{Bin}(n,p)\), and all modes change an upper bound only by a fixed factor \(k\). Chernoff upper bounds and one-mass Stirling lower bounds therefore give the sharp constant \(x\) solving \(c(x\log x-x+1)=k-1\). At \(d=c\log n\), the binomial point-mass expansion and geometric tail ratio yield the center \(xc\log n-(\log\log n)/(2\log x)\) and the stated lattice profile. I independently checked the rate inversion and sample constants, including \(x=e\) for \(k=3,c=2\). The same rate comparison gives the polynomial-tail obstruction and Lambert-W sublogarithmic scale.

### Correctness sources

- Zhou–Zhu, arXiv:2609.20520 full text
- assigned RESULT.md and exact-tail verifier
- independent large-deviation inversion checks
- classical discrete extreme-value literature

### Correctness risks

- The exact lattice limit is proved only for one fixed mode; the maximum over all modes is localized to \(O_P(1)\), not assigned a cross-mode limit law.
- The result gives a lower obstruction, not the full tensor-norm limiting constant.

## Originality — PASS

Zhou–Zhu explicitly note the maximum-fiber obstruction and qualitative sublogarithmic divergence, so those ideas are prior and are not treated as novelty. Their full paper uses a deliberately nonsharp Chernoff constant in the maximum-degree lemma and states only existence of \(C_{k,r,c}\). Fresh Resultary searches found no tensor-specific theorem with the exact large-deviation constant, second-order lattice center, polynomial-tail exponent, or the necessary \(C\ge\sqrt{h^{-1}((k-1+r)/c)}\) dependence. Classical scalar maxima may contain the one-dimensional extreme-value asymptotic, but not the tensor-specific high-probability constant consequence located here.

### equivalent_formulations

Searches:
- Resultary searches for sparse Bernoulli tensor fiber extremes, the rate equation, the second-order center, and the polynomial-tail constant
- full-text search of Zhou–Zhu for maximum fiber degree and optimality

Evidence:
- The audited theorem was the only exact tensor-specific match.
- The source paper's Lemma 4.3 chooses any sufficiently large \(\kappa\), without optimizing it.

Reasoning:
Equivalent formulations via the maximum binomial degree and via unavoidable spectral-norm constants were both checked.

### broader_coverage

Searches:
- Zhou–Zhu 2026 full text
- Anderson–Coles–Hüsler discrete maxima context
- sparse random graph degree extremes

Evidence:
- The source already contains the obstruction mechanism but not the sharp asymptotics.
- Classical scalar extreme-value theory can subsume parts of the binomial-max calculation, so novelty is restricted to the tensor-specific sharpened barrier package.

Reasoning:
The tensor conclusion is not a claim of a new scalar extreme-value method.

### exact_database_or_table

Searches:
- current Resultary random-tensor and Bernoulli-extreme findings

Evidence:
- No exact table or stronger tensor-specific constant theorem was found.

Reasoning:
The constants arise from an asymptotic theorem, not a database lookup.

### claim_vs_prior_implication

Searches:
- implication comparison with Theorem 2.1 and Lemma 4.3 of Zhou–Zhu

Evidence:
- Theorem 2.1 asserts existence of a constant \(C_{k,r,c}\); Lemma 4.3 uses a slack Chernoff threshold. Neither determines the optimal necessary dependence on \(k,r,c\) or the second-order maximum profile.

Reasoning:
The audited theorem sharpens an explicitly order-optimal but constant-unspecified source result.

### source_inspections

- **Sharp spectral norm concentration of sparse random tensors** — https://arxiv.org/abs/2609.20520. Trigger: Direct source theorem whose unavoidable fiber obstruction is quantified. Material read: Full primary paper through the main theorem, optimality paragraph, maximum-fiber lemma, multibox discrepancy, and deterministic heavy-tuple summation. Method: Primary full-text statement/proof comparison. Assessment: PARTIAL BACKGROUND, not full coverage. Evidence: It states \(\sqrt d\)-order optimality and qualitative sublog divergence, but leaves the sharp fiber constant and second-order law unspecified.
- **Assigned fiber-extremes verifier** — artifacts/verify_fiber_extremes.py. Trigger: Exact binomial-tail numerics and lattice centering checks. Material read: Complete source and saved output. Method: Inspection plus independent rate inversion. Assessment: Corroborates the asymptotic calculations. Evidence: Independent inversion reproduces the stated sample thresholds.

### checked_sources

- Zhou–Zhu arXiv:2609.20520 full text
- current Resultary tensor-extreme searches
- classical discrete-extreme literature references
- assigned RESULT.md and verifier

### residual_risks

- The scalar maximum asymptotic may be available in classical triangular-array literature under different notation; the audit therefore limits originality to the tensor-specific sharpened barrier and constant consequences.

## Scientific value — PASS

The source theorem is explicitly sharp only in order and leaves its high-probability constant unspecified. Determining the exact unavoidable dependence on tensor order, logarithmic sparsity, and requested tail exponent, together with the second-order transition and sublogarithmic scale, is a natural and useful sharpness boundary for sparse tensor concentration.

### Value sources

- Zhou–Zhu spectral-norm theorem
- audited maximum-fiber barrier

### Value risks

- The result is a lower-bound obstruction and does not determine the full injective-norm limit.

## Limitations

- Homogeneous independent Bernoulli tensors only.
- The one-mode lattice law does not assert independence across modes.
- Classical scalar extreme-value theory may cover the binomial-maximum component; originality is restricted accordingly.

## Disposition

**PASSED**
