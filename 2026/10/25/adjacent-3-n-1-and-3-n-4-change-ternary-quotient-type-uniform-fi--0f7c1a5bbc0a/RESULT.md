# Adjacent \(3^n+1\) and \(3^n+4\) change ternary quotient type: uniform five-term local denominators

## Finding
Let \(\mathcal N\) consist of integer polynomials with coefficients in \(\{0,1\}\) and constant coefficient \(1\). A representation \(m=P(3)/Q(3)\) with \(P,Q\in\mathcal N\) is *universal* when \(Q\mid P\) in \(\mathbb Z[x]\), and *local* otherwise. For **every** integer \(n\ge5\), the number \(m_n=3^n+4\) has both a trivial universal representation and an explicitly constructed local representation. The local representation always has exactly nine numerator powers of three and five denominator powers, independent of \(n\).

Explicitly, put
\[
Q_n(x)=1+x^2+x^{n-1}+x^n+x^{n+1},
\]
\[
P_n(x)=1+x+x^2+x^3+x^{n-1}+x^{n+3}
+x^{2n-1}+x^{2n}+x^{2n+1}.
\]
Then \(P_n,Q_n\in\mathcal N\), \(P_n(3)=(3^n+4)Q_n(3)\), and \(Q_n\nmid P_n\) in \(\mathbb Z[x]\). In contrast, the previously established only-universal theorem for \(3^n+1\) applies to the immediately preceding value congruent to \(1\pmod 3\). Thus the smallest positive admissible increment, namely \(3\), crosses from exclusively universal to mixed universal/local representations for all \(n\ge5\).

## Assumptions and scope
The exponent parameter is an arbitrary integer \(n\ge5\); there is no upper bound, primality condition, or limiting qualifier. A polynomial in \(\mathcal N\) has finitely many monomials, every nonzero coefficient is exactly one, and the constant coefficient equals one. The adjective *local* refers exclusively to the polynomial divisibility test in \(\mathbb Z[x]\), not to \(p\)-adic locality. The only-universal comparison for \(3^n+1\) is established prior literature; the new assertion is the uniform local construction for \(3^n+4\).

## Proof
For \(n\ge5\) the numerator exponents
\[
0,1,2,3,n-1,n+3,2n-1,2n,2n+1
\]
are pairwise distinct: \(n-1\ge4\), while \(2n-1\ge n+4\). The five denominator exponents \(0,2,n-1,n,n+1\) are likewise pairwise distinct. Hence \(P_n,Q_n\) are admissible Newman polynomials with exactly nine and five nonzero coefficients.

Multiplying in \(\mathbb Z[x]\) gives the **coefficient identity**
\[
\begin{aligned}
(x^n+x+1)Q_n(x)
={}&1+x+x^2+x^3+x^{n-1}\\
&+3x^n+2x^{n+1}+2x^{n+2}\\
&+x^{2n-1}+x^{2n}+x^{2n+1}.
\end{aligned}
\]
At \(x=3\), the three consecutive middle terms coalesce by ordinary base-three carrying:
\[
3\cdot3^n+2\cdot3^{n+1}+2\cdot3^{n+2}
=(3+6+18)3^n=3^{n+3}.
\]
Consequently \((3^n+4)Q_n(3)=P_n(3)\) exactly. On the other hand \(Q_n(1)=5\) and \(P_n(1)=9\). If \(Q_n\mid P_n\) in \(\mathbb Z[x]\), then evaluation of the integer quotient polynomial at \(1\) would give \(P_n(1)/Q_n(1)\in\mathbb Z\), contradicting \(9/5\notin\mathbb Z\). So this representation is local.

Finally, \(m_n=3^n+3+1\) belongs to \(\mathcal N\) when evaluated at \(3\): \((x^n+x+1)(3)=m_n\). Choosing numerator \(x^n+x+1\) and denominator \(1\) gives a trivial universal representation. Both types therefore occur for every \(n\ge5\). The result of Anders--Dawsey--Reznick--Sisneros-Thiry that \(3^n+1\) admits only universal representations supplies the adjacent-value comparison; no new proof of that earlier theorem is claimed.

## Verification
A standalone Python 3 standard-library verifier accompanies this result. It constructs both exponent sets, verifies pairwise disjointness, reconstructs the uncarried product coefficient-by-coefficient, and performs the exact integer identity for each \(5\le n\le204\), together with the divisibility obstruction \(5\nmid9\). The script prints `VERIFIED` on success. These finite tests corroborate the symbols but are not used to infer the theorem for unbounded \(n\); the preceding coefficient identity and evaluation argument are the complete proof.

## Relationship to prior work
Anders, Dawsey, Reznick, and Sisneros-Thiry (2023) introduce the precise universal/local dichotomy in Definition 1.1. Their Theorem 2.4(1) shows that \(3^n+1\) can have only universal representations. Their Example 1.3 gives a mixed representation for \(31=3^3+4\), and their Section 4 table records the mixed type at \(247=3^5+4\). Neither isolated computation nor the source's four only-universal families implies that every \(3^n+4\), \(n\ge5\), has a local certificate with fixed support sizes. The displayed formula supplies the missing uniform construction.

A later study by Idris and Sac-Épée (2026) concerns polynomial divisors of Newman polynomials and Mahler measure rather than numeric ternary quotients with a prescribed evaluation. A previously accessible, distinct claim classifies all ternary quotient representations of the single value \(289\) as universal; it neither covers the present infinite family nor is challenged by it. Searches for equivalent constructions, the family \(3^n+4\), and digit-sparse local quotients did not identify a stronger covering result. This is a best-knowledge comparison, not a priority certification.

## Limitations
This is an existence and uniform sparsity theorem. It does not establish minimality of the nine or five monomial counts, classify all representations of \(3^n+4\), extend to arbitrary bases, or characterize every mixed-type integer. No independent mathematical audit has been performed. Earlier unindexed examples, generalized insertion identities, or unpublished results could reduce the originality of the uniform formula.

## References
1. K. Anders, M. L. Dawsey, B. Reznick, S. Sisneros-Thiry, *Representations of integers as quotients of sums of distinct powers of three*, arXiv:2308.07252 (first posted 14 August 2023), especially Definition 1.1, Theorem 2.4(1), Example 1.3, Section 4, and Section 5. https://arxiv.org/abs/2308.07252
2. M. Idris and J.-M. Sac-Épée, *Algorithmic aspects of Newman polynomials and their divisors*, arXiv:2601.11486 (2026), especially the introduction and divisibility problem statement. https://arxiv.org/abs/2601.11486
