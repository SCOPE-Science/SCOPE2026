# Exact short-block binary two-burst deletion codes and a perfect length-nine construction

## Finding

For each integer \(n\ge5\), let \(M_2(n,(2,2))\) denote the greatest cardinality of a binary length-\(n\) code correcting two deletions of contiguous pairs at disjoint positions. The exact first five values are
\[
\boxed{\bigl(M_2(5,(2,2)),M_2(6,(2,2)),M_2(7,(2,2)),M_2(8,(2,2)),M_2(9,(2,2))\bigr)=(2,4,4,4,8).}
\]
The length-six value has a prior general explanation [1]; the new finite-length content is the plateau at lengths seven and eight, the first subsequent increase at length nine, and an optimal **perfect** binary linear construction at length nine. In the perfect construction the deletion balls of eight codewords partition all \(32\) received words of length five.

## Assumptions and scope

The alphabet is \(\{0,1\}\). A permitted error deletes **exactly** two nonoverlapping contiguous blocks, each of length two, from the original length-\(n\) word; the blocks may be adjacent to one another. Deleting a four-symbol block using two adjacent blocks is allowed, but two overlapping blocks are not. Define
\[
D(x)=\{x_1\cdots x_{i-1}\,x_{i+2}\cdots x_{j-1}\,x_{j+2}\cdots x_n:
1\le i,\ i+2\le j\le n-1\}.
\]
A code \(C\) corrects this channel if \(D(x)\cap D(x')=\varnothing\) for every distinct \(x,x'\in C\). No claims are made about a smaller or larger number of bursts, arbitrary four deletions, alphabets other than binary, or lengths at least ten.

## Proof

**Transversal bound.** Suppose \(H\subseteq\{0,1\}^{n-4}\) intersects every deletion ball \(D(x)\). If \(C\) is a correcting code, choose one point of \(D(x)\cap H\) for each \(x\in C\). Disjointness of different deletion balls makes these points distinct. Thus \(|C|\le|H|\).

For lengths five and six take all binary output words, giving bounds \(2\) and \(4\).

For length seven take \(H_7=\{y\in\{0,1\}^3:y_1=y_3\}\), of size \(4\). Among the four odd-position symbols of any seven-bit word, two agree. Delete the other two odd-position symbols, pairing each with an adjacent even-position symbol. The two chosen even positions can always be distinct: each odd position has an adjacent even position, and any two distinct odd positions together have at least two adjacent even positions. Thus the two adjacent deletion pairs are disjoint. Since each deletion removes two consecutive positions, surviving coordinates retain their original parity; the two surviving odd-indexed symbols become the odd-indexed output symbols, which agree. Hence the output belongs to \(H_7\).

For length nine, use \(H_9=\{y\in\{0,1\}^5:y_1=y_3=y_5\}\), of size \(8\). Among five odd-position symbols, three agree. Delete the other two odd-position symbols, each with a distinct adjacent even-position symbol, as above. The three surviving odd-position symbols become the three odd-position output symbols, so the output belongs to \(H_9\). Therefore \(M_2(9,(2,2))\le8\).

For length eight, let \(H_8=\{0000,0101,1010,1111\}\), also of size \(4\). Partition an arbitrary eight-bit word into its four aligned length-two blocks. If any two blocks coincide, delete the other two entire aligned blocks; the received word is the repeated pair and lies in \(H_8\). Otherwise the four blocks are a permutation of \(00,01,10,11\). Under bit complementation and reversal of the entire input, the \(24\) permutations form six orbits, represented in the following table. Entries \(i,j\) are the one-based initial positions of the two deleted adjacent pairs, and each displayed output lies in \(H_8\).

| Input representative | \(i\) | \(j\) | Output |
| --- | ---: | ---: | --- |
| `00011011` | 4 | 7 | `0000` |
| `00011110` | 4 | 6 | `0000` |
| `00101101` | 2 | 4 | `0101` |
| `00110110` | 2 | 7 | `0101` |
| `00111001` | 1 | 6 | `1111` |
| `01001110` | 4 | 7 | `0101` |

The deletion channel and membership in \(H_8\) are invariant under bit complementation and reversal. Hence every length-eight deletion ball meets \(H_8\), proving the upper bound \(4\). The six orbit representatives and their outputs are exhaustively checked by `verify.py`.

**Lower bounds through length eight.** The constant words `00000` and `11111` yield the length-five lower bound \(2\). For each \(n\in\{6,7,8\}\), use the four length-\(n\) periodic words obtained from the repeated binary pair \((a,b)\in\{0,1\}^2\). Deletion of an adjacent pair preserves the parity of all surviving positions. Each resulting word is therefore the length-\((n-4)\) periodic word with the *same* ordered pair \((a,b)\). Distinct ordered pairs give distinct received words, so these four codewords have disjoint deletion balls.

**Perfect length-nine code.** Consider the binary linear code generated over \(\mathbb F_2\) by
```
100000111
010101010
001010010
```
Its eight codewords and their received-word bit masks are shown below. A five-bit received word \(y\) contributes the bit \(2^{\operatorname{int}_2(y)}\) to its codeword's mask, with `00000` indexing bit zero. These masks are computed by the defining disjoint-pair deletion rule.

| Codeword | Number of distinct outputs | Output mask |
| --- | ---: | --- |
| `000000000` | 1 | `0x00000001` |
| `001010010` | 7 | `0x00540074` |
| `010101010` | 1 | `0x00000400` |
| `011111000` | 7 | `0x5100d100` |
| `100000111` | 7 | `0x008b008a` |
| `101010101` | 1 | `0x00200000` |
| `110101101` | 7 | `0x2e002a00` |
| `111111111` | 1 | `0x80000000` |

The eight masks have pairwise disjoint bit supports and bitwise OR `0xffffffff`. Thus the eight deletion balls partition all \(2^5=32\) received words; in particular, no received word can be produced from two different codewords. This gives \(M_2(9,(2,2))\ge8\), meeting the preceding upper bound. All five values and the perfect-partition assertion follow.

## Verification

Run `python3 verify.py` with Python's standard library (or optionally compile and run `verify_cpp.cpp` with a C++17 compiler). The Python checker reconstructs every legal pair of length-two deletion blocks, checks that every input word at lengths five through nine meets the asserted transversal, checks pairwise disjointness of every listed code's deletion balls, verifies the six length-eight symmetry orbits and their witnesses, and establishes that the eight length-nine balls partition every length-five received word. On the supplied artifact it prints `VERIFY_OK`. The finite codeword mask table above is an independently inspectable certificate; the transversal arguments establish the upper bounds without trusting a computational search.

## Relationship to prior work

Wang–Kong–Yaakobi–Duman [1], first publicly available on 2026-05-31, defines this same multiple-burst deletion channel and its maximum-size invariant. The exact length-six boundary is covered by their general length-\((t+1)b\) construction and bound. Their Sections IV–V derive general and asymptotic bounds, particularly for two bursts of length two, and discuss length-eight deletion-ball sizes, but do not give this consecutive short-block optimum profile or the perfect length-nine construction. Ye–Sun–Yu–Ge–Elishco [2] develops constructions and asymptotic redundancy bounds for two fixed-length bursts; its stated nontrivial asymptotic hypotheses do not imply these short-block equalities. Lan–Sun–Yu–Ge [3] studies multiple-burst ball sizes, their intersections, and sequence reconstruction, rather than determining these exact maximum code sizes.

## Limitations

The result concerns the exactly-two, disjoint-length-two-burst model and only lengths five through nine. It does not classify all optimal codes, prove uniqueness of the displayed length-nine code, or extend the perfect partition to larger lengths. Published-source comparisons are evidence rather than a proof that no unindexed prior enumeration exists. The executable checker verifies the finite masks and transversals; the noncomputational upper-bound proof is provided above.

## References

[1] Chen Wang, Xiangliang Kong, Eitan Yaakobi, Tolga M. Duman, *Bounds on Multiple b-Burst Deletion-Correcting Codes*, arXiv:2606.01245v1 (first public 2026-05-31). https://arxiv.org/abs/2606.01245

[2] Zuo Ye, Yubo Sun, Wenjun Yu, Gennian Ge, Ohad Elishco, *Codes Correcting Two Bursts of Exactly b Deletions*, arXiv:2408.03113 (first public 2024-08-06). https://arxiv.org/abs/2408.03113

[3] Zhaojun Lan, Yubo Sun, Wenjun Yu, Gennian Ge, *Sequence Reconstruction under Channels with Multiple Bursts of Insertions or Deletions*, arXiv:2504.20460v1 (first public 2025-04-29). https://arxiv.org/abs/2504.20460
