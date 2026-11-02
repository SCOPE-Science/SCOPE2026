# Exact two-phase Kaczmarz sampling for a bipartite inverse Gram with one antagonistic pair

## Finding

Let \(p,q\ge2\) be integers and \(A\in\mathbb R^{(p+q)\times(p+q)}\) invertible with every row of Euclidean norm one. Partition the rows into \(U=\{s,t,u_3,\ldots,u_p\}\) and \(V=\{v_1,\ldots,v_q\}\). Suppose the inverse row Gram \(C=(AA^{\mathsf T})^{-1}\) is positive definite, its off-diagonal entries are \(C_{ij}=w>0\) for all \(i\in U,j\in V\), \(C_{st}=C_{ts}=-v<0\), and zero at every other off-diagonal position. The diagonal entries of \(C\) may be different.

Choose row \(i\) independently at every step with fixed probability \(\pi_i\) and perform the ordinary orthogonal Kaczmarz projection. Define its sharp worst-direction one-step expected squared-error decrement by
\[
\gamma(\pi)=\lambda_{\min}\!\left(A^{\mathsf T}\operatorname{diag}(\pi)A\right),\qquad \pi_i\ge0,\quad\sum_i\pi_i=1.
\]
Set \(z=\min\{1,wq/(2v)\}\), and define
\[
\begin{split}
 k_s=k_t&=wqz-v(2z^2-1),\\
 k_i&=wq\quad(i\in U\setminus\{s,t\}),\\
 k_j&=w(p-2+2z)\quad(j\in V),\\
 d_i&=C_{ii}+k_i,\qquad T=\sum_i d_i.
\end{split}
\]
**Then \(d_i>0\) for every row, and the unique maximizer over all independent fixed row probabilities is \(\pi_i^*=d_i/T\), with \(\gamma_*=1/T\).** In particular, writing \(v_c=wq/2\), the exact two-regime solution is
\[
\begin{array}{ll}
0<v\le v_c:& T=\operatorname{tr}C+2wpq-2v,\quad
 d_s=C_{ss}+wq-v,\quad d_t=C_{tt}+wq-v,\\
&d_i=C_{ii}+wq\ (i\in U\setminus\{s,t\}),\quad d_j=C_{jj}+wp\ (j\in V);\\
v\ge v_c:& T=\operatorname{tr}C+2wq(p-2)+2v+\dfrac{w^2q^2}{v},\\
&d_s=C_{ss}+v,\quad d_t=C_{tt}+v,\\
&d_i=C_{ii}+wq\ (i\in U\setminus\{s,t\}),\quad
 d_j=C_{jj}+w\left(p-2+\dfrac{wq}{v}\right)\ (j\in V).
\end{array}
\]
Both formulas agree at \(v=v_c\). The critical ratio \(v/w=q/2\) is independent of the size \(p\) of the part containing the antagonistic pair. For \(v<v_c\), a rank-one correlation certificate is optimal; for \(v>v_c\), it is strictly suboptimal, and a rank-two certificate is optimal.

## Assumptions and scope

The system is square, real, nonsingular and consistent. Its rows have unit norm; the probability distribution is fixed, independent and used for single-row orthogonal projections without overrelaxation or preconditioning. The specified inverse Gram pattern is a condition on \(C\), not on \(AA^{\mathsf T}\). The theorem applies to every actual such normalized system, irrespective of whether a proposed arbitrary diagonal and off-diagonal parameter tuple is realizable under the unit-row constraint. The sign and support pattern is a complete positive bipartite off-diagonal block plus exactly one negative within-part pair. No assumption of equal diagonal entries is imposed. The cases \(p=q=2\) and \(v=v_c\) are included.

## Proof

**1. One-step decrement and diagonal-majorant primal.** For an error vector \(e\), the conditional expected squared norm after projecting onto a randomly chosen unit row is \(\|e\|^2-e^{\mathsf T}A^{\mathsf T}\operatorname{diag}(\pi)Ae\). Thus the worst-direction decrement is exactly \(\gamma(\pi)\). If it is positive, \(A^{\mathsf T}\operatorname{diag}(\pi)A\succeq\gamma I\) is equivalent by invertible congruence to \(\operatorname{diag}(\pi)\succeq\gamma C\). Consequently maximizing \(\gamma\) is equivalent to minimizing \(\sum_i d_i\) over diagonal majorants \(\operatorname{diag}(d)-C\succeq0\), with \(\gamma_*=1/T_*\) and \(\pi_i=d_i/T_*\). Every feasible majorant has \(d_i\ge C_{ii}>0\).

**2. Universal lower bound from correlation matrices.** For any positive-semidefinite \(X\) with \(X_{ii}=1\), and any feasible diagonal majorant \(D\),
\[
\operatorname{tr}D=\operatorname{tr}(DX)\ge\operatorname{tr}(CX).
\]
Represent \(X_{ij}=u_i\cdot u_j\) using unit vectors in a real Euclidean space. Its value is
\[
\operatorname{tr}(CX)=\operatorname{tr}C+2w\Big(\sum_{i\in U}u_i\Big)\cdot\Big(\sum_{j\in V}u_j\Big)-2v\,u_s\cdot u_t.
\]
Fixing \(u_s,u_t\) with \(u_s\cdot u_t=2z^2-1\), where \(0\le z\le1\), the triangle inequality shows that the expression is at most
\[
\operatorname{tr}C+2\big[wq(p-2+2z)-v(2z^2-1)\big].
\]
Equality is attainable: choose \(u_s=(z,\sqrt{1-z^2})\), \(u_t=(z,-\sqrt{1-z^2})\), and every other \(u_i=(1,0)\). Indeed, \(\sum_{i\in U}u_i=(p-2+2z,0)\) and all \(V\)-vectors align with this sum. The resulting scalar objective is strictly concave in \(z\), with unique maximizer \(z=\min\{1,wq/(2v)\}\). This supplies a feasible correlation matrix \(X\) attaining the stated value \(T\). For \(z=1\), all vectors agree, so \(X\) has rank one; for \(0<z<1\), it has rank two.

**3. Matching positive-semidefinite diagonal majorant.** Put \(d_i=C_{ii}+k_i\) as stated and \(S=\operatorname{diag}(d)-C\). When \(v\le wq/2\), for an arbitrary real vector \(x\) (with \(x_i\) on \(U\) and \(y_j\) on \(V\)), its quadratic form is
\[
 x^{\mathsf T}Sx=w\sum_{i\in U}\sum_{j\in V}(x_i-y_j)^2-v(x_s-x_t)^2\ge0.
\]
The inequality follows by summing \((x_s-y_j)^2+(x_t-y_j)^2\ge(x_s-x_t)^2/2\) over all \(q\) vertices of \(V\). For \(v\ge wq/2\), the quadratic form instead has the manifestly nonnegative decomposition
\[
\begin{aligned}
 x^{\mathsf T}Sx={}&w\sum_{i\in U\setminus\{s,t\}}\sum_{j\in V}(x_i-y_j)^2\\
 &+v\left(x_s+x_t-\frac wv\sum_{j\in V}y_j\right)^2\\
 &+\frac{w^2}{v}\left(q\sum_{j\in V}y_j^2-\left(\sum_{j\in V}y_j\right)^2\right).
\end{aligned}
\]
The last bracket is \(\sum_{j<k}(y_j-y_k)^2\), so \(S\succeq0\). Direct substitution of the certificate vectors from step 2 yields \(SX=0\): in the high-ratio regime this uses \(2vz=wq\), and in the low-ratio regime it follows from \(S\mathbf1=0\). Hence \(\operatorname{tr}(SX)=0\) and \(\sum_i d_i=\operatorname{tr}(CX)=T\). The lower bound of step 2 and the feasible majorant give exact optimality, including the boundary.

**4. Uniqueness without a symmetry assumption.** Let \(D'\) be any other optimal feasible diagonal majorant. For the fixed optimal correlation certificate \(X\), both \(S'=D'-C\) and \(X\) are positive semidefinite and \(\operatorname{tr}(S'X)=0\). Therefore \(S'X=0\). Its \((i,i)\)-entry and \(X_{ii}=1\) imply
\[
 D'_{ii}=C_{ii}+\sum_{j\ne i}C_{ij}X_{ji}=d_i.
\]
Thus the majorant, and hence every optimizing probability, is unique. Strict concavity of the one-variable correlation objective also shows that the rank-one certificate is no longer optimal once \(v>wq/2\).

## Verification

Run \(\texttt{python verify.py}\) in the directory containing the embedded script. It evaluates the exact rational primal and dual formulas and checks \(SX=0\), \(\operatorname{tr}D=\operatorname{tr}(CX)\) and the asserted closed form for \(T\) over 450 rational parameter configurations, including both regimes and their boundary. It also checks finite-matrix positive semidefiniteness and the inverse-Gram spectral decrement numerically, tests 20 models against feasible random and perturbed probabilities, and tests three explicitly normalized-row examples. The executable check is supporting evidence; steps 1–4 prove the all-parameter, all-dimension theorem. Numerical eigenvalue comparisons have floating-point tolerance and do not certify all matrices.

## Relationship to prior work

Strohmer and Vershynin (first arXiv version February 8, 2007) introduced the standard randomized Kaczmarz convergence analysis. Gower and Richtárik (arXiv 2015) formulate optimal sampling as a semidefinite eigenvalue optimization; this general optimization framework is not claimed as new. Zelazo and Bürger (arXiv 2014) establish the effective-resistance condition for positive semidefiniteness of signed Laplacians; the low-ratio certificate is consistent with that prior result, but the current proof also computes the complete supercritical optimum and uniquely optimal sampling probabilities in a distinct inverse-Gram model. The unrestricted two-regime, arbitrary-\(p,q\) sampling formula, the rank transition, and uniqueness of every optimizer are the claims assessed here. The general framework does not itself provide these explicit formulas.

## Limitations

The result optimizes the sharp conditional one-step expected squared-error decrease, not the exact multistep annealed mean-square exponent or the asymptotic almost-sure rate. It excludes rectangular matrices, block sampling, adaptive probabilities, more than one negative within-part inverse-Gram interaction, and nonconstant bipartite cross couplings. The prescribed inverse-Gram pattern with arbitrary diagonal entries must actually arise from normalized rows; not every arbitrary positive-definite candidate matrix is automatically such a normalized inverse Gram. Searches do not establish absolute novelty; an equivalent specialized treatment may exist. No independent mathematical audit has been performed.

## References

1. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, arXiv:math/0702226, version 1, February 8, 2007. https://arxiv.org/abs/math/0702226
2. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296 (first posted 2015), SIAM Journal on Matrix Analysis and Applications 36 (2015), 1660–1690. https://arxiv.org/abs/1506.03296
3. D. Zelazo and M. Bürger, *On the Definiteness of the Weighted Laplacian and its Connection to Effective Resistance*, arXiv:1408.2187 (2014). https://arxiv.org/abs/1408.2187
4. A. Agaskar, C. Wang and Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, IEEE GlobalSIP (2014). https://dash.harvard.edu/entities/publication/73120379-2750-6bd4-e053-0100007fdf3b
