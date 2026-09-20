# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof starts from the exact invariant recurrence and angle formulas in arXiv:2609.18788. The limiting scalar map is a contraction on the source invariant interval, its unique fixed point is the stated cubic root, and the perturbation from finite b is uniformly quadratic in b. This yields convergence of the projective ratio and summability strong enough for the positive limit of b_n/rho^n. A local Taylor expansion gives derivative -1/2 and the displayed b^2 forcing coefficient; because rho^2>1/2, normalization by b_n^2 is stable and gives the stated second-order coefficient. The inradius, volume, cut-fraction, and limiting-dihedral formulas were independently re-derived from the tetrahedral coordinates. The standalone high-precision artifact checks the formulas on four initial conditions, including the source seed.

Adversarial checks included: verifying that the fixed-point cubic has only one root in the invariant interval; checking that the projective derivative is contractive; checking that the claimed volume fraction equals the geometric angle-bisector fraction exactly; recomputing the tetrahedral inradius from volume divided by total face area; and verifying that the limiting double-angle identity follows algebraically from the cubic rather than numerical coincidence.

## Originality

**PASS, to the best of our knowledge.** The motivating paper already proves the invariant family, unique selected edge, exact recurrence, fixed-seed degeneration, coarse rate bounds, angle bounds, and conforming adaptive realization. None of those are claimed. The recent longest-edge literature also uses projective dynamical systems and contains distinct degeneration mechanisms, so projective analysis of bisection itself is prior.

The originality claim is limited to the consequences specific to the new largest-dihedral-angle recurrence: attraction of the full invariant rectangle to one universal fixed ratio, the sharp exponential rate rho and positive prefactor C, the universal second-order coefficient (t_n-rho)/b_n^2, the limiting cut/volume fraction rho^2, and the limiting dihedral double-angle profile. Searches used the source identifier and title, largest-dihedral-angle/LAB terminology, asymptotic/fixed-point terminology, the cubic 7 rho^3-12 rho^2+4, and the resulting numerical constants. The repository was also searched for the source paper and LAB terminology. No overlapping SCOPE record or accessible external statement was found.

Residual originality risk is nonzero because arXiv:2609.18788 is very recent and a contemporaneous follow-up may not yet be indexed. The accessible full text of the source paper and abstracts/full text where available for the two closest 2026 longest-edge papers were inspected. No inaccessible specific paper was identified as likely to contain this exact LAB asymptotic theorem.

## Value

**PASS.** The source counterexample establishes failure using interval bounds. The new result identifies the attracting projective shape and the exact exponential degeneration mechanism for an entire invariant family, quantifies the asymptotic 61.3956% retained-volume split, and gives the exact mesh-quality growth base 1.276237... together with the limiting nondegenerate dihedral profile. This separates transient interval estimates from the long-run geometric mechanism and makes the counterexample quantitatively reusable for mesh-refinement analysis and benchmark construction.

## Limitations

The theorem is confined to the source's retained LAB branch and its invariant two-parameter family with c=7/8. It does not classify arbitrary LAB seeds or global refinement policies. The prefactor C depends on the initial point and has no closed form here. All analytic claims are exact-arithmetic statements; the verification script is supporting evidence rather than a substitute for the proof.
