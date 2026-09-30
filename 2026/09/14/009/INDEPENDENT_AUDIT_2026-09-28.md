    # Independent audit — 2026/09/14/009

    **Audit date:** 2026-09-28 (UTC)  
    **Repository:** `SCOPE-Science/SCOPE2026`  
    **Assigned source tree:** `6905c728854bf5e7647eb51a24b0399bceae871a`  
    **Audited current source tree:** `6905c728854bf5e7647eb51a24b0399bceae871a`  
    **Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
    **Disposition:** repaired

    The current `main` tree for this record matches the assignment tree SHA.

    ## Correctness

    **PASSED** — PASS AFTER REPAIR. Independent exact symbolic expansion reproduces F1=±63/4, F2=-81/32, G0=-3√3/2, G1=±183√3/8, u1=±7√3/2, u2=447√3/8, K2=111√3/4 and K3=±855√3/2. Thus the two symmetric reduced-action critical values differ by -855√3 epsilon^3+O(epsilon^4). The original prose overstated the twist-map implication as if all period-3 orbits globally had common action. The repair uses the correct necessary condition: a persisting 1/3 resonant invariant curve forces the resonant reduced phase action/high-order obstruction to be constant. Distinct symmetric critical values prove nonconstancy. Artifact paths are also repaired.

    ## Originality

    **PASSED** — SUPPORTED, NARROW. Koudjinan–Ramírez-Ros provides the necessary-and-sufficient high-order persistence framework and explicitly notes that checking the first nonzero resonant harmonic at the next order is a challenge. The checked paper does not evaluate this polar n=5,q=3 coefficient. The retained contribution is exactly the explicit 855√3 third-order obstruction, not the general perturbation theory.

    ## Scientific value

    **PASSED** — MEANINGFUL EXPLICIT OBSTRUCTION. The calculation resolves a case where first-order resonance vanishes and identifies the first nonzero barrier coefficient, providing a concrete test of the new high-order theory.

    ## Independent checks

    - rederived the exact chord expansion and Lyapunov-Schmidt coefficients
- recomputed K2 and K3 for both reflection axes
- checked the logical use of reduced-action nonconstancy against the high-order persistence theorem
- verified committed scripts live under artifacts/
- confirmed current and assigned tree SHAs agree

    ## Limitations

    - The result is local for sufficiently small nonzero epsilon.
- The exact-twist/high-order persistence criterion is cited rather than reproved.
- No claim is made about unrelated period-3 orbits away from the resonant reduction.
- Targeted search is not an exhaustive priority proof.
- Open-access full text was available; Oxford Download was not needed.

    ## Evidence and references

    - https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/009
- https://arxiv.org/abs/2503.07488

    This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
