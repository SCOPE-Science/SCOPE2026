# A sharp ten-factor test for three-position attractors of the tenth Tribonacci word

## Finding

Let \(T_j=\tau^j(0)\), where \(\tau(0)=01\), \(\tau(1)=02\), and \(\tau(2)=0\). A nonempty factor of \(T_{10}\) is *hit* by a set of positions if at least one occurrence interval of that factor meets the set. A string attractor hits all nonempty factors.

For \(T_{10}\), the least number of distinct nonempty factors whose hit predicates together distinguish the attractors among **all three-position sets** is exactly **ten**. Specifically, the factors \(f_0,\ldots,f_9\) in the table below suffice, and no family of nine arbitrary factors of this word suffices.

## Assumptions and scope

Positions are zero-based and the word is the length-504 iterate starting at \(T_0=0\). A factor is a contiguous substring. A test is the single predicate that the candidate set hits that particular factor; the predicate can use any occurrence of the factor. The theorem concerns a conjunction of such predicates and candidates of exactly three distinct positions. It does not measure complexity of arbitrary decision procedures, testing all sizes, or testing other iterates.

## Proof

For a factor \(u\), write \(S(u)\) for the union of the positions in all its occurrences. The hit predicate for \(u\) is just intersection with \(S(u)\). Keep a single representative of each inclusion-minimal set among the distinct \(S(u)\). A triple that meets those minimal sets meets every factor support, since each support contains a minimal one. For this word there are twelve minimal supports. The factors \(f_0,\ldots,f_{11}\) in the table represent them; the last column records obstruction triples for the first ten.

| Index | Factor \(f_i\) | Obstruction \(W_i\) |
|---:|:---|:---|
| 0 | `1010201001020101` | \((12,148,273)\) |
| 1 | `00102010010201010201001020102010010201010201001020100` | \((43,80,148)\) |
| 2 | `20102010010201010201001020102` | \((23,229,273)\) |
| 3 | `001020100` | \((80,148,293)\) |
| 4 | `20102` | \((80,155,277)\) |
| 5 | `101` | \((84,150,273)\) |
| 6 | `2` | \((80,149,273)\) |
| 7 | `20102010010201010201001020102010010201010201001020100102010102010010201020100102010` | \((80,273,422)\) |
| 8 | `00` | \((80,148,275)\) |
| 9 | `1` | \((81,148,273)\) |
| 10 | `201020100102010` | — |
| 11 | `001020100102010102010010201020100102010` | — |

**Exact finite calculations.** Generate the word, scan all \(\binom{505}{2}=127260\) nonempty intervals, and take the union of their position masks for each literal substring. This gives 80,559 distinct nonempty factors and 79,983 distinct masks. Sort masks by cardinality and discard each mask containing one already retained; this recovers the entire minimal antichain and verifies that it consists precisely of the supports in the table. For each listed \(W_i\), direct intersection checks show that it misses \(S(f_i)\) and hits each of the other eleven minimal supports.

**Upper bound.** Given a list of supports, annotate each position with the bit mask of the listed supports containing it. A triple hits the list exactly if the bitwise OR of its three signatures is the full mask. Group positions with the same signature, and scan unordered multisets of three signature classes with full OR. Multiply the binomial counts of the positions drawn from each class; this includes repeated classes but not repeated positions. For the full set of twelve supports the calculation gives 133 classes and 416 triples. For the first ten supports it gives 65 classes and 416 triples. Every solution for all twelve is a solution for the first ten. Equal finite cardinalities show that their sets of solutions are identical.

**Lower bound for arbitrary factors.** Each \(W_i\) is not an attractor. If some factor \(u\) is missed by \(W_i\), then any minimal support contained in \(S(u)\) must be \(S(f_i)\), since \(W_i\) hits all the other minimal supports. At least one minimal support is contained in \(S(u)\). The same factor therefore cannot be missed by a second witness \(W_j\), \(j\ne i\). A test equivalent to the attractor predicate must reject all ten witnesses, and each tested factor rejects at most one. This proves the bound of ten against *all* choices of factors, including ones with nonminimal supports.

## Verification

The accompanying `certify.py` (Python 3.10+, standard library only) constructs the word and every support, checks the twelve representatives and the ten obstructions in the table, and computes the two exact signature-class counts. Run `python3 certify.py`; the full check ends with `PASS`. As a separate check of the underlying attractor census, `python3 independent_replay.py` exhausts candidate triples using per-position factor identities. The word has ASCII SHA-256 `b791afd79668cf46a43a74bf97563e159fc146b8902a13763ee0fe4191d9049e`. The necessity of ten depends on the obstruction checks and the minimal-support inclusion argument, not on a census of attractors alone.

## Relationship to prior work

The earlier *Exact smallest-string-attractor census for twelve Tribonacci morphic words* [1] enumerates the full family of minimum attractors for this same word (416 triples), including the explicit list in `certificates/attractors.json`. Its proof uses the inclusion-minimal support reduction; the indexed certificate records twelve such masks for \(T_{10}\). Those facts and the preceding stage count of 224 are prior data, not contributions of this theorem. The four-box representation checked by `certify.py` is a compact description of the same listed triples, not a new census. The present theorem instead minimizes the number of factor predicates on triples. An inclusion-minimal support need not be an indispensable predicate on a cardinality-restricted domain: here two of the twelve can be omitted and ten are necessary even if nonminimal supports are eligible.

Schaeffer and Shallit [2, Theorem 6] give the size-three minimum and an explicit optimum for Tribonacci prefixes of length at least four. Dvořáková [3, Example 8 and Theorem 10] puts this size result in the episturmian setting. The simple-Parry work [4] gives related constructions, and [5] enumerates optimal sets for other morphic words. These are not statements about the minimum number of predicates in this test.

## Limitations

This exact finite result applies only to three-position candidates for \(T_{10}\). It does not claim optimality over general tests, or a law for the minimum predicate count along the morphism iterates. The literature comparison is bounded and does not certify historical priority.

## References

1. *Exact smallest-string-attractor census for twelve Tribonacci morphic words*, Resultary record [`1c390833d969`](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exact-smallest-string-attractor-census-for-twelve-tribonacci-mor--1c390833d969), theorem, proof and `certificates/attractors.json`.
2. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, [arXiv:2012.06840](https://arxiv.org/abs/2012.06840), §5, Theorem 6.
3. L. Dvořáková, *String attractors of episturmian sequences*, [arXiv:2211.01660](https://arxiv.org/abs/2211.01660), Example 8 and Theorem 10.
4. F. Gheeraert, G. Romana and M. Stipulanti, *String attractors of some simple-Parry automatic sequences*, [arXiv:2302.13647](https://arxiv.org/abs/2302.13647).
5. M. Banbara et al., *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, [arXiv:2602.16152](https://arxiv.org/abs/2602.16152).
