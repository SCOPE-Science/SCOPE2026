# Pentagonal locking and residue-sensitive finite Turán defects for a five-point cyclic support

## Finding
For each integer \(N\geq9\), let \(G_N=\mathbb Z/N\mathbb Z\), \(\Omega_N=\{0,\pm1,\pm4\}\subset G_N\), and set
\[
T_N=\max\left\{\sum_{x\in G_N}f(x):f(0)=1,\ \operatorname{supp}f\subseteq\Omega_N,\ f\text{ positive definite}\right\}.
\]
The sum uses counting measure. Put \(c=\cos(\pi/5)=(1+\sqrt5)/4\). Then
\[
T_N=\sqrt5\quad\Longleftrightarrow\quad5\mid N,\qquad T_N>\sqrt5\quad\text{if }5\nmid N.
\]
For each nonzero residue \(r\in\{1,2,3,4\}\), as \(N\to\infty\) with \(N\equiv r\pmod5\),
\[
T_N=\sqrt5+\frac{C_r}{N^2}+O_r(N^{-3}),\qquad
C_1=C_4=\frac{48\pi^2}{25c},\quad C_2=C_3=\frac{32\pi^2}{25c}.
\]
Furthermore, for every sufficiently large \(N\) not divisible by five, there is exactly one **real-even** optimizing positive-definite function. Its coefficients at \(\pm1\) and \(\pm4\) are uniquely fixed by the two equalities
\[
1+2a_N\cos\frac{2\pi j}{N}+2b_N\cos\frac{8\pi j}{N}=0,
\qquad j=\left\lfloor\frac{2N}{5}\right\rfloor,
\left\lfloor\frac{2N}{5}\right\rfloor+1.
\]
In particular the two-contact equations supply an explicit finite trigonometric formula for the unique real-even optimum in that range. The theorem does **not** assert uniqueness among complex-valued optimizers or that this two-contact formula applies to every small modulus.

## Assumptions and scope
A function \(f:G_N\to\mathbb C\) is positive definite when \(\sum_{u,v}z_u\overline{z_v}f(u-v)\geq0\) for all complex coefficient vectors. The finite Fourier criterion makes this equivalent to nonnegativity of all Fourier coefficients. The objective is real for positive-definite functions. Replacing \(f\) by its real part retains positivity and its objective; thus the optimum is attained among real-even functions. As \(N\geq9\), the five support residues are distinct, and such a function is uniquely specified by \(a=f(1)=f(-1)\) and \(b=f(4)=f(-4)\). The Fourier conditions are
\[
P_{a,b}(\theta_j)=1+2a\cos\theta_j+2b\cos4\theta_j\geq0,
\qquad\theta_j=2\pi j/N,\quad 0\leq j<N,
\]
and the objective is \(1+2(a+b)\). The feasible set is compact because positive definiteness and \(f(0)=1\) imply \(|a|,|b|\leq1\). Throughout, \(O_r\) permits a constant depending on the fixed residue, not on \(N\).

## Proof
**Continuous witness and pentagonal locking.** Put
\[
a_0=\frac{2(\sqrt5-1)}5,\quad b_0=\frac{\sqrt5-1}{10},\quad
s_0=a_0+b_0=\frac{\sqrt5-1}{2},\quad \varphi=\frac{1+\sqrt5}{2}.
\]
Writing \(x=\cos\theta\) and \(\cos4\theta=8x^4-8x^2+1\), direct expansion gives
\[
P_{a_0,b_0}(\theta)=\frac{8(\sqrt5-1)}5(x+c)^2\left(x^2-\varphi x+\frac{1+3\sqrt5}{8}\right).
\]
The final quadratic has discriminant \(1-\sqrt5<0\), so the trigonometric polynomial is nonnegative for every real \(\theta\) and has zeros exactly at \(\theta=\pm4\pi/5\pmod{2\pi}\). Its objective is \(1+2s_0=\sqrt5\). If \(5\mid N\), the grid contains \(4\pi/5\), where both \(\cos\theta\) and \(\cos4\theta\) equal \(-c\). Consequently every feasible pair obeys \(1-2c(a+b)\geq0\), implying \(1+2(a+b)\leq1+1/c=\sqrt5\). If \(5\nmid N\), all sampled values of \(P_{a_0,b_0}\) are strictly positive. With finitely many grid sites, a sufficiently small positive common scaling \((a_0,b_0)\mapsto((1+\epsilon)a_0,(1+\epsilon)b_0)\) preserves all inequalities. It strictly increases the objective; hence \(T_N>\sqrt5\).

**Eventual two-contact optimum.** Fix a nonzero residue modulo five. Let \(\theta_*=4\pi/5\), \(h=2\pi/N\), \(u=\{2N/5\}\in\{1/5,2/5,3/5,4/5\}\), and let \(\theta_- =\theta_*-hu\) and \(\theta_+=\theta_*+h(1-u)\) be consecutive sample points. For sufficiently small \(h\), the matrix with rows \((\cos\theta_\pm,\cos4\theta_\pm)\) is invertible: its determinant has leading term \(-5c\sin(\pi/5)h\), which is nonzero. Let \((a_N,b_N)\) be the unique solution of \(P_{a_N,b_N}(\theta_-)=P_{a_N,b_N}(\theta_+)=0\). A two-equation Taylor expansion at the double zero shows \((a_N,b_N)=(a_0,b_0)+O(h)\).

This candidate is feasible for every sufficiently large modulus in the fixed residue class. Indeed, away from the two zeros \(\pm\theta_*\), the continuous witness is bounded positively and the candidate converges uniformly to it. In fixed small neighborhoods of the two zeros the witness has positive second derivative \(P_{a_0,b_0}''(\pm\theta_*)=4\), hence the candidate is strictly convex there for large \(N\). Its two consecutive grid zeros near \(\theta_*\), together with their reflections near \(-\theta_*\), force every other grid value in those neighborhoods to be strictly positive: a strictly convex function with zero values at two points is positive to either side of their interval. No grid point lies strictly between consecutive nodes. Thus all sampled Fourier values are nonnegative.

For sharpness, write \(v(\theta)=(\cos\theta,\cos4\theta)\). The unique weights solving
\[
\lambda_-v(\theta_-)+\lambda_+v(\theta_+)=-(1,1)
\]
satisfy \(\lambda_-=(1-u)/c+O(h)\), \(\lambda_+=u/c+O(h)\). They are therefore both positive for large \(N\). For any feasible \((a,b)\), multiply its two Fourier constraints by the respective weights and add to obtain
\[
0\leq\lambda_-P_{a,b}(\theta_-)+\lambda_+P_{a,b}(\theta_+)
=\lambda_-+\lambda_+-2(a+b).
\]
Our candidate attains equality, so it maximizes \(a+b\). Every real-even maximizer must make both positively weighted constraints equal zero; invertibility forces the same \((a_N,b_N)\). This proves eventual uniqueness in the real-even class.

**Sharp residue correction.** Write \(s=a+b\), \(b=b_0+\delta b\), \(s=s_0+\delta s\), and \(\Delta_-= -hu\), \(\Delta_+=h(1-u)\). For \(P(s,b;\theta)=1+2s\cos\theta+2b(\cos4\theta-\cos\theta)\), the relevant derivatives at \((s_0,b_0,\theta_*)\) are
\[
P=P_\theta=0,\quad P_{\theta\theta}=4,\quad P_s=-2c,\quad P_b=0,\quad P_{\theta b}=10\sin(\pi/5).
\]
The two contact equations first yield \(\delta b=O(h)\), \(\delta s=O(h^2)\), then more precisely, with \(v=\sin(\pi/5)\),
\[
0=-2c\delta s+10v\Delta_\pm\delta b+2\Delta_\pm^2+O(h^3).
\]
Subtracting the two equations gives \(\delta b=-(\Delta_-+\Delta_+)/(5v)+O(h^2)\); substitution gives \(\delta s=-\Delta_-\Delta_+/c+O(h^3)=h^2u(1-u)/c+O(h^3)\). Therefore
\[
T_N=1+2s_N=\sqrt5+\frac{8\pi^2u(1-u)}{cN^2}+O(N^{-3}).
\]
For residues \(r=1,4\), \(u(1-u)=6/25\); for residues \(r=2,3\), it is \(4/25\). These are exactly the two stated constants. There are only four nonzero residue classes, so eventual conclusions hold uniformly for all sufficiently large nonmultiples of five.

## Verification
Run \(\texttt{python3 check.py}\) using the standard library. The program verifies the displayed factorization at 2001 test points, directly compares the proposed optimizer with all two-constraint intersections of the bounded finite linear program for \(9\le N\le60\), checks nonnegative grid values and positive two-contact dual weights for \(61\le N\le400\), and tests convergence along all four nonzero residue classes through moduli above 6000. Its deterministic execution passed 5190 assertions. These finite checks do not establish the infinite statements; those follow from the displayed analytic arguments. Full proof requires neither probabilistic simulation nor third-party packages.

## Relationship to prior work
Kolountzakis and Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218 (first posted 2003-12-10), Example 3, **already proves** the \(\sqrt5\) continuous optimum for the integer group support \(\{0,\pm1,\pm4\}\), as part of its \(\{0,\pm1,\pm2n\}\) family. That continuous optimum and its witness are not claimed as new. The contribution here concerns finite cyclic groups with varying modulus, exact divisibility locking, two-contact optimality, and the residue-dependent second-order defect. Their earlier *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193 (first posted 2003-02-17), introduces the discretized Carathéodory–Fejér framework, but its first-harmonic objective is different from this total-mass objective. The closest examined mathematical research records address \(\{0,\pm1,\pm3\}\) or different sparse harmonic objectives; their statements do not imply this modulus-five theorem through a parameter substitution.

## Limitations
The eventual two-contact formula has no explicit minimum modulus proved here, although finite cases were checked. Only real-even optimizer uniqueness is claimed; complex optimizers can have imaginary parts without changing the real-even symmetrization. The exact value of \(T_N\) for arbitrary small \(N\) not divisible by five is not presented in closed form beyond the finite linear program. The published literature search was bounded; an older finite-grid theorem or unexamined equivalent specialization could cover the claimed arithmetic refinement. The result is not independently audited.

## References
- M. N. Kolountzakis and Sz. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193, first public version 2003-02-17, https://arxiv.org/html/math/0302193v1.
- M. N. Kolountzakis and Sz. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218, first public version 2003-12-10, https://arxiv.org/html/math/0312218v1, especially Example 3.
