# Quaternary multiset codes with three surviving symbols: exact sizes and extremal census

## Finding

Let \(S_4(n,n-3)\) be the largest number of distinguishable length-\(n\) multisets over a **labeled four-symbol alphabet** when up to \(n-3\) symbols may be deleted. For every integer \(n\ge5\),

\[
S_4(n,n-3)=\begin{cases}
6,&n=5,\\
5,&6\le n\le8,\\
4,&n\ge9.
\end{cases}
\]

The number of distinct labeled optimal codebooks, and their numbers of orbits under global alphabet permutation, are respectively

| \(n\) | optimal size | labeled optimal codebooks | alphabet-permutation orbits |
|---|---:|---:|---:|
| 5 | 6 | 288 | 14 |
| 6 | 5 | 708 | 46 |
| 7 | 5 | 16 | 2 |
| 8 | 5 | 1 | 1 |

Thus the codebook itself is unique at \(n=8\), namely the four constant words together with \((2,2,2,2)\). No uniqueness assertion is made for \(n\ge9\).

## Assumptions and scope

The alphabet is the fixed labeled set \(\{0,1,2,3\}\), and a transmitted multiset is its multiplicity vector \(x=(x_0,x_1,x_2,x_3)\) with nonnegative integral entries summing to \(n\). The output is another multiset, containing precisely three remaining symbols after exactly \(n-3\) deletions. Since an output of size greater than three contains an output of size three, correction of exactly \(n-3\) deletions is equivalent to correction of up to that many deletions. Two words are distinguishable precisely when their multiset intersection

\[
I(x,y)=\sum_{i=0}^{3}\min(x_i,y_i)
\]

is at most two. Equivalently, their one-half \(\ell_1\)-distance is at least \(n-2\). Codes are **sets** of vectors, not ordered sequences of words. Labeled codebooks distinguish symbol labels; orbit counts identify codebooks under the natural \(S_4\)-action on these four labels.

## Proof

**Heavy-symbol injection.** Call a coordinate heavy in \(x\) when its multiplicity is at least three. Two compatible codewords cannot be heavy at the same coordinate, since their multiset intersection would contain three copies of that symbol. Hence at most four codewords can have a heavy coordinate. Call words with all four coordinates at most two *exceptional*. If a code contains four heavy words, these four words must use the four heavy coordinates exactly once, and none can have a second heavy coordinate.

For \(n\ge9\), the pigeonhole principle ensures every word is heavy. The four constant words \(n e_0,n e_1,n e_2,n e_3\) attain the upper bound four.

For \(n\ge6\), at most one exceptional word can occur. Indeed, if two distinct exceptional words \(x,y\) of total weight \(n\) coexisted, then

\[
I(x,y)=2n-\sum_i\max(x_i,y_i)\ge 2n-8\ge4,
\]

contradicting compatibility. Exceptional words exist for \(6\le n\le8\), and each is compatible with all four constant words. Thus the exact optimum is five in this range.

For \(n=5\), each exceptional word has composition type \((2,2,1,0)\) or \((2,1,1,1)\), up to permutation. A word of the second type has intersection at least three with every other exceptional word. Thus any compatible exceptional pair must use type \((2,2,1,0)\). Its two coordinates of multiplicity two must be disjoint from the corresponding two coordinates of the other word: otherwise their two three-element supports intersect in an additional positive coordinate and the multiset intersection is at least three. Conversely, disjoint doubled-coordinate pairs give intersection exactly two. At most two disjoint two-subsets of a four-set exist, so a code contains at most two exceptional words. This gives \(|C|\le4+2=6\). The four constants together with \((2,2,1,0)\) and \((0,1,2,2)\) attain six.

**Exact labeled maximizer counts.** For \(n=5\), equality forces exactly four heavy words and two exceptional words. There are twelve unordered compatible exceptional pairs: choose one of the three partitions into doubled-coordinate pairs, then select the position of the single copy in each member in two ways apiece. All twelve are equivalent by symbol permutation. Normalize one pair as \(E=(2,2,1,0)\) and \(F=(0,1,2,2)\). The heavy words forced to use coordinates \(0,1,2,3\), respectively, have forms

\[
(5-u,0,0,u),\quad(0,5-v,0,v),\quad(w,0,5-w,0),\quad(z,0,0,5-z),
\]

with \(u,z\in\{0,1,2\}\) and \(v,w\in\{0,1\}\). Their only nonautomatic compatibility condition is \(u+z\le2\), leaving six choices for \((u,z)\) and four for \((v,w)\). Hence there are \(12\cdot24=288\) labeled optimal codebooks.

For \(n=6\), a size-five code contains exactly one exceptional word and one uniquely heavy word at each coordinate. If the exceptional word has composition type \((2,2,2,0)\), choose the coordinate \(d\) with multiplicity zero. For each of the other three heavy coordinates \(i\), its codeword must be \((6-u_i)e_i+u_i e_d\), with \(u_i\in\{0,1,2\}\). The word heavy at \(d\) has the form \((6-\sum_i y_i)e_d+\sum_i y_i e_i\), where all \(y_i\ge0\) and \(\sum_i y_i\le2\). Compatibility is exactly \(u_i+y_i\le2\) for every \(i\). The number of completions is

\[
\sum_{\substack{y_i\ge0\\\sum_i y_i\le2}}\prod_{i=1}^{3}(3-y_i)
=27+54+63=144.
\]

There are four exceptional words of this type, contributing \(576\) codes. For type \((2,2,1,1)\), there are six exceptional words. The heavy words on its two doubled coordinates must be constants. Each of the other two heavy words has five possibilities: a constant; a word with five copies at its heavy coordinate and one at any other coordinate; or a word with four at its heavy coordinate and two at the other singly occupied exceptional coordinate. Of the \(25\) pairs, exactly three have mutual intersection at least three (the pair with both extra multiplicities two, and the two mixed extra-multiplicity-one/two pairs). There are \(22\) completions for each exceptional word, contributing \(132\) further codes. In total \(576+132=708\).

For \(n=7\), the exceptional word has type \((2,2,2,1)\), in four labeled ways. The three heavy words at its doubled coordinates must be constants. The remaining heavy word is either a constant or has six copies at its heavy coordinate and one copy at one of the other three coordinates. Thus there are \(4\cdot4=16\) codes. For \(n=8\), the sole exceptional word is \((2,2,2,2)\) and all four heavy words must be constants, giving precisely one code.

**Alphabet-permutation orbit counts.** Burnside's lemma gives the orbit number by averaging the number of codebooks fixed by each permutation in \(S_4\). The following table gives the fixed count **per permutation** in each cycle type, in the order identity, transposition, double transposition, three-cycle, four-cycle. The conjugacy-class multiplicities are \((1,6,3,8,6)\):

| \(n\) | identity | transposition | double transposition | three-cycle | four-cycle |
|---|---:|---:|---:|---:|---:|
| 5 | 288 | 0 | 16 | 0 | 0 |
| 6 | 708 | 58 | 8 | 3 | 0 |
| 7 | 16 | 4 | 0 | 1 | 0 |
| 8 | 1 | 1 | 1 | 1 | 1 |

These fixed counts follow from the complete finite enumeration of exceptional/heavy selections given in the standalone verifier. Burnside averaging yields \(14,46,2,1\), respectively. The recursion enumerates lexicographically increasing codeword indices, intersects the allowed-neighbor masks after every extension, and records only compatible sets of the proven optimal size. Hence it is exhaustive and never counts an ordered permutation of a codebook as a new codebook.

## Verification

The included `verify.py` uses only the Python standard library. Run `python verify.py`. It independently enumerates all optimal-size cliques in the compatibility graph and, by a different exceptional/heavy-word Cartesian-product decomposition, recomputes their counts. It directly checks that compatibility is equivalent to disjoint three-symbol deletion shadows for every pair of candidate words at lengths five through eight. It also recomputes alphabet-permutation fixed counts and Burnside orbit numbers, checks explicit witnesses, and checks the pigeonhole argument over additional sample lengths. The recorded output is in `verification_output.txt`; a successful run ends with `QUATERNARY_THREE_SURVIVOR_VERIFICATION_OK`.

## Relationship to prior work

Kreindel, Essayag, and Zabokritskiy [1, Section 4.4, Proposition 12] study this three-survivor regime for general alphabets. Their certificate bound for \(n\ge q+2\) yields \(S_4(n,n-3)\le10\), which neither determines the values \(5\) and \(4\) nor classifies all optimizers. Their exact quaternary single-deletion results concern the different regime \(t=1\), which agrees with this parameterization only at \(n=4\), outside the present theorem. Their later study [2] develops multiset deletion-ball geometry and general bounds, not this fixed-alphabet high-deletion optimizer census. Kovačević and Tan [3] establish the general multiset channel and algebraic bounds; their results do not state the present quaternary profile or labeled/orbit counts. Earlier work on ternary three-survivor codes addresses a different alphabet and does not imply these counts. Prior exact results and constructions are not relabeled here as new.

## Limitations

The theorem concerns precisely four alphabet symbols and three surviving multiset elements. The census is complete for lengths five through eight; it does not classify all maximizing codebooks for \(n\ge9\). Finite orbit fixed-point numbers rely on the included exhaustive enumeration, whose completeness follows from the stated mask recursion; the capacity and labeled maximizer formulas have separate combinatorial proofs. An equivalently formulated result in older discrete-simplex packing or lattice-code tables is a remaining historical priority risk. No independent mathematical audit is claimed.

## References

[1] A. Kreindel, I. Barouch Essayag, and A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636, first public version 9 January 2026, Section 4.4. https://arxiv.org/abs/2601.05636

[2] A. Kreindel, I. Barouch Essayag, and A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322, 18 March 2026. https://arxiv.org/abs/2603.18322

[3] M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837, originally public 28 December 2016. https://arxiv.org/abs/1612.08837
