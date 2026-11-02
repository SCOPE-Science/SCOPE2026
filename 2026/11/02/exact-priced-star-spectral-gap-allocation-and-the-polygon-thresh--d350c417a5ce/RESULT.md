# Exact priced-star spectral-gap allocation and the polygon threshold

## Finding

Let \(K_{1,m}\) be a star with \(m\ge 2\) leaves. Each hub–leaf edge \(i\) has conductance \(w_i\ge0\), unit vertex masses, and strictly positive per-unit-conductance price \(c_i>0\). For budget \(B>0\), maximize the second-smallest eigenvalue \(\lambda_2(L(w))\) of the combinatorial weighted Laplacian, subject to \(\sum_i c_iw_i\le B\).

Put
\[
N=m+1,\quad a_i=\sqrt{c_i},\quad A=\sum_{i=1}^{m}a_i,\quad
\Delta=\max\{0,2\max_i a_i-A\},\quad
C_*=\sum_i c_i-\frac{\Delta^2}{N}.
\]
Then \(C_*>0\), and the **exact optimal gap** is
\[
\boxed{\max_{w_i\ge0,\ \sum_i c_iw_i\le B}\lambda_2(L(w))=\frac{B}{C_*}.}
\]
The optimum is **unique**. If \(\Delta=0\), every optimal conductance is equal to \(B/C_*\), irrespective of the differences among prices. If \(\Delta>0\), there is a unique dominant price index \(j\) satisfying \(a_j>\sum_{i\ne j}a_i\), and
\[
\boxed{
 w_j^*=\frac{B}{C_*}\left(1-\frac{\Delta}{Na_j}\right),\qquad
 w_i^*=\frac{B}{C_*}\left(1+\frac{\Delta}{Na_i}\right)\quad(i\ne j).
}
\]
All optimal conductances are strictly positive. Thus the phase boundary separating equal-conductance from nonuniform allocation is precisely the polygon inequality \(\max_i\sqrt{c_i}\le\sum_{k\ne i}\sqrt{c_k}\). For \(m\ge3\), the optimal eigenvalue \(\lambda_2\) has multiplicity \(m-1\) when \(\Delta=0\), and multiplicity one when \(\Delta>0\). In the two-leaf case the multiplicity is one in both regimes.

## Assumptions and scope

The graph has one hub labeled \(0\) and leaves \(1,\ldots,m\), with precisely the \(m\) undirected hub–leaf edges and no other edges. The edge rates \(w_i\) are nonnegative and independent decision variables, not transition probabilities for a discrete-time stochastic matrix. The Laplacian is the ordinary unnormalized combinatorial Laplacian with \(L_{00}=\sum_iw_i\), \(L_{ii}=w_i\), \(L_{0i}=L_{i0}=-w_i\), and remaining entries zero. Its eigenvalues are ordered with multiplicities as \(0=\lambda_1\le\lambda_2\le\cdots\le\lambda_N\). The spectral objective is that of a continuous-time symmetric diffusion or continuous-time Markov process with generator \(-L\). Prices \(c_i\) and budget \(B\) are arbitrary strictly positive real numbers. No integer or rational restriction is imposed in the theorem.

## Proof

**1. Reduction to a diagonal semidefinite constraint.** For any vertex vector \(x\) perpendicular to the all-ones vector, set \(y_i=x_i-x_0\). The zero-sum condition forces \(x_0=-\sum_i y_i/N\). Consequently,
\[
 x^{\mathsf T}L(w)x=\sum_iw_iy_i^2,\qquad
 \|x\|_2^2=y^{\mathsf T}Qy,\qquad
 Q=I_m-\frac{\mathbf1\mathbf1^{\mathsf T}}N.
\]
The map \(x\mapsto y\) is a bijection from the zero-sum subspace to \(\mathbb R^m\); hence
\[
\lambda_2(L(w))\ge 1\quad\Longleftrightarrow\quad
 S(w)=\operatorname{diag}(w)-Q\succeq0.
\]
By positive homogeneity of \(\lambda_2\), the fixed-budget problem is equivalent to minimizing \(\sum_i c_iw_i\) subject to \(S(w)\succeq0\), and then scaling the minimizing vector to budget \(B\).

**2. A sharp universal lower bound on cost.** Let \(X\succeq0\) be any positive semidefinite matrix with diagonal \(X_{ii}=c_i\). If \(S(w)\succeq0\), the nonnegative trace product yields
\[
0\le\operatorname{tr}(S(w)X)=\sum_i c_iw_i-\operatorname{tr}(QX),
\quad\text{so}\quad \sum_i c_iw_i\ge \operatorname{tr}(QX).
\]
Factor \(X\) as a Gram matrix \(X_{ij}=v_i^{\mathsf T}v_j\); then \(\|v_i\|_2=a_i\) and
\[
\operatorname{tr}(QX)=\sum_i c_i-\frac1N\Big\|\sum_i v_i\Big\|_2^2.
\]
The minimum norm of the sum of vectors having prescribed lengths \(a_1,\ldots,a_m\), in an unrestricted Euclidean space, is exactly \(\Delta=\max\{0,2\max_i a_i-A\}\). The triangle inequality gives the lower bound. Equality when \(\Delta>0\) is obtained by putting the longest vector on a line in the opposite direction from all others. Equality when \(\Delta=0\) is obtained by laying the lengths consecutively around a closed polygon in the plane (including a degenerate two-edge polygon for equality in the two-vector case). The resulting Gram matrix is feasible and gives the lower bound \(C_*\) for every primal feasible \(w\).

**3. Construction and primal feasibility.** If \(\Delta=0\), set \(u_i=1\) for all \(i\). Then \(S(u)=\mathbf1\mathbf1^{\mathsf T}/N\succeq0\) and \(\sum_ic_iu_i=C_*\), proving optimality.

If \(\Delta>0\), let \(j\) be the unique dominant index, \(b=a_j\), and \(A'=\sum_{i\ne j}a_i=b-\Delta>0\). Set
\[
u_j=1-\frac{\Delta}{Nb},\qquad
u_i=1+\frac{\Delta}{Na_i}\quad(i\ne j).
\]
All entries are positive. For every \(y\in\mathbb R^m\), write \(s=\sum_{i\ne j}y_i\). Weighted Cauchy–Schwarz gives \(\sum_{i\ne j} y_i^2/a_i\ge s^2/A'\), hence
\[
\begin{aligned}
N y^{\mathsf T}S(u)y
&=\Delta\left(\sum_{i\ne j}\frac{y_i^2}{a_i}-\frac{y_j^2}{b}\right)+(y_j+s)^2\\
&\ge\Delta\left(\frac{s^2}{A'}-\frac{y_j^2}{b}\right)+(y_j+s)^2\\
&=\left(\sqrt{\frac{A'}b}\,y_j+\sqrt{\frac b{A'}}\,s\right)^2\ge0.
\end{aligned}
\]
Thus \(S(u)\succeq0\), and direct substitution gives
\[
\sum_ic_iu_i=\sum_i c_i+\frac{\Delta}{N}\left(\sum_{i\ne j}a_i-b\right)
=\sum_i c_i-\frac{\Delta^2}{N}=C_*.
\]
The dual lower bound is attained, so \(u\) is globally optimal. Scaling by \(B/C_*\) gives the displayed unique-budget candidate and objective value. Since \(m\ge2\) and all \(a_i>0\), the proposed rates and \(C_*\) are positive.

**4. Uniqueness.** In the polygon regime choose the zero-sum Gram vectors \(v_i\) from Step 2, with nonzero lengths. Their Gram matrix \(X\) satisfies \(X\mathbf1=0\). For any optimal feasible \(w\), equality of primal and dual objectives forces \(S(w)X=0\). Since \(QX=X\), this reads \(\operatorname{diag}(w-\mathbf1)X=0\). The \(i\)-th diagonal entry is \((w_i-1)c_i\), so every \(w_i=1\).

In the dominant regime set \(z_j=b\) and \(z_i=-a_i\) for \(i\ne j\). Then \(\sum_i z_i=\Delta\) and \(X=zz^{\mathsf T}\) attains the dual bound. Any optimal \(w\) obeys \(S(w)z=0\); its \(i\)-th equation is \((w_i-1)z_i+\Delta/N=0\). As each \(z_i\ne0\), this uniquely forces exactly the rates \(u_i\). Therefore uniqueness holds in both regimes, and survives scaling to budget \(B\).

**5. Optimal gap multiplicity.** The reduction in Step 1 identifies the gap eigenspace with \(\ker S(u)\). When \(\Delta=0\), \(S(u)=\mathbf1\mathbf1^{\mathsf T}/N\) has kernel dimension \(m-1\). When \(\Delta>0\), equality in the weighted Cauchy–Schwarz step and in the concluding square forces all nondominant \(y_i\) proportional to \(a_i\), and \(y_j\) equal to the opposite multiple of \(b\). Thus \(\ker S(u)\) is the one-dimensional span of \(z\).

## Verification

A standalone exact-rational Python verifier is supplied as `verify_star_budget.py` (standard library only). Run `python verify_star_budget.py` after extraction. The replay output is `VERIFY_OK 13940 exact-rational assertions`. It checks all length tuples with \(m\in\{2,3,4\}\) and \(a_i\in\{1,2,3,4\}\), additional seeded cases through seven leaves, the price threshold, primal cost, all principal minors of the reduced slack matrix, primal–dual complementary slackness in the dominant regime, and the Rayleigh quadratic-form identity on exact vectors. These finite checks are consistency tests; the proof above establishes the statement for all real positive prices and budgets.

For example, with three leaves, prices \((16,1,1)\), and target spectral gap at least one, the formula gives \(\Delta=2\), \(C_*=17\), and optimal rates \((7/8,3/2,3/2)\). Equal unit rates cost \(18\). At budget \(B=18\), the optimal gap is \(18/17\), as compared with \(1\) for the equal-rate budget allocation.

## Relationship to prior work

Sun, Boyd, Xiao and Diaconis established the general fastest-mixing continuous-time process optimization under an arbitrary positive linear cost on edge rates, its SDP dual, and a maximum-variance geometric interpretation. Their sections 3–5 and examples treat the general formulation, paths and cycles; the present contribution is the explicit all-price star solution, the exact polygon transition and the uniqueness/multiplicity classification, not a new general SDP formulation. Göring, Helmberg and Wappler give an optimal equal-price star embedding and describe separator/embedding properties, which subsume the equal-price special case but do not state the arbitrary-price rule. Their later arbitrary-length rotational-dimension framework also contains the relevant optimization as a general instance, but its structural embedding statements do not provide the closed-form conductances or threshold. Ghosh and Boyd establish convex spectral-gap optimization techniques for graph families rather than this fixed-star heterogeneous-price optimization. Fiedler's absolute algebraic connectivity of trees deals with uniform edge-price normalization, and its uniform-star implications are not claimed as new.

## Limitations

This theorem concerns *continuous-time*, unnormalized Laplacian spectral gaps on a fixed star, not discrete-time fastest-mixing matrices, node-weighted Laplacians, changing topology or general trees. The bounds do not imply the same formula under upper bounds on individual rates or nonlinear price functions. The optimization itself is a special case of an older generic semidefinite program. The novel-content assessment is limited to the explicit formulas, all-price phase boundary, unique optimal rates and eigenvalue multiplicities; exhaustive exclusion of all specialist historical publications has not been established. The accessible 1990 Fiedler article was represented by an abstract and cannot support claims about its entire text.

## References

1. Jun Sun, Stephen Boyd, Lin Xiao and Persi Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699. DOI: 10.1137/S0036144504443821. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf (published electronically 2006-11-02).
2. Arpita Ghosh and Stephen Boyd, *Upper Bounds on Algebraic Connectivity via Convex Optimization*, Linear Algebra and its Applications 418 (2006), 693–707. DOI: 10.1016/j.laa.2006.03.006. Full text: https://www-leland.stanford.edu/~boyd/papers/pdf/eigbounds_laplacian.pdf (available online 2006-05-05).
3. Frank Göring, Christoph Helmberg and Markus Wappler, *Embedded in the Shadow of the Separator*, research preprint (2007 revision), https://www-user.tu-chemnitz.de/~helmberg/GoeHelWap_R07_SIOPT.pdf, especially Example 6.
4. Frank Göring, Christoph Helmberg and Markus Wappler, *The Rotational Dimension of a Graph*, 2008 preprint, https://www.tu-chemnitz.de/mathematik/preprint/2008/PREPRINT_16.pdf, especially equations (3)–(4).
5. Miroslav Fiedler, *Absolute Algebraic Connectivity of Trees*, Linear and Multilinear Algebra 26 (1990), 85–106. DOI: 10.1080/03081089008817967 (abstract-level comparison only).
