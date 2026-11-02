# Universal resolving thresholds and extremal bisectors in products of complete graphs

## Finding
Let \(G=\square_{i=1}^{d}K_{q_i}\) with \(d\ge1\) and integers \(q_i\ge2\). Put \(N=\prod_i q_i\), \(Q=\max_iq_i\), and let \(b,t,f\) denote the numbers of factors of orders \(2,3,4\), respectively. A landmark set resolves \(G\) when every two distinct vertices have different distance vectors to the landmarks. Let \(\operatorname{th}(G)\) be the least cardinality at which **every** landmark subset resolves \(G\). Then \(\operatorname{th}(G)=M+1\), where
\[
M=\begin{cases}
N(Q-2)/Q,&Q\ge5,\\
N/2,&Q=4,\\
N/2,&Q=3\text{ and }b\ge2,\\
N/3,&Q=3\text{ and }b\le1,\\
N/2,&Q=2\text{ and }d\ge2,\\
0,&Q=2\text{ and }d=1.
\end{cases}
\]
Furthermore, the complete number \(A(G)\) of **maximum-cardinality nonresolving landmark sets**, with distinct labeled sets counted separately, is
\[
A(G)=\begin{cases}
\#\{i:q_i=Q\}\binom Q2,&Q\ge5,\\
6f+2\binom b2,&Q=4,\\
2\binom b2,&Q=3\text{ and }b\ge2,\\
3t+6\binom t2+6bt,&Q=3\text{ and }b\le1,\\
2\binom b2,&Q=2\text{ and }d\ge2,\\
1,&Q=2\text{ and }d=1.
\end{cases}
\]
These sets are exactly the eligible families in the following structural classification. (A) For a factor of order at least four, remove two distinct alphabet symbols from one coordinate: the landmark set consists of every word avoiding those symbols in that coordinate. This family is eligible only on factors of order \(Q\) when \(Q\ge5\), and on order-four factors when \(Q=4\). (B) For two binary coordinates, retain words satisfying one of the two binary parity equations on those coordinates; eligible exactly when \(M=N/2\). (C) For one ternary coordinate, retain one chosen symbol in that coordinate. (D) For two ternary coordinates, retain pairs satisfying \(w_j=\pi(w_i)\), for one of the six permutations \(\pi\) of the ternary alphabet. (E) For one binary coordinate \(i\) and one ternary coordinate \(j\), retain \((w_i,w_j)\in\{(0,v),(1,u)\}\) with distinct ternary symbols \(u,v\). Families (C)--(E) are eligible exactly when \(Q=3\) and \(b\le1\). In the exceptional single-factor graph \(K_2\), the unique largest nonresolving set is empty.

For the homogeneous Hamming graph \(H(d,q)=K_q^{\square d}\), the theorem implies the three-way transition
\[
\operatorname{th}(H(d,q))=\begin{cases}
1,&q=2,\ d=1,\\
2^{d-1}+1,&q=2,\ d\ge2,\\
3^{d-1}+1,&q=3,\\
(q-2)q^{d-1}+1,&q\ge4.
\end{cases}
\]
The corresponding numbers of maximum nonresolving sets are \(d(d-1)\) for binary \(d\ge2\), \(3d^2\) for ternary graphs, and \(d\binom q2\) for \(q\ge4\).

## Assumptions and scope
All graphs are finite, simple, undirected Cartesian products of complete graphs; each coordinate alphabet has exactly \(q_i\) labeled symbols. Product distance is Hamming distance, the number of differing coordinates. The threshold concerns **arbitrary** landmark subsets of a specified size, not the minimum size of a carefully chosen resolving set. An equidistance bisector is \(B(x,y)=\{w:d(w,x)=d(w,y)\}\) for distinct vertices \(x,y\).

## Proof
**1. Reduction to largest bisectors.** A set \(S\) is nonresolving if and only if for some distinct vertices \(x,y\) it satisfies \(S\subseteq B(x,y)\). Consequently, with \(M=\max_{x\ne y}|B(x,y)|\), every set of size \(M+1\) resolves, and some set of size \(M\) does not. A nonresolving set of size \(M\) must be precisely one largest bisector. This also justifies counting distinct largest bisectors rather than arbitrary landmark subsets.

**2. Independent coordinate law.** For fixed \(x\ne y\), suppose their differing-coordinate set is \(I\). For a uniform random word \(W\), define \(X_i=d(W_i,x_i)-d(W_i,y_i)\) on \(I\). Each independent \(X_i\) takes \(-1,+1,0\) with probabilities \(1/q_i,1/q_i,(q_i-2)/q_i\), respectively. Thus \(|B(x,y)|/N=\Pr(\sum_{i\in I}X_i=0)\).

**3. Sharp coordinate-support bounds.** If some \(q_i\ge4\) occurs in \(I\), the mass at zero, \((q_i-2)/q_i\), is the *unique* maximum atom of \(X_i\). Conditioning on the independent sum of other coordinate contributions gives an upper bound \((q_i-2)/q_i\), with equality only when \(I=\{i\}\): with any other differing coordinate, the other sum is nonconstant, so it is nonzero with positive probability and strictly reduces the average. If all coordinates of \(I\) are binary, its size \(k\) gives zero center mass when \(k\) is odd, and \(2^{-k}\binom{k}{k/2}\) when \(k\) is even. This equals \(1/2\) exactly when \(k=2\), and is strictly less for all even \(k\ge4\), since the ratio of consecutive even-length central masses is \((k+1)/(k+2)<1\). A single binary coordinate has zero center mass.

If \(I\) contains a ternary coordinate and no coordinate of order at least four, conditioning on one ternary contribution gives center mass at most \(1/3\), since each of its three atoms has mass \(1/3\). Equality holds if and only if the sum of the remaining contributions is always in \(\{-1,0,1\}\). When there are no other differing coordinates or exactly one further binary or ternary differing coordinate, this is true. If at least two further differing coordinates occur, the remaining independent sum takes an absolute value at least \(2\) with positive probability, so the inequality is strict. Comparison of these three classes proves all six displayed values of \(M\) and shows that the only maximizing supports are: a single largest nonbinary coordinate of size at least five; a single quaternary or a binary pair for \(Q=4\); a binary pair for \(Q=3,b\ge2\); one ternary coordinate or a pair of ternary/ternary or binary/ternary coordinates for \(Q=3,b\le1\); a binary pair for \(Q=2,d\ge2\); and the sole coordinate for \(K_2\), whose bisector is empty.

**4. Exact bisectors and nonduplication.** On one differing coordinate of order \(q\ge3\), equidistant words avoid both endpoint symbols, giving (A) or (C). On two binary coordinates, equidistance is a parity equation, giving the two alternatives in (B). On two ternary coordinates, equidistance consists of the two cross-corners of the selected endpoint rectangle and the pair of unused symbols, hence is the graph of a permutation of the two ternary alphabets; conversely, each of the six permutations arises. On one binary and one ternary coordinate, equidistance is exactly a two-cell opposite-corner matching using two distinct ternary symbols, giving six alternatives in (E). All unspecified coordinates are free. Each family has the displayed \(M\) vertices. A bisector's set of essential coordinates (those on which its membership condition depends) is intrinsic, and within a fixed essential-coordinate set the forbidden pairs, parity values, permutations, and distinct-symbol matchings are all different. Therefore, no labeled family is counted twice. Counting the eligible supports and patterns gives the stated formula for \(A(G)\).

## Verification
The standalone standard-library program `verify_bisectors.py` independently enumerates vertices and unordered vertex pairs, computes Hamming distances directly, constructs each equidistance bisector as a bit mask, and compares the largest size and number of distinct largest masks to the formulas. It tests all products of one factor of size \(2\) through \(7\), all pairs of factor sizes \(2\) through \(6\), and 22 mixed products of three to five factors. On the tested instances it prints `VERIFY_OK`. This is finite checking of boundary cases and independent implementation, not the proof for unbounded dimensions.

## Relationship to prior work
Korivand, Khashyarmanesh, and Tavakoli (2022) introduced the metric-dimension threshold and studied paths, cycles, Petersen graphs, and general extreme-threshold cases. Their general bisector lower bound does not give the closed formulas or maximum-landmark obstruction classification here. Laird, Tillquist, Becker, and Lladser (first public preprint 2019) characterize resolvability of arbitrary Hamming landmark sets using a constrained linear system, but do not state these universal worst-placement thresholds or enumerate extremal failures. Gispert-Fernández, Rodríguez-Velázquez, and Yero (2026) determine equidistant dimensions of some Cartesian products; their condition existentially seeks landmarks of *equal* distance for pairs outside a set, and is not the universal *unequal*-distance condition treated here. The latter paper is not used to determine the cohort date. Exact prior-art equivalence is not asserted beyond the sources inspected.

## Limitations
The theorem concerns only arbitrary Cartesian products of complete graphs. It gives the number of largest nonresolving sets, not the complete polynomial counting nonresolving sets of every cardinality, nor an independent determination of the minimum metric dimension. The proof is self-contained; published-priority assessment remains provisional pending independent literature review. No independent mathematical audit has been performed.

## References
1. Laird, L.; Tillquist, R. C.; Becker, S.; Lladser, M. E. *Resolvability of Hamming Graphs*, arXiv:1907.05974 (first posted 2019-07-12); SIAM Journal on Discrete Mathematics 34 (2020), 2063–2081, DOI: 10.1137/19M1274511.
2. Korivand, M.; Khashyarmanesh, K.; Tavakoli, M. *Metric Dimension Threshold of Graphs*, Journal of Mathematics (2022), article 1838719, DOI: 10.1155/2022/1838719 (first published 2022-09-14).
3. Gispert-Fernández, A.; Rodríguez-Velázquez, J. A.; Yero, I. G. *Equidistant dimension of Cartesian product graphs*, Bulletin of the Malaysian Mathematical Sciences Society 49 (2026), article 101, DOI: 10.1007/s40840-026-02088-4 (different graph invariant).
