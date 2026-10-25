# Mathematical review: Hermitian quartic splitting-fiber spectrum

## Correctness
**PASS.** The smooth plane quartic \(Y^3Z+YZ^3=X^4\) has genus three. The field is explicitly \(\mathbb F_3[t]/(t^6+t+2)\), all inverses are checked, and all \(532171\) rational projective lines and centers are exhausted. A curve-point/line incidence calculation with independent pair counting agrees with a distinct quartic-root line-enumeration implementation. They agree on the 17-value exterior histogram, the line-character histogram, and the 63 exceptional subfield points. The proof of the exceptional locus uses both inclusion and exhaustive multiplicity. An earlier binary completeness claim is properly excluded from the claimed novelty.

## Originality
**PASS subject to residual risk.** The 2022 Korchmáros Irsee slides already say Magma established completeness for the \((892,4)\)-Hermitian arc, and give on-curve incidence counts. The 2023 Korchmáros–Nagy–Szőnyi preprint treats Hermitian arc completeness more generally, while Bartoli–Timpanella (2025) prove large-base-field \(r=3\) completeness. The inspected passages did not state or imply the 17-value *exterior* projection-fiber distribution, its sharp minimum 25, or the 222-fiber subfield maximum. Targeted published-record searches found no matching exterior arithmetic classification, but absence of indexed results cannot prove absolute priority. Unpublished original Magma computations may include the finer data; this remains a scientific residual risk.

## Mathematical value
**PASS.** Rational degree-four projections of a canonical genus-three curve are natural arithmetic morphisms. Classifying their completely split fibers across every exterior center strengthens prior binary arc completeness into an exact distribution, identifies the uniform optimal lower bound 25 for these projections, and characterizes exceptional maximal splitting by descent to \(\mathbb F_9\). The exact numerical spectrum and subfield mechanism are substantive finite arithmetic invariants, independent of a generalization to larger fields.

## Limits
No symbolic general theorem is claimed for other \(q\), and the second verifier is computationally independent but not an external audit. The work does not claim first proof of arc completeness for \(q=3,r=3\). No unpublished external census could be comprehensively ruled out.

Self-review: passed. Independent audit: not yet performed.
