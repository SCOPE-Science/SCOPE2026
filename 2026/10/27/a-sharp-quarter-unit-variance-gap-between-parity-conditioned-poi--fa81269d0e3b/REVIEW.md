# Review

**Correctness — PASS.** Under strictly positive masses, classical Hurwitz stability and Hermite--Biehler interlacing yield a Bernoulli parameter chain alternating across the two conditional distributions. Integrating the variance kernel against its zero-one alternating count gives the sharp upper and lower quarter-unit bounds. Continuity covers all nonnegative masses with positive conditioning probability. Both equality examples are explicit. The standalone exact-rational verifier checked 53,886 finite cases; it does not substitute for the general proof.

**Originality — PASS, with priority risk.** The most directly relevant full primary paper, Broadie and Petkova (2026), proves conditional real-rootedness and mean/mode bounds, not the sharp two-sided variance comparison. The accessible earlier self-reviewed result on half-unit conditional couplings is not enough to imply a bounded variance difference; a counterexample is supplied in RESULT.md. Searches of relevant mathematical records and the classical interlacing literature revealed no matching sharp statement. A general variance-kernel interlacing lemma might subsume the calculation and remains a documented historical risk.

**Value — PASS.** The result supplies a sharp, dimension-free bound on an interpretable conditional uncertainty difference in ternary score aggregation. It is not a routine normalization check or an arbitrary finite table: its extremal constant is valid for every independent array length and attained in both directions.

The model assumes independent \(\{0,1/2,1\}\)-valued summands and nonzero probabilities for both parity events. No analogous conclusion is established for dependent scores or other supports. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
