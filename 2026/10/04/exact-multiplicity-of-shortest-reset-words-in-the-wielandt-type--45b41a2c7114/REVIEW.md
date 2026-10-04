# Same-model review

## Correctness
PASS. The proof rewrites reverse preimages in rotating coordinates. Under this conjugation \(b\) fixes the set and \(a\) copies one scheduled bit from \(j+q-p\) to \(j\). Because \(q-p\) is coprime to \(q\), the dependency graph is one cycle. The first possible creation times of the successive states are therefore \(1,1+p,\ldots,1+(q-2)p\), forcing all \(q-1\) productive \(a\)-steps. The initial endpoint is exposed to exactly \(p-1\) harmful scheduled visits before completion, forcing \(b\). All other steps compare equal bits, so either letter gives the identical preimage. Exact power-automaton BFS agrees for every coprime pair \(2\le p<q\le13\).

## Originality
PASS. The defining Gusev--Pribavkina paper was inspected through its full arXiv text. It proves the reset threshold, proves the target of every shortest reset word, and exhibits one shortest word, but does not count all shortest words. published-finding corpus searches for the exact formula, family name, multiplicity terminology, reset-word-language aliases, and stronger coverage found no matching claim. The generic exact-algorithm literature computes shortest words but does not imply this closed family-specific count.

## Value
PASS. The formula refines a classical extremal reset-threshold family by quantifying the degeneracy of the optimum. It reveals that the family has only \(p+q-2\) critical letter positions while all remaining \((p-1)(q-3)\) positions are independent binary choices, a structural fact not visible from the threshold alone.

## Closest literature and limitations
The closest source is Gusev--Pribavkina, which supplies the same automaton and threshold but only a single optimal witness. The claim is limited to the \(n=q\) subfamily and does not cover \(W(n,q,p)\) with \(n>q\) or other primitive-digraph colorings. Literature searches cannot rule out every differently phrased unpublished observation.

Same-model review: passed. Independent audit: not yet performed.
