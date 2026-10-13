# Self-review

## Correctness
PASS. The claim follows from an exact image-cardinality bound for the subset-sum map \(S\mapsto\sum_{i\in S}k_i\pmod{2^n-1}\). The two lower bounds are elementary consequences of that count, and the source power-of-two bank supplies a matching construction by binary expansion. The proof states the single-use/on/off model explicitly, so target-dependent controlled powers are not silently excluded after the fact.

## Originality
PASS. The primary paper gives the \(n\)-register construction and quadratic catalyst size but no arbitrary-bank lower bound. The later universal-catalyst construction was inspected in full text and uses a target-dependent controlled power of \(U_f\), so it does not cover the fixed-kickback bank theorem. Searches over source identifiers, phase-kickback aliases, subset-sum language, universal-catalyst language, and the exact parameters found no covering statement.

## Value
PASS. This is a sharp structural boundary for the exact mechanism that produced the original quadratic variable-angle overhead. It proves that changing only the bank labels cannot reduce the number of catalyst registers, and that at the register minimum one cannot reduce the worst-case number of active fixed kickbacks below \(n-1\). The later linear-size construction makes the boundary more informative, because it shows concretely which architectural change escapes it.

## Closest literature and limitations
The closest source is Kim's selectable phase-kickback bank, arXiv:2506.15147 / Quantum 10, 2191. The closest stronger resource result is Kim–Laakkonen, arXiv:2512.24982v1, which achieves one universal eigenstate catalyst by controlling a target-dependent power. The result here does not lower-bound that method, general catalytic embeddings, arbitrary repeated kickback use, or \(T\)-count.

Self-review: passed. Independent audit: not yet performed.
