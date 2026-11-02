# Two sharp norm transitions within a five-site numerical-shadow fibre

## Finding

For every positive nilpotent five-site weighted shift, the smallest operator norm among **strictly positive weighted shifts with exactly the same complete Haar numerical shadow** has an explicit three-branch expression. The two transitions have different meanings: one is loss of attainment at a reducible boundary; the other changes the number of minimizing weight allocations from two to a one-parameter family.

Let \(A e_{j+1}=a_j e_j\) on \(\mathbb C^5\), where \(a_1,a_2,a_3,a_4>0\). Let \(J=(A+A^*)/2\), whose eigenvalues are \(\lambda_1,\lambda_2,0,-\lambda_2,-\lambda_1\), with \(\lambda_1>\lambda_2>0\). Define \(q=(\lambda_2/\lambda_1)^2\) and
\[
q_*=\frac{7-3\sqrt5}{2},\qquad
\tau(q)=\begin{cases}
\dfrac{1+q+\sqrt{(1+q)^2-8q}}4,&0<q\le q_*,\\[2mm]
\dfrac{1+q+\sqrt{(1+q)^2-5q}}5,&q_*\le q\le\frac13,\\[2mm]
q,&\frac13\le q<1.
\end{cases}
\]
For the numerical shadow \(\mu_A\) (the distribution of \(\langle Au,u\rangle\) when \(u\) is Haar-uniform on the complex unit sphere), one has
\[
\boxed{\inf\{\|B\|:\ B\text{ is a positive five-site weighted shift},\ \mu_B=\mu_A\}=2\lambda_1\sqrt{\tau(q)}.}
\]
The infimum is not attained within strictly positive weights for \(0<q\le q_*\). For \(q_*<q<1/3\), exactly two ordered positive weight strings attain it, interchanged by reversal. At \(q=1/3\) there is one minimizing positive weight string. For \(1/3<q<1/2\), minimizers form a nontrivial closed segment; for \(1/2\le q<1\), they form a nontrivial open segment, as specified precisely below.

## Assumptions and scope

All spaces are complex Euclidean with standard Hermitian norm; the matrix is unitarily phase-normalized to strictly positive upper-superdiagonal weights. We optimize only over strictly positive one-step weighted shifts in dimension five, not over arbitrary matrices sharing the shadow. The shadow is the entire probability measure, not merely its numerical-range support. The source date is the original public submission of the motivating numerical-shadow rigidity study, October 21, 2026; the earlier general determinant criterion is expressly treated as prior theory.

Set \(x_j=(a_j/(2\lambda_1))^2\), \(S=1+q\), and \(t=\max_{1\le j\le4}x_j\). The fixed-shadow feasible set in these coordinates is exactly
\[
\mathcal F_q=\{(x_1,x_2,x_3,x_4)\in(0,\infty)^4:\ \sum x_j=S,\quad x_1x_3+x_1x_4+x_2x_4=q\}.
\]
Every point in this set has Hermitian-part eigenvalues \(\pm\lambda_1,\pm\lambda_2,0\), and conversely. The operator norm equals \(2\lambda_1\sqrt{t}\).

The minimizing allocations are, with \(t=\tau(q)\):

* If \(q_*<q<1/3\), exactly \((S-3t,t,t,t)\) and \((t,t,t,S-3t)\).
* If \(q=1/3\), exactly \((1/3,1/3,1/3,1/3)\).
* If \(1/3<q<1\), exactly \((q,u,1-q-u,q)\), where \(0<u<1-q\) and \(u\le q\), \(1-q-u\le q\).
* If \(0<q\le q_*\), no strictly positive allocation attains the infimum. In the nonnegative closure an optimal allocation is \((S-2t,t,t,0)\); positive fixed-shadow allocations converge to it.

## Proof

**1. Complete-shadow parameterization.** The numerical-shadow determinant criterion of Dunkl et al. states that two matrices of a common dimension have the same Haar numerical shadow exactly when their polynomials \(\det(I-sA-tA^*)\) agree. For a five-site one-step weighted shift, a tridiagonal determinant recurrence yields
\[
\det(I-sA-tA^*)=1-st\sum_{j=1}^4a_j^2+(st)^2(a_1^2a_3^2+a_1^2a_4^2+a_2^2a_4^2).
\]
The eigenvalues of \(J\) are symmetric about zero by the alternating-sign conjugation, and strict positivity of its four Jacobi edges gives five simple eigenvalues. On putting \(s=t=1/2\), its characteristic polynomial is
\[
\det(zI-J)=z\bigl(z^4-\lambda_1^2(\sum_j x_j)z^2+\lambda_1^4(x_1x_3+x_1x_4+x_2x_4)\bigr).
\]
Consequently, precisely the two displayed constraints define the fixed-shadow fibre. Since \(A^*A\) is diagonal with entries \(0,a_1^2,a_2^2,a_3^2,a_4^2\), minimizing \(\|A\|\) is minimizing \(t\).

**2. The constrained matching-polynomial minimum.** Fix \(S>0\) and a possible cap \(t\) satisfying \(S/4\le t\le S/2\). Put \(u=x_1+x_2\), so \(S-2t\le u\le2t\). The quadratic matching expression is
\[
Q=x_1x_3+x_1x_4+x_2x_4=u(S-u)-x_2x_3.
\]
For fixed \(u\), the smallest possible \(Q\) under \(0\le x_j\le t\) is attained by \(x_2=\min(u,t)\) and \(x_3=\min(S-u,t)\). Thus the remaining scalar function is
\[
F_t(u)=u(S-u)-\min(u,t)\min(S-u,t).
\]
It is a concave quadratic on each of the intervals separated by \(u=t\) and \(u=S-t\); its minimum on the feasible interval occurs at an endpoint of one of those intervals. A direct evaluation gives the exact bound
\[
\boxed{Q\ge Q_{\min}(S,t):=\begin{cases}
2St-5t^2,&S/4\le t\le S/3,\\
t(S-2t),&S/3\le t\le S/2.
\end{cases}}
\]
Both formulas decrease strictly as \(t\) increases on their specified ranges. For \(t<S/3\), equality requires \((x_1,x_2,x_3,x_4)=(S-3t,t,t,t)\) or its reversal, apart from the all-equal junction. For \(S/3\le t<S/2\), equality requires at least one zero entry.

**3. The first two branches and nonattainment.** The spectrum-imposed invariant is \(Q=q\), with \(S=1+q\). At \(t=S/3\), the lower envelope equals \(S^2/9\). The equation \(q=S^2/9\) has its unique root in \((0,1)\) at \(q_*=(7-3\sqrt5)/2\). If \(q\le q_*\), the first feasible cap is the larger root of \(q=t(S-2t)\), namely the first displayed branch. If \(q_*\le q\le1/3\), the first feasible cap is the larger root of \(q=2St-5t^2\), the second branch; its value lies in \([S/4,S/3]\). The explicit equality configurations above prove sharpness. In the first branch every nonnegative equality configuration has a zero edge; it therefore cannot be an admissible strict weighted shift. For approach from positive edges, start at the boundary \((r,t,t,0)\), where \(r=S-2t=q/t>0\), choose a small \(\varepsilon>0\), and put
\[
x_4=\varepsilon,\quad x_3=t,\quad x_1=\frac{q-\varepsilon(S-t-\varepsilon)}t,\quad x_2=S-t-\varepsilon-x_1.
\]
These four entries are strictly positive for all sufficiently small positive \(\varepsilon\), satisfy both constraints exactly, and have maximum converging to \(t\). This includes \(q=q_*\). In the second branch the two listed positive minimizers are the only ones except at the all-equal junction.

**4. Sharp large-gap branch.** Reorder the odd and even basis coordinates of \(J/\lambda_1\). The resulting bipartite block has the \(3\times2\) matrix
\[
C=\begin{pmatrix}\sqrt{x_1}&0\\\sqrt{x_2}&\sqrt{x_3}\\0&\sqrt{x_4}\end{pmatrix}
\]
whose squared singular values are \(1\) and \(q\). Testing its least-singular-value Rayleigh quotient on \((\sqrt{x_3},-\sqrt{x_2})\) gives
\[
q\le\frac{x_1x_3+x_2x_4}{x_2+x_3}\le\max(x_1,x_4)\le t.
\]
Equality \(t=q\) with strictly positive middle entries forces \(x_1=x_4=q\). The two invariants then require \(x_2+x_3=1-q\). These middle entries can be positive and at most \(q\) precisely for \(q\ge1/3\). This proves the third branch and exhausts its equality cases; the junction \(q=1/3\) forces all four entries to equal \(1/3\).

## Verification

The companion standalone script `CHECK.py` uses deterministic finite arithmetic, spectral-invariant identities, and sampled feasible caps. It checks the two algebraic transition formulas, boundary and interior extremizing allocations, positive approximants below the first transition, and many random inequalities for the constrained matching polynomial. Run `python CHECK.py` using standard-library Python. The test run returned `CHECK_OK 3817 cases`. The universal theorem is established by the exact arguments above, **not** by sampling; finite checks do not prove global optimization.

## Relationship to prior work

Dunkl, Gawron, Holbrook, Puchała, and Życzkowski's numerical-shadow determinant criterion is an essential established input; the shadow characterization alone is not claimed new. Johnson's 2026 paper treats the rigidity problem in dimension three and discusses older non-rigid examples, but not the present five-site sharp norm minimization. The zero-diagonal Jacobi isospectral sets and their Volterra dynamics were studied by Penskoi, and more general tridiagonal isospectral topology by Martínez Torres; these concern topology/integrable dynamics rather than the exact minimax offdiagonal cap under a fixed five-point symmetric spectrum. The new contribution is the quantitative three-branch minimum and the two distinct transitions in attainment geometry.

## Limitations

The optimization is restricted to five-site strictly positive one-step nilpotent weighted shifts; no claim is made for all matrices with the same numerical shadow or for longer shifts. The infimum in the first branch is a genuine nonattained infimum, not a minimum. The proof determines the lower operator-norm envelope, not the upper envelope or every norm distribution along the fibre. Independent mathematical and publication-priority reviews have not been performed. An equivalent result in inverse eigenvalue or Jacobi minimax literature under other terminology remains a priority risk.

## References

1. D. Johnson, *Numerical Shadow Rigidity for 3×3 Matrices*, arXiv:2610.29675v1, originally publicly submitted October 21, 2026; primary MSC 47A12. https://arxiv.org/html/2610.29675v1
2. C. F. Dunkl, P. Gawron, J. A. Holbrook, J. Puchała, and K. Życzkowski, *Numerical shadows: measures and densities on the numerical range*, arXiv:1010.4189. https://arxiv.org/pdf/1010.4189
3. A. V. Penskoi, *The Volterra system and topology of the isospectral variety of zero-diagonal Jacobi matrices*, arXiv:math-ph/0701061 (2007). https://arxiv.org/abs/math-ph/0701061
4. D. Martínez Torres, *The topology of tridiagonal isospectral sets*, arXiv:2609.05733 (September 2026). https://arxiv.org/abs/2609.05733
