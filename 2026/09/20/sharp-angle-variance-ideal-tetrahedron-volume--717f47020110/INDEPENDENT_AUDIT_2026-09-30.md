# Independent Audit — Sharp angle-variance profile for ideal tetrahedron volume

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `7f143e5255ef9b626c690d75fb6867e5428b42fc`  
**Audited current source tree:** `7f143e5255ef9b626c690d75fb6867e5428b42fc`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path has no changes from the assignment snapshot, so the audited tree equals the assigned source tree. GitHub was used read-only. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. The fixed-Q reduction is correct. At an interior constrained extremum, the Lagrange equation Λ'(x)=λ+2μ(x-π/3) has at most two roots because its left-minus-linear second derivative is Λ'''(x)=csc^2 x>0; hence a maximizer has two equal angles. Writing the isosceles triple as (2s,π/2-s,π/2-s), one gets V=2Λ(s) and Q=6(s-π/6)^2. The plus branch has larger volume because the derivative of Λ(π/6+r)-Λ(π/6-r) is -log(1-4 sin^2 r)>0. For the global coefficient, f(r)=Λ(π/6)-Λ(π/6+r) has nonnegative decreasing f''=cot(π/6+r), which makes f(r)/r^2 decreasing; the boundary r=π/3 gives exactly 3v3/(2π^2). Independent random tests of 3,000 angle triples found no violation of the exact profile, and the deficit/Q ratio approached the sharp constant from above near degeneration.

## Originality — PASS

PASS, narrowly scoped. The Lobachevsky volume formula, strict concavity, and the fact that the regular ideal tetrahedron uniquely maximizes volume are classical (Milnor, Thurston, Haagerup–Munkholm). Targeted searches did not locate the submitted exact maximum-volume envelope at fixed squared dihedral-angle deviation Q, its unique isosceles equality branch, or the globally optimal variance coefficient 3v3/(2π^2). No novelty is assigned to the classical volume formula or ordinary maximal-volume theorem.

## Scientific value — PASS

PASS. The theorem upgrades qualitative near-maximal-volume rigidity to a closed global stability profile with a best possible coefficient and full equality/degeneration description. The distinction between the stronger local coefficient 1/(2√3) and the smaller globally sharp constant forced by boundary degeneration is mathematically informative and directly reusable in ideal-tetrahedron estimates.

## Independent checks

- Re-derived the Lagrange-multiplier two-value reduction and the exact isosceles parametrization.
- Rechecked the Lobachevsky duplication identity used to reduce the isosceles volume to 2Λ(s).
- Verified analytically that the plus stationary branch dominates the minus branch and that the latter disappears at the correct boundary.
- Reproved monotonicity of f(r)/r^2 from decreasing f'' and recovered the sharp endpoint constant.
- Numerically tested 3,000 random angle triples: no violation of the exact fixed-Q envelope was found.
- Compared against classical ideal-simplex maximal-volume literature; no fixed-Q variance profile was located.
- GitHub comparison found no changes under the assigned record path since the assignment snapshot; both 2026-09-30 audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The result is specific to nondegenerate ideal tetrahedra in H^3 and to Euclidean squared distance in the three dihedral angles.
- The proof is elementary once the classical Lobachevsky formula is used, so an equivalent special-function inequality under different terminology remains a residual priority risk.
- No claim is made for finite, hyperideal, generalized, or higher-dimensional simplices.

## Evidence and references

- https://doi.org/10.1007/BF02392865
- https://doi.org/10.1090/S0273-0979-1982-14958-8
- https://library.slmath.org/books/gt3m/PDF/6.pdf
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/sharp-angle-variance-ideal-tetrahedron-volume--717f47020110

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
