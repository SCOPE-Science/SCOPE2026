# Self-review

## Correctness — PASS
The claim and proof concern one fixed point and positive integers \(k\ge1\). The full length-\(3^k\) starting windows through the first collision lie within the explicit prefix \(U0^{3^k}U\). The proof distinguishes all left-side windows by rightmost-one positions, all right-side windows by leftmost-one positions, rules out every cross-side equality before the threshold using one counts or support separation, and supplies the matching pair at positions \(3^{k-1}\) and \(5\cdot3^{k-1}\). Direct finite checks with two sequence generators agree through \(k=8\). There is no reliance on finite extrapolation.

## Originality — PASS within documented access limits
The closest source introducing the invariant is Nicholson–Rampersad (2015); its publicly accessible abstract names evaluations for Thue–Morse, Fibonacci, and Tribonacci words, not the Cantor word. The source's full text remained inaccessible, so absence of a hidden Cantor example cannot be asserted. Chen–Lü–Wu (2016) establish Cantor factor and permutation complexity, not first repetition locations. Factor complexity does not imply an initial collision law: even changing the origin changes initial non-repetitive complexity while preserving the factor language. Searches for first-repeated length-\(3^k\) Cantor factors, aliases of initial non-repetitive complexity, and stronger source coverage found no equivalent evaluated law. Residual risk: an uninspected statement in the 2015 paper or unindexed work.

## Mathematical value — PASS
Initial non-repetitive complexity was introduced to measure when the first repeated window appears, distinct from the number of factors globally. The Cantor word has exceptionally sparse, self-similar ones and long zero gaps, making its prefix collision geometry a natural different regime from the classical recurrent examples. The result gives an exact all-scale threshold, a unique identified first-collision partner within the initial range, and a nontrivial limiting fraction \(5/6\) of the known factor-complexity count at triadic scales. It is not a generic consequence of computing ordinary factor complexity.

## Scope and limitations
No nondyadic-length formula is asserted. The proof is self-contained and uses finite substitutions, but an equivalent inaccessible literature result remains possible. Computational checks and this self-review are not external validation.

Self-review: passed. Independent audit: not yet performed.
