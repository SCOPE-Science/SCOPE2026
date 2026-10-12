# Exact quaternary four-symbol mutually uncorrelated codes with single-substitution detection

## Finding
Let \(\Sigma=\{0,1,2,3\}\). A non-overlapping code \(C\subseteq\Sigma^4\) has no nonempty proper prefix of any member equal to the suffix of another member, including the same member. Suppose further that all distinct members of \(C\) have Hamming distance at least \(2\). Then
\[
\max |C|=12.
\]
There are exactly \(24\) distinct maximizing subsets of the labeled alphabet \(\Sigma^4\). Under simultaneous permutations of the four alphabet symbols, these comprise exactly two orbits, each of size \(12\) (equivalently, each has symbol-permutation stabilizer of size \(2\)). In the terminology of Levy and Yaakobi, this says \(A_{MU}(4,4,2,1)=12\) and classifies all equality cases.

Two explicit maximal examples, with strings separated by spaces, are:

```text
C1: 0023 0032 0122 0133 0302 0313 1022 1033 1123 1132 1202 1213
C2: 0022 0033 0123 0132 0302 0313 1023 1032 1122 1133 1202 1213
```

These are representatives of the distinct symbol-permutation orbits; their images under the \(24\) symbol permutations generate all the maximizing codes after duplicate removal.

## Assumptions and scope
The alphabet has exactly four distinguishable symbols. Each word has exactly four positions. Prefix/suffix overlaps of every length \(r\in\{1,2,3\}\), for every ordered pair \((u,v)\in C^2\), are forbidden. Hamming distance is the ordinary number of differing positions, at least two for distinct members. There are no reverse-complement, composition-balance, edit-distance, or biochemical constraints. Codes are sets, not multisets. The orbit relation permits *symbol* relabeling only, not reversal or position permutations.

## Proof
The condition at overlap length one implies the first-letter set \(F(C)\) and the last-letter set \(L(C)\) are disjoint. Every nonempty admissible code therefore belongs to a bipartition class with nonempty proper \(A\subset\Sigma\), \(B=\Sigma\setminus A\), in which each word starts in \(A\) and ends in \(B\). There are exactly \(2^4-2=14\) such ordered bipartitions; allowing multiple possible partitions does not lose any code.

For a fixed partition, construct its eligible-vertex set \(V_A\) from all \(4^4\) words starting in \(A\) and ending in \(B\), retaining only self-non-overlapping words. The unequal endpoint symbols automatically rule out self-borders of lengths one and three. A border of length two occurs precisely for period-two words \(u_0=u_2\) and \(u_1=u_3\). Hence \(|V_A|=16|A||B|-|A||B|=15|A||B|\), which is \(45\) for a \(1+3\) partition and \(60\) for a \(2+2\) partition.

Join two distinct vertices \(u,v\in V_A\) by an undirected edge if (i) their Hamming distance is at least two and (ii) for each \(r\in\{1,2,3\}\), neither prefix of length \(r\) equals the other word's suffix of length \(r\). Then \(C\subseteq V_A\) is admissible **if and only if** \(C\) is a clique of the resulting graph \(G_A\). Thus maximal admissible codes are precisely maximal cliques of these \(14\) explicitly constructed graphs.

The accompanying `verify_primary.py` performs complete Bron--Kerbosch enumeration with pivoting for all fourteen graphs, with exact integer bitsets. Its partition-level complete maximal-clique certificates give maximum \(9\) for each of the eight \(1+3\) or \(3+1\) partitions, and maximum \(12\), attained by precisely four cliques, for each of the six \(2+2\) partitions. Taking the union of the optimal code sets removes possible duplicate representations across partitions and yields precisely \(24\) distinct sets. Acting by all \(4!=24\) alphabet permutations partitions the \(24\) sets into two orbits of \(12\) each. This computes both the global upper bound and the asserted classification; the displayed representatives are verifiable members of those two orbits.

As an independent exhaustive route, `verify_secondary.py` uses a separately written word eligibility and pair-conflict test, and a color-bounded depth-first clique enumerator. Its greedy coloring gives a valid upper bound on the number of vertices remaining in a clique: vertices of the same greedy color cannot coexist in a clique. It counts exactly \(24\) cliques of size \(12\) across the partitions and **no** cliques of size \(13\). Any code of larger size would contain a \(13\)-element clique, so none exists. This independently confirms the optimum, multiplicity, and the partition counts.

## Verification
Use Python 3 with only the standard library, from the directory containing both packaged scripts:

```sh
python3 verify_primary.py
python3 verify_secondary.py
```

Each program terminates with `VERIFY_OK` after checking its assertions. The first reports the fourteen partition maxima, total distinct maximizing codes, and permutation-orbit sizes. The second reports, for each partition, the number of size-twelve and size-thirteen cliques. The enumerations cover all four-symbol length-four words and all possible nonempty code partitions, so they are exhaustive for this **finite** theorem. Their execution does not certify unexamined lengths, alphabet sizes, or other distances.

## Relationship to prior work
Chee--Kiah--Purkayastha--Wang (2012) and Blackburn (2013) study ordinary non-overlapping/cross-bifix-free codes. Blackburn's construction establishes the unconstrained optimum \(27\) at alphabet and word length both four; this has **no imposed minimum distance two** and therefore does not imply the present \(12\)-word bound or classification. Levy--Yaakobi (2018), Definition 6.1, defines exactly the joint Hamming/overlap invariant used here; Theorem 6.1 gives the general bound \(A_{MU}(4,4,2,1)\leq 16\) using \(M(4,4,2)=64\). The exact value \(12\) and its complete equality cases are not given by that theorem or its asymptotic constructions. Work on restricted \((1,k)\)-overlap-free and balanced codes has different constraints or general bounds, and does not by itself determine this joint finite optimum.

## Limitations
Originality is relative to the specifically examined literature, not a guarantee that no unindexed appendix, database, or unpublished enumeration has the same twenty-four code sets. Some related publisher PDFs were unavailable for full-text comparison. The mathematical conclusion covers only \(n=q=4\) and minimum Hamming distance two; it neither proves an all-length formula nor supports error *correction* or reverse-complement avoidance. Codes with distance two detect a single substitution between codewords, but need not correct it.

## References
1. Y. M. Chee, H. M. Kiah, P. Purkayastha, C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236, initial public submission 2012-09-03, https://arxiv.org/abs/1209.0236 .
2. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, initial public submission 2013-03-05, https://arxiv.org/abs/1303.1026 .
3. M. Levy and E. Yaakobi, *Mutually Uncorrelated Codes for DNA Storage*, arXiv:1804.05371, §6 and Theorem 6.1, https://arxiv.org/html/1804.05371v1 .
4. *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography, https://doi.org/10.1007/s10623-023-01344-z .
5. X. Wang, Y. Fang, T. Feng, *q-ary (1,k)-overlap-free codes with given restrictions*, Discrete Mathematics 348 (2025) 114236, https://doi.org/10.1016/j.disc.2024.114236 .
