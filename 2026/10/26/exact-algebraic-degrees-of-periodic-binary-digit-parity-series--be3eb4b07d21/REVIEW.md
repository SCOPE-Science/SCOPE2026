# Scientific review

**Correctness — PASS.** The even/odd digit recurrence gives the explicit Frobenius equation. Cancelling its gcd factor is valid because the factor has constant coefficient one and acts injectively on formal series with vanishing constant term. Bézout's identity transforms the reduced equation into an additive polynomial with right-hand side having a simple pole; the ramification index at that pole is divisible by the full polynomial degree. This proves irreducibility, not merely algebraicity. The coefficient checker corroborates the equations and the independent automaton check corroborates the published \(\mathcal M_2\) specialization.

**Originality — PASS within examined evidence.** The 2026 meta-automatic paper proves the digit-mask identity but not the exact algebraic degree. The 2026 Thue-Morse-transform paper treats weighted digit sums and mask generating series, while the 2025 Rowland–Stipulanti–Yassawi work studies general automata/algebraic-series bounds. Neither inspected theorem supplies the periodic-mask gcd classification. The OEIS entry supplies the mask without this minimal polynomial. Searches under Frobenius, Artin–Schreier, digit-weight, and algebraic-degree terminology did not identify a dominating published result; failed retrieval is not proof of priority. A differently formulated earlier additive-polynomial theorem remains a risk.

**Value — PASS.** Exact minimal algebraic degree is a standard invariant strictly finer than knowing automaticity or an annihilating polynomial. The result gives a closed formula simultaneously for all periods and masks, identifies degree changes caused by shared Frobenius factors, and completely classifies the eight natural period-three cases surrounding the 2026 example. The degree-four meta-automatic case is a concrete motivated application, not the sole contribution.

Scientific limits: Binary, periodic position masks only. Irreducibility is over \(\mathbb F_2(x)\), and published priority beyond examined sources is not certified. Computational checks are finite corroboration.

Self-review: passed. Independent audit: not yet performed.
