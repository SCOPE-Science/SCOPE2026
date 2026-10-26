# A sharp curvature–mixing stability frontier for two-agent gradient tracking

## Finding

For the two-agent gradient-tracking iteration and normalized common step \(\alpha=1/\bar h\), **convergence from every correctly gradient-initialized primal pair** is equivalent to
\[
J(\lambda,d^2):=1+\lambda-\lambda^2+\lambda(1-\lambda)d^2-\lambda^2d^4>0.
\]
Here \(\lambda=2w-1\) is the non-consensus eigenvalue of the communication matrix and \(d=(h_1-h_2)/(h_1+h_2)\) measures relative curvature mismatch. The inequality yields a complete, sharp phase diagram:

1. For \(-1/3\le\lambda<1\), every \(|d|<1\) converges.
2. For \(1/3<t<(\sqrt5-1)/2\), where \(t=-\lambda\), convergence holds if and only if
   \[
   d^2<\frac{\sqrt{5-2t-3t^2}-(1+t)}{2t}.
   \]
3. For \((\sqrt5-1)/2\le t<1\), no admissible curvature mismatch, including zero, permits universal convergence at this step.

All inequalities are strict when they define a stability boundary. At equality, universal convergence fails; the boundary has a conjugate pair of eigenvalues of modulus one.

## Assumptions and scope

Fix \(h_1,h_2>0\), arbitrary real centers \(b_1,b_2\), and \(0<w<1\). Let
\[
f_i(x)=\tfrac12 h_i(x-b_i)^2,\quad
W=\begin{pmatrix}w&1-w\\1-w&w\end{pmatrix},\quad
\bar h=(h_1+h_2)/2,\quad \alpha=1/\bar h,
\]
and let \(x_\star=(h_1b_1+h_2b_2)/(h_1+h_2)\). The tracker and primal updates are exactly
\[
x_{k+1}=W(x_k-\alpha y_k),\qquad
y_{k+1}=Wy_k+H(x_{k+1}-x_k),\qquad H=\operatorname{diag}(h_1,h_2),
\]
where \(y_{i,0}=h_i(x_{i,0}-b_i)\). Both components of \(x_k\) must converge to \(x_\star\) **for every** \(x_0\in\mathbb R^2\). Correct gradient initialization is essential. If all centers vanish, it becomes the simpler initialization \(y_{i,0}=h_ix_{i,0}\). No claim concerns arbitrary, inconsistent initial tracker states.

## Proof

**Reduction.** Write \(x_c=(x_1+x_2)/2\), \(x_d=(x_1-x_2)/2\), \(e_c=x_c-x_\star\), and \(e_d=x_d\). Let \(z_c=\alpha(y_1+y_2)/2\), \(z_d=\alpha(y_1-y_2)/2\), \(\lambda=2w-1\), and \(d=(h_1-h_2)/(h_1+h_2)\). Since averaging preserves the total tracker increment, the gradient-initialized trajectory obeys the exact invariant
\[
z_{c,k}=e_{c,k}+d e_{d,k}\quad\text{for every }k\ge0.
\]
Directly transforming the two update equations, and eliminating \(e_c\) through this invariant, gives
\[
\begin{pmatrix}z_{c,k+1}\\e_{d,k+1}\\z_{d,k+1}\end{pmatrix}
=A_{\lambda,d}\begin{pmatrix}z_{c,k}\\e_{d,k}\\z_{d,k}\end{pmatrix},\quad
A_{\lambda,d}=\begin{pmatrix}
0&d(\lambda-1)&-d\lambda\\
0&\lambda&-\lambda\\
-d&\lambda-1&0
\end{pmatrix}.
\]
The primal error recovers as \(e_c=z_c-d e_d\). The characteristic polynomial is
\[
p(z)=z^3-\lambda z^2+\lambda(\lambda-1-d^2)z+\lambda d^2.
\]

**Exact Schur test.** For a real monic cubic \(p(z)=z^3+az^2+bz+c\), the Schur reduction of \(p\) is
\[
\frac{p(z)-c z^3p(1/z)}{z}
=(1-c^2)z^2+(a-bc)z+(b-ac).
\]
The ordinary quadratic disk test shows that all cubic roots have modulus below one precisely when
\[
|c|<1,\quad p(1)>0,\quad -p(-1)>0,\quad 1-b+ac-c^2>0.
\]
For clarity, the final quadratic inequality not displayed in this list is already implied: adding the two endpoint inequalities for the reduced quadratic gives \(1+b-ac-c^2>0\). In our case the four quantities become
\[
|\lambda|d^2<1,\quad p(1)=(1-\lambda)^2>0,
\quad -p(-1)=1+\lambda^2-2\lambda d^2>0,
\]
and
\[
1-b+ac-c^2=1+\lambda-\lambda^2+\lambda(1-\lambda)d^2-\lambda^2d^4=J(\lambda,d^2).
\]
The first three are strictly positive under the stated parameter restrictions; thus \(\rho(A_{\lambda,d})<1\) if and only if \(J>0\).

**Phase diagram.** Set \(u=d^2\in[0,1)\). For \(0\le\lambda<1\), \(J(\lambda,u)\) is concave in \(u\), with \(J(\lambda,0)=1+\lambda-\lambda^2>0\) and \(J(\lambda,1)=(1-\lambda)(1+3\lambda)>0\). For \(\lambda=-t\), \(0<t<1\),
\[
J(-t,u)=1-t-t^2-t(1+t)u-t^2u^2.
\]
This expression is strictly decreasing in \(u\), with \(J(-t,0)=1-t-t^2\) and \(J(-t,1)=(1+t)(1-3t)\). Hence all \(u<1\) are admissible up to \(t=1/3\); for \(1/3<t<(\sqrt5-1)/2\), the unique root lies strictly between zero and one and has the asserted radical formula. For larger \(t\), even \(u=0\) fails. At \(J=0\), the polynomial factors as
\[
p(z)=(z+c)\bigl(z^2+(a-c)z+1\bigr),\qquad a=t,\quad c=-tu.
\]
The quadratic has two distinct unit-circle roots because \(0<t(1+u)<2\).

**Necessity for actual initialized trajectories.** The Schur test characterizes the reduced matrix on the full three-dimensional space. It also characterizes *universal primal convergence despite the gradient-initialization restriction*: varying \(x_0\) changes the reduced initial vector along the two directions
\[
v_1=(1,0,d)^\top,\qquad v_2=(d,1,1)^\top.
\]
A direct determinant computation gives \(\det[v_1,v_2,A_{\lambda,d}v_2]=\lambda-1\ne0\). If every initialized primal trajectory converged to \(x_\star\), differences between any two such trajectories would have both primal errors tending to zero. For \(\lambda\ne0\), the relation \(e_{d,k+1}=\lambda(e_{d,k}-z_{d,k})\) also forces \(z_{d,k}\to0\), and the invariant forces \(z_{c,k}\to0\). Therefore \(A^kv_1,A^kv_2,A^{k+1}v_2\to0\); these three vectors span, giving \(A^k\to0\), hence \(\rho(A)<1\). When \(\lambda=0\), the displayed matrix is nilpotent, so the conclusion holds directly. Conversely \(\rho(A)<1\) implies every reduced error tends to zero and hence both primal components converge to \(x_\star\). This completes necessity and sufficiency, including non-convergence at the boundary.

## Verification

The standalone `VERIFY.py` performs exact symbolic verification of the reduced characteristic polynomial, the two endpoint conditions, the remaining Schur expression and the determinant \(\lambda-1\); it independently expands the original update equations to check each reduced-state equation. `CHECKS.txt` contains the actual script output. Numerical eigenvalue checks at selected interior and exterior points are included as diagnostics, not used to prove the global inequalities. As a transparent benchmark, for \(\lambda=-1/2\), the exact mismatch boundary is
\[
d^2=(\sqrt{13}-3)/2,
\]
with stability at \(d=1/2\) and failure at \(d=3/5\). The proof above, not finite tests, establishes all quantified claims.

## Relationship to prior work

Wang et al. (2026, arXiv:2608.03548v1), equations (2) and (8), provide the specific gradient-tracking iteration and general reduced matrix, prove the complete-mixing optimum \(\alpha=1/\bar h\), and give a conservative certificate for general curvature heterogeneity. The result here is the exact **heterogeneous two-agent** stability frontier for that distinguished, already-motivated step. The recent exact worst-case DIGing/AugDGM analyses of Tian, Chai and Xu (2026, arXiv:2607.23601v1) concern distinct tracker-update orders and worst-case classes; neither supplies this two-agent polynomial or fixed-instance curvature threshold. A published homogeneous-curvature graph-specific tuning result (published-finding corpus record below) treats \(d=0\) and optimal common-step choice over all steps, not the nonzero-curvature-mismatch frontier. These comparisons concern mathematical implications rather than matching terminology.

## Limitations

The theorem is only for two scalar agents, positive curvatures, positive self/edge weights, the stated communication matrix, a **common** stepsize equal to the reciprocal *average* curvature, and correctly initialized gradient tracking. It neither optimizes the stepsize for non-complete graphs nor gives a convergence criterion for arbitrary graphs, vector objectives, changing weights, mismatched tracker initialization, or nonlinear costs. The previously derived general reduced-state formalism makes the cubic obtainable, but the precise strict phase boundary must still be established. Completeness of all global literature cannot be guaranteed.

## References

- Y. Wang, L. Ballotta, R. Carli, A. Iannelli, X. Cao, and L. Schenato, *Adaptive Stepsizes With Certified Convergence in Distributed Gradient Tracking With Quadratic Costs*, arXiv:2608.03548v1, first posted 2026-08-04, https://arxiv.org/html/2608.03548v1.
- Q. Tian, L. Chai, and J. Xu, *Exact Worst-case Convergence Rates of Distributed Gradient Tracking Methods*, arXiv:2607.23601v1, first posted 2026-07-26, https://arxiv.org/abs/2607.23601.
- *Exact sign-aware graph-specific tuning for homogeneous distributed gradient tracking*, published scientific finding, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-sign-aware-graph-specific-tuning-for-homogeneous-distribut--4bef30512fd6.
