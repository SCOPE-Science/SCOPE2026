# Scientific review: rank-two matroid base-polytope asymmetry

## Correctness — PASS
Every loopless rank-two matroid is specified by a partition into parallel classes. The proof derives its base-polytope halfspace description directly from convex combinations of pairs of classes. For three or more classes, the reflection-containment criterion is exactly a list of coordinate lower bounds and class-sum upper bounds. The associated interval feasibility system has three sharp obstructions. For two classes the polytope is a product of simplices and is treated separately. The residual-coordinate description proves the complete center locus and all dimension branches. The included standard-library exact-rational checker tests 2036 class-size profiles and 77808 reflected bases through total size eleven; an independent general-rank-inequality LP matched 247 profiles through size eight. Finite checks are not the infinite proof.

## Originality — PASS, subject to residual search risk
Ferroni–Jochemko–Schröter establish the rank-two hyperplane description and Ehrhart formulas, not Minkowski centers. Pineda-Villavicencio–Schröter treat basis-exchange graph reconstruction. Den Hertog–Pauphilet–Soali provide a general polyhedral-center linear program, which implicitly computes an instance but neither supplies this class-size maximum nor classifies every minimizing center and its dimension. Published search and statement comparisons found no covering claim. Searches cannot certify global priority, and an earlier reformulation of the exact classification remains possible.

## Value — PASS
Minkowski asymmetry is a natural affine invariant, and class sizes are canonical complete parameters of rank-two matroids. The sharp formula separates three competing extremal obstructions, handles disconnected products, and determines all center-space dimensions. In particular, connected rank-two base polytopes can have nonunique optimal centers even though the uniform rank-two case has a unique one. This is a complete natural family classification, not a numerical table or renaming of an existing result.

## Closest literature and limitations
The most direct full-text comparisons are Ferroni–Jochemko–Schröter, *Ehrhart polynomials of rank two matroids* (arXiv:2106.08183, §2.2), and den Hertog–Pauphilet–Soali, *Minkowski Centers via Robust Optimization* (Proposition 4 and §2.4). The scope is rank two with no loops. The result is proved from an exact halfspace model; finite testing does not prove the theorem. Residual risk: equivalent prior results may use different terminology, especially submodular base-polytope symmetry.

Same-model review: passed. Independent audit: not yet performed.
