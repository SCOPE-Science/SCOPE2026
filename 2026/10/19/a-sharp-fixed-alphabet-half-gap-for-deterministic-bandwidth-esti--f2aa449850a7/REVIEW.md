# Scientific review

## Correctness — PASS
The one-layer lifting lemma is valid in the useful minimal partial DFA because every residual reachable from a useful residual can be extended to an accepted word. The adjacent-layer inequality follows directly from the definition of the position-unfolding estimator, including the zero layers beyond the maximum accepted length. Pairing successive levels proves the finite bound; separating bounded radii from long radii proves the asymptotic half-gap. For the binary copy-with-gap witness, residual languages at the long middle plateau are distinct singleton suffix languages, giving the matching lower bound. The standalone checker exercised the definitions independently for 1,024 examples, but no finite enumeration is used as an infinite proof.

## Originality — PASS, subject to historical-priority risk
The closest source is Cho--Fazekas--Wiedenhöft, arXiv:2608.24246, Sections 5--6. It supplies the two estimators and their general sandwich bound, an unbounded-alphabet equality example, and a fixed-alphabet question. A material reading of the source did not identify the claimed strict finite comparison or sharp fixed-alphabet half-gap. Prior NFA bandwidth work, arXiv:2606.00663, concerns a different automaton model. Searches comparing the bound names, fixed-alphabet equality, and the constant-half phenomenon found no covering claim; unindexed equivalent work remains possible. The reported contribution is a new relation *between the estimators*, not a new general minimum-bandwidth formula.

## Value — PASS
The sharp asymptotic separation resolves the unbounded-value portion of the motivating paper's fixed-alphabet matching-bounds question in the negative and quantifies the unavoidable estimator slack by a factor approaching two. The matching family shows that the half-gap is structural, not an artifact of proof weakness. This informs when the published upper and lower certificates can and cannot agree for binary and larger fixed alphabets.

## Limits
The actual minimum bandwidth remains between the estimators; bounded-valued equality is possible and not excluded. The closest full text was inspected; no independent scientific audit is asserted.

Self-review: passed. Independent audit: not yet performed.
