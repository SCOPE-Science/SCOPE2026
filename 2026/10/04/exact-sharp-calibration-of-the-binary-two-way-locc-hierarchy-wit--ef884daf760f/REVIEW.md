# Same-model review

## Correctness

**PASS.** The source's exact protocol error is
\[
E(p)=\frac1{16}\left(6-\sqrt{4-3p}-\sqrt{4+5p}\right).
\]
The sum of square roots is strictly concave on \([0,1]\), so it has at most one stationary point. Its derivative vanishes exactly when
\[
25(4-3p)=9(4+5p),
\]
giving \(p=8/15\); the endpoint derivative signs show this is the unique global maximizer of the square-root sum and hence the unique global minimizer of the error. Direct radical simplification gives the stated \(E_*\), one-way gap, and separable gap. The packaged checker independently replays every constant and a dense finite stress test.

## Originality

**PASS, narrowly scoped.** The direct source derives the error function and plots it, establishing only that all interior \(p\) improve on the one-way endpoints. The inspected text does not state the exact minimizing parameter, exact minimum error, or exact largest error gap within the family.

Searches using the exact error formula, the value \(8/15\), the radical \(3/8-\sqrt{15}/15\), and aliases involving two-way versus one-way LOCC returned no covering statement. The earlier two-qubit discrimination paper supplies the separable benchmark but does not optimize this later one-parameter feedback protocol.

Residual risk remains because the calculus is compact once the published formula is isolated; an equivalent simplification could appear in unindexed notes or under a different parameter convention.

## Value

**PASS.** The source uses this family as an explicit operational witness that feedback can outperform one-way communication. The exact optimizer identifies the strongest witness inside the published construction, gives the exact size of its communication advantage, and supplies a reproducible calibration target rather than a qualitative plot. The parameter is intrinsic to the source protocol rather than an arbitrary numerical slice.

Same-model review: passed. Independent audit: not yet performed.
