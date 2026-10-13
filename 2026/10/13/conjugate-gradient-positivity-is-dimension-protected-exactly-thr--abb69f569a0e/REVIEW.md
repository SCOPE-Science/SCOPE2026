# Review

## Correctness
PASS. The universal part uses only two facts that are reconstructed in the result: \(x^{(1)}=\alpha_0b\ge0\) with \(\alpha_0>0\), and exact CG termination in at most \(n\) steps. In dimension \(2\), the explicit inverse formula for a Stieltjes matrix is entrywise nonnegative, so the terminal iterate is nonnegative. The three-dimensional witness is verified with exact rational arithmetic; its Sylvester minors are positive, its inverse is strictly positive, and its second CG iterate has third component \(-32/3219\).

## Originality
PASS, with stated residual risk. The closest classical sources establish CG finite termination, Krylov-space minimization, and norm convergence, while the closest positivity literature concerns inverse positivity of \(M\)-matrices or algorithms modified to enforce nonnegative constraints. Searches using the aliases “componentwise positivity,” “positive cone,” “inverse positive,” “Stieltjes,” “M-matrix,” “monotone iterate,” and “second CG iterate” did not locate an implication-equivalent minimal-dimension/minimal-iteration theorem. The principal residual risk is older numerical-linear-algebra literature phrased in different monotonicity terminology.

## Value
PASS. For inverse-positive elliptic-type systems, the exact solution respects order, while CG is commonly interpreted through energy minimization. The result identifies the first dimension and first iteration where those two structures diverge: energy-optimal Krylov progress does not imply preservation of the coordinatewise positive cone. The boundary is complete at the smallest dimensions and is witnessed by a small irreducible rational system, making it directly reusable as a diagnostic or test case for positivity-sensitive solvers.

Closest literature and limitations are summarized in `RESULT.md` and `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
