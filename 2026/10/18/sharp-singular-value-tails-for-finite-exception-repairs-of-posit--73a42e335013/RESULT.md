# Sharp singular-value tails for finite-exception repairs of positive norm-attaining operators

## Finding
Let \(H\) be a separable infinite-dimensional complex Hilbert space, let \(c>0\), and let \(D=cI+K\geq0\), where \(K=K^*\) is compact. Put \(Q=(cI-D)_+\), and denote its nonincreasing eigenvalues, with multiplicities and zeros appended, by \(\kappa_1\geq\kappa_2\geq\cdots\geq0\). A positive operator belongs to \(\beta(H)\) if its restriction to every nonzero reducing subspace attains its norm.

For any positive \(B\in\beta(H)\) with \(B-D\) compact, the subspace \(E_B([0,c))H\) has finite dimension \(r\); moreover, simultaneously for every integer \(n\geq1\),
\[
s_n(B-D)\geq\kappa_{r+n}.
\]
For every integer \(m\geq0\) one explicit operator \(B_m\) attains all these inequalities at once for the class with \(r\leq m\): take an orthonormal eigenbasis \(u_j\) for the strictly positive eigenvalues of \(Q\), listed with multiplicities, and set
\[
B_m=D+\sum_{j>m}\kappa_j\langle\,\cdot\,,u_j\rangle u_j.
\]
Then \(B_m\geq0\), \(B_m\in\beta(H)\), \(\dim E_{B_m}([0,c))H\leq m\), and
\[
s_n(B_m-D)=\kappa_{m+n}\quad(n\geq1).
\]
Consequently the entire lower singular-value envelope, as well as every Schatten-error quasi-norm for \(0<p<\infty\), is minimized simultaneously:
\[
\inf_{\substack{B\geq0,\ B\in\beta(H),\ B-D\text{ compact}\\ \dim E_B([0,c))H\leq m}}\|B-D\|_{\mathcal S_p}^p
=\sum_{j>m}\kappa_j^p,
\]
with the convention that the value can be infinite. In particular, a positive \(\beta(H)\)-repair at Schatten order \(p\), meaning \(B-D\in\mathcal S_p\), exists **if and only if** \(Q\in\mathcal S_p\). If \(Q\in\mathcal S_p\) has infinite rank, repairs have arbitrarily small Schatten \(p\)-quasi-norm, but the zero distance is not attained. If \(Q\) has finite rank, \(D\in\beta(H)\) and the zero distance is attained.

## Assumptions and scope
The space is complex, separable, and infinite-dimensional. The operator \(D\) is positive and differs by a self-adjoint compact operator from a fixed positive scalar \(cI\). The competitors \(B\) are positive, lie in \(\beta(H)\), and differ compactly from \(D\); no commutation between \(B\) and \(D\) is assumed. Here \(E_B\) denotes the spectral resolution, \(s_n\) the singular values of a compact operator in nonincreasing order, and \((A)_+\) the positive part of a self-adjoint operator. Finite-rank \(Q\) uses zero-padding of \(\kappa_j\). Schatten classes with \(0<p<1\) have their standard quasi-norm meaning.

## Proof
**Finite subthreshold multiplicity.** Because \(B-D\) and \(D-cI\) are compact, \(B-cI\) is compact self-adjoint. Its spectrum below \(c\) consists of isolated eigenvalues of finite multiplicity, possibly increasing to \(c\). If infinitely many such eigenvalues existed, an infinite strictly increasing subsequence would violate the positive \(\beta(H)\) spectral criterion: a positive \(\beta(H)\) operator has no strictly increasing sequence of eigenvalues (Golla–Osaka–Sequeira, Theorem 2.2). Hence \(r:=\dim E_B([0,c))H<\infty\).

**Noncommuting singular-value lower bound.** Fix \(m=r\) and \(n\geq1\). If \(\kappa_{m+n}=0\), the assertion is immediate. Otherwise let \(N\) be the span of \(m+n\) orthonormal eigenvectors of \(Q\) corresponding to the largest \(m+n\) eigenvalues. This lies in the negative spectral subspace of \(K\), so \(D|_N=cI-Q|_N\) and \(\langle Qx,x\rangle\geq\kappa_{m+n}\|x\|^2\) for \(x\in N\). Put \(M=E_B([c,\infty))H\). Its codimension is \(m\), so \(\dim(N\cap M)\geq n\). Every \(x\in N\cap M\) satisfies
\[
\langle(B-D)x,x\rangle=\langle(B-cI)x,x\rangle+\langle Qx,x\rangle\geq\kappa_{m+n}\|x\|^2.
\]
For the compact self-adjoint operator \(B-D\), the positive-eigenvalue min–max principle therefore supplies at least \(n\) positive eigenvalues of size at least \(\kappa_{m+n}\). Consequently \(s_n(B-D)\geq\kappa_{m+n}\). This argument applies to arbitrary noncommuting \(B\).

**Simultaneous sharpness.** The spectral subspaces of \(K\) with positive and negative eigenvalues are orthogonal. The operator \(B_m\) leaves all nonnegative spectral components unchanged, retains the first \(m\) negative eigenvalues of \(K\), and clips every remaining negative eigenvalue to zero. Since \(D\geq0\), all retained eigenvalues are nonnegative. The spectrum of \(B_m\) below \(c\) has at most \(m\) eigenvalues counted with multiplicity, while all eigenvalues above \(c\) can accumulate only downwards to \(c\). Its spectral resolution is pure point (including the clipped \(c\)-eigenspace), so the same positive \(\beta(H)\) criterion proves \(B_m\in\beta(H)\). Its error is the positive compact tail \(\sum_{j>m}\kappa_j\langle\cdot,u_j\rangle u_j\), with singular values exactly \(\kappa_{m+n}\). For a competitor with \(r\leq m\), monotonicity of the \(\kappa_j\) gives \(s_n(B-D)\geq\kappa_{r+n}\geq\kappa_{m+n}\). Summing \(p\)-th powers proves the Schatten formula, including the value \(+\infty\).

**Repair threshold and attainment.** If some positive \(B\in\beta(H)\) has \(B-D\in\mathcal S_p\), its finite \(r\) and the singular-value bound force \(\sum_{j>r}\kappa_j^p<\infty\), equivalently \(Q\in\mathcal S_p\). Conversely, if \(Q\in\mathcal S_p\), the clipped \(B_0=D+Q\) is an admissible repair with \(B_0-D=Q\). The tails for \(B_m\) tend to zero in \(\mathcal S_p\). If \(Q\) has infinitely many positive eigenvalues, the eigenvalues of \(D\) below \(c\) form a strictly increasing sequence tending to \(c\), so \(D\notin\beta(H)\); thus zero error cannot be attained. If \(Q\) has finite rank, \(D\) itself satisfies the pure-point, well-ordered criterion and attains zero error.

## Verification
A standalone deterministic Python program, `verify.py`, checks the exact finite-dimensional clipping singular-value identities and the noncommuting inequality on 27 positive-matrix configurations of sizes 8, 12, and 20. All diagnostics passed. They serve only as supplementary tests. The proof above establishes the infinite-dimensional assertions by spectral decomposition and min–max; no finite enumeration is taken as a universal proof.

## Relationship to prior work
Golla, Osaka, and Sequeira (2026), Theorem 2.2, give the positive \(\beta(H)\) eigenvalue well-ordering criterion used here; the criterion itself is not new. Pandey and Paulsen established the scalar-plus-positive-compact-plus-finite-rank structure of positive absolutely norm attaining operators, and Doust gave a related spectral reformulation. Published work on positive \(\beta(H)\) operator-norm distance gives a different, operator-norm approximation question. Bala and Golla (2026) study Schatten perturbations of scalar multiples of partial isometries, rather than the finite-exception positive \(\beta(H)\) repair envelope. The proposed contribution here is the simultaneous, all-ranks singular-value bound for **noncommuting** competitors, its attained finite-exception optimizers, and the exact one-sided Schatten repair threshold. No assertion is made that generic compact clipping or finite-rank spectral truncation is new.

## Limitations
Only positive scalar-plus-compact source operators and positive compact-difference competitors are covered. No analogous claim is proved for arbitrary normal or nonnormal operators, noncompact differences, or other norm-attainment classes. The positivity of \(D\) and \(c>0\) are used. The main comparison with Bala–Golla and Su–Zhang (2026) is based on accessible abstracts because their full texts were not available; this leaves a specific priority risk, though no inspected source gives the whole theorem. Independent expert assessment and literature-priority verification have not been performed.

## References
1. R. Golla, H. Osaka, S. S. Sequeira, *Quasinormal and hyponormal operators in the \(\beta(H)\)-class*, arXiv:2610.13490v1, first posted 2026-10-09, Theorem 2.2. https://arxiv.org/html/2610.13490v1
2. S. K. Pandey and V. I. Paulsen, *A spectral characterization of \(\mathcal{AN}\) operators*, arXiv:1501.05869 and Journal of the Australian Mathematical Society 102 (2017), Theorem 5.11.
3. I. Doust, *A note on positive \(\mathcal{AN}\) operators*, arXiv:1810.08286 (2018).
4. N. Bala and R. Golla, *Spectral Characterizations of Schatten-class perturbations of Partial isometries*, arXiv:2607.15222v1, first posted 2026-07-16 (abstract inspected; full text unavailable).
5. Z. Su and Y. Zhang, *The Stability and Density of Norm Attaining Operators on Reducing Subspaces*, arXiv:2609.37621v1, first posted 2026-09-29 (abstract inspected; full text unavailable).
