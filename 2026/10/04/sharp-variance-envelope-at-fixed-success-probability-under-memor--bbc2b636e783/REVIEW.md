# Same-model review

## Correctness
PASS. The proof reconstructs the published variance identity and isolates the only remaining base-law quantity as \(M=s g'(s)=\mathbb E[T_0s^{T_0}]\). The lower endpoint follows pointwise from \(T_0\ge1\). The upper endpoint follows from Jensen applied to the concave polygonal interpolation of \(\phi(x)=x\log(x)/\log(s)\) on the geometric lattice. Equality and nonattainment conditions are checked explicitly, as is the \(\{1,N\}\) approximating family.

## Originality
PASS. The motivating source gives the variance formula and a continuous Jensen estimate but does not classify the exact lattice-constrained feasible set at fixed \(p\). The closest general discrete-restart paper gives moment formulas without this extremal problem. Focused searches for aliases involving geometric restart, coefficient of variation, fixed success probability, and tilted derivatives did not locate an implication-equivalent result.

The closest contextual literature on optimal restart concerns optimization over the restart rate and therefore does not dominate this fixed-\(q\), fixed-\(p\) theorem. A residual risk remains that the same convex-hull statement appears under different terminology in older restart or moment-problem literature.

## Value
PASS. Fixing \(p\) fixes the restarted mean exactly, so the variance envelope is the natural second-order uncertainty question. The adjacent-duration minimizer and long-tail supremizing family give a complete structural answer rather than a routine numerical refinement.

Same-model review: passed. Independent audit: not yet performed.
