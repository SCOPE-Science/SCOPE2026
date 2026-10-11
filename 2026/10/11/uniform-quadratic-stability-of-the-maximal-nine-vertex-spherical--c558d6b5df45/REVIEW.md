# Scientific assessment: transverse stability of the nine-vertex volume maximizer

## Correctness — PASS

The fixed configuration and global maximum are Theorem 1.1 of Hoehner–Ledford (arXiv:2608.04392v1). The fourteen strictly supporting facets, twenty-one two-sided edges, all eighteen orthonormal tangent directions, and the constrained Hessian formula have been independently reconstructed. The determinant volume formula gives \(3\sqrt{2\sqrt3-3}\). The analytic gradient vanishes by global optimality (and by direct algebra). Exact rotational symmetry provides precisely three **known** null vectors; the integer-only outward-interval \(LDL^{\mathsf T}\) certificate makes \(-\mathcal H+P-0.39I\) positive definite, excluding all other null directions. A uniform Taylor theorem on the compact rotation orbit gives the local quadratic volume deficit with coefficient \(1/10\). Replaying the bundled certificate prints `VERIFY_OK`.

## Originality — PASS

The closest primary full text proves global optimality/equality but does not give a full constrained Hessian or a local quadratic deficit bound in all fifteen transverse modes. The Hessian appearing in its auxiliary inequality is for a **different two-variable concavity function**. Classical stationarity and the unique global maximum do not imply nondegeneracy: a unique smooth maximum can be arbitrarily flat. Targeted searches for second variation, Hessian, Morse–Bott, quantitative rigidity and distance-to-orbit inequalities yielded no covering statement. Remaining risk is an unindexed prior local-stability analysis.

## Value — PASS

This is a full-dimensional quantitative rigidity theorem around the newly identified global nine-vertex extremizer, not a special symmetry-preserving perturbation. The explicit bound controls all fifteen genuine shape-deformation directions and establishes the **quadratic order** of local stability, information not contained in uniqueness. The certified \(0.39\) spectral bound can inform error estimates and near-extremal numerical reconstruction of maximal-volume nine-point configurations.

## Closest literature and limits

Hoehner–Ledford, *The maximum volume polytope with nine vertices inscribed in the sphere*, arXiv:2608.04392v1 (2026-08-05), especially Theorem 1.1 and its proof, supplies the extremizer and global inequality. Berman–Hanes (1970) supplies historical maximum-volume and first-order conditions, not the full nine-point transverse Hessian. The new statement is local near a specified labeled rotation orbit; neither a global deficit constant nor an optimal Hessian gap is asserted. The certificate establishes rational inequalities for the Hessian but its near-zero gradient residuals are only consistency checks; exact stationarity is mathematical, not inferred from floating-point tolerance.

Same-model review: passed. Independent audit: not yet performed.
