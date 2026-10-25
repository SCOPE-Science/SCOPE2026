# Independent mathematical audit

## correctness

PASS

C PASS for the fully repaired theorem, NOT for the unmodified finding. The original RESULT.md claimed that for 0<s<(sqrt(5)-1)/2 a symmetrically truncated trapezoid has THREE stable side equilibria. This is false: it has FOUR (base BC, old sides CQ/PB, and new cut side QP). At s=1/2 the exact four projection parameters (BC,CQ,QP,PB) are (1/2,5/6,1/2,1/6); all four lie strictly inside their sides. In fact the symmetric base/cut projections stay at 1/2 and both old projections remain internal until s0=(sqrt(5)-1)/2, where they reach endpoints (1,0). The full corrected RESULT.md replaces the erroneous 3 with 4, documents this phase, and also corrects three literal form-feed escape corruptions in displayed LaTex. Independently reconstructed G=(GT-tu Gcap)/(1-tu), side projection functions, L=t²u-4tu²+6u-3 and R=-4t²u+tu²+6t-3, the QP numerator factorization and M convexity/endpoint signs, and the cap-triangle projection formulas. The quadrilateral has fewer than 3 stable feet only when both old slanted sides fail, forcing tu >= (3-sqrt(5))/2 by fixed-product monotonicity; the alternative retained cap triangle requires removed fraction >3/4. Equality at s0 is degenerate; s>s0 approaches it admissibly with exactly two stable sides. Explicit vertex-touching cuts are covered as continuous limits of strict cuts whenever the retained polygon has nondegenerate stable classification. Independent exact SymPy identities were verified, and a 249x249 rational-grid stress test gave smallest strictly feasible p=0.3844 (grid-dependent); the grid is not an infinite proof. All seven actual source blobs and their Git tree identity were checked against the assignment. The bundled verifier was read but was not used as a stand-alone correctness certificate.

## originality

PASS

Qualified best-of-knowledge PASS for the repaired complete one-line centroid-coupled equilateral-triangle robustness theorem, including sharp infimum and correct four-to-two stable-side transition. The only exact match in published-finding semantic search was this same submitted record, which is not independent earlier evidence. Domokos-Lángi defines/proposes the problem but supplies only decoupled theorems and a square illustration. The exact regular odd-polygon central-cut area profile and the universal offcenter centroid core were materially read and address other invariants. The golden-ratio threshold was not found as an earlier theorem. This is an evidence-limited priority assessment, not proof of global novelty.

## value

PASS

The object is the regular triangle, smallest regular polygon, and the invariant is the minimum fraction of its area removed by ONE line to reduce stable equilibria about the retained body centroid, a reduced model explicitly proposed in Domokos-Lángi. The all-line classification and nondegenerate boundary identify a genuinely motivated exact phase: symmetric trapezoid FOUR stable equilibria before s0, two degenerate slanted-side feet at s0, and TWO stable equilibria above s0. The sharp golden-ratio fraction is a natural reference point for more general robustness of regular polygons. This is not merely a textbook centroid or golden-ratio substitution; it solves a two-variable constrained geometry optimization and checks both retained pieces. It does not solve the unrestricted multi-cut conjecture, nor does it claim that this one triangle calculation guarantees a downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
