# Exact diagonal preconditioning of a rank-one update: a sharp dominant-coordinate transition

## Finding

Let \(n\geq2\), let \(u\in\mathbb R^n\), and set \(A=I_n+uu^{\mathsf T}\). For each positive diagonal matrix \(P\), denote the spectral condition number of \(P^{-1/2}AP^{-1/2}\) by \(\kappa(P)\). Put
\[
S=\sum_{i=1}^n u_i^2,\qquad M=\max_i u_i^2,\qquad R=S-M.
\]
If \(S=0\), the minimum is \(1\) and \(P=I_n\) attains it. If \(S>0\), the **exact global minimum over all independent positive diagonal entries** is
\[
\min_{P\succ0\,\mathrm{diagonal}}\kappa(P)=
\begin{cases}
1+S,&M\leq R,\\[2mm]
\dfrac{1+\rho}{1-\rho},&M>R,
\end{cases}
\qquad
\rho=\sqrt{\frac{MR}{(1+M)(1+R)}}.
\]
The matrix \(P=I_n\) is optimal **if and only if** \(M\leq S/2\) (apart from the trivial \(S=0\) case, where it is also optimal). If \(M>R\), select the unique index \(j\) with \(u_j^2=M\). An optimal diagonal preconditioner is
\[
P_*=\operatorname{diag}(p_1,\ldots,p_n),\quad
p_j=\frac{1+M}{1+R},\quad p_i=1\ (i\neq j).
\]
Hence, even though all \(n\) diagonal entries are independently adjustable, **changing one coordinate is sufficient for global optimality**, and changing none is optimal precisely when no squared coordinate exceeds the sum of the others. The formulas agree continuously at \(M=R\), where \(\rho=M/(1+M)\) and \((1+\rho)/(1-\rho)=1+2M\).

As an explicit failure of diagonal normalization as an automatic improvement rule, for \(u=(1/2,1,1,1)^{\mathsf T}\), no scaling is best, with \(\kappa(I)=17/4\). The Jacobi choice \(P=\operatorname{diag}(A)\) instead yields \(\kappa(P)=3+\sqrt{11/5}>17/4\).

## Assumptions and scope

The matrix \(A\) is a real, symmetric positive-definite identity plus a *positive* rank-one update. Its entries need not be nonnegative: arbitrary signs of \(u_i\) are allowed. The admissible transformations are symmetric positive diagonal congruences \(P^{-1/2}AP^{-1/2}\); the objective is the ratio of the largest to the smallest positive eigenvalue. A common positive scaling of \(P\) changes no condition number. The result covers zero coordinates and all threshold equalities. It does not describe unrestricted nonsymmetric two-sided scalings, general diagonal backgrounds other than a scalar multiple of the identity, higher-rank updates, or actual runtime of iterative methods.

## Proof

**1. Two elementary spectral bounds.** For any symmetric positive-definite pair \((A,P)\), its extreme generalized eigenvalues satisfy
\[
\lambda_{\max}(A,P)=\max_{x\ne0}\frac{x^{\mathsf T}Ax}{x^{\mathsf T}Px},\quad
\lambda_{\min}(A,P)=\min_{x\ne0}\frac{x^{\mathsf T}Ax}{x^{\mathsf T}Px}.
\]
If \(H\succeq0\) is nonzero, decomposing \(H\) into rank-one positive-semidefinite summands gives
\[
\lambda_{\min}(A,P)\leq\frac{\operatorname{tr}(AH)}{\operatorname{tr}(PH)}
\leq\lambda_{\max}(A,P).
\]
Likewise, restricting both Rayleigh quotients to any linear subspace can only reduce their ratio. These bounds do not assume that \(P\) respects any symmetry.

**2. The nondominant regime.** Suppose \(S>0\) and \(M\leq S/2\). The elementary polygon lemma says that for nonnegative lengths \(q_i\) with total \(S\), there exist planar unit vectors \(z_i\) such that \(\sum_i q_i z_i=0\) exactly when \(\max_i q_i\leq S/2\). One proof is induction on the number of lengths: their possible resultant magnitudes form the interval \([\max(0,2\max_i q_i-S),S]\), since adding a segment of length \(q\) to a resultant of length \(r\) realizes all magnitudes in \([|r-q|,r+q]\). Zero lengths do not affect the construction.

Apply this lemma to \(q_i=u_i^2\), and define the Gram matrix
\[
H_{ij}=\frac{u_i u_j}{S}\,z_i\cdot z_j.
\]
Then \(H\succeq0\), \(\operatorname{tr}H=1\), \(H_{ii}=u_i^2/S\), and \(Hu=0\). Therefore \(AH=H\). For every admissible \(P=\operatorname{diag}(p_i)\), write \(W=\sum_i u_i^2p_i>0\). Testing the top generalized Rayleigh quotient on \(u\) and the bottom quotient against \(H\) gives
\[
\lambda_{\max}(A,P)\geq\frac{S(1+S)}{W},\qquad
\lambda_{\min}(A,P)\leq\frac{S}{W}.
\]
Their ratio is at least \(1+S\). At \(P=I_n\), the spectrum is \(\{1+S,1,\ldots,1\}\), so equality holds. This proof simultaneously establishes global optimality against arbitrary asymmetric diagonal choices.

**3. The dominant regime.** Suppose \(M>R\) and \(R>0\). There is a unique dominant coordinate \(j\). Define the unit vector \(w=(u-u_je_j)/\sqrt R\), so \(e_j\perp w\). On the plane \(E=\operatorname{span}\{e_j,w\}\), the restrictions of \(A\) and an arbitrary diagonal \(P\) are
\[
B=\begin{pmatrix}1+M&u_j\sqrt R\\u_j\sqrt R&1+R\end{pmatrix},\qquad
P_E=\operatorname{diag}\!\left(p_j,\frac{1}{R}\sum_{i\ne j}u_i^2p_i\right).
\]
The sign of the off-diagonal entry does not affect the eigenvalues. Put \(\rho=\sqrt{MR/((1+M)(1+R))}\), which lies in \((0,1)\). For any positive \(2\times2\) diagonal preconditioner \(\operatorname{diag}(s,t)\), let \(C=\operatorname{diag}(s,t)^{-1/2}B\operatorname{diag}(s,t)^{-1/2}\), with diagonal entries \(x,y>0\). Its squared-trace/determinant invariant is
\[
\frac{(\operatorname{tr}C)^2}{\det C}=
\frac{(x+y)^2}{xy(1-\rho^2)}\geq\frac{4}{1-\rho^2},
\]
where equality holds exactly when \(x=y\). Since \((\operatorname{tr}C)^2/\det C=\kappa(C)+\kappa(C)^{-1}+2\), this proves that every such plane has condition number at least \((1+\rho)/(1-\rho)\). By the subspace Rayleigh bound, every full diagonal preconditioner satisfies the same lower bound.

Now take \(P_*\) as displayed in the finding. On \(E\), the scaled matrix has diagonal entries \(1+R\) and off-diagonal magnitude \((1+R)\rho\), so its eigenvalues are \((1+R)(1\pm\rho)\). On \(E^\perp\), the scaled matrix acts as the identity. The inequality \((1+R)(1-\rho)<1<(1+R)(1+\rho)\) follows from \(M>R>0\); for the first inequality, squaring its equivalent \(\rho>R/(1+R)\) reduces exactly to \(M>R\). Thus the two planar eigenvalues are also the extreme *full* eigenvalues, and the lower bound is attained.

When \(R=0\), the matrix \(A\) is diagonal, and \(P_*=A\) makes its scaled version the identity; both the formula and the optimal value reduce to \(\rho=0\), \(\kappa_*=1\). At \(M=R>0\), the nondominant argument applies and \(P_*=I_n\); the two values coincide. If \(S=0\), \(A=I_n\) directly. The exact criterion for identity optimality is strict in the dominant regime because the scalar balancing \(p_j=(1+M)/(1+R)>1\) improves the planar condition number over its unequal-diagonal value at \(P=I_n\).

**4. Jacobi counterexample.** For \(u=(1/2,1,1,1)^{\mathsf T}\), \(S=13/4\) and \(M=1\leq9/4\). The unscaled condition number is \(17/4\). Under \(P=\operatorname{diag}(A)=\operatorname{diag}(5/4,2,2,2)\), the eigenvalues are \(1/2\) (twice) and \((3\pm\sqrt{11/5})/2\). Hence \(\kappa(P)=3+\sqrt{11/5}>17/4\).

## Verification

Execute `python verify.py` using Python 3 with NumPy, SciPy, and SymPy. The included output record is `VERIFY_OUTPUT.txt`. The test program compares the proposed value with the spectral condition number of the proposed preconditioner for 145 fixed or pseudorandom real vectors in dimensions 2 through 12, checks 5,800 independently chosen asymmetric diagonal preconditioners, and runs 23 numerical minimizations. It also checks exact symbolic spectra in the dominant regime, an exact polygon-dual witness, and the rational Jacobi counterexample. These finite calculations are corroboration only: the proof above establishes the result for all admissible dimensions, vectors, and diagonal preconditioners.

## Relationship to prior work

Optimal diagonal scaling and equilibration are classical problems. Braatz and Morari (1994) develop a general convex formulation of optimal Euclidean condition-number scaling, including control applications. Takapoui and Javadi (2016) study practical equilibration and diagonal scaling, explicitly noting that heuristics need not reduce condition numbers. Qu and coauthors (2022) give general optimization and SDP algorithms for diagonal preconditioning. Kolotilina (2002) and Shapiro (1985) study general characterizations of optimally conditioned matrices under block/diagonal scalings. These works establish broad frameworks and necessary conditions; the assessed contribution here is **the explicit all-vector, all-dimension rank-one formula**, its polygon-majority transition, and the global one-coordinate optimal design. Generic numerical solvability is not presented as new.

## Limitations

The theorem does not assert that the displayed preconditioner is the only optimizer, and no uniqueness of individual entries is needed. It addresses a rank-one positive update of the identity and symmetric positive diagonal scaling, not arbitrary matrix scalings. Improved spectral condition number need not imply proportional improvement in every finite-step computational metric. The search did not establish that no previous specialized derivation exists. In particular, the full text of Kolotilina (2002) was not available in the accessed sources; its general optimal-conditioning characterization could contain more directly comparable special cases.

## References

1. R. D. Braatz and M. Morari, “Minimizing the Euclidean Condition Number,” *SIAM Journal on Control and Optimization* **32** (1994), 1763–1768. https://web.mit.edu/braatzgroup/Minimizing_the_Euclidean_condition_number.pdf
2. R. Takapoui and H. Javadi, “Preconditioning via Diagonal Scaling,” arXiv:1610.03871v1, publicly submitted 2016-10-12. https://arxiv.org/html/1610.03871v1
3. Z. Qu, W. Gao, O. Hinder, Y. Ye, and Z. Zhou, “Optimal Diagonal Preconditioning,” arXiv:2209.00809, 2022. https://arxiv.org/abs/2209.00809
4. L. Yu. Kolotilina, “Optimally Conditioned Block Matrices,” *Linear Algebra and its Applications* **340** (2002), 55–67, https://doi.org/10.1016/S0024-3795(01)00412-8 (accessible abstract; full comparison limited).
5. A. Shapiro, “Optimal Block Diagonal \(\ell_2\)-Scaling of Matrices,” *SIAM Journal on Numerical Analysis* **22** (1985), 81–94. https://doi.org/10.1137/0722005 (abstract consulted).
