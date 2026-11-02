# Four-one abelian-square minima and all extremizers through length 128

## Finding
For every integer \(19\le n\le128\), consider the binary words of length \(n\) containing exactly four \(1\)'s. Let \(\theta(w)\) be the number of **distinct words** that appear as nonempty contiguous factors of \(w\) and are Abelian squares: an Abelian square is a concatenation of two equally long words having the same number of \(1\)'s. In particular, repeated occurrences of the *same factor word* count only once.

The exact minimum is
\[
M(4,n)=\min_{|w|=n,\,|w|_1=4}\theta(w)
=\left\lfloor\frac{n+2}{4}\right\rfloor\quad(19\le n\le128).
\]
Every minimizing word is one of the following forms or its reversal:
\[
0^a1\,0^b1^3 0^c.
\]
Write \(n=4m+t\) with \(t\in\{0,1,2,3\}\). Exactly the displayed triples \((a,b,c)\) occur:

| Remainder \(t\) | Complete set of \((a,b,c)\) | Number including reversals |
| --- | --- | ---: |
| \(0\) | \((0,2m-1,2m-3)\) | 2 |
| \(1\) | \((0,2m-1,2m-2)\) | 2 |
| \(2\) | \((0,2m-1,2m-1)\), \((0,2m+1,2m-3)\), \((1,2m-1,2m-2)\), \((2,2m-1,2m-3)\) | 8 |
| \(3\) | \((0,2m+1,2m-2)\), \((2,2m-1,2m-2)\) | 4 |

The classification is **finite through length 128**. Its periodic-looking table has *not* been established for all lengths. The complete exhaustive counts for every \(n=4,\ldots,128\), including the stated \(110\) lengths \(19,\ldots,128\), are in `abelian_four_optimized_n128.txt`.

## Assumptions and scope
The alphabet is the labeled binary alphabet \(\{0,1\}\). Positions are linear, not cyclic; distinct means distinct factor *strings* rather than distinct occurrence positions or Abelian equivalence classes. Reversal does not identify words for counting. Exactly four symbols are \(1\); all others are \(0\). All comparisons and exhaustive claims are for integers \(19\le n\le128\). The auxiliary counting identity below holds for every word with exactly four \(1\)'s, but the minimum/classification is not claimed for unrestricted length.

## Proof
**Counting lemma (unrestricted length).** Every word under consideration has a unique zero-run vector \(r=(r_0,r_1,r_2,r_3,r_4)\) with nonnegative integer entries and \(w=0^{r_0}1 0^{r_1}1 0^{r_2}1 0^{r_3}1 0^{r_4}\). Set \(R=\max_i r_i\). For a nonnegative integer \(g\) and bounds \(L,U\), define
\[
H_g(L,U)=\{(u,v)\in\mathbb Z_{\ge0}^2:\ u\le L,\ v\le U,\ |u-v|\le g,\ u-v\equiv g\pmod2\}.
\]
Let \(P_2\) be the union of the labeled triples \((g,u,v)\), as \(j=1,2,3\) varies, where \(g=r_j\) and \((u,v)\in H_{r_j}(r_{j-1},r_{j+1})\). Let
\[
P_4=\left\{(u,v)\in\mathbb Z_{\ge0}^2:
 u\le r_0,\ v\le r_4,\ r_1-r_2-r_3\le v-u\le r_1+r_2-r_3,
\quad u+v+r_1+r_2+r_3\equiv0\pmod2\right\}.
\]
Then
\[
\boxed{\theta(w)=\left\lfloor R/2\right\rfloor+|P_2|+|P_4|.}
\]
To prove this, partition distinct Abelian squares by their number of \(1\)'s. Equal-half Parikh vectors force an even total number, hence only zero, two, or four. The zero-one factors are the constant words \(0^{2h}\) for \(1\le h\le\lfloor R/2\rfloor\). A factor with exactly two \(1\)'s must contain an adjacent pair of the word's four \(1\)'s; its unique string is \(0^u1 0^g1 0^v\). Exactly one \(1\) is in each half precisely when \(u+v+g\) is even and \(|u-v|\le g\). The neighboring \(1\)'s limit the left and right zero prefixes to the bounds in \(H_g\). Two occurrences of the same factor string with the same \((g,u,v)\) must be counted only once, explaining the union \(P_2\). A four-one factor necessarily contains all four \(1\)'s. Its unique string is \(0^u1 0^{r_1}1 0^{r_2}1 0^{r_3}1 0^v\), with \(0\le u\le r_0\) and \(0\le v\le r_4\). Both first \(1\)'s lie in the first half and both last \(1\)'s in the second half if and only if its half-boundary lies strictly after the second \(1\) and no later than the third \(1\), exactly the inequalities and parity in \(P_4\). Each \((u,v)\) determines a different factor string. Finally, the zero/two/four-one factor groups are disjoint, proving the identity.

**Exhaustive finite step.** For each integer \(n=4,\ldots,128\), `abelian_four_optimized.cpp` enumerates the \(\binom n4\) strictly increasing quadruples of \(1\)-positions once each, computes their five run lengths, and evaluates exactly the proved formula. It records the minimum, the number of minimizers, and the first minimizing quadruple. For the \(110\) target lengths, the output gives \(\lfloor(n+2)/4\rfloor\) and the counts \(2,2,8,4\) by \(n\) modulo four.

The separate `abelian_four_certify.py` independently evaluates the structural formula for every proposed minimizing run vector in the displayed classification, verifies its length and distinctness, checks its value against each exhaustive minimum, and verifies that the number of proposed minimizing words equals the **exhaustively computed count**. Therefore there can be no unlisted minimizer at any target length. This establishes all the stated formulas and the complete classification through \(128\), without extrapolating them to larger lengths.

## Verification
The main C++ enumeration visits exactly \(275234400\) different four-one words across \(n=4,\ldots,128\), the sum of \(\binom n4\). The source `abelian_four_optimized.cpp`, complete output `abelian_four_optimized_n128.txt`, and independent checking script `abelian_four_certify.py` are provided; the latter prints the visited-word total and verifies all \(110\) classified lengths. A second C++ program `abelian_four_direct.cpp` independently constructs each four-one word and directly enumerates every even-length substring, comparing exact half-Parikh counts and inserting each passing substring **bitstring** into a set. Its complete results through \(n=50\) (`abelian_four_direct_n50.txt`) agree with the optimized formula on all \(47\) tested lengths \(4,\ldots,50\); a third simple Python direct-substring implementation checks through \(n=18\). The exact source/output files are embedded with their SHA-256 digests in the containing artifact.

Run on an ordinary C++17/Python3 installation, from the directory containing the files:

```sh
g++ -std=c++17 -O3 -Wall -Wextra -o optimized abelian_four_optimized.cpp
./optimized 128 > recomputed_n128.txt
cmp recomputed_n128.txt abelian_four_optimized_n128.txt
python3 abelian_four_certify.py abelian_four_optimized_n128.txt
g++ -std=c++17 -O3 -Wall -Wextra -o direct abelian_four_direct.cpp
./direct 50 > recomputed_direct_n50.txt
cmp recomputed_direct_n50.txt abelian_four_direct_n50.txt
python3 abelian_four_naive.py
```

No floating-point evaluation, random search, heuristic early termination, or extrapolation is used in the finite certificate.

## Relationship to prior work
Fazekas, Mammoliti, Mercaş, and Simpson (arXiv:2604.23188v1; publicly posted April 25, 2026) study the minimum number of **distinct** Abelian-square factors at fixed binary Parikh vector. Their proofs determine the cases containing up to three instances of one letter (and symmetric boundary cases), while the interior cases remain conjectural. Their displayed numerical example at length \(18\) includes weight four but supplies neither a general weight-four minimum proof nor all finite-range extremizers through length \(128\). Their effective-word construction gives upper bounds; by itself it does not rule out better words or classify all equality words. The present result settles the first interior weight-four range by complete finite exhaustion, with full extremizer multiplicities. Fici and Saarela's earlier conjectural universal lower bound is weaker and does not give exact fixed-Parikh minima. The sequence A268084 counts Abelian-square **occurrences**, not distinct factors, so does not cover this invariant. Kociumaka and collaborators study **maximum** distinct Abelian-square counts, not the present minimum.

## Limitations
This is a finite, reproducible result for \(19\le n\le128\); the finite computation is exhaustive only in that range. It does not prove the conjectured formula, optimizer multiplicity, or family classification for \(n>128\). The direct-substring algorithm independently reaches \(n=50\), not \(128\); the longer certificate relies on the proved exact factor decomposition and the optimized exhaustive implementation. No claim about the global Fici–Saarela conjecture, other Parikh weights, or publication priority outside the inspected literature is made. Independent mathematical auditing has not been performed.

## References
- S. Z. Fazekas, A. Mammoliti, R. Mercaş, J. Simpson, *Binary Words Containing Few Abelian Squares*, arXiv:2604.23188v1 (April 25, 2026), https://arxiv.org/html/2604.23188v1.
- G. Fici and A. Saarela, *On the Minimum Number of Abelian Squares in a Word*, Dagstuhl Reports 4 (2014), issue 3, pp. 34–35 (as cited in the 2026 article).
- T. Kociumaka, J. Radoszewski, W. Rytter, T. Waleń, *Maximum Number of Distinct and Nonequivalent Nonstandard Squares in a Word*, arXiv:1604.02238, https://arxiv.org/abs/1604.02238.
- OEIS A268084, *Minimum number of occurrences of abelian squares in a binary word of length n*, https://oeis.org/A268084 (distinct-factor and occurrence statistics are different).
