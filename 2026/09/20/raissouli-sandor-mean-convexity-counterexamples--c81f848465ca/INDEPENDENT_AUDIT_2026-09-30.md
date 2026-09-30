# Independent audit — 2026-09-30

**Record:** `2026/09/20/raissouli-sandor-mean-convexity-counterexamples--c81f848465ca`  
**Audited source tree:** `df448a18e2f770b6e55feb3a02cb9dded7ab22e8`  
**Disposition:** passed

## Correctness — PASS

PASS. For q_c(t)=c t^2(2-t^2), 0<c<=1/8 and |t|<1, 0<q_c(t)<|t| off the diagonal, so M_c^- and M_c^+ lie strictly between the two inputs with A between them. The exact partial-derivative formulas together with f>=7/8 and |f'|<=1/(3 sqrt(3)) give a uniform positive lower bound on both coordinate derivatives. Independent differentiation of the section x -> M_c^±(x,1) gives second derivative ∓16 c (x^2-4x+1)/(x+1)^5, which changes sign at 2+sqrt(3). Because convexity/concavity would force the corresponding one-variable section to have one curvature sign, both means are neither convex nor concave.

## Originality — PASS

PASS, to the best of current evidence. The 2016 source explicitly poses Problem 4(ii) with the same symmetric, homogeneous, strictly monotone hypotheses and notes only a nonmonotone counterexample. The same-year characterization literature gives broad representations of homogeneous symmetric monotone means but I found no solution of Problem 4(ii) or equivalent quartic-profile counterexamples. Searches by exact problem wording and by equivalent order/curvature terminology found no covering result.

## Scientific value — PASS

PASS. The record resolves both directions of a published open problem with smooth one-parameter families, not isolated examples, and isolates the structural reason: order relative to A is controlled by the profile value while curvature is controlled by its second derivative.

## Independent checks

- Re-derived both coordinate derivatives and their uniform lower bound.
- Symbolically differentiated the x,1 sections and verified the sign-change polynomial.
- Read the source's exact Problem 4(ii) statement and its convexity/partial-convexity definitions.

## Literature evidence

- https://doi.org/10.1186/s13660-016-1212-z — Raïssouli and Sándor (2016), open-access source; Problem 4(ii) asks exactly the order-versus-curvature question answered here.
- https://doi.org/10.1186/s13660-016-1150-9 — Raïssouli and Rezgui (2016), characterization of homogeneous symmetric monotone bivariate means; no covering solution was located.

## Limitations

- Problem 4(i) is not addressed.
- The result does not classify additional assumptions that would restore the proposed order-curvature implication.
- Equivalent prior examples under substantially different mean parametrizations cannot be excluded exhaustively.

No GitHub write was performed by the audit chat. This file is staged by the guarded `scope-audit-change-set-v1` plan only.
