# Exact nine-read reconstruction capacities reveal a finite-length decline

## Finding
For binary words of length \(n\ge 1\), let \(\mathcal B_n(x)\) be the *set of distinct* length-\(n-1\) outputs produced by deleting exactly one symbol from \(x\) and then changing at most one surviving symbol. Define
\[
A_9(n)=\max\left\{|C|:C\subseteq\{0,1\}^n,\ \bigl|\mathcal B_n(x)\cap\mathcal B_n(y)\bigr|<9\ \text{for all distinct }x,y\in C\right\}.
\]
The complete initial profile through length eight is
\[
\boxed{(A_9(1),A_9(2),\ldots,A_9(8))=(2,4,8,16,18,26,26,24).}
\]
In particular, the optimal nine-read codebook cardinality **strictly decreases** between lengths seven and eight, from \(26\) to \(24\); this is the first such decrease in the stated profile. The bound \(A_9(8)=24\) is attained by an explicit code, and a complete finite branch-and-bound certificate excludes any code with \(25\) or more words.

## Assumptions and scope
The channel uses **one exact deletion and zero or one substitution**, not two arbitrary edits, exact-one substitution, or multiplicity-counted outputs. All words and reads are binary. A code's condition is the formal reconstruction inequality \(\lvert\mathcal B_n(x)\cap\mathcal B_n(y)\rvert<9\). No additional balance, distance or ball-size condition is imposed on individual codewords. The definition is meaningful even for a word whose ball contains fewer than nine distinct outputs; in that case obtaining nine distinct physical reads from that particular word is impossible, so the corresponding operational promise is vacuous. The result concerns the mathematical codebook maximum under the published pairwise criterion.

## Proof
For \(1\le n\le4\), all possible outputs have length \(n-1\). Hence \(\lvert\mathcal B_n(x)\cap\mathcal B_n(y)\rvert\le2^{n-1}<9\), so every binary word may belong to a code and \(A_9(n)=2^n\).

For each \(5\le n\le8\), form the finite compatibility graph \(G_n\): its \(2^n\) vertices are indexed by the integers \(0,1,\ldots,2^n-1\), representing their zero-padded binary words, and two distinct vertices are adjacent precisely when their output-ball intersection has size *strictly below nine*. The defining condition says exactly that a code is a clique of \(G_n\). Consequently \(A_9(n)=\omega(G_n)\).

The file `CHECKER.cpp` computes each output ball as a bitset. For every deleted coordinate, it adds the unchanged deleted string and all the words obtained by flipping one remaining coordinate. Thus every possible output appears, repetitions are removed, and there are no extraneous outputs. An independent string-based implementation crosschecks every ball. It then compares all unordered pairs of vertices to construct \(G_n\). The numbers of **incompatible** unordered pairs for \(n=5,6,7,8\) are respectively \(69,555,2373,7835\).

Explicit cliques of sizes \(18,26,26,24\) are stored as exact decimal-index arrays in `CHECKER.cpp`, and every pair in each clique is checked. This gives the four lower bounds.

For the matching upper bounds, the verifier performs exhaustive branch-and-bound for cliques. At every recursion it maintains a candidate set consisting of common neighbors of the vertices already chosen. It greedily and *properly* colors this candidate subgraph by successive independent classes. Any clique contains at most one vertex of each color class. The algorithm processes candidates in reverse nondecreasing color order and prunes only if the current clique size plus the number of available color classes cannot exceed the claimed upper bound. At each unpruned vertex it recursively considers its unprocessed common neighbors, then removes that vertex from the current candidate set. Every possible larger clique is thereby considered in some branch unless excluded by a valid coloring bound. If a clique exceeding the claimed size is encountered, the program exits with failure; otherwise a complete search returning successfully certifies that no such clique exists.

In the actual complete searches, the numbers of recursive nodes for lengths \(5,6,7,8\) were respectively \(19,23,820,6{,}756{,}323\). All completed without finding a larger clique. The upper bounds therefore agree with the explicitly verified lower bounds, proving the stated capacities.

## Verification
Compile and execute from the directory containing `CHECKER.cpp`:

```sh
g++ -O3 -std=c++17 CHECKER.cpp -o checker
./checker
```

`OUTPUT.txt` contains the recorded deterministic output. No external optimization solver, data download or result from a separate run is required. The program verifies two independent descriptions of the channel ball for all \(480\) centers at lengths five through eight, checks every witness, and exhaustively proves the four maxima. It uses the GNU C++ standard library's `_Find_first` bitset helper and thus should be built with GCC/libstdc++.

## Relationship to prior work
Li, Sun and Ge introduced and investigated this fixed-read mixed deletion–substitution reconstruction model. Their 2026 work supplies constructions for nine reads with an asymptotic redundancy bound and states its explicit nine-read theorem for \(n\ge10\); it does not establish the exact unrestricted maxima at lengths five through eight. Their 2025 paper gives other fixed-read constructions and read-coverage bounds, but not this length-resolved nine-read capacity sequence. Song, Cai and Quek (2025) analyze pairwise output-ball intersection upper bounds under additional distance hypotheses, not the unrestricted optimum cardinality of a nine-read codebook at these lengths.

Related exact finite capacities for five reads employ the stronger condition \(\lvert\mathcal B_n(x)\cap\mathcal B_n(y)\rvert<5\). Those capacities do not determine the current larger nine-read maxima: monotonicity in the allowed number of reads supplies only a lower bound, not an exact value. The first finite-length decline at the nine-read threshold is the distinct observation here.

## Limitations
The exact capacity formula covers only lengths one through eight. It gives no classification of all maximum codebooks, no general-length capacity, and no guarantee of nine physically distinct outputs for individual words with smaller balls. The exhaustive upper bound is computer-assisted but finite and inspectable; independent mathematical auditing and publication-priority verification have not been performed. A previously unindexed finite table could affect priority.

## References
- Y. Li, Y. Sun and G. Ge, *Correcting One Deletion and One Substitution with a Constant Number of Reads*, arXiv:2604.25294, first posted 2026-04-28. https://arxiv.org/abs/2604.25294
- Y. Li, Y. Sun and G. Ge, *Binary Reconstruction Codes for Correcting One Deletion and One Substitution*, arXiv:2505.04232, first posted 2025-05-07. https://arxiv.org/abs/2505.04232
- W. Song, K. Cai and T. Q. S. Quek, *Sequence Reconstruction for the Single-Deletion Single-Substitution Channel*, arXiv:2501.03833, first posted 2025-01-07. https://arxiv.org/abs/2501.03833
