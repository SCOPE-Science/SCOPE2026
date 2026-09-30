# Independent Audit — Pairwise independence does not preserve Lorden's mean-overshoot bound

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `9cd59e373277d9675fea995ab4c989154e224734`  
**Audited current source tree:** `9cd59e373277d9675fea995ab4c989154e224734`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path has no changes from the assigned inventory snapshot, so the audited tree equals the assigned source tree. GitHub was used only as read-only evidence. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. The finite-field construction is correct. For distinct i,j, (U,V)↦(U+iV,U+jV) is bijective on F_q^2, so the first q indicators are pairwise independent Bernoulli(1/q); adjoining independent Bernoulli coordinates preserves pairwise independence and the common marginal. At b=q-1 the crossing is forced within the first q steps. Splitting the q^2 outcomes into (U,V)=(0,0), V=0 with U≠0, and V≠0 with the unique hit J gives E R_b=3q/2-1+3/(2q). The marginal moments give E X^2/E X=(4q^2+q-1)/(3q-1), and subtraction is exactly (q-1)(q^2-10q+3)/(2q(3q-1)), positive for q≥11. I independently recomputed the exact fractions at q=11,13,17,101 and recovered the claimed formula and 9/8 limiting ratio.

## Originality — PASSED

PASS, narrowly scoped. Lorden's classical theorem is for independent renewal increments, and recent dependent-renewal extensions impose substantial comparison/renewal-measure hypotheses rather than mere pairwise independence. Explicit failures of other limit theorems under pairwise independence are known, and finite-field pairwise-independent constructions are standard; neither is credited as new. Targeted searches did not locate an explicit bounded positive identically distributed pairwise-independent sequence violating the original marginal-only Lorden constant. The novelty credited here is only that source-specific first-passage counterexample and exact violation calculation.

## Scientific value — PASSED

PASS. The construction cleanly separates a first-passage inequality from results controlled by one- and two-dimensional marginals: pairwise independence and finite second moment are insufficient even for a two-point positive marginal. The exact factor tends to 9/8, so the example quantifies rather than merely asserts the failure. It does not purport to determine the optimal bound under pairwise independence or stronger dependence conditions.

## Independent checks

- Re-derived pairwise independence from the invertible 2×2 finite-field linear map.
- Recomputed the stopping/overshoot in all three (U,V) cases and the exact expectation.
- Independently evaluated the exact difference formula at q=11,13,17,101.
- Compared with Lorden's 1970 independent-increment bound and Kalimulina–Zverkina's 2026 dependent-renewal extension, which requires additional comparison and renewal-measure domination hypotheses.
- Targeted searches for pairwise-independent Lorden/overshoot counterexamples found no covering result; generic pairwise-independent CLT counterexamples were treated only as background.
- GitHub compare from the inventory snapshot to current main showed no file changes under the assigned path; both INDEPENDENT_AUDIT_2026-09-30 files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The sequence is not claimed to be strictly stationary.
- The result disproves the original marginal-only Lorden constant under pairwise independence; it does not identify the best pairwise-independent constant.
- The finite-field construction itself is classical and receives no originality credit.

## Evidence and references

- https://doi.org/10.1214/aoms/1177697092
- https://arxiv.org/abs/2501.18329
- https://doi.org/10.1016/j.jmaa.2021.124982
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/pairwise-independent-lorden-overshoot-counterexample--9d2c1e07f7b4

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
