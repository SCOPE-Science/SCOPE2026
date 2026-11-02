# Independent mathematical audit

## correctness

PASS

PASS. The transformation that deletes the first one and appends it, applied k times, maps the ith zero position z_i to max(i,z_i−k), including k beyond the word’s number of ones. This preserves prefix-zero dominance and therefore monotone lexicographic phase ordering for lower-mechanical Sturmian coding. There are n+1 distinct phase factor intervals cut by fractional parts {−jα}, j=0..n. The final-letter boundary x_n cannot merge because one-count changes. For j=1..n−1, adjacent words are p01s/p10s; they have the same k-step output precisely when prefix p contains fewer than k ones. Its one count is ceil(jα)−1, so exactly min(n−1,floor(k/α)) boundaries merge for irrational α. Thus rho_(α,k)(n)=max(2,n+1−floor(k/α)) for all n≥1,k≥2, and n=0 gives 1. The agreement cutoff floor(k/α)+1 and slope limit k/floor(k/α)→α follow. Independent high-precision irrational mechanical-factor simulation checked 154 (n,k) cases (n=1..22,k=1..7) and reproduced the formula; finite simulation is corroboration only.

## originality

PASS

PASS, best-of-knowledge. Campbell–Rampersad 2026 formally defines iterated tortoise complexity and its Abelian comparison and explicitly invites Sturmian extensions; inspected Sections 3–4 and 7 do not state this all-k Sturmian formula. Defant–Kravitz previously defined the general finite-word tortoise operator but did not calculate Sturmian factor-language profiles. A previously known single-iterate case does not cover k≥2 without the new zero-position/phase-boundary argument. Slope recovery is presented only as a consequence, not separately claimed novel.

## value

PASS

PASS. The complete n,k profile solves an explicit family proposed in recent complexity literature, quantifies an exact sharp phase transition from constant Abelian complexity to linear output growth and determines the irrational Sturmian slope from discrete cutoffs. The method is a structural order/collision lemma for the natural language of irrational rotations, not a small finite test or arbitrary alphabet slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
