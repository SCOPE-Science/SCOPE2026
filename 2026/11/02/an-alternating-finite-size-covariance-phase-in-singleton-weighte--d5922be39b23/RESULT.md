# An alternating finite-size covariance phase in singleton-weighted noncrossing partitions

## Finding
Fix \(q\ge0\). Give each noncrossing partition \(\pi\) of \([n]\) probability proportional to \(q^{C_1(\pi)}\), where \(C_j(\pi)\) is its number of blocks of cardinality \(j\). At \(q=0\), this means the uniform distribution on partitions without singleton blocks. For each of the first four orders \(n\in\{5,6,7,8\}\) at which a doubleton and a tripleton can coexist, the sign of their count covariance is classified exactly:

\[
\begin{array}{c|c}
 n&\operatorname{sgn}\operatorname{Cov}_{q}(C_2,C_3)\\\hline
 5&+\ (0\le q<\alpha_5),\quad0\ (q=\alpha_5),\quad-\ (q>\alpha_5)\\
 6&-\quad\text{for all }q\ge0\\
 7&+\ (0\le q<\alpha_7),\quad0\ (q=\alpha_7),\quad-\ (q>\alpha_7)\\
 8&-\quad\text{for all }q\ge0.
\end{array}
\]

Here \(\alpha_5\approx0.1641576174\) and \(\alpha_7\approx0.0654143441\) are the unique positive roots of

\[
P_5(q)=19q^5+40q^3+5q-1,
\]
\[
P_7(q)=90q^9+694q^7+126q^6+1218q^5+560q^4+1190q^3+741q^2+252q-20.
\]

In particular, at the fixed strictly positive weight \(q=1/20\), the covariance sign alternates \(+,-,+,-\) as \(n\) runs through \(5,6,7,8\). This is a finite-size boundary to the negative block-count covariance seen in the unweighted \(q=1\) model.

## Assumptions and scope
A set partition is noncrossing if no two distinct blocks contain four elements \(a<b<c<d\) with \(a,c\) in the first block and \(b,d\) in the second. Every set partition receives one unnormalized weight \(q^{C_1}\), with \(0^0=1\). For \(q>0\) all noncrossing partitions have positive probability; at \(q=0\), the state space is restricted to those with no singleton blocks. The normalizing polynomial is strictly positive for every \(q\ge0\). The conclusions cover exactly \(n\in\{5,6,7,8\}\); no assertion about a universal order cutoff is implied.

## Proof
For any nonnegative integer profile \(\mathbf r=(r_1,\ldots,r_n)\) with \(\sum_{j=1}^n j r_j=n\), write \(m=\sum_jr_j\). Kreweras's noncrossing block-profile enumeration gives exactly

\[
T_n(\mathbf r)=\frac{n!}{(n-m+1)!\prod_{j=1}^{n}r_j!}.
\]

This classical enumeration is taken from Arizmendi's statement of Kreweras's formula (Proposition 1.4 of the referenced paper); it is also verified independently by enumeration in the checker for the four orders here. Form the four integer polynomials

\[
\begin{aligned}
 Z_n(q)&=\sum_{\mathbf r}T_n(\mathbf r)q^{r_1},\\
 A_n(q)&=\sum_{\mathbf r}r_2T_n(\mathbf r)q^{r_1},\\
 B_n(q)&=\sum_{\mathbf r}r_3T_n(\mathbf r)q^{r_1},\\
 M_n(q)&=\sum_{\mathbf r}r_2r_3T_n(\mathbf r)q^{r_1}.
\end{aligned}
\]

Directly from normalized expectations,

\[
 \operatorname{Cov}_q(C_2,C_3)=\frac{M_n(q)Z_n(q)-A_n(q)B_n(q)}{Z_n(q)^2}=-\frac{nP_n(q)}{Z_n(q)^2}.
\]

For reproducibility, the following are **complete ascending coefficient vectors** for \(Z_n\) and \(P_n\): an array \((c_0,\ldots,c_d)\) denotes \(\sum_{j=0}^{d}c_jq^j\).

| \(n\) | coefficients of \(Z_n\) | coefficients of \(P_n\) |
|---|---|---|
| 5 | `(6,15,10,10,0,1)` | `(-1,5,0,40,0,19)` |
| 6 | `(15,36,45,20,15,0,1)` | `(21,60,30,145,15,200,0,45)` |
| 7 | `(36,105,126,105,35,21,0,1)` | `(-20,252,741,1190,560,1218,126,694,0,90)` |
| 8 | `(91,288,420,336,210,56,28,0,1)` | `(547,1442,3752,8939,10486,11424,4340,6174,581,1918,0,161)` |

All denominators are positive on \(q\ge0\), because the constant terms of all four \(Z_n\) are strictly positive and their remaining coefficients are nonnegative. Every coefficient of \(P_6\) and \(P_8\) is nonnegative, with positive constant term, so the corresponding covariances are strictly negative. Each of \(P_5\) and \(P_7\) has negative constant term, only nonnegative remaining coefficients, a positive linear coefficient, and positive leading coefficient. Thus each is strictly increasing for \(q\ge0\), starts negative, tends to positive infinity, and has exactly one positive real root. The covariance therefore has the claimed positive/zero/negative regimes. Exact rational substitution at \(q=1/20\) yields \(P_5(q)<0\), \(P_6(q)>0\), \(P_7(q)<0\), \(P_8(q)>0\), proving alternation.

## Verification
The standalone `verify.py` independently generates all set partitions of each size \(5\le n\le8\), rejects crossings by testing the defining four-index condition, accumulates the four moment polynomials using integer arithmetic, compares the resulting covariance numerator against the stated exact coefficient vectors, and independently compares every observed block-profile multiplicity to Kreweras's formula. It also evaluates seven rational fugacities, tests all polynomial identities, and checks the alternation at \(q=1/20\). Execution of the embedded program returned `VERIFIED 127 independent exact checks; alternating q=1/20 signs +,-,+,-`. The infinite continuum of fugacities is covered by the exact polynomial proof, not by the finite numerical tests.

## Relationship to prior work
Kargin (2019, arXiv:1907.00632v1, primary MSC 60C05) proved asymptotic normality and negative covariance for distinct block-size counts in *unweighted* noncrossing partitions. Kortchemski and Marzouk (2015, arXiv:1503.09174v1) studied general simply generated/Gibbs noncrossing partitions, with an asymptotic covariance formula for block-size frequencies (Theorem 16). Those established frameworks include the present weight model and provide important eventual-asymptotic context; the present claim is **only** the explicit finite-order sign diagram and its two algebraic fugacity thresholds. Arizmendi (2012, arXiv:1201.6576v1), reproducing Kreweras's formula, gives the general exact profile enumeration from which the finite moment polynomials can be computed; that underlying enumeration is not claimed as new.

## Limitations
Only the first four feasible orders are classified. There is no theorem here for all \(n\ge9\), no claim of new universal asymptotics, and no assertion of conditional independence or full negative association. A broader closed-form treatment of general Gibbs partition covariances, or an earlier tabulation of the same four finite sign diagrams, may subsume the novelty; independent historical and mathematical review has not been performed.

## References
1. V. Kargin, *Limit theorems for statistics of non-crossing partitions*, arXiv:1907.00632v1 (first posted July 1, 2019), https://arxiv.org/abs/1907.00632.
2. I. Kortchemski and C. Marzouk, *Simply generated non-crossing partitions*, arXiv:1503.09174v1 (2015), https://arxiv.org/abs/1503.09174.
3. O. Arizmendi, *Statistics of blocks in k-divisible non-crossing partitions*, arXiv:1201.6576v1 (2012), https://arxiv.org/abs/1201.6576; Proposition 1.4 reproduces Kreweras's block-profile enumeration.
