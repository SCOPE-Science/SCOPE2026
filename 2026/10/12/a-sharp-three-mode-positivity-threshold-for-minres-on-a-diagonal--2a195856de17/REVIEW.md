# Self-review

## Correctness
PASS. The exact residual least-squares equations were reconstructed independently. The first iterate is a positive multiple of the nonnegative right-hand side. In dimension at most two, the only possible later MINRES point is the exact solution, which is nonnegative for Stieltjes matrices. In the three-mode family, the normal equations give the displayed closed form and the exact threshold \(\varepsilon=1/\sqrt{50}\). The irreducible witness is checked with exact rational arithmetic.

## Originality
PASS. The review compared MINRES with its symmetric-GMRES equivalent formulation, residual-minimization literature, Stieltjes/inverse-positive terminology, the closest semantic-database records, and the distinct prior CG/Stieltjes result. The inspected Paige--Saunders full text provides the residual-minimization framework but not the coordinatewise theorem. No inspected source implies the exact threshold or the stated minimality. Residual risk remains from older conjugate-residual terminology.

## Value
PASS. Residual minimization can violate a natural order cone even on a diagonal SPD system whose exact solution is strictly positive. The exact three-mode threshold explains how a small high-curvature component changes sign, while the minimality result shows this cannot occur earlier or in lower dimension for the stated Stieltjes class. The irreducible witness shows the effect survives genuine coupling.

## Closest literature and limitations
Paige and Saunders are the direct algorithmic source for MINRES. Saunders, Simon, and Yip provide the MSC \(65\mathrm{F}10\) classification lineage. The closest semantic-database match concerns Euclidean error amplification for symmetric GMRES(1), which does not cover the unrestarted two-dimensional Krylov iterate or componentwise positivity. The exact threshold is not claimed beyond the displayed diagonal family, and no exhaustive literature search can eliminate all alias risk.

Self-review: passed. Independent audit: not yet performed.
