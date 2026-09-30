# Independent Audit — Bounded radial Toeplitz symbols realize every U(n)-intertwiner for a logarithmic Fock weight

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `2eecd8efdfcdd765b40575331aca93af65a3afc5`  
**Audited current source tree:** `2eecd8efdfcdd765b40575331aca93af65a3afc5`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment tree SHA. GitHub was used read-only as evidence, and the dated independent-audit files were absent when this guarded plan was prepared.

## Correctness — PASSED

PASS. The moment kernels are probability densities and Bdarneh's logarithmic-weight Laplace peak lies at u_m=(4/9)(2m+2n)^2. The submitted disjoint windows have endpoint log-slopes ±1 and exponentially small leakage, so the step-symbol map S gives T=Lambda_n S=I+K with compact K on l_infinity. A subspace containing the closed finite-codimensional range of this Fredholm operator is itself closed and finite-codimensional, so ran Lambda_n is closed. The preadjoint J:l_1->L_1 is injective: absolute L1 convergence permits division by the common positive radial factor and the resulting power series is entire, while its a.e. vanishing on the positive axis forces every coefficient to vanish. Closed range plus injectivity makes J bounded below, and Hahn--Banach then gives surjectivity of J*=Lambda_n. The final bounded linear right inverse is valid because the Fredholm range has a finite-dimensional complement and Lambda_n is surjective.

## Originality — PASSED

PASS, narrowly scoped. Bdarneh's current v2 full text was obtained after direct arXiv/OA full-text access failed. It proves the radial spectral formula, strong-operator density of invariant Toeplitz operators, and for the same logarithmic weight constructs one bounded radial symbol whose eigenvalues tend to (-1)^m; it does not state exact bounded-symbol surjectivity onto l_infinity or a bounded linear right inverse. Grudsky--Vasilevski's older Fock result allows arbitrary spectral data only in a larger symbol class whose symbols are generally unbounded, while the classical bounded-radial algebra is much smaller. Targeted searches found no prior theorem identifying bounded radial symbols for this logarithmic weight with the full U(n)-commutant.

## Scientific value — PASSED

PASS. The theorem upgrades the source's qualitative failure of the classical square-root-uniform-continuity picture and its strong-operator density statement to exact single-symbol realization of every bounded U(n)-intertwiner. The bounded linear lifting is a robust functional-analytic strengthening and sharply contrasts this logarithmic Fock weight with the classical Gaussian bounded-symbol regime.

## Independent checks

- Read the complete relevant logarithmic-weight section of Bdarneh v2 after lawful open-access routes failed and institutional retrieval completed.
- Recomputed the Laplace peak, endpoint exponents, endpoint derivative signs, and exponential leakage mechanism.
- Checked that a linear subspace containing a closed finite-codimensional subspace is itself closed and finite-codimensional.
- Checked absolute a.e. convergence of the l1 kernel series and the entire-function injectivity argument.
- Checked the closed-range/Hahn--Banach surjectivity step and constructed the bounded right inverse from Fredholm complements.
- Compared against classical bounded-radial Fock spectral-algebra results and the older unbounded-symbol interpolation result.
- Verified the current main tree SHA equals the assigned source tree and that the dated audit-marker files are absent.

## Limitations

- The result is specific to the displayed logarithmic radial weight and U(n)-radial symbols; it does not classify all weights or quasi-radial multi-parameter maps.
- The right inverse is existential and no optimal lifting norm or uniqueness statement is established.
- Bdarneh's preprint is extremely recent; simultaneous unindexed work remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.20652
- https://arxiv.org/abs/1505.07906
- https://doi.org/10.1007/BF01197858
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/bounded-radial-symbols-all-un-intertwiners-log-fock--f07edacc9484

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
