# Unique hub-star minimum for reversible multigroup epidemic risk

## Finding

Consider at least three equally represented epidemiological groups whose transmission matrix satisfies reciprocal contact balance. If one group's known total contact rate is at least the sum of all other group totals, then the **unique** arrangement with the smallest basic reproduction number sends every peripheral group's contacts to that dominant group and leaves a self-contact remainder only at the dominant group.

More precisely, let \(m\ge2\), \(L_1,\ldots,L_m>0\), and \(H\ge\sum_{i=1}^m L_i\). Put
\[
h=H-\sum_{i=1}^mL_i,\qquad
Q=\sum_{i=1}^mL_i^2,\qquad
\Lambda=\frac{h+\sqrt{h^2+4Q}}2.
\]
Let \(\mathcal{C}(H,L)\) consist of all symmetric, entrywise-nonnegative, real \((m+1)\)-by-\((m+1)\) matrices \(M\) with row sums \((H,L_1,\ldots,L_m)\). Indices range from \(0\) to \(m\). Every such matrix represents a next-generation matrix satisfying detailed balance when each of the \(m+1\) groups has the same population fraction.

Define the **hub-star** matrix \(M_\star\) by
\[
(M_\star)_{00}=h,\qquad
(M_\star)_{0i}=(M_\star)_{i0}=L_i\ (1\le i\le m),
\]
with every other entry zero. Then
\[
\boxed{\min_{M\in\mathcal{C}(H,L)}\rho(M)=\Lambda,
\quad\text{with equality if and only if } M=M_\star.}
\]

The minimum has a quantitative uniqueness certificate. For every admissible \(M\),
\[
\boxed{
\rho(M)-\Lambda\ \ge\
\frac{\displaystyle \sum_{i=1}^m M_{ii}(\Lambda-L_i)^2
 +2\sum_{1\le i<j\le m}M_{ij}(\Lambda-L_i)(\Lambda-L_j)}{\Lambda^2+Q}.}
\]
Writing \(\delta=\Lambda-\max_iL_i>0\) and \(T_{\rm per}=\sum_{i,j=1}^m M_{ij}\), it follows that
\[
\rho(M)-\Lambda\ge\frac{\delta^2}{\Lambda^2+Q}\,T_{\rm per}.
\]
Thus *all* within-peripheral contact mass is penalized by an explicit positive spectral margin.

As a sharp threshold consequence, some admissible balanced transmission matrix has basic reproduction number at most one exactly when
\[
\boxed{h+Q\le1.}
\]
At the boundary \(h+Q=1\), only \(M_\star\) attains the threshold.

## Assumptions and scope

The group index is \(\{0,1,\ldots,m\}\) with \(m\ge2\). Group \(0\) is the dominant-contact group; the remaining \(m\) groups are peripheral. Every peripheral row sum is strictly positive. The hub row sum satisfies \(H\ge\sum_iL_i\); equality is allowed and gives \(h=0\). All matrix entries are nonnegative; diagonal terms and structural zeros are allowed. No fixed sparsity pattern is imposed on competing matrices. The groups have equal population proportions, so reciprocal contact balance \(\pi_iM_{ij}=\pi_jM_{ji}\) is equivalent to symmetry.

The conclusion concerns the spectral radius of a nonnegative next-generation matrix, i.e. the initial reproduction threshold. No claim is made about final epidemic size, stochastic extinction probability, or interventions' implementation costs. Unequal group proportions and row totals outside the dominant-contact regime are not covered.

## Proof

**Existence and the candidate eigenvalue.** The row sums of \(M_\star\) are \((H,L_1,\ldots,L_m)\) by construction, and its nonnegative off-diagonal star is irreducible because each \(L_i>0\). The defining equation for \(\Lambda\) is
\[
\Lambda^2-h\Lambda-Q=0.
\]
Consequently the strictly positive vector
\[
v=(\Lambda,L_1,\ldots,L_m)^\mathsf{T}
\]
satisfies \(M_\star v=\Lambda v\): its center coordinate is \(h\Lambda+Q=\Lambda^2\), and the \(i\)-th leaf coordinate is \(L_i\Lambda\). Perron–Frobenius or the nonnegative symmetric Rayleigh principle therefore gives \(\rho(M_\star)=\Lambda\).

**Fixed-row-sum quadratic identity.** For any symmetric matrix \(M\) with row sums \(r_i\) and any real vector \(x\),
\[
x^\mathsf{T}Mx=\sum_{i=0}^m r_i x_i^2
 -\sum_{0\le i<j\le m}M_{ij}(x_i-x_j)^2.
\]
To prove the identity, expand the squares and use symmetry to collect at coordinate \(i\) the diagonal contribution \(M_{ii}\) and all off-diagonal row contributions \(M_{ij}\). For the hub-star matrix, the only off-diagonal terms are the hub–leaf edges of weight \(L_i\).

Write \(d_i=M_{ii}\) for each leaf and \(e_{ij}=M_{ij}\) for distinct leaves. The prescribed leaf row sums enforce
\[
M_{0i}=L_i-d_i-\sum_{j\ne i,\ j\ge1} e_{ij}.
\]
Consequently the quadratic identity, evaluated at the common vector \(v\), gives the exact, not asymptotic, difference
\[
 v^\mathsf{T} Mv-v^\mathsf{T}M_\star v
 =\sum_{i=1}^m d_i(\Lambda-L_i)^2
   +2\sum_{1\le i<j\le m}e_{ij}(\Lambda-L_i)(\Lambda-L_j).
\]
This also follows directly by noting that adding a leaf self-loop shifts its corresponding hub–leaf mass to the center self-loop, while adding a leaf–leaf edge shifts both associated hub–leaf masses to the center self-loop.

**Sign and sharpness.** Because \(m\ge2\) and every \(L_i>0\), we have \(Q>L_i^2\) for each leaf. Also \(\Lambda^2=h\Lambda+Q\ge Q\), whence \(\Lambda>L_i\) for every \(i\). Thus all coefficients on the right of the exact difference identity are strictly positive. For symmetric nonnegative \(M\), its spectral radius equals its largest real eigenvalue, so Rayleigh–Ritz gives
\[
\rho(M)\ge\frac{v^\mathsf{T}Mv}{v^\mathsf{T}v}
=\Lambda+\frac{v^\mathsf{T} Mv-v^\mathsf{T}M_\star v}{\Lambda^2+Q}.
\]
This is the claimed quantitative bound. Equality in the minimum forces every \(d_i\) and every \(e_{ij}\) to vanish. The row-sum constraints then force \(M=M_\star\), showing uniqueness among all admissible matrices, even reducible ones. Conversely the star attains the bound. Replacing every \(\Lambda-L_i\) by its positive minimum \(\delta\) gives the simplified stability bound using \(T_{\rm per}\).

**Critical epidemic threshold.** The positive root \(\Lambda\) of \(z^2-hz-Q=0\) satisfies \(\Lambda\le1\) if and only if \(1-h-Q\ge0\): since \(h,Q\ge0\), the quadratic has precisely one positive root and is strictly increasing above that root. Since the hub star is admissible and minimizes the spectral radius, some admissible matrix has \(\rho(M)\le1\) exactly when \(h+Q\le1\). If \(h+Q=1\), uniqueness of the minimizer proves that no other matrix is at or below threshold.

## Verification

A standalone standard-library Python script, `verify.py`, checks the fixed-row-sum and symmetry constraints; the exact Rayleigh difference identity with rational data represented symbolically in the quadratic field \(\mathbb Q(\Lambda)\) modulo \(\Lambda^2=h\Lambda+Q\); and independent symmetric-matrix eigenvalue calculations. Across 495 deterministic finite cases (including dimensions three through seven), every exact identity and numerical spectral inequality passed. These tests illustrate the identities; the preceding argument proves them for every admissible dimension and every real parameter in scope.

One exact three-group example is
\[
L_1=L_2=\tfrac25,\quad H=\tfrac{37}{25},\quad
h=\tfrac{17}{25},\quad Q=\tfrac8{25},\quad\Lambda=1.
\]
The optimal matrix is
\[
M_\star=\begin{pmatrix}
17/25&2/5&2/5\\ 2/5&0&0\\2/5&0&0
\end{pmatrix}.
\]
At the same row sums, the matrix
\[
M=\begin{pmatrix}
22/25&3/10&3/10\\3/10&0&1/10\\3/10&1/10&0
\end{pmatrix}
\]
has \(\rho(M)-1\ge3/55>0\). This illustrates both uniqueness and the epidemic threshold despite the dominant row sum exceeding one.

To reproduce the finite checks, use `python3 verify.py`. No external data files or third-party packages are required.

## Relationship to prior work

Bizzotto, Ball, and Britton [1] pose the partly known next-generation-matrix problem, prove a general detailed-balance lower bound in Theorem 3.2, give a sharp analytic answer for two types in Theorem 3.6, and formulate a semidefinite optimization recipe for general dimensions in Appendix 8.1. Their explicit lower bound is not sharp in general and their higher-dimensional recipe does not supply the closed-form dominant-row solution or the strict penalty for peripheral contact mass established here. The present result solves a natural *multi-type* subfamily of their problem; it does not purport to solve every detailed-balance matrix problem.

Engel, Schneider, and Sergeev [2] study eigenvalue ranges for nonnegative matrices with prescribed row sums and graph patterns, without the symmetry constraint central here. Xing and Zhou [3] derive entry-sensitive general spectral inequalities but do not establish this simultaneous constrained minimizer. Standard Rayleigh–Ritz and Perron–Frobenius facts are used, not claimed as novel.

## Limitations

The hub dominance assumption \(H\ge\sum_i L_i\) is sufficient for the star to be feasible and is not asserted necessary for an analytic solution in another regime. Peripheral row sums are strictly positive; zero rows and the two-group case are deliberately excluded from the strict uniqueness statement. The theorem assumes equal group proportions. General unequal proportions yield a diagonally symmetrizable rather than literally symmetric matrix and require separate analysis. The result describes the initial reproduction threshold and does not calculate outbreak size or assert nonlinear epidemic extinction at equality.

The algebra is exact, but originality remains subject to potentially unindexed prior work on symmetric nonnegative fixed-row-sum optimization and the spectral characterization of weighted stars. A general-purpose semidefinite formulation alone does not state the present closed-form optimum or defect bound.

## References

[1] A. Bizzotto, F. Ball, and T. Britton, *Bounds on \(R_0\) and final epidemic size when the next-generation matrix \(M\) is only partially known*, arXiv:2602.23885, first publicly submitted 2026-02-27. https://arxiv.org/abs/2602.23885 ; full revised text: https://arxiv.org/html/2602.23885v2.

[2] G. M. Engel, H. Schneider, and S. Sergeev, *On sets of eigenvalues of matrices with prescribed row sums and prescribed graph*, arXiv:1312.2782 (2013). https://arxiv.org/html/1312.2782v1.

[3] R. Xing and B. Zhou, *Bounds for the spectral radius of nonnegative matrices*, arXiv:1309.5604 (2013). https://arxiv.org/html/1309.5604v1.
