# Independent mathematical audit

## correctness

PASS

Each unmatched man–woman pair contributes at most one rank-before-match incidence, else it blocks, so Σ(r_a-1)≤n(n−1), hence L≤floor((n+1)/2). For n≤4, L≤2; at n=5 any stable matching with L=3 has all ten ranks 3 and is simultaneously gap- and regret-optimal (a hypothetical all-ranks≤2 stable matching would block it). Otherwise choose among min-regret matchings a min-gap one with R=q; all others have R≥q+1 and L≤2, hence gap≥q−1≥chosen gap. An independently written direct checker enumerated all 720 perfect matchings of supplied six-pair witness, exactly seven stable, with unique min gap (2,5) identity and unique min regret (3,4) matching (1,0,2,3,4,5). Complete universal n≤5 follows from incidence proof, not the 720-case check. Read verify_independent.py and RESULT.md frozen blobs.

## originality

PASS

Best-of-knowledge: claim-specific mathematical comparisons of exactly defined source objects against established primary results; no matching stronger implication identified in actual searched and materially read sources. Neither a polynomial algorithm for each objective nor related profile/sex-equal compatibility results implies existence of a common optimizer for n≤5 or failure at n=6; the incidence inequality proves the cutoff.

## value

PASS

The exact smallest market size separating two natural stable-marriage fairness objectives gives a meaningful universal boundary and an explicit minimal witness, useful for comparing algorithmic fairness guarantees; finite obstruction itself is accompanied by an all-profile proof for n≤5.

The dated certificate retains the supplied scientific assessment, sources and limitations.
