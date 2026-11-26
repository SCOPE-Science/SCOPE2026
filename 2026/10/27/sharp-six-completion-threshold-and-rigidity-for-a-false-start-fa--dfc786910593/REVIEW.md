# Independent mathematical audit

## correctness

PASS

With y=1−x the signed block polynomial is −∏_{j<i}(1−y^{2^j}), so its first nonzero x coefficient is −2^{i(i−1)/2} at degree i. Translating a block for appending multiplies by y to the preceding length, which leaves this leading coefficient unchanged; appending the prescribed number cancels degree i without disturbing lower degrees. This proves the divisibility test and justifies truncation through degree six in the exhaustion. Sign inversion preserves stage admissibility and exchanges the appended blocks with their complements. At each length there is just one normalized exceptional word; both length-one words are exceptional. The independent bounded replay checked all 131054 normalized nonexceptional words of lengths 2–17, with zero survivors through 16 and the single survivor T4T0 at 17, giving two words before normalization. Direct materialized arithmetic yields stage counts (−1,−1,−1,−1,−2,−4,−12) and length 960 after stage six. The stage-seven coefficient is −192675840, not divisible by 2^21, so the first failed stage is seven. By the source's period theorem the tail repeats T8 (up to its stated sign convention), with least period 256; the two halves are complements, so no proper divisor of 256 can be a period. Period 256 therefore requires stage-six admissibility and cannot occur at a shorter nonexceptional length. Admissibility through six alone does not imply period exactly 256 for other words. This is an exact finite computation for the sixth stage, not a formula for all stages or a formal certificate.

## originality

PASS

The original paper already gives the completion recursion, period correspondence, length-17 construction and general bound giving λ(6)≤17. Credit only the sharp lower bound and uniqueness up to sign at equality, and hence the first length attaining the known witness period. Neither the upper-bound construction nor the period map is new.

## value

PASS

The originating work's λ(i) bounds leave an explicit gap between its witness and the true minimum at stage six. Closing that gap and identifying every equality case resolves a natural exact boundary, and supplies a proved datum on the tightness of the proposed Thue–Morse-based upper-bound family and the attainable periods for short false starts. The value is the lower bound and rigidity, not the already-known witness or a claim to resolve general growth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
