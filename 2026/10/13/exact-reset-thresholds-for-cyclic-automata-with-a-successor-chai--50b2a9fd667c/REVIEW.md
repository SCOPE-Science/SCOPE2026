# Independent mathematical audit

## correctness

PASS

For all n>=3 and 2<=k<=n-1, a is cyclic successor and b sends i<k to i+1 and fixes i>=k. The inverse-image method starts from the best singleton {k}, on which exactly k strict b inverse expansions create [0,k]. Every nonfull cyclic interval admits the displayed dominance comparison between inverse a and b, so choosing inverse b only when k is present and 0 absent cannot lengthen the expansion; monotonicity of preimages gives an optimum greedy sequence. Each further full k-state expansion costs n steps, with the final remainder treated by r=(n-1) mod k. Reversing yields a resetting word of the proven minimal length n(ceil((n-1)/k)-1)+k. We independently BFS-enumerated all reachable image subsets for 55 n,k pairs (3<=n<=12); all exact shortest lengths equal formula. That finite enumeration corroborates, not proves, all n.

## originality

PASS

The exact uniform two-parameter reset-threshold equality and closed shortest witness for a rank-n-1 nonidempotent successor-chain letter are distinguishable from known one-point-merge Cerny and broader synchronizability/upper-bound results. Best-of-knowledge originality survives the inspected theorem statements; a renamed equivalent transformation family or earlier short-word result remains plausible.

## value

PASS

Reset threshold is the central exact invariant in synchronizing automata. The parameter k interpolates quadratic versus linear behavior with a sharp arithmetic boundary, and the proof classifies a full natural nonidempotent cyclic-letter family rather than an ad hoc finite example. The shortest-word construction gives independently useful normal form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
