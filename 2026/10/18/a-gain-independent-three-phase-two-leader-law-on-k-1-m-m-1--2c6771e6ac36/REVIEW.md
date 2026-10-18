# Scientific review: a gain-independent three-phase two-leader law

## Correctness — PASS

For every integer \(m\ge1\) and positive real feedback gain \(\kappa\), the proof reduces the trace of the inverse pinned Laplacian to effective resistances using the grounded Green matrix and Sherman--Morrison identity. The complete multipartite Laplacian eigenspaces give exact resistances. Rational differences between each competing leader-pair orbit and the proposed optimum have positive denominators and numerators. The \(m\ge4\) inequalities are proved globally by expanding in \(u=m-4\ge0\); the \(m=1,2,3\) cases are shown exactly. The packaged exact-arithmetic script cross-checks the formulas on 320 resistance evaluations and 87 matrix inversions, without treating these finite tests as a proof.

## Originality — PASS, with residual risk

Fitch and Leonard (arXiv:1407.1569, Sections II and V-B--V-D) give the relevant general two-noisy-leader joint-centrality formula and solve paths and cycles. Patterson, Yi, and Zhang (arXiv:1708.06873, Sections III--IV) develop equivalent resistance methods with path/cycle/tree coverage. Clark, Bushnell, and Poovendran (arXiv:1208.0946) study a different noisy-link/fixed-leader model. The present strict, uniform, three-regime \(K_{1,m,m+1}\) law is not stated or implied without new orbit inequalities in the inspected sources. published-finding corpus searches for direct claims and equivalent trace-inverse, pinned-Laplacian, and noisy-coherence formulations found no dominating published record. As with any limited literature search, unindexed or inaccessible equivalent coverage remains possible.

## Value — PASS

A complete structural optimizer classification for two equal-gain leaders is useful for designing noise-resistant control in symmetric multipartite networks. The boundary at \(m=4\), where a universal vertex becomes indispensable and the optimizer switches type regardless of gain, is a nontrivial feature not apparent from vertex degree alone. This result resolves all relevant combinatorial placements on an unbounded natural family rather than fitting a few finite examples.

## Scope and limitations

The result applies only to simple unweighted \(K_{1,m,m+1}\) networks, exactly two distinct leaders, identical finite positive gains, and the trace-inverse variance cost. Heterogeneous gains, arbitrary multipartite sizes, and distinct objectives remain open outside this statement. A self-review is not external verification.

Self-review: passed. Independent audit: not yet performed.
