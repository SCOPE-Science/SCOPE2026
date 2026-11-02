# First informative collision and complete ambiguity census for binary three-separated three-decks

## Finding
For a binary word \(w\) of length \(n\), observe the **multiset** of all of its three-separated scattered subsequences of lengths one, two, and three. A pair of selected positions must differ by at least three. The following is an exact finite classification:

* For every integer \(7\le n\le16\), the observation identifies each of the \(2^n\) words uniquely.
* At \(n=17\), the \(2^{17}=131072\) words produce exactly \(131056\) distinct observations: precisely \(131040\) singleton fibers and \(16\) doubleton fibers, with no larger fiber.
* The sixteen ambiguous unordered pairs form four orbits of size four under word reversal and simultaneous binary complementation. Representatives (each line comprises two different words) are:

```
01000101001010101   01001000011100101
01000101001010110   01001000011100110
01010101101011110   01011000111101110
01100111000010001   01101010010100001
```

The complete sixteen-pair list is in `COLLISIONS.csv`. Thus length seventeen is the **first reconstruction collision in the informative range** where admissible triples can exist.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). Positions are numbered \(1,\ldots,n\). For each \(\ell\in\{1,2,3\}\) and ordered binary pattern \(p\in\{0,1\}^{\ell}\), define

\[
C_w(p)=\#\{(i_1,\ldots,i_\ell):1\le i_1<\cdots<i_\ell\le n,\quad
 i_{j+1}-i_j\ge3,\quad (w_{i_1},\ldots,w_{i_\ell})=p\}.
\]

The observation \(\mathcal D_3(w)\) is the integer vector of all fourteen values \(C_w(p)\), ordered first by pattern length and then lexicographically. The multiplicity is essential: this is not merely the set of patterns appearing. The range starts at \(n=7\), the minimum length admitting three positions with both consecutive spacings at least three. This restriction is part of the claim: it is **not** a statement that all shorter words are uniquely reconstructible, nor is it a claim about ordinary ungapped decks.

## Proof
Let \(C_i(p)\) count valid embeddings of \(p\) in the first \(i\) letters of a word, and set \(C_j(\varepsilon)=1\) for every \(j\ge0\). Set \(C_0(p)=0\) for nonempty \(p\). For \(p=p_1\cdots p_\ell\), \(1\le\ell\le3\), appending the symbol at position \(i\ge1\) gives the exact recurrence

\[
 C_i(p)=C_{i-1}(p)+\mathbf1_{\{w_i=p_\ell\}}
 C_{\max(0,i-3)}(p_1\cdots p_{\ell-1}).
\]

To prove the recurrence, partition embeddings according to whether they omit position \(i\) or end at position \(i\). In the latter case the preceding selected index is at most \(i-3\); deleting the final index leaves exactly an admissible embedding of the prefix pattern. Conversely, adjoining \(i\) to every such embedding gives all valid embeddings ending there. For \(\ell=1\), the empty prefix contributes one whenever the appended bit equals the pattern bit. This establishes every coordinate by induction on \(i\).

The finite exhaustive proof is the deterministic Python 3 program `verify.py`, using only the standard library and unbounded exact integers. Its recursion traverses the **complete binary prefix tree** down to depth seventeen, extending the fourteen coordinates by the proved recurrence. At each depth from seven to seventeen it places every distinct complete vector into a dictionary; a repeated vector is assigned to its first word and collision pair. It explicitly rules out a third word in any fiber. The exhaustive results are:

| \(n\) | Realizable deck vectors | Doubleton fibers |
|---:|---:|---:|
| 7 | 128 | 0 |
| 8 | 256 | 0 |
| 9 | 512 | 0 |
| 10 | 1024 | 0 |
| 11 | 2048 | 0 |
| 12 | 4096 | 0 |
| 13 | 8192 | 0 |
| 14 | 16384 | 0 |
| 15 | 32768 | 0 |
| 16 | 65536 | 0 |
| 17 | 131056 | 16 |

As all \(2^n\) words are considered for each \(n\), every absent collision below length seventeen is excluded, and the sixteen length-seventeen collisions are complete. The total at length seventeen is checked as \(131040+2\cdot16=131072\). The program converts all collision pairs to canonical ordered strings, compares the resulting set to `COLLISIONS.csv`, and partitions it under the two commuting involutions reversing both words and complementing both words. It proves computationally that each resulting orbit has four pairs and that there are four orbits. Because reversal/complement consistently relabel the fourteen deck coordinates, these operations preserve equality of observations.

This is an **exhaustive finite proof** for the specified range, not an extrapolation from sampling. The full domain and integer arithmetic are explicit and finite. No inference for larger lengths is asserted.

## Verification
Run `python3 verify.py` in the same directory as `COLLISIONS.csv`; no packages, external data, probabilistic hashes, solvers or network requests are required. The verifier produces `VERIFY_OK` followed by all eleven census lines and the four representatives. Its independent literal index-combination procedure recomputes all fourteen deck coordinates for every binary word at lengths seven through ten (1920 words), and independently recomputes them for the 32 length-seventeen collision words. The exhaustive traversal checks all 131072 length-seventeen words and all shorter informative lengths. Dictionary equality is equality of full fourteen-coordinate integer tuples, not equality of hash digests.

## Relationship to prior work
Golm, Nahvi, Gabrys and Milenkovic [1] introduced gap-constrained multiplicity decks, gave explicit small-case values for the different **two-separated** setting, and established a general upper bound. Specializing their general upper bound to the present parameters gives \(41\), whereas the present exact first **informative** length is \(17\), together with the complete first-fiber census. Their stated \(G_2(3)=13\) is **not** the present three-separated measurement. Day, Kosche, Manea and Schmid [2] analyze matching and equivalence of sets of gap-constrained subsequences; set equivalence does not record the multiplicities defining this observation. Thus neither cited result directly implies the exact census or four-orbit classification.

## Limitations
The classification applies only to a binary alphabet, separation at least three, maximum subsequence length three, and word lengths seven through seventeen. It does not determine all collision fibers at length eighteen or higher or at larger gap constraints, nor does it prove uniqueness on the vacuous shorter range. An equivalent census under a different name may exist outside the examined literature. Computation establishes a finite theorem but provides no closed-form formula for the distribution at arbitrary length.

## References
1. R. Golm, M. Nahvi, R. Gabrys, O. Milenkovic, *The Gapped \(k\)-Deck Problem*, arXiv:2201.12671, first posted 29 January 2022; https://arxiv.org/abs/2201.12671 .
2. J. D. Day, M. Kosche, F. Manea, M. L. Schmid, *Subsequences With Gap Constraints: Complexity Bounds for Matching and Analysis Problems*, arXiv:2206.13896, first posted 28 June 2022; https://arxiv.org/abs/2206.13896 .
