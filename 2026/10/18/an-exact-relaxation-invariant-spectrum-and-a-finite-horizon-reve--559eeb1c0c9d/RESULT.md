# An exact relaxation-invariant spectrum and a finite-horizon reversal for cyclic relaxed Douglas–Rachford on a regular line fan

## Finding
For every integer \(m\ge 3\), let \(\theta=\pi/m\), \(c=\cos\theta\), and let \(A_0,\ldots,A_{m-1}\) be any affine lines in the Euclidean plane whose tangent directions are \((\cos(j\theta),\sin(j\theta))\). Translations are unrestricted, so the lines need not meet. For every common relaxation parameter \(0\le\lambda\le1\), the cyclic relaxed Douglas–Rachford operator defined below is affine with linear part
\[
M_\lambda=-c^m\begin{pmatrix}1&0\\\tan\theta(1-\lambda^m)&\lambda^m\end{pmatrix}.
\]
Thus its eigenvalues are precisely \(-c^m\) and \(-c^m\lambda^m\), and **its spectral radius is \(c^m\), independent of relaxation**. Every orbit converges globally to the unique fixed point, and the spectral rate is attained by a nonzero error direction.

For every integer \(k\ge1\), the exact cycle-power law is
\[
M_\lambda^k=(-c^m)^k\begin{pmatrix}1&0\\\tan\theta(1-\lambda^{mk})&\lambda^{mk}\end{pmatrix}.
\]
The full Douglas–Rachford choice \(\lambda=1\) uniquely minimizes the worst-case Euclidean error after **every positive finite number of cycles**:
\[
\|M_1^k\|_2=c^{mk}<\|M_\lambda^k\|_2\qquad (0\le\lambda<1,\ k\ge1).
\]
Therefore relaxation leaves the exact asymptotic factor unchanged on this symmetric family while strictly worsening the worst-case finite-cycle error relative to the respective fixed point. In particular, a decrease in the relaxation parameter does not accelerate this benchmark, despite the two standard endpoints being cyclic projections and cyclic Douglas–Rachford.

## Assumptions and scope
Work in \(\mathbb R^2\) with its standard Euclidean norm. For \(j=0,\ldots,m-1\), choose any affine line \(A_j=z_j+\mathbb Ru_j\), with \(u_j=(\cos(j\theta),\sin(j\theta))\). Let \(P_j\) be its Euclidean projector, let \(R_j=2P_j-I\) be its reflector, and impose cyclic indices \(A_m=A_0\). For any fixed \(\lambda\in[0,1]\), define the ordered two-set operator
\[
T_{\lambda,j}=\frac\lambda2(R_jR_{j+1}+I)+(1-\lambda)P_{j+1},
\]
and the full cycle \(F_\lambda=T_{\lambda,0}\circ T_{\lambda,1}\circ\cdots\circ T_{\lambda,m-1}\), with the rightmost pair applied first. This ordering is that of Dinh, Jansen, and Luke's cyclic relaxed method (their sets are numbered from one). The formal \(\lambda=0\) endpoint is included by its explicit formula. Offsets \(z_j\) are arbitrary and do not affect the linear part, but they can and generally do affect the fixed point. All results are exact-arithmetic statements about full cycles, not individual two-set steps or shadows.

## Proof
Set \(Q=\begin{psmallmatrix}c&-s\\s&c\end{psmallmatrix}\), where \(s=\sin\theta\), and let \(P=\begin{psmallmatrix}1&0\\0&0\end{psmallmatrix}\). The linear part of \(P_j\) is \(Q^jP Q^{-j}\). The linear part of \(R_j\) is \(Q^j(2P-I)Q^{-j}\). Denote the linear part of \(T_{\lambda,0}\) by \(L_0\), and that of \(T_{\lambda,j}\) by \(L_j\); then \(L_j=Q^jL_0Q^{-j}\), including the last wrap-around pair because \(Q^m=-I\) acts trivially by conjugation. Direct two-by-two multiplication gives
\[
L_0Q=
\frac\lambda2\bigl[(2P-I)Q(2P-I)+Q\bigr]+(1-\lambda)QP
=\begin{pmatrix}c&0\\(1-\lambda)s&\lambda c\end{pmatrix}=:K_\lambda.
\]
Here the first displayed identity uses the cyclic pair definition and the fact that the second line has tangent \(Qu_0\); it is also verifiable by substituting the two explicit rank-one projections. Multiplying the conjugated factors in cyclic order telescopes:
\[
M_\lambda=L_0L_1\cdots L_{m-1}=(L_0Q)^mQ^{-m}=-K_\lambda^m.
\]
For any integer \(r\ge1\), the lower triangular power is
\[
K_\lambda^r=\begin{pmatrix}
c^r&0\\s c^{r-1}(1-\lambda^r)&(\lambda c)^r
\end{pmatrix},
\]
because the lower-left entry is \((1-\lambda)s\sum_{j=0}^{r-1}c^{r-1-j}(\lambda c)^j=sc^{r-1}(1-\lambda^r)\), with the same formula at both endpoints by continuity. Taking \(r=m\) proves the asserted matrix and eigenvalues. Since \(0<c<1\), both eigenvalue moduli are strictly less than one. Every \(T_{\lambda,j}\) is affine, hence \(F_\lambda(x)=M_\lambda x+b_\lambda\). The matrix \(I-M_\lambda\) is invertible and determines the unique fixed point \(x_\lambda^*=(I-M_\lambda)^{-1}b_\lambda\). For all initial points \(x\) and integers \(k\ge1\),
\[
F_\lambda^k(x)-x_\lambda^*=M_\lambda^k(x-x_\lambda^*).
\]
The eigenvector \(e_2=(0,1)\) has the smaller eigenvalue, while \(v_\lambda=(1,\tan\theta)\) has eigenvalue \(-c^m\) for every \(\lambda<1\), and every nonzero direction is an eigenvector when \(\lambda=1\). This proves sharpness of the common asymptotic factor. The displayed power law follows either from the triangular formula or by substituting \(r=mk\) in \((-K_\lambda^m)^k=(-1)^kK_\lambda^{mk}\).

At \(\lambda=1\), the linear part is exactly \(M_1=-c^m I\), so \(\|M_1^k\|_2=c^{mk}\). At \(\lambda<1\), applying \(M_\lambda^k\) to the unit vector \(e_1\) yields the strictly larger norm
\[
\|M_\lambda^ke_1\|_2
=c^{mk}\sqrt{1+\tan^2\theta(1-\lambda^{mk})^2}
>c^{mk}.
\]
This proves the unique worst-case finite-horizon optimum for every \(k\). No assumption on line offsets enters any matrix calculation.

For completeness, as \(m\to\infty\), Taylor expansion gives \(\log(c^m)=-\pi^2/(2m)+O(m^{-3})\). One cycle makes \(m\) two-set updates, so the worst-case number of constituent pair updates required for a fixed positive error-reduction factor scales on the order of \(m^2\) for large \(m\), independent of \(\lambda\) at the spectral level. This asymptotic concerns the fixed point of the selected \(\lambda\), not proximity to a common feasible point.

## Verification
A standalone standard-library program `verify.py` reconstructs the full ordered product directly from projectors and reflectors for every \(3\le m\le30\), seven relaxation weights, and four cycle horizons. It checks the closed matrices, matrix powers, predicted norms, strict endpoint comparison, and the linear part of explicitly translated affine-line maps. Running `python verify.py` produced `PASS: 5528 finite independent matrix and affine checks`. These numerical computations check implementation consistency only; the proof above supplies the exact result for every integer \(m\ge3\) and every real \(\lambda\in[0,1]\).

## Relationship to prior work
Dinh, Jansen, and Luke introduce this exact ordered cyclic relaxed Douglas–Rachford operator for possibly inconsistent and nonconvex feasibility, characterize its fixed points, and prove qualitative and local quantitative convergence under regularity conditions. Their open-access full text, especially equations (2)–(3) and Sections 3–4, does not state the present regular-fan linear matrix, a relaxation-independent exact spectrum, or a sharp uniform finite-cycle norm comparison. Borwein and Tam introduce the \(\lambda=1\) cyclic Douglas–Rachford construction and norm convergence for affine subspaces; that convergence assertion neither evaluates the \(0<\lambda<1\) spectrum nor compares all relaxation parameters at every finite cycle horizon. The two-set affine-subspace and relaxed Douglas–Rachford/Friedrichs-angle literature studies an important related setting, but a two-set sharp rate does not imply the displayed all-parameter cyclic \(m\)-line matrix identity. The contribution is this explicit sharp family and its relaxation tradeoff, not the algorithm, classical projectors, or general linear convergence theory.

## Limitations
These identities hold only for an equally spaced two-dimensional line fan with a common relaxation parameter, fixed cycle order, and exact Euclidean projections. Arbitrary perturbations to the directions, nonaffine or higher-dimensional sets, independently changing parameters, and floating-point behavior are not covered. The unique finite-horizon optimum is measured as Euclidean error relative to **each method's own fixed point**; since inconsistent line offsets may give different fixed points for different \(\lambda\), it does not imply that \(\lambda=1\) minimizes a common feasibility objective, set gap, residual or wall-clock cost. This is an exact mathematical benchmark, not evidence that relaxation is generally ineffective. Earlier specialized angle-product calculations could overlap despite the full inspected cyclic papers not stating this classification; in particular, the 2018 Luke–Martins–Tam workshop presentation of relaxed cyclic DR was identified but not inspected in full.

## References
1. T. L. Dinh, G. S. M. Jansen, and D. R. Luke, *Cyclic Relaxed Douglas–Rachford Splitting for Inconsistent Nonconvex Feasibility*, arXiv:2502.12285 (public preprint 2025-02-17); *Journal of Optimization Theory and Applications* 209, article 50 (2026). https://arxiv.org/abs/2502.12285; https://doi.org/10.1007/s10957-026-02996-2.
2. J. M. Borwein and M. K. Tam, *A Cyclic Douglas–Rachford Iteration Scheme*, arXiv:1303.1859 (2013); *Journal of Optimization Theory and Applications* 160 (2014), 1–29. https://arxiv.org/abs/1303.1859.
3. H. H. Bauschke and W. M. Moursi, *The Douglas–Rachford Algorithm for Two (Not Necessarily Intersecting) Affine Subspaces*, arXiv:1504.03721 (2015), *SIAM Journal on Optimization* 26 (2016). https://arxiv.org/abs/1504.03721.
4. N. H. Thao, *A convergent relaxation of the Douglas–Rachford algorithm*, *Computational Optimization and Applications* 70 (2018), 841–863. https://doi.org/10.1007/s10589-018-9989-y.
5. D. R. Luke, A.-L. Martins, and M. K. Tam, *Relaxed Cyclic Douglas–Rachford Algorithms for Nonconvex Optimization*, ICML Workshop (2018). Full text was not inspected; identified from the source article bibliography.
