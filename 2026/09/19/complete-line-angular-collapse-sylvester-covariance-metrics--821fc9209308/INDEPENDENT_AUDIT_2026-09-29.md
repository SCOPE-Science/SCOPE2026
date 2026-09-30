# Independent Audit — 2026-09-29

**Record:** `2026/09/19/complete-line-angular-collapse-sylvester-covariance-metrics--821fc9209308`  
**Title:** Completeness and angular collapse in Sylvester-power covariance metrics  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `1ee163638b6437d44dd11fae0142f63195dfe017`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The global geometry argument is sound. Homogeneity makes scalar-ray length finite at zero for degree r<2 and at infinity for r>2. For r=2, diagonal metric terms control Euclidean motion of the ordered log-spectrum; a metric-Cauchy sequence therefore remains in a compact spectral annulus, where positivity and continuity of the kernel give uniform equivalence with the Frobenius metric. The dilation and inversion pullbacks follow directly from homogeneity and differential inversion. The normalized complete-line kernel is xy cosh((a/2)log(x/y)); its mean threshold |a|≤2 and the quarter-turn length formula check algebraically. Independent numerical evaluation reproduced the π κ^((2−|a|)/4) asymptotic and all three threshold regimes.
- **Originality — PASS:** Hiai–Petz and the Thanwerdas–Pennec synthesis state completeness for mean-kernel metrics with homogeneity power two; the latter explicitly phrases the completeness result for mean kernels. Searches of that literature did not locate the stronger theorem for every smooth positive homogeneous kernel, nor the non-mean |p−q|>2 complete members or the exact angular-collapse law for the 2026 Sylvester-power family. The result is elementary enough that differently phrased older coverage remains a residual risk, but no concrete prior statement was found.
- **Scientific value — PASS:** The theorem adds a sharp global phase diagram to a metric family proposed as a tunable preconditioner: p+q=2 is exactly the complete and scale/inversion-symmetric line, while |p−q|>2 has asymptotically cheap eigendirection rotation. This is useful geometric information not captured by local Hessian conditioning.

## Independent checks

- Re-derived the scalar-ray incompleteness integral and log-spectrum coercivity bound.
- Checked dilation and inversion pullbacks symbolically.
- Recomputed quarter-turn lengths for a=1,2,3 at κ=10² and 10⁶; the scaled values converge to π with the stated exponent.

## Literature and evidence

- Li et al., Optimization over covariance matrices with a parameterized metric — Primary 2026 source introduces the two-parameter family and its conditioning analysis, not the audited global completeness/angular-collapse theorem. (https://arxiv.org/abs/2609.17089)
- Hiai and Petz, Riemannian metrics on positive definite matrices related to means — Introduces kernel metrics and studies mean-power kernels; established mean-kernel completeness is prior art. (https://arxiv.org/abs/0809.4974)
- Thanwerdas and Pennec, O(n)-invariant Riemannian metrics on SPD matrices — Synthesizes kernel metrics and states completeness for mean-kernel metrics with homogeneity power two. (https://arxiv.org/abs/2109.05768)

## Limitations

- The angular-collapse statement is an upper bound from one explicit isospectral path, not an exact geodesic-distance formula.
- Completeness concerns the full SPD cone and does not imply convergence or failure of a particular optimization algorithm.
- Originality of the general homogeneous-kernel lemma is to the best of searched literature; older equivalent terminology remains a residual risk.

**Independent-audit disposition:** passed.

GitHub was read only as evidence; no repository writes were made by this audit run.
