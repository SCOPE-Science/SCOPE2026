# Independent Audit — 2026-09-30

**Record:** `2026/09/20/lorenz84-eddy-memory-and-small-forcing-convergence--9ae03d7abd20`  
**Title:** Stationary eddy-energy law and a small-forcing convergence criterion for Lorenz-84  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `00b2d5ac87ff92953dd606ddebaeb9e16a39bdcf`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The trajectory, invariant-measure, and contraction claims are correct. With U=F-X and R=Y^2+Z^2, the first equation gives Udot=R-aU exactly; backward variation of constants on a bounded complete orbit yields the positive memory law and X<=F. If G!=0, U cannot vanish on such an orbit, and compactness upgrades this to sup X<F on a compact invariant set. For an invariant compactly supported measure, applying the generator to H(X) for arbitrary continuous H'=h gives int h(X)[a(F-X)-R]dmu=0, exactly E[R|X]=a(F-X); the covariance, total-variance, and Jensen consequences follow. For F<1, W=Y+iZ obeys Wdot=[(X-1)+ibX]W+G, giving |W|<=|G|/(1-F) on complete bounded trajectories and the X slab. Comparing two such trajectories gives P<=(2M/a)V and V<=(sqrt(1+b^2)M/(1-F))P, so the stated strict inequality makes the complete orbit unique. The exact total-energy identity gives dissipativity and hence a compact global attractor, whose uniqueness then forces a singleton equilibrium. Independent symbolic expansion reproduced the R and total-energy identities exactly.
- **Originality — PASS:** The raw scalar and energy balances are elementary and are not treated as novel. The accessible Lorenz-84 literature covers dissipation/energy transfer, bifurcations, attractors, and invariant-measure-based system identification. Pelino–Pasini (2001) is the strongest historical energy-transfer risk; no OA full text was available, and an authorized institutional retrieval attempt reached a human-verification barrier, so this audit does not claim to have read it. Its public abstract describes Lie–Poisson dissipation and a mechanism of energy transfer, not the conditional law or small-forcing global contraction. Wang–Yu–Wen (2014) treats equilibrium stability/Hopf/chaotic dynamics. Gallo–Anselmi–Lazzari (2026) uses an invariant-measure moment matrix for identifiability; its accessible abstract does not state E[R|X]=a(F-X). No located source gives the package of the past-memory support barrier, exact stationary conditional law with covariance/variance hierarchy, explicit recurrent slab, and nonzero-forcing global-attractor collapse criterion. That package therefore passes originality, with the Pelino full-text limitation documented.
- **Scientific value — PASS:** The conditional law is a strong exact constraint on every compact stationary statistical state and gives directly testable covariance/variance diagnostics. The same scalar structure yields a geometric support barrier and, together with the complex eddy equation, an explicit region excluding every nontrivial recurrent attractor under nonzero forcing. This materially complements local/numerical Lorenz-84 analyses.

## Independent findings
- Independent symbolic expansion gives Rdot=2(GY+(X-1)R) and Edot=aFX+GY-aX^2-R, confirming the exact balances used by the proof.
- The conditional expectation statement follows from generator invariance for arbitrary continuous functions of X; it is stronger than a single mean energy balance.
- Uniqueness of bounded complete trajectories, combined with finite-dimensional dissipativity, is sufficient to make the global attractor a singleton equilibrium.
- Authorized retrieval of Pelino–Pasini (2001) reached a publisher human-verification barrier; only its public abstract was compared, and inaccessible pages are not represented as read.

## Independent checks
- Re-derived the memory formula and strict support barrier on bounded complete trajectories.
- Re-derived the generator argument for the full conditional law and the covariance/variance consequences.
- Reconstructed the two-trajectory sup-norm contraction and checked the coefficient 2 sqrt(1+b^2) G^2/[a(1-F)^3].
- Symbolically verified the eddy-energy and total-energy polynomial identities; searched and compared Pelino–Pasini, Wang–Yu–Wen, and Gallo–Anselmi–Lazzari statements.

## Literature evidence
- https://doi.org/10.1016/S0375-9601(01)00764-2 — Pelino–Pasini (2001), dissipation/energy-transfer context. Public abstract inspected; authorized full-text attempt required human verification and was not completed.
- https://doi.org/10.1155/2014/296279 — Wang–Yu–Wen (2014), equilibrium stability, Hopf and chaotic-dynamics context rather than the filed invariant-measure/global-contraction theorem.
- https://arxiv.org/abs/2607.18490 — Gallo–Anselmi–Lazzari (2026), invariant-measure moment-matrix/system-identification context; accessible abstract does not state the filed conditional eddy-energy law.
- https://doi.org/10.1111/j.1600-0870.1984.tb00230.x — Lorenz (1984), original Lorenz-84 model and dissipativity background.

## Limitations
- The global-convergence inequality is sufficient, not claimed necessary or sharp, and requires F<1.
- The invariant-measure statement is formulated for compactly supported invariant measures.
- Pelino–Pasini (2001) full text remained inaccessible without human verification, so originality is qualified at the historical energy-transfer boundary.
- Seasonally forced, stochastic, and coupled Lorenz-84 variants are outside the theorem.

The assigned source tree remained unchanged from the inventory/source-tree-check interval through current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the exact tree audited is `00b2d5ac87ff92953dd606ddebaeb9e16a39bdcf` and matches the assignment guard. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific audit contract.
