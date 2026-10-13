# Review

## Correctness

PASS. The source FR equations reduce exactly to a triangular system in the follower ridge error. The distinct-root solution is a geometric divided difference and its repeated-root limit is \(t r^{t-1}\). At resonance, an explicit unit initialization gives a one-step Euclidean amplification that diverges as the coupling grows while both eigenvalues remain fixed.

Risk: this is an exact linear-quadratic transient theorem, not a nonlinear or stochastic bound.

## Originality

PASS. The defining FR paper derives an upper-triangular similarity form and emphasizes that all eigenvalues are real, but does not analyze the surviving off-diagonal block as a source of nonnormal transient growth. The inspected later HessianFR work also does not state the fixed-spectrum amplification family. Published-record searches returned generic Jordan-transient theory but no implication-equivalent FR result.

Residual risk: the linear-algebra mechanism is classical, so originality is specifically in its exact optimizer realization, ridge-coordinate formula, and identification of the defining paper's resonant quadratic.

## Value

PASS. FR's central theoretical narrative is that eliminating complex eigenvalues removes rotational instability. The theorem shows sharply what that spectral statement does not guarantee: real stable eigenvalues can coexist with arbitrarily large state transients, and the repeated-rate resonance already occurs in the canonical quadratic used to motivate the method.

Self-review: passed. Independent audit: not yet performed.
