# Rule 73 attains the complete determinization bound for elementary cellular-automaton images

## Finding

The complete minimal DFA for the finite-block language of the bilateral one-step spatial image of Rule 73 has **16 states**, including a rejecting sink. Thus the powerset bound for the canonical four-state labeled de Bruijn presentation is sharp even in the restricted setting of elementary cellular-automaton images: all subsets can be reached, and no two can be merged.

## Assumptions and scope

Rule 73 sends exactly the neighborhoods `000`, `011` and `110` to `1`; all others map to `0`. Apply the rule once to arbitrary bilateral binary configurations. The language consists of all finite contiguous words occurring anywhere in the resulting image, including the empty word. Automata read from left to right, require a transition on both letters at every state, and accept by final state. The count 16 refers to recognition of this language, not to a minimal presentation of bi-infinite paths without a distinguished start or to iteration of the cellular automaton.

## Proof

Number the two-letter input states `00`, `01`, `10`, `11` by 0, 1, 2, 3. For each triple `abc`, draw an arrow from `ab` to `bc` labeled by its Rule 73 output. A word of length \(n\) labels a path if and only if it has an input block of length \(n+2\). Such an input block extends arbitrarily to a bilateral input, so finite paths recognize exactly the specified language. Starting from all four states and stopping at any state is allowed. The complete subset automaton therefore starts at mask 15 and accepts precisely at nonzero masks, where mask \(m=\sum_{j\in S}2^j\) encodes the subset \(S\). This also proves the upper bound \(2^4\) for every elementary binary rule in the same setting.

The entries below follow from the eight triples: on `0` the four singleton destination masks in order are \(2,4,3,8\); on `1` they are \(1,8,0,4\). The destination of a subset is the bitwise union of its singleton destinations.

| Mask | On `0` | On `1` | Access word from 15 |
|---:|---:|---:|:---|
| 0 | 0 | 0 | `100111` |
| 1 | 2 | 1 | `111` |
| 2 | 4 | 8 | `1110` |
| 3 | 6 | 9 | `110` |
| 4 | 3 | 0 | `10011` |
| 5 | 3 | 1 | `11` |
| 6 | 7 | 8 | `1100` |
| 7 | 7 | 9 | `11000` |
| 8 | 8 | 4 | `11001` |
| 9 | 10 | 5 | `1101` |
| 10 | 12 | 12 | `11010` |
| 11 | 14 | 13 | `10` |
| 12 | 11 | 4 | `1001` |
| 13 | 11 | 5 | `1` |
| 14 | 15 | 12 | `100` |
| 15 | 15 | 13 | empty word |

The table certifies reachability. For minimality, read each of the words `111`, `11001`, `0111`, `10011` from each singleton. Their masks of possible **starting** states are respectively \(1,2,4,8\), as obtained by backward propagation through the labeled arrows (starting from all possible ending states). Thus testing these four continuations recovers the membership bits of any current subset: a continuation is accepted exactly when that subset contains its unique possible starting state. Any two unequal subsets differ on one such continuation. By the right-language criterion for DFA minimization, all sixteen reachable states are pairwise inequivalent.

## Verification and comparison

The access words and the four backward singleton tests give a finite exact certificate for the minimality of an automaton recognizing words of **arbitrary** length; this is not inference from testing all words up to a length bound. To replay the checks, run `python3 verify.py` in this directory (standard library only).

The standard de Bruijn and subset constructions and their powerset upper bound are not claims of novelty. Wolfram's [Rule 73 properties](https://atlas.wolfram.com/01/01/73/01_01_1_73.html) list Rule 109 as the black–white conjugate, so letter complementation gives the same state complexity for Rule 109. The [catalogue of elementary spatial-image entropies](https://github.com/Resultary/2026/tree/main/2026/10/27/SCOPE-exact-nineteen-value-spatial-image-entropy-spectrum-of-elementar--d4f1725c3486) gives 15 reachable nonempty subsets for Rule 73; a reachable-state count alone does not show that their right languages are different. The [first-offender growth classification](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-a-first-offender-growth-gap-for-all-elementary-cellular-automato--23171f1f1979) concerns a different invariant and already implies that the image is not of finite type. The claim here is tightness of the complete recognizer bound, not the spatial entropy, forbidden-word growth, or series for the number of image words. Historical priority beyond the compared sources is not asserted.
