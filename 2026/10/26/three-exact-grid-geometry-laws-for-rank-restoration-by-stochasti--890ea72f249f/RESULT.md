# Three exact grid-geometry laws for rank restoration by stochastic rounding

## Finding

A two-column matrix rounded independently into a common interval of two adjacent quantization levels admits an exact, nonasymptotic full-real-rank probability. There are precisely three distinct cases: a zero quantization level, opposite levels, and a generic pair of nonzero, nonopposite levels. The distinction persists in a rare-rounding critical window, even when rounding probabilities and entrywise noise variances are identical.

## Assumptions and scope

Fix an integer \(N\ge2\) and real \(L<U\), with spacing \(\rho=U-L>0\). Independently across all entries, let the rounded matrix \(B\in\mathbb R^{N\times2}\) have row \(i\) equal to \((U,L)\) with probability \(b_i\), \((L,U)\) with probability \(c_i\), \((L,L)\) with probability \(a_i\), and \((U,U)\) with probability \(d_i\), where
\[
a_i=(1-p_i)(1-q_i),\quad b_i=p_i(1-q_i),\quad c_i=(1-p_i)q_i,\quad d_i=p_iq_i,
\]
and \(0\le p_i,q_i\le1\). This is unbiased stochastic rounding of input entries \(L+\rho p_i\) and \(L+\rho q_i\). Rank is taken over the real numbers, in exact arithmetic.

## Proof

**Zero level.** First take \(L=0\). Every rounded row lies in \(\{(0,0),(\rho,0),(0,\rho),(\rho,\rho)\}\). Rank is below two precisely when all rows lie in one of the three lines through the origin spanned by the last three nonzero row types. These events have probabilities \(\prod_i(a_i+b_i)\), \(\prod_i(a_i+c_i)\), and \(\prod_i(a_i+d_i)\). Every pairwise intersection and the triple intersection consist of the all-zero matrix, of probability \(\prod_i a_i\). Inclusion–exclusion gives
\[
\Pr(\operatorname{rank}B=2)=1-\prod_i(a_i+b_i)-\prod_i(a_i+c_i)-\prod_i(a_i+d_i)+2\prod_i a_i.
\]
If \(U=0\), interchange the two endpoints, equivalently substitute \(1-p_i\) and \(1-q_i\) for \(p_i\) and \(q_i\).

**Opposite levels.** Suppose \(L=-U\ne0\). The four possible rows occupy precisely two distinct lines: \((L,L)\), \((U,U)\) are diagonal and \((U,L)\), \((L,U)\) are antidiagonal. No row is zero, so rank is below two exactly when all rows lie on the same one of these two lines. Thus
\[
\Pr(\operatorname{rank}B=2)=1-\prod_i(a_i+d_i)-\prod_i(b_i+c_i).
\]

**Generic nonzero levels.** Suppose \(LU\ne0\) and \(L\ne-U\). The diagonal rows \((L,L)\), \((U,U)\) remain collinear, while the rows \((U,L)\) and \((L,U)\) lie on two distinct lines, each different from the diagonal. Their mutual determinant is \(U^2-L^2\ne0\); the determinant between a diagonal row and an offdiagonal row is a nonzero multiple of \(L(U-L)\) or \(U(U-L)\). Accordingly the three disjoint rank-deficiency events are: every row is diagonal, every row is exactly \((U,L)\), or every row is exactly \((L,U)\). Independence gives
\[
\Pr(\operatorname{rank}B=2)=1-\prod_i(a_i+d_i)-\prod_i b_i-\prod_i c_i.
\]
These cases exhaust all \(L<U\). They remain valid when some row probabilities vanish.

**Sharp rare-rounding window.** Suppose \(p_i=q_i=r_N=\alpha/N\) with fixed \(\alpha>0\) and sufficiently large \(N\). The unrounded matrix is constant-row and has rank one for each \(N\) unless its entry itself vanishes. In the zero-lower-level case, the exact formula simplifies to
\[
1-2(1-r_N)^N-(1-2r_N+2r_N^2)^N+2(1-r_N)^{2N},
\]
which tends to \((1-e^{-\alpha})^2\). In the opposite-level case it becomes
\[
1-(1-2r_N+2r_N^2)^N-(2r_N-2r_N^2)^N;
\]
in the generic case it becomes
\[
1-(1-2r_N+2r_N^2)^N-2[r_N(1-r_N)]^N.
\]
Both tend to \(1-e^{-2\alpha}\). The strict difference is \(2e^{-\alpha}(1-e^{-\alpha})>0\). All three cases have identical rounding variance \(\rho^2r_N(1-r_N)\) when their spacing \(\rho\) is the same. For \(N=2\), \(r=1/4\), substitution gives the exact values \(15/128\), \(15/32\), and \(69/128\) for \([0,\rho]\), \([-\rho/2,\rho/2]\), and \([\rho,2\rho]\), respectively. Each corresponding input has rank one.

**Dependence boundary.** When \(p_i=q_i\), using the same uniform random number to round both entries of each row forces the two rounded columns to coincide in every realization, hence prevents rank two. This contrasts with independent entry rounding and uses the same one-entry marginals.

## Verification

The standalone `verify_rank.py` enumerates all \(4^N\) possible rounded row strings for small \(N\), tests real rank using exact integer/rational determinants, and independently compares with the three product laws. It also checks nonidentical row probabilities and rare-rounding limits. It passed 827 checks in the accompanying exact-arithmetic test suite. The analytic proof above is exhaustive for arbitrary \(N\); finite computations do not establish that universality.

## Relationship to prior work

Ma, Yu and Drineas (2026) study stochastic rounding as a spectral regularizer for rectangular matrices, proving high-probability smallest-singular-value bounds under variance and dimension assumptions. Dexter and coauthors (2024/2025) establish earlier high-probability full-rank regularization in tall-and-thin matrices. These results motivate quantifying rank-restoration probabilities but do not yield the three case-by-case exact finite-sample laws or their rare-variance phase contrast. The classical fair binary-matrix rank formula is subsumed at one special parameter value; that fair case is not claimed as novel.

## Limitations

This concerns exactly two columns whose entries share one adjacent pair of quantization levels; it is not a general finite-bit or multicolumn rank law. The formulas classify zero versus nonzero rank, not the sizes of nonzero singular values. The model assumes independent entrywise rounding except for the explicitly contrasting shared-randomness example. An equivalent earlier probability formula may exist in the literature on low-dimensional random discrete matrices.

## References

1. Linkai Ma, Tingzhou Yu, and Petros Drineas, *Stochastic Rounding Increases Small Singular Values*, arXiv:2606.00312v1, first posted 2026-05-29, Sections 1.1–3 and Appendix A.
2. Gregory Dexter, Christos Boutsikas, Linkai Ma, Ilse C. F. Ipsen, and Petros Drineas, *Stochastic Rounding Implicitly Regularizes Tall-and-Thin Matrices*, arXiv:2403.12278, first posted 2024-03-18; SIAM J. Matrix Anal. Appl. 46 (2025), 341–369.
3. C. Cooper, *On the distribution of rank of a random matrix over a finite field*, Random Structures & Algorithms 17 (2000), 197–212. Background on random finite-field rank distributions; it is not asserted to contain the present quantizer laws.
