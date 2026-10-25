# Commuting idempotents of Catalan monoids: a gap criterion, centralizer transfer, and exact density

## Finding
For every integer \(n\ge1\), let \(\mathcal C_n\) be the monoid of order-preserving, order-decreasing maps of the finite chain \([n]=\{1,\ldots,n\}\), with composition. Its idempotents are indexed by subsets \(S\subseteq[n]\) containing \(1\):
\[
e_S(x)=\max\{s\in S:s\le x\}.
\]
Given two such subsets \(S,T\), their idempotents commute **if and only if** every component of \([n]\setminus(S\cap T)\) contains elements of at most one of the two exclusive sets \(S\setminus T\) and \(T\setminus S\). Components here are the intervals between successive common fixed points, including the terminal interval; the initial interval is empty because \(1\in S\cap T\).

Write \(a_n\) for the number of *ordered* commuting idempotent pairs. Then
\[
a_1=1,\qquad a_2=4,\qquad a_n=4a_{n-1}-2a_{n-2}\quad(n\ge3),
\]
\[
\sum_{n\ge1}a_n z^{n-1}=\frac{1}{1-4z+2z^2},\qquad
 a_n=\frac{(2+\sqrt2)^n-(2-\sqrt2)^n}{2\sqrt2}.
\]
There are exactly \(2^{n-1}\) idempotents, so two uniform independent idempotents commute with probability
\[
p_n=\frac{a_n}{4^{n-1}}\sim \sqrt2\left(\frac{2+\sqrt2}{4}\right)^n.
\]
The individual commuting-idempotent centralizer size is also computable directly from the fixed-point set: with row vector \(v=(1,0,0)\), column \(w=(1,1,1)^{\mathsf T}\), and
\[
M_0=\begin{pmatrix}1&0&1\\0&1&0\\0&0&2\end{pmatrix},\qquad
M_1=\begin{pmatrix}1&1&0\\1&1&0\\1&0&0\end{pmatrix},
\]
we have, for every \(S\ni1\),
\[
|\{e_T:e_Te_S=e_Se_T\}|=v\left(\prod_{i=2}^{n}M_{\mathbf1_{i\in S}}\right)w,
\]
where the product is ordered by increasing \(i\); the empty product is the identity. The formula gives an exact individual centralizer profile, not merely the aggregate count.

## Assumptions and scope
All quantifiers range over positive integers \(n\) and the specified subsets \(S,T\). Maps act on the left by the usual function composition \((fg)(x)=f(g(x))\). This is the regressive realization of the classical Catalan monoid; reversing the chain conjugates it to the extensive realization. Counts include the identity and all other idempotents, with ordered pairs and no exclusions. The term centralizer above is restricted to **idempotent elements** commuting with \(e_S\), not the full centralizer in \(\mathcal C_n\).

## Proof
**Idempotent normal form.** If \(f\) is idempotent, its image equals its fixed-point set \(S\). Since \(f\) is regressive and nondecreasing, \(1\in S\). If \(s\) is the greatest fixed point not exceeding \(x\), then \(s=f(s)\le f(x)\le x\), and the element \(f(x)\) is itself fixed, so maximality forces \(f(x)=s\). Conversely every predecessor projection \(e_S\) is regressive, nondecreasing and idempotent. Thus there are \(2^{n-1}\) idempotents.

**Pair criterion.** For any \(x\) set \(i=e_S(x)\) and \(j=e_T(x)\). If \(i<j\), then \(e_S(j)=i\), whereas \(e_T(i)\le i\), with equality exactly when \(i\in T\). Thus \(e_S(e_T(x))=e_T(e_S(x))\) is equivalent to \(i\in T\). If \(j<i\), the symmetric criterion is \(j\in S\). When \(i=j\) both composites equal \(i\). Therefore commutation fails precisely when, for some \(x\), the last \(S\)-fixed and last \(T\)-fixed points at most \(x\) are distinct and the smaller is exclusive to its own set.

If a common-fixed-point gap contains an \(S\)-only point and a \(T\)-only point, take \(x\) at the later of one such pair, choosing the earliest transition between exclusive colors within the gap. Then the two last fixed points are exclusive and distinct; commutation fails. Conversely, if no gap contains both exclusive colors, the latest fixed points of \(S\) and \(T\) before any \(x\) are either equal or the smaller is a common fixed point, satisfying the preceding criterion. This proves the equivalence.

**Transfer and aggregate enumeration.** Scan indices \(2,\ldots,n\), treating the status of each index as \(0\) (neither fixed), \(A\) (only fixed by \(S\)), \(B\) (only fixed by \(T\)), or \(C\) (fixed by both). Maintain states \(0,A,B\), recording which exclusive color, if any, has occurred since the last \(C\). A \(C\) resets to state \(0\); a \(0\) leaves the state unchanged; an exclusive color is forbidden only when the other color already occurred in the gap. The transition matrix for arbitrary simultaneous choices is
\[
M=M_0+M_1=\begin{pmatrix}2&1&1\\1&2&0\\1&0&2\end{pmatrix}.
\]
Consequently \(a_n=vM^{n-1}w\). The symmetry of the last two coordinates confines \(M\) on the reachable and observable subspace to \(\left(\begin{smallmatrix}2&2\\1&2\end{smallmatrix}\right)\), with eigenvalues \(2\pm\sqrt2\). This yields \(a_1=1\), \(a_2=4\), the displayed recurrence, generating function and closed form. For fixed \(S\), splitting the transitions according to whether \(i\in S\) gives \(M_0\) or \(M_1\), hence the individual centralizer expression.

**Density.** There are \(2^{n-1}\) choices independently for each of the two idempotents. Dividing the explicit \(a_n\) by \(4^{n-1}\) gives the probability, and the smaller root \(2-\sqrt2\) is exponentially negligible, proving the asymptotic.

## Verification
Run `python3 verify.py` using Python 3 and its standard library. The checker constructs predecessor projections directly, exhaustively enumerates ordered idempotent pairs for \(1\le n\le10\), tests commutation by independent map composition, tests the gap characterization, and compares with both transfer formulas and the recurrence. There are \(\sum_{n=1}^{10}4^{n-1}=349525\) ordered pairs across this range. These finite tests do not prove the all-\(n\) statements; their proofs are above.

## Relationship to prior work
Pantazi and Spircu (2016/2017) identify and study idempotents and structural relations among consecutive classical Catalan monoids. The normal form and the number \(2^{n-1}\) of idempotents are therefore background, not claimed as new. Sapir and Volkov (first public 2022) study finite-basis properties of classical Catalan monoids, distinguishing them from injection monoids with commuting idempotents. Their statements about commuting idempotents in *other* monoids do not give a pair count for Catalan monoids. The result here instead characterizes exactly which pairs of classical Catalan-monoid idempotents commute, counts such ordered pairs uniformly in \(n\), and gives a fixed-set-resolved centralizer transfer. The numerical sequence and the recurrence are already listed as OEIS A007070 (with its index shifted by one). Their abstract discovery is not claimed as new; the claimed contribution is the specific semigroup-theoretic interpretation, exact gap equivalence and individual commuting-idempotent centralizer profile. Related work on commuting arbitrary idempotent transformations without order restrictions does not imply this Catalan subfamily enumeration from its rank-only information.

## Limitations
This theorem concerns only idempotent elements of the regressive or, equivalently by chain reversal, extensive Catalan monoid, not arbitrary commuting elements or complete semigroup element-centralizers. Neither finite brute force nor literature searches can establish historical uniqueness. An equivalent semigroup-theoretic interpretation or structural theorem in less readily indexed literature is a residual originality risk.

## References
1. O. B. Sapir and M. V. Volkov, *Catalan monoids inherently nonfinitely based relative to finite \(\mathcal R\)-trivial semigroups*, arXiv:2211.12952v1 (first public 2022-11-23), https://arxiv.org/abs/2211.12952 ; primary MSC2020 20M07.
2. S. V. Pantazi and T. Spircu, *Relations between consecutive Catalan monoids*, preprint dated 2016-02-10, updated 2017-03-17, author-uploaded text at https://www.researchgate.net/publication/330567006_Relations_between_consecutive_Catalan_monoids .
3. OEIS A007070, the previously known sequence with recurrence \(a_{k+2}=4a_{k+1}-2a_k\), https://oeis.org/A007070 .
