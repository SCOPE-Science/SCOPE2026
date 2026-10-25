# Sharp zero-only cyclic equalization cost for binary words of Hamming weight two

## Finding

For each integer \(n\ge 3\), consider two length-\(n\) binary words \(u,v\), each containing exactly two symbols equal to \(1\). A simultaneous zero insertion places the same nonnegative number of zeroes into each of the \(n+1\) corresponding gaps of both words. Let \(\kappa_0(u,v)\) be the least total number of inserted zeroes for which the two expanded words are cyclic shifts of each other.

Write the one-positions (numbered from \(0\)) as \(a<b\) in \(u\) and \(c<d\) in \(v\). Define the insertion-gap intervals
\[
I=\{a+1,\ldots,b\},\qquad J=\{c+1,\ldots,d\},\qquad r=b-a,\quad s=d-c.
\]
Then the **exact optimal insertion cost** is
\[
\kappa_0(u,v)=
\begin{cases}
|n-r-s|,&I\subsetneq J\text{ or }J\subsetneq I,\\
|r-s|,&I\cap J=\varnothing,\\
\min\{|r-s|,|n-r-s|\},&\text{otherwise}.
\end{cases}
\]
In particular,
\[
\max_{\substack{u,v\in\{0,1\}^{n}\\ |u|_1=|v|_1=2}}\kappa_0(u,v)=n-3.
\]
For every \(n\ge4\), exactly \(4n\) **ordered pairs** of such words attain this maximum. They fall into three disjoint geometric types: strictly nested intervals of lengths \(1,2\), strictly nested intervals of lengths \(n-2,n-1\), and disjoint intervals of lengths \(1,n-2\). The numbers of ordered pairs of these types are, respectively, \(4(n-2)\), \(4\), and \(4\).

The pair \(u=11 0^{n-2}\) and \(v=101 0^{n-3}\) realizes the maximum for every \(n\ge3\). At \(n=3\), all nine ordered pairs are already cyclically equivalent and have cost zero. At \(n=2\), there is just the word \(11\) and the cost is zero.

## Assumptions and scope

The alphabet is \(\{0,1\}\), each word has exactly two ones, and only zeroes may be inserted. An insertion operation is specified by an integer vector \(z=(z_0,\ldots,z_n)\in\mathbb Z_{\ge0}^{n+1}\); the same \(z_i\) zeroes are placed immediately before the original position \(i\) in each word for \(0\le i<n\), with \(z_n\) appended after the last symbol. The optimization objective is \(\sum_{i=0}^{n}z_i\). Cyclic equivalence means equality after a rotation, without reversing either word. Repeated simultaneous insertions combine into one such gap vector, so this representation loses no cases. The two words are ordered when counting maximizers.

## Proof

**1. Two circular arc lengths.** Let \(K=\sum_{i=0}^{n}z_i\) and \(N=n+K\). The clockwise distance between the two ones in the expanded \(u\), in their inherited linear order, is
\[
R=r+\sum_{i\in I}z_i.
\]
The corresponding distance for \(v\) is
\[
S=s+\sum_{i\in J}z_i.
\]
A length-\(N\) binary circular word containing two ones is specified, up to rotation, by the unordered pair of clockwise arc lengths \(\{R,N-R\}\). Hence the expanded words are cyclic shifts exactly when
\[
R=S\quad\text{or}\quad R+S=N. \tag{1}
\]
This equivalence holds even when the two ones are adjacent or the circular arcs have equal lengths.

**2. Minimization of the two alternatives.** The first alternative in (1) is
\[
r-s+\sum_{i\in I\setminus J}z_i-\sum_{i\in J\setminus I}z_i=0. \tag{2}
\]
If \(r=s\), zero insertions solve (2). Otherwise, (2) is possible precisely when a gap exists in the part of the *shorter* interval outside the longer interval, and then its minimum insertion cost is \(|r-s|\): place that many zeroes in one such gap. Indeed, every inserted zero changes the left side of (2) by at most one in absolute value.

The second alternative in (1) is
\[
\sum_{i\in I\cap J}z_i-\sum_{i\notin I\cup J}z_i=n-r-s. \tag{3}
\]
If \(n-r-s>0\), equation (3) can be solved exactly when \(I\cap J\ne\varnothing\), with minimum cost \(n-r-s\). If \(n-r-s<0\), the outer gap \(0\notin I\cup J\) solves it with minimum cost \(r+s-n\); the zero case needs no insertions. Thus its feasible minimum is \(|n-r-s|\). A coefficient in (2) or (3) has absolute value at most one, so no smaller total cost can solve that equation.

When \(I\) is a strict subset of \(J\) or conversely, their lengths differ, (2) is impossible, whereas (3) is feasible. When the intervals are disjoint, (2) is feasible and \(r+s\le n-1\), so (3) is impossible. In every remaining case, the intervals are equal or overlap without strict containment: (2) is feasible (trivially when \(r=s\)), and (3) is feasible. Taking the smaller feasible cost proves the displayed exact formula.

**3. Sharp worst-case bound.** If one interval is strictly contained in the other, its lengths satisfy \(3\le r+s\le2n-3\), so \(|n-r-s|\le n-3\). If the intervals are identical, the cost is zero. In every other case, neither interval has length \(n-1\), since the unique interval of that length contains every other interval; hence \(1\le r,s\le n-2\), and the always-feasible equality alternative gives \(\kappa_0(u,v)\le |r-s|\le n-3\). For the explicit witness \(u=11 0^{n-2}\), \(v=1010^{n-3}\), the intervals have lengths \(1,2\) with the first strictly contained in the second. Its exact cost is \(n-3\).

**4. Classification and count of maximizers.** Suppose \(n\ge4\). In the strict-containment case, equality \(|n-r-s|=n-3\) forces \(r+s=3\) or \(r+s=2n-3\). The respective length pairs, unordered, are exactly \(\{1,2\}\) and \(\{n-2,n-1\}\). There are \(n-2\) intervals of length two, each containing two singleton intervals, and either member may belong to either word: \(4(n-2)\) ordered pairs. The full interval of length \(n-1\) contains exactly two intervals of length \(n-2\), giving four additional ordered pairs.

Outside strict containment, a maximal cost needs \(|r-s|=n-3\), because the cost is at most \(|r-s|\). This forces lengths \(1,n-2\). To avoid strict containment, the singleton interval must be the unique interior gap outside the length-\(n-2\) interval. There are exactly two choices for the latter and two possible orders of the words, yielding four pairs. These three types are disjoint and exhaust the maximizers, for a total of \(4(n-2)+4+4=4n\).

## Verification

The standalone standard-library script `verify.py` implements the exact formula and, independently, constructs literal zero-padded words and tests their rotations for every insertion vector of lower cost through \(n=8\). It checks every ordered pair of weight-two words at lengths \(3\) to \(8\), verifies the formula-derived histograms through \(n=12\), and verifies the sharp witness through \(n=100\). Run `python3 verify.py`; the last line is `VERIFY_OK`. The exact histogram at \(n=8\) has costs \(0,1,2,3,4,5\) in quantities \(208,256,144,96,48,32\), respectively. The proof above, not these finite checks, establishes the theorem for every \(n\).

## Relationship to prior work

Shinagawa and Nuida (arXiv:2507.04916, first posted 7 July 2025) introduced cyclic equalizability and characterized the unrestricted binary existence condition in terms of Hamming weight. Thongjarast, Pasiphol, and Ruangwises (arXiv:2604.19504v1, 21 April 2026) extended the characterization to arbitrary alphabets and explicitly identified optimal insertion length as an open problem (Section 7). Thongjarast (arXiv:2607.18452v1, 20 July 2026) proved that binary words of equal weight can be equalized by inserting only zeroes, gave a polynomial-length construction, and asked for exact nonasymptotic bounds (Section 10.1). These general existence and construction results do not specify the exact weight-two insertion cost, classify its maximizers, or count them. No claim of general optimality outside weight two is made here.

## Limitations

The sharp result applies only to two binary inputs containing two ones each and to insertions restricted to zeroes. The minimum can be smaller if ones are also permitted to be inserted. The result does not improve the published all-Hamming-weight upper bound, nor settle the conjectural growth of the unrestricted-weight extremal insertion length. Publication priority may be affected by an equivalent unindexed calculation or unexamined portions of earlier foundational work. Independent scientific validation has not been carried out.

## References

1. K. Shinagawa and K. Nuida, *Cyclic Equalizability of Words and Its Application to Card-Based Cryptography*, arXiv:2507.04916 (first public version 7 July 2025).
2. S. Thongjarast, S. Pasiphol, and S. Ruangwises, *Cyclic Equalizability Characterized by Parikh Vectors*, arXiv:2604.19504v1 (21 April 2026), particularly Section 7.
3. S. Thongjarast, *0-Cyclic Equalizability of Binary Words Characterized by Hamming Weight*, arXiv:2607.18452v1 (20 July 2026), particularly Section 10.1 and Appendix 0.A.
