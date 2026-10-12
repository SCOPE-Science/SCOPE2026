# A maximal-length binary linear three-read MDS code of dimension five

## Finding
There exists a binary linear code of length \(20\) and dimension \(5\) with minimum cyclic three-symbol distance \(18\). It attains simultaneously the three-symbol Singleton and binary three-symbol Griesmer bounds. Moreover, **no binary linear code of dimension \(5\) and cyclic three-symbol distance at least \(n-2\) has length \(n>20\)**. Thus the exact largest length of a dimension-five binary linear three-symbol MDS code is \(20\). The witness has thirty nonzero words of three-symbol weight \(18\) and one of weight \(20\).

## Assumptions and scope
Over \(\mathbb F_2\), the three-symbol weight of a length-\(n\) vector \(c\) is the number of indices \(i\in\mathbb Z/n\mathbb Z\) for which \((c_i,c_{i+1},c_{i+2})\ne(0,0,0)\). Three-symbol distance is the three-symbol weight of a difference. All indices are cyclic. For a linear code of dimension \(5\), the three-symbol Singleton bound is \(d_3\le n-5+3=n-2\). All claimed lengths satisfy \(n\ge5\).

Take the \(5\)-by-\(20\) binary generator matrix \(G\) whose columns, left to right, are the five-bit vectors whose least-significant-bit-first integer encodings are

```
31, 6, 24, 12, 8, 25, 18, 27, 7, 19,
2, 29, 30, 23, 4, 5, 14, 13, 21, 15
```

Equivalently, its five rows are

```
10000101110101010111
11000011111011001001
11010000100111111111
10111101000110001101
10100111010111000010
```

An integer encoding is only a compact way to specify generator columns, not an exponent or a finite-field power.

## Proof
**Lower bound (existence).** For a message \(u\in\mathbb F_2^5\), its associated codeword is \(c(u)=uG\). Exhaustive finite enumeration of all \(32\) messages, using the transparent standalone verifier below, establishes that the \(32\) codewords are distinct. Hence \(\operatorname{rank}(G)=5\). For each nonzero message, count the starts of cyclic all-zero length-three windows in \(c(u)\). The verified exact multiset is thirty copies of \(2\) and one copy of \(0\), with the latter at message integer \(14\) in least-significant-bit-first encoding. Therefore the minimum three-symbol distance is \(20-2=18\), and the nonzero weight enumerator is \(30z^{18}+z^{20}\).

**Upper bound (universal).** Let \(H\) be any generator matrix of a binary linear dimension-five length-\(n\) code, where \(n\ge5\), and suppose its minimum three-symbol distance is at least \(n-2\). Define \(Z_u\) as the number of cyclic all-zero length-three windows in the codeword \(uH\), for nonzero messages \(u\in\mathbb F_2^5\). By the hypothesis, \(Z_u\le2\); thus \(\sum_{u\ne0} Z_u\le2(2^5-1)=62\). On the other hand, fix a position \(i\). The three columns of \(H\) beginning there impose at most three independent homogeneous linear equations on five message coordinates. Hence their common kernel has dimension at least two and contains at least \(2^2-1=3\) nonzero messages. Every cyclic position therefore contributes at least three to the same incidence sum, giving \(3n\le62\), and so \(n\le20\). This requires no assumptions about cyclic invariance, repeated columns, or a particular construction family.

**Tight bounds.** The Singleton bound gives \(d_3\le20-5+3=18\), met by the witness. The binary three-symbol Griesmer inequality from Luo and coauthors reads

\[
(2^3-1)n\ \ge\ \sum_{j=0}^{4}\left\lceil\frac{2^{3-1}d_3}{2^j}\right\rceil.
\]

For \(n=20\), \(d_3=18\), both sides equal \(140\): the summands are \(72,36,18,9,5\). The equality demonstrates sharpness of the established bound; it is not used to prove the finite existence witness. The same Griesmer bound already implies the upper length restriction for Singleton-tight codes and is acknowledged as prior theoretical coverage of that part of the statement.

## Verification
The included standalone `verify_code.py` uses no third-party packages. Running `python3 verify_code.py` enumerates all messages and the cyclic three-read windows, checks the rank and exact weight distribution, confirms that every cyclic three-column block has rank three, and verifies the two bounds. Every arithmetic certificate is exhaustively finite and is reproducible directly from the printed generator.

## Relationship to prior work
Ding, Zhang and Ge (2016) introduced the three-symbol Singleton bound and explicit MDS families, but the families displayed in the inspected original paper address different three-read distances and do not provide this \([20,5,18]\) binary instance. Luo, Ezerman, Güneri, Ling and Özbudak (2024) give the general binary three-symbol Griesmer inequality and cyclic/extended-cyclic families at other lengths; their inequality supplies the pre-existing upper-bound implication. The newly demonstrated content here is **an explicit realizing code at the exact extremal length**, which is not obtained from either inequality by itself. Kurz (2025) treats eventual Griesmer-bound attainment for sufficiently large distances and explicitly completes small-dimension parameters for the pair-symbol case; the inspected text does not state this specific three-read construction. No claim of exhaustive classification of inequivalent optimal codes is made.

## Limitations
The maximum concerns *linear binary* codes of dimension exactly five and the *cyclic three-symbol* read metric. It is not an upper bound for arbitrary nonlinear codes or for other dimensions. Exhaustive verification is a complete proof of the displayed finite witness, but not a classification of all optimal generators. The existence of an earlier equivalent unpublished, unindexed or implicit construction cannot be excluded.

## References
1. G. Luo, M. F. Ezerman, C. Güneri, S. Ling, F. Özbudak, *Griesmer Bound and Constructions of Linear Codes in b-Symbol Metric*, arXiv:2401.04941, first submitted 10 January 2024. https://arxiv.org/abs/2401.04941
2. B. Ding, T. Zhang, G. Ge, *Maximum Distance Separable Codes for b-Symbol Read Channels*, arXiv:1609.09236, first submitted 29 September 2016. https://arxiv.org/abs/1609.09236
3. S. Kurz, *Linear codes for b-symbol read channels attaining the Griesmer bound*, arXiv:2507.07728, first submitted 10 July 2025. https://arxiv.org/abs/2507.07728
