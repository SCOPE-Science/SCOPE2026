    # Independent audit — 2026/09/14/010

    **Audit date:** 2026-09-28 (UTC)  
    **Repository:** `SCOPE-Science/SCOPE2026`  
    **Assigned source tree:** `33f137a09cda5d610c6b3567ac0ca9abd2f47c73`  
    **Audited current source tree:** `33f137a09cda5d610c6b3567ac0ca9abd2f47c73`  
    **Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
    **Disposition:** passed

    The current `main` tree for this record matches the assignment tree SHA.

    ## Correctness

    **PASSED** — PASS. On the imaginary axis, symmetry gives G_mu(iv)=-iA(v) with A(v)>0 and H_t(iv)=i[tv-(t-1)/A(v)]. From 1<=|x|<=2 one gets v/(4+v^2)<=A(v)<=v/2. These bounds trap the subordination solution for z=i eta, 0<eta<=1, in a compact interval bounded away from v=0 and hence give a uniform positive lower bound on -Im G_{mu^{boxplus t}}(i eta). If 0 were outside the support, the Stieltjes transform imaginary part would instead tend to 0. Thus 0 belongs to the support for every t>1. A symmetric support consisting of exactly two disjoint intervals cannot contain 0, so the proposed delayed 2-to-1 regime is disproved.

    ## Originality

    **PASSED** — SUPPORTED, NARROW. Huang supplies the general subordination/support theory and proves monotonicity of the number of support components for t>1, but the checked source does not state this immediate central-support conclusion for the symmetric two-box uniform law. The record claims only this explicit counterexample to the posed merger scenario; search non-detection is not a priority proof.

    ## Scientific value

    **PASSED** — USEFUL TARGET DISPROOF. The argument identifies a sharp qualitative mechanism at t=1+: mass/support appears at the symmetry center immediately, invalidating the proposed two-interval phase before any later merger analysis. It is elementary once formulated but directly resolves the stated support-topology question.

    ## Independent checks

    - rederived the imaginary-axis subordination reduction
- verified both Stieltjes bounds and the resulting uniform v-trap analytically
- checked the support contradiction via distance from zero
- checked the symmetry/parity obstruction for exactly two disjoint intervals
- confirmed current and assigned tree SHAs agree

    ## Limitations

    - The result disproves the proposed two-interval-to-one-interval scenario but does not determine all later support edges or merger times.
- The exploratory 2→3→1 remark in the original limitations is not treated as certified.
- Targeted literature comparison cannot establish exhaustive priority.
- Open-access sources were sufficient; Oxford Download was not needed.

    ## Evidence and references

    - https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/010
- https://arxiv.org/abs/1205.5542
- https://arxiv.org/abs/2408.06573

    This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
