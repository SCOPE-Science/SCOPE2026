# Self-review

## Correctness — PASS
The claim applies to finite connected simple unicyclic graphs, arbitrary positive edge weights and roots at distance at least one from the unique cycle; it assumes no diagonal potentials. A gauge argument isolates one cycle flux; winding-lift geodesics establish minimal lengths and unique shortest-walk weights. Splitting the return amplitude into real even and imaginary odd series certifies the even-cycle contribution and cancellation of the linear odd-cycle winding sector. The inequality \(2m+2d<2(m+2d)\) for \(d\ge1\) establishes the leading twice-winding term, with no missing lower-order interference. Exact rational checker cases corroborate the formula without replacing the proof. The root-on-cycle boundary requires a different calculation and is excluded.

## Originality — PASS, with residual risk
The comparison is against weighted/chiral continuous-time walks, cycle-flux winding expansions, and published rooted-return/interference theory, rather than matching paper titles. Coutinho et al. (arXiv:2208.08971) focus on exact spectral/average-mixing questions; Frigerio and Paris (arXiv:2207.05168) on swift transport; Chaves et al. (arXiv:2203.13857) on Hermitian directed walks and zero transfer. Luppi (arXiv:2608.12519) explicitly treats cycle-rooted parity onset and general rooted-walk interference, making it the closest antecedent. The inspected description does not give the arbitrary attached-tree, off-cycle-root, distance-dependent weighted coefficients proved here. The full text of that especially relevant source could not be materially examined, so a stronger implication from its general statements remains a concrete priority risk. This review does not establish universal novelty.

## Value — PASS
The first flux-visible power of time quantifies local detection latency of a remote magnetic loop in a coherent transport network. Its exact dependence on graph distance, cycle parity and edge-weight products supplies a natural invariant robust against the shape of off-path tree branches. The unexpected odd-cycle double-winding mechanism, including exact half-flux blindness, sharpens the geometric interpretation of phase response and gives direct design predictions beyond a small-case calculation.

## Verification and limitations
`verify.py` gives exact integer/Laurent and rational checks on 96 graph-weight profiles, including boundary controls. The derivation does not depend on finite enumeration. The source from 2026 was inspected via its publicly accessible abstract/secondary detailed summary, not full primary text. No multi-cycle or onsite-potential generalization is certified.

Self-review: passed. Independent audit: not yet performed.
