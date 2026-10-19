# Exact FCSR-denominator and reversal spectrum of binary order-five de Bruijn cycles

## Finding
Let \(\mathcal D_5\) be the set of binary de Bruijn cycles of order five, modulo cyclic rotation but not modulo reversal or bit complementation. There are exactly \(2048\) members. For a cycle \(B\), choose any linear representative \(b_0b_1\cdots b_{31}\), put
\[
S(B)=\sum_{j=0}^{31} b_j2^j,\qquad M=2^{32}-1=4294967295,\qquad g(B)=\gcd(S(B),M),\qquad q(B)=M/g(B).
\]
The denominator \(q(B)\) of the reduced periodic 2-adic expansion is the FCSR connection denominator. The associated 2-adic complexity is \(\log_2 q(B)\). Cyclic rotation does not change \(g(B)\).

The complete distribution of \(g(B)\), with no other possible values, is

| \(g(B)\) | Number of cycles | \(q(B)\) |
|---:|---:|---:|
| 1 | 1138 | 4294967295 |
| 3 | 450 | 1431655765 |
| 5 | 214 | 858993459 |
| 15 | 118 | 286331153 |
| 17 | 62 | 252645135 |
| 51 | 28 | 84215045 |
| 85 | 8 | 50529027 |
| 255 | 26 | 16843009 |
| 257 | 2 | 16711935 |
| 3855 | 2 | 1114129 |

Let \(B^{\mathrm R}\) be the reverse cycle. The **complete joint unordered reversal spectrum**, counting each of the \(2048\) cycles once, is:

| \(\{g(B),g(B^{\mathrm R})\}\) | Number of cycles |
|:---:|---:|
| \(\{1,1\}\) | 924 |
| \(\{1,5\}\) | 332 |
| \(\{1,17\}\) | 76 |
| \(\{1,85\}\) | 16 |
| \(\{1,257\}\) | 4 |
| \(\{3,3\}\) | 364 |
| \(\{3,15\}\) | 116 |
| \(\{3,51\}\) | 48 |
| \(\{3,255\}\) | 4 |
| \(\{3,3855\}\) | 4 |
| \(\{5,5\}\) | 36 |
| \(\{5,17\}\) | 24 |
| \(\{15,15\}\) | 56 |
| \(\{15,51\}\) | 8 |
| \(\{17,17\}\) | 12 |
| \(\{255,255\}\) | 24 |

Exactly \(632\) cycles have unequal denominators after reversal, or \(316\) reversal-pairs. The maximum ratio of their denominators is \(1285\), attained when the two gcds are \(3\) and \(3855\). Thus reversal can change 2-adic complexity by exactly \(\log_2 1285\), even though classical binary linear complexity is reversal-invariant. For example, the canonical cycle `00000111000100110110010101111101` has \(g=3855\), whereas its reversal has \(g=3\); both have binary linear complexity \(31\). The two \(g=3855\) cycles have linear complexity \(31\).

## Assumptions and scope
A binary de Bruijn cycle of order five has length \(32\) and contains each five-bit binary word at exactly one circular starting position. Cycles are identified only up to rotation. Every cycle has a unique occurrence of `00000`; the supplied `cycles.csv` writes each rotation class beginning there. The polynomial and integer generating functions use least-significant-bit-first indexing exactly as in the definition of \(S(B)\). Reverse means reversal of the underlying circular sequence, followed by the same canonical rotation. The invariant \(g\) is independent of which rotation is used, since a rotation multiplies \(S\) by a power of two modulo \(M\), and \(\gcd(2,M)=1\). Complementation maps \(S\) to \(M-S\), preserving \(g\). Reversal does not generally preserve \(g\).

The output is a finite exact classification at order five, plus the stated rotation/complement invariances, with no general higher-order distribution claimed.

## Proof
**Arithmetic reduction.** The 2-adic sum of the infinite periodic sequence equals
\[
\sum_{t=0}^{\infty}S(B)2^{32t}=\frac{S(B)}{1-2^{32}}=-\frac{S(B)}{M}.
\]
After cancellation its positive denominator is exactly \(q(B)=M/\gcd(S(B),M)\), and the numerator magnitude is smaller than this denominator, so the standard strictly periodic 2-adic complexity is \(\log_2 q(B)\). Since \(M=3\cdot5\cdot17\cdot257\cdot65537\) is squarefree, \(g\) can also be computed by testing divisibility by these five primes. The verifier implements both this prime-divisibility calculation and an independent Euclidean gcd calculation and confirms equality for every cycle and its reverse.

**Completeness of the cycle domain.** Use the standard directed binary order-four de Bruijn graph: its \(16\) vertices are four-bit words and its \(32\) edges are five-bit words, each edge going from its first four bits to its last four. Every vertex has two incoming and two outgoing edges. An Euler circuit induces a bijection between the two incoming and two outgoing incident edges at every vertex; hence it induces one of \(2^{16}=65536\) local pairing assignments. Conversely, each assignment induces a permutation of all \(32\) edges, and it forms a single Euler circuit precisely when this permutation has a single cycle of length \(32\). Fixing the unique five-bit edge `00000` as the first edge removes all rotational duplication. Therefore enumerating and retaining the single-cycle pairings is exhaustive and has no duplicate rotation classes. The verifier separately enumerates all Euler circuits using depth-first search from the fixed edge. These two logically independent complete generators produce exactly the same set of \(2048\) normalized cycles, with all \(32\) five-bit factors verified distinct for each.

**Exhaustive classification.** For each of the \(2048\) cycles, the verifier computes \(g\) by both methods; it independently computes the same two arithmetic quantities on the reversed sequence. It tallies each gcd and the unordered pair of the original and reversed gcds. These exact integer counts produce the two complete tables, and each table sums to \(2048\). The checker also confirms the complement invariance and checks ordinary binary linear complexity by two different methods: polynomial multiplicity in characteristic two and Berlekamp–Massey applied to two periods. It checks reversal invariance of that characteristic-two complexity and the reported example. The complete independent input/output table in `cycles.csv` provides the canonical binary cycle, \(g(B)\), \(g(B^{\mathrm R})\), and the ordinary binary linear complexity on every row. The executable `verify.py` reconstructs and checks the table from first principles.

## Verification
Run `python verify.py cycles.csv` with Python 3.10 or later and the Python standard library. The program rebuilds all \(65536\) pairing assignments and independently enumerates the Eulerian circuits, computes every invariant with two methods, compares all \(2048\) sorted rows of `cycles.csv`, tests the exact table constants, and prints `VERIFY_OK` markers if all assertions pass. It uses integer arithmetic, so no numerical precision tolerance is involved. Both the exhaustive generating algorithms and the independent denominator tests are in the package rather than assumed from an external table. The explicit csv is a record of all \(2048\) cycles, not a sampling experiment.

## Relationship to prior work
Klapper and Goresky established the mathematical FCSR framework, including its representation of periodic binary sequences by rational 2-adic numbers and the concept of connection denominators. Etzion and Lempel gave distributional results for the **ordinary binary linear complexity** of de Bruijn sequences. Zhao, Wen, Zhang, and Jin studied bounds and counting functions for 2-adic complexity of general prime-power-period binary sequences. The accessible abstract of their 2012 article does not describe an exact classification conditioned on the order-five de Bruijn property, but its complete text was not accessible; no negative full-text conclusion is drawn. Ren and Winterhof studied general reversal behavior of 2-adic complexity, including a demonstration that it need not be reversal invariant. None of the accessible, inspected full-text works gives the two exact order-five tables here. Their broader definitions, bounds, and examples are not treated as equivalent to a complete de Bruijn-restricted frequency census. Earlier inaccessible or unindexed work may still contain overlapping results; the classification is not asserted to establish historical priority conclusively.

## Limitations
The full 2-adic gcd histogram and reverse-pair spectrum are proved only for order five. The calculations do not establish a distribution at orders six or above, an asymptotic law, or real-world cryptographic security. The standard denominator-to-complexity conversion is cited rather than claimed as new. The GF(2) linear-complexity facts are supporting comparisons and not claimed as independently new. The relevant 2012 period-general paper could be inspected at abstract level only, leaving a residual historical-priority uncertainty. Computational completeness depends on the explicit exhaustiveness argument for the two finite generators and the reproducibility of the contained code; no infinite theorem is inferred from finite tests.

## References
- A. Klapper and M. Goresky, *Feedback Shift Registers, 2-Adic Span, and Combiners With Memory*, author-available full text: https://www.cs.uky.edu/~klapper/pdf/fcsr.pdf.
- T. Etzion and A. Lempel, *On the Distribution of de Bruijn Sequences of Given Complexity*, IEEE Transactions on Information Theory, 30(4), 1984, 611–614. Full text: https://etzion.net.technion.ac.il/files/2016/02/P3.pdf.
- T. Etzion, *Linear Complexity of de Bruijn Sequences—Old and New Results*, IEEE Transactions on Information Theory, 45, 1999. Author-available full text: https://etzion.net.technion.ac.il/files/2016/02/P51.pdf.
- L. Zhao, Q.-Y. Wen, J. Zhang and Z.-P. Jin, *On the 2-Adic Complexity of Periodic Binary Sequences*, IEICE Transactions on Fundamentals, E95-A (2012), 367–371, https://doi.org/10.1587/transfun.E95.A.367 (publisher abstract inspected; complete text not accessed).
- Y. Ren and A. Winterhof, *Symmetric measures of pseudorandomness for binary sequences*, arXiv:2603.23166, https://arxiv.org/pdf/2603.23166 (complete primary text inspected; used for context only).
