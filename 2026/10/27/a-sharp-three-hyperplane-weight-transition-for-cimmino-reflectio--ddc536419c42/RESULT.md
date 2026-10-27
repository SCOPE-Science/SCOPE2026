# A sharp three-hyperplane weight transition for Cimmino reflections

## Finding

The first nontrivial three-row symmetric correlation family has an exact, globally optimal positive weighting for the simultaneous-reflection (weighted Cimmino) iteration. Two distinct spectral regimes meet at the sharp surface \(c^2=2d^2/(1+d)\). Before the transition the limiting error norm is attained on all three spectral modes; after the transition only the two modes of the symmetric subspace determine the minimax factor. Equal relative row weights are rate-optimal exactly when all three off-diagonal correlations coincide.

For \(0<d<1\) and \(0<c<\sqrt{(1+d)/2}\), set \(h=1+d\) and \(s=2d^2/h\). Define
\[
z_*(c,d)=\begin{cases}
\dfrac{d(1-d)}{d-c^2},&c^2\le s,\\[2mm]
h,&c^2\ge s,
\end{cases}\qquad
q_*(c,d)=\begin{cases}
\dfrac{2d^2-(3d-1)c^2}{2d-(1+d)c^2},&c^2\le s,\\[2mm]
c\sqrt{\dfrac2{1+d}},&c^2\ge s.
\end{cases}
\]
These formulas agree at equality and satisfy \(0<q_*<1\). The globally optimal weights include \(w=\tau_*(z_*,1,1)\), where \(\tau_*>0\) is specified in the proof. For \(c>0\), the optimal ratio \(z_*\) among weights with the last two components equal is unique. More particularly, \(z_*<1\) for \(c<d\), \(z_*=1\) for \(c=d\), and \(z_*>1\) for \(c>d\). Equal relative weights are globally rate-optimal if and only if \(c=d\).

At the exact rational witness \(c=1/4\), \(d=1/2\), the optimum is \(w=(16,28,28)/29\) with sharp contraction \(15/29\). Even after optimizing a common weight, equal relative weights only achieve \((3+\sqrt3)/(7+\sqrt3)>15/29\). This is not merely an ordering effect: each individual row remains fixed, and only the positive simultaneous-reflection weights are changed.

## Assumptions and scope

Let \(r_1,r_2,r_3\in\mathbb R^3\) be linearly independent real unit *row* vectors with Gram matrix
\[
G=(r_i r_j^{\mathsf T})_{i,j=1}^3=
\begin{pmatrix}1&c&c\\c&1&d\\c&d&1\end{pmatrix}.
\]
The parameter inequalities above imply \(G\succ0\), since its eigenvalue in the antisymmetric row combination is \(1-d>0\) and its remaining positive-definite block has determinant \(1+d-2c^2>0\). Conversely, every such \(G\) is realized by three linearly independent unit row vectors (for example, by a Cholesky factor).

For any consistent nonsingular three-row system, consider the exact-arithmetic positive-weight simultaneous projection/reflection error step
\[
e^+=M(w)e,\qquad M(w)=I-\sum_{i=1}^3w_i r_i^{\mathsf T}r_i,\qquad w_i>0.
\]
Here the row normals are regarded as rows in the displayed Gram matrix; the outer products \(r_i^{\mathsf T}r_i\) are \(3\times3\). The objective is the worst-case Euclidean **one-step solution-error** ratio \(\sup_{e\ne0}\|e^+\|_2/\|e\|_2=\|M(w)\|_2\), not the matrix-condition number itself, the residual norm, an averaged noise model, or an iteration count. There is no prescribed normalization on the positive weights; a common relaxation scale is optimized too.

## Proof

**1. Global symmetrization.** Write \(R\) for the nonsingular matrix of the three row normals, so \(RR^{\mathsf T}=G\). Exchanging row labels two and three leaves \(G\) invariant. Accordingly an orthogonal change of coordinates on \(\mathbb R^3\) implements this exchange of the outer products. Therefore \(\|M(w_1,w_2,w_3)\|_2=\|M(w_1,w_3,w_2)\|_2\). Since the spectral norm is convex as a function of the three weights, replacing \((w_2,w_3)\) by their common arithmetic mean cannot increase the objective. Hence a global minimizer can be selected with \(w_2=w_3\); it suffices to optimize \(w=\tau(z,1,1)\) with \(\tau,z>0\). All weight vectors remain strictly positive.

**2. Exact spectrum and optimal common scale.** The positive eigenvalues of \(\sum_i w_i r_i^{\mathsf T}r_i\) agree with those of \(\operatorname{diag}(\sqrt w)G\operatorname{diag}(\sqrt w)\). Without the common factor \(\tau\), the eigenvalues are
\[
\lambda_0=1-d,\qquad \lambda_\pm(z)=\frac{z+h\pm\sqrt{(z-h)^2+8zc^2}}{2},\qquad h=1+d.
\]
In particular \(\lambda_+(z)>\lambda_0\). Let \(m(z)=\min\{\lambda_0,\lambda_-(z)\}\), \(L(z)=\lambda_+(z)\). For fixed \(z\), the exact minimax common scale is \(\tau(z)=2/(m(z)+L(z))\), which balances the two endpoint errors. Its best contraction factor is
\[
q(z)=\frac{L(z)-m(z)}{L(z)+m(z)}.
\]
Minimizing \(q(z)\) is equivalent to minimizing the condition ratio \(L(z)/m(z)\).

**3. Locate the unique possible mode crossing.** The lower symmetric-block eigenvalue \(\lambda_-(z)\) equals the fixed antisymmetric mode \(1-d\) precisely when
\[
2d\bigl(z-(1-d)\bigr)-2zc^2=0,
\]
which admits a positive solution exactly when \(c^2<d\), namely \(z_0=d(1-d)/(d-c^2)\). The lower eigenvalue starts at zero as \(z\downarrow0\) and tends to \(h-2c^2\) as \(z\to\infty\). Thus, if \(c^2<d\), the smaller extreme eigenvalue is \(\lambda_-(z)\) for \(z<z_0\) and \(\lambda_0\) for \(z>z_0\); if \(c^2\ge d\), it is always \(\lambda_-(z)\).

**4. Globally optimize the shape.** On any region with \(m(z)=\lambda_-(z)\),
\[
\frac{\lambda_+(z)-\lambda_-(z)}{\lambda_+(z)+\lambda_-(z)}
=\sqrt{1-\frac{4z(h-2c^2)}{(z+h)^2}}.
\]
Because \(h-2c^2>0\), this expression decreases strictly for \(0<z<h\) and increases strictly for \(z>h\). On any region with \(m(z)=\lambda_0\), the ratio \(L(z)/\lambda_0\) increases strictly with \(z\): \(L(z)\) is the largest eigenvalue of the entrywise-increasing positive symmetric \(2\times2\) matrix \(\begin{psmallmatrix}z&c\sqrt{2z}\\c\sqrt{2z}&h\end{psmallmatrix}\), and \(c>0\). Consequently the global optimal shape is \(z_*=\min\{h,z_0\}\) when the crossing exists, and \(z_*=h\) otherwise. The condition \(z_0\le h\) simplifies exactly to \(c^2\le 2d^2/h\). Notice that \(2d^2/h<d\) for \(0<d<1\); this gives the stated exhaustive two-branch formula. The monotonicity also makes \(z_*\) unique among symmetric weight shapes.

**5. Evaluate both branches.** In the crossing regime, \(\lambda_-(z_*)=\lambda_0=1-d\) and \(L(z_*)=z_*+2d\), so \(\tau_*=2/(z_*+d+1)\) and
\[
q_* =\frac{z_*+3d-1}{z_*+d+1}
=\frac{2d^2-(3d-1)c^2}{2d-(1+d)c^2}.
\]
In the other regime, \(z_*=h\) and the endpoint eigenvalues are \(h\pm c\sqrt{2h}\), so \(\tau_*=1/h\) and \(q_*=c\sqrt{2/h}\). Equality of the two expressions at \(c^2=2d^2/h\) follows by substitution.

**6. Equal-weight criterion and rational witness.** The crossing branch satisfies \(z_*<1\), \(=1\), or \(>1\) exactly when \(c<d\), \(c=d\), or \(c>d\), respectively; the other branch has \(z_*=h>1\). As the global symmetric minimizer has a unique shape, equal relative weights are globally optimal exactly for \(c=d\). For \(c=1/4\), \(d=1/2\), the unscaled optimum spectrum is \(\{1/2,1/2,11/7\}\), whence \(z_*=4/7\), \(\tau_*=28/29\), \(w=(16,28,28)/29\) and \(q_*=15/29\). At equal relative weights, the unscaled extreme eigenvalues are \(1/2\) and \((5+\sqrt3)/4\), giving \(q_{\mathrm{equal}}=(3+\sqrt3)/(7+\sqrt3)>15/29\). This proves the strict separation.

## Verification

Run `python check.py` with Python 3, NumPy and SymPy. It checks determinant and branch-matching identities symbolically, the exact rational witness algebraically, 4,200 arbitrary positive-weight spectral comparisons against the claimed optimum, and 350 independently constructed real row matrices. The tests are finite diagnostics; the universal minimax assertion is supported by steps 1–6 of the proof.

## Relationship to prior work

Sharma (2026) formulates positive-weight Cimmino error propagation spectrally and identifies globally optimal unit weights for the two-row system. The present result addresses the first nonsymmetric three-row weight pattern, with both relative weights and the common relaxation scale free. This is not a claim to have introduced weighted simultaneous projections or spectral-radius optimization.

The general matrix-scaling and diagonal-preconditioning problems are classical; in particular, Boyd et al.'s 1994 LMI treatment formulates diagonal condition optimization as a generalized eigenvalue problem, and Shapiro (1985), Qu et al. (2022), and Ghadimi et al. (2025) develop broader optimal-scaling frameworks. The asserted distinct contribution is an analytic two-branch minimax formula and an exact symmetry-breaking criterion for this prescribed two-correlation Gram family, not a general solution method. Numerical optimization under the broader frameworks could of course reproduce individual values from the formula.

## Limitations

The claim is restricted to strictly positive correlation parameters with \(0<d<1\), \(0<c<\sqrt{(1+d)/2}\), three independent real normalized rows, arbitrarily positive weights, and exact arithmetic. No stability assertion for roundoff, asynchronous updating, randomized row selection, inconsistent least squares, non-Euclidean norms, or larger unconstrained Gram matrices follows. The result concerns a one-step spectral contraction, which implies a geometric exact-arithmetic error bound but is not an iteration-count comparison for any stopping tolerance. Related closed-form cases in older matrix-scaling literature may require further historical comparison; see the scientific review.

## References

- H. Sharma, *Sharp Convergence Rates and Optimal Weights for Cimmino's Reflection Algorithm*, arXiv:2605.24692 (first posted 2026-05-23), https://arxiv.org/abs/2605.24692.
- M. Guida and C. Sbordone, *The Reflection Method for the Numerical Solution of Linear Systems*, SIAM Review 65 (2023), https://doi.org/10.1137/22M1470463.
- A. Shapiro, *Optimal Block Diagonal \(\ell_2\)-Scaling of Matrices*, SIAM Journal on Numerical Analysis 22 (1985), 81–94, https://doi.org/10.1137/0722005.
- S. Boyd, L. El Ghaoui, E. Feron and V. Balakrishnan, *Linear Matrix Inequalities in System and Control Theory*, SIAM (1994), Sections 3.1–3.2, https://web.stanford.edu/~boyd/lmibook/.
- Z. Qu, W. Gao, O. Hinder, Y. Ye and Z. Zhou, *Optimal Diagonal Preconditioning*, arXiv:2209.00809 (2022), https://arxiv.org/abs/2209.00809.
- S. Ghadimi et al., *New Insights and Algorithms for Optimal Diagonal Preconditioning*, arXiv:2509.23439 (2025), https://arxiv.org/abs/2509.23439.
