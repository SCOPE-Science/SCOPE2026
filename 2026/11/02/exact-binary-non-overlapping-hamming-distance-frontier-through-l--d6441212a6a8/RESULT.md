# Exact binary non-overlapping Hamming-distance frontier through length eleven

## Finding

Let \(A(n,d)\) be the maximum cardinality of a set \(C\) of binary length-\(n\) words satisfying both conditions: (i) for every ordered pair \(u,v\), including \(u=v\), no nonempty proper prefix of \(u\) equals an equally long suffix of \(v\); (ii) every pair of distinct codewords has Hamming distance at least \(d\). Singleton codes satisfy (ii) vacuously.

**Theorem.** The following table determines \(A(n,d)\) exactly for every integer pair \(2\le n\le11\) and \(2\le d\le n\). A dash means \(d>n\), outside the stated range.

| Length \(n\) | \(d=2\) | \(d=3\) | \(d=4\) | \(d=5\) | \(d=6\) | \(d=7\) | \(d=8\) | \(d=9\) | \(d=10\) | \(d=11\) |
|:--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 2 | 1 | — | — | — | — | — | — | — | — | — |
| 3 | 1 | 1 | — | — | — | — | — | — | — | — |
| 4 | 1 | 1 | 1 | — | — | — | — | — | — | — |
| 5 | 2 | 1 | 1 | 1 | — | — | — | — | — | — |
| 6 | 3 | 1 | 1 | 1 | 1 | — | — | — | — | — |
| 7 | 5 | 2 | 2 | 1 | 1 | 1 | — | — | — | — |
| 8 | 8 | 3 | 2 | 2 | 1 | 1 | 1 | — | — | — |
| 9 | 14 | 6 | 4 | 2 | 2 | 1 | 1 | 1 | — | — |
| 10 | 23 | 9 | 6 | 2 | 2 | 2 | 1 | 1 | 1 | — |
| 11 | 42 | 14 | 10 | 4 | 2 | 2 | 2 | 1 | 1 | 1 |

In particular the exact length-\(11\) distance profile is
\[ (A(11,2),A(11,3),\ldots,A(11,11))=(42,14,10,4,2,2,2,1,1,1). \]
The maximum non-overlapping code sizes without the extra distance constraint are \(A(10,1)=24\) and \(A(11,1)=44\), as previously established by Chee et al. The stronger requirement \(d=2\) first reduces this optimum at length \(10\): \(A(10,2)=23\) and \(A(11,2)=42\). At length \(11\), a code correcting a single substitution within an already aligned block (\(d=3\)) has at most \(14\) words, and an explicit \(14\)-word code attains this.

## Assumptions and scope

A word is *unbordered* when none of its nonempty proper prefixes is a suffix. The prefix/suffix exclusion must hold for **every** pair, including the same word; this is the strong non-overlapping, cross-bifix-free, or mutually uncorrelated definition. It is not merely the comma-free condition. The Hamming requirement is an aligned substitution distance; no claim is made that a substitution inside an unknown frame boundary preserves the original synchronization guarantee. All codes are arbitrary nonlinear subsets of \(\{0,1\}^n\); there is no balance or constant-weight assumption. Codewords are distinct and not identified under rotation.

The underlying archival starting point is Chee, Kiah, Purkayastha, and Wang's 2012 preprint (arXiv:1209.0236, first posted September 3, 2012). Later material is compared for coverage rather than used to change the source's age classification.

## Proof

**Orientation lemma.** For each \(u\in C\), the length-one self-overlap condition gives \(u_1\ne u_n\). If \(u,v\in C\), the cross-overlap exclusions \(u_1\ne v_n\) and \(v_1\ne u_n\) force the same first symbol in every codeword, and the opposite last symbol. Global bit complementation preserves both hypotheses and cardinality. Consequently it is enough to enumerate words starting in \(0\), ending in \(1\), and unbordered; this loses no optimal code.

For a fixed length \(n\), let \(B_n\) be precisely these candidate words. Form an undirected graph \(G_{n,d}\) with vertices \(B_n\); distinct vertices \(u,v\) are adjacent if their Hamming distance is at least \(d\), and neither nonempty proper prefix of either word equals an equally long suffix of the other. The orientation lemma and definition show the exact equivalence
\[A(n,d)=\omega(G_{n,d}),\]
where \(\omega\) denotes the maximum-clique size. The number of candidate vertices for \(n=11\) is \(284\), so the search is over a finite explicitly specified graph.

The attached `verify.py` enumerates all \(B_n\) using complete integer iteration from \(0\) through \(2^n-1\). For each pair, it tests all \(n-1\) overlap lengths and computes integer Hamming distance. It then runs an exact maximum-clique branch-and-bound algorithm, not a heuristic. Here is the argument that no clique can be omitted by its pruning rule.

At a recursive node keep a selected clique \(Q\) and a set \(P\) of eligible remaining vertices. Properly greedily color the graph induced by \(P\), obtaining independent color classes \(C_1,\ldots,C_t\). List vertices class by class in nondecreasing color index. Process this list backwards. When the currently considered vertex has color index \(j\), all as-yet-unprocessed vertices lie in the first \(j\) independent classes, and hence contain no clique larger than \(j\). If \(\lvert Q\rvert+j\) does not exceed the best known clique, pruning is safe. Otherwise branch on including the vertex, intersect the eligible set with its neighbors, and then remove it before processing the next branch. Thus every potentially improving clique survives some branch; the final best size is the exact graph clique number. This reasoning applies to the full finite graph, not a sample or a solver time limit.

For each of the \(55\) parameter pairs, `certificates.json` supplies an explicit clique of the asserted size. The verifier checks every word, border condition, pairwise cross-overlap and Hamming distance, giving a matching lower bound. The exhaustive maximum-clique search gives the matching upper bound. Independent C++17 code in `verify_independent.cpp` reconstructs the words and edges with character strings and uses its own fixed-word bitset clique search to corroborate all \(55\) numbers. These two computations, together with the orientation lemma and the pruning proof, establish the claimed finite exactness.

For comparison with the previously published \(d=1\) boundary, the same exhaustive graph computation gives \(A(n,1)=1,1,1,2,3,5,8,14,24\) for \(n=2,3,\ldots,10\); Chee et al.'s Table I reports and certifies \(A(11,1)=44\). The displayed \(d=2\) column first differs from the \(d=1\) values at \(n=10\). This comparison is contextual; the new exact theorem itself is the entire \(d\ge2\) table above.

## Verification

The three necessary files are `certificates.json`, `verify.py`, and `verify_independent.cpp`, in the same directory. Run `python3 verify.py` with Python 3.9 or later; it requires only the standard library and produces `VERIFY_OK 55 exact finite parameter pairs` on success. For a separate implementation, compile `c++ -O3 -std=c++17 verify_independent.cpp -o check` and run `./check`; its lines have the form `n,d,size` and may be compared against `certificates.json`. The independent compilation and 55-pair comparison both succeeded, as did execution of the Python verifier. A fresh replay from the final embedded package is required before distribution; no external certifier has been used.

## Relationship to prior work

Chee, Kiah, Purkayastha, and Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236 (initial submission September 3, 2012), give constructions and exact unconstrained \(d=1\) values for small \(n\), including \(A(11,1)=44\). Their Table I separately lists \(42\) as the cardinality of a Dyck-path construction at \(n=11\), not an upper bound for distance-\(2\) codes. The constant-weight nature of the odd-length Dyck construction gives a distance-\(2\) example, but does not prove no larger such code exists.

Blackburn, *Non-overlapping codes*, arXiv:1303.1026 (initial submission March 5, 2013), treats unconstrained non-overlapping code cardinalities and bounds, not the full joint distance frontier. Yazdi, Kiah, and Milenkovic, *Weakly Mutually Uncorrelated Codes*, arXiv:1601.08176 (initial submission January 29, 2016), introduce error-correcting constructions, but their statements do not determine the displayed exact maxima. Levy and Yaakobi, *Mutually Uncorrelated Codes for DNA Storage*, arXiv:1804.05371 (initial submission April 15, 2018), Section 6, treat the exact definitional class for overlap-distance parameter one, but prove general bounds and constructions rather than these exact finite values. The latter work's general upper bound at length \(11\) and overlap parameter one is \(\lfloor2^{10}/11\rfloor=93\) for distance at least two, which does not imply the stronger values \(42\) or \(14\).

An exact maximum for simultaneously non-overlapping *single-deletion* codes is a different invariant. A single-deletion-correcting pair must have Hamming distance at least two, but the converse fails, and distance at least three does not ensure deletion correction. For example, the non-overlapping pair `0000011`, `0010111` has Hamming distance two and disjoint single-deletion sets, whereas the non-overlapping pair `0000101`, `0010011` has Hamming distance three but shares deletion descendant `000011`. Consequently deletion-code counts neither subsume nor establish this exact Hamming frontier.

## Limitations

Exact optimality is proved only for binary length \(2\le n\le11\) and minimum pairwise Hamming distance \(2\le d\le n\). No all-length formula, all-optimum classification, or quaternary extension is claimed. The finite search is completely specified and reproducible, but is not a proof about larger lengths. The priority comparison covers the identified source texts and targeted searches; an unindexed prior exact table could affect novelty. The work has not received an independent scientific audit.

## References

1. Y. M. Chee, H. M. Kiah, P. Purkayastha, and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236, https://arxiv.org/abs/1209.0236 (2012 initial preprint).
2. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, https://arxiv.org/abs/1303.1026 (2013 initial preprint).
3. S. M. H. T. Yazdi, H. M. Kiah, and O. Milenkovic, *Weakly Mutually Uncorrelated Codes*, arXiv:1601.08176, https://arxiv.org/abs/1601.08176 (2016 initial preprint).
4. M. Levy and E. Yaakobi, *Mutually Uncorrelated Codes for DNA Storage*, arXiv:1804.05371, https://arxiv.org/abs/1804.05371 (2018 initial preprint).
