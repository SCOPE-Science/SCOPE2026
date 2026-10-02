# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. A fresh exact chip-firing reconstruction on the stated eight-vertex multigraph reproduced the headline vertex rank exactly. For each of the eight vertices q, the class of D* minus q has an effective q-reduced representative; independently enumerating degree-two vertex subtractions found exactly 18 pairs with empty linear system, including (v0,v4). This gives rank at least one and rank at most one, hence vertex Baker-Norine rank exactly one. The committed verifier and certificate agree with the fresh calculation. The RESULT text uses the word “bridges” for the four square edges although those individual edges are not graph-theoretic bridges; that terminology defect does not alter the displayed graph or the rank computation.

Originality: PASS. Published rank theory supplies the general algorithm and the equality between graph rank and the corresponding metric-graph rank, while recent tropical-trigonal papers classify existence of degree-three rank-one divisors under connectivity hypotheses. None of the inspected sources states this named divisor on this named square-backbone genus-five multigraph or gives its exact reduced-divisor certificate. Searches of the published-record index returned this exact record and nearby but different rank examples, not a prior covering result.

Scientific value: PASS. The claim is a motivated exact invariant at the genus-five Brill-Noether boundary, on a small closed loop assembly for which the stated divisor provides a concrete specialness witness. It is not offered as a generic family theorem or a lifting result. The exact reduced-divisor certificate is reusable for later skeleton-specific questions.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
