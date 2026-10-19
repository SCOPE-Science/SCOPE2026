# Exact multiplicities of shortest rooted palindrome-complete binary cycles through order eight

## Finding
For an integer \(k\ge2\), let \(\mathcal P_k\) be the set of all binary palindromes of length \(k\). A *palindrome-complete cyclic word* of order \(k\) is a cyclic binary word containing every member of \(\mathcal P_k\) as a contiguous cyclic factor. Let \(L_k\) be its minimum possible length. Let \(R_k\) count the ordinary binary strings \(w\) of length \(L_k\) that represent such cycles and whose first \(k\) symbols are zero. Thus \(R_k\) counts cycles rooted at a specified occurrence of the all-zero palindrome; rotations are not identified unless their resulting rooted strings coincide.

The exact values for every \(2\le k\le8\) are

| \(k\) | \(|\mathcal P_k|\) | \(L_k\) | \(R_k\) |
|---:|---:|---:|---:|
| 2 | 2 | 4 | 1 |
| 3 | 4 | 8 | 2 |
| 4 | 4 | 12 | 2 |
| 5 | 8 | 22 | 8 |
| 6 | 8 | 32 | 40 |
| 7 | 16 | 60 | 6272 |
| 8 | 16 | 74 | 768 |

In particular, the number of shortest rooted coverings drops from \(6272\) to \(768\) between orders \(7\) and \(8\), although each order has exactly sixteen required palindrome patterns. The *multiplicities of cyclic rooted coverings* are the principal assertion. Coincident shortest lengths of **linear** palindrome superstrings already appear in OEIS A330022; they are not asserted to be new.

## Assumptions and scope
The alphabet is \(\{0,1\}\), the factors are **contiguous** (not scattered), and all indexing of a cyclic word is modulo its length. The cyclic word is a linear binary string with cyclic adjacency, not an equivalence class under rotation. Its first \(k\) symbols are fixed at zero for the count \(R_k\). A given cyclic string may have several occurrences of \(0^k\); rooting refers to one specified position and is not a quotient by those occurrences. The theorem concerns exactly the seven orders \(2\le k\le8\), not larger orders or nonbinary alphabets.

## Proof
**1. De Bruijn walk correspondence.** Let \(V=\{0,1\}^{k-1}\). The directed graph on \(V\) has, for each \(v\in V\) and bit \(b\), an edge labeled \(vb\) to the last \(k-1\) bits of \(vb\). Every cyclic binary word of length \(\ell\), with a specified index, gives a length-\(\ell\) closed walk in this graph; the edge labels are precisely its length-\(k\) cyclic factors. Conversely, every such closed walk determines the corresponding rooted cyclic word.

Because every palindrome-complete word contains \(0^k\), root at a designated traversal of the \(0^k\) self-loop. That first loop costs exactly one edge and returns to vertex \(0^{k-1}\). The remaining walk must return to the same vertex and must traverse each palindrome-labeled edge at least once.

**2. Finite expanded graph.** Order the \(m=2^{\lceil k/2\rceil}\) palindromes by binary numerical value, with \(0^k\) first. Use states \((v,S)\), where \(v\in V\) and \(S\subseteq\mathcal P_k\) is the set of palindrome edges visited. Appending a bit \(b\) moves to the usual successor vertex and adds edge \(vb\) to \(S\) exactly when that edge is palindromic. Start at \((0^{k-1},\{0^k\})\), at distance \(1\). The target is \((0^{k-1},\mathcal P_k)\). This exact finite directed graph has \(2^{k-1+m}\) possible states; there are only two transitions from any state.

Unit-weight breadth-first search gives the minimum distance to the target. Maintain an integer path count \(c(v,S)\) initialized to one at the start and zero elsewhere. Whenever an edge enters a state at the same minimum distance, add the predecessor's count. By induction on the BFS layer, this counts *every* shortest path, without duplication. Since the initial \(0^k\) loop has been fixed, paths counted at the target are in bijection with distinct optimal cyclic strings having an occurrence of \(0^k\) fixed at the root. Rotate the fixed loop's ending index to the first index of that zero window to get precisely the strings counted in the definition of \(R_k\). This yields both \(L_k\) and \(R_k\).

**3. Exact finite evaluation.** `verify_rooted_counts.cpp` implements the complete transition rule, performs BFS without heuristics or state pruning, and uses unsigned 128-bit integers for exact path counts, checking for overflow on each addition. Its output for \(k=2,3,4,5,6,7,8\) is exactly the \((L_k,R_k)\) table above. Its numbers of visited states are respectively \(4,30,64,2015,4096,2097136,4194304\). The source contains explicit assertions of every final value and is part of the evidence for this finite computation. The count is checked to fit in 128 bits throughout the search.

**4. Independent optimization check.** `verify_overlap_tsp.cpp` uses a distinct dynamic program. Treat each palindrome as a compulsory de Bruijn edge. The least number of additional edges from the end of compulsory edge \(p\) to the start of compulsory edge \(q\) is \(k-1\) minus the maximum suffix-prefix overlap between the corresponding \((k-1)\)-bit vertices. A complete covering closed walk may be shortcut between chosen occurrences of compulsory edges; conversely, a Hamiltonian tour using these shortest connections gives a covering walk. Hence the minimum cycle length equals the minimum total length of a directed Hamiltonian tour with edge-to-edge cost \(1+d\). A Held–Karp subset dynamic program, with the \(0^k\) edge fixed first, independently gives \(L_k\), and it counts optimal tours. For these seven orders the independently computed optimal-tour counts agree numerically with \(R_k\). This second computation is a cross-check rather than an assumption that all coverings have unique palindrome visiting orders.

Every numerical assertion is therefore established by a specified, executable, finite exhaustive algorithm whose correctness follows from the graph correspondence and dynamic-programming invariants.

## Verification
Compile and run each of the two self-contained programs with GCC (GNU C++17; the first program uses a built-in unsigned 128-bit integer), e.g.:

```
g++ -O2 -std=gnu++17 verify_rooted_counts.cpp -o verify_rooted_counts
./verify_rooted_counts
g++ -O2 -std=gnu++17 verify_overlap_tsp.cpp -o verify_overlap_tsp
./verify_overlap_tsp
```

Both independent programs return `VERIFY_OK` and the claimed seven rows. The second constructs a cycle of each optimal length and independently checks its cyclic palindrome coverage. For \(k=8\), one such 74-bit cycle is:

```
01111111100111111000011110011001101101111010010110100001001000000110000000
```

For reproducibility the first program reports 4,194,304 reachable BFS states at order eight; the second evaluates all subsets of sixteen compulsory palindromes. These checks establish finite exactness, not an unbounded formula.

## Relationship to prior work
Anisiu, Anisiu and Kása (arXiv:1002.2723v1, first posted 2010-02-13), Section 2, study generating all palindromes of a given length and prove that they cannot generally appear as consecutive windows without intervening nonpalindromes. They do not enumerate minimum cyclic palindrome-complete coverings or their rooted multiplicities.

OEIS A330022 reports shortest **linear** binary superstring lengths \(4,8,12,22,32,60,74\) at orders 2–8; OEIS A390882 reports numbers of shortest **linear** superstrings, including \(960\) at order 7 and \(176\) at order 8. A linear string is a different object from a cyclic string rooted at the all-zero palindrome: windows spanning its join are allowed here, and the counted populations differ. The existing length table is acknowledged, not claimed as a novelty. The count \(R_7=6272\), \(R_8=768\) and the full rooted cyclic count spectrum are not consequences of those linear multiplicities.

Blondin Massé and coauthors (2008) study reconstructing words from palindromic-length profiles and discuss a constrained problem requiring a given palindrome set to be *exactly* the set of all palindromic factors. Here other palindromic lengths may occur, and only coverage of a fixed length is required. Orenstein and coauthors (2013) study reverse-complement complete DNA designs; their objects and required pattern sets differ.

## Limitations
The result is a finite exact classification only through order eight; it gives no claimed value at order nine or beyond, nor a general asymptotic. It is not an enumeration of unrooted necklaces. The proof of the numerical statements uses fully specified exhaustive integer computation, independently cross-checked by a second algorithm, rather than an elementary closed form. Novelty is limited to the rooted cyclic multiplicities; the corresponding shortest *linear* lengths and their multiplicities are already tabulated. Other as-yet-unindexed cyclic-enumeration studies remain a literature risk.

## References
1. M.-C. Anisiu, V. Anisiu and Z. Kása, "Properties of palindromes in finite words," arXiv:1002.2723v1 (2010-02-13), https://arxiv.org/abs/1002.2723.
2. OEIS A330022, "Length of shortest binary string containing all palindromes of length n as substrings," https://oeis.org/A330022.
3. OEIS A390882, "Number of shortest strings containing all binary palindromes of length n as substrings," https://oeis.org/A390882.
4. A. Blondin Massé, S. Brlek, A. Frosini, S. Labbé and S. Rinaldi, "Reconstructing words from a fixed palindromic length sequence," IFIP TCS 2008, DOI:10.1007/978-0-387-09680-3_7.
5. Y. Orenstein et al., "Design of shortest double-stranded DNA sequences covering all k-mers," Bioinformatics 29 (2013), https://academic.oup.com/bioinformatics/article/29/13/i71/195654.
