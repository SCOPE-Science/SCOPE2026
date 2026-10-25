# A three-block face forces sharp coordinatewise instability in bistochastic least-squares projection

## Finding

Let \(\mathcal B_n\) denote the \(n\times n\) doubly stochastic matrices, and let \(\Pi_n\) be nearest-point projection onto \(\mathcal B_n\) in Frobenius (Euclidean) distance. The matrix entrywise norm is \(\|X\|_{\max}=\max_{i,j}|X_{ij}|\); it is not the induced matrix row-sum norm. For every integer \(m\ge2\), define \(n=3m\) and the specific face support \(E_m\) below. At a strictly complementary observation whose projection belongs to the relative interior of this face, the derivative \(Q_m\) of \(\Pi_n\) has a distinguished output coordinate \(e\) with **exact, attained coordinatewise amplification**
\[
\sum_{f\in E_m}|(Q_m)_{e,f}|=\Lambda_m:=\frac{2(3m^2+m-1)}{(m+1)(m+2)}.
\]
In particular, there exist two strictly positive observation matrices \(X_m,X_m'\) realizing \(\|\Pi_n(X_m)-\Pi_n(X_m')\|_{\max}/\|X_m-X_m'\|_{\max}=\Lambda_m\); hence the global Lipschitz constant of \(\Pi_n\) for \(\|\cdot\|_{\max}\) is at least \(\Lambda_m\).

At any full-support projected matrix the derivative is the affine doubly-centering projection, whose sharp entrywise amplification is \(4(1-1/n)^2\). For every \(m\ge4\), the constructed proper-face amplification is strictly larger. The first such departure **within this three-block family** is at \(m=4\), hence \(n=12\):
\[
\Lambda_4=\frac{17}{5}>\frac{121}{36}=4(1-1/12)^2.
\]
Moreover \(\Lambda_m\longrightarrow6\), whereas the full-support amplification tends to \(4\). No claim is made that this is the global Lipschitz constant, or that twelve is the earliest possible dimension among *all* face supports.

## Assumptions and scope

Fix an integer \(m\ge2\), and identify both the row and column labels with \((r,k)\), where \(r\in\{0,1,2\}\) is read cyclically modulo three and \(0\le k<m\). The allowed support consists of three complete diagonal square blocks together with one cyclic successor matching from each block:
\[
E_m=\{((r,k),(r,\ell)):0\le r<3,\ 0\le k,\ell<m\}\ \cup\ \{((r,k),(r+1\pmod3,k)):0\le r<3,\ 0\le k<m\}.
\]
Each row and column has exactly \(m+1\) allowed entries. Consequently the matrix \(Y\), equal to \(1/(m+1)\) on \(E_m\) and zero elsewhere, belongs to \(\mathcal B_{3m}\) and is in the relative interior of the proper face \(F_m=\{Z\in\mathcal B_{3m}:Z_f=0\text{ for }f\notin E_m\}\). Let \(T_m\) be the real vector space of matrices supported on \(E_m\) with all row and column sums zero, and let \(Q_m\) be Frobenius orthogonal projection onto \(T_m\). The special output entry is \(e=((0,0),(1,0))\), an allowed successor-matching entry.

## Proof

**1. Realization of the local derivative.** Write \(\mathbf1_{E_m^c}\) for the matrix that is one outside the support and zero within it. The observation \(X=Y-\mathbf1_{E_m^c}\) projects to \(Y\): for any \(Z\in\mathcal B_{3m}\), \(\langle X-Y,Z-Y\rangle=-\sum_{f\notin E_m}Z_f\le0\). Strict positivity of the entries of \(Y\) on its support and the strictly negative multipliers off the support give an open cell of observations on which the active constraints are constant. On that cell \(\Pi_n\) agrees with the affine orthogonal projection onto the affine hull of \(F_m\), with linear part \(Q_m\). This can also be seen directly from the equality-constraint multipliers: for every small perturbation \(tH\) the candidate \(Y+tQ_mH\) stays positive on allowed entries, while the previously unit-size inactive-coordinate multiplier gaps remain positive for sufficiently small \(t\). Therefore \(\Pi_n(X+tH)=Y+tQ_mH\) for all sufficiently small \(t\) whenever \(H\) is supported on \(E_m\).

**2. Cycle-space projection.** Regard the allowed entries as oriented edges in a connected bipartite graph, with left vertices indexed by rows and right vertices by columns. For each edge \(f=(i,j)\), let its signed incidence vector be \(d_f=\mathbf e_{L(i)}-\mathbf e_{R(j)}\). If \(D\) has these columns, then \(T_m=\ker D\), and
\[
Q_m=I-D^{\mathsf T}(DD^{\mathsf T})^\dagger D.
\]
Let \(\phi\) be the dipole potential solving \(DD^{\mathsf T}\phi=d_e\), in the gauge \(\phi_{L(0,0)}=0\). With common denominator \(d=3m(m+1)(m+2)\), the following complete table gives the numerator \(d\phi\); the label \(k\ne0\) means any \(1\le k<m\):

| vertex group | \(k=0\) | \(k\ne0\) |
|:--|--:|--:|
| \(L(0,k)\) | \(0\) | \(-3m(m+1)\) |
| \(L(1,k)\) | \(-(5m+1)(m+1)\) | same |
| \(L(2,k)\) | \(-(4m-1)(m+1)\) | same |
| \(R(0,k)\) | \(-(3m^2+m-1)\) | same |
| \(R(1,k)\) | \(-m(8m+7)\) | \(-m(5m+4)\) |
| \(R(2,k)\) | \(-(2m+1)^2\) | same |

The table is verified by substituting into the Kirchhoff equation at each vertex: each left vertex has the \(m\) right neighbors in its own block and one right successor neighbor; each right vertex has \(m\) left neighbors in its own block and one left predecessor neighbor. The resulting Laplacian values are \(+1\) at \(L(0,0)\), \(-1\) at \(R(1,0)\), and zero at every other vertex. Connectivity makes the gauge-fixed solution unique. It follows, without any matrix pseudoinverse computation, that
\[
(Q_m)_{e,f}=\mathbf1_{f=e}-\bigl(\phi_{L(f)}-\phi_{R(f)}\bigr).
\]

**3. Exact absolute mass.** Set
\[
A_m=\frac{5m^2-2}{3(m+1)(m+2)},\qquad B_m=\frac{m}{3(m+1)}.
\]
Substituting the six rows of the potential table and splitting the \(3m(m+1)\) edges by their three internal blocks and three successor matchings gives the respective sums of absolute values
\[
\begin{array}{c|ccc}
& r=0&r=1&r=2\\ \hline
\text{internal block}&A_m&A_m&B_m\\
\text{successor matching}&A_m&B_m&B_m
\end{array}.
\]
This is a finite algebraic calculation, including the special diagonal term \(f=e\): specifically \((Q_m)_{e,e}=(3m^2+m-1)/(3(m+1)(m+2))>0\). The displayed table gives \(3A_m+3B_m=2(3m^2+m-1)/((m+1)(m+2))\), which is \(\Lambda_m\).

Choose \(H_f=\operatorname{sgn}((Q_m)_{e,f})\) on allowed entries (arbitrarily zero on any zero coefficient), and \(H_f=0\) outside. Since \(Q_m\) is symmetric, \(\|H\|_{\max}=1\) and \((Q_mH)_e=\Lambda_m\). The local projection identity from step 1 proves the finite-pair equality. Adding a sufficiently large scalar multiple of the all-ones matrix to both observations makes every observed coordinate strictly positive without affecting their projections: for doubly stochastic \(Z\), the quadratic objective under this shift changes by a \(Z\)-independent constant because \(\sum_{i,j}Z_{ij}=n\).

**4. Strict departure from the full-support benchmark.** For the interior affine doubly-centering projection \(A\mapsto (I-J/n)A(I-J/n)\), where \(J\) is the all-ones matrix, each row of its \(n^2\times n^2\) matrix is a tensor product of two rows of \(I-J/n\). Its sharp \(\|\cdot\|_{\max}\) amplification is therefore \([2(1-1/n)]^2=4(1-1/n)^2\). Direct subtraction, with \(n=3m\), yields
\[
\Lambda_m-4\left(1-\frac1{3m}\right)^2
=\frac{2(9m^4-33m^3-11m^2+18m-4)}{9m^2(m+1)(m+2)}.
\]
For \(m=4+t\) with integer \(t\ge0\), the polynomial in parentheses equals \(9t^4+111t^3+457t^2+650t+84>0\). The cases \(m=2,3\) are negative. Substituting \(m=4\) gives the stated strict gap \(7/180\); passage to the limit gives six versus four. This completes the proof.

## Verification

The standalone `verify.py` uses only Python's standard-library `fractions.Fraction`. It reconstructs all allowed edges, checks the six closed-form potential groups against every Kirchhoff equation for \(2\le m\le20\), computes the exact projected kernel row and six absolute-mass groups, and checks the factorized strict-gap identity. Additionally, for \(2\le m\le6\), it **independently** solves the grounded full bipartite Laplacian by rational Gaussian elimination and compares every potential. It checks 3,625 assertions. Run `python3 verify.py` next to this file. Finite tests corroborate; the all-integer theorem follows from the symbolic potential substitution and positive-coefficient polynomial identity, not an extrapolation from tests.

## Relationship to prior work

Paffenholz (2013, arXiv:1304.3948v1) studies face graphs of Birkhoff polytopes and explains their characterization by allowed bipartite support; those underlying geometric facts are not new here. Li, Sun, and Toh (2017, arXiv:1702.05934) derive general generalized-Jacobian formulas for Euclidean Birkhoff projectors; the cycle-space representation is an instance of this established projection calculus. Neither inspected text states the rational three-block amplification family \(\Lambda_m\), its explicit sign-extremizer, or its strict entrywise instability relative to full support beginning at the dimension-twelve member of this family. The additional contribution is the closed evaluation and dimension-uniform comparison, **not** the generic Jacobian identity.

A related independent analysis of contiguous cyclic-band supports yields a later within-band departure, but those band graphs differ from the present three-complete-block-plus-matching supports: the earlier band restriction does not imply the present nonband equality. Earlier Euclidean bi-stochastic approximation algorithms (Wang, Li, and König, 2010) also do not supply this worst-case coordinatewise perturbation ratio.

## Limitations

The theorem gives an exact local output-coordinate sensitivity on one specified support family, and hence a sharp attained **global lower bound**. It does not determine the global norm of every Birkhoff projection derivative, the maximum over all faces, or the first dimension of instability across arbitrary supports. The independent systematic search of the complete literature is not exhaustive: terminology in transportation and parametric polyhedral projections creates residual priority risk. No independent mathematical audit or external verification is claimed.

## References

1. Andreas Paffenholz, *Faces of Birkhoff Polytopes*, arXiv:1304.3948v1, publicly posted 2013-04-14, https://arxiv.org/abs/1304.3948.
2. Xudong Li, Defeng Sun and Kim-Chuan Toh, *On the efficient computation of a generalized Jacobian of the projector over the Birkhoff polytope*, arXiv:1702.05934, publicly posted 2017-02-20, https://arxiv.org/abs/1702.05934.
3. *Learning a Bi-Stochastic Data Similarity Matrix* (2010), https://fodava.gatech.edu/files/reports/FODAVA-10-11.pdf. Its symmetric constrained approximation problem differs from the present stability problem.
