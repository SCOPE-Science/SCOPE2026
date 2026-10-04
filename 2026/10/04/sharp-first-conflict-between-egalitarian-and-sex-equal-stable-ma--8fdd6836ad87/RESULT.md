# Sharp first conflict between egalitarian and sex-equal stable marriage
## Finding
Consider the classical stable-marriage problem with \(n\) men and \(n\) women, complete strict preferences, and perfect stable matchings.

For a stable matching \(M\), write
\[
c_M(M)=\sum_m \operatorname{rank}_m(M(m)),
\qquad
c_W(M)=\sum_w \operatorname{rank}_w(M(w)).
\]
Define the egalitarian cost by
\[
c_E(M)=c_M(M)+c_W(M),
\]
and the sex-equal cost by
\[
c_S(M)=\left|c_M(M)-c_W(M)\right|.
\]
Let \(E(I)\) and \(S(I)\) be the complete argmin sets of these two objectives over the stable matchings of an instance \(I\).

For every \(2\times2\) instance,
\[
E(I)=S(I).
\]

For \(3\times3\), the exact relation across all
\[
6^6=46656
\]
labeled strict-preference profiles is
\[
\begin{array}{c|r|c}
\text{relation} & \text{profiles} & \text{probability}\\ \hline
E(I)=S(I) & 40056 & 1669/1944\\
S(I)\subsetneq E(I) & 3720 & 155/1944\\
E(I)\subsetneq S(I) & 360 & 5/648\\
E(I)\cap S(I)=\varnothing & 2520 & 35/648
\end{array}
\]
and there are no profiles with nonnested nonempty overlap.

Hence three pairs are the smallest balanced strict stable-marriage market in which egalitarian and sex-equal fairness can force incompatible stable choices.

A concrete \(3\times3\) witness is:
\[
\begin{aligned}
m_1&:A\succ B\succ C,\\
m_2&:A\succ B\succ C,\\
m_3&:A\succ C\succ B,
\end{aligned}
\qquad
\begin{aligned}
A&:m_1\succ m_2\succ m_3,\\
B&:m_1\succ m_3\succ m_2,\\
C&:m_2\succ m_1\succ m_3.
\end{aligned}
\]

It has exactly two stable matchings:
\[
M_S=(A,B,C)
\]
for men \(m_1,m_2,m_3\), with men's and women's total rank costs \(5\) and \(7\), giving
\[
(c_E,c_S)=(12,2),
\]
and
\[
M_E=(A,C,B),
\]
with men's and women's total rank costs \(7\) and \(4\), giving
\[
(c_E,c_S)=(11,3).
\]
Therefore
\[
E(I)=\{M_E\},
\qquad
S(I)=\{M_S\},
\qquad
E(I)\cap S(I)=\varnothing.
\]

## Assumptions and scope
Preferences are complete and strict. All partner ranks are one-based. Stability means absence of a man-woman blocking pair.

The egalitarian objective minimizes the sum of all participants' partner ranks. The sex-equal objective minimizes the absolute difference between the men's aggregate partner-rank cost and the women's aggregate partner-rank cost.

Optimal sets retain all ties; no arbitrary tie-breaking is imposed.

The exact classification concerns \(n=2\) and \(n=3\). No frequency statement for \(n\ge4\) is claimed.

## Proof
For \(n=2\), the verifier exhausts all
\[
2^4=16
\]
labeled strict-preference profiles and finds equality of the two argmin sets in every instance.

For \(n=3\), each person has \(6\) strict orders, so there are
\[
6^6=46656
\]
labeled profiles. For each profile, every one of the \(3!=6\) perfect matchings is checked for stability. For each stable matching, the men's rank sum, women's rank sum, egalitarian cost, and absolute sex-equal cost are computed as exact integers.

Two independently written stability tests are required to return the same stable set profile by profile. One uses precomputed rank maps; the other compares list positions directly.

The complete enumeration yields exactly
\[
40056,\quad3720,\quad360,\quad2520
\]
profiles in the four relation classes stated above, and zero profiles with a nonempty nonnested overlap.

As a separate marginal check, the same run reproduces the known \(3\times3\) stable-matching-count distribution
\[
34080,\quad11484,\quad1092
\]
for instances with respectively one, two, and three stable matchings.

For the displayed witness, exhaustive testing leaves exactly the two stated stable matchings. Their objective pairs are directly
\[
(12,2)
\quad\text{and}\quad
(11,3),
\]
so one uniquely minimizes sex-equal cost and the other uniquely minimizes egalitarian cost.

## Verification
The embedded `verify_egalitarian_sexequal_boundary.py` uses only the Python standard library and exact integer arithmetic.

It verifies:
- all \(16\) strict \(2\times2\) profiles;
- all \(46656\) strict \(3\times3\) profiles;
- equality of two independent stability tests on every tested profile;
- the exact relation counts \(40056,3720,360,2520\);
- absence of nonnested nonempty overlap;
- the stable-count marginal \(34080,11484,1092\);
- the displayed two-stable-matching witness and both objective pairs.

Run:

`python3 verify_egalitarian_sexequal_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
The egalitarian and sex-equal objectives are classical fairness criteria for stable marriage. Iwama, Miyazaki, and Yanagisawa define egalitarian cost as the total rank sum and sex-equalness as the difference between the aggregate men's and women's rank costs; they study approximation for the sex-equal stable-marriage problem and also discuss optimizing egalitarian cost subject to sex-equality constraints.

De Clercq, Schockaert, De Cock, and Nowé give an exact optimization framework covering egalitarian, minimum-regret, and sex-equal stable matchings, confirming the same objective definitions in a broader stable-matching setting.

Khovanova and coauthors later enumerate several small stable-marriage profile statistics and egalitarian-cost distributions, including the \(3\times3\) distribution of the number of stable matchings. Their paper does not tabulate sex-equal optima or the relation between the egalitarian and sex-equal argmin sets.

The contribution here is the exact first-conflict boundary and complete \(3\times3\) argmin-set relation census, including the \(2520\) disjoint profiles and a smallest explicit disjoint-optimum witness.

## Limitations
The result is restricted to complete strict bipartite stable marriage and one-based ordinal rank costs.

The \(3\times3\) theorem is a complete finite classification, not a symbolic formula for arbitrary \(n\). Larger markets, ties, incomplete lists, roommates, and many-to-one variants are outside scope.

Targeted searches did not locate the exact four-way \(3\times3\) argmin-set relation table or the sharp \(2\)-to-\(3\) pair boundary, but an unindexed note, thesis, exercise, or software table could contain an equivalent classification.

## References
1. K. Iwama, S. Miyazaki, and H. Yanagisawa, “Approximation Algorithms for the Sex-Equal Stable Marriage Problem,” WADS 2007 / later ACM Transactions on Algorithms 7 (2010). DOI: 10.1145/1868237.1868239. Kyoto University repository record 2433/226949.
2. S. De Clercq, S. Schockaert, M. De Cock, and A. Nowé, “Solving stable matching problems using answer set programming,” *Theory and Practice of Logic Programming* 16 (2016), 247–268. DOI: 10.1017/S147106841600003X.
3. S. Bistarelli and F. Santini, “Abstract argumentation and (optimal) stable marriage problems,” *Argument & Computation* 11 (2020), 15–40. DOI: 10.3233/AAC-190474.
4. M. Borodin, E. Chen, A. Duncan, T. Khovanova, B. Litchev, J. Liu, V. Moroz, M. Qian, R. Raghavan, G. Rastogi, and M. Voigt, “Sequences of the Stable Matching Problem,” *Journal of Integer Sequences* 27 (2024), Article 24.2.2.
