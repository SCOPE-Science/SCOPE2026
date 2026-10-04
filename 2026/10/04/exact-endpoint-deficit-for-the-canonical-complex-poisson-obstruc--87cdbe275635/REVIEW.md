# Review of Exact endpoint deficit for the canonical complex Poisson obstruction family

## Correctness

PASS. The proof starts from the exact Fourier expansion of the cited unimodular family, applies the Poisson multiplier term by term, reduces the fourth moment to the Hardy \(H^4\) norm of one rational analytic function, and then uses \(\|H\|_4^4=\|H^2\|_2^2\). Summing the geometric coefficient series gives the stated rational expression. Clearing denominators produces the exact deficit factorization. Positivity is not inferred from sampling: the residual polynomial has an explicit tensor-product Bernstein expansion whose coefficients are all nonnegative, and the basis is strictly positive in the open square.

Boundary behavior is consistent: \(\varepsilon=0\) gives the analytic monomial and equality, while \(r\uparrow1\) makes the deficit vanish as expected from Poisson convergence to the unimodular boundary function. The accepted claim is only for \(0<\varepsilon,r<1\), where every denominator is positive and the factorization is strict.

## Originality

PASS. The closest source, arXiv:2609.28938v1, introduces exactly this family in Proposition 4.4 to prove failure for \(\(p>4\)\), but only uses its small-radius limiting function and a supercritical expansion. The same paper explicitly leaves complex endpoint \(\(p=4\)\) Schwarz-contractivity as Conjecture 5.1 and cites prior work only for the limiting \(r\to0\) endpoint. The inspected earlier Brevig--Ortega-Cerdà--Seip paper develops the exponent-\(4\) Riesz-projection obstruction and its two-variable analogue, not a finite-radius Poisson fourth-moment formula.

literature searches for the source, the conjecture, the explicit family, the endpoint fourth moment, and equivalent Poisson/Riesz-projection formulations returned no record stating this all-radius factorization. The new statement is not inferred from search failure alone: it was compared directly against the full relevant sections of the 2026 source and the full earlier primary paper.

Residual risk: a mathematically equivalent finite-radius computation may exist under different notation in literature not surfaced by the searches. No such statement was found in the inspected primary sources.

## Value

PASS. The complex critical exponent is explicitly narrowed by the source to the open interval \([3,4]\), with \(4\) conjectured sharp. The family treated here is not arbitrary: it is the canonical family used to prove that every exponent above \(4\) fails. Showing, by an exact global formula, that this same family is strictly safe at \(\(p=4\)\) for every finite radius rules out the most immediate sharpness mechanism as an endpoint obstruction and supplies a concrete algebraic test case for attempts at Conjecture 5.1. The contribution is a motivated boundary calculation, not a routine recomputation of a known table.

Same-model review: passed. Independent audit: not yet performed.
