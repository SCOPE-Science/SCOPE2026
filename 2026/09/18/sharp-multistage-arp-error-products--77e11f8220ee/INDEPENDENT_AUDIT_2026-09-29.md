# Independent Audit — 2026-09-29

**Record:** `2026/09/18/sharp-multistage-arp-error-products--77e11f8220ee`  
**Title:** Worst-case sharpness of multistage adaptive randomized pivoting  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `0decfd9030517aae01f2875ddc5bd39672a1f9f7`  
**Disposition:** **PASSED**

## Independent checks

- Algebraically normalized every conditional DPP law in the codimension-one construction.
- Checked that zero-padding old basis columns preserves every earlier stage law.
- Checked order of limits: for fixed staged distribution, delta to zero is a finite sum; stage epsilons can then be selected successively.

## Three-axis assessment

- **Correctness — PASS**: The codimension-one projection-DPP calculation is correct. For K=I-zz^T, a size-d sample omits j with probability z_j^2, and after conditioning on retained indices the remaining omission weights renormalize over the unselected coordinates. This reproduces the exact two-stage mean (k+1)(p+1)/(1+kp epsilon^2), and the zero-padded induction multiplies the preceding expectation by k_r+1 in the epsilon_r to zero limit. The orthogonal-CSS transfer also checks: the selected-principal-minor height identity gives error ratio 1/(z_j^2+delta^2(1-z_j^2)), so finite summation converges to the oblique mean as delta tends to zero.
- **Originality — PASS**: The current Grigori--Xue preprint was found as arXiv v1 and publicly advertises expected-error guarantees for conditional-DPP/MSARP, not full unconditional multistage sharpness. Targeted searches found no public source stating the arbitrary-stage product sharpness, the orthogonal-CSS transfer, or the 2^d/(d+1) staged-versus-one-shot separation. One-shot ARP/volume-sampling literature supplies the d+1 baseline but not this nested construction.
- **Scientific Value — PASS**: The result resolves whether the multiplicative MSARP guarantee is proof slack: it is a genuine worst-case supremum, even for the actual orthogonal projection objective. The rare-event construction also explains why benign experiments can coexist with an exponentially worse staged worst case.

## Findings

- Current source tree exactly matches the assigned SHA.
- Independently rederived the conditional omission law and the two-stage expected-error formula.
- Independently checked the arbitrary-stage induction and the orthogonal-CSS Gram-determinant ratio.
- Fresh web searches found the primary preprint as v1 and no public matching full-product sharpness result.

## Sources compared

- Grigori and Xue, Incremental Column Subset Selection via Conditional Determinantal Point Processes: https://arxiv.org/abs/2609.20556 — Primary MSARP source; current public listing is v1 and states expected Frobenius guarantees.
- Cortinovis and Kressner, Adaptive Randomized Pivoting for Column Subset Selection, DEIM, and Low-Rank Approximation: https://doi.org/10.1137/24M1719189 — One-shot ARP comparison literature; does not address nested conditional-DPP product sharpness.
- Epperly, Adaptive randomized pivoting and volume sampling: https://arxiv.org/abs/2510.02513 — Related one-shot ARP/volume-sampling analysis; no matching multistage sharpness construction located.

## Limitations

- Worst-case sharpness is a supremum approached by imbalanced leverage scores and does not characterize typical data.
- The orthogonal-CSS mean sharpness uses an additional delta-to-zero limit; the explicit variance divergence is for the oblique surrogate.
- The source preprint is extremely recent, so unindexed simultaneous work remains a residual originality risk.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
