# Independent Audit — Exact calibration of the critical dyadic square-function sharpness example

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `1bf603acd3a6b1155a5da2a45ca2e739d90c9ada`  
**Audited current source tree:** `1bf603acd3a6b1155a5da2a45ca2e739d90c9ada`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment tree SHA. GitHub was used read-only as evidence, and the dated independent-audit files were absent when this guarded plan was prepared.

## Correctness — PASSED

PASS. The full Osekowski v1 text was lawfully retrieved after direct full-text access failed, and the submitted exact bookkeeping agrees with its construction. The state products in Phase I and Phase II are maximized at the claimed terminal Phase-I state, giving [w_N]_{A_2^d}=1+A/alpha. The ordinary-terminal weighted second moment simplifies exactly to E_N=y_N^2/[A(A+alpha)], continuation multiplies weighted mass by r_N=p_N lambda_N, and the final split contributes exactly 4 r_N^A alpha^{-1} gamma_N. The source's conditional iid variables have normalized sum converging to 3/8, so every fixed threshold theta<3/8 has conditional probability tending to one; preserving the conditional w-average gives the claimed e^{-4} tail mass. The asymptotic expansion alpha=1/2+3/A+O(A^{-2}), r=1-4/A+O(A^{-2}) then yields the norm limit and the normalized constant 0.1065624665....

## Originality — PASSED

PASS, narrowly scoped. Osekowski proves sharpness of the logarithmic factor using the same martingale example but intentionally uses coarse estimates: [w] between A/2 and 6A, ||f||^2<=8A, a 1/3 tail probability, and the explicit lower constant e^{-2}/48. The audited record extracts the exact dyadic A2 characteristic, exact input norm, full limiting tail event, and a substantially stronger explicit normalized lower constant from that example. Searches did not locate this exact calibration elsewhere. The sharp order itself and the underlying example are not credited as new.

## Scientific value — PASSED

PASS. Exact calibration of a canonical sharpness example is a meaningful quantitative refinement: it identifies the actual extremal state and asymptotic energy, removes deliberately coarse losses in the source proof, and improves the certified universal lower constant by a large factor. The contribution is limited to calibration of one example rather than a new upper bound or optimal constant theorem, but it clears the value threshold.

## Independent checks

- Read Osekowski v1 in full via authorized institutional retrieval after direct arXiv/OA full-text access failed.
- Matched the submitted alpha, beta, gamma, exceptional probability, continuation scaling, terminal values, and iid xi distribution to the source construction.
- Re-derived the exact one-block weighted second moment and final-split term.
- Checked the Phase-I/Phase-II state-product maximum analytically and inspected the repository numerical calibration artifact.
- Re-derived r_N^A->e^{-4}, the normalized input-energy limit 4(1-e^{-4})/9, and the final weak-L2 constant.
- Verified the current main tree SHA equals the assigned source tree and that the dated audit-marker files are absent.

## Limitations

- The result calibrates Osekowski's specific dyadic martingale example and does not claim the displayed numerical lower bound is the optimal universal constant.
- The limiting tail statement imports the source paper's iid-sum convergence rather than reproving its characteristic-function argument from first principles.
- No nondyadic or continuous Littlewood--Paley analogue is established.

## Evidence and references

- https://arxiv.org/abs/2609.14430
- https://doi.org/10.1112/blms/bdv090
- https://arxiv.org/abs/1211.4219
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/calibrated-dyadic-square-function-sharpness--76b65c21f30b

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
