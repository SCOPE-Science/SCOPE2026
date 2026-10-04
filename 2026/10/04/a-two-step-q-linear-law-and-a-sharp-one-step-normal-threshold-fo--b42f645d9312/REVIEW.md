# Same-model review of A two-step Q-linear law and a sharp one-step normal threshold for GDPolyak on quartic Rosenbrock ravines

## Correctness
PASS. The proof begins from the exact gradient of \(f_a(x,y)=x^4+a(y-x^2)^2\). At the curvature-matched short step \(h=1/(2a)\), the vertical coordinate becomes exactly the previous \(x^2\), yielding an exact normal-residual identity. A first short step converts every bounded parabolic-wedge residual into order \(x^4\); a second resets its leading coefficient to \(4/a\). The Polyak step then has an explicit expansion with tangential factor \(3/4\), and composition keeps the trajectory in a bounded wedge. For one short step, the same formulas give the affine scaled-normal map with multiplier \(8a/9\). The numerical replay checks representative stable cases but is not used as proof.

## Originality
PASS. The 2025 primary source defines GDPolyak, presents the canonical Rosenbrock quartic, and gives a general near-linear theorem, but its displayed benchmark uses \(K=100\) and its theorem does not imply arbitrary-accuracy convergence for fixed \(K=2\). The April 2026 follow-up publicly reports a block-length-one numerical baseline on an orthogonally equivalent \(a=1/2\) nonconvex quartic, but its advertised theorem is convex and no exact normal multiplier or parameter threshold was located. Statement-level web searches and semantic published-finding searches did not identify the exact fixed-block normal form or its constants.

The main residual risk is access-related: a verified full PDF of the April 2026 follow-up was not obtainable, so an unseen model-specific derivation there cannot be excluded. This risk is recorded rather than converted into a novelty claim.

## Value
PASS. The finding gives a sharp, interpretable mechanism on the motivating quartic family. It analytically explains why a one-short-step baseline succeeds in the recent \(a=1/2\) experiment, identifies the exact normal-stability boundary \(a=9/8\), and shows that two curvature-matched short steps remove the incoming leading normal mode for every \(a>0\). For the original \(a=10\) Rosenbrock benchmark, this replaces the source's large experimental short-step block by a model-specific constant block and yields an exact asymptotic Q-factor.

Same-model review: passed. Independent audit: not yet performed.
