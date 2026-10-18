# Sharp relaxation windows and two universal stability barriers for a four-operator splitting method

## Finding

The finite-parameter four-operator splitting iteration of Alcantara, Lee, and Takeda has an exact Schur-stability window on a scalar strongly convex difference-of-quadratics problem, and two distinct sharp thresholds for per-instance and robust relaxation. Write \(u=\eta F\), \(v=\eta P\), where \(F>P\geq0\), \(\eta>0\), and let \(\tau>0\) denote relaxation. The complete state \((y_k,z_k)\) converges geometrically to the minimizer from **every** real initialization if and only if
\[
\max\!\left\{0,\frac{(v-1)(1+u)}{v+1}\right\}<\tau<\frac{2(1+u)(v+3)}{u+v+2}.
\]
For fixed \(u>0\), there exists some relaxation depending on \(v\) that works for **each** \(0\leq v<u\) if and only if \(u<17\). A **single** relaxation working for **every** \(0\leq v<u\) exists if and only if
\[
0<u<\frac{5+\sqrt{57}}2.
\]
The robust statement is pointwise in \(v\), not a claimed uniform spectral gap as \(v\uparrow u\).

A smooth genuine weak-concavity example shows this obstruction is not an artifact of a purely concave quadratic. For \(f(x)=10x^2\), \(g=h=0\), and
\[
p(x)=-\tfrac52x^2+\tfrac52(1-\cos x)^2,
\]
with \(\alpha=\beta=1\) and \(\gamma=1/2\), the objective is globally \(5\)-strongly convex, \(-p\) is \(5/8\)-weakly convex, and the splitting map's fixed point at the unique minimizer is linearly unstable for **every** \(\tau>0\).

## Assumptions and scope

Consider the scalar objective \(\Psi(x)=f(x)+g(x)+h(x)+p(x)\), with \(f(x)=Fx^2/2\), \(p(x)=-Px^2/2\), \(g=h=0\), \(F>P\geq0\), and fixed \(\eta>0\). Thus \(\Psi(x)=(F-P)x^2/2\) has the unique minimizer zero. Fix the published finite-parameter update \(\alpha=\beta=\eta\), \(\gamma=\eta/2\) (which satisfies \(1/\gamma=1/\alpha+1/\beta\)) and arbitrary \(\tau>0\). Interpret \(T_{\beta p}(y)=y-\beta p'(y)\), and use the exact proximal mappings. The state is the pair \((y,z)\), with \(x=z/(1+u)\). All convergence classifications are **from every deterministic initial pair**. The separate smooth example uses the same update with specified functions and parameters.

## Proof

**1. Exact reduction.** Algorithm 1, equations (3.1)–(3.3) of the source, gives
\[
x_k=\frac{z_k}{1+u},\qquad
 y_{k+1}=\frac{1+v}{2}y_k+\frac{1-u}{2(1+u)}z_k,
\qquad z_{k+1}=z_k+\tau(y_{k+1}-x_k).
\]
Consequently, with \(s_k=(y_k,z_k)^\top\),
\[
s_{k+1}=M s_k,\quad
M=\begin{pmatrix}
(1+v)/2&(1-u)/(2(1+u))\\
\tau(1+v)/2&1-\tau/2
\end{pmatrix}.
\]
Let \(T=\operatorname{tr}M=(v+3-\tau)/2\) and \(D=\det M=(1+v)(1-\tau/(1+u))/2\). The three strict quadratic Jury inequalities, necessary and sufficient for both eigenvalues to lie in the open unit disk, simplify to
\[
1-T+D=\frac{\tau(u-v)}{2(1+u)}>0,\quad
1+T+D=v+3-\frac{\tau(u+v+2)}{2(1+u)}>0,
\]
\[
1-D=\frac{1-v}{2}+\frac{\tau(1+v)}{2(1+u)}>0.
\]
Write \(L(u,v)=\max\{0,(v-1)(1+u)/(v+1)\}\) and \(U(u,v)=2(1+u)(v+3)/(u+v+2)\). The first inequality is automatic from the assumptions; the other two give exactly \(L(u,v)<\tau<U(u,v)\). At either endpoint of a nonempty stability interval, a strict Jury condition becomes equality, so convergence from every initial pair fails. This is an equivalence of spectral stability and all-state geometric convergence, not merely a local empirical criterion.

**2. Fixed-pair feasibility and its sharp collision.** For \(v\leq1\), the lower bound is zero; the upper bound is positive. For \(v>1\), comparing the two positive endpoints gives
\[
L<U\quad\Longleftrightarrow\quad
u<v+8+\frac{16}{v-1}=:u_c(v).
\]
At \(u=u_c(v)\), both endpoints equal \(v+7\), and direct multiplication gives \((M+I)^2=0\ne M+I\): there is a nontrivial Jordan block at eigenvalue \(-1\). When \(u>u_c(v)\), every \(\tau>0\) is unstable: for \(\tau<L\), \(D>1\); for \(\tau\ge L>U\), \(\det(-I-M)=1+T+D<0\), so a real eigenvalue lies below \(-1\). For \(v>1\), setting \(w=v-1>0\) gives \(u_c(v)=9+w+16/w\ge17\), with equality uniquely at \(v=5\). Hence for each \(u<17\) every \(v<u\) admits some relaxation; for each \(u\ge17\), the allowed choice \(v=5\) makes convergence impossible for every relaxation.

**3. One relaxation across every concave curvature.** For fixed \(u>0\), \(L(v)\) is nondecreasing in \(v\), while \(U(v)=2(1+u)(v+3)/(u+v+2)\) is strictly increasing in \(v\), because \(u>0\). For \(u>1\), \(\sup_{v<u}L(v)=u-1\) (approached only as \(v\uparrow u\)), whereas \(\min_{0\le v<u}U(v)=U(0)=6(1+u)/(u+2)\). Thus a single \(\tau\) works for all such \(v\) precisely when \(u-1<U(0)\), equivalently \(u^2-5u-8<0\); for \(1<u<(5+\sqrt{57})/2\), \(\tau=u-1\) is an explicit working choice. For \(0<u\le1\), \(\tau=1\) works. At equality of the robust endpoints no \(\tau\) is feasible: a \(\tau\) at or above \(U(0)\) fails for \(v=0\), and a smaller \(\tau\) fails for sufficiently large \(v<u\). The same argument handles all larger \(u\).

**4. Genuine nonquadratic weak-concavity obstruction.** Set \(f(x)=10x^2\) and \(p(x)=-5x^2/2+5(1-\cos x)^2/2\). Then
\[
p''(x)=-5+5(\cos x-\cos2x),\quad
-2\leq \cos x-\cos2x\leq9/8,
\]
where \(\cos x-\cos2x=-2(\cos x-1/4)^2+9/8\), and both extreme values are attained. Therefore \(-15\le p''\le5/8\), showing \(L_p=5/8>0\) is the exact weak-convexity modulus for \(-p\), while \(\Psi''(x)=20+p''(x)\ge5\). The unique minimizer is zero. Taking \(\alpha=\beta=1\le1/L_p=8/5\) and \(\gamma=1/2\) yields the exact smooth map
\[
x=z/21,\quad y^+=\tfrac12(2x-z)+\tfrac12(y-p'(y)),\quad z^+=z+\tau(y^+-x).
\]
Its derivative at \((y,z)=(0,0)\) is \(M(20,5,\tau)\), because \(p''(0)=-5\). Here \(u=20>u_c(5)=17\), so for every \(\tau>0\), this Jacobian has a multiplier of modulus strictly greater than one. The classical linearized-instability theorem for continuously differentiable discrete maps proves instability of the fixed point; it does not claim all initial points diverge, nor that nonlinear trajectories have the linear recurrence globally.

## Verification

The self-contained Python/SymPy program `verification.py` symbolically reconstructs the full matrix, trace, determinant, all three Schur inequalities, collision identity and Jordan block; checks the exact smooth witness and its Jacobian; and makes 1,000 independent direct-map/spectral comparisons plus 200 dimensional scaling checks. Run `python verification.py` with Python 3 and SymPy. Its numerical tests supplement, but do not replace, the algebraic proofs for continuous parameter ranges. The stand-alone program does not require any external data or files.

## Relationship to prior work

Alcantara, Lee, and Takeda (2024, arXiv:2406.16025v1), Algorithm 1 and their later exposition, introduce the four-operator update and obtain convergence under sufficient parameter restrictions; the algorithm itself, its operator-splitting interpretation, and the use of weakly concave terms are entirely prior work. The original source specifically favors \(\beta=\infty\) when \(L_p=0\); the quadratic calculation here concerns the algebraically permitted **finite** choice \(\alpha=\beta\), not that particular recommended limit. The nonquadratic witness has \(L_p>0\) and uses the finite-parameter regime. Dao, Pham, and Tung (2024, arXiv:2405.08485v1) analyze a related doubly relaxed forward-Douglas–Rachford framework under different parametrization and provide sufficient convergence conditions. These inspected analyses do not state the precise three-part Schur classification, the two sharp universal curvature thresholds, or the strongly convex smooth instability witness. No assertion of absolute priority is made beyond the scope of the comparisons.

## Limitations

The exact global convergence window is a scalar quadratic, equal-finite-stepsize result; it is not a general result for arbitrary nonsmooth functions or matrix-valued Hessians. The robust statement requires a common relaxation only, not a rate uniformly bounded away from one as \(v\uparrow u\). The nonlinear witness proves **local fixed-point instability**, not global divergence of all trajectories or failure under parameter values satisfying the source's small-stepsize sufficient convergence hypotheses. The weak-concavity modulus refers to \(-p\), and \(\beta\le1/L_p\) alone does not imply convergence for arbitrarily large \(\alpha\). Earlier equivalent scalar reductions under different terminology remain a literature risk; independent validation is not implied.

## References

1. J. H. Alcantara, C.-p. Lee, and A. Takeda, *A four-operator splitting algorithm for nonconvex and nonsmooth optimization*, arXiv:2406.16025v1 (public 2024-06-23), https://arxiv.org/pdf/2406.16025v1; revised public text https://arxiv.org/html/2406.16025v3; SIAM Journal on Optimization 35 (2025), 1846–1872, doi:10.1137/24M1672067.
2. M. N. Dao, T. N. Pham, and P. T. Tung, *Doubly relaxed forward-Douglas–Rachford splitting for the sum of two nonconvex and a DC function*, arXiv:2405.08485v1 (2024), https://arxiv.org/abs/2405.08485.
3. E. I. Jury, *Inners and Stability of Dynamic Systems*, Wiley (1974), standard second-degree Schur/Jury criterion (used directly and proved equivalent through explicit inequalities above).
