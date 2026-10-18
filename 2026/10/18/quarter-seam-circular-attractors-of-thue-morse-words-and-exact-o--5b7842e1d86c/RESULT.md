# Quarter-seam circular attractors of Thue–Morse words and exact order-seven/eight extremizers

## Finding
Write \(t_n=\mu^n(0)\) for the finite binary Thue–Morse word, with \(\mu(0)=01\) and \(\mu(1)=10\), and write \(N=2^n\). A *circular string attractor* is a subset of the positions of \(t_n\) that meets some cyclic occurrence of every nonempty circular factor of length at most \(N\). Positions are numbered \(0,\ldots,N-1\), modulo \(N\).

**Theorem.** For every integer \(n\ge4\), the minimum circular string-attractor cardinality of \(t_n\) is exactly \(4\). In addition, let \(m=2^{n-2}\) and \(B_n=\{0,m,2m,3m\}\). For every choice of one position from each cyclic adjacent pair \(\{b-1,b\}\), \(b\in B_n\), the resulting four positions form a smallest circular attractor. These are \(16\) distinct attractors for each \(n\ge4\).

For \(n=7\) and \(n=8\) there are **exactly \(80\)** smallest circular attractors, and they admit a complete classification. Put \(h=2^{n-4}\), and define
\[
\mathcal B=\big\{(0,4,8,12),(2,4,10,12),(2,5,10,13),(3,6,11,14),(4,6,12,14)\big\}.
\]
For each tuple \((j_1,j_2,j_3,j_4)\in\mathcal B\), independently select one endpoint from each cyclic pair \(\{j_i h-1,j_i h\}\). The resulting \(5\cdot 2^4=80\) sets are **all** smallest circular attractors, with no duplicates.

The complete small-order counts of smallest attractors, for \(n=2,3,4,5,6,7,8\), are respectively \(2,2,151,96,96,80,80\); the corresponding minimum cardinalities are \(2,2,4,4,4,4,4\). Only the optimum size and the quarter-seam subfamilies are asserted at all larger orders. No formula for the *total* number of smallest circular attractors beyond order \(8\) is proved here.

## Assumptions and scope
For a word \(w\) of length \(N\), a circular factor of length \(\ell\), with \(1\le\ell\le N\), is the word read from some start \(s\) along \(\ell\) consecutive positions of the circle. An occurrence at \(s\) covers positions \(s,s+1,\ldots,s+\ell-1\pmod N\). A selected set is an attractor precisely when each distinct circular factor admits a covered occurrence. Unlike a linear string attractor, cyclic occurrences crossing the end-to-start seam are allowed.

The general theorem applies only to the explicitly given binary substitution words and the standard circular-factor definition. It does not assert an infinite-order characterization of all optimal position sets, nor a classification of arbitrary cyclic binary words.

## Proof
**Boundary transport.** Put \(U_r(a)=\mu^r(a)\) for \(a\in\{0,1\}\). We prove, by induction on \(r\), that for any factor \(z\) of \(U_r(a)\) with \(|z|\ge2\), there exist \(x,y\in\{0,1\}\) such that \(z\) occurs in \(U_r(x)U_r(y)\) at an interval containing both positions immediately adjacent to the block boundary. At \(r=0\), no such factor exists.

For the induction, the identity \(U_{r+1}(a)=U_r(a)U_r(1-a)\) splits a factor \(z\) into two cases. If one occurrence of \(z\) crosses this internal boundary, the same occurrence crosses the boundary of \(U_{r+1}(1-a)U_{r+1}(1-a)\): the two adjacent \(r\)-blocks there are exactly \(U_r(a)U_r(1-a)\). Otherwise, the occurrence is contained in a single \(r\)-block. By induction it occurs across some boundary \(U_r(x)\mid U_r(y)\), which is the boundary between \(U_{r+1}(1-x)\) and \(U_{r+1}(y)\). In either case the transferred occurrence contains both positions adjacent to the larger boundary. This proves the property at every \(r\).

For \(n\ge2\), let \(r=n-2\). The cyclic four-block decomposition of \(t_n\) is
\[
U_r(0)\,U_r(1)\,U_r(1)\,U_r(0),
\]
whose four cyclic seams realize **all four ordered pairs** of block types, \(01,11,10,00\). Every cyclic factor of length at least \(2\) either has an occurrence crossing a four-block seam already, or has an occurrence wholly inside one block, to which the boundary-transport property applies. Therefore that factor has an occurrence containing both endpoints of one of the four seams. Selecting either endpoint of each seam meets this occurrence. For one-letter factors, the four seams realize every ordered pair of **actual binary letters**: the first letter of \(U_r(a)\) is \(a\), and the last is \(a\) for even \(r\), \(1-a\) for odd \(r\). In particular one seam has adjacent letters \(00\) and another has \(11\), so any selection of seam endpoints covers both letters. Thus all stated quarter-seam choices are circular attractors. For \(n\ge4\), their four adjacent endpoint pairs are disjoint, giving \(16\) distinct size-four sets.

**Lower bound for every \(n\ge6\).** The first \(64\) letters of \(t_n\) form \(t_6\). The latter contains exactly \(40\) distinct *linear* factors of length \(13\) (the standalone exhaustive generator independently checks this finite premise). All \(40\) are circular factors of every \(t_n\), \(n\ge6\). For any one selected circular position, exactly \(13\) cyclic length-\(13\) starting positions have occurrences crossing it; it therefore covers at most \(13\) distinct length-\(13\) factors. Three positions cover at most \(39\) distinct such factors. Consequently at least four selected positions are necessary. Combined with the construction this proves the infinite cardinality assertion for \(n\ge6\).

**Orders four and five and exact finite classifications.** For \(n=4,5\), exhaustive finite factor-coverage enumeration establishes no three-position attractor and confirms four-position attractors. For \(n=2,3,4,5,6,7,8\), the computation also determines the *complete* family of minimum hitting sets. Specifically, for each cyclic factor \(z\), let \(C_z\) be the union of positions hit by at least one occurrence of \(z\). A set is an attractor if and only if it intersects every \(C_z\). An inclusion-minimal family of these finite sets has the same hitting sets as the full family. The executable checker constructs these exact sets at **all** lengths \(1\) through \(N\), reduces them by inclusion, and exhaustively branches on the positions of a not-yet-hit constraint. Every possible solution has to take at least one such position, so branching is complete. It establishes the numerical counts listed in the theorem. For \(n=7,8\) it also constructs, independently, the \(80\) candidate sets from the five asserted families and tests exact equality of sets with the exhaustive enumeration. This proves both their sufficiency and their necessity at those two specified orders.

## Verification
Execute `python verify.py` using Python 3 with the standard library. The program constructs every distinct circular factor and its union-of-occurrences position mask; it then removes redundant superset constraints, exhausts every smaller cardinality, and enumerates all minimum transversals. The exact outputs are in `verification_output.txt`. Reproducible values are: minimum-covering counts \(2,2,151,96,96,80,80\) at orders \(2\) through \(8\), minimal-constraint counts \(4,4,14,20,28,36,44\), and \(40\) distinct linear length-\(13\) factors in \(t_6\). The generated optimizer families are compared by equality of full bitmask sets, not by sample sizes or unverified pattern fitting. The infinite boundary-transport induction and counting lower bound are mathematical arguments independent of the finite optimizer census.

## Relationship to prior work
Romana's 2023 *Algorithmic View on Circular String Attractors* develops the circular definition and verification algorithms, using Fibonacci words as examples; it does not give a Thue–Morse minimum or a complete enumeration. The 2026 full-text work of Faro, Marino, and Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words* (arXiv:2610.10950v1, first posted 2026-10-07), determines the **linear** attractor families (\(32\) smallest attractors for \(n\ge6\)), not circular ones. Its center-transport argument supplies useful background but does not assert the quarter-seam cyclic theorem or the five-family \(80\)-set classification. Banbara et al.'s 2026 Thue–Morse extension likewise concerns linear attractors. The present circular families are different: cyclic occurrences are allowed to wrap, so linear and circular coverage constraints do not imply each other's exact extremizer classifications.

## Limitations
The fully explicit enumeration of **all** optimal circular position sets stops at order \(8\). The observed \(80\)-set count at two successive orders must not be extrapolated as a theorem to higher orders. The exhaustive finite checks are not a substitute for the infinite boundary-transport argument. Originality is assessed against accessible published records and cited full-text sources; unindexed earlier results or equivalent terminology remain possible. Independent scientific validation has not been performed.

## References
1. S. Faro, F. P. Marino, A. Pavone, *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words*, arXiv:2610.10950v1, 2026-10-07, https://arxiv.org/html/2610.10950v1.
2. G. Romana, *Algorithmic View on Circular String Attractors*, ICTCS 2023, pp. 169–180, https://ceur-ws.org/Vol-3587/9885.pdf.
3. S. Mantaci, A. Restivo, G. Romana, G. Rosone, M. Sciortino, *A combinatorial view on string attractors*, Theoretical Computer Science 850 (2021), 236–248, DOI:10.1016/j.tcs.2020.11.006.
4. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, Y. Okamoto, *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, arXiv:2602.16152 (first posted 2026-02-18), https://arxiv.org/html/2602.16152v3.
