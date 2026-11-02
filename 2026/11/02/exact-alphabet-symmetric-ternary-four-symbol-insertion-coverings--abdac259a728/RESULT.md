# Exact alphabet-symmetric ternary four-symbol insertion coverings

## Finding

Let \(\Sigma=\{0,1,2\}\). A *single-insertion covering code* of length four is a subset \(C\subseteq\Sigma^4\) such that every word of \(\Sigma^5\) has at least one length-four scattered subsequence in \(C\). Call \(C\) *alphabet-symmetric* when \(\pi(C)=C\) for every permutation \(\pi\in S_3\) applied simultaneously to all coordinates.

**Theorem.** The minimum size of an alphabet-symmetric code is exactly \(39\). Exactly \(37\) distinct labeled alphabet-symmetric codes attain that size. Under common reversal of all codewords, they form \(21\) classes: five fixed codes and sixteen pairs exchanged by reversal. Moreover, there exists an unrestricted covering code of size \(31\), so imposing full alphabet symmetry costs **at least eight additional words** relative to the unrestricted minimum. No exact value for the unrestricted minimum is asserted.

## Assumptions and scope

All words are finite and ordered; subsequences need not be contiguous. The insertion radius is exactly one, the source length is exactly four, the target length is exactly five, and the alphabet contains exactly three labeled symbols. Alphabet symmetry means *the whole codebook* is invariant under all six global symbol relabelings, not just that a code can be relabeled into another code. Reversal is an additional equivalence, not assumed in the definition.

## Proof

**Orbit reduction.** The action of \(S_3\) partitions the \(81\) words of \(\Sigma^4\) into \(14\) orbits: the constant orbit \(\{0000,1111,2222\}\) of size three and thirteen other orbits, each of size six. In lexicographic orbit order their representatives are

`0000, 0001, 0010, 0011, 0012, 0100, 0101, 0102, 0110, 0111, 0112, 0120, 0121, 0122`.

The target words \(\Sigma^5\) split into \(41\) orbits under the same action. Since each constant target has only its own constant four-letter subsequence, every covering code must contain all three constant words. An alphabet-symmetric code therefore consists of the constant orbit together with some of the thirteen size-six orbits. If it chooses \(r\) of those, its size is \(3+6r\).

**Exact finite orbit incidence.** For each target orbit, choose its lexicographically least representative \(y\); form the set \(D(y)\) of its at most five distinct four-letter subsequences obtained by deleting one position. Map these subsequences to the fourteen source-orbit indices and obtain a fourteen-bit incidence mask \(m_y\). This mask is invariant over the target orbit because deleting a position commutes with alphabet relabeling. Therefore a selected orbit mask \(B\), which always contains the constant orbit, is covering if and only if \(B\cap m_y\neq\varnothing\) for each of the \(41\) target orbit representatives.

Enumerate *all* subsets of size \(r\le6\) among the thirteen nonconstant source-orbit indices. The exhaustive counts are

| Nonconstant orbits chosen | Covering selections |
|---|---:|
| \(0\) through \(5\) | \(0\) |
| \(6\) | \(37\) |

There are only \(\sum_{r=0}^{5}\binom{13}{r}=2380\) candidate masks in the lower-bound cases and \(\binom{13}{6}=1716\) at equality. The exact deletion, orbit, and mask-generation procedures are implemented in `verify.py` and independently, using base-three indexing, in `verify_independent.cpp`. Thus the finite exhaustive comparison covers every permissible alphabet-symmetric code of size at most \(39\); it is not a sampling argument. It proves both the sharp minimum and the exact number of labeled minima.

**Reversal classification.** Reversing any codeword commutes with global alphabet relabeling and with the one-deletion subsequence relation, so reversal permutes the \(37\) optima. The induced permutation of the fourteen orbit indices, in the representative order above, is

`[0, 9, 5, 3, 13, 2, 6, 12, 8, 1, 10, 11, 7, 4]`.

The finite check finds exactly five fixed six-orbit selections. All remaining \(32\) optima pair under this involution, giving \(5+16=21\) reversal classes.

**Unrestricted witness.** The following explicit collection of \(31\) words covers all \(243\) length-five ternary targets:

`0000, 0011, 0012, 0021, 0022, 0100, 0111, 0122, 0210, 0220, 1000, 1011, 1022, 1100, 1102, 1111, 1120, 1122, 1201, 1220, 2001, 2002, 2110, 2112, 2120, 2121, 2200, 2211, 2212, 2221, 2222`.

Each of the \(243\) target words is checked directly against its complete deletion set in both standalone verifiers. Thus the unrestricted optimum is at most \(31\), whereas the symmetric optimum is \(39\), establishing the asserted lower bound of eight on the symmetry penalty. This concludes the proof.

## Verification

Run `python3 verify.py` from the directory containing the standalone artifacts. Independently compile and run `verify_independent.cpp` with a C++17 compiler, for example `c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent`. The exact observed outputs appear in `verification_output.txt`. Both verifiers independently construct all source and target orbits, enumerate the finite admissible orbit selections, classify reversal actions, and check every target of the unrestricted witness. Neither needs a third-party mathematical library.

## Relationship to prior work

Xie, Sun, and Ge (2026) study insertion-covering bounds and distinguish them from deletion covering; their general theory motivates the present finite, symmetry-constrained extremum. Lenz, Rashtchian, Siegel, and Yaakobi (2019/2021) establish general covering bounds and constructions. Pikhurko, Verbitsky, and Zhukovskii (2024/2025) study asymptotic insertion-covering density; their Example 2 credits Grozea's known exact result for **three-letter words over the ternary alphabet**, a different source length. In particular, that earlier exact \(12\)-word result is not part of the present claim. Pikhurko–Verbitsky–Zhukovskii also use the term *symmetric*, but for **coordinate permutations**, not the global alphabet-symbol permutations studied here. The present theorem instead counts all fully alphabet-relabeling-invariant minima for **four-letter** source words and quantifies their symmetry penalty.

## Limitations

This is a finite exact classification for one alphabet and blocklength under the global \(S_3\)-invariance constraint. It does not determine the unrestricted optimum, generalize the \(39\) bound to other lengths, claim optimality of the \(31\)-word witness, or prove independent publication priority. Source comparisons cannot rule out unindexed computations. The exhaustive computation is logically complete only because the orbit parametrization and all incidence cases are justified and the programs enumerate every reduced candidate.

## References

1. Chengfei Xie, Yubo Sun, and Gennian Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379, initially public June 13, 2026. https://arxiv.org/abs/2606.15379
2. Andreas Lenz, Cyrus Rashtchian, Paul H. Siegel, and Eitan Yaakobi, *Covering Codes using Insertions or Deletions*, arXiv:1911.09944 (2019; later published 2021). https://arxiv.org/abs/1911.09944
3. Oleg Pikhurko, Oleg Verbitsky, and Maksim Zhukovskii, *New bounds for the optimal density of covering single-insertion codes via the Turán density*, arXiv:2409.06425, initially public September 10, 2024; IEEE Transactions on Information Theory 71 (2025), 4260–4266. https://arxiv.org/abs/2409.06425
