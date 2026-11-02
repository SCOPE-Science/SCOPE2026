# Self-review

## Correctness — PASS

The conditional generating function is summed exactly over the geometric emigration, and the stationary functional equation is transformed by \(u=1/(1-s)\). Monotonicity forces its unique stationary anchor and rules out invariant probabilities at \(a\le1\). A Foster–Lyapunov argument with variance \(2y+O(1)\) and drift \(1-a+o(1)\) establishes positive recurrence for \(a>1\). The exact gamma-ratio recurrence supplies the beta-integral constant \(\Gamma(a)^2\Gamma(2-a)\); a monotone Tauberian theorem yields the asserted tail. At and above \(a=2\), the same recurrence gives the precise generating-function singularities. The standalone finite checker passed 990 assertions. Infinite assertions depend on the written argument, not numerical extrapolation.

## Originality — PASS, provisional

Carper (arXiv:2609.06311v1, 2026) treats positive post-reproduction immigration; that model does not directly imply this no-post-reproduction-immigrant stationary tail. An accessible earlier result on the post-immigration chain likewise has a different transition kernel, so its moment law does not cover this theorem. Kosygina–Peterson's excited-walk branching processes do not state the gamma-square coefficient. Searches covering equivalent branching/emigration terminology, stationary PGFs, gamma constants, and primary references did not identify a matching theorem. The abstract of Yanev–Yanev (2004) discusses finite-variance critical branching with emigration–immigration, but the full comparison is unresolved and is a stated historical-priority risk. No claim of exhaustive novelty is made.

## Mathematical value — PASS

The source problem isolates a natural mechanism change—removing the post-reproduction immigrant—and the result gives a complete positive-recurrence threshold, a sharp nontrivial stationary tail constant, and the distinct finite-mean boundary. This identifies the heavy-tail phase in an analytically tractable critical branching process and quantifies a transition obscured by qualitative recurrence statements. It is not merely a finite numerical exercise, parameter renaming, or a reprint of a known table.

## Residual scientific limitations

No pointwise critical \(a=2\) tail coefficient, no transient-time mixing estimates, and no general offspring-law extension are claimed. Historical priority is provisional because broad older emigration–immigration theory was not exhaustively inspected.

Self-review: passed. Independent audit: not yet performed.
