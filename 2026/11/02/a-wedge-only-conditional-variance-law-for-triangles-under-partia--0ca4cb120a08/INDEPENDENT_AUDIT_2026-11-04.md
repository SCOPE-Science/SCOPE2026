# Independent mathematical audit

## correctness

PASS

Condition on all present and absent edges of H and partition triangles by number of internal vertices: outside-only and one-internal each have three random edges, two-internal possible triangles indexed by e(H) each have two random cross edges, fully internal triangles are deterministic. Distinct nonzero indicators covary only when sharing one RANDOM edge; if each has r and s required random edges, covariance=p^(r+s-1)(1-p). Enumerate all six unordered dependent class pairs: A0/A0, A0/A1, A1/A1 same internal vertex, A1/A1 different internal vertices, A1/A2, A2/A2; last count N*w(H). All pair counts reproduce the exact RESULT.md polynomial: (C(N,3)+h C(N,2))(p³-p⁶)+eN(p²-p⁴)+2C(N,2)[C(N-2,2)+2h(N-2)+C(h,2)]p⁵(1-p)+4eN(N-1)p⁴(1-p)+2Nw p³(1-p). Deterministic triangle count t(H) appears in conditional mean only. For equal e subtract to get 2N delta_w p³(1-p); claw w=3 vs path w=2 at h4 gives strict witness for N>=1, 0<p<1. At N=0 deterministic; p endpoints allowed only for positive-probability H, formula algebraic otherwise. Independent exact enumeration over all relevant free-edge configurations in selected small n,h,p cases agreed; complete overlap census is all-n proof.

## originality

PASS

Unconditional general triangle count covariance and subgraph overlap formulas already exist (Ellis–Ferry 2010, Kunegis 2014); they furnish counting tools but do not state this graph-conditioned polynomial after full induced revelation. Ginoza–Mugler different edge-swap randomization. Existing generic copy-overlap machinery might imply a specialized formula when one computes this conditional exposure, and that is a real residual risk; no direct covering wedge-only conditional theorem found by Resultary and primary comparisons. Exact triangle-count first conditional moment is elementary prior work, not novelty.

## value

PASS

The natural edge-exposure conditional fluctuation quantity admits a non-obvious collapse from full H topology to only e and w, and gives an exact equal-mean unequal-variance witness. This complete all-n two-statistic law is mathematically motivated for random graph revelation and not merely an arbitrary tiny-instance computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
