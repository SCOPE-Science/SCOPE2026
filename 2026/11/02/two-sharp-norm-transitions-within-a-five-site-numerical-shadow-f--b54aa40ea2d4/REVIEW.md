# Scientific assessment: five-site shadow-fibre norm minimization

## Correctness

**PASS (self-review).** The exact determinant recurrence for five-site nilpotent shifts reduces equality of complete Haar numerical shadows to a fixed sum and matching quadratic of four positive squared edges. With a fixed maximum-edge cap, the quadratic minimization reduces to a one-variable, piecewise-concave function whose endpoint minima give the two algebraic branches. A least-singular-value test of the bipartite Hermitian part supplies the sharp third branch. Explicit positive and boundary allocations prove attainability/nonattainability, and equality conditions classify every positive minimizer. The companion finite checker returned `CHECK_OK 3817 cases`, which is supplementary and is not substituted for the proof.

## Originality

**PASS (best-knowledge same mathematical model literature comparison).** The numerical-shadow determinant criterion, the general radial density formula, and zero-diagonal Jacobi isospectral geometry are published prior inputs. The closest 2026 rigidity paper classifies dimension three, and existing four-site shadow-norm analyses concern a one-dimensional feasible fibre. None of these statements yields the exact five-site three-branch maximum-edge minimum with distinct attainment transitions and a continuous family of minimizers above the second threshold. Older inverse-eigenvalue minimax literature may contain an equivalent formulation; publication priority is not independently established.

## Mathematical value

**PASS.** The complete shadow is an experimentally meaningful distributional operator invariant, but it does not fix the operator norm. The theorem quantifies the *smallest possible norm consistent with the entire shadow* on the first two-dimensional strictly positive nilpotent-shift fibre. The exact thresholds distinguish unattained, two-point, unique, and continuum minimizer regimes. They determine sharp boundaries of norm identifiability rather than a minor numerical improvement.

## Closest literature and limitations

Relevant sources: Dunkl et al., *Numerical shadows: measures and densities on the numerical range*, arXiv:1010.4189 (complete-shadow determinant equivalence and radial data); Johnson, *Numerical Shadow Rigidity for 3×3 Matrices*, arXiv:2610.29675v1 (three-dimensional rigidity); Penskoi, *The Volterra system and topology of the isospectral variety of zero-diagonal Jacobi matrices*, arXiv:math-ph/0701061 (isospectral geometry); and Martínez Torres, *The topology of tridiagonal isospectral sets*, arXiv:2609.05733 (broader topological classification). The result is not a claim about arbitrary shadow-equivalent matrices, larger shifts, or a sharp upper norm bound. Publication priority and independent mathematics review remain open.

Self-review: passed. Independent audit: not yet performed.
