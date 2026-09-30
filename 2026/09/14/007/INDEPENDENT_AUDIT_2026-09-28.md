    # Independent audit — 2026/09/14/007

    **Audit date:** 2026-09-28 (UTC)  
    **Repository:** `SCOPE-Science/SCOPE2026`  
    **Assigned source tree:** `bb5a366c3d6585e8e0bcda1189eb7724cfecf9b2`  
    **Audited current source tree:** `bb5a366c3d6585e8e0bcda1189eb7724cfecf9b2`  
    **Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
    **Disposition:** repaired

    The current `main` tree for this record matches the assignment tree SHA.

    ## Correctness

    **PASSED** — PASS AFTER REPAIR. Independent symbolic differentiation reproduces H_t' and H_t'', and the cubic discriminant equals 12[9x^4+(3t^2-36t+27)x^2+(3-2t)^3]. The atom mass is 1-2t/3, so atoms disappear at t=3/2. At the unique real cubic degeneracy (t,w)=(3/2,0), H~ -3w^3 and G_mu~1/(3w), giving the stated 3^(5/6)/(6 pi)|x|^(-1/3) pole rather than a +1/3 zero. The committed verifier paths were wrong and are repaired.

    ## Originality

    **PASSED** — SUPPORTED, NARROW. Huang supplies the general free-power support/density machinery and Moreillon classifies generic local singular behavior, but the checked statements do not give this exact three-atom global t-classification, critical time 3/2, and pole constant. The record is retained only as that explicit solvable example, without a broad priority claim.

    ## Scientific value

    **PASSED** — USEFUL EXACT MODEL. The example cleanly distinguishes a cubic degeneracy that produces an inverse-cubic density pole from the cubic-root zeros sought by the target, while giving the complete support transition across t=3/2.

    ## Independent checks

    - rederived H_t', H_t'' and the cubic discriminant symbolically
- checked the atom threshold and mass formula
- rederived the t=3/2 cubic-pole constant
- verified committed verifier files live under artifacts/
- confirmed current and assigned tree SHAs agree

    ## Limitations

    - The result is specific to the symmetric three-point law.
- Square-root boundary conclusions use standard free-convolution boundary regularity in addition to the explicit cubic algebra.
- Targeted search is not an exhaustive priority proof.
- Open-access sources were sufficient; Oxford Download was not needed.

    ## Evidence and references

    - https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/007
- https://arxiv.org/abs/1205.5542
- https://arxiv.org/abs/2209.15607
- https://arxiv.org/abs/1804.11199

    This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
