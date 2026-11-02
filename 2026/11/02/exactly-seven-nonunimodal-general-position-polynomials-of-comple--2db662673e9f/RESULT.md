# Exactly seven nonunimodal general-position polynomials of complete bipartite graphs

## Finding

**Theorem.** Let \(m\ge n\ge1\) be integers, and let \(\psi(K_{m,n};z)=\sum_{k\ge0}a_kz^k\) count vertex subsets in general position in the complete bipartite graph \(K_{m,n}\). Then the full coefficient sequence is **not unimodal if and only if**
\[
(m,n)\in\{(8,4),(8,5),(8,6),(8,7),(8,8),(9,6),(9,7)\}.
\]
In each of these seven cases, and nowhere else, the failure is a strict valley at cardinality three:
\[
a_2>a_3<a_4.
\]
Moreover, for every \(m\ge n\ge1\), the auxiliary sequence \(\bigl(\binom mk+\binom nk\bigr)_{k=0}^{m}\) is log-concave. In particular the general-position coefficients from cardinality three onward are always unimodal, and no later valley is possible.

## Assumptions and scope

All graphs are finite, simple and undirected. Two vertices of \(K_{m,n}\) are adjacent precisely when they lie in opposite parts. A vertex set is in *general position* if no three distinct vertices in it lie on a common shortest path. A finite nonnegative coefficient sequence is *unimodal* if it is nondecreasing up to some index and nonincreasing thereafter (equalities are allowed). Only coefficients through the degree of the polynomial are considered; no trailing zeros are appended. Part sizes are positive, and \((m,n)\) denotes an unordered isomorphism type by imposing \(m\ge n\). The theorem includes stars and the single-edge graph \(K_{1,1}\).

The known exact general-position polynomial [1] is
\[
\psi(K_{m,n};z)=1+(m+n)z+\binom{m+n}{2}z^2
+\sum_{k=3}^{m}\left(\binom mk+\binom nk\right)z^k,
\]
with the convention \(\binom rk=0\) when \(k>r\). The finding is the **complete all-parameter shape classification**, not this previously published coefficient formula.

## Proof

**1. Counting interpretation.** Every subset of at most two vertices is in general position. If a selected set of size at least three meets both bipartition classes and contains two vertices \(u,v\) in one class, any selected vertex \(w\) in the other lies internally on the length-two geodesic \(u,w,v\). Conversely, if all selected vertices lie in one part, any internal vertex of a geodesic between two selected vertices belongs to the *other* part, so the set is in general position. This proves the displayed coefficient formula, independently of the citation.

**2. A log-concave binomial tail.** Write \(t_k=\binom mk+\binom nk\), including \(k=0,1,2\), and put \(d=m-n\). Its generating polynomial factors exactly as
\[
\sum_{k=0}^{m}t_kz^k=(1+z)^n\bigl(1+(1+z)^d\bigr).
\]
The coefficient sequence of \((1+z)^n\) is log-concave without internal zeros. The second factor has coefficients \(b_0=2\) and \(b_k=\binom dk\) for \(1\le k\le d\). For \(d\le1\) log-concavity is immediate. For \(d\ge2\), its only non-binomial log-concavity test is
\[
b_1^2-b_0b_2=d^2-2\binom d2=d\ge0.
\]
All other tests follow from the usual binomial coefficient inequalities. Thus both factors have contiguous, log-concave nonnegative coefficient sequences.

For completeness, convolution preserves this property. Extend a finite such sequence \(u\) by zeros and form its Toeplitz matrix \(T(u)_{ij}=u_{j-i}\), with integer indices. Successive coefficient ratios are nonincreasing wherever defined, so every \(2\)-by-\(2\) minor of \(T(u)\) is nonnegative. For two sequences \(u,v\), the identity \(T(u*v)=T(u)T(v)\) holds entrywise, with only finitely many nonzero summands. The \(2\)-by-\(2\) Cauchy–Binet identity expresses each minor of the product as a sum of products of nonnegative minors. Hence \(u*v\) is log-concave, by applying the adjacent minor inequality. The displayed factorization therefore proves \(t_k^2\ge t_{k-1}t_{k+1}\) for every interior \(k\). In particular the actual coefficients \(a_k=t_k\) for \(k\ge3\) form a unimodal tail.

**3. Only one potential valley.** Except for \(K_{1,1}\), which has polynomial \(1+2z+z^2\), the first three coefficients obey \(a_0\le a_1\le a_2\), since \(a_2=\binom{m+n}{2}\) and \(m+n\ge3\). Because the tail from index three is unimodal, the full sequence can fail unimodality *only if* \(a_2>a_3\) and \(a_4>a_3\). Conversely those strict inequalities exhibit a failure. If \(m<4\), put \(a_4=0\) and the same criterion cannot hold.

**4. No anomaly for \(m\le7\).** For each \(r\le7\), \(\binom r4\le\binom r3\). Hence \(a_4\le a_3\), ruling out the only possible valley.

**5. No anomaly for \(m\ge10\).** We show \(a_3\ge a_2\). If \(n\ge9\), then for every integer \(r\ge9\),
\[
\binom r3\ge r^2
\quad\text{because}\quad
(r-1)(r-2)\ge6r.
\]
Consequently
\[
a_3=\binom m3+\binom n3\ge m^2+n^2
\ge\frac{(m+n)^2}{2}\ge\binom{m+n}{2}=a_2.
\]
For \(1\le n\le8\), set
\[
F(m,n)=\binom m3+\binom n3-\binom{m+n}{2}.
\]
The exact finite difference is
\[
F(m+1,n)-F(m,n)=\binom m2-(m+n)>0
\quad(m\ge10,\ 1\le n\le8).
\]
At \(m=10\), the values of \(F(10,n)\) in order \(n=1,\ldots,8\) are
\[
65,54,43,33,25,20,19,23.
\]
All are positive; the finite-difference identity extends this to every larger \(m\). Thus \(a_3\ge a_2\) in all cases with \(m\ge10\).

**6. Exhausting the two remaining part sizes.** For \(m=8\),
\[
a_4-a_3=14+\binom n4-\binom n3>0
\quad(1\le n\le8).
\]
For \(m=9\), similarly
\[
a_4-a_3=42+\binom n4-\binom n3>0
\quad(1\le n\le9).
\]
Both assertions follow because \(\binom n4-\binom n3\ge-5\) for \(1\le n\le9\), as is immediate from \(\binom n4-\binom n3=\binom n3(n-7)/4\). It therefore suffices to inspect \(F(m,n)=a_3-a_2\). The exact values for \(n=1,\ldots,m\), respectively, are
\[
\begin{aligned}
m=8:&\quad20,11,2,-6,-12,-15,-14,-8;\\
m=9:&\quad39,29,19,10,3,-1,-1,4,15.
\end{aligned}
\]
The negative entries occur at precisely the seven unordered part-size pairs in the theorem. Each has \(a_4>a_3\), establishing nonunimodality, while every other case has been excluded. \(\square\)

## Verification

Run `python3 verify.py` using Python 3.10 or later, without third-party packages. The verifier constructs complete bipartite graph adjacencies, computes all graph distances by breadth-first search, rejects subsets containing any geodesically aligned triple, and compares *every* cardinality coefficient with the independently derived closed formula. It exhausts 530604 vertex subsets on 36 boards (including all seven exceptional parameter pairs and \(K_{8,8}\), \(K_{9,9}\)), and separately checks the classification, convolution identity and tail log-concavity for all 11325 unordered pairs with largest part at most 150. Its successful final line is `VERIFY_OK`. These finite calculations check implementation and small cases; the six proof steps establish the theorem for all positive part sizes.

## Relationship to prior work

Iršič, Klavžar, Rus and Tuite [1] introduced the general-position polynomial, derived the complete-bipartite coefficient formula (Proposition 2.1(v)), and exhibited \(K_{8,4}\) and \(K_{9,7}\) as nonunimodal examples. Those two examples and the coefficient formula are prior work. Rather [2] revisited the complete-multipartite formula and exhibited \(K_{8,8}\) as another nonunimodal example, with general balanced-multipartite investigations but no universal two-part classification. The general-position survey [3], in its August 2026 version, summarizes these results without specifying every exceptional complete-bipartite part-size pair. The present all-parameter *if and only if* statement and its log-concave-tail proof resolve the remaining classification for the complete-bipartite subclass; they are not a new formula for the polynomial.

## Limitations

The claim concerns ordinary general position, not dual, outer or total variants. It makes no assertion about general complete multipartite graphs with three or more nonempty parts, corona graphs, or log-concavity of the **whole** polynomial; full log-concavity can fail even when unimodality holds. A literature and mathematical-record comparison identified no earlier complete classification, but an unindexed or inaccessible equivalent result cannot be ruled out. Finite computational checks alone would not prove the infinite classification. No independent mathematical audit has been performed.

## References

[1] V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General position polynomials*, arXiv:2401.05696v1 (first posted 2024-01-11), especially Proposition 2.1(v) and Section 4; published in *Results in Mathematics* 79 (2024), article 110. https://arxiv.org/html/2401.05696v1

[2] B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930v1 (2026-03-06), especially Sections 3–4. https://arxiv.org/abs/2603.06930

[3] U. Chandran S. V., S. Klavžar, J. Tuite, *The General Position Problem: A Survey*, arXiv:2501.19385v5 (2026-08-16), Section 2.3.4. https://arxiv.org/html/2501.19385v5
