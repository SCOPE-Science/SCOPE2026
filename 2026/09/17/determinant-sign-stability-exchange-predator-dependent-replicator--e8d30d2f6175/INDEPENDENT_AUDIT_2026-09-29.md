# Independent Audit — determinant-sign-stability-exchange-predator-dependent-replicator--e8d30d2f6175

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `a9566a72b6ea963f3ab1062038d6556fb74534f0`  
**Audited current source tree:** `a9566a72b6ea963f3ab1062038d6556fb74534f0`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA. No intervening source change required a stale-source re-audit.

## Correctness — PASSED

PASS. The local stability-exchange proof is valid under the record's stated genericity assumptions. At a boundary collision the source's exact identity det J = beta*delta*F^2*x*(1-x)*g*kappa' isolates the sign of the unique small real eigenvalue because the other two eigenvalues stay in the open left half-plane and hence have positive product. Independently redoing the endpoint sign bookkeeping gives the opposite sign for the AY/BY invasion eigenvalue and the AB predator-invasion eigenvalue on the neighboring ABY branch. In the reproduction-codominance AB case, the pre-existing positive prey-plane eigenvalue persists and forces ABY instability. The proof therefore establishes the three numbered stability assertions locally without asserting the failed Sotomayor transcritical nondegeneracy condition.

## Originality — PASSED

PASS, TO THE BEST OF THE SEARCHED PUBLIC LITERATURE. Cruz--Neves explicitly label the statement Conjecture 6.2, describe the observed stability exchange as transcritical-like rather than proved transcritical, and close by listing a proof of Conjecture 6.2 as future work. Targeted searches through 2026-09-29 did not locate a later proof or correction. The determinant formula and boundary-stability criteria are prior ingredients from the source; the original contribution is the short sign-comparison argument that resolves the source-specific conjecture under its generic hypotheses.

## Scientific value — PASSED

PASS. This resolves a named conjecture in a July 2026 population-dynamics preprint and explains why the desired local stability exchange can be certified even though a standard Sotomayor condition fails. The argument is compact and potentially reusable for invariant-boundary ecological systems with a simple zero eigenvalue and an already-separated stable spectral pair.

## Independent checks

- checked the public full text of Cruz--Neves around Conjecture 6.2, the determinant identity, the AY/BY/AB stability theorems, and the authors' future-work statement
- independently rederived the AY and BY branch-side/invasion-eigenvalue sign comparisons
- independently rederived the AB coexistence and codominance cases
- verified the current main record tree exactly equals the assigned tree SHA and contains no 2026-09-29 independent-audit marker

## Limitations

- The conclusion is local near nondegenerate boundary collisions; it does not exclude later Hopf or other bifurcations along the ABY branch.
- The audit does not claim the collision satisfies the standard Sotomayor transcritical hypotheses; the source itself explains that a required condition fails.
- Originality is necessarily qualified because the source is recent and an unindexed contemporaneous proof could exist.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/17/determinant-sign-stability-exchange-predator-dependent-replicator--e8d30d2f6175
- https://arxiv.org/abs/2607.13281
- https://www.researchgate.net/publication/410160623_Predator-dependent_replicator_dynamics_or_a_predator-prey_model_with_two_prey_types_and_frequency_dependence
