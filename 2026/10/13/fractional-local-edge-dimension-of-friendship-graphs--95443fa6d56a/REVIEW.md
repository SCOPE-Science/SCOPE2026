# Review of Fractional local edge dimension of friendship graphs

## Correctness
PASS. For any distinct noncentral vertices \(u,v\), the adjacent center edges \(cu,cv\) are distinguished exactly by \(u\) and \(v\). Hence the local fractional constraints contain \(g(u)+g(v)\ge1\) for every pair among the \(2r\) noncentral vertices, forcing total noncentral weight at least \(r\). Weight \(1/2\) on every noncentral vertex and \(0\) on the center satisfies those constraints and the only remaining adjacent-edge pair type, whose neighborhood has weight \(r-1/2\). Equality in the pairwise system forces all noncentral weights to \(1/2\), so the optimum is unique. Direct LP reconstruction for \(2\le r\le8\) agrees.

## Originality
PASS with a documented access risk. The 2023 source introducing fractional local edge dimension was checked through its bibliographic record, abstract, subject classification, and later literature summaries. Those materials list exact computations for Petersen, Coxeter, cycle, complete, wheel, grid, and complete multipartite families, not friendship graphs. Exact searches under friendship, windmill, FLED, and fractional local edge terminology found no same claim. The full text of that introducing source was not accessible through the available open routes, so a body-text friendship computation cannot be completely excluded. The 2021 primary full text for global fractional edge dimension was inspected directly and proves only the global scalar value \(r\) for friendship graphs.

## Value
PASS. The result determines a newly introduced local fractional invariant on a canonical graph family already important for the global edge invariant. It shows that the local relaxation does not reduce the global fractional edge-dimension value \(r\), and it identifies the unique optimal weighting rather than only the scalar minimum. The proof isolates a clean complete-pair obstruction on the noncentral vertices that can serve as a reusable pattern for other windmill-type graphs.

Self-review: passed. Independent audit: not yet performed.
