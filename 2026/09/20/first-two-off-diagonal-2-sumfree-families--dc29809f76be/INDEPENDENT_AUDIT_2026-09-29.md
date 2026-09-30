# Independent Audit — Exact periodicity of the first two off-diagonal greedy 2-sumfree families

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `f83d5b314eb511e3341b0df7641b6c81b6dab615`  
**Audited current source tree:** `f83d5b314eb511e3341b0df7641b6c81b6dab615`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path is unchanged from the dispatcher's source-check commit, so the audited tree equals the assigned source tree. GitHub was used read-only. The UTC-dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. The proposed residue description satisfies both directions of the greedy criterion. Before f+(2f+delta), all values in the stated initial interval are admitted, and the next f-term gap is blocked by adding f. In the tail, the three modular sumsets E hat+ E, E+R, and R+R are disjoint from R for both delta=1 and 2, so no proposed term is a forbidden sum. The listed witness intervals cover every omitted residue in one full tail period, and shifting a tail summand by multiples of M propagates the witnesses to all later periods. The difference word therefore has the claimed length and sum; its unique large entry proves minimal period, while the transition gap not occurring in the cyclic word proves the minimal preperiod. I independently regenerated the greedy sequence for every f=5,...,100 and delta in {1,2} through ten full periods and found zero discrepancies.

## Originality — PASS

PASS, with a disclosed historical residual. Van Berkel--Bosma's full 2026 paper proves the region g<=2f-1 and the diagonal g=2f, but presents the beyond-diagonal period/preperiod formulas as conjectures supported by computation. For d=f+1 and f+2 their conjectured period data agree with the submitted formulas, so the contribution is the first uniform proof of those two off-diagonal lines, not discovery of their numerical pattern. The foundational Queneau 1972 article could not be lawfully retrieved because institutional access stopped at human verification; it is not claimed as read. The recent authors' historical treatment and targeted searches did not identify a prior variable-f theorem for these two lines, so the remaining Queneau risk is recorded rather than hidden.

## Scientific value — PASS

PASS. The theorem converts two infinite slices of a current all-parameter periodicity conjecture from computation to exact proof, including closed residue sets, minimal period/preperiod and density. It is a meaningful incremental advance because the source paper explicitly emphasizes the difficulty of finding a general proof beyond the diagonal.

## Independent checks

- Read the relevant portions of van Berkel--Bosma arXiv:2609.18522 in full; Conjecture 5 covers all periods, while the confirmed theorems stop at g<=2f-1 and g=2f.
- Recomputed the modular sumset exclusions and checked the witness-propagation mechanism for both offsets.
- Independently generated the greedy construction for all f=5,...,100 and both offsets through ten periods with no mismatch.
- Checked the minimal-period and minimal-preperiod arguments against the explicit difference blocks.
- Open-access searches for Queneau 1972 did not yield full text; authorized institutional retrieval reached a human-verification gate, so no inaccessible content was treated as read.
- Targeted web and repository searches found no earlier infinite theorem for S_{f,2f+1} or S_{f,2f+2}.
- GitHub comparison found no changes under the assigned record path; both UTC-dated audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- Queneau's 1972 full article remained inaccessible after open and authorized retrieval attempts and is an explicit residual originality risk.
- The theorem covers only f>=5 and offsets delta=1,2; it does not settle larger offsets or the global periodicity conjecture.
- The independent finite recomputation is corroborative; correctness rests on the residue/witness proof.

## Evidence and references

- https://arxiv.org/abs/2609.18522
- https://arxiv.org/abs/2609.16843
- https://doi.org/10.1016/0097-3165(72)90083-0
- https://doi.org/10.1080/00029890.1992.11995911
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/first-two-off-diagonal-2-sumfree-families--dc29809f76be

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
