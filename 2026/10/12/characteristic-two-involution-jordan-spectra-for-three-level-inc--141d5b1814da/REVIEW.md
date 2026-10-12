# Scientific review

## Correctness — PASS

The proof completely reduces \(g^2=1\) to \(N^2=0\) with three dense off-diagonal blocks and diagonal identity over characteristic \(2\). Matrix multiplication makes this precisely \(AB=0\). With ranks \(r=\operatorname{rank}A\) and \(s=\operatorname{rank}B\), the rank of \(N\) is \(r+s+t\), where \(t\) is the rank of the induced map \(\ker B\to\mathbb F_q^a/\operatorname{im}A\). The restriction-and-quotient map is surjective with kernel dimension \(ac-(a-r)(c-s)\). The resulting Gaussian-matrix count and the independent total-count summation agree. The standalone checker exhaustively compares ten small-field, small-size rank spectra, including \(\mathbb F_4\); it is corroboration and not the general proof. Every hypothesis, especially characteristic \(2\), positive sizes, labeled matrix counts and inclusion of identity, is explicit.

## Originality — PASS, with bibliographic uncertainty

The closest direct study, Gargate–Gargate, arXiv:1907.06805v1, was inspected in full HTML, including introduction, main enumeration method and tables; its results require odd characteristic and depend on invertibility of \(2\). The present characteristic-two **rank-refined** formula is not implied by those conclusions. Fornaroli–Pezzott, arXiv:2209.09690v1, inspected in full HTML, studies anti-automorphisms of incidence algebras, a different object. A 2026 Cholesky-fiber paper announces rank-refined counts over the whole upper-triangular algebra; its abstract does not furnish the counts restricted to this three-level incidence pattern. The latter paper's full text was not accessible for a conclusive stronger-coverage check, and older parabolic-nilradical literature remains a residual possibility. Searches of related published mathematical-result summaries produced different matrix and algebra counting problems, not an equivalent fixed-pattern Jordan spectrum. No failed search is treated as a proof of novelty.

## Value — PASS

The invariant is the entire Jordan type distribution of actual order-two units in a natural infinite family of incidence algebras. Characteristic \(2\) invalidates the published odd-characteristic sign argument, while the rank \(r+s+t\) decomposition yields a conceptual stratification with exact coefficients and a useful unrefined count. The theorem is not a routine isolated field sample, a mere reparametrization, or a finite table recomputation. A nontrivial group-theoretic invariant is resolved uniformly in all three layer sizes.

## Scope and limitations

The result counts matrices and Jordan block multiplicities, not conjugacy classes; only complete three-level incidence posets over finite fields of characteristic \(2\) are covered. The source-comparison uncertainty about rank-refined parabolic radical matrices and the unavailable 2026 full text is preserved. Finite enumeration is not a substitute for the rank-fiber proof. No independent audit was undertaken.

Self-review: passed. Independent audit: not yet performed.
