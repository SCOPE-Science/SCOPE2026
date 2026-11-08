# Independent mathematical audit

## correctness

PASS

Solve convex Beckmann potential for shortcut-flow c: Φ_d(c)=(d+c)²/4+d−c, c=clip(2−d,0,d); equal old-route flows (d−c)/2. This yields C1(d)=2d² (0≤d≤1),2d (1≤d≤2),C0(d)=d(1+d/2) (d≥2), hence Δ(d)=3d²/2−d, d−d²/2, 0 respectively. The globally sharp support q(d)=3/4(d−2/3)(2−d) satisfies Δ−q=(1−3d/2)², (1−d/2)², or 3/4(d−2/3)(d−2), all nonnegative on their domains and zero only at d=2/3 or 2. Taking E uses finite second moment to obtain EΔ≥3/4[(m−2/3)(2−m)−v]. Equality with v=v*(m) forces unique {2/3,2} two-atom law; for any v>v* and 2/3<m<2, choose low points 2/3±eps and corresponding high h=m+v/(m−low)>2 to construct identical first moments but opposite signs. Verified 616 independent exact rational support/moment tests; finite tests supplement algebra.

## originality

PASS

Classical Braess paradox and deterministic Wardrop flow are not claimed new. Nakayama–Watling 2014 full accepted manuscript develops stochastic-flow equilibrium frameworks but not the same realized-demand deterministic Wardrop normalized-network exact moment frontier in inspected sections. Steinberg–Zangwill 1983 examines fixed-demand Braess occurrence, not sharp EΔ lower envelope over nonnegative distributions with fixed first two moments. Zhao–Fu–Wang 2014 logit/elastic-demand work accessible only in abstract, explicitly retained as residual risk.

## value

PASS

Mean and variance are commonly available demand summaries. Exact sign-identifiability frontier under realized-demand user equilibrium is a natural sharp distributionally robust comparison of road additions; the uniquely extremal law and opposite-sign same-moment construction demonstrate what the two moments can and cannot guarantee. Network and latency functions are fixed canonical choices, not all networks or risk-averse equilibria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
