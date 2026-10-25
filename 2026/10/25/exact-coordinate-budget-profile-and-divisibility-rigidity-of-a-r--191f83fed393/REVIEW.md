# Self-review

## Correctness — PASS

The theorem has explicit integer domain \(n\ge2,r\ge1\), complex scalar field, the prescribed endpoint norm and consistent normalizations. Rebuilding the proof: (i) maximize convex endpoint coordinates on unit circles, reducing to \(r\) projective phases; (ii) use nearest-point ordering on the regular projective lattice to establish the sharp bound \(2\sin(k\pi/(2n))/\sin(\pi/(2n))\) for a cluster of \(k\) columns; (iii) strict sine concavity forces balanced block sizes, with explicit consecutive-block midpoint phases realizing the bound; (iv) Jensen gives the precise divisibility equality condition; (v) Taylor expansion gives the quadratic residue-dependent deficit. Special cases \(r=1\), \(r=n\), and \(r>n\) are consistent. The packed stdlib script passed 75,263 supplementary checks; finite sampling is not treated as a proof of phase optimality.

## Originality — PASS, with residual priority risk

The closest primary source is Santos and Serrano-Rodríguez, *Effective Dimensions in Grothendieck–Hölder Inequalities*, arXiv:2610.04398v1, October 3, 2026. Its Lemma 4.1 establishes a general phase-partition reduction; Proposition 4.6 proves the sharp supremum over **all** complex two-row matrices; Remark 4.11 evaluates only the specific \(n=3,r=2\) Fourier example. The new theorem is a *pointwise* exact profile for **all** \(n,r\) for the fully populated regular Fourier matrix, including optimal balanced allocations, the full arithmetic saturation classification and explicit finite-grid deficit. In particular the published universal bound is strict for this family whenever \(r<n\) and \(r\nmid n\), a statement not supplied by the published universal constant. Ambrus–Grundbacher (arXiv:2502.13752v2) treat planar large signed sums, including the one-center inequality invoked by the 2026 source, not an \(r\)-center Fourier profile. Public index searches also retrieved an unrelated real-field rectangular tensor-norm saturation result, but no covering statement. Residual risk: equivalent regular-circle facility-location or tensor-norm formulas might exist outside indexed resources; searches do not prove priority.

## Mathematical value — PASS

The regular two-row Fourier matrix is a natural test family for the complex rectangular endpoint. General matrix-uniform estimates do not say whether this one fully populated family attains the bound at each intermediate coordinate budget. The theorem answers that natural structural question exactly for every budget, exposes the divisibility obstruction rather than simply adding a finite example, gives optimizing phase allocations, and quantifies the loss as \(n^{-2}\) at nondivisible residues. The continuous-density profile establishes a dimension-budget tradeoff with loss of order \(r^{-2}\), useful for choosing coordinate budgets and understanding pointwise versus uniform stabilization. The proof is not a restatement of the prior universal inequality.

## Scope and remaining risks

No arbitrary-matrix classification, interior Hölder-scale exact values, or independent audit is asserted. A complete external novelty examination against old circular quantization literature is still warranted.

Self-review: passed. Independent audit: not yet performed.
