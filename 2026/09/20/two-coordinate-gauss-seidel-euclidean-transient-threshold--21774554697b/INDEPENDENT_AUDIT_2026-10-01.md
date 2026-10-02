---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For exact cyclic Gauss--Seidel on every real two-dimensional SPD system, updating the larger diagonal first minimizes one-sweep Euclidean amplification, and the exact fixed-condition-number minimax factor is \(\delta\sqrt{1+\delta^2}\), giving the sharp uniform nonexpansion threshold \(\kappa\approx8.352410032\); ordering changes only the first-sweep transient because \(T^2=qT\).

## Correctness — PASS

The two sweep matrices follow directly from the coordinate updates and each has one nonzero column, so its spectral norm is the displayed column norm. The common \(q^2\) term makes the larger-diagonal-first rule exact. With eigenvalues \(\lambda\le\Lambda\), the bounds \(|c|/\max(a,d)\le\delta\) and \(q\le\delta^2\) are both attained by the balanced-diagonal rotation, proving the minimax factor. Solving \(\delta^2+\delta^4=1\) gives the threshold. Direct multiplication gives \(T^2=qT\). The actual verifier was inspected, and an independent algebraic replay reproduced the threshold and quartic relation.

**Checked sources.** assigned RESULT.md at frozen tree 4a8b75f1a07303eefbb072460fd32857344b3be8; artifacts/verify_gs_2d_ordering.py blob 8e07b53893f4e1ea0df74c83255f5de0e90e8c06; Varga 1959 ordering literature; Wright 2015 coordinate-descent survey; Mohlenkamp--Young--Barany 2020 transient block-coordinate study

**Residual risks.** No correctness defect was found.

## Originality — PASS

Classical ordering work, modern random-reordering analyses, and transient block-coordinate studies establish that order can affect convergence or startup behavior, but targeted semantic and literature searches did not locate the exact two-dimensional Euclidean minimax factor, the sharp condition-number threshold, or the identity isolating all ordering dependence to one startup sweep.

### Equivalent formulations

The audited target is one-sweep Euclidean operator norm at fixed condition number, not asymptotic spectral convergence.

### Broader coverage

Their broader algorithmic scope does not imply the exact two-coordinate minimax envelope in the inspected theorem-level material.

### Exact database or table

A finite database is inapplicable because the theorem is an analytic minimax statement over all matrices at each condition number.

### Claim versus prior implication

The elementary update formulas alone do not state the sharp condition-number frontier; nevertheless their simplicity leaves a real folklore risk.

**Checked sources.** https://doi.org/10.2140/pjm.1959.9.925; https://doi.org/10.1007/s10107-015-0892-3; https://www.global-sci.com/ijnam/article/view/10419; Resultary semantic search

**Residual risks.** Because the proof is elementary, an equivalent two-dimensional calculation may exist in older numerical-linear-algebra literature under different terminology.

## Value — PASS

The theorem is a natural exact benchmark separating asymptotic convergence from nonnormal startup amplification. It gives a sharp robust condition-number frontier and a closed-form static ordering rule, so it is more than a routine sign or normalization check despite its low dimension.

**Checked sources.** classical Gauss--Seidel ordering literature; modern coordinate-descent transient literature

**Residual risks.** The value is diagnostic and structural rather than a higher-dimensional algorithmic improvement.

## Limitations

- Only two-dimensional real SPD systems and the ordinary Euclidean error norm are treated.
- Exact coordinate minimization and exact arithmetic are assumed.
- No higher-dimensional ordering theorem or implementation-speed claim is made.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
