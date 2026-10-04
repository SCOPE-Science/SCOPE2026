# Sharp coincidence boundary for egalitarian and minimum-regret stable marriage
## Finding
Consider the classical stable-marriage problem with the same number of men and women, complete strict preferences, and perfect matchings. For a stable matching \(M\), define its egalitarian cost as the sum of the partner ranks of all participants, and define its regret as the largest partner rank attained by any participant.

Let \(E(I)\) denote the stable matchings of an instance \(I\) minimizing egalitarian cost, and let \(R(I)\) denote those minimizing regret.

For every instance with at most \(3\) men and \(3\) women,
\[
E(I)\subseteq R(I)
\qquad\text{or}\qquad
R(I)\subseteq E(I).
\]
Thus the two standard fairness criteria always admit a common stable optimizer through size \(3\).

For \(3\) men and \(3\) women there are
\[
6^6=46656
\]
labeled strict-preference profiles. Their exact classification is
\[
\begin{array}{c|r}
\text{relation between }E(I)\text{ and }R(I) & \text{profiles}\\ \hline
E(I)=R(I) & 40056\\
E(I)\subsetneq R(I) & 5400\\
R(I)\subsetneq E(I) & 1200
\end{array}
\]
and there are no profiles with nonnested overlap or with disjoint optimum sets. The corresponding probabilities under independent uniform strict preferences are
\[
\frac{1669}{1944},\qquad
\frac{25}{216},\qquad
\frac{25}{972}.
\]

The coincidence boundary is sharp. With women labeled \(A,B,C,D\), take men's preferences
\[
\begin{aligned}
m_1&: B\succ C\succ D\succ A,\\
m_2&: A\succ C\succ B\succ D,\\
m_3&: A\succ D\succ C\succ B,\\
m_4&: A\succ D\succ C\succ B,
\end{aligned}
\]
and women's preferences
\[
\begin{aligned}
A&:m_2\succ m_3\succ m_1\succ m_4,\\
B&:m_3\succ m_4\succ m_1\succ m_2,\\
C&:m_1\succ m_4\succ m_3\succ m_2,\\
D&:m_4\succ m_2\succ m_3\succ m_1.
\end{aligned}
\]

This instance has exactly two stable matchings. The matching
\[
M_R=(B,A,C,D)
\]
has individual partner ranks, listing men first and then women,
\[
(1,1,3,2,1,3,3,1),
\]
so its egalitarian cost is \(15\) and its regret is \(3\). The other stable matching,
\[
M_E=(C,A,B,D),
\]
has rank vector
\[
(2,1,4,2,1,1,1,1),
\]
so its egalitarian cost is \(13\) and its regret is \(4\). Hence
\[
E(I)=\{M_E\},
\qquad
R(I)=\{M_R\},
\qquad
E(I)\cap R(I)=\varnothing.
\]
Therefore size \(4\) is the first balanced strict stable-marriage market in which the egalitarian and minimum-regret objectives can force different stable matchings.

## Assumptions and scope
Preferences are complete and strict on the opposite side. All matchings are perfect. A matching is stable when no unmatched man-woman pair strictly prefers each other to their assigned partners.

Partner rank is one-based. The egalitarian objective minimizes the sum of all \(2n\) partner ranks. The minimum-regret objective minimizes the maximum of those ranks. Ties among equally optimal stable matchings are retained, so \(E(I)\) and \(R(I)\) are sets rather than arbitrarily tie-broken single matchings.

The theorem concerns exact objective-set relations for \(n\le3\) and a sharp explicit conflict witness at \(n=4\). It makes no classification claim for larger markets.

## Proof
For \(n=2\), direct enumeration of all \(2^4=16\) labeled preference profiles shows that the two optimum sets coincide in every instance.

For \(n=3\), the verifier enumerates every one of the \(6^6=46656\) labeled preference profiles. For each profile it enumerates all \(3!=6\) perfect matchings and tests stability by the absence of a blocking pair. Among the stable matchings, it computes both exact integer objectives and records their full argmin sets.

Two independent stability implementations must return the same stable set profile by profile. One implementation uses precomputed rank maps; the other compares positions directly in the preference lists. Their complete results agree.

The resulting relation counts are
\[
40056,\quad 5400,\quad 1200
\]
for equality, strict egalitarian-set inclusion, and strict minimum-regret-set inclusion respectively. The counts for nonnested overlap and disjointness are both zero. This exhausts the finite domain and proves universal nesting for \(n=3\).

As a marginal cross-check, the same enumeration reproduces the stable-matching-count distribution
\[
34080,\quad11484,\quad1092
\]
for instances with respectively \(1,2,3\) stable matchings.

For the displayed \(4\times4\) witness, all \(4!=24\) perfect matchings are tested. Exactly two are stable, namely \(M_R\) and \(M_E\). Their participant-rank vectors are explicitly
\[
(1,1,3,2,1,3,3,1)
\]
and
\[
(2,1,4,2,1,1,1,1).
\]
The first has objective pair
\[
(\text{sum},\text{regret})=(15,3),
\]
while the second has
\[
(\text{sum},\text{regret})=(13,4).
\]
With only these two stable matchings, \(M_E\) is uniquely egalitarian and \(M_R\) is uniquely minimum-regret, proving disjointness at size \(4\). Together with the exhaustive \(n\le3\) result, this proves sharpness.

## Verification
The embedded `verify_egalitarian_minregret_boundary.py` uses only the Python standard library and exact integer comparisons.

It checks:
- all \(16\) strict \(2\times2\) profiles;
- all \(46656\) strict \(3\times3\) profiles;
- equality of two independently coded stability tests on every tested profile;
- the exact \(3\times3\) relation histogram \(40056,5400,1200\);
- absence of nonnested and disjoint objective sets at \(3\times3\);
- the independent stable-count marginal \(34080,11484,1092\);
- all \(24\) perfect matchings of the \(4\times4\) witness;
- exactly two stable witness matchings and their complete participant-rank vectors;
- disjoint unique egalitarian and minimum-regret optima in that witness.

Run:

`python3 verify_egalitarian_minregret_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Egalitarian stable marriage and minimum-regret stable marriage are established optimization criteria. The egalitarian criterion minimizes the total partner-rank cost, while minimum regret minimizes the worst individual partner rank. Both are known to be polynomially solvable in the classical strict stable-marriage model.

Gelain, Pini, Rossi, Venable, and Walsh survey and computationally study these and related stable-matching objectives. De Clercq, Schockaert, De Cock, and Nowé explicitly formulate the egalitarian cost as the sum of individual ranks and regret as the maximum individual rank.

Recent fair-stable-matching work gives examples where the two criteria conflict in larger markets, so qualitative incompatibility is prior. In particular, a five-pair example in recent work exhibits different stable matchings favored by the two criteria.

The result here is the exact small-market boundary: universal nesting of the complete argmin sets for every strict instance through \(3\times3\), the full \(46656\)-profile census at \(3\times3\), and a \(4\times4\) witness proving that the nesting property fails immediately at the next size. Targeted searches for this exact boundary, its profile counts, and the \(4\times4\) minimal conflict did not locate an equivalent published theorem.

## Limitations
The result is restricted to the classical bipartite stable-marriage model with complete strict preferences. It does not address ties, incomplete lists, roommates, many-to-one matching, capacities, or larger-market classifications.

The \(3\times3\) theorem is an exhaustive finite classification rather than a symbolic case proof. The use of two independent stability tests and a separate marginal check reduces implementation risk but does not convert the computation into a general-\(n\) theorem.

An unindexed thesis, exercise, software table, or supplementary computation could contain the same small-market boundary even though the targeted literature and repository searches did not reveal one.

## References
1. M. Gelain, M. S. Pini, F. Rossi, K. B. Venable, and T. Walsh, “Local Search Approaches in Stable Matching Problems,” *Algorithms* 6 (2013), 591–617. DOI: 10.3390/a6040591. Published 3 October 2013.
2. S. De Clercq, S. Schockaert, M. De Cock, and A. Nowé, “Solving stable matching problems using answer set programming,” *Theory and Practice of Logic Programming* 16 (2016), 247–268. DOI: 10.1017/S147106841600003X. Published online 7 March 2016.
3. S. Desai, S. Rasheed, G. Ghalme, and S. Gujar, “Fair Stable Matching: A Nash Social Welfare Approach,” arXiv:2609.02354, first submitted 2 September 2026.
