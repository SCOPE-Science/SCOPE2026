# Independent Audit — Exact total-variation leakage of uniform low-rank factor masks

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `865544536ca1a06dceb9a9cb87837eb0b2479f41`  
**Audited current source tree:** `865544536ca1a06dceb9a9cb87837eb0b2479f41`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence, and the dated independent-audit files were absent when this guarded plan was prepared.

## Correctness — PASS

PASS. Conditioning on rank(U)=s gives the submitted rank-d likelihood by counting s-dimensional row spaces containing row(A) and then using that a full-row-rank U makes UV uniform on matrices whose rows lie in row(U). The likelihood depends only on d=rank(A) and strictly decreases with d. At full row rank d=k only s=k contributes, giving P(M=A)=p_{k,r}(q)q^{-kn}<q^{-kn}; for every d<k the s=k-1 contribution alone has likelihood ratio q^{n-r}p_{k-1,r}(q)>1. Hence the sign of P-Q is exactly rank-deficient versus full-row-rank, and summing the uniform deficit over full-row-rank matrices yields d_TV=p_{k,n}(q)(1-p_{k,r}(q)). Independent exhaustive computations over small prime fields reproduce the exact formula and the constant-on-rank likelihoods.

## Originality — PASS

PASS, narrowly scoped. Cohen--D'Oliveira--Sprintson's September 2026 paper proves approximate row/column individual security for low-rank factor masks, with the published total-variation guarantee bounded by 1-p_{k,r}(q) (and then by q^{k-r}/(q-1)); its full text does not state the exact ambient-dimension factor p_{k,n}(q), the rank-by-rank likelihood formula, or the iff leakage-vanishing criterion. Searches of finite-field random-matrix rank literature found sharp rank-distribution TV results but no equivalent exact product-mask-to-uniform identity. Novelty is credited only to this exact leakage calculation and its masking consequence.

## Scientific value — PASS

PASS. The result replaces the source's sufficient privacy bound by an exact leakage formula, identifies precisely where the signed mass discrepancy lies, and gives the sharp fixed-field condition r-k→∞. This materially calibrates the privacy/complexity tradeoff of the motivating masking scheme rather than merely tightening a constant.

## Independent checks

- Read the complete lawful-open 5-page source text after direct arXiv HTML access failed; Theorem 3 supplies only the approximate individual-security upper bound used for comparison.
- Independently derived the conditional law given rank(U)=s and the Gaussian-binomial count of admissible row spaces.
- Checked the strict deficient/full-rank sign split, including the edge case k=1.
- Independently exhaustively enumerated small cases (q,k,r,n)=(2,1,1,2),(2,2,2,3),(3,1,2,3); each exactly matched the TV formula and rank likelihoods.
- Searched targeted finite-field random-matrix/TV literature; Fulman--Goldstein concerns rank-distribution approximation rather than the submitted product-mask identity.
- Verified the assigned record tree is unchanged from the dispatcher source-check commit to current main and that the dated audit markers are absent.

## Limitations

- The theorem concerns uniform independent factor masks and comparison with the fully uniform k-by-n matrix law; it is not an exact leakage formula for uniform rank-ball masks or arbitrary factor distributions.
- The masking interpretation is for the row/column marginal considered in the source's individual-security reduction.
- The motivating preprint is very recent, so simultaneous unindexed follow-up work remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.18876
- https://doi.org/10.1214/13-AOP889
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/exact-tv-low-rank-factor-masks--defb12bcd300

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
