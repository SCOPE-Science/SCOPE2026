# Exact greedy string attractor of the period-doubling word
## Finding
Let \(p\) be the one-sided period-doubling word, the fixed point beginning with \(1\) of the morphism \(\mu(1)=10\) and \(\mu(0)=11\). Under the greedy string-attractor rule of Schaeffer and Shallit, the selected positions are exactly
\[
G=\{2^k-1:k\ge0\}.
\]
Hence the greedy attractor restricted to a prefix of length \(n\ge1\) has cardinality
\[
|G\cap\{0,\ldots,n-1\}|=\lfloor\log_2 n\rfloor+1.
\]
In contrast, the minimum string-attractor size of every period-doubling prefix of length at least \(2\) is \(2\). Thus the greedy rule is logarithmically larger than optimum on this canonical automatic word.

## Assumptions and scope
Positions are numbered from \(0\). A set \(S\) is a string attractor for a finite word if every distinct factor has an occurrence whose interval meets \(S\). The greedy rule starts with the empty set and repeatedly adds the smallest endpoint \(j\) for which the current set ceases to attract the prefix ending at \(j\).

Write \(P_k=\mu^k(1)\) and \(Q_k=\mu^k(0)\), both of length \(2^k\). Let
\[
S_k=\{2^j-1:0\le j\le k\}.
\]
The claim concerns this exact greedy rule and this standard period-doubling fixed point.

## Proof
The morphism gives
\[
P_{k+1}=P_kQ_k,\qquad Q_{k+1}=P_kP_k.
\]
Induction also gives that \(P_k\) and \(Q_k\) agree in every position except the final one. Indeed the assertion is true for \(P_0=1\) and \(Q_0=0\); if it holds at level \(k\), then \(P_{k+1}=P_kQ_k\) and \(Q_{k+1}=P_kP_k\) differ only in the last symbol of their second blocks.

We prove by induction on \(k\) that for every
\[
2^k\le n\le2^{k+1}-1,
\]
the set \(S_k\) attracts the prefix of \(p\) of length \(n\). The case \(k=0\) is immediate.

Let \(L=2^k\). First, \(S_k\) attracts \(P_k\). Its prefix of length \(L-1\) lies in the preceding induction interval and is attracted by \(S_{k-1}\). Therefore any factor of \(P_k\) having an occurrence that avoids the final position \(L-1\) has an occurrence crossing \(S_{k-1}\). Every remaining factor has every occurrence crossing \(L-1\), which belongs to \(S_k\).

Now take a prefix of length \(L+r\), where \(0\le r\le L-1\). Since the first \(r\) symbols of \(Q_k\) equal the first \(r\) symbols of \(P_k\), this prefix is
\[
P_kP_k[0:r].
\]
Every factor occurrence is either contained in the first copy of \(P_k\), crosses the boundary between the two copies, or lies wholly in the copied prefix. In the first case it has an occurrence crossing \(S_k\); in the second it crosses the boundary position \(L-1\in S_k\); in the third, shifting the occurrence left by \(L\) gives an identical occurrence in the first copy. Hence \(S_k\) attracts every prefix through length \(2L-1\).

It remains to show failure exactly at length \(2L\). The prefix is \(P_kQ_k\). The suffix \(Q_k\), of length \(L\), occurs there only once. It is not the window starting at \(0\), because \(P_k\ne Q_k\). A window starting at \(j\) with \(1\le j\le L-1\) ends before the unique flipped final symbol of \(Q_k\), so it is the cyclic rotation \(P_k[j:L]P_k[0:j]\). Such a rotation has the same number of \(1\)'s as \(P_k\), whereas \(Q_k\) differs from \(P_k\) in exactly one bit and therefore has a different number of \(1\)'s. Thus no such window equals \(Q_k\). The unique occurrence is the suffix beginning at \(L\), whose interval avoids \(S_k\) because \(\max S_k=L-1\).

Therefore \(S_k\) remains an attractor up to length \(2^{k+1}-1\) and first fails at length \(2^{k+1}\). The greedy rule must add its new endpoint \(2^{k+1}-1\). Starting from \(0\), this proves that the complete greedy set is exactly \(\{2^k-1:k\ge0\}\). Counting those positions below \(n\) gives \(\lfloor\log_2 n\rfloor+1\).

## Verification
The standalone verifier reconstructs the period-doubling fixed point directly from the morphism. For every prefix length through \(128\), it enumerates every distinct factor and the union of positions covered by its occurrences, executes the greedy rule from the definition, and obtains exactly the positions \(0,1,3,7,15,31,63,127\).

Independently, for thirteen dyadic levels it checks that \(P_k\) and \(Q_k\) agree except in their last bit and that \(Q_k\) has exactly one occurrence in \(P_kQ_k\), namely the suffix occurrence used in the proof. These computations are finite checks supporting the proof; the all-length theorem follows from the induction above.

## Relationship to prior work
Schaeffer and Shallit introduced the greedy string-attractor rule for infinite words and proved a general logarithmic upper bound when the appearance constant is finite. In the same work they proved that period-doubling prefixes have minimum attractor size \(2\) from length \(2\) onward and gave explicit minimum attractors. Their greedy section does not specialize the greedy process to the period-doubling word.

Later work completely characterizes all smallest attractors of dyadic period-doubling words. That result concerns minimum-cardinality attractors chosen separately for each fixed word; it does not determine the cumulative nested set produced by the greedy rule. The theorem here supplies that missing exact greedy profile and shows that the general logarithmic bound can be attained in order even while the optimum profile is constant.

Targeted searches under greedy-attractor, period-doubling, minimal-novel-factor, exact-position, and powers-of-two formulations did not reveal a prior statement of this exact set. This is evidence of non-coverage, not a proof that no unindexed observation exists.

## Limitations
The conclusion is specific to the stated period-doubling morphism and the Schaeffer--Shallit greedy endpoint rule. It does not claim analogous formulas for other automatic sequences or for alternative online attractor heuristics. The originality assessment retains residual risk from unindexed notes or equivalent formulations of this elementary morphic consequence.

## References
1. L. Schaeffer and J. Shallit, “String Attractors for Automatic Sequences,” arXiv:2012.06840, first public version 2020-12-12.
2. J. Cassaigne, G. Fici, M. Sciortino, and L. Q. Zamboni, “New string attractor-based complexities for infinite words,” Journal of Combinatorial Theory, Series A 199 (2024), 105936, DOI 10.1016/j.jcta.2024.105936.
3. M. Banbara, K. Iseri, M. Inoue, S. Kawakami, S. Inenaga, and H. Bannai, “The Smallest String Attractors of Fibonacci and Period-Doubling Words,” arXiv:2602.16152.
