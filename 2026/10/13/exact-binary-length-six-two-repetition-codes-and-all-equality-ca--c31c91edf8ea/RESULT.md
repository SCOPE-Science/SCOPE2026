# Exact binary length-six two-repetition codes and all equality cases
## Finding
For binary words of length \(6\), the exact maximum size of a code correcting up to two repetition errors is \(18\). Here one repetition replaces one chosen symbol by two adjacent copies of that symbol; the received length therefore reveals whether zero, one, or two repetitions occurred. Exactly \(22{,}500\) labeled maximum codes attain the bound.

Every word \(x=x_1x_2\cdots x_6\) is represented by its first bit \(a=x_1\) and derivative
\[
d(x)=(x_1\mathbin{\oplus}x_2,\ldots,x_5\mathbin{\oplus}x_6)\in\{0,1\}^5.
\]
In each fixed-first-bit sector, the derivative-weight layers \(w=0,1,2,3,4,5\) contribute maximum sizes
\[
(1,2,3,1,1,1),
\]
and the numbers of maximizing layer choices are
\[
(1,3,1,10,5,1).
\]
Thus each first-bit sector has maximum size \(9\) and exactly \(150\) maxima; the two sectors combine independently, giving \(18\) and \(150^2=22{,}500\).

Every maximum has the displayed derivative-weight profile in each first-bit sector. Its disjoint descendant balls after exactly two repetitions cover \(142\) of the \(256\) binary words of length \(8\), so no maximum is perfect.

## Assumptions and scope
The alphabet is binary. A repetition duplicates a single symbol immediately adjacent to itself, equivalently a tandem duplication of length \(1\). The code must uniquely correct any number of repetitions from \(0\) through \(2\). Because output length identifies the number of repetitions, confusion can occur only between descendant sets produced by the same number of repetitions.

The statement is for arbitrary, not necessarily linear, labeled codes. No quotient by coordinate or alphabet symmetries is taken. The claim does not address longer block lengths, larger alphabets, or duplications of length greater than \(1\).

## Proof
The map from a binary word to its first bit together with its derivative is a bijection. Duplicating one symbol inserts one zero into the derivative and leaves the first bit unchanged. Hence two different first-bit sectors can never be confused, and derivative Hamming weight is invariant under repetitions.

Fix a first bit and a derivative weight \(w\). Write a derivative of length \(5\) as \(w\) ones separated by \(w+1\) zero bins, and let
\[
b=(b_0,\ldots,b_w),\qquad b_i\ge0,\qquad \sum_i b_i=5-w.
\]
After exactly two repetitions, the derivative descendants are precisely the vectors \(c\ge b\) coordinatewise with \(\sum_i c_i=7-w\). For two bin vectors \(b,b'\) with the same sum, a common descendant exists exactly when
\[
\sum_i\max(b_i,b'_i)\le 7-w.
\]
Since
\[
\sum_i\max(b_i,b'_i)=(5-w)+\frac12\lVert b-b'\rVert_1,
\]
the two descendant sets are disjoint exactly when
\[
\lVert b-b'\rVert_1\ge6.
\]

For \(w=0\) there is only one derivative. For \(w=1\), the bin vectors are \((j,4-j)\) for \(0\le j\le4\); their distance is \(2|j-k|\), so a compatible pair requires \(|j-k|\ge3\). The maximum is therefore \(2\), and exactly the three pairs with index sets \({0,3},{0,4},{1,4}\) attain it.

For \(w=2\), the bin vectors are nonnegative triples summing to \(3\). Their \(\ell_1\)-distance is at most \(6\), with equality exactly when their supports are disjoint. A compatible family therefore has at most three members. Equality forces the unique triple
\[
(3,0,0),\quad(0,3,0),\quad(0,0,3).
\]
Thus the layer maximum is \(3\) and its maximizing family is unique.

For \(w\ge3\), the zero-bin sum is at most \(2\), so any two bin vectors have \(\ell_1\)-distance at most \(4\). Consequently each such layer contributes at most one derivative. The numbers of possible singleton choices are respectively \(\binom53=10\), \(\binom54=5\), and \(\binom55=1\).

Adding the six independent weight-layer maxima gives \(9\) per first-bit sector. Multiplying their equality counts gives \(1\cdot3\cdot1\cdot10\cdot5\cdot1=150\). Since the first bit is invariant, the two sectors are independent, so every global code has size at most \(9+9=18\), and equality requires a sector maximum on each side. Hence there are exactly \(150^2=22{,}500\) labeled maximum codes.

Finally, for derivative weight \(w\), the number of distinct descendants after two repetitions is the number of weak compositions of \(2\) into \(w+1\) bins,
\[
\binom{w+2}2.
\]
Using the layer multiplicities \((1,2,3,1,1,1)\), one first-bit sector covers
\[
1+2\cdot3+3\cdot6+10+15+21=71
\]
outputs. The two sectors are disjoint, so a maximum covers \(142\) of the \(256\) possible length-eight outputs.

## Verification
The standalone script `verify.py` reconstructs all \(64\) source words and their exact one- and two-repetition descendant sets. It verifies, for every source word, that one repetition agrees exactly with zero insertion in the derivative. On every unordered source pair it checks that exact-two correction implies exact-one correction. On every pair in each fixed-first-bit, fixed-derivative-weight layer it independently compares direct descendant-ball disjointness with the bin-vector criterion \(\lVert b-b'\rVert_1\ge6\).

The script then exhaustively enumerates every subset of every derivative-weight layer, verifies the six layer optima and all equality counts, constructs all \(150\) maximum codes in each first-bit sector, directly rechecks their one- and two-repetition correction property, and verifies the \(71\)-output sector coverage. Running `python3 verify.py` must reproduce the single line stored in `EXPECTED.txt`.

## Relationship to prior work
Dolecek and Anantharam introduced the same repetition-error model and explicitly study maximally sized equal-length binary sets immune to a prescribed number of repetitions. Their derivative transformation converts repetition errors to zero insertions, and their multiple-repetition results give constructions and asymptotic bounds rather than this finite \(n=6\), two-repetition equality classification. The 2007 ISIT paper is the earliest day-resolved public source used here; its conference dates are June 24--29, 2007. The expanded 2010 paper has primary classification 94B50.

Jain, Farnoud, Schwartz, and Bruck later formulate fixed-length tandem-duplication correction and reduce bounded-duplication codes to constant-weight \(\ell_1\) codes. Their framework contains the present length-one duplication model but does not state the \(18\) optimum or the \(22{,}500\)-code equality census. Kovačević and Tan derive asymptotic cardinality bounds for fixed-length duplication codes; their exact asymptotic coincidence concerns one duplication, not this finite two-duplication case.

Targeted searches over repetition-error, zero-insertion, tandem-duplication, exact-parameter, and equality-classification aliases, together with the checked published-finding index, found no statement implying this finite classification. This negative search evidence is not treated as a proof of priority.

## Limitations
The proof is finite and exact only for binary length \(6\) and at most two length-one tandem duplications. It does not classify symmetry orbits of the maximum codes and does not extrapolate the finite pattern to arbitrary length. The originality comparison retains a residual risk of an obscure or unindexed historical small-parameter enumeration. Independent audit has not been performed.

## References
1. L. Dolecek and V. Anantharam, “On Subsets of Binary Strings Immune to Multiple Repetition Errors,” IEEE International Symposium on Information Theory, 2007, pp. 1691--1695; bibliographic key `dblp:conf/isit/DolecekA07`.
2. L. Dolecek and V. Anantharam, “Repetition Error Correcting Sets: Explicit Constructions and Prefixing Methods,” SIAM Journal on Discrete Mathematics 23(4), 2120--2146, DOI `10.1137/080730093`.
3. S. Jain, F. Farnoud, M. Schwartz, and J. Bruck, “Duplication-Correcting Codes for Data Storage in the DNA of Living Organisms,” arXiv `1606.00397`.
4. M. Kovačević and V. Y. F. Tan, “Asymptotically Optimal Codes Correcting Fixed-Length Duplication Errors in DNA Storage Systems,” arXiv `1808.10328`.
