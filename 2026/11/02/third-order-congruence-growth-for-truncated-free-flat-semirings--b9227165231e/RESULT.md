# Third-order congruence growth for truncated free flat semirings

## Finding
Let \(X\) be a finite alphabet of size \(n\ge2\), let \(k\ge2\) be fixed, and let \(T_{n,k}=S(X^k)\) be the flat additively idempotent semiring whose nonzero elements are all nonempty words over \(X\) of length at most \(k\). Write \(C_{n,k}=|\operatorname{Con}(T_{n,k})|\) for the number of semiring congruences in the signature \((+,\cdot)\).

For fixed \(k\ge3\), with \(N=n^{k-1}\) and
\[
Q_k(n)=\binom{N}{2}+2n(N-1)+3n(n-1),
\]
the following three-term expansion holds as \(n\to\infty\):
\[
\boxed{C_{n,k}=2^{n^k}\left[1+(N+n)2^{-2n}+Q_k(n)2^{-4n}+O_k\!\left(N^3 2^{-6n}\right)\right].}
\]
For \(k=2\), an exact formula and its three-term expansion are
\[
\boxed{C_{n,2}=\sum_{j=0}^{n}\binom nj 2^{(n-j)^2}
=2^{n^2}\left[1+2n2^{-2n}+16\binom n2 2^{-4n}+O\!\left(n^3 2^{-6n}\right)\right].}
\]
For every \(n\ge2\), the displayed main, first, and second corrections are **exactly** the contributions from congruences whose zero class contains respectively zero, one, or two distinct words of length \(k-1\), and no shorter nonzero word. The error counts all remaining congruences and is nonnegative. In particular, the relative chance that a uniformly chosen congruence collapses any word shorter than length \(k\) is
\[
(N+n)2^{-2n}+O_k\!\left(N^2 2^{-4n}\right)\quad(k\ge3),
\]
while for \(k=2\) the leading probability is \(2n2^{-2n}+O(n^2 2^{-4n})\).

## Assumptions and scope
The alphabet \(X\) is arbitrary but labeled; its size \(n\) tends to infinity while the truncation length \(k\) stays fixed. The word set consists of **nonempty** words, so there is no identity/empty word. The product of two words is their concatenation if its length is at most \(k\), and is zero otherwise. Addition satisfies \(u+u=u\) and \(u+v=0\) for distinct elements \(u,v\); in particular zero is the additive maximum and multiplicative zero. Congruences preserve both operations. The \(O_k\) constant may depend on \(k\) but not on \(n\). The expansion is asymptotic, not asserted as an absolute remainder bound for every small alphabet.

## Proof
**1. Congruences are word-factor upsets.** A known fact about flat semirings, used here as a starting point, is the bijection between semiring congruences and multiplicative ideals: if distinct nonzero elements \(a,b\) are congruent, then \(a=a+a\) is congruent to \(a+b=0\); hence every nonzero congruence class other than the zero class is a singleton. Conversely, each multiplicative ideal containing zero defines a congruence with that ideal as its zero class and other elements singleton. In \(T_{n,k}\), membership of a word in a multiplicative ideal **forces** membership of every contiguous superword of length at most \(k\). Conversely, every set closed under this implication is an ideal. Thus ideals correspond to upward-closed subsets of nonempty words of lengths at most \(k\) under the contiguous-factor order, together with zero.

**2. Exact de Bruijn decomposition.** Put \(V=X^{k-1}\) and choose \(F\subseteq V\), the set of length-\(k-1\) words in the zero class. Let \(w(F)\) count the admissible choices of words of lengths at most \(k-2\) in the ideal, subject to having precisely \(F\) at length \(k-1\). These choices need only satisfy factor-upward closure below length \(k\); the empty choice is always admissible. For each word of length \(k\), inclusion in the ideal is forced if and only if its prefix or suffix of length \(k-1\) belongs to \(F\). Regard length-\(k\) words as arcs in the directed de Bruijn graph on \(V\), from their prefix to their suffix; loops and arc multiplicities are retained. The graph has \(N=n^{k-1}\) vertices and in/out degree \(n\). If \(e(F)\) denotes the number of arcs with both endpoints in \(F\), inclusion-exclusion gives precisely \(2n|F|-e(F)\) forced top words. Every remaining top word can be included independently. Hence the **exact**, finite identity
\[
C_{n,k}=2^{n^k}\sum_{F\subseteq V}w(F)\,2^{-2n|F|+e(F)}.\tag{1}
\]

**3. The zero-, one- and two-vertex terms.** For \(k\ge3\), including any word of length at most \(k-2\) forces at least \(2n-1\) distinct length-\(k-1\) superwords. To see this, extend the selected word to one of length \(k-2\); its \(n\) left extensions and \(n\) right extensions overlap in at most one word. As \(2n-1\ge3\), \(w(F)=1\) whenever \(|F|\le2\). When \(F\) is empty, its contribution to (1) is \(1\). A singleton \(F=\{v\}\) induces a loop exactly when \(v\) is constant; there are exactly \(n\) constant vertices, all others loopless. Thus the total singleton coefficient at \(2^{-2n}\) is \(2n+(N-n)=N+n\).

For a two-element set \(F\), \(e(F)\le2\) when \(k\ge3\). Counting each nonloop arc once and each loop in all \(N-1\) pairs containing it gives
\[
\sum_{|F|=2}e(F)=(nN-n)+n(N-1)=2n(N-1).
\]
Exactly \(3n(n-1)\) pairs induce two arcs: \(\binom n2\) pairs of distinct constant vertices, \(2n(n-1)\) pairs consisting of a constant vertex and an incident distinct vertex, and \(\binom n2\) pairs forming nonconstant two-cycles (alternating two-letter periodic words). The cases are disjoint, and all two-cycles have been accounted for because reciprocal overlaps force period two. For \(e\in\{0,1,2\}\) one has \(2^e=1+e+\binom e2\); hence
\[
\sum_{|F|=2}2^{e(F)}=\binom N2+2n(N-1)+3n(n-1)=Q_k(n).
\]
This gives the exact first three contributions in the theorem.

**4. Controlling all remaining terms.** For each \(F\) with \(|F|=m\), every admissibly selected shorter word must occur as a contiguous factor of a word in \(F\). The number of distinct proper factors of one length-\(k-1\) word is at most \(c_k=\sum_{j=1}^{k-2}(k-j)=k(k-1)/2-1\). Therefore \(1\le w(F)\le 2^{c_k m}\). Also
\[
e(F)\le\min(m^2,nm),
\]
because there is at most one arc for each ordered pair of vertices, and at most \(n\) outgoing arcs per vertex. The sum over \(m=3\) is \(O_k(N^3 2^{-6n})\). The sum over \(m=4\) is \(O_k(N^4 2^{-8n})\), smaller. For \(5\le m\le n/2\), use \(e(F)\le m^2\le nm/2\), so the tail is dominated by the geometric bound \(\sum_{m\ge5}(N2^{c_k-3n/2})^m=O_k(N^5 2^{-15n/2})\). For \(m>n/2\), use \(e(F)\le nm\) and \(\binom Nm\le N^m\) to bound the remaining sum by \(\sum_{m>n/2}(N2^{c_k-n})^m=2^{-\Omega_k(n^2)}\). As \(N\) is a fixed power of \(n\), all these are absorbed in the stated error.

**5. Length two.** If \(k=2\), the vertices are the individual letters; there are no lower nonzero words. Choosing \(j\) letters for the zero class forces exactly \(n^2-(n-j)^2\) two-letter words, leaving \(2^{(n-j)^2}\) choices. Sum over the \(\binom nj\) choices. The terms \(j=0,1,2\) give the displayed coefficients, and the \(j\ge3\) tail has order \(O(n^3 2^{-6n})\) after division by \(2^{n^2}\).

Finally, all three distinguished contributions are exact, so the statement about a random congruence follows by dividing by the total and expanding its reciprocal. This finishes the proof.

## Verification
The standalone Python 3 checker `check_congruences.py` uses exact integer arithmetic. It enumerates all admissible lower-layer factor upsets, counts freely selectable top words, and independently reconstructs the answer via a de Bruijn subset sum when \(k\le3\). For the smallest instances it also exhaustively checks all possible ideals directly. It reports \(C_{2,2}=21\), \(C_{3,2}=567\), \(C_{4,2}=67689\), \(C_{2,3}=390\), \(C_{3,3}=163211542\), and \(C_{2,4}=130315\). Additional arc-level enumeration verifies the two-vertex coefficient for seven parameter pairs through \((n,k)=(5,3)\). The recorded stdout is in `check_output.txt` and ends in `VERIFY_OK`. These computations check finite instances and the local combinatorial identity; the asymptotic conclusion is proved by the preceding inequalities.

## Relationship to prior work
Gao and Zhou (2026) define the exact family \(S(W)\), explain its congruence–ideal correspondence, and resolve its finite identity-basis problem; that correspondence is **previously known** and is not the new claim. Gao, Ren and Zhao (2026) establish the finite-basis behavior of the special truncation family \(S(X^k)\), again without these congruence-growth coefficients. Bailey, Finn-Sell and Snocken (2014) study ideal and congruence growth for the infinite free semigroup, with different index/rank regimes; their statements do not imply the fixed-truncation, growing-alphabet, third-order expansion here. The new content is the exact de Bruijn decomposition and the second overlap correction plus a uniform remainder estimate for all fixed truncation lengths. No exhaustive historical-priority assertion is made.

## Limitations
The asymptotic holds for fixed truncation length \(k\), not uniformly when \(k\) grows with \(n\). The total number of congruences is given exactly only at \(k=2\); equation (1) is an exact finite sum but is not evaluated in closed form for arbitrary \(k\). Other earlier enumerations of word-factor upsets could potentially imply some or all coefficients, and absolute novelty remains subject to independent literature assessment. 

## References
- Z. Gao and Y. Zhou, *Equational theories of flat semirings \(S(W)\)*, arXiv:2610.20308v1, first publicly posted 2026-10-14, https://arxiv.org/abs/2610.20308.
- Z. Gao, M. Ren and X. Zhao, *The finite basis problem for the flat semirings \(S(W)\)*, arXiv:2608.12284v1, https://arxiv.org/abs/2608.12284.
- A. Bailey, M. Finn-Sell and R. Snocken, *Subsemigroup, ideal and congruence growth of free semigroups*, arXiv:1409.2444v1, https://arxiv.org/abs/1409.2444.
