# Independent Audit — 2026-09-30

**Record:** `2026/09/19/strict-alpha-filtration-log-monotone-marcinkiewicz-kernels--a4c3b8aeff80`  
**Title:** Strict alpha-filtration of logarithmically monotone Marcinkiewicz kernels  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `2b2c637d191fd2ec0221e26daf042def42ba626e`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** PASS. For alpha<beta, p_n^(alpha)<p_n^(beta), so Lyapunov monotonicity of normalized L^p means gives Phi_alpha≤Phi_beta term by term. The compressed-block probe is consistent: R_n=exp(L_n-r_n^gamma) has block mass r_n, cumulative mass L_n+O(1), and belongs to M_psi by concavity of log. For p=1-r_n^{-alpha}, the nth block contributes r_n^p(Delta_n')^(1-p); Jensen bounds all preceding blocks and the next partial block is exponentially negligible. Using log Delta_n'=L_n-r_n^gamma+o(1) yields exp(-r_n^(gamma-alpha)/p), hence the exact 0/e^{-1}/1 transition. The Huang f,g pair then gives the claimed Hardy–Littlewood obstruction for every interior alpha, while the endpoint is used only for the norm non-strong-symmetry statement. No sign or endpoint inconsistency was found.
- **Originality — PASS:** PASS, to the best of the accessible evidence. Huang's public abstract establishes the two broad phenomena—a logarithmically monotone symmetric norm that is not strongly symmetric and a strongly symmetric space with no equivalent fully symmetric norm—but does not advertise a strict continuum alpha-filtration or the concentration-threshold phase diagram. Earlier Kalton–Sukochev work supplies prior art for nonsymmetric singular functionals on Marcinkiewicz spaces, not this parameter geometry. The record appropriately limits novelty to the exact ordering and probes in Huang's explicit family.
- **Scientific value — PASS:** PASS. The theorem reveals that the interpolation parameter in the motivating construction is mathematically substantive rather than cosmetic: it produces continuum many distinct embedded kernels with an exact concentration threshold. The probes give an interpretable and reusable mechanism for separating the spaces.

## Independent findings
- The previous-block estimate has the correct Jensen direction because 0<p<1.
- The next-block contribution before T_n is negligible on the doubly exponential scale L_{n+1}=L_n^2.
- The boundary constant is exactly e^{-1}, not merely a nonzero constant.
- The record carefully limits the no-equivalent-fully-symmetric claim to 0<alpha<1 while treating alpha=1 only in the norm obstruction.

## Independent checks
- Recomputed the parameter monotonicity of the normalized L^p means.
- Re-derived the M_psi bound for the compressed-block probe, including interior points of each block.
- Recomputed dominant-block asymptotics and the threshold exponent.
- Checked the f,g Hardy–Littlewood comparison and endpoint usage.

## Literature evidence
- https://arxiv.org/abs/2609.20270 — Huang's motivating logarithmic-submajorization construction and the two broad counterexample phenomena.
- https://doi.org/10.4153/CMB-2008-009-3 — Kalton–Sukochev prior art on rearrangement-invariant functionals and traces.
- https://doi.org/10.1515/CRELLE.2008.059 — Kalton–Sukochev background on symmetric norms and operator spaces.

## Limitations
- The result is specific to Huang's chosen scales and Marcinkiewicz function psi.
- Distinctness is as embedded subspaces of the common M_psi, not a classification up to Banach-lattice isomorphism.
- The accessible public source did not expose searchable full text for every alpha-level construction detail, so originality is qualified to the public abstract plus the record's internally checkable formulas and targeted literature search.

The assigned source-tree SHA still matches the current record tree inspected on `main`. GitHub was used only as read-only evidence; no repository writes were made.
