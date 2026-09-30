# Independent Audit — 2026-09-29

**Record:** `2026/09/20/clark-ismail-positivity-theta-bound--b7fd6cc070ac`  
**Title:** A squarefree theta bound for Clark–Ismail derivative positivity  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `8ebee3aeef9cc92d05c58966944f42ee0746d372`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** Starting from the corrected Hermite–Laguerre identity, the scaling q=e^{-x/2} is consistent and absolute convergence justifies the kernel interchange. Unique factorization j=d m^2 with d squarefree turns each block into a theta_3 series; Jacobi’s product gives the theta_4 lower bound. Recombining signs using “m even iff 4 divides j” yields exactly (1-q-q^2-q^3)/(1-q^4). For q<=rho this is nonnegative, and at equality continuity plus K_q(0)>0 makes the weighted Hermite-square integral strictly positive.
- **Originality — PASS:** Castillo’s 2025 correction restores the explicit uniform interval x>2 log 2 after correcting the earlier Hermite–Laguerre formula and only remarks that alternative integral representations might give slight refinements. Searches for the cubic rho threshold, the decimal constant, and squarefree/theta decompositions did not locate the filed bound or method. The claim is therefore plausibly original, while the correction’s unspecified refinements remain an explicit residual risk.
- **Scientific value — PASS:** The record gives a concrete rigorous improvement from 2 log 2 to about 1.2187557 and introduces a reusable arithmetic decomposition of a nonharmonic cosine kernel into theta blocks. It does not solve the optimal-threshold problem, but the structural method and quantitative gain are scientifically substantive.

## Independent findings
- Recomputed the corrected Hermite–Laguerre scaling and verified that the kernel coefficient is q^j with q=e^{-x/2}.
- Verified theta_3(z,r)>=theta_4(0,r) factor-by-factor from Jacobi’s product.
- Recomputed the squarefree recombination to 1-q/(1-q)+2q^4/(1-q^4)=(1-q-q^2-q^3)/(1-q^4).
- Checked the endpoint strict-positivity argument despite a zero global lower bound.

## Independent checks
- Compared directly against the 2025 correction’s restored x>2 log 2 theorem and corrected identity.
- Searched exact cubic, threshold-decimal, squarefree, Hermite/Laguerre and theta formulations; no equivalent indexed result was found.
- Verified the monotonicity/unique-root conversion q<=rho iff x>=-2 log rho.

## Evidence and literature
- https://doi.org/10.1007/s11139-025-01024-7 — Castillo (2025) correction: corrected Hermite–Laguerre identity and restored x>2 log 2 positivity theorem; mentions only unspecified slight refinements.
- https://doi.org/10.1007/s11139-023-00759-5 — Castillo (2024), original article whose stronger interval was later corrected.
- https://doi.org/10.1016/j.jat.2004.02.008 — Alzer, Berg and Koumandos (2005), context for failure of the global conjecture and the remaining uniform-threshold problem.
- https://dlmf.nist.gov/20.5 — Jacobi theta product formulas used in the block lower bound.

## Limitations
- The bound is sufficient, not proved optimal, and it does not identify the first derivative order failing below it.
- The 2025 correction mentions unspecified possible refinements, so unpublished or differently indexed overlap cannot be excluded.
- The full 2006 Al-Musallam–Bustoz article was not separately needed for the new proof; its 2 log 2 benchmark is documented in later primary literature.

The assigned source tree remains exactly `8ebee3aeef9cc92d05c58966944f42ee0746d372` at current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; it matches the assignment guard. GitHub was used only as read-only evidence and no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific contract.
