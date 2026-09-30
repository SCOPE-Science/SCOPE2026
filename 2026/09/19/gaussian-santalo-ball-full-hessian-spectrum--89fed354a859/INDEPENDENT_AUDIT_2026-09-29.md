    # Independent audit — 2026-09-29

    **Record:** `2026/09/19/gaussian-santalo-ball-full-hessian-spectrum--89fed354a859`  
    **Title:** The full support-function Hessian of the uncentered Gaussian Santaló product  
    **Repository:** `SCOPE-Science/SCOPE2026`  
    **Audited tree:** `6748e2059dc616947b7c4f2e52fabeccadb9960b`  
    **Disposition:** **REPAIRED**

    ## Correctness

    **PASS_AFTER_REPAIR** — The retained critical-translation fourth-order formula is correct. At q=(n+1)/2, independent expansion of the shifted-ball factor gives 1-R(n+1)t^2/(4n)+R(n+1)^2(n+3)t^4/[64n(n+2)]+O(t^6); expanding the polar radial factor F((1+tY)^-1) gives the opposite quadratic term and quartic coefficient R(n+1)(n^2-4n-37)/[64n(n+2)]. Their product yields the stated C_n. The radial identity R=n-q I_2/I_0>(n-1)/2 makes the bracket in C_n larger than 2n^2+16n-2, so C_n>0.

    ## Originality

    **PASS_AFTER_REPAIR** — The filed record's full-Hessian claim is not original within SCOPE: records `gaussian-volume-product-hessian-spectrum--714d3bdc8013` (17 September) and `gaussian-volume-product-hessian-instability-index--adb76edfac12` (18 September) already contain the complete second variation and spherical-harmonic sign classification. The repair credits those results and retains only the negative fourth-order coefficient along the critical translation family. The motivating Artstein-Avidan–Fradelizi–Wyczesany preprint supplies the translated-ball quadratic threshold but the inspected prior audit found no endpoint quartic formula.

    ## Scientific value

    **PASS_AFTER_REPAIR** — Once the duplicate Hessian material is removed, the endpoint computation still closes a natural local question left by the quadratic spectrum: the unique null modes at sigma^2=2/(n+1) do not immediately destabilize along genuine translations, but bend downward at fourth order. The claim is appropriately limited to that branch and does not pretend to solve the global gap.

    ## Findings

    - The entire second-variation spectrum is duplicated by earlier SCOPE records and is removed from the corrected originality claim.
- At the critical variance, the translated-ball and polar quadratic coefficients cancel exactly.
- The independently reconstructed quartic coefficient agrees with the filed C_n formula.
- The inequality R>(n-1)/2 proves C_n>0 in every dimension n>=2.

    ## Independent checks

    - Re-expanded the translated Gaussian-ball integral using spherical moments E[Y^2]=1/n and E[Y^4]=3/[n(n+2)].
- Re-expanded the polar radial factor via derivatives of F at r=1.
- Symbolically multiplied both expansions and simplified the quartic coefficient.
- Checked positivity with the radial integration-by-parts identity and audited overlap against the 17/18 September SCOPE records.

    ## Sources

    - https://arxiv.org/abs/2609.18472 — Artstein-Avidan–Fradelizi–Wyczesany motivating Gaussian Santaló problem and translated-ball threshold.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/17/gaussian-volume-product-hessian-spectrum--714d3bdc8013 — Earlier SCOPE full-Hessian spectrum record.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/18/gaussian-volume-product-hessian-instability-index--adb76edfac12 — Earlier SCOPE full-Hessian/instability-index record.

    ## Limitations

    - Only the actual translation branch is expanded to fourth order.
- No complete fourth-order normal form or topology-uniform local maximality theorem is proved.
- The global maximization problem in the remaining higher-dimensional parameter gap is unchanged.

    This audit is independent of the repository's pre-existing same-model review. GitHub was read only as evidence; no repository changes were made by this audit run.
