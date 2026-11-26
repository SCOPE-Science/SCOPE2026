# Census of optimal quaternary multiset deletion codes with three survivors

## Finding

Consider sets of length-\(n\) multisets over the fixed labelled alphabet \(\{0,1,2,3\}\) that correct up to \(n-3\) deletions. The number of optimal codebooks at each of the lengths \(5,6,7,8\), and the number of their classes under global alphabet permutation, are as follows. The known optimal sizes are included to specify the sets being counted.

| \(n\) | optimal size (known) | labelled optimal codebooks | alphabet-permutation classes |
|---|---:|---:|---:|
| 5 | 6 | 288 | 14 |
| 6 | 5 | 708 | 46 |
| 7 | 5 | 16 | 2 |
| 8 | 5 | 1 | 1 |

In particular, at length eight the unique optimal codebook consists of the four constant words and \((2,2,2,2)\). The census concerns these four lengths only. The known optimal size is four for \(n\ge9\); no count or uniqueness claim is made there.

## Model and optimal sizes

A word is a nonnegative integer vector \(x=(x_0,x_1,x_2,x_3)\) of sum \(n\). A codebook is a set of such vectors, with no ordering of the words. Two words share a three-symbol output if and only if \(I(x,y)=\sum_i\min(x_i,y_i)\ge3\), since the intersection multiset then contains a multiset of size three. A larger common output can always be shortened to a common output of size three. Thus codebooks are exactly the sets whose distinct words satisfy \(I(x,y)\le2\). Global alphabet permutation acts on each word by the same coordinate permutation.

For completeness, the known optimal-size argument is short. Call a coordinate heavy in a word if its multiplicity is at least three. Distinct compatible words cannot share a heavy coordinate, so there are at most four words with a heavy coordinate. If there are four, each has exactly one heavy coordinate and every coordinate is used. Call words with no heavy coordinate exceptional. For \(n\ge9\) no exceptional word exists, and the four constants give equality. For \(6\le n\le8\), two distinct exceptional words would have intersection at least \(2n-8>2\), since each coordinatewise maximum is at most two. An exceptional word together with the four constants gives size five. For \(n=5\), exceptional words have types \((2,2,1,0)\) and \((2,1,1,1)\), up to permutation. The latter has intersection at least three with any other exceptional word. Two words of the former type are compatible exactly when their doubled-coordinate pairs are disjoint: a common doubled coordinate and a second support intersection give at least three, whereas disjoint doubled pairs give exactly two. There can thus be at most two compatible exceptional words. The four constants with \((2,2,1,0)\) and \((0,1,2,2)\) attain size six.

## Labelled optimizer counts

**Length five.** An optimizer has four heavy words and two exceptional words. The unordered exceptional pair is specified by one of three partitions into doubled-coordinate pairs and two choices of single-copy position for each member in the opposite pair, giving \(12\) choices. They are equivalent under alphabet permutation. Normalize to \((2,2,1,0)\) and \((0,1,2,2)\). Compatibility with these two words gives the heavy words, in order of their heavy coordinate, as
\[
(5-u,0,0,u),\quad (0,5-v,0,v),\quad (w,0,5-w,0),\quad (z,0,0,5-z),
\]
where \(u,z\in\{0,1,2\}\) and \(v,w\in\{0,1\}\). For example, the first word already meets the first exceptional word in two copies at coordinate zero, leaving only coordinate three for any other copies. The other constraints follow in the same way; at coordinates one and two the second compatibility condition caps the extra multiplicity at one. Only the pair heavy at zero and three can have mutual intersection greater than two, and its intersection is \(u+z\). This leaves \(6\cdot4=24\) completions for each exceptional pair, hence \(288\) codebooks.

**Length six.** There is exactly one exceptional word and one heavy word per coordinate. For exceptional type \((2,2,2,0)\), write \(d\) for its zero coordinate. The heavy word at \(i\ne d\) has the form \((6-u_i)e_i+u_i e_d\), with \(0\le u_i\le2\); here \(e_i\) is the unit vector at \(i\). The heavy word at \(d\) has \(y_i\) copies off that coordinate, where \(y_i\ge0\) and \(\sum_{i\ne d}y_i\le2\). The only remaining constraints are \(u_i+y_i\le2\). The number of completions per exceptional word is
\[
\sum_{\substack{y_i\ge0\\\sum_{i\ne d}y_i\le2}}\prod_{i\ne d}(3-y_i)=27+54+63=144.
\]
The four choices of \(d\) contribute \(576\). For exceptional type \((2,2,1,1)\), there are six choices for the doubled coordinates. The heavy words there must be constants. At each singly occupied coordinate the heavy word is a constant, has a single extra copy at any other coordinate, or has two extra copies at the other singly occupied coordinate. Among the resulting \(25\) pairs of heavy words at those last two coordinates, exactly three violate compatibility: both send two copies to each other, or one sends two to the other and receives one in return. There are consequently \(6\cdot22=132\) additional codebooks, for a total of \(708\).

**Lengths seven and eight.** At seven the exceptional word has type \((2,2,2,1)\), in four labelled ways. The three heavy words at its doubled coordinates are constants. The remaining heavy word can be a constant or have one extra copy at any of the other three coordinates. This gives \(16\) codebooks. At eight the exceptional word must be \((2,2,2,2)\), and all heavy words must be constants.

## Alphabet-permutation classes

The cycle types in \(S_4\) have multiplicities \(1,6,3,8,6\) in the order shown below. The table records the number of optimal codebooks fixed by **one** permutation of each type. Fixing a codebook means fixing it as a set, not fixing every word individually.

| \(n\) | identity | transposition | double transposition | three-cycle | four-cycle |
|---|---:|---:|---:|---:|---:|
| 5 | 288 | 0 | 16 | 0 | 0 |
| 6 | 708 | 58 | 8 | 3 | 0 |
| 7 | 16 | 4 | 0 | 1 | 0 |
| 8 | 1 | 1 | 1 | 1 | 1 |

To obtain the table, list all four-part compositions of \(n\) in lexicographic order and mark compatible pairs. Start with the empty codebook and all indices available. For each available index, append it, retaining only later available indices that are compatible with the appended index. Stop and record a set at the known optimal size; abandon any branch with fewer available indices than the number of unfilled slots. Every compatible set of the target size follows its unique increasing index sequence and cannot be pruned along it. For each recorded set and each permutation, permute coordinates and compare the resulting set with the original. This gives the fixed counts above; Burnside averaging gives \(14,46,2,1\), respectively.

## Reproduction and significance

`python verify.py` uses Python 3.10 or later and the standard library. In addition to the exhaustive set enumeration and fixed-point tests, it checks the intersection versus deletion-shadow criterion and recounts the labelled optimizers via the exceptional/heavy decomposition. The recorded output is in `verification_output.txt`. The orbit counts rely on a finite exhaustive calculation; the labelled counts also have the separate combinatorial derivation above.

The census distinguishes abundance of optimizers from genuine inequivalence under relabelling and identifies the exact rigidity at the last length admitting five codewords. Neither property follows from the optimum sizes alone.

## Known results and scope of the contribution

The exact quaternary capacity profile, including the \(n=5\) endpoint, appears in [*Exact quaternary three-survivor multiset deletion spectrum*](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exact-quaternary-three-survivor-multiset-deletion-spectrum--10c1013a7401). The broader [*Exact three-survivor multiset deletion codes over arbitrary alphabets*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-three-survivor-multiset-deletion-codes-over-arbitrary-alph--da6ffbe21ef7) gives the same sizes for \(q=4,n\ge6\) and a general heavy-coordinate description, not the counts in this table.

Kreindel, Barouch Essayag and Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, [arXiv:2601.05636v2](https://arxiv.org/abs/2601.05636v2), §4.4 Proposition 12 gives a certificate upper bound in the three-survivor regime. The updated [v3](https://arxiv.org/abs/2601.05636v3), §4 Theorem 8 and Corollary 9, uses constant-sum \(\ell_1\) packing and gives the exact sizes for general alphabets, explicitly covering the size column and the eventual cutoff here. Neither the size column nor the cutoff is claimed as a contribution. The broader multiset-channel geometry is treated in [arXiv:2603.18322](https://arxiv.org/abs/2603.18322) and Kovačević and Tan, [arXiv:1612.08837](https://arxiv.org/abs/1612.08837). No claim of historical priority over every possible older representation of the census is made.
