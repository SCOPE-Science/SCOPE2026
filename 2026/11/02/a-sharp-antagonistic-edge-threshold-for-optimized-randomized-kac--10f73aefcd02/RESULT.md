# A sharp antagonistic-edge threshold for optimized randomized Kaczmarz sampling on dense inverse-Gram networks

## Finding

Let \(n\ge5\), and put \(m=n-2\). Let \(B\in\mathbb R^{n\times n}\) be invertible with every row of Euclidean norm one. Suppose \(C=(BB^{\mathsf T})^{-1}\) has off-diagonal entries \(C_{ij}=w>0\) for every unordered pair except \(\{1,n\}\), where \(C_{1n}=C_{n1}=-tw\) with \(t>0\). The diagonal entries of \(C\) are positive but otherwise unrestricted, subject to the stated existence and normalization assumptions.

For fixed independent, identically distributed selection of a row in the ordinary randomized Kaczmarz method, define the sharp one-step worst-direction expected squared-error decrement
\[
\gamma(p)=\lambda_{\min}\!\left(B^{\mathsf T}\operatorname{diag}(p)B\right),\qquad p_i\ge0,\quad\sum_i p_i=1.
\]
The unique maximizing probability vector is \(p_i^*=q_i/T\), where \(T=\sum_iq_i\) and
\[
q_i=\begin{cases}
C_{ii}+w(m-t),&i\in\{1,n\},\
C_{ii}+w(m+1),&2\le i\le n-1
\end{cases}\qquad\text{if }0<t\le m/2,
\]
while
\[
q_i=\begin{cases}
C_{ii}+wt,&i\in\{1,n\},\\
C_{ii}+w(m-1+m/t),&2\le i\le n-1
\end{cases}\qquad\text{if }t\ge m/2.
\]
The two definitions coincide at \(t=m/2\). In particular,
\[
\gamma_*=\frac1T,\qquad
T=\operatorname{tr}C+w\begin{cases}
m(m+3)-2t,&0<t\le m/2,\\
m(m-1)+m^2/t+2t,&t\ge m/2.
\end{cases}
\]
Consequently the uniquely optimal worst-direction one-step expected squared-error contraction factor is \(1-1/T\). The slack \(\operatorname{diag}(q)-C\) has nullity one when \(0<t<m/2\), and nullity two for \(t\ge m/2\). Thus \(t_{\mathrm{crit}}=(n-2)/2\) is the exact transition: the optimizer follows a signed-row-sum law below threshold and a different rational law above it.

## Assumptions and scope

The result concerns square invertible real systems with unit-norm rows and a complete off-diagonal inverse-Gram network with precisely one antagonistic edge. All \(n\ge5\), all \(t>0\), all \(w>0\) for which the stated normalized matrix \(B\) exists, and arbitrary admissible positive diagonal entries \(C_{ii}\) are covered. It is an exact fixed-iid, one-step, worst-direction result, not a statement about adaptive choices, without-replacement sampling, or the exact multistep mean-squared error.

The class is nonempty for every \(n\ge5\) and every \(t>0\) if \(w>0\) is sufficiently small. To see this, start with the off-diagonal pattern multiplied by \(w\) and unknown diagonal entries \(c_i\). At \(w=0\), \(c_i=1\) makes \(C=I\) and \((C^{-1})_{ii}=1\); the Jacobian of the map \(c\mapsto\operatorname{diag}(C^{-1})-\mathbf1\) is \(-I\). The implicit-function theorem supplies positive diagonal entries near one for small \(w\), with \(C\succ0\) and \(\operatorname{diag}(C^{-1})=\mathbf1\). Taking any real factor \(B\) with \(BB^{\mathsf T}=C^{-1}\) yields unit-norm rows.

## Proof

**1. Exact diagonal-majorant reduction.** For unit rows, the conditional expected error decrease from error vector \(e\) is \(e^{\mathsf T}B^{\mathsf T}\operatorname{diag}(p)Be\). If \(\gamma>0\), congruence by the inverse of \(B\) shows
\[
B^{\mathsf T}\operatorname{diag}(p)B\succeq\gamma I
\quad\Longleftrightarrow\quad
\operatorname{diag}(p)\succeq\gamma C.
\]
Setting \(d_i=p_i/\gamma\) reduces maximum \(\gamma\) to the inverse of
\[
T_{\min}=\min\left\{\sum_i d_i:\operatorname{diag}(d)-C\succeq0\right\}.
\]
Nonnegativity of \(d\) is automatic because \(d_i\ge C_{ii}>0\). The dual, by positive-semidefinite cone duality and the diagonal equality constraints, is
\[
\max\left\{\operatorname{tr}(CX):X\succeq0,\ X_{ii}=1\ \text{for every }i\right\}.
\]
Weak duality already suffices for the explicit matching certificates below. Let \(I=\{2,\ldots,n-1\}\), with \(|I|=m\), and \(S=\operatorname{diag}(q)-C\).

**2. Weak antagonism, \(0<t\le m/2\).** Insert the first proposed formula. For every real vector \(x\),
\[
\frac{x^{\mathsf T}Sx}{w}=
2\sum_{j\in I}\left(x_j-\frac{x_1+x_n}{2}\right)^2
+\sum_{\substack{i<j\\i,j\in I}}(x_i-x_j)^2
+\left(\frac m2-t\right)(x_1-x_n)^2\ge0.
\]
Also \(S\mathbf1=0\). The dual matrix \(X=\mathbf1\mathbf1^{\mathsf T}\) has diagonal one, is positive semidefinite, and has objective \(\operatorname{tr}(CX)=\sum_iq_i\). Thus primal and dual attain the same value, proving global optimality. For \(t<m/2\), the displayed quadratic form vanishes only on constant vectors; at equality it additionally allows one independent terminal-difference direction. This proves the nullities in this regime.

**3. Strong antagonism, \(t>m/2\).** Put \(r=m/(2t)\), so \(0<r<1\). Define the vector \(v=e_1+e_n-t^{-1}\sum_{j\in I}e_j\). With \(L_I\) the combinatorial Laplacian of the unit-weight complete graph on \(I\), embedded by zero rows and columns at the endpoints, the second proposed formula gives the exact factorization
\[
\frac Sw=t vv^{\mathsf T}+(1+t^{-1})L_I\succeq0.
\]
The first term has rank one and \(L_I\) has rank \(m-1\). The vector \(v\) is linearly independent of the range of \(L_I\), so \(S\) has rank \(m=n-2\), giving nullity two.

For a matching dual witness, let \(a\in\mathbb R^n\) have entries \(a_1=a_n=r\) and \(a_j=1\) for \(j\in I\). Let \(f=e_1-e_n\). Then
\[
X=aa^{\mathsf T}+(1-r^2)ff^{\mathsf T}\succeq0,\qquad X_{ii}=1.
\]
The identities \(Sa=0\), \(Sf=0\) and
\[
\operatorname{tr}(CX)=\operatorname{tr}C+w\bigl(m(m-1)+4mr-4tr^2+2t\bigr)
=\operatorname{tr}C+w\bigl(m(m-1)+m^2/t+2t\bigr)=\sum_iq_i
\]
establish complementary slackness and equality of primal and dual objectives. Hence the displayed \(q\) is globally optimal, without assuming symmetry of competing sampling probabilities.

**4. Uniqueness and sharpness.** Let \(d\) be any other optimal diagonal majorant. The dual witness from the corresponding regime gives \(\operatorname{tr}((\operatorname{diag}(d)-C)X)=0\). Positivity of both matrices implies their product is zero. In the weak regime, \(X=\mathbf1\mathbf1^{\mathsf T}\) forces \((\operatorname{diag}(d)-C)\mathbf1=0\), determining every \(d_i\) uniquely as the row sum \(\sum_j C_{ij}\). In the strong regime, \(X\) has positive coefficients on both \(aa^{\mathsf T}\) and \(ff^{\mathsf T}\); therefore \((\operatorname{diag}(d)-C)a=0\) and \((\operatorname{diag}(d)-C)f=0\). The first equation fixes each interior value \(d_j=C_{jj}+w(m-1+2r)\), and the endpoint-difference equation fixes \(d_1=C_{11}+wt\), \(d_n=C_{nn}+wt\). Since \(2r=m/t\), these are precisely the proposed values. The threshold is included in the weak argument. Therefore \(d\), hence \(p\), is unique. The smallest eigenvalue criterion is attained by a worst-direction error vector, so the contraction assertion is sharp.

## Verification

The standard-library-only `verify.py` recomputes the exact primal diagonal majorants, constructs their nonnegative rank-one/Laplacian decompositions, verifies positive-semidefinite dual Gram constructions, tests diagonal constraints, primal-dual equality, complementary slackness, and exact slack rank with rational arithmetic. It covers \(124\) rational parameter cases spanning both branches and the threshold, and separately constructs \(28\) small unit-row examples by solving for diagonal normalization and checks the claimed eigenvalue directly. Its current successful run reports \(47{,}263\) assertions. These finite calculations are corroborative; the universal statement follows from the preceding algebraic certificates.

Reproduce with `python3 verify.py`. No external package or solver is required.

## Relationship to prior work

Dai, Soltanalian and Pelckmans (first posted February 12, 2014, arXiv:1402.2863) derive the general semidefinite program for optimized Kaczmarz row selection, including an equivalent trace-minimization formulation. The present result solves that program explicitly, with uniqueness and a sharp antagonistic-edge threshold, for a dense signed inverse-Gram class not evaluated in their paper. The earlier exact-MSE analyses of Agaskar, Wang and Lu address multistep error criteria, which are not the objective here. General signed-graph and elliptope formulations provide background but do not themselves supply the stated Kaczmarz probabilities or the full phase classification. The signed triangle, signed cycle, and forest-supported inverse-Gram cases are distinct previously treated geometries; the dense graph here has every off-diagonal interaction nonzero, including many frustrated triangles, so their sparse formulas do not specialize to this theorem.

## Limitations

The rate is the exact **worst-direction conditional one-step** expected squared-error rate. It is not asserted to minimize long-horizon exact mean-squared error, to optimize adaptive sampling, or to hold for arbitrary correlated/nonuniform off-diagonal patterns. Existence at a prescribed large \(w\) is not automatic; feasibility of \(C\) as the inverse Gram of unit rows is a hypothesis. The literature comparison is best knowledge rather than a guarantee that no equivalent historical derivation exists. 

## References

1. L. Dai, M. Soltanalian, K. Pelckmans, *On the Randomized Kaczmarz Algorithm*, arXiv:1402.2863, first posted February 12, 2014. https://arxiv.org/abs/1402.2863
2. A. Agaskar, C. Wang, Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, IEEE GlobalSIP (2014), DOI:10.1109/GlobalSIP.2014.7032145. https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b
3. C. Wang, A. Agaskar, Y. M. Lu, *Randomized Kaczmarz Algorithm for Inconsistent Linear Systems: An Exact MSE Analysis*, arXiv:1502.00190, first posted February 1, 2015. https://arxiv.org/abs/1502.00190
4. T. Strohmer, R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, Journal of Fourier Analysis and Applications 15 (2009), 262–278. https://doi.org/10.1007/s00041-008-9030-4
