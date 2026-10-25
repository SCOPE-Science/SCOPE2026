# Independent mathematical audit

## correctness

PASS

Fix k≥2 and b_i≥1, choose pivot p maximizing b_p. H(t)=((t_j-t_p) mod b_j) for j≠p maps the product of label alphabets onto C=prod_{j≠p}Z/b_j, and every fixed-coordinate slice still surjects: when nonpivot t_i fixed, choose t_p congruent to t_i−d_i mod b_i, possible since b_p≥b_i; other coordinates follow. |C|=min_i prod_{j≠i}b_j. Under |C|≥r, surject π:C→R; for each neighborhood tuple choose fallback point in common intersection. Outcome π(H(t)) when in intersection, fallback otherwise gives inclusion in each chosen neighborhood; common reachable range and slice surjectivity give reverse inclusion for each target point and fixed action. The one-neighborhood full-range frame forces each complement-product≥r by counting completion profiles. Independent exhaustive check of all 3-agent budgets b_i=1..4 confirmed surjectivity on every coordinate slice, including unit cases; universal theorem from constructive proof.

## originality

PASS

PASS best of knowledge relative to Ciardelli 2026 Theorem 2.2 and published Resultary records 4bce89f50bf5, 114a0e0912e6. The source primary paper supplies a world-sized auxiliary action coordinate; the later root-size record has necessary complementary-product inequalities and an equal-budget construction, not hetero sufficiency. Mixed-modulus slice-surjective array is a new nontrivial ingredient, unless an equivalent older mixed-level covering array is shown.

## value

PASS

The complete heterogeneous Pareto budget region is a natural representation-cost classification, not a parameter rename: e.g. (3,4,4) universally realizes r=12 with strictly fewer first-agent copies than the symmetric 4,4,4 construction. Such exact per-agent tradeoffs are useful for finite multi-agent game representations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
