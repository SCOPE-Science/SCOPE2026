# Independent Audit — 2026/09/11/075

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `7ed7469a97724c368017a811d258b53e3b90d044`  
**Audited current source tree:** `7ed7469a97724c368017a811d258b53e3b90d044`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** repaired

The current `main` record tree matches the assignment tree SHA.

## Correctness

PASS AFTER REPAIR. Direct recomputation confirms both printed matrices are Latin, have 100 distinct superimposed pairs, satisfy SIG^3=id with profile 3+3+3+1, and are simultaneously equivariant at every cell. The prior word “semiregular” was inaccurate because 9 is fixed, and referenced verifier artifacts are absent; the repair removes both defects.

## Originality

SUPPORTED, NARROW. Egan–Wanless is exhaustive only through order 9; Gill–Wanless uses a different non-trivial-relation restriction at order 10. A targeted search found no prior statement of this exact witness/profile. Search absence is not proof of priority, so the repair removes stronger priority language.

## Scientific value

MEANINGFUL EXACT WITNESS. A concrete OA(4,10)/orthogonal pair with simultaneous order-3 coordinate symmetry is reusable in the difficult order-10 MOLS landscape as a symmetry-constrained seed/data point.

## Independent checks

- direct Latin row/column checks
- 100/100 orthogonality
- SIG order/profile and all-cell equivariance
- record tree unchanged from assignment

## Limitations

- No exhaustive order-10 isotopism/autotopism census was performed.
- Missing verifier artifacts were not treated as read or executed.
- The repair removes “semiregular” because the action fixes 9.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/11/075
- https://arxiv.org/abs/1406.3681
- https://arxiv.org/abs/2204.10996

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
