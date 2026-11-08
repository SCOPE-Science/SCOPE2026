# Independent mathematical audit

## correctness

PASS

For two identical additive agents max positive envy after each item equals d=|L1−L2|, so F_(w,W)(d)=min(|d−w|+F_W(|d−w|),d+w+F_W(d+w)). The analytical backward induction on every suffix W in {1,2} establishes (i) F_W(d+2)≥F_W(d) for d≥1, (ii) F_W(0)−2≤F_W(2)≤F_W(0), (iii) F_W(4)≥F_W(0). Verify w=1 base cases F(0)=F(2)=1+f(1), F(1)=f(0); w=2 cases F(0)=F(4)=2+f(2), F(2)=f(0), F(1)=F(3)=1+f(1); general d≥2 or ≥3 follows by shifted successor monotonicity. These imply greedy Bellman choice at every reachable d=0,1,2 and both weights, proving every finite length and tie handling. Scaling by a is valid. For (1,1,k,1) greedy path (1,0,k,k−1) costs 2k; alternate (1,2,k−2,k−3) costs 2k−2, and the only second-stage alternatives d=0,2 prove optimality using z+|z−1| nondecreasing. For any three positive goods, the optimal last-stage cost z+|z−c| is nondecreasing in second-stage d; greedy minimizes it. Independently implemented exact DP checked 8191 binary words lengths 0..12, all three inequalities for 2047 words lengths 0..10 at 0..32, 820 words lengths ≤3 over {1,...,9}, 98 witnesses k=3..100, and 6138 reachable-state Bellman inequalities. Exhaustive finite cases corroborate but do not prove unbounded quantifiers. One nonmathematical typo in RESULT says first two goods go to "the self-review" where the imbalances unambiguously require "the same agent"; the invariant proof and explicit witness remain correct. No claim for real-valued general ratios/zeros/more agents.

## originality

PASS

Best-of-knowledge original all-length myopic-optimality theorem at the strictly positive ratio {a,2a} for the fixed-order cumulative maximum-envy objective, plus sharp integer-alphabet and four-item boundaries. Closest full original source Goldberg–Robinson–Teh (2026) proves binary {0,1} greedy via simultaneous stage lower bounds and general DP, which do not imply greedy optimality for {1,2}. Independent proof supplies new two-step suffix Bellman invariants. Bounded published-results searches produced no same theorem; an unindexed signed-discrepancy/scheduling theorem remains a priority risk.

## value

PASS

The two strictly positive and unequal item values {a,2a} are a natural smallest heterogeneous positive integer alphabet, directly adjacent to binary {0,1} but not reducible by shifting valuations. The exact globally optimal zero-lookahead policy replaces full-future dynamic programming for every fixed sequence length. The dynamic-suffix invariant is nontrivial: a locally suboptimal prefix imbalance can tie in total even for (1,1,2). The four-good witness (1,1,3,1), sharp K=3 threshold and all-positive three-item minimality locate a meaningful structural frontier, not an arbitrary tiny-instance computation. No broad real-ratio or multiagent theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
