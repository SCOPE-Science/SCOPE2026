# A unique maximal ternary synchronization string at the published \(12/13\) benchmark

## Finding

Let \(\Sigma=\{0,1,2\}\) and \(\varepsilon=12/13\). Among finite strict \(\varepsilon\)-synchronization words, the maximum length is exactly \(123\), and exactly six words attain that length. They are all alphabet permutations of the following explicit word:

```
010210120212010201202101210201021201210120212010201210212021012102010210120212010201210120102120210121020120212010201210212
```

Thus there is **one extremal word up to relabeling**. Its symbol counts are \((41,41,41)\), it is invariant under reversal accompanied by complementing the alphabet \(0\leftrightarrow2\), and its maximum adjacent-block normalized common-subsequence ratio is exactly \(58/63\). Among alphabet-normalized valid words there are exactly four of length \(122\), one of length \(123\), and zero of length \(124\). The complete positive-length prefix census contains \(76{,}864\) nodes. The published numerical bound \(12/13\) itself is **not** claimed as new; the claim here is the exact terminal length and uniqueness at this established benchmark.

## Assumptions and scope

A word \(w=w_0\cdots w_{n-1}\) is *strictly \(\varepsilon\)-synchronizing* if for **all** integers \(0\le i<j<k\le n\), its adjacent nonempty factors \(u=w[i:j]\) and \(v=w[j:k]\) satisfy

\[
\operatorname{ED}(u,v)>(1-\varepsilon)(|u|+|v|),
\]

where edit distance allows insertions and deletions, with no substitutions. Equivalently,

\[
2\operatorname{LCS}(w[i:j],w[j:k])<\varepsilon(k-i).
\]

At \(\varepsilon=12/13\) we test the **integer** inequality \(26\operatorname{LCS}<12(k-i)\). This is a strict boundary; equality is a violation. Alphabet symbols are distinguishable when counting six words; normalization by alphabet permutations is used only to make the exhaustive enumeration finite and smaller. No constraint of equal adjacent-block lengths is imposed.

## Proof

**1. Prefix closure and exhaustive recursion.** If a word is admissible then all its prefixes are admissible, since each forbidden triple of intervals of a prefix also appears in the whole word. Every admissible word has a unique representative under global permutations of the alphabet in restricted-growth form: the first symbol is \(0\), and a subsequent symbol belongs to the already seen symbols or is the next unused symbol. Thus each normalized prefix has at most three children and is tested by appending each permitted symbol. Every normalized word occurs in this tree exactly once.

**2. Complete validity test.** When one symbol is appended to a valid prefix, all previously checked interval triples remain valid. Hence it is necessary and sufficient to test new triples whose right endpoint is the new word length \(n\). For each split \(1\le j<n\) and left endpoint \(0\le i<j\), the checker calculates \(\operatorname{LCS}(w[i:j],w[j:n])\) by the standard exact integer dynamic-programming recurrence; it rejects the appended word if \(26\operatorname{LCS}\ge12(n-i)\). The two compiled verifiers use algebraically different LCS methods: a classic scalar DP and a bit-parallel DP. The scalar implementation's induction is the usual LCS recurrence with the two segments read backwards. The bit-parallel implementation represents all DP row differences as bits and updates them through bitwise masks and arithmetic subtraction. Both compute the same integer LCS without heuristics or floating point.

**3. Exhaustion certificate.** The complete tree search capped at length \(124\) produced exactly \(76{,}864\) normalized valid nodes at lengths \(1\) through \(123\), including \(4\) nodes at length \(122\), \(1\) node at length \(123\), and **zero at length \(124\)**. Both independent implementations output identical numbers at each of all \(123\) depths, and the same length-\(123\) word; the entire count table is provided in `certificates/counts.csv`. All shorter candidates and all allowed extensions are exhaustively traversed by the stated recursion, not sampled. Since any word of length at least \(124\) would have an admissible prefix of length \(124\), none can exist. Conversely the supplied word is admissible; therefore the maximum is exactly \(123\).

**4. Uniqueness and symmetry.** Restricted-growth normalization identifies precisely the orbits of alphabet permutations. The unique normalized length-\(123\) word contains all three letters, so its six permutations are distinct. The explicit word has \(41\) occurrences of each letter, and satisfies \(w_t+w_{122-t}=2\) for every \(0\le t\le122\). Thus reversal equals complementation, which maps it into its unique relabeling orbit.

**5. Precise margin.** A third independent Python implementation of the ordinary two-string LCS algorithm checks all interval triples for the explicit witness and verifies that the largest ratio \(2\operatorname{LCS}/(k-i)\) is \(58/63\). Ten interval triples attain this ratio, for example \((i,j,k)=(24,54,87)\), with \(\operatorname{LCS}=29\). In particular \(58/63<12/13\), so the witness satisfies the strict criterion.

## Verification

The original standalone verification files are `certificates/search_classic.cpp`, `certificates/search_bitparallel.cpp`, `certificates/check_witness.py`, `certificates/witness.txt`, `certificates/counts.csv`, and `certificates/replay_output.txt`. Using C++17 and Python 3, from the package root run:

```bash
c++ -O3 -std=c++17 certificates/search_classic.cpp -o classic
c++ -O3 -std=c++17 certificates/search_bitparallel.cpp -o bitparallel
./classic 12 13 124
./bitparallel 12 13 124
python3 certificates/check_witness.py
```

All three were run successfully. The C++ outputs agree on the entire depth count table, with exactly \(76{,}864\) nodes and a single normalized terminal word. An automatic consistency check compared the outputs to the provided CSV. Source code and complete output data, rather than a log alone, substantiate the exhaustive computer-assisted proof.

## Relationship to prior work

Cheng, Haeupler, Li, Shahrasbi and Wu (2018), Appendix A, report the **previously known finite-search numerical obstruction** \(B_3\ge12/13\) in the ternary synchronization-string problem. This does not specify the exact maximum finite length at the boundary, the number of extremal words, or reversal-complement symmetry. These finite-data classification claims are the subject here; the numerical lower bound is explicitly credited to that earlier work.

Xu, Fu, Qiao and Tao (first public September 3, 2026) establish ternary synchronization strings of unbounded length for sufficiently larger \(\varepsilon\). Their asymptotic existence result does not imply the terminal finite length or uniqueness at the much smaller value \(12/13\). Camungol and Rampersad (2016) treat approximate repetitions of two equal-length adjacent blocks, while the present synchronization constraint quantifies over unequal-length pairs as well. Searches of indexed mathematical results and accessible related literature did not locate an equivalent published exact-length-and-uniqueness classification. Unindexed computational searches could nevertheless exist.

## Limitations

This is a computer-assisted **finite** extremal classification for the fixed ternary alphabet and strict value \(\varepsilon=12/13\). It does not improve the published asymptotic lower bound or determine the optimal ternary synchronization threshold. The recursions and complete count data are reproducible, but there has been no independent external mathematical audit or exhaustive priority certification. A past unpublished enumeration underlying the 2018 bound may have already found the same finite extremizer; this risk is not eliminated by absence of a printed theorem. The strict-versus-nonstrict endpoint convention must not be changed when interpreting the counts.

## References

1. K. Cheng, B. Haeupler, X. Li, A. Shahrasbi and K. Wu, *Synchronization Strings: Efficient and Fast Deterministic Constructions over Small Alphabets*, arXiv:1803.03530 (2018), especially Appendix A. https://arxiv.org/pdf/1803.03530
2. H. Xu, S. Fu, Y. Qiao and D. Tao, *Synchronization Strings over the Optimal Alphabet*, arXiv:2609.04122, first public 2026-09-03. https://arxiv.org/abs/2609.04122
3. A. Camungol and N. Rampersad, *Avoiding approximate repetitions with respect to the longest common subsequence distance*, Involve 9 (2016). https://msp.org/involve/2016/9-4/involve-v9-n4-p07-s.pdf
