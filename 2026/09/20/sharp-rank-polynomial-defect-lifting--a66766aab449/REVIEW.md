# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS**. The defect range is invariant because the polynomial defect commutes with the operator. Cayley–Hamilton on the restriction to this finite-dimensional range produces an annihilating polynomial of degree at most the polynomial degree plus defect rank. Complementing the range gives an upper-triangular block operator whose quotient block is already annihilated by the polynomial; replacing only the defect-range block by a scalar root gives a correction supported inside the defect range with no rank inflation. The noncommutative telescoping formula factors the polynomial difference through the perturbation in at most the polynomial degree many terms, yielding the lower rank-distance bound. The nilpotent, scalar and cyclic-shift examples give the stated sharpness.
- Originality: **PASS**. Barnes 1985 is a close qualitative antecedent: Corollary 11 gives some finite-rank perturbation that makes the polynomial vanish. The inspected source does not state localization of the perturbation inside the defect range, the no-rank-inflation bound, the minimal-polynomial degree bound, or the two-sided rank-distance estimate. No earlier exact quantitative theorem was located.
- Scientific value: **PASS**. The theorem converts one natural defect rank into a sharp degree bound, a correction supported exactly where the defect lives, and optimal universal rank-distance bounds. These are reusable quantitative structural facts, not a mere restatement of qualitative algebraicity.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`. Earlier review evidence is preserved in `AUDIT.json` without being relabeled as fresh independent evidence.
