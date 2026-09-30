# Independent Audit — 2026-09-29

**Record:** `2026/09/20/halvorsen-diagonal-slab-and-mean-square-sphere--f567f56cc506`  
**Title:** Exact diagonal balance and compact-recurrence bounds for the Halvorsen flow  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `0599c74ab886c17092106576a20d02325cab9d10`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The global consequences follow correctly from the exact scalar balance S'=-sigma S-dQ. Completing the square gives S'=3 sigma^2/(4d)-d||X+(sigma/(2d))1||^2, so bounded forward trajectories have the stated mean-square time average and invariant measures satisfy the same identity. At sigma=0, boundedness makes Q integrable and uniformly continuous, hence Q->0; for a bounded complete orbit this occurs at both time ends and monotonicity of S forces the orbit to be identically zero. For sigma!=0, variation of constants gives v=dS/sigma<=0; Q>=S^2/3 and Riccati comparison exclude v<-3 (forward for sigma>0, backward for sigma<0). Equality cases force the diagonal equilibria. Integrating the balance against an invariant measure yields the sharp second-moment interval. I found no sign or completeness error.
- **Originality — PASS:** The 2025 open Halvorsen paper is explicitly a local transcritical/Hopf-bifurcation analysis and does not advertise the global balance/slab/invariant-measure conclusions. The detailed public abstract of Vaidyanathan–Azar (2016) lists dissipativity, instability of the origin, Lyapunov exponents, Kaplan–Yorke dimension, adaptive control, and synchronization as its main results, not the present identities or recurrence bounds. Authorized institutional retrieval of that chapter was attempted twice after OA searches but timed out, so its full text was not read and no claim to the contrary is made. Targeted exact-identity searches found no prior statement. On that evidence the theorem-level package passes originality, with a documented residual risk that an elementary balance identity could appear in inaccessible older text.
- **Scientific value — PASS:** The result turns an elementary-looking scalar balance into strong global restrictions on all bounded recurrent dynamics and all compactly supported invariant measures, including collapse at the transcritical surface. Those conclusions materially complement the predominantly numerical/control and local-bifurcation Halvorsen literature.

## Independent findings
- For sigma=0, bounded forward trajectories converge to the origin; bounded complete trajectories are necessarily the zero equilibrium.
- For sigma!=0, the normalized diagonal coordinate v=dS/sigma is confined to the sharp slab [-3,0] on every bounded complete orbit, with rigid boundary equality at the two diagonal equilibria.
- The invariant-measure estimate 0<=integral Q<=3(sigma/d)^2 follows directly from the slab and the integrated balance.
- The strongest inaccessible historical comparison, Vaidyanathan–Azar (2016), could not be retrieved through the authorized institutional fallback after two retries; only its detailed public abstract was used.

## Independent checks
- Re-derived the summed ODE and completed-square identity symbolically by hand.
- Checked the Barbalat/uniform-continuity step used at sigma=0 and the two-sided complete-orbit argument.
- Re-derived both signs of the variation-of-constants formula and the Riccati comparison producing v>=-3.
- Compared the novelty claim with the detailed 2016 chapter abstract and the 2025 local-bifurcation article; searched exact x+y+z/a+b+c balance terminology.

## Literature evidence
- https://doi.org/10.1007/978-3-319-30340-6_10 — Vaidyanathan–Azar (2016). Detailed public abstract inspected; full text remained inaccessible after authorized fallback retries, so inaccessible pages are not claimed read.
- https://doi.org/10.21271/ZJPAS.37.6.4 — Othman–Jalal (2025), open article/abstract; focuses on local transcritical and Hopf bifurcations and periodic-orbit stability.
- https://sprott.physics.wisc.edu/chaos/symmetry.htm — Sprott note for the standard symmetric Halvorsen flow context.

## Limitations
- The theorem is conditional on bounded forward or bounded complete trajectories where stated; it does not prove global boundedness or existence of an attractor for arbitrary initial data.
- The 2016 Vaidyanathan–Azar full chapter could not be inspected in this run despite OA searches and two authorized retrieval attempts, leaving a concrete originality caveat for elementary identities.
- The strongest novelty is in the global slab, recurrence, and invariant-measure consequences, not in the mere act of summing the three equations.

The assigned source tree remained unchanged from the inventory/source-tree-check interval through current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the exact tree audited is `0599c74ab886c17092106576a20d02325cab9d10` and matches the assignment guard. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific audit contract.
