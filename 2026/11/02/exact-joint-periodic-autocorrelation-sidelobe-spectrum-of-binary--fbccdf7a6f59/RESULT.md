# Exact joint periodic-autocorrelation sidelobe spectrum of binary order-five de Bruijn cycles

## Finding
Let \(\mathcal B_5\) be the set of binary de Bruijn cycles of order five, counted modulo rotation but not reversal or complementation. Every \(W\in\mathcal B_5\) has length \(32\) and exactly one cyclic occurrence of each binary length-five word. Represent it as \(w_0\ldots w_{31}\), set \(s_i=(-1)^{w_i}\), and define its unnormalized periodic autocorrelation and its two nontrivial extremal sidelobes by
\[
R_W(t)=\sum_{i=0}^{31}s_i s_{(i+t)\bmod 32},\qquad
m(W)=\min_{1\le t\le31}R_W(t),\qquad
p(W)=\max_{1\le t\le31}R_W(t).
\]
The complete joint distribution of \((m(W),p(W))\) among all \(2{,}048\) cycles is as follows. Each entry is the exact number of distinct cycles; all unlisted pairs have zero multiplicity.

| \(m\) / \(p\) | \(0\) | \(4\) | \(8\) | \(12\) | \(16\) | Total |
|---:|---:|---:|---:|---:|---:|---:|
| \(-24\) | 0 | 0 | 4 | 0 | 8 | 12 |
| \(-20\) | 0 | 0 | 44 | 36 | 8 | 88 |
| \(-16\) | 0 | 100 | 140 | 22 | 6 | 268 |
| \(-12\) | 0 | 214 | 612 | 32 | 6 | 864 |
| \(-8\) | 4 | 356 | 404 | 24 | 8 | 796 |
| \(-4\) | 0 | 12 | 8 | 0 | 0 | 20 |
| Total | 4 | 682 | 1212 | 114 | 36 | 2048 |

Exactly twenty pairs of extremal sidelobes occur. In particular, precisely four cycles have no positive nonzero autocorrelation sidelobe, and their common minimum is \(-8\). The previously reported thresholds of twelve cycles with all sidelobes of magnitude at most four and 784 with all sidelobes of magnitude at most eight are recovered as exact sums of entries, but they do not determine the joint table.

## Assumptions and scope
The order is fixed at five, the alphabet is \(\{0,1\}\), and the word is circular. Cyclic rotations are identified and no other symmetries are factored out. Bipolar encoding \(0\mapsto+1\), \(1\mapsto-1\) is used. Both \(m\) and \(p\) range over shifts \(1\le t\le31\), excluding shift zero, where correlation is \(32\). Correlations are integer sums, not divided by \(32\). Dividing every table row and column label by \(32\) gives the corresponding normalized-extremum distribution.

## Proof
**1. Exhaustive feedback parametrization.** Interpret a five-bit state as \(bu\), where \(b\in\{0,1\}\) is the first bit and \(u\in\{0,1\}^4\) is the four-bit suffix. For a de Bruijn cycle, the successor on five-bit windows traverses each of the \(32\) states once, hence is a permutation. The states \(0u\) and \(1u\) have successors in \(\{u0,u1\}\); since the successor map is injective, their appended bits differ. Consequently every de Bruijn cycle determines a unique Boolean function \(g:\{0,1\}^4\to\{0,1\}\) such that its five-bit successor is
\[
T_g(bu)=u\bigl(b\oplus g(u)\bigr).
\]
Conversely, for any Boolean \(g\), this formula sends \(0u\) and \(1u\) bijectively onto \(u0,u1\), so it is a permutation of all \(32\) states. It yields an order-five de Bruijn cycle exactly when the orbit of state \(00000\) under \(T_g\) has length \(32\). Thus checking the \(2^{16}=65{,}536\) Boolean truth tables is an exhaustive finite decision procedure, not a sample. Every de Bruijn cycle has a unique occurrence of \(00000\), giving a unique root, and the resulting rooted word recovers \(g\). Hence successful truth tables correspond bijectively to distinct cyclic de Bruijn words.

**2. Integer expression for the invariant.** On each successful orbit, output its successive first state bits to obtain \(W=w_0\ldots w_{31}\). For every shift \(t\), the two equivalent exact expressions are
\[
R_W(t)=\sum_{i=0}^{31}(-1)^{w_i+w_{(i+t)\bmod32}}
=32-2\,d_H(W,\operatorname{rot}_t(W)),
\]
where \(d_H\) is Hamming distance. Both expressions are calculated independently in the attached `verify.py`. The code examines all shifts \(1\) through \(31\) for all successful feedback functions and increments one exact integer counter for the pair of extrema.

**3. Exhaustive finite certificate.** The standalone certificate implements the finite sets and transition of step 1 directly, and asserts the whole twenty-cell table (including zero cells), the total \(2048\), and all row and column totals. For an independent coverage check it separately constructs all de Bruijn words by depth-first extension of the canonical prefix `00000`, forbidding repeated length-five windows and checking the four cyclic wraparound windows. These two differently parametrized constructions yield identical sets of exactly \(2048\) rooted words. A direct bipolar dot product and a bit-rotation/XOR-popcount calculation agree at every one of the \(31\) nonzero shifts for each word. These finite, exact, fully specified loops and assertions establish every displayed multiplicity.

## Verification
Running `python3 verify.py` using Python 3 with arbitrary-precision integers and no external packages prints `VERIFY_OK`. The SHA-256 digest of the sorted canonical root words, joined with one newline after each, is `e8b5746482780303fec542789b123a2d51a892f460137bb9f8a96c85fec30421`. The verified integer row vectors (columns \(0,4,8,12,16\)) are
\[
\begin{aligned}
-24 &: (0,0,4,0,8),\\
-20 &: (0,0,44,36,8),\\
-16 &: (0,100,140,22,6),\\
-12 &: (0,214,612,32,6),\\
-8 &: (4,356,404,24,8),\\
-4 &: (0,12,8,0,0).
\end{aligned}
\]
The checks separately reproduce the previously published twelve and 784 low-absolute-sidelobe counts. The theoretical coverage argument is essential: agreement of two partial experiments alone would not prove exhaustive coverage.

## Relationship to prior work
Spinsante, Andrenacci, and Gambi (2011) examine the complete family of \(2048\) order-five cycles and report the cardinalities of the families whose maximum absolute sidelobes are at most four and eight, respectively \(12\) and \(784\), together with average correlation information. Fujisaki and Nabeshima (2011) give autocorrelation bounds and tabulate the most negative, second-most-negative, and maximum positive sidelobes with associated shifts for small orders. Both are important antecedents and the listed facts are **not new**. Neither of their inspected full texts supplies or implies the exact joint \((m,p)\) classification in the table above: the published partial counts and thresholds do not fix the remaining cells. The new claim is the complete joint extremal distribution and its exact finite certificate, not a new general de Bruijn counting formula or a new absolute peak-sidelobe optimum.

## Limitations
This is an exhaustive finite classification at order five only. It does not determine distributions at order six or beyond, general bounds for arbitrary orders, pairwise cross-correlation between different cycles, or communications performance. Exhaustive verification of a finite universe is distinct from a general infinite-order theorem. The accessible prior work does not settle historical priority against every possible unindexed table; independent scientific review remains outstanding.

## References
1. S. Spinsante, S. Andrenacci, and E. Gambi, "Binary De Bruijn sequences for DS-CDMA systems: analysis and results," *EURASIP Journal on Wireless Communications and Networking*, 2011:4, first published 2011-06-06. DOI: https://doi.org/10.1186/1687-1499-2011-4 . Full OA text: https://link.springer.com/article/10.1186/1687-1499-2011-4 .
2. H. Fujisaki and Y. Nabeshima, "On auto-correlation values of de Bruijn sequences," *Nonlinear Theory and Its Applications, IEICE* 2(4), 400–408 (2011), published 2011-10-01. DOI: https://doi.org/10.1587/nolta.2.400 . Full OA PDF: https://www.jstage.jst.go.jp/article/nolta/2/4/2_4_400/_pdf/-char/en .
3. N. G. de Bruijn, "A combinatorial problem," *Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen* 49 (1946), 758–764 (classical cycle enumeration).
