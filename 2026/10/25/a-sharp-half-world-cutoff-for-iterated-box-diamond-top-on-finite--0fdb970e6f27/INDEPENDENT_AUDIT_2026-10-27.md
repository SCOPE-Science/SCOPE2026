# Independent mathematical audit

## correctness

PASS

PASS. Let T_0=empty, T_{r+1}=Pre(U_r), U_r={x:R(x) subseteq T_r}. Both sequences are increasing. Induction on i+j proves T_i intersect U_j=empty: a successor witnessing x in T_i and x in U_j belongs to T_j intersect U_{i-1}, a contradiction. If T_{r+1} differs from T_r, each prior T-step and each U-step is strict (otherwise a fixed point). Thus |T_{r+1}|>=r+1 and |U_r|>=r+1; disjointness yields n>=2r+2. Therefore stabilization by floor(n/2), and a terminal directed path of 2r+2 worlds witnesses the exact lower bound. Explicit recurrence on terminal distance d gives failure at stage j exactly for odd d<=2j-1. Independent exhaustive iteration over all directed relations for n=1..4 produced stabilization histograms {0:2}, {0:12,1:4}, {0:374,1:138}, {0:52056,1:12712,2:768}. This is an infinite combinatorial proof, not extrapolation from n<=4.

## originality

PASS

PASS, best knowledge: the prior Alpay–Başaran work describes paths separating neighboring iterates and selected small-index minima; the all-r lower bound and exact n/2 stabilization follow from the newly identified T_i/U_j separation invariant. Full text of that exact primary was not accessible in this run; the abstract does not prove its absence from appendices, so priority is qualified.

## value

PASS

PASS. Sharp stabilization speed is a natural exact invariant of a variable-free modal operator on arbitrary n-world frames. The two-sided separation lemma rules out half the naively possible iteration length and completely classifies the minimal separation size for every depth. Not a finite search or trivial renaming; relevant to finite-model semantics and fixpoint convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
