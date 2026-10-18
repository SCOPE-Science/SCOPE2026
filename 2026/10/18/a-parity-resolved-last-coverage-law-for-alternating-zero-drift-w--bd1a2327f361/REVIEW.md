# Scientific review: alternating zero-drift cycle coverage

## Correctness — PASS

The claim is a finite exact distributional identity for every cycle size \(n\ge3\) and every parameter \(0<p<1\). The proof identifies the independent time schedule with a spatial parity-dependent birth-and-death walk on the integer lift, constructs its increasing harmonic scale, and derives last-site probabilities from two gambler's-ruin events. The treatment of endpoint starting positions, normalization, and parity indices is explicit. A separate rational finite-state absorption algorithm confirms all probabilities in the tested small sizes, and the scale-function identity is checked over a much larger finite range. The computations are not used to prove the unrestricted theorem.

## Originality — PASS, qualified

Idnani and Salem's arXiv:2610.15115v1 covers arbitrary time-varying schedules by an unevaluated infinite path series and gives a closed form for constant, rather than alternating, bias. The present result evaluates the complementary period-two schedule in elementary terms and extracts an odd-versus-even parity classification that is not displayed in that paper. Classical symmetric last-vertex theorems and general controller-based cover-time estimates do not assert this law. One general periodic-environment formula might subsume the scale-function derivation; the 1993 source's full text was unavailable, although its accessible abstract specifies the symmetric uniform-choice setting. No claim of independent verification or absolute priority is made.

## Mathematical value — PASS

Last-discovered location is a natural coverage statistic in random walks on rings. The exact law replaces infinite trajectory enumeration for a fundamental periodically forced schedule and reveals a structural obstruction to the naive assertion that a zero-drift two-step motion has uniform coverage risk. Odd and even cycle sizes differ qualitatively: parity-flat versus interlaced linear site profiles. These are complete natural classifications for the stated model, not isolated numerical samples.

## Limits and closest literature

The analysis assumes a specified starting phase, complementary alternating probabilities strictly between zero and one, and one walker. It does not determine joint cover-time fluctuations or general periodic schedules. Relevant literature: arXiv:2610.15115v1 (motivation and general series); Lovász–Winkler, DOI:10.1002/jgt.3190170505 (classical symmetric setting); arXiv:2209.08079v2 (uniform-outdegree digraph setting); arXiv:2006.02475v2 (different controller-based time-dependent cover model).

Self-review: passed. Independent audit: not yet performed.
