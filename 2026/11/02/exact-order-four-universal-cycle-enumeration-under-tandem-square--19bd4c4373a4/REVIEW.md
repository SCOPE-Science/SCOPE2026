# Scientific review: tandem-square-avoiding universal cycles

## Correctness — PASS

The exact domain is a labeled alphabet of size \(q\ge2\), a fixed forbidden motif family \(\{abab:a,b\in\Sigma\}\), and a cyclic universal cycle that lists every admissible length-\(m\) factor once, modulo rotation. The proof accounts for the constant-letter squares as deleted loops and all remaining squares as two-cycles. The order-three de Bruijn adjacency satisfies \(A^3=J\), permitting its exact inverse on the zero-sum subspace. The matrix-tree determinant reduction and the complete-graph incidence spectrum yield the closed formula for all \(q\). The BEST factorial exponents count \(q^2\) reduced-degree triple-states and \(q^3-q^2\) full-degree states. Independently, a single valid \((m-1)\)-vertex with unequal in/outdegrees excludes the higher-order Euler circuits. The finite integer-cofactor, exhaustive binary Euler-circuit, and witness tests in `verify.py` passed. Boundary cases \(q=2\) and \(m=1,2,3\) are explicit.

The proof is symbolic for arbitrary alphabet size and order; finite verification is corroboration, not a substitute for it. No independent scientific audit has yet occurred.

## Originality — PASS, with residual priority risk

Chen, Kitaev and Sun (2019 preprint, 2020 journal) already imply **existence at order four** after deleting binary loops/two-cycles; that part is explicitly not new. Their inspected Theorem 2.1 and binary tables do not contain an all-alphabet count of rotation classes for the specific full tandem-square deletion set, nor the higher-order obstruction for a fixed length-four forbidden family. Alhakim (2022) constructs sequences satisfying *separation* conditions; his “square-free” at separation one forbids adjacent equal symbols and is not equivalent to excluding exactly factors \(abab\). Moreno and Matamala (2004/2007) treat lexicographically minimal universal cycles in general forbidden-factor languages; the available abstract does not settle this closed enumeration, but full-text comparison could not be completed.

A previously recovered result on **covering** the excluded squares computes a minimum covering length, not the number of Eulerian cycles on the complementary edge set. Another result on pairwise-distinct four-factors concerns only a strict subset of the permitted language; universal-cycle counts are not additive under taking complements or subsets. Search of published records by both motif and graph-theoretic descriptions did not reveal the stated closed formula. Searches cannot establish uniqueness, so equivalent unindexed formulas remain a residual risk.

## Mathematical value — PASS

The restricted factor language is a canonical finite-type constraint in coding and forbidden-substring problems. Its fourth-order graph has a nontrivial rank-\(\binom q2\) deleted-edge correction, and the resulting determinant collapses to two incidence eigenvalues, giving a fully evaluated formula rather than a determinant requiring exponentially growing matrices. The sharp phase change—from Eulerian coverage at order four to a uniform local obstruction at every higher order—describes a structural limitation of exact one-pass constrained universal sequences. Both the enumeration and the order cutoff are complete infinite-parameter statements, not a small-table exercise.

## Literature limitations and remaining checks

The priority comparison is strongest against the inspected full arXiv manuscript of Chen, Kitaev and Sun and the relevant sections of Alhakim. An inaccessible full text of Moreno and Matamala and possible specialized results on square-edge deletions remain risks; neither an abstract nor a failed index search constitutes full-document noncoverage. The result does not address avoiding squares of all sizes, arbitrary orientation quotients, or error-correction properties.

Self-review: passed. Independent audit: not yet performed.
