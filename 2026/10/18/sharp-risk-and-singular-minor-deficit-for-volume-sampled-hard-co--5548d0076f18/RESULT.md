# Sharp risk and singular-minor deficit for volume-sampled hard constraints in least squares

## Finding

Enforcing randomly selected equations exactly can bias a least-squares solution when the full system is inconsistent. The following finite-dimensional theorem gives an exact, all-design answer for row sampling by the principal minors of the full-data hat matrix. It includes sample sizes strictly below the parameter dimension and permits rank-deficient individual row subsets, which are assigned zero sampling probability.

**Theorem.** Let \(m>n\ge2\), let \(A\in\mathbb R^{m\times n}\) have full column rank, and let \(b\in\mathbb R^m\). Define
\[
G=A^{\mathsf T}A,\quad x_*=G^{-1}A^{\mathsf T}b,\quad r=b-Ax_*,\quad H=AG^{-1}A^{\mathsf T}.
\]
Assume \(r\ne0\) and fix an integer \(1\le k<n\). Select a \(k\)-element row set \(S\subseteq\{1,\ldots,m\}\) with probabilities
\[
\Pr(S)=\frac{\det H_{SS}}{\binom nk}.
\]
For each positive-probability set, let \(x_S\) be the unique solution of
\[
\min_{x\in\mathbb R^n}\|Ax-b\|_2^2\quad\text{subject to}\quad A_Sx=b_S.
\]
Set \(u=r/\|r\|_2\) and \(Q=H+uu^{\mathsf T}\). Then \(H\) and \(Q\) are orthogonal projectors of ranks \(n\) and \(n+1\), respectively, and
\[
\boxed{\frac{\mathbb E_S\|Ax_S-b\|_2^2}{\|r\|_2^2}
=\frac{n+1}{n-k+1}-\frac1{\binom nk}
\sum_{\substack{|S|=k\\\det H_{SS}=0}}\det Q_{SS}.}
\]
In particular, the **sharp, matrix-independent frontier** is
\[
\boxed{1\ \le\ \frac{\mathbb E_S\|Ax_S-b\|_2^2}{\min_x\|Ax-b\|_2^2}
\ \le\ \frac{n+1}{n-k+1}.}
\]
For fixed \(n,k\), both endpoints occur for admissible data. Equality in the upper bound holds precisely when every singular \(k\)-row subset of \(H\) has vanishing corresponding principal minor in \(Q\). In particular, it holds if **every \(k\)-row subset of \(A\) is linearly independent** (full support of the sampling law).

## Assumptions and scope

The sample-size restriction is \(1\le k<n\); the sampled response values are imposed as hard equalities, but **the objective still evaluates all \(m\) responses**. Consequently this is not a method for estimating a full-data least-squares solution when only \(k<n\) response values are observed. Sampling depends on \(A\), not on \(b\). All computations and claims are for real, exact finite-dimensional matrices. Only subsets with \(\det H_{SS}>0\) are selected, and these are exactly the subsets whose rows in \(A_S\) are independent. If \(r=0\), every constrained problem has the unique minimizer \(x_*=x_S\), so its loss is zero and the displayed ratio is inapplicable.

## Proof

**1. Probability and feasibility.** Since \(H=H^{\mathsf T}=H^2\) and \(\operatorname{rank}H=n\),
\[
\sum_{|S|=k}\det H_{SS}=[t^k]\det(I+tH)=[t^k](1+t)^n=\binom nk.
\]
Also, \(H_{SS}=A_SG^{-1}A_S^{\mathsf T}\). Thus \(\det H_{SS}>0\) precisely when \(A_S\) has row rank \(k\), which makes every equality system \(A_Sx=b_S\) feasible for arbitrary \(b_S\). The objective is strictly convex because \(G\) is positive definite, hence its constrained minimizer is unique.

**2. Exact cost of enforced rows.** The normal equations give \(A^{\mathsf T}r=0\). By Pythagoras,
\[
\|Ax-b\|_2^2=\|r\|_2^2+(x-x_*)^{\mathsf T}G(x-x_*).
\]
Writing \(\delta=x-x_*\), the sampled equalities are \(A_S\delta=r_S\). The first-order condition for minimizing the strictly convex quadratic in \(\delta\) yields
\[
\delta_S=G^{-1}A_S^{\mathsf T}H_{SS}^{-1}r_S,
\qquad \|Ax_S-b\|_2^2-\|r\|_2^2=r_S^{\mathsf T}H_{SS}^{-1}r_S.
\]
No inverse of a singular \(H_{SS}\) is used, since those subsets have probability zero.

**3. Rank-one augmentation and complete minor sum.** Since \(u\perp\operatorname{im}A\), \(Q=H+uu^{\mathsf T}\) is an orthogonal projector of rank \(n+1\). For a positive-probability set \(S\), the matrix determinant lemma gives
\[
\det Q_{SS}=\det H_{SS}
\left(1+\frac{r_S^{\mathsf T}H_{SS}^{-1}r_S}{\|r\|_2^2}\right).
\]
For singular subsets, \(\det H_{SS}=0\) but \(\det Q_{SS}\ge0\), so those determinants cannot simply be discarded. Summing the displayed identity over positive-probability sets and using the rank-\(n+1\) elementary symmetric projector identity yields
\[
\binom nk\left(1+
\frac{\mathbb E_S[\|Ax_S-b\|_2^2-\|r\|_2^2]}{\|r\|_2^2}\right)
=\binom{n+1}k-\sum_{\substack{|S|=k\\\det H_{SS}=0}}\det Q_{SS}.
\]
Divide by \(\binom nk\) and simplify \(\binom{n+1}k/\binom nk=(n+1)/(n-k+1)\). Nonnegativity of the excess loss and every singular-subset minor proves the two-sided bound. A singular-subset minor can vanish even without full support; therefore the stated condition is exactly, not just sufficiently, the equality criterion.

**4. Sharpness of both endpoints.** For any fixed \(n\ge2\) and \(1\le k<n\), choose \(m=n+1\) distinct real numbers \(t_1,\ldots,t_m\) and the Vandermonde design whose \(i\)-th row is \((1,t_i,\ldots,t_i^{n-1})\). Every \(k\)-row subset is independent. With \(b=e_1\), the least-squares residual is nonzero, because a polynomial of degree below \(n\) cannot vanish at the \(n\) distinct locations \(t_2,\ldots,t_m\) while taking value one at \(t_1\). The singular-minor sum is empty, attaining the **upper** bound.

For the **lower** bound, set \(m=n+1\), \(A=\begin{bmatrix}I_n\\0\end{bmatrix}\), and \(b=e_{n+1}\). Then \(x_*=0\), the only sampled sets comprise rows of \(I_n\), and the constrained solution remains \(x_S=x_*=0\). Its full-data loss is exactly optimal, so the lower bound is attained.

**5. Rank-degeneracy is a genuine correction.** In the explicit example
\[
A=\begin{bmatrix}1&0&0\\1&0&0\\0&1&0\\0&0&1\\1&1&1\end{bmatrix},
\quad b=(1,0,4,2,0)^{\mathsf T},\quad n=3,\quad k=2,
\]
there is one singular two-row subset, the first two rows. Exact rational calculation gives \(\|r\|_2^2=88/7\), expected excess loss \(87/7\), and singular augmented-minor sum \(3/88\). Thus the full expected risk ratio is \(175/88\), strictly below the universal upper frontier \(2\) by precisely \(1/88\). This illustrates why an all-design equality without the singular-subset term is false.

## Verification

Run the supplied standalone `CHECK.py` using Python 3 and SymPy:

```shell
python CHECK.py
```

The program uses exact integer and rational arithmetic to verify normalization, projector identities, sampled feasibility, KKT solutions, determinant-lemma equality, the main sum identity, both sharp endpoints, and an explicit strict singular-deficit example. It also tests a fixed-seed collection of random small full-column-rank designs for every admissible sample size. In the supplied execution it passed 6,275 individual exact checks across 59 random admissible matrices and the explicit families. The symbolic finite checks support the proof but do not replace its universal projector/minor argument.

## Relationship to prior work

Sun, Qi, Han, and Xie (2026) analyze the acceleration of randomized solvers obtained by enforcing selected equations exactly in **consistent** systems, and identify inconsistent systems as a direction for future investigation. Here, the full objective remains least squares when the global system cannot be satisfied, and the quantity assessed is the statistical cost of hard row constraints, not the iterative convergence rate.

Dereziński and Warmuth (2018, Theorem 8) establish an expected full-loss formula for volume-sampled **interpolation with a number of sampled rows equal to the parameter dimension**, and account for singular sampling supports. Their other principal matrix expectation formulas cover samples at least as large as the parameter dimension (with a separate regularized extension). In contrast, the present theorem covers \(k<n\), retains access to the full objective, and minimizes it subject to only the sampled equations. Epperly (2025/2026) connects projection-DPP sampling with interpolation/projection error for a fixed \(k\)-dimensional approximation subspace, rather than the hard-constraint risk for the full \(n\)-dimensional design.

Fanuel, Schreurs, and Suykens (2022, Theorems 4.1 and 5.8) analyze DPP subsampling of semiparametric/kernel interpolation and projected Nyström estimators, proving implicit regularization and a noise-averaged prediction-risk bound. Their estimator and random-support law do not impose \(k<n\) hard linear equations while minimizing the unregularized full-data least-squares objective.

The normal-equation and principal-minor identities used in the proof are classical; the claimed finding is their exact assembly into this **subdimension hard-constraint risk law**, including the singular-minor deficit and sharp all-design extremes. No claim is made that determinantal sampling, subspace constraints, or Cauchy–Binet is new.

## Limitations

The objective uses **all** responses after row selection, so the factor is not a label-efficiency bound or an iterative runtime guarantee. The analysis does not model noisy approximate constraint satisfaction, weighted/regularized objectives, floating-point error, or arbitrary row-selection laws. The exact degeneracy correction can be cumbersome to evaluate for large \(m\). The result does not prove a method to attain the optimum of an inconsistent system while enforcing arbitrarily many contradictory equations. Coverage by a differently formulated older projector/DPP identity cannot be ruled out solely from literature searches; this remains a bibliographic limitation.

## References

1. Y. Sun, H.-D. Qi, D. Han, and J. Xie, *On subspace-constrained preconditioning for randomized iterative methods*, arXiv:2605.29304v1, publicly submitted 2026-05-28, https://arxiv.org/html/2605.29304v1 .
2. M. Dereziński and M. K. Warmuth, *Reverse Iterative Volume Sampling for Linear Regression*, Journal of Machine Learning Research 19(23), 1–39 (2018), https://jmlr.org/papers/volume19/17-781/17-781.pdf .
3. E. N. Epperly, *Adaptive randomized pivoting and volume sampling*, arXiv:2510.02513v2 (2026 revision of 2025 preprint), https://arxiv.org/pdf/2510.02513 .
4. M. Fanuel, J. Schreurs, and J. A. K. Suykens, *Determinantal Point Processes Implicitly Regularize Semi-parametric Regression Problems*, SIAM Journal on Mathematics of Data Science 4(3), 1171–1190 (2022); preprint arXiv:2011.06964v2, https://arxiv.org/pdf/2011.06964 .
