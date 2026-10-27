# Scientific review — period-doubling Lie complexity

## Correctness — PASS
The proof defines the exact all-rotations invariant and derives the parity constraints \(d_{2j}=0\), \(d_{2j+1}=1-d_j\). These rule out both \(11\) and \(0000\). The factor decomposition into substituted factors and their one-place rotations is exact; it yields a bijection of fully present cyclic classes under substitution. The critical reverse implication uses the mutually exclusive parity of \(1\)-positions in even- and odd-phase factors, valid when the preimage has length at least two. The exceptional one-symbol base is checked separately. For odd lengths at least five, a cut between two \(1\)'s forces opposite parities, while the zero- and one-\(1\) cases force four consecutive zeros. The remaining bases \(1\) and \(3\) are completely enumerated. The conclusions hold for all positive lengths, not merely those computed. The independent finite checker verified lengths through 192 and all 96 tested renormalizations.

## Originality — PASS, with residual risk
Bell–Shallit [1] develops Lie complexity and supplies explicit examples for other automatic sequences, but does not give the period-doubling spectrum. Cassaigne–Fici–Sciortino–Zamboni [2] proves two *cyclic* classes at power-of-two lengths for period doubling; that counts classes when merely one rotation is present and does not imply the all-rotations spectrum or the complete classification. Li [3] gives general Lie-complexity theory, not this formula. De Luca–Fici [4] treats Sturmian words. Direct mathematical-record searches for Lie complexity, period doubling, substitution, conjugacy, powers of two and three found no exact prior match. The possibility of an unindexed equivalent expression or an implicit deduction in further automata/Toeplitz literature remains a genuine risk. Search absence alone is not used as proof of novelty.

## Mathematical value — PASS
Lie complexity is a natural invariant of factor languages and their complete cyclic Rauzy structures. General automaticity/boundedness does not identify support, class multiplicity, or representatives. The theorem computes the exact infinite support (two geometric progressions), proves total absence at every other length, constructs the two classes throughout, and explains the entire law by a length-doubling bijection. This is a substantive structural classification of a canonical nonperiodic automatic word, not a finite table extension.

## Limits and closest literature
The result is specific to the fixed point of \(0\mapsto01\), \(1\mapsto00\), and the all-rotations Lie invariant; it does not classify all uniform morphisms. The strongest neighboring coverage is [2, Proposition 17] for a different invariant and [1, Theorem 1.4] for general automaticity; neither contains the concrete asserted spectrum. Additional unindexed or reformulated results cannot be ruled out by the finite search.

Self-review: passed. Independent audit: not yet performed.
