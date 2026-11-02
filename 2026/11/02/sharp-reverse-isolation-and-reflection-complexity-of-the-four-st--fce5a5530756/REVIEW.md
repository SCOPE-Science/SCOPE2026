# Scientific review

## Correctness — PASS

The theorem separates the four-letter fixed point from its binary projection, states all quantifiers, and gives a symbolic recurrence for factor complexity. Classwise injection at the boundaries of even/odd substitution windows proves the full \(P(n)=8n-8\) formula. The explicit eight-adjacent-pair lemma proves that `factors8.txt` is the complete infinite-word length-eight factor set, not a prefix approximation; a complete reversal comparison of those 56 factors proves the sharp threshold. Every larger reflected pair would contain a reflected length-eight pair. All seven exceptional reflection values follow from the exhaustive short table and the orbit identity. The attached standalone code was actually run, produced `VERIFY_OK`, and its eight-factor certificate digest was checked. Critical risk addressed: no finite experiment was used alone to establish an infinite assertion.

## Originality — PASS, qualified

The strongest close comparison is Allouche et al., arXiv:2406.09302, generalized Golay–Shapiro section: their input is the **binary coded** sequence, their no-reflection cutoff is length \(15\), and their values for short lengths differ. Coding a four-letter factor can merge distinct symbols and does not preserve reversibility, so that theorem does not imply the present four-letter classification. The earlier *Palindrome complexity* (arXiv:math/0106121, §4.1) also treats binary generalized Rudin–Shapiro palindrome bounds, not the four-letter literal-reversal orbit census. The independent general constructions in *Words avoiding reversed subwords* (arXiv:math/0311121, §2) do not supply this fixed point's sharp profile. The automatic-sequence survey confirms the chosen four-symbol precursor but not this theorem. Relevant public-source, exact-substitution, alias and implication searches plus searchable mathematical-result records found no equivalent claim. This search is not a proof of priority: unindexed equivalent work and results under a conjugate four-state coding remain risks, particularly historic work on palindrome or factor complexity.

## Mathematical value — PASS

The unprojected four-state Rudin–Shapiro word is a canonical natural morphic object in automatic-sequence theory. The exact reflection complexity and sharp finite reverse-isolation threshold are full classical word invariants, not a sample or relabeling of the known binary result. The proof explains structurally how paired parity classes and substitution blocks produce a shorter cutoff than in the binary projection and gives an explicit finite certificate usable in follow-up factor-language studies.

## Verification and limitations

The `verify.py` checker and `factors8.txt` are complete and included with the proof. The certificate is exhaustive for lengths at most eight by the eight-block lemma; it is not a finite-prefix extrapolation. Earlier statements are cited for motivation/contrast, not attributed as this finding. No independent audit has occurred, and novelty beyond accessible searched literature remains qualified.

Self-review: passed. Independent audit: not yet performed.
