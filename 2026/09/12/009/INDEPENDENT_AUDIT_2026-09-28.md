# Independent Audit — 2026/09/12/009

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `e3ecab2655525933e7d12639d4cb83c73295190e`  
**Audited current source tree:** `e3ecab2655525933e7d12639d4cb83c73295190e`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** repaired

The current `main` record tree matches the assigned tree SHA.

## Correctness

PASS AFTER NOTATION/SCOPE REPAIR. The audit independently reproduces the constant-cocycle equations, the everywhere-rank-two family Pi+t d01, and the degree<=2 linear algebra (90 unknowns, rank 56, cocycle dimension 34; affine coboundary rank 16; d01 essential). The original definition dx_i∧dx_j was the wrong tensor type and is corrected to ∂_i∧∂_j. The radial/single-component obstruction claims are consistent with the exact certificates.

## Originality

SUPPORTED, NARROW. General Poisson normal-form, Nambu-cohomology and log-symplectic references are adjacent but do not state this exact constant-cocycle/radial-cutoff/finite-slice package for the quadratic hyperbolic–hyperbolic germ.

## Scientific value

MEANINGFUL PARTIAL OBSTRUCTION PACKAGE. The explicit global jump plus two failed localization ansätze and a finite cohomology slice are useful guidance for the open compact-support problem. The repair removes the false claim that the entire linearized localization problem has been decided.

## Independent checks

- direct symbolic constant Schouten-bracket equations
- degree<=2 cocycle matrix rank 56 / nullity 34
- affine coboundary rank 16 and augmented d01 rank 17
- current main tree equals assigned tree

## Limitations

- General nonradial multicomponent compactly supported cocycles are not ruled out.
- The nonlinear deformation/persistence problem remains open.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/12/009
- https://link.springer.com/book/10.1007/b137493
- https://www.kurims.kyoto-u.ac.jp/~prims/pdf/42-2/42-2-11.pdf
- https://doi.org/10.1016/j.aim.2014.07.032

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
