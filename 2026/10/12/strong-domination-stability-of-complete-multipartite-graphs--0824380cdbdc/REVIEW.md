# Independent mathematical audit

## correctness

PASS

For N total vertices a vertex in a part of size b has degree N-b and strongly dominates a vertex of a different size-a part iff b≤a. If s=1 the singleton part gives γ=1; if unique minimum s≥2 every vertex in it must be selected, γ=s; if repeated minima s≥2 one from each of two minimum parts suffices, γ=2 and a singleton cannot dominate its own part. For s=1 deletion of all q singleton vertices is necessary/sufficient. For unique minimum s≥2, deletion of one from it changes γ. For repeated s≥2, one deletion creates singleton if s2 or unique smallest s-1≥3 if s≥4, changing γ; exceptional s3 creates unique size2 but retains γ2, and every other single deletion also retains γ2, while two deletions create singleton. Exhaustive partial check all noncomplete partitions through n7 corroborates universal degree logic. The original 2026 paper’s balanced theorem and stated bounds disagree on balanced cases (e.g. K4,4,4 deletion one gives γ3 vs original γ2, stability1), so the current claim is a substantive correction/generalization.

## originality

PASS

PASS best-of-knowledge: The full 2026 Alikhani–Ghanbari–Mehraban–Shojaaldini Ardakani arXiv 2601.03891v2 defines the SAME vertex-deletion stability and treats complete bipartite and balanced multipartite subfamilies, but its statements about balanced graphs are NOT a stronger prior covering this theorem; they conflict with direct degree-order calculation. For K4,4,4 the source states a balanced stability at least 2 (indeed p+1 in its relevant theorem) while deleting just one vertex creates a unique minimum part of size 3 and changes γ from2 to3, giving stability1. For K3,3,3 current formula gives stability2, source gives p+1=4. Vaidya–Karkar older papers treat γ itself, not its deletion stability. Resultary returned different (3,2), Roman, paired and certified domination invariants; no superseding correct arbitrary-profile theorem found.

## value

PASS

The complete arbitrary-part-size classification in terms of the two canonical statistics s,q resolves a natural vertex-deletion stability invariant for all connected noncomplete complete multipartite graphs and corrects incorrect balanced-family assertions in the original 2026 study. The exceptional s=3 and multiplicity threshold are structural, not arbitrary narrow slices or recomputation of known tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
