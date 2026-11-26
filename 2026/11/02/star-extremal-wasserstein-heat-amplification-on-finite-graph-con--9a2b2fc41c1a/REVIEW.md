# Independent mathematical audit

## correctness

PASS

Finite Kantorovich duality and the edge formula for the Lipschitz seminorm reduce the operator norm to evolved edge pairs. The hub mode has eigenvalue −(d+1), while the mean-zero peripheral subspace evolves by e^(−t)R_t with R_t=exp(tQ_H), since Q_H annihilates constants and is symmetric. Fixing the hub potential at zero, the signed hub-edge mass has peripheral coordinates α−a q_v, where a=e^(−t), b=e^(−(d+1)t), α=(a−b)/d and q=R_t(y,·). Optimizing over the larger star potential cube gives dα+a−2 sum min(α, a q_v)≤a+(d−2)α, with equality only if q is supported on one point: either all a q_v<α and the sum is a, or one already contributes α and all others must vanish for equality. A nonisolated y has positive probability of zero jumps and of exactly one jump to a neighbor at any t>0. For an isolate the star-optimal potential with opposite values at y and the other peripheral vertices remains feasible on the cone. For an internal edge, rate-d uniformization gives at least 2/d row overlap at the first jump (at its two endpoints), retained under subsequent steps in total variation. The zero-Poisson term has transport one, and all subsequent terms have transport at most 2−4/d by the peripheral diameter bound. This gives B_d as in the record: for d=2,3 its scaled bracket is strictly below one at t>0, and for d≥4 direct subtraction gives e^t(F_d−B_d)≥(2/d)(1−e^(−dt)). Thus no internal edge can attain the envelope at positive time. At t=0 all edge costs equal one. Differentiation yields F'_d(0)=d−3 and the given unique interior maximum precisely for d≥4. Using the critical-point relation gives the stated peak formula, and expanding its logarithm gives both asymptotics. Inspected the supplied finite numerical checker without running it; it is not the all-graph proof.

## originality

PASS

The star formula and the singleton-blade equality case on clique bouquets are already covered by the matching indexed family statements, without an identifiable priority order on the shared date. Best of current knowledge, the bound on every unit-rate cone, and the timewise isolated-vertex iff classification for an arbitrary peripheral graph, are distinct. The general known transport/curvature equivalences do not yield this profile.

## value

PASS

The sharp benchmark holds at all times on a large natural class, including disconnected peripheral graphs, and equality at any single positive time recovers the presence of a pendant vertex. The result captures transient amplification missed by a pure large-time rate. It does not assert a general diameter-two bound for graphs without a hub or give the individual profiles for nonextremizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
