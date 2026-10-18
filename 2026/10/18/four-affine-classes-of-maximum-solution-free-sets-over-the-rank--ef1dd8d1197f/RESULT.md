# Four affine classes of maximum solution-free sets over the rank-two eight-adic group

## Finding
For the additive group \(G=(\mathbb Z/8\mathbb Z)^2\), a subset \(A\) is **solution-free** for the translation-invariant equation
\[
x+5y=3z+3u
\]
if its only solutions with \(x,y,z,u\in A\) satisfy \(x=y=z=u\). Its maximum size is **exactly eight**.

There are exactly \(98{,}304\) eight-element solution-free subsets of \(G\). Under affine maps \(v\mapsto Mv+t\), where \(M\in\mathrm{GL}_2(\mathbb Z/8\mathbb Z)\), they form **four distinct orbits**, each of size \(24{,}576\). Each maximum set meets every coset of \(2G\) in exactly two points.

Encode \((a,b)\in G\) as the integer \(8a+b\). The four orbit representatives are:

| Class | Eight encoded elements |
| --- | --- |
| I | 0, 1, 8, 9, 20, 21, 28, 29 |
| II | 0, 1, 8, 9, 20, 21, 28, 61 |
| III | 0, 1, 8, 9, 20, 28, 29, 53 |
| IV | 0, 1, 8, 9, 20, 29, 53, 60 |

## Assumptions and scope
All group operations are componentwise modulo eight. Repetitions among the four variables are allowed. Consequently a *nontrivial* solution means any solution in which the four group elements are not all equal, including cases with two or three distinct elements. Equivalence is under the **full** affine group, not merely translation or coordinate permutation. The statement concerns only this specified group and equation; it is not a claim for all ranks or all moduli.

The motivating 2026 study uses the same equation and the same base-eight group structure for large solution-free constructions. Rank two is the first noncyclic case after a single factor, and its exact extremizers provide small-rank constraints and distinct candidate gadgets for larger constructions.

## Proof
**1. Exhaustive forbidden supports.** Three is invertible modulo eight, with inverse three. The equation is exactly equivalent to
\[
u=3x+7y-z\pmod 8.
\]
Thus every solution is generated, exactly once as an ordered quadruple, by one of the \(64^3=262{,}144\) choices \((x,y,z)\in G^3\). For each such triple, form the set of **distinct** vertices \(E=\{x,y,z,u\}\). Omit \(|E|=1\), because this is a trivial solution, and declare every other \(E\) forbidden. This gives exactly \(31{,}152\) distinct forbidden supports of size two, three or four. A set is solution-free if and only if it contains no forbidden support: this equivalence handles repeated variables without omission.

**2. Translation normalization and exact search.** The coefficients satisfy \(1+5=3+3\), so translation by any element preserves the equation. Every nonempty solution-free set can therefore be translated so that \(0\in A\). Order the 64 elements by their integer encodings. Enumerate subsets containing zero by adding vertices in strictly increasing order. For a selected prefix \(P\), keep only vertices whose addition does not complete a forbidden support. The verifier precomputes exact bit masks from all supports of sizes two, three and four. After selecting a new vertex \(v\), it excludes precisely those future vertices that would complete a forbidden pair with \(v\), a forbidden triple with \(v\) and an earlier vertex, or a forbidden quadruple with \(v\) and two earlier vertices. A cardinality bound prunes only branches whose remaining labels cannot reach the target size. Hence induction on the increasing prefix proves that the search visits **every** admissible rooted set of the requested cardinality; there is no random sampling or assumption about a solver.

The exhaustive results are: \(12{,}288\) eight-point sets containing zero, but **zero** nine-point sets containing zero. A larger admissible set would contain a nine-point admissible subset; translating it to include zero contradicts the latter count. Class I above is an explicit eight-point witness (and all four representatives are directly checked). Therefore the extremal size is eight.

**3. Affine-orbit classification.** An invertible matrix over \(\mathbb Z/8\mathbb Z\) is characterized by an odd determinant. There are exactly \(6\cdot4^4=1{,}536\) such matrices, exhaustively listed by their four entries. For a rooted representative \(R\), apply every such matrix and, for each of its eight image points, translate that image point to zero; the resulting set is exactly its rooted affine orbit. Starting with the lexicographically smallest remaining rooted maximum set and removing this rooted orbit partitions all \(12{,}288\) rooted maximum sets into exactly four orbits of \(3{,}072\) rooted sets each. The four representatives in the table are the lexicographically first members of those orbits. This proves both completeness and inequivalence.

**4. Removal of the root.** By translation symmetry, every vertex belongs to the same number \(12{,}288\) of maximum sets. Counting incidences \((A,a)\), where \(a\in A\), gives \(8N=64\cdot12{,}288\), hence \(N=98{,}304\). Applied within each affine orbit, this gives \(64\cdot3{,}072/8=24{,}576\) sets per orbit. Every listed representative has two members in each coset of \(2G\); affine automorphisms permute these cosets, so the property holds for every maximum set.

## Verification
Execute `python verify_rank_two.py` with Python 3.9 or newer. The standalone program uses built-in exact integer arithmetic, sets, tuples, bit masks, and exhaustive loops. It recomputes all \(262{,}144\) ordered triples, all \(31{,}152\) forbidden supports, both rooted cardinality searches, all \(1{,}536\) invertible matrices, and the four affine orbits. Its asserted outputs are `rooted_eight=12288`, `size_nine=0`, `nodes8=57143`, `nodes9=16096`, `affine_orbits=[3072,3072,3072,3072]`, and `total_extremizers=98304`. The exact finite search is itself a terminating exhaustive proof because the loop ranges and the pruning equivalence are established above.

## Relationship to prior work
Katalin Gyarmati, *Translation-invariant equations in F_p^n and groups* (arXiv:2610.09887v1, first submitted October 7, 2026, primary MSC 11C08), establishes large solution-free sets for this coefficient quadruple, notably in powers of the eight-element cyclic group and, asymptotically, in cyclic groups. Its displayed finite table in Section 4 instead concerns the different equation \(2X+2Y=U+3Z\). The finite rank-two maximum, total count and four affine classes proved here are not among its stated theorems. Paul Hametner and József Solymosi, *Large solution-free sets via combinatorial degenerations* (arXiv:2609.13972v1), obtain large asymptotic constructions for four-variable equations over integer intervals; those estimates do not determine a complete finite affine classification for the present group. This comparison is not a claim of absolute novelty.

## Limitations
This is an exact, reproducible **finite computational classification**, not a uniform bound in dimension. The rigorous search depends on executing and/or independently inspecting the supplied short integer algorithm. No mathematical independence, formal proof-assistant certification, or human referee validation has been performed. The motivating paper's introductory statements and relevant table were accessible; its full later proof sections and the second paper's complete text were not fully inspected, leaving a limited residual prior-art risk. The result does not imply that the square-root exponent is optimal in higher ranks; published asymptotic constructions can exceed it.

## References
1. K. Gyarmati, *Translation-invariant equations in F_p^n and groups*, arXiv:2610.09887v1 (2026), https://arxiv.org/abs/2610.09887.
2. P. Hametner and J. Solymosi, *Large solution-free sets via combinatorial degenerations*, arXiv:2609.13972v1 (2026), https://arxiv.org/abs/2609.13972.
