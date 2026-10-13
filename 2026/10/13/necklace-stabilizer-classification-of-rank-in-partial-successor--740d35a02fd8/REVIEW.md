# Scientific review

## Correctness: PASS
The theorem is stated for every integer \(n\ge2\) and every binary active mask \(A\subseteq\mathbb Z/n\mathbb Z\), including empty/full masks and wrap-around increments. A word commutes with each translation stabilizing \(A\), so its image contains a full stabilizer coset. In the quotient, a nonzero oriented pair gap \(d\) has an active position whose distance-\(d\) successor is inactive; rotating into that position and applying the partial successor decreases the oriented gap to \(d-1\). This gives explicit compression of every quotient pair, a quotient reset word and the matching upper bound. The fixed-weight Möbius calculation follows from primitive-root decomposition, not numerical guessing. Independent exact subset-state searches and enumerations in `verify.py` agree with the formulas. Those finite tests are not a proof for arbitrary input sizes.

## Originality: PASS, with remaining priority risk
The closest rank source inspected in full is Kari–Ryzhikov–Varonka (DLT 2019), whose Theorem 3 bounds shortest minimum-rank word lengths *given the rank*; their constructed examples do not enumerate minimum rank across all partial-successor masks. Volkov (2023), Rystsov–Szykuła (2023), and Hoffmann (2020) provide synchronization criteria or state-complexity statements with different hypotheses or goals. Exact-statement and equivalent-formulation searches did not identify a stronger covering theorem. General prime-degree and single-active-position synchronization facts are standard, and Möbius inversion itself is classical; the new claim is the uniform symmetry-to-rank identification and consequent full spectrum. Earlier equivalents expressed in different terminology remain possible.

## Value: PASS
Exact minimum rank measures the smallest set of possible states remaining under any control word. For the full natural family of cyclic shift plus partial-successor automata, the theorem gives a closed-form structural decision procedure, a precise synchronization criterion, and the complete rank counts at any fixed active-set weight. It also explains why two circular automata with the same number of active transitions can have different minimum ranks. This is a complete natural classification rather than a finite numerical curiosity.

## Limits
No exact formula for shortest minimum-rank word lengths is asserted. The constructive cubic bound is not claimed sharp. An independent external audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
