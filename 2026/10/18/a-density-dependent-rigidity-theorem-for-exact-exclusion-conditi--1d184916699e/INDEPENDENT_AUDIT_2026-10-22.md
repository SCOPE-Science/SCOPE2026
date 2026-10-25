# Independent mathematical audit

## correctness

PASS

The killed k-subset generator differs from ordinary exclusion by the exact internal-jump killing potential c_k(A)=sum_{u<v in A}(q_uv+q_vu). Finite-state Feynman–Kac gives a path-law RN derivative proportional to exp(-int_0^T c_k(X_t)dt). If equality holds from a single set over one T>0, this integral must be pathwise constant; positive densities of prescribed jump-time simplices and connectivity of the k-subset exclusion graph force every adjacent state to have equal c_k. For 2<=k<=n-2, comparing k-subsets differing in u,v gives equal (k-1)-subset sums of (w_ux-w_vx); index-replacement proves every symmetrized pair weight equal, and positivity/connectivity yields complete support. For k=n-1, c_{n-1}(V\{v})=W-d_w(v); equality iff weighted degrees equal. Four-cycle has one-hole equality but not two-particle equality. Read verifier’s exhaustive n=3,4 and bounded larger-n capacity enumeration; finite enumeration corroborates only small cases.

## originality

PASS

Shiatis (2026) derives the Feynman–Kac conditioning/exclusion measure change generally, which is acknowledged as prior. The submitted result adds an explicit graph-rate iff theorem at all particle densities, notably a single starting set/horizon rigidity and the exceptional one-hole weighted-regular class. The primary article’s integrable ring/lattice examples and general change-of-measure statement do not provide this subset-sum classification. Resultary searches on collision/exclusion conditioning yielded nearby configurations, not the exact graph-rate equivalence. Best-of-knowledge PASS despite possible classical finite-set-potential alias.

## value

PASS

Exact equality of conditioning-on-survival and rejection-only exclusion is a natural probabilistic equivalence question. The classification gives an abrupt, mathematically motivated density boundary between complete uniform-symmetrized-rate graphs and sparse weighted-regular graphs. Its one-starting-law/one-horizon strengthening and nonreversibility robustness make a complete, reusable structural lemma, not a standalone normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
