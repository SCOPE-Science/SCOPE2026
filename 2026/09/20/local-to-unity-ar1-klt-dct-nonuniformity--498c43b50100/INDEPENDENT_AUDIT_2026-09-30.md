# Independent Audit — 2026-09-30

**Record:** `2026/09/20/local-to-unity-ar1-klt-dct-nonuniformity--498c43b50100`  
**Title:** A nonuniform DCT limit for the AR(1) KLT under growing block length  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `74bffba5cad3f5e986fcb2d5585e4bec56b271a8`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The principal-mode asymptotics are correct. The symmetric Kac–Murdock–Szego secular equation cos((N+1)omega/2)=rho cos((N-1)omega/2) rearranges to 2N tan(xi_N/2)tan(xi_N/(2N))=2N(1-rho)/(1+rho), with xi_N=N omega. The left side is strictly increasing on (0,pi), converges locally uniformly to xi tan(xi/2), and forces xi_N->pi when the scaled parameter diverges. Exact trigonometric sums give the stated finite-N overlap. I independently diagonalized R_N(rho) for N=64,256 and a=0.1,1,5 under rho=e^{-a/N}; the closed-form overlap agrees with dense eigendecomposition to machine precision and converges to the stated C(a). At a=1 I recovered xi=1.306542374188806, C=0.997807929633788 and lambda_1/N->0.738810809416455. The small-a expansion and eigenvalue identity 2a/(a^2+xi^2)=sin(xi)/xi also check.
- **Originality — PASS:** Reznik's 2026 source states the exact DCT-core factorization and that, for fixed N, correction factors become identities as rho->1; it does not advertise a joint growing-N/local-to-unity threshold. Jain (1979) proves broad asymptotic equivalence of a sinusoidal transform family and warns that DCT need not be a good finite approximation, but its accessible statement does not give the explicit principal-vector phase transition or the iff N(1-rho)->0 criterion. Clarke (1981) is the closest historical source and is consistently described by later sources as establishing the rho->1 DCT-II coincidence. I attempted authorized institutional retrieval after OA searches failed, but the publisher required human verification, so its two-page full text was not read in this noninteractive run. Because the filed novelty is the explicit joint-scaling law rather than the classical endpoint, and no source located states that law, originality passes with this documented residual risk.
- **Scientific value — PASS:** The result turns a fixed-size limiting statement into a sharp dimension-dependent criterion and gives an explicit geometric obstruction to dropping KLT correction factors in growing blocks. The block-length/correlation-length ratio N(1-rho) is a practically interpretable scaling parameter, and a one-row mismatch already rules out uniform operator-norm convergence.

## Independent findings
- The exact finite-N overlap formula agrees with independent dense eigendecomposition to floating-point precision in tested local-to-unity cases.
- For finite scaled parameter a, the limiting eigenvalue fraction is both 2a/(a^2+xi^2) and sin(xi)/xi once a=xi tan(xi/2) is used.
- The large-scaled-parameter limit xi->pi gives overlap 2sqrt(2)/pi and therefore row distance sqrt(2-4sqrt(2)/pi).
- Authorized retrieval of Clarke (1981) reached a publisher human-verification barrier; the audit does not claim to have read that inaccessible text.

## Independent checks
- Re-derived the tangent secular equation directly from the symmetric boundary equation.
- Compared the exact phase/overlap formula with dense eigen-decomposition at N=64 and 256 for several local-to-unity parameters.
- Numerically checked the small-a expansion C(a)=1-a^2/360+O(a^3) and the distance asymptotic a/sqrt(180).
- Compared the novelty boundary with Reznik (2026), Jain (1979), and secondary descriptions of Clarke (1981); attempted but could not complete authorized full-text retrieval of Clarke without human verification.

## Literature evidence
- https://arxiv.org/abs/2609.20221 — Reznik (2026), exact AR(1) KLT factorizations and fixed-N rho->1 disappearance of correction factors; no joint growing-N law stated in the accessible source.
- https://doi.org/10.1109/TPAMI.1979.4766944 — Jain (1979), sinusoidal transform family and asymptotic-equivalence background; accessible abstract warns DCT is not always a good finite approximation.
- https://doi.org/10.1049/ip-f-1.1981.0061 — Clarke (1981), closest historical DCT/KLT endpoint source. Full text could not be obtained in this run because publisher human verification was required; later sources describe it as the rho->1 DCT-II coincidence.
- https://doi.org/10.1109/TSP.2013.2265225 — Torun–Akansu (2013), explicit finite-N AR(1) KLT kernels and DCT comparison background.

## Limitations
- The sharp theorem is for the principal KLT vector; it yields a lower-bound obstruction for the full transform but not a complete transform-norm asymptotic.
- Coding gain, rate-distortion loss, and floating-point/truncation behavior are outside the result.
- Clarke (1981) full text remained inaccessible without human verification; originality is therefore qualified at the historical-literature boundary.

The assigned source tree remained unchanged from the inventory/source-tree-check interval through current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the exact tree audited is `74bffba5cad3f5e986fcb2d5585e4bec56b271a8` and matches the assignment guard. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific audit contract.
