# Scientific review

**Correctness (PASS).** The entry formula for the absorbing unit-rate chain reduces every endpoint entry to a generating-function coefficient or tail. The sign-angle argument proves impossibility for every positive step when the chain has twelve or more states; exact finite rational coefficients at step three establish feasibility for all smaller chains. The six-state quintic derivative proves uniqueness of its boundary. The standalone verifier checked 1701 exact assertions, including matrix-inverse comparisons.

**Originality (PASS, subject to literature risk).** Lóczi–Ketcheson (2013) studies rational absolute monotonicity, and Higueras–Ketcheson–Kocsis (2015) studies perturbed RK methods. Prior directed-cycle Radau IIA work establishes related six-state small-step failure and an *unbounded* large-step positivity window; it does not cover the absorbing-chain eleven-state existence cutoff or bounded six-state window. The published eight-state fourth-order Padé Markov counterexample concerns another rational scheme. Its full text was inaccessible, leaving specialist overlap risk.

**Mathematical value (PASS).** The result is a sharp all-size threshold for whether any Markov-compatible endpoint step exists on a canonical absorbing chain, plus a complete algebraic safe domain in six states. It distinguishes a true feasibility obstruction from small-step or scalar stability alone, and gives implementable bounds for numerical Markov propagation.

**Limits.** Only equal-rate absorbing pure-birth chains and endpoint nonnegativity are classified. Exact complete intervals for seven through eleven states remain unproved. Search coverage is bounded and not a novelty certificate.

Self-review: passed. Independent audit: not yet performed.
