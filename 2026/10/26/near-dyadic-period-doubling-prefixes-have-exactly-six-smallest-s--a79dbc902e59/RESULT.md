# Near-dyadic period-doubling prefixes have exactly six smallest string attractors

## Finding
Let \(\varphi(0)=01\) and \(\varphi(1)=00\). Write \(D_n=\varphi^n(0)\) and \(P_n\) for \(D_n\) with its final letter removed. For every integer \(n\ge4\), the **complete** collection of smallest string attractors of \(P_n\) consists of the following six sets of positions, indexed from one:
\[
2^{n-4}\{4,8\},\quad 2^{n-4}\{4,10\},\quad 2^{n-4}\{5,10\},\quad
2^{n-4}\{6,11\},\quad 2^{n-4}\{6,12\},\quad 2^{n-4}\{8,12\}.
\]
Every such attractor has size two; no attractor has size one. This classifies an infinite family of prefixes of lengths \(2^n-1\).

## Assumptions and scope
A *string attractor* of a finite word \(v=v_1\cdots v_N\) is a set \(\Gamma\subseteq\{1,\ldots,N\}\) such that every nonempty distinct factor of \(v\) has at least one occurrence whose position interval meets \(\Gamma\). The morphism is extended to words by concatenation. All indices are one-based; powers of two multiply positions, not symbols. The statement concerns exactly the penultimate-length prefix \(P_n\), not every prefix length. Its underlying fixed point begins \(0100010101000100\cdots\).

## Proof
**1. Recursive decomposition.** Each substituted letter begins in \(0\). Consequently, for every \(n\ge1\),
\[
P_n=\varphi(P_{n-1})0.
\]
Every word \(P_n\) with \(n\ge2\) contains both binary symbols and avoids \(11\), as does the infinite fixed point.

**2. Doubling lifts attractors.** For any finite binary word \(x\) containing both symbols, put \(y=\varphi(x)0\). If \(\Gamma\) is an attractor of \(x\), then \(2\Gamma=\{2i:i\in\Gamma\}\) attracts \(y\). Indeed, each odd-positioned symbol of \(y\) is \(0\), while the symbol at position \(2i\) is the complement of \(x_i\). For any factor \(v\) of \(y\) of length at least two, take an occurrence and read its nonempty consecutive run of even-positioned symbols; the corresponding source letters form a nonempty factor \(u\) of \(x\). Choose an occurrence of \(u\) crossing \(\Gamma\). The same alternating pattern of odd zeroes and complemented even symbols reproduces \(v\), including a possible leading or trailing odd zero, and the reproduced occurrence crosses \(2\Gamma\). A trailing odd zero exists even when this source occurrence ends in the last letter because \(y\) has the appended final \(0\). For the singleton factor \(1\), an attracted occurrence of source letter \(0\) gives a doubled \(1\); for the singleton \(0\), an attracted occurrence of source letter \(1\) gives a doubled \(0\). Hence \(2\Gamma\) attracts \(y\).

**3. Any two-element attractor at level \(n\ge5\) occupies even positions.** In \(P_5\), all six factors in
\[
\mathcal W=\{1,00100,00101,10100,100,001\}
\]
occur. Thus any attractor for a longer \(P_n\) must hit an occurrence of each. For a position \(j\), let its \(\mathcal W\)-signature be the subset of \(\mathcal W\) having an occurrence crossing \(j\). The signature depends only on the centered length-nine window in the infinite period-doubling word, because every word in \(\mathcal W\) has length at most five. The fixed point is partitioned into aligned blocks of length sixteen of the form \(\varphi^4(a)\); every centered nine-window lies in \(\varphi^4(ab)\) for some adjacent \(ab\in\{00,01,10\}\). Enumerating the twenty-four allowable centers in each of these three explicitly constructed length-thirty-two words gives six possible signatures at odd one-based positions and eight at even positions. The full finite enumeration is reproduced by `verify.py`. No union of a possible odd-position signature with **any** possible signature contains all of \(\mathcal W\). Signatures in the finite prefixes can only omit occurrences compared with the infinite word. Therefore no two-position attractor of \(P_n\) contains an odd position.

**4. Even attractors descend.** Let \(x=P_{n-1}\), \(y=P_n\), and suppose \(\{2a,2b\}\) attracts \(y\). Every factor \(u\) of \(x\) of length at least two contains a \(0\), since \(11\) is absent. The factor \(\varphi(u)\) thus has a \(1\) at a relative even position. Every occurrence of \(\varphi(u)\) in \(y\) must begin at an odd position: beginning at an even position would put this \(1\) at an odd (hence zero) absolute position. Therefore every such occurrence is aligned with source substitution blocks and projects to an occurrence of \(u\) in \(x\). Since the two-position attractor crosses some occurrence of \(\varphi(u)\), its halved positions meet the projected occurrence of \(u\). For singleton source factor \(0\), attraction of target factor \(1\) forces a halved position on a source \(0\); for singleton source factor \(1\), attraction of target factor \(00\) forces a halved position on a source \(1\), because an even-indexed zero in the substituted word comes precisely from a source \(1\). Thus \(\{a,b\}\) attracts \(x\).

**5. Base and induction.** Exhaustive direct factor-interval coverage on the fifteen-letter word \(P_4\) gives precisely \(\{4,8\},\{4,10\},\{5,10\},\{6,11\},\{6,12\},\{8,12\}\) among two-position attractors; `verify.py` recreates all distinct factors and all \(\binom{15}{2}\) candidate pairs. At level five and above, Steps 2–4 show a bijection between two-position attractors at adjacent levels, given by doubling. By induction all six and only these six survive for each \(n\ge4\). Finally each \(P_n\) contains both symbols; no singleton position can cross an occurrence of both distinct one-letter factors, so the cardinality two is minimal.

## Verification
Run `python3 verify.py` (Python 3 standard library only). It checks the exact base enumeration, all six test factors in \(P_5\), the six/eight odd/even local-signature types, the signature-union obstruction, and direct full factor coverage against the asserted six attractors for \(4\le n\le8\). The infinite assertion relies on Steps 1–5, not finite sampling.

## Relationship to prior work
Banbara, Bannai, Guo, Köppl, Mieno, and Okamoto (2026) classify smallest attractors for canonical period-doubling words of full dyadic length and explicitly identify complete classification for arbitrary prefixes as a natural further question. The present family removes the final letter from each canonical word, changing the family of minimum attractors: the precise six-pair classification is not a consequence of the two-attractor result for the untruncated words. Schaeffer and Shallit's earlier analysis of automatic-sequence attractors proves that size two is available for period-doubling prefixes and provides a general mechanical recognition method; it does not state the explicit all-\(n\) six-pair classification proved here. The general recognition method can in principle independently verify individual finite instances.

## Limitations
This gives no classification for other prefix lengths, no new asymptotic attractor-size bound, and no independent audit. The finite local-signature enumeration is fully replayable and exhaustive because aligned two-block contexts cover every possible centered length-nine factor. Literature-priority claims are limited to the examined primary sources and searchable records; equivalent unindexed results remain possible.

## References
1. M. Banbara, H. Bannai, J. Guo, D. Köppl, T. Mieno, and M. Okamoto, *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue-Morse Words*, arXiv:2602.16152 (first public version 18 February 2026).
2. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840.
