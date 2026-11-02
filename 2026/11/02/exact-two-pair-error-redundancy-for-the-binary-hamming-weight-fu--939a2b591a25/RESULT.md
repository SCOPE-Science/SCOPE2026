# Exact two-pair-error redundancy for the binary Hamming-weight function

## Finding

The **exact minimum systematic redundancy** for protecting the ordinary Hamming-weight function against two cyclic binary symbol-pair read errors is
\[
r_{\mathrm{wt}}^{(2)}(k)=\begin{cases}4,&k=1,\\3,&k\ge2.\end{cases}
\]
For every message \(u\in\{0,1\}^k\) with \(k\ge2\), write \(w=\mathrm{wt}(u)\) and append
\[
P(w)=(w\bmod 2,\ \lfloor w/2\rfloor\bmod2,\ w\bmod2).
\]
The four labels for residues \(w\bmod4=0,1,2,3\) are respectively 000, 101, 010, 111. Then the cyclic symbol-pair distance between the encoded words is at least five whenever their message weights differ. Redundancy three is optimal even among nonlinear systematic suffix maps.

## Assumptions and scope

The alphabet is binary. The encoded block has length \(n=k+r\), and the systematic encoder has the form \(E(u)=(u,P(u))\), with no restriction that \(P\) be linear or depend only on weight in the converse. For two length-\(n\) binary words \(a,b\), their **cyclic symbol-pair distance** is
\[
d_{\mathrm{pair}}(a,b)=\#\{i\in\{0,\ldots,n-1\}:(a_i,a_{i+1})\ne(b_i,b_{i+1})\},
\]
where indices are modulo \(n\). Distinguishability of distinct function values after up to two erroneous pair-read symbols requires pair distance at least five. The function is the **ordinary Hamming weight of the information word**, not symbol-pair weight or full-message recovery. For \(k=1\) we use blocks of length five, and the same cyclic definition applies.

## Proof

**Pair-shadow lemma.** If a binary difference word has nonempty support \(T\subseteq\{0,\dots,n-1\}\), its pair distance from zero is the number of cyclic edges incident to \(T\), equivalently \(|T\cup(T-1)|\). If \(|T|\ge4\) and \(n\ge5\), then this number is at least five. Indeed, if \(T\) is proper, each connected run has an extra incident edge and the total is at least \(|T|+1\); if \(T\) is the whole cycle, the number is \(n\ge5\).

Fix distinct-weight messages \(u,v\), set \(S=\{i<k:u_i\ne v_i\}\), \(s=|S|\), and \(w=\mathrm{wt}(u)\), \(w'=\mathrm{wt}(v)\). Their message-weight difference has the same parity as \(s\), and its magnitude is at most \(s\). The displayed labels have the elementary properties
\[
P(w)\oplus P(w')\in\{101,111\}\quad\text{if }|w-w'|\text{ is odd},
\]
and
\[
P(w)\oplus P(w')=010\quad\text{if }|w-w'|=2.
\]
(The odd-difference assertion follows from the identical first and third parity bits; the middle bit can flip or not.) We consider all cases.

If \(s\ge4\), the pair-shadow lemma gives distance at least five independently of the suffix. If \(s=3\), then \(|w-w'|\) is one or three, hence the suffix difference is 101 or 111. The three changed message coordinates occupy at least four incident cyclic edges. In addition, the two suffix edges with left endpoints \(k\) and \(k+1\) are incident to changed suffix coordinates but to **no** message coordinate, giving at least six distinct changed pairs.

If \(s=2\), different message weights force \(|w-w'|=2\) and suffix difference 010. The two changed message coordinates occupy at least three pair edges, while the changed central check coordinate (position \(k+1\)) supplies the fresh pair edges with left endpoints \(k\) and \(k+1\), totaling at least five.

If \(s=1\), different message weights force \(|w-w'|=1\), and suffix difference is 101 or 111. Either suffix difference changes the four cyclic pairs whose left endpoints are \(k-1,k,k+1,k+2\). Because \(k\ge2\), the changed message coordinate contributes at least one edge outside those four (the pair with left endpoint \(0\) when the coordinate is \(0\), or an edge with left endpoint at most \(k-2\) otherwise). Thus distance is at least five.

Every distinct-weight pair has been covered, proving that three check bits suffice. Equality of the minimum pair distance is attained by zero message and the message with a one in its first coordinate: the suffix difference is 101 and exactly one message edge lies outside its four suffix edges.

**Sharp converse.** For any systematic encoder of redundancy \(r\le2\), compare the all-zero information word with the word whose only one is in the *last* information position. Their codewords can differ only in that last message coordinate and the following \(r\) check coordinates, a cyclic interval of length at most \(r+1\). At most \(r+2\le4\) consecutive pair edges meet this interval, contradicting the required distance five. Thus \(r\ge3\) for \(k\ge2\).

When \(k=1\), two messages have different weights, so their two encoded words must have pair distance at least five. Since the pair distance cannot exceed blocklength \(1+r\), necessarily \(r\ge4\). Sending 0 as 00000 and 1 as 11111 attains pair distance five, proving \(r=4\).

## Verification

The standalone script `verify.py` independently constructs the labels and computes cyclic pair distance directly for **all** unordered message pairs of unequal ordinary Hamming weight at every \(2\le k\le11\). It exhaustively checks 2,318,009 such pairs, finding exact minimum distance five for each blocklength. Additional exhaustive tests inspect all possible suffix assignments for the one-coordinate converse configurations for \(k\le39\), \(r\le2\). These finite tests corroborate the explicit infinite-length proof but do not substitute for it. The script uses only the Python standard library and prints a deterministic success marker.

## Relationship to prior work

The September 2026 paper of Singh and Singh motivates quantitative protection in the symbol-pair metric, including functions and data protection, but the present code **does not** claim data protection of the full message. The inspected accessible text of Singh, Singh and Yaakobi's March 2025 paper studies redundancy for *symbol-pair weight* (number of nonzero overlapping reads), which is not the ordinary Hamming-weight function studied here. Ge and coauthors' February 2025 work addresses ordinary Hamming weight in the Hamming metric rather than this cyclic pair metric. Xia, Liu and Chen's earlier paper develops general symbol-pair function-correcting bounds and specialized pair-weight functions. The proposed exact value and four-periodic parity-suffix construction were not identified in the material actually inspected; no inference of novelty is based merely on different paper titles.

The full text of the September 2026 paper and the original Xia–Liu–Chen paper could not be obtained. Their accessible abstracts **do not establish noncoverage of their full texts**. An equivalent construction may be implicit in generalized symbol-pair function-correcting constructions. No absolute priority is claimed.

## Limitations

The claim concerns systematic *function* correction at two cyclic pair-read errors, not simultaneous full-message recovery, larger error budgets, arbitrary alphabets, or noncyclic pair sampling. An all-parameter proof is supplied; computational tests cover finitely many lengths. The literature comparison is qualified by incomplete access to two highly relevant sources; an independent novelty audit has not been performed.

## References

1. A. Singh and A. K. Singh, *Data Protection in Function-Correcting Symbol-Pair Codes: Redundancy Bounds and Protection Profiles*, arXiv:2609.10989, first submitted 2026-09-10. https://arxiv.org/abs/2609.10989
2. A. Singh, A. K. Singh and E. Yaakobi, *Function-Correcting Codes for b-Symbol Read Channels*, arXiv:2503.12894, first submitted 2025-03-17. https://arxiv.org/abs/2503.12894
3. G. Ge, Z. Xu, X. Zhang and Y. Zhang, *Optimal redundancy of function-correcting codes*, arXiv:2502.16983, first submitted 2025-02-24. https://arxiv.org/abs/2502.16983
4. Q. Xia, H. Liu and B. Chen, *Function-Correcting Codes for Symbol-Pair Read Channels*, arXiv:2312.16271, first submitted 2023-12-26. https://arxiv.org/abs/2312.16271
