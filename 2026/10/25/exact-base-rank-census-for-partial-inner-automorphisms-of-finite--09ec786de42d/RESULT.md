# Exact base-rank census for partial inner automorphisms of finite full transformation monoids

## Finding
Let \(X\) be an \(n\)-element set, \(n\geq2\), let \(T_X\) be its full transformation monoid, and let \(\operatorname{Inn}(T_X)\) be the inverse monoid of partial inner automorphisms associated to natural semigroup conjugacy. Every element has a canonical partial-bijection component \(\alpha\) on \(X\). Define its **base rank** to be \(k=|\operatorname{dom}\alpha|\), and denote the number of elements of base rank \(k\) by \(N_{n,k}\).

Write \(S(a,b)\) for the Stirling number of the second kind, \(B_a=\sum_b S(a,b)\) for the Bell number, and, for integers \(m\geq0\), \(q\geq1\), \(0\leq t\leq m\), put
\[
U_m(q,t)=\sum_{j=t}^{m}\binom mj q^{m-j}S(j,t).
\]
Then the **complete base-rank distribution** is
\[
\boxed{N_{n,0}=1,\qquad N_{n,1}=n^2,}
\]
and for every \(2\leq k\leq n\), putting \(m=n-k\),
\[
\boxed{
N_{n,k}=\binom nk^2 k!\left(
\sum_{q=1}^{k} S(k,q)
\sum_{t=0}^{m}t!\,U_m(q,t)^2
-B_k\,m!\right)+n!\,\mathbf 1_{\{k=n\}}.
}
\]
In particular, \(N_{n,n}=n!\), and, for \(n\geq3\),
\[
\boxed{N_{n,n-1}=n^2(n-1)!\bigl(B_{n+1}-2B_n\bigr).}
\]
For \(n=1\) the monoid has only its identity, of base rank one.

The rank distributions from \(n=2\) through \(n=6\) are, respectively,
\[
(1,4,2),\quad (1,9,90,6),\quad
(1,16,3672,2112,24),
\]
\[
(1,25,141800,157800,59400,120),
\]
\[
(1,36,6202350,10245600,7635600,2034720,720).
\]
Thus the respective total orders are \(7,106,5825,359146,26119027\).

## Assumptions and scope
Throughout \(n\geq2\) and \(X\) is a set with precisely \(n\) distinct elements. Composition in \(T_X\) is the usual semigroup multiplication, in which functions act on the right. If \(g,h\in T_X\), define
\[
D_{g,h}=\{a\in T_X:(gh)a=a(gh)=a\},\qquad
\varphi_{g,h}:D_{g,h}\to D_{h,g},\quad a\mapsto hag.
\]
The inverse monoid \(\operatorname{Inn}(T_X)\) is generated, under partial-map composition, by the \(\varphi_{g,h}\). This is the definition used by Araújo and collaborators [1]. The rank defined above is **not** the cardinality of the domain of a partial map on \(T_X\): it is the size of the domain of its canonical partial bijection \(\alpha\) on \(X\), as specified by their representation theorem. That rank is well defined for all elements, including the two low-rank quotient classes.

For \(S(0,0)=1\), put \(S(j,t)=0\) for \(t>j\); use \(0!=1\). Empty sums have value zero. The formulas are exact in integers and do not use probabilistic or asymptotic assumptions.

## Proof
**Step 1: canonical finite representation.** Theorems 5.7 and 5.9 of [1] give a faithful realization of \(\operatorname{Inn}(T_X)\) through pairs \((\alpha,\beta)\), where \(\alpha:I\to I'\) is a bijection of subsets of \(X\), and \(\beta:P\to P'\) is a bijection between the blocks of two set partitions of \(X\). The required compatibility is
\[
\beta([i]_P)=[\alpha(i)]_{P'}\quad\text{for all }i\in I.
\]
Pairs with \(|I|\leq1\) are identified exactly when they have the same \(\alpha\). For \(k=|I|\geq2\), each compatible pair represents a distinct element **if and only if** either (i) \(I=X\) and \(P\) is the singleton partition, or (ii) some block \(C\in P\) has \(|C|\geq2\) and \(C\not\subseteq I\). The published proof also establishes that every pair satisfying either condition really occurs in the generated inverse monoid. This last surjectivity statement is essential: the count is not taken in a larger ambient partial-bijection monoid.

**Step 2: choose the partial bijection and its marked partition.** Fix a bijection \(\alpha:I\to I'\) with \(|I|=|I'|=k\geq2\). There are exactly \(\binom nk^2k!\) choices of \(\alpha\). A compatible source partition \(P\) restricts to a partition \(R=P|_I\) of the marked set \(I\). Let \(q\) be the number of blocks of \(R\). There are exactly \(S(k,q)\) possible \(R\). The target partition necessarily restricts to the transported partition \(\alpha(R)\) of \(I'\), and \(\beta\) is forced on the \(q\) blocks that meet the marked sets.

**Step 3: extend the marked partition.** Put \(m=n-k\). Suppose a partition \(P\) of \(X\) restricts to \(R\) and has precisely \(t\) further blocks disjoint from \(I\). Choose \(j\) of the \(m\) unmarked points to form those \(t\) nonempty blocks in \(\binom mj S(j,t)\) ways. Each of the other \(m-j\) unmarked points is independently adjoined to one of the \(q\) marked blocks in \(q^{m-j}\) ways. Summing over \(j\) gives exactly \(U_m(q,t)\). The same count applies to the target partition. Compatibility forces matching marked blocks, while the \(t\) unmarked source blocks can be bijected with the \(t\) unmarked target blocks in \(t!\) ways. Thus, for fixed \(\alpha,R\), the number of all compatible pairs is
\[
\sum_{t=0}^{m}t!\,U_m(q,t)^2.
\]
Summing over the \(S(k,q)\) choices of \(R\) gives the double sum in the statement.

**Step 4: remove precisely the forbidden pairs.** Condition (ii) fails exactly when **every unmarked element is a singleton block of \(P\)**. Indeed, an unmarked point in a block of size at least two makes that block satisfy (ii), and the converse is immediate. For fixed \(R\), a forbidden source partition is forced to be \(R\) together with the \(m\) unmarked singleton blocks. To admit a compatible block bijection, the target must also have \(m\) blocks disjoint from \(I'\). With just \(m\) unmarked target points, these must likewise all be singleton blocks. The only remaining freedom is the \(m!\) permutations of the unmarked blocks. Thus there are exactly \(B_km!\) forbidden pairs for each fixed \(\alpha\), proving the correction term.

If \(k<n\), condition (i) never applies, so the permitted count is the double sum minus this correction. If \(k=n\), every compatible pair fails (ii), but (i) admits precisely the singleton source partition; each full bijection \(\alpha\) then has one forced compatible \(\beta\). These are the \(n!\) units, explaining the final indicator term. Finally, the low-rank quotient gives one empty partial bijection and \(n^2\) singleton partial bijections, proving \(N_{n,0}=1\) and \(N_{n,1}=n^2\).

**Step 5: the next-to-top rank.** For \(k=n-1\geq2\), \(m=1\). Directly from the definition, \(U_1(q,0)=q\) and \(U_1(q,1)=1\). The parenthesized contribution per partition with \(q\) blocks is therefore \(q^2+1-1=q^2\). The standard Bell-polynomial recurrence gives
\[
\sum_{q=1}^{k}q^2S(k,q)=B_{k+2}-2B_{k+1}.
\]
Since \(\binom n{n-1}^2(n-1)!=n^2(n-1)!\), the stated corank-one formula follows.

## Verification
Run \(\texttt{python3 verify.py}\) alongside this file using ordinary Python 3. The script uses only the standard library and reports `VERIFY_OK` on completion. Three checks are deliberately separate:

1. The displayed Stirling-number formula is evaluated at every \(n\leq6\).
2. Independently, for every \(n\leq5\), every ordered pair of partitions and every bijection of their blocks is enumerated; polynomial weights count all compatible marked-point bijections. Forbidden pairs are removed and the surviving base-rank vectors agree with the formula.
3. For \(n=2,3\), the actual maps \(\varphi_{g,h}\) on the complete transformation monoid are explicitly constructed and their generated semigroup is exhaustively closed under composition; the orders are \(7\) and \(106\), respectively.

The first six rank vectors in the Finding section are exact program outputs. These checks do **not** prove the formula for unbounded \(n\); the counting argument and cited structural theorem do.

## Relationship to prior work
Araújo, Bentz, Kinyon, Konieczny, Malheiro, and Mercier [1], Theorems 5.7 and 5.9, construct and classify the compatible pairs representing partial inner automorphisms of \(T_X\). This is indispensable prior coverage, not new here. Their explicit criterion, including the exceptional full-domain units and collapse of the low-rank pairs, is used verbatim as a theorem. The contribution here is a **complete enumerative base-rank spectrum** with a finite Stirling/Bell formula and its corank-one Bell difference, not an alternative structural classification.

An earlier combined manuscript by the same authors [2] introduced natural conjugacy and originally contained material later separated into [1]. Its publicly accessible current version does not state the above rank enumerator; the older separate-section version is a residual comparison risk. Related literature on symmetric inverse monoids counts partial bijections without compatible partition data, so those formulas do not yield this enumeration. Direct searches for the five numerical totals and the paired-partition enumeration found no equivalent published formula.

## Limitations
The result assumes finite \(X\) and the full transformation monoid. It does not enumerate arbitrary partial automorphism monoids, describe the Green structure of the resulting inverse monoid, or assert a new characterization of its elements. The base rank of \(\alpha\) is not the transformation rank of a typical \(a\in T_X\). All claimed counts depend on Theorem 5.9 of [1]; the computational verifier does not provide a separate infinite proof of that foundational classification. Independent peer review and an exhaustive check of all older, possibly unindexed sources have not occurred.

## References
[1] J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro, V. Mercier, *The Inverse Monoid of Partial Inner Automorphisms of a Semigroup*, arXiv:2605.00041, publicly submitted 2026-04-28; https://arxiv.org/abs/2605.00041 . In particular, Theorems 5.7 and 5.9, pp. 12–14.

[2] J. Araújo, W. Bentz, M. Kinyon, J. Konieczny, A. Malheiro, V. Mercier, *Conjugacy in Semigroups: the Partition and Brauer Diagram Monoids, Conjugacy Growth, and Partial Inner Automorphisms*, arXiv:2301.04252, first submitted 2023-01-11; https://arxiv.org/abs/2301.04252 . An earlier version contained material later published separately as [1].

[3] Standard definitions of Stirling and Bell numbers: R. P. Stanley, *Enumerative Combinatorics*, vol. 2, Cambridge University Press, 1999, Chapter 5.
