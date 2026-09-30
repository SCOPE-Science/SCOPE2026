# Independent Audit — Cumulant effective-trial hierarchy for Poisson-binomial laws

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `52c1e02c0599c42040308db9e74b877e1cd8bcbb`  
**Audited current source tree:** `52c1e02c0599c42040308db9e74b877e1cd8bcbb`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path has no changes from the assigned inventory snapshot, so the audited tree equals the assigned source tree. GitHub was used only as read-only evidence. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. Writing w_i=v_i/V and p*=Σw_i p_i gives κ3/V=1-2p* and therefore N3=V/[p*(1-p*)]. Also A=Σv_i^2 gives V-κ4=6A and N4=V^2/A. Weighted variance of p_i yields p*(1-p*)≥A/V, hence N3≤N4, while Cauchy–Schwarz gives N4≤r; p*(1-p*)≤1/4 gives 4V≤N3. The stated equality cases follow from equality in weighted variance and Cauchy–Schwarz. The joint cumulant inequality, fixed-(n,V) skew bound, packed-variance fourth-cumulant interval, and Lyapunov numerator identity all follow algebraically. I independently tested the hierarchy on 10,000 random Bernoulli parameter vectors and re-derived the endpoint optimization of Σv_i^2.

## Originality — PASSED

PASS, narrowly scoped. Bernoulli cumulant formulas, Hoeffding-style homogenization, effective participation ratios, and the three-parameter shifted-binomial moment-matching parameters are prior art; in particular the submitted N3 is the real trial count n* in Peköz–Röllin–Čekanavičius–Shwartz. The claimed contribution is the exact hierarchy linking that third-cumulant count to the fourth-cumulant participation count, its equality classification, and the resulting sharp joint/skewness/kurtosis/Lyapunov envelopes. Targeted searches of Poisson-binomial surveys, Bernoulli-sum moment work, and shifted-binomial approximation literature did not locate these exact inequalities. The result is elementary enough that terminology-equivalent older moment inequalities remain a residual risk, so the originality claim is deliberately narrow.

## Scientific value — PASSED

PASS. The hierarchy extracts representation-level information (a lower bound on the number of active Bernoulli trials) from only the first four cumulants and organizes several sharp finite-n moment constraints in one framework. The exact Berry–Esseen numerator range is also directly useful. The contribution is a compact moment-geometry theorem rather than a new approximation method, and the record accurately limits its scope.

## Independent checks

- Re-derived N3 and N4 from κ3,κ4 using variance weights.
- Reproved N3≤N4 by weighted variance and N4≤r by Cauchy–Schwarz, including all equality cases.
- Re-derived 3κ3^2≤V^2+2Vκ4 and the sharp fixed-(n,V) skew bound.
- Checked the convex packing extremizer for Σv_i^2 with 0≤v_i≤1/4 and fixed sum V.
- Verified L3=V-2Σv_i^2=(2V+κ4)/3 and the fixed-(n,V) range.
- Random testing on 10,000 parameter vectors found no hierarchy violation beyond floating-point roundoff.
- Compared with Peköz et al. shifted-binomial matching, Tang–Tang's Poisson-binomial survey and Bernoulli-sum moment literature; no exact hierarchy was located.
- GitHub compare found no changes under the assigned path; both UTC-dated audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The hierarchy assumes independent Bernoulli summands and does not characterize the full feasible cumulant region.
- N3's moment-matching interpretation is prior work; only the hierarchy and exact envelopes receive novelty credit.
- Equivalent inequalities may exist under older moment-problem terminology despite the targeted searches.

## Evidence and references

- https://doi.org/10.1214/AOMS/1177728178
- https://arxiv.org/abs/0906.2855
- https://doi.org/10.1214/22-STS852
- https://arxiv.org/abs/2110.02363
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/poisson-binomial-cumulant-effective-trial-hierarchy--c64930932dda

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
