# Sharp Lyndon-factor reconstruction of binary order-five de Bruijn cycles

## Finding

Let \(B\) be a binary de Bruijn cycle of order \(5\), viewed up to cyclic rotation, with the fixed letter order \(0<1\). Thus \(B\) has length \(32\), and each binary word of length \(5\) occurs exactly once as a circular factor. For \(1\leq \ell\leq32\), put

\[
\lambda_\ell(B)=\left|\{u\in\{0,1\}^\ell:u\text{ is Lyndon and occurs as a circular factor of }B\}\right|.
\]

**Theorem.** The vector \((\lambda_1(B),\ldots,\lambda_{19}(B))\) uniquely determines \(B\) up to rotation, among all binary order-five de Bruijn cycles. The cutoff \(19\) is sharp: the vector ending at \(\ell=18\) has exactly \(2047\) values over the \(2048\) cycles, with one doubleton and no larger collision. At length \(19\) all \(2048\) vectors are distinct. Specifically, the only two cycles with equal vectors through length \(18\), represented by their unique `00000` starting positions, are

```
00000101001101110010001111101011
00000111010111110010100110110001
```

Their common vector through length \(18\) is

\[
(2,1,2,3,6,6,5,3,3,3,4,5,4,3,2,1,1,1),
\]

while their values of \(\lambda_{19}\) are \(1\) and \(2\), respectively. The first five entries are fixed for every order-five cycle:

\[
(\lambda_1,\ldots,\lambda_5)=(2,1,2,3,6).
\]

In particular, it is only necessary to retain the fourteen counts at lengths \(6,\ldots,19\). The result does not assert uniqueness from the *sum* of these counts.

## Assumptions and scope

A nonempty word \(u\) is *Lyndon* if it is strictly lexicographically smaller than every nontrivial cyclic rotation of itself, with \(0<1\); in particular, it is primitive. A circular factor of length \(\ell\) starting at \(i\) is the word \(B_iB_{i+1}\cdots B_{i+\ell-1}\), with indices modulo \(32\). We count distinct factor *strings*, not occurrences, and do not identify a factor with its reversal, complement, or other conjugates. Each binary de Bruijn cycle has exactly one occurrence of `00000`, providing a unique rooted representative. Only cycles up to rotation, not reversal or complementation, are identified.

## Proof

**1. Exhaustive domain.** Consider the directed binary de Bruijn graph whose vertices are binary four-words and whose edges are binary five-words. Each vertex has exactly two incoming and two outgoing edges. An Eulerian circuit traversing all \(32\) edges once spells an order-five de Bruijn cycle. Conversely, each such cycle defines an Eulerian circuit. Fixing the edge `00000` as the initial edge eliminates rotations.

At every vertex, pair its two incoming edges bijectively with its two outgoing edges. There are exactly two choices at each of the \(16\) vertices, giving \(2^{16}=65536\) pairing assignments. Each assignment is a permutation of the \(32\) edges, and it gives an Eulerian circuit exactly when its permutation consists of one cycle. Thus testing all assignments, accepting precisely those with a single \(32\)-cycle, is exhaustive. The supplied checker obtains exactly \(2048\) distinct rooted cycles. A separate depth-first traversal of unused directed edges, starting with `00000` and closing after exactly \(32\) edges, obtains the same set of \(2048\) cycles. These are two distinct complete enumerations.

**2. Exact evaluation of each entry.** For a rooted cycle \(b\), each length-\(\ell\) circular factor, \(1\leq\ell\leq19\), occurs among the \(32\) strings of length \(\ell\) starting at the positions \(0,\ldots,31\) in \(b\) periodically extended. Remove repeated strings. For each remaining string \(u\), the checker applies both the defining test

\[
u<\operatorname{rot}_j(u)\quad (1\leq j<|u|)
\]

and the equivalent Lyndon characterization

\[
u<u[j:]\quad (1\leq j<|u|),
\]

where \(u[j:]\) is the nonempty proper suffix after position \(j\). The latter characterization is standard (see Saari, Lemma 4). Both tests agree on all factors encountered. Counting their accepted distinct strings gives \(\lambda_\ell(b)\) with no probabilistic approximation. For \(\ell\leq5\), every possible binary length-\(\ell\) word occurs, giving the fixed values quoted above.

**3. Certificate of sharp separation.** The checker evaluates every resulting profile \((\lambda_1,\ldots,\lambda_k)\) and groups equal profiles. Its exhaustive counts of distinct profiles for \(k=16,17,18,19\) are, respectively,

\[
2044,\qquad2045,\qquad2047,\qquad2048.
\]

The numbers of unordered colliding pairs are, respectively, \(4,3,1,0\). At \(k=18\) the unique doubleton is the two strings displayed in the theorem; its length-\(19\) counts differ. This verifies injectivity at \(19\) and noninjectivity at every shorter cutoff (truncating a signature cannot split a collision). The complete row-by-row table is `profiles.csv`, and `verify.py` regenerates it from both the graph constructions and both Lyndon predicates. All loops have explicit finite ranges and the code makes assertions at each claimed equality. These computations, with the exhaustiveness argument of step 1, constitute a finite proof.

## Verification

Run `python3 verify.py profiles.csv` in a directory containing both supplied files. The program uses only the Python standard library. It enumerates all \(65536\) local pairings, independently enumerates all Eulerian circuits by depth-first search, checks the de Bruijn property of every accepted cycle, calculates every Lyndon count by both predicates, verifies the exact collision counts and exceptional pair, and compares the entire \(2048\)-row table with `profiles.csv`.

A verified run reports:

```
VERIFY_OK distinct_de_bruijn_cycles=2048 pairing_assignments=65536 independent_eulerian_enumeration=yes independent_lyndon_criteria=yes distinct_profiles_cutoff18=2047 unique_profiles_cutoff19=2048 sole_cutoff18_collision=2 cycles
```

## Relationship to prior work

Fredricksen and Maiorana's necklace-concatenation construction connects Lyndon words with the construction of individual de Bruijn cycles. Saari studies Lyndon factors and their minimal counts, especially in Fibonacci and recurrent infinite words; Goc, Saari and Shallit study Lyndon-factor counting in automatic and linearly recurrent sequences. Glen, Simpson and Smyth study maximum and expected counts for unrestricted finite words. None of those inspected statements specifies an injectivity threshold for the *aggregate lengthwise counts* on the complete order-five de Bruijn family. The known reconstruction problem from full positionwise Lyndon arrays concerns strictly richer, different input data; the present assertion concerns counts of distinct factors only.

Every order-five de Bruijn cycle has the same ordinary circular factor-complexity vector: \(2^\ell\) distinct length-\(\ell\) factors for \(\ell\leq5\) and exactly \(32\) for \(5<\ell\leq32\). The Lyndon restriction nonetheless distinguishes all cycles already by length \(19\). Literature comparisons are not a proof of historical priority.

## Limitations

The reconstruction theorem is exhaustive only for binary order \(5\) with \(0<1\), counting cycles modulo rotation. It does not assert the same threshold at other orders, for other alphabets, or under identification of reversal or complementation. The computational proof is finite and transparent, but an independently conducted audit has not been carried out. Published and indexed literature may not include every earlier unpublished table or computational study.

## References

1. K. Saari, *Lyndon Words and Fibonacci Numbers*, arXiv:1207.4233, first publicly posted 17 July 2012. https://arxiv.org/abs/1207.4233
2. D. Goc, K. Saari and J. Shallit, *Primitive Words and Lyndon Words in Automatic and Linearly Recurrent Sequences*, arXiv:1207.5124, first publicly posted 21 July 2012. https://arxiv.org/abs/1207.5124
3. H. Fredricksen and J. Maiorana, *Necklaces of beads in k colors and k-ary de Bruijn sequences*, Discrete Mathematics 23 (1978), 207–210 (as cited in [1]).
4. A. Glen, J. Simpson and W. F. Smyth, *Counting Lyndon Factors*, Electronic Journal of Combinatorics 24 (2017), P3.28, arXiv:1701.00928. https://arxiv.org/abs/1701.00928
5. J. W. Daykin, F. Franěk, J. Holub, A. S. M. S. Islam and W. F. Smyth, *Reconstructing a String from Its Lyndon Arrays*, Theoretical Computer Science 710 (2018), 44–51. doi:10.1016/j.tcs.2017.04.008.
