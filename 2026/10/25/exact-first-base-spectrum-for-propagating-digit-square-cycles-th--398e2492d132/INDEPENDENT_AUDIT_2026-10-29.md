# Independent mathematical audit

## correctness

PASS

For each base b, every eligible two-digit state 1<=n<b² with r=n mod b!=0 is a vertex of the exact successor functional graph; its cycles are precisely primitive propagating cycles, without missing any eligible states. For each integer b=2..1230, complete traversal of all states proves existence at the stated first bases and nonexistence at every smaller base. Original C++ includes two different exhaustive methods (three-color path tracing and indegree peeling) and explicit witness rows. An independently written optimized C++ DFS fully traversed 620,288,590 eligible states over all 1229 bases and reproduced every one of the 19 values, not just preselected seeds. The maximum is 1230 at length20. It is a bounded finite assertion; no infinite-length conjecture is being inferred.

## originality

PASS

Novelty is a qualified best-of-knowledge mathematical comparison, not a guarantee of priority; exact original claim was searched against equivalent formulations, general theorems and data tables.

## value

PASS

The smallest-base spectrum for a canonical, explicitly posed digit-dynamics problem is a meaningful finite complete classification: the 19 exact minima reveal sharp nonmonotonicity (beta(17)=1120, beta(18)=96) and prove the original uniform existence cutoff 1230 is optimal. Finite exhaustive mathematics is intrinsically valuable here because the invariant concerns a fixed natural cutoff and was explicitly posed in prior work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
