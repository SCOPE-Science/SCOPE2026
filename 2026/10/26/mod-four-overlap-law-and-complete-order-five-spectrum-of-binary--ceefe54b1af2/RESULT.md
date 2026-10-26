# Mod-four overlap law and complete order-five spectrum of binary de Bruijn cycles

## Finding

Let \(\mathcal D_k\) be the set of binary cyclic de Bruijn sequences of order \(k\), with sequences identified precisely under cyclic rotation (not reversal or symbol complementation). For \(S,T\in\mathcal D_k\), let \(I(S,T)\) be the number of *distinct* length-\(k+1\) binary strings that occur as circular factors of both cycles.

**Universal law.** For every integer \(k\ge2\) and every \(S,T\in\mathcal D_k\),
\[
I(S,T)\ge4,\qquad I(S,T)\equiv0\pmod4.
\]
This includes \(S=T\), for which \(I(S,S)=2^k\).

**Exact order-five distribution.** For the \(2048\) members of \(\mathcal D_5\), the complete unordered *distinct-pair* distribution is:

| Shared circular length-six factors \(I(S,T)\) | Number of unordered pairs |
|---:|---:|
| \(4\) | \(368\) |
| \(8\) | \(27104\) |
| \(12\) | \(254800\) |
| \(16\) | \(710976\) |
| \(20\) | \(758800\) |
| \(24\) | \(305376\) |
| \(28\) | \(38704\) |

All other overlap values occur zero times. The seven counts sum to \(\binom{2048}{2}=2096128\). Exactly \(368\) unordered pairs attain the universal lower bound \(4\). Each cycle has at most one such partner; consequently exactly \(736\) cycles (fraction \(23/64\)) have a best-possible partner and the remaining \(1312\) do not.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). A cyclic de Bruijn sequence of order \(k\) has length \(2^k\), with each binary word of length \(k\) occurring exactly once when cyclic wrap-around is included. A factor at a circular position uses the next symbols modulo the period. Only rotations are identified; reversing or complementing a sequence produces a possibly different member. The universal law holds for all \(k\ge2\); the complete numerical pair distribution is asserted **only** for \(k=5\). The phrase "near-orthogonal" in the discussion refers to minimizing shared length-\(k+1\) factors, not to zero-overlap orthogonality.

## Proof

**1. Local transition encoding.** Use the directed binary de Bruijn graph whose vertices are words \(v\in\{0,1\}^{k-1}\) and whose arcs are words \(av\in\{0,1\}^k\); the arc \(av\) ends at \(v\), and the outgoing arcs from \(v\) are \(v0,v1\). A cyclic de Bruijn sequence is exactly an Euler circuit on these \(2^k\) labeled arcs, counted up to rotation. Each of the two incoming arcs \(0v,1v\) must have a different successor from the two outgoing arcs \(v0,v1\). Thus there is a unique bit \(t_v\in\{0,1\}\) for which the successor of the arc \(av\) is
\[
\pi_t(av)=v(a\oplus t_v),
\]
where \(\oplus\) denotes binary addition modulo \(2\). The function \(\pi_t\) is a permutation of all \(2^k\) arcs; it represents one cyclic de Bruijn sequence **if and only if** it consists of a single cycle containing all arcs. Hence distinct de Bruijn cycles give distinct wiring vectors \(t=(t_v)_v\).

The ordered pair of arcs \(av\) followed by \(vb\) corresponds uniquely to the length-\(k+1\) circular factor \(avb\). Two circuits use the same such factor at \(v\) exactly when their wiring bits at \(v\) agree; then both choices \(a=0,1\) agree. Consequently, if \(d_H\) is the Hamming distance between two wiring vectors,
\[
I(S,T)=2\sum_{v\in\{0,1\}^{k-1}}\mathbf1\{t_v=t'_v\}=2^k-2d_H(t,t').\tag{1}
\]

**2. Four forced common factors.** At the constant vertex \(0^{k-1}\), the arc \(0^k\) is a loop. If the wiring were \(t_{0^{k-1}}=0\), the arc would succeed itself, forming a separate one-arc cycle; this is impossible in an Euler circuit when \(k\ge2\). Therefore \(t_{0^{k-1}}=1\). The same argument for the loop \(1^k\) gives \(t_{1^{k-1}}=1\). Both bits are fixed across all cycles and these are distinct vertices. Their four common length-\(k+1\) factors are \(0^k1\), \(10^k\), \(1^k0\), and \(01^k\). Formula (1) proves \(I(S,T)\ge4\).

**3. Parity obstruction.** Each \(\pi_t\) is a permutation with one \(2^k\)-cycle, so its sign is \((-1)^{2^k-1}=-1\). Replacing a single wiring bit \(t_v\) interchanges the images of precisely the two incoming arcs \(0v\) and \(1v\), and changes the sign of the permutation. Thus for two one-cycle wiring vectors the number \(d_H(t,t')\) of changed bits is even. Formula (1) gives \(I(S,T)\equiv2^k\equiv0\pmod4\) for every \(k\ge2\). In particular, two distinct cycles differ at least at two vertices and so \(I(S,T)\le2^k-4\).

**4. Finite complete order-five computation.** Set \(k=5\), identify a length-five binary word with an integer \(e\) from \(0\) to \(31\) in standard binary order, and a length-four vertex with an integer \(v\) from \(0\) to \(15\). A wiring vector is the sixteen-bit integer \(m\), whose bit at position \(v\) is \(t_v\). Its forced bits are positions \(0\) and \(15\). It therefore has the unique representation
\[
m=1+2^{15}+2u,\qquad 0\le u<2^{14}.
\]
For every such candidate compute the next arc from \(e\) as
\[
v=e\bmod16,\quad a=\lfloor e/16\rfloor,\quad
\pi_m(e)=2v+\bigl(a\oplus((m\mathbin{\mathrm{div}}2^v)\bmod2)\bigr).
\tag{2}
\]
Declare \(m\) valid if the orbit of arc \(0\) under (2) has length exactly \(32\) and returns to \(0\). This criterion is necessary and sufficient, since (2) is a permutation of all \(32\) arcs. Exhausting exactly \(2^{14}=16384\) candidates yields \(2048\) valid masks, agreeing independently with the classical de Bruijn enumeration \(2^{2^{4}-5}=2048\).

For every unordered pair of distinct valid masks compute \(32-2\operatorname{wt}(m\oplus m')\). The seven totals are exactly those displayed above; the bundled file `verify_overlap.py` is complete executable code for this enumeration. It additionally generates every rooted Euler circuit independently by depth-first traversal of distinct arcs and separately forms its set of circular length-six factors. The two routes produce the same \(2048\) circuits and the same seven counts, independently computing overlap from transition-bit Hamming distance and literal six-mer set intersection.

A direct sharpness witness is the pair of cyclic words

`00000111110111001100010110101001`

`00000100111010001101100101011111`.

Their shared length-six factors are exactly `000001`, `011111`, `100000`, and `111110`. Their wiring masks are `0x80af` and `0xff51`, which differ at all fourteen nonconstant vertices.

Finally, attaining \(I=4\) forces two wiring vectors to agree only at the two constant vertices, so the partner of any given mask \(m\) is uniquely determined by \(m\oplus\texttt{0x7ffe}\); it may or may not define an Euler circuit. The exact enumeration finds \(736\) masks admitting this complementary valid mask, giving \(368\) disjoint unordered pairs, as claimed.

## Verification

Run `python3 verify_overlap.py` using Python 3.8 or later. It must print a `PASS` line and the exact histogram \((4,368),(8,27104),(12,254800),(16,710976),(20,758800),(24,305376),(28,38704)\). The two independent enumerations are (i) all \(16384\) admissible local wiring masks, checked for a single permutation orbit, and (ii) all arc-simple rooted Euler circuits produced by DFS. The second calculation measures actual six-mer intersections instead of using formula (1). These finite exhaustive checks certify only the finite \(k=5\) distribution. The universal lower bound and congruence were proved separately in steps 1--3.

## Relationship to prior work

Lin, Ward, Jain, and Skiena (2011) define orthogonal de Bruijn sequences through non-overlap of length-\(k+1\) factors and show that genuine binary orthogonal pairs do not exist. The present statistic quantifies how close binary pairs can be to this forbidden extreme, derives a general mod-four obstruction, and counts every pair at order five. Chen, Sima, and Milenkovic (2025) study generalizations allowing repeated contexts and balanced/fixed-weight de Bruijn sequences; the accessible relevant sections concern bounds on collection sizes, not this pairwise intersection spectrum. Spinsante, Andrenacci, and Gambi (2011) exhaustively analyze order-five binary de Bruijn sequences for **bit-level cyclic cross-correlation** in wireless communications; cross-correlation of aligned symbol sequences is different from the number of shared length-six factor *types*. No implication from their cross-correlation data to the stated spectrum was found in the inspected full text.

## Limitations

The full pair-count spectrum is proved only for the naturally exhaustive \(2048\)-cycle order-five family. The universal statement does **not** assert that four shared factors are attainable for every order. It asserts only the lower bound and mod-four divisibility at all orders. No claim is made for alphabets with more than two symbols, for linear rather than circular factors, or for reverse/complement quotient conventions. A later generalized-orthogonality source was examined from accessible indexed sections rather than its complete article; the possibility of an undiscovered equivalent finite enumeration remains a literature risk. No independent audit or external validation is claimed.

## References

1. Y.-L. Lin, C. B. Ward, B. Jain, and S. Skiena, "Constructing Orthogonal de Bruijn Sequences," *Algorithms and Data Structures*, WADS 2011, LNCS 6844, pp. 595--606, DOI: 10.1007/978-3-642-22300-6_50. (Verified public publication record: 2011-08-12.)
2. S. Spinsante, S. Andrenacci, and E. Gambi, "Binary De Bruijn sequences for DS-CDMA systems: analysis and results," *EURASIP Journal on Wireless Communications and Networking* 2011, article 4, DOI: 10.1186/1687-1499-2011-4. (First-public article date: 2011-06-06.)
3. Y.-P. Chen, J. Sima, and O. Milenkovic, "Generalized Orthogonal de Bruijn and Kautz Sequences," *Entropy* 27 (2025), 366, DOI: 10.3390/e27040366; arXiv:2501.12921.
