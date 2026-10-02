# Independent audit — 2026-10-01

**Disposition:** passed

## Correctness

The proof survives reconstruction. For reduced block-length ratio \(u/v\), the worst point-count exponent \(1/2\) occurs only at \(u=2,v=1\), so summing the family \((2h,h)\) costs \(L^5\), while all \(u\ge3\) pairs cost at most \(X^{1/3}L^6\). Hence \(A(\theta)=1/2+5\theta\). Substitution into the independently checked length-sensitive forest sum gives \(F(\theta)=(1-\theta)A(\theta)+2\theta\), with \(F(1/20)=13/16\) and limiting value \(F(1/24)=439/576\). Runbo Li’s Theorem 1.1 supplies the required almost-all backward prime interval for every exponent \(1/24+\varepsilon\), so the displayed bound is correctly stated with an arbitrary positive loss rather than at the endpoint.

## Originality

The pinned Sneiderman reconstruction proves the same construction and length-sensitive forest mechanism but uses the cruder raw-root exponent \(1/2+6\theta\), giving \(43/50\) at \(\theta=1/20\). The audited reduced-ratio observation is not present there. Resultary found a later 2026-09-19 SCOPE record with a weaker \(5/6+\varepsilon\) short-gap exponent, not prior coverage. The available Kielhorn metadata establishes the same density-one prime-gap-deletion problem but does not expose a matching quantitative exponent; the main manuscript remains inaccessible and is retained as risk.

### Equivalent formulations

The comparison was made at the level of raw-root counting and forest implications, not titles.

### Broader coverage

Neither inspected statement dominates the audited quantitative claim.

### Exact database or table comparison

The result is an analytic theorem, so database lookup is not a proof path.

### Claim versus prior implication

Prior theorems supply ingredients but do not mechanically imply the sharper exponent without the new counting observation.

### Source inspections

- **Audit and reconstruction of Chojecki’s gap-greedy preprint on Erdős Problem 421 with a sharpened short-gap estimate** — PRIOR_INGREDIENT_NOT_COVERING. Material read: complete main.tex including split-product curves, raw count, branch bounds and length-sensitive forest summation. Evidence location: https://github.com/Robby955/erdos-421-audit/tree/318c112c7a70879d98d86d8c3d9a280d77dadb35.

- **Primes in almost all short intervals III** — PRIOR_ANALYTIC_INPUT. Material read: primary PDF theorem statement and surrounding introduction. Evidence location: https://runbolicarey.com/assets/downloads/Primes_in_almost_all_short_intervals_III.pdf.

- **Distinct consecutive products in a density-one set via prime-gap deletions** — PLAUSIBLE_INACCESSIBLE_SOURCE. Material read: public metadata and detailed abstract; main manuscript not obtained. Evidence location: https://doi.org/10.5281/zenodo.21287064.

## Value

The quantitative sparsity of the rejected set is intrinsic to the density-one construction, and improving the short-gap exponent from the earlier \(43/50\) mechanism to the limiting \(439/576\) by identifying the one-parameter worst degree ratio is a motivated structural sharpening rather than a parameter renaming.

## Residual risks and limitations

The power exponents concern the short-gap component; the full complement has arbitrary fixed logarithmic savings rather than a global power saving. The value 439/576 is a limiting infimum obtained from parameters above 1/24. The main Kielhorn manuscript was not obtained in full and remains an explicit originality risk.
