# Independent Audit — Strong cleanness descends from M2 to T2 over local rings

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `b74492af30f1b54a31533cc10bf7b3ec1c2d1c26`  
**Audited current source tree:** `b74492af30f1b54a31533cc10bf7b3ec1c2d1c26`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment snapshot. GitHub was used only as read-only evidence. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. After excluding the trivial unit and 1-minus-unit cases, an upper triangular matrix over a local ring has one diagonal entry in J(R) and the other in 1+J(R). From a strong-clean decomposition in M2(R), reduction modulo J makes Abar and Ebar commuting idempotents with Abar-Ebar invertible; (p-e)(p+e-1)=0 therefore forces Ebar=1-Abar. In either residue case, ker(E) or im(E) is a rank-one free invariant right module whose generator can be normalized to (t,1)^T. A-invariance yields at+b=tc, exactly the equation needed to build an upper-triangular commuting idempotent F, and A-F then has unit diagonal. I independently exhaustively checked all 64 upper-triangular matrices over Z/4Z: every matrix strongly clean in M2(Z/4Z) was strongly clean in T2(Z/4Z), with no counterexample.

## Originality — PASSED

PASS, narrowly scoped. Borooah–Diesl–Dorsey's 2008 paper explicitly poses the elementwise descent question as Problem 49 and the ring-level version as Problem 48. Later T2/local-ring criteria and Tang–Zhou embedding results impose additional hypotheses such as bleaching or address different directions. Targeted searches did not locate an affirmative arbitrary-local-ring n=2 solution to Problem 49. The submitted theorem therefore resolves the published open question in dimension two; no novelty is claimed for existing T2 strong-cleanness criteria or M2 local-ring characterizations.

## Scientific value — PASSED

PASS. The result answers a concrete published open problem in the first nontrivial matrix size and does so for noncommutative local rings without bleaching, completeness, or finiteness assumptions. The invariant-line proof is short but structurally useful, showing why a full-matrix strong-clean idempotent can be replaced by a triangular one in dimension two.

## Independent checks

- Read the accessible full Section 7 of Borooah–Diesl–Dorsey (2008), which states Problems 48 and 49 exactly.
- Re-derived the reduction-mod-J idempotent identity and the rank-one invariant-module construction in both residue cases.
- Exhaustively enumerated M2(Z/4Z) and T2(Z/4Z): among all 64 upper-triangular matrices, the strong-clean statuses agreed exactly.
- Compared with Yang–Zhou arXiv:0805.0359 and targeted later triangular/bleached-local-ring literature; no covering arbitrary-local n=2 descent theorem was located.
- Searched the current SCOPE repository for a duplicate solution to Problems 48/49; no overlap was found.
- Verified the current main tree SHA exactly equals the assigned source-tree SHA; the dated audit pair is absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The theorem is specific to 2×2 matrices and does not settle Problems 48/49 for n>=3.
- The finite Z/4Z enumeration is corroborative only; the proof handles arbitrary local rings.
- Later ring-theory literature is broad, so a differently phrased n=2 observation remains a residual priority risk despite targeted searches.

## Evidence and references

- https://doi.org/10.1016/j.jpaa.2007.05.020
- https://doi.org/10.1016/j.jalgebra.2006.10.029
- https://arxiv.org/abs/0805.0359
- https://doi.org/10.1080/03081087.2016.1211083
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/strong-cleanness-descends-to-t2-over-local-rings--72f274369f61

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
