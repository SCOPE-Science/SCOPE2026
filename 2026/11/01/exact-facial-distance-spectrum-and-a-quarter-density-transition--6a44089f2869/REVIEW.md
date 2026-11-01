# Scientific evaluation

## Correctness — PASS

The claim is an exact metric statement for the standard Euclidean hypersimplex and every valid integer parameter. All faces arise by fixing coordinate zeros and ones. Finite-group averaging is admissible because both separated convex sets are invariant under the face stabilizer. The two-parameter quadratic lower bound is sharp, not merely a relaxation: explicit one-swap outside vertices attain both endpoint mass configurations. Exact minimization gives the face formula. A separate argument handles vertex faces, after which maximizing a concave integer quadratic yields the globally sharp piecewise value. The exceptional segment \(\Delta_{2,1}\) is treated separately. The accompanying standard-library verifier completed 49,100 exact comparisons and witness checks; selected independently posed convex-hull quadratic programs also agreed. Neither calculation is substituted for the global proof.

## Originality — PASS (historical priority provisional)

The two nearest primary papers, Peña–Wirth arXiv:2608.28971 and Deza–Martínez-Rubio–Peña–Wirth arXiv:2609.32440, provide general face-gap bounds and a sharp Birkhoff-polytope calculation, but their accessible full texts do not give the present exact all-rank hypersimplex formula, its facewise version, or the integer transition. Searches for hypersimplex, Johnson-polytope and uniform-matroid-base-polytope facial distance and pyramidal width did not yield a stronger equivalent calculation. Targeted mathematical-record searches returned nearest claims about matroid inballs, circumspheres, and related simplex metrics, not this face-to-complement metric. Standard simplex endpoint values and the general 0–1-polytope bounds are expressly credited. Unindexed equivalent formulations in optimization or matroid work remain possible.

## Value — PASS

The facial distance is the pyramidal width, a conditioning invariant in geometric analysis of conditional-gradient algorithms. Hypersimplices are the canonical uniform-matroid base polytopes, so an exact all-parameter value and optimizing face classification supply a natural benchmark beyond the previously isolated exact simplex/cube/Birkhoff cases. The quarter-density transition changes the dimension of the minimizing faces and makes the calculation structural rather than a routine evaluation of one fixed example. No new algorithmic convergence guarantee is claimed.

## Sources, methods and remaining risks

The primary-paper full texts were inspected in their definitions, generic calculus, examples and main theorem sections. The comparison included both published mathematical records and available earlier claims, checking whether their conclusions imply this face-separation result. Numeric optimizations verify representative finite instances only. Historical priority remains provisional; weighted and nonuniform-matroid variants are not addressed. Independent validation was not performed.

Self-review: passed. Independent audit: not yet performed.
