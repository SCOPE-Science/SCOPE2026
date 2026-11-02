# Complete extremizers for additive-square avoidance on \(\{0,1,2,5\}\)

## Finding

Let \(A=\{0,1,2,5\}\) with its **integer**, not merely formal-symbol, values. A word avoids additive squares if no two consecutive nonempty blocks of the same length have equal integer sums. The longest such words have length \(86\) (the maximum length was previously established). **There are exactly eight longest words**, forming **four orbits under reversal**. Choosing the lexicographically smaller word in each reversal pair, all four representatives are:

```
02050125051012101501025152505251202515015201215120105010201521201525150201025202515202
02050125051012101501205152505251202515015201215120105010201521201525150201025202515202
02105025212505251012010510120252101215052051205251525051202502010205251505205010205251
25051252021050121051252052515051521502101501252125012010501020521250521501512025152505
```

The other four longest words are their reversals. The eight words have exactly three Parikh profiles, with multiplicities ordered by letters \((0,1,2,5)\): four words have \((23,21,21,21)\), two have \((24,17,22,23)\), and two have \((20,20,21,25)\). Hence this is a complete equality-case classification, not a restatement of the known length bound.

## Assumptions and scope

Words are finite non-cyclic strings with entries in the specific integer alphabet \(A\). A prohibited factor consists of adjacent blocks \(U,V\) of a common positive length \(k\) with \(\sum U=\sum V\). Words and their reversals are counted as different unless identical; labels cannot be freely permuted because additive sums depend on their numerical values. No unproved asymptotic or other-alphabet statement is asserted.

## Proof

For a prefix \(w_1\cdots w_t\), write \(P_0=0\) and \(P_j=\sum_{i=1}^{j}w_i\). Assume the prefix avoids additive squares. Append a letter \(a\in A\). Any newly created additive square must end at the new last position. For a proposed half-length \(1\le k\le\lfloor(t+1)/2\rfloor\), its right block has sum \(P_t+a-P_{t+1-k}\), and its left block has sum \(P_{t+1-k}-P_{t+1-2k}\). Equality holds precisely when

\[
a=2P_{t+1-k}-P_{t+1-2k}-P_t.
\]

Therefore all and only the letters of \(A\) outside this finite forbidden set may extend the prefix. Starting from the empty word, depth-first search on these exact integer constraints visits every admissible word once, by induction on length. The standalone program `verify_forbidden.cpp` implements this recursion, without sampling or pruning away valid prefixes. It visits \(299596819\) nodes, including the empty word. At lengths \(80,81,82,83,84,85,86,87\), the node counts are respectively \(2696,1530,792,338,120,38,8,0\). Thus there are exactly eight admissible words of length \(86\), and no word of length \(87\). Since admissibility is prefix-closed, no longer word can exist.

A second program, `verify_direct.cpp`, independently checks new terminal squares using two sliding block sums of the actual letters rather than the forbidden-letter formula. It makes the same exhaustive depth-first traversal and returns the same node total, the same final counts and exactly the same eight strings. A separate direct test also checks every contiguous comparison in each printed extremizer. Reversal preserves equality of block sums, and inspection of the enumerated list gives precisely the stated four reversal pairs and three Parikh profiles. This finishes the computer-assisted finite proof.

## Verification

Compile with a conforming C++17 compiler, for example:

```sh
g++ -O3 -std=c++17 verify_forbidden.cpp -o verify_forbidden
./verify_forbidden
g++ -O3 -std=c++17 verify_direct.cpp -o verify_direct
./verify_direct
```

The complete winning list is `extremizers.txt`; expected counts and summary are in `verification-output.txt`. These files are self-contained. Both programs use exact integer arithmetic; the largest intermediate prefix sum is at most \(435\), and their node counters fit comfortably in unsigned 64-bit integers. The original construction reaches the same depth and its published search visit count agrees with the exact total above.

## Relationship to prior work

Zhang's 2026 paper establishes the maximum length \(g(\{0,1,2,5\})=86\), prints one extremal witness in its supplementary section S1, and reports \(299596819\) search visits in section S5. These results establish existence and the sharp length but **do not state the number of extremizers or classify their reversal and Parikh types**. The present contribution is exactly that optimizer census and classification. The earlier Freedman–Brown work covers a different endpoint-sum family and does not imply this equality-case statement.

## Limitations

The result is an exact classification for one natural extremal alphabet, not a general formula over arbitrary integer alphabets. The proof depends on a finite exhaustive computation whose completeness rests on the displayed recursive extension equivalence and fully embedded independent implementations. The associated electronic archive for the closest paper could not be inspected directly; its raw search output may contain related implicit counting information. Independent external review of priority and computation has not been performed.

## References

- E. Zhang, *The additive-square-free spectrum below 139*, arXiv:2610.02215v1 (first public preprint 2026-09-08); especially Theorem 1 and technical supplement S1 and S5.
- E. Zhang, supplemental electronic materials, DOI:10.5281/zenodo.22651748 (archive availability noted; contents not independently inspected here).
- A. R. Freedman and T. C. Brown, *Sequences on sets of four numbers*, Integers 16 (2016), A33 (earlier endpoint-sum classification, as identified in Zhang's references).
