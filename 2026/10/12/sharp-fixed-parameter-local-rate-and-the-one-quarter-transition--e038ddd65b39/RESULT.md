# Sharp fixed-parameter local rate and the one-quarter transition for two-atom Acc-Sinkhorn

## Finding

Consider the fixed-parameter Acc-Sinkhorn iteration of Xu and Chen [1, Algorithm 1] on the positive two-atom entropy-regularized transport problem defined below. For each correlation parameter \(0<s<1\), there is a **unique** permitted tuning \(\mu_*(s)\) minimizing the spectral radius of the linearized two-sequence iteration at the optimum. Put
\[
\begin{aligned}
 a_*(s)&=\frac{\sqrt{(1-s)^4+4(1-s)(1+3s)}-(1-s)^2}{2},\\
 \mu_*(s)&=\frac{a_*(s)^2}{2},\\
 q_*(s)&=\frac{s}{1+a_*(s)}.
\end{aligned}
\]
Then \(0<a_*(s)\leq1\), so \(0<\mu_*(s)\leq1/2<1\). The least possible local spectral radius is exactly \(q_*(s)\). Ordinary normalized Sinkhorn has local spectral radius \(s^2\), and the ordering is sharp:
\[
\boxed{\quad q_*(s)>s^2\ \ (0<s<1/2),\qquad
q_*(1/2)=1/4,\qquad q_*(s)<s^2\ \ (1/2<s<1).\quad}
\]
Thus the optimally tuned fixed-parameter acceleration is locally slower than ordinary Sinkhorn below the **exact second-eigenvalue threshold \(s^2=1/4\)**, but faster above it. Every fixed choice \(0<\mu<1\) is nonetheless locally exponentially attracting on this family.

This is a statement about the asymptotic linearization of the **fixed-parameter inner algorithm** and its two-component dual state, not about the homotopy outer loop, a finite-horizon objective ordering, or global convergence.

## Assumptions and scope

Let \(s\in(0,1)\), let the prescribed row and column marginals both equal \(b=(1/2,1/2)\), and set the strictly positive balanced coupling and Gibbs kernel
\[
P_s=K_s=\frac14\begin{pmatrix}1+s&1-s\\1-s&1+s\end{pmatrix}.
\]
Every entry lies in \((0,1)\), so \(K_s=\exp(-C_s)\) for the nonnegative entropic-transport cost matrix \(C_s=-\log K_s\), with regularization coefficient one. The optimal coupling is \(P_s\) itself. Center each dual potential on \(N^\perp=\{(t,-t):t\in\mathbb R\}\), and write \(S:N^\perp\to N^\perp\) for the centered, complete row-then-column Sinkhorn log-potential step. The optimal fixed point is \(0\).

The fixed-parameter Acc-Sinkhorn state comprises \((x_k,w_k)\in N^\perp\times N^\perp\), with \(a=\sqrt{2\mu}\), \(0<\mu<1\), and source-defined updates
\[
x_{k+1}=\frac{w_k+S(x_k)}{1+a},\qquad
w_{k+1}=\frac{w_k+(a^2-2)x_{k+1}+2S(x_{k+1})}{1+a}.
\]
Use one iteration to mean one update of this pair, as in [1, Algorithm 1]. The comparison with ordinary Sinkhorn uses one complete normalized Sinkhorn step. The rate of a differentiable local iteration refers to the spectral radius of its derivative at the fixed point; at repeated eigenvalues a factor \(k\) can accompany the corresponding linearized geometric term, so no uniform \(O(q_*^k)\) assertion is made at critical tuning.

## Proof

**Step 1: the exact Sinkhorn derivative.** For a log column variable \(v\), define row scalings \(u(v)=b./(K_s\exp v)\), the row-balanced matrix \(P(v)=\operatorname{diag}(u(v))K_s\operatorname{diag}(\exp v)\), and its column vector \(c(v)=P(v)^\mathsf T\mathbf 1\). The complete column update in log variables is \(v\mapsto v+\log(b./c(v))\), followed by subtraction of its mean. At \(v=0\), both marginals equal \(b\), and differentiating the row scalings gives
\[
 Dc(0)=\operatorname{diag}(b)-P_s^\mathsf T\operatorname{diag}(b)^{-1}P_s.
\]
It follows that the centered Sinkhorn derivative is the restriction of
\[
 DS(0)=\operatorname{diag}(b)^{-1}P_s^\mathsf T
        \operatorname{diag}(b)^{-1}P_s
\]
to \(N^\perp\). Since \(\operatorname{diag}(b)^{-1}=2I\) and \(2P_s\) has the eigenvalues \(1\) and \(s\), one gets exactly \(DS(0)|_{N^\perp}=s^2 I\). Put \(\lambda=s^2\in(0,1)\). No infinitesimal rank or sign approximation is used.

**Step 2: the two-state characteristic polynomial.** Differentiating the displayed Acc-Sinkhorn recurrences and writing one coordinate for each centered two-vector gives
\[
 M(a,\lambda)=
 \begin{pmatrix}
 \lambda/(1+a)&1/(1+a)\\
 \lambda(a^2-2+2\lambda)/(1+a)^2&(a^2+a-1+2\lambda)/(1+a)^2
 \end{pmatrix}.
\]
Consequently the characteristic polynomial is
\[
p_{a,\lambda}(z)=z^2-\frac{a^2+a-1+(a+3)\lambda}{(1+a)^2}z
                   +\frac{\lambda}{(1+a)^2}.
\]
Writing its middle coefficient as \(T\) and its constant coefficient as \(D\), the exact identities
\[
\begin{aligned}
(1+a)^2(1-T+D)&=(a+2)(1-\lambda)>0,\\
(1+a)^2(1+T+D)&=2a^2+3a+(a+4)\lambda>0,\\
D&=\lambda/(1+a)^2<1
\end{aligned}
\]
imply by the real quadratic Schur/Jury criterion that the two eigenvalues are strictly inside the open unit disk for every \(0<a<\sqrt2\), which is the source-permitted range. Standard smooth fixed-point stability then gives local exponential attraction (at any rate strictly above the derivative spectral radius and below one).

**Step 3: the unique spectral optimum.** Put \(r=s\). The equation that \(p_{a,r^2}\) have the repeated **positive** root \(q=r/(1+a)\) is precisely
\[
G_r(a):=a^2+(1-r)^2a-(1-r)(1+3r)=0.
\]
Since \(G_r(0)<0\) and \(G'_r(a)=2a+(1-r)^2>0\) for \(a>0\), this has one positive root \(a_*(r)\), given by the formula above. Moreover, \(G_r(1)=(2r-1)^2\ge0\), so \(a_*(r)\le1\), strictly unless \(r=1/2\). At that root the characteristic trace equals \(2r/(1+a_*)\) and the determinant equals \(r^2/(1+a_*)^2\), establishing the double positive eigenvalue \(q_*=r/(1+a_*)\).

For **every** \(0<a<a_*\), the product of the two eigenvalues implies
\[
\rho(M(a,r^2))\ge \sqrt{\det M(a,r^2)}=\frac{r}{1+a}>q_*.
\]
For **every** \(a>a_*\), evaluate the characteristic polynomial at the fixed number \(q_*\). The resulting polynomial in \(a\) is
\[
F(a)=(1+a)^2q_*^2-\bigl(a^2+a-1+(a+3)r^2\bigr)q_*+r^2.
\]
At \(a=a_*\), \(F(a_*)=0\), and its first and second derivatives satisfy
\[
F'(a_*)=-q_*\bigl(2a_*+(1-r)^2\bigr)<0,
\qquad F''(a)=2q_*(q_*-1)<0.
\]
Thus \(F(a)<0\) for every \(a>a_*\). A real quadratic with positive leading coefficient and negative value at \(q_*>0\) has a real root strictly larger than \(q_*\); hence \(\rho(M(a,r^2))>q_*\). Together the two inequalities prove unique global minimization over the entire admissible fixed-parameter range \(0<\mu<1\).

**Step 4: exact acceleration versus slowdown frontier.** The condition \(q_*<r^2\) is equivalent to \(a_*>r^{-1}-1\). Strict monotonicity of \(G_r\), combined with the exact identity
\[
G_r(r^{-1}-1)=\frac{(r-1)(r+1)^2(2r-1)}{r^2},
\]
shows that this inequality holds precisely when \(r>1/2\); the reverse holds for \(r<1/2\), and equality holds at \(r=1/2\). Since ordinary Sinkhorn has local derivative \(r^2\), the three-way comparison follows. As \(r\uparrow1\), the quadratic root additionally gives \(a_*(r)=2\sqrt{1-r}+O(1-r)\) and \(q_*(r)=1-2\sqrt{1-r}+O(1-r)\).

## Verification

The self-contained standard-library script `verify.py` recomputes the rational trace, determinant, and Jury identities; the algebraic critical-root conditions at 70-digit precision; the strict minimax inequalities on explicit grids; and finite differences of the **nonlinear** two-atom Sinkhorn and Acc-Sinkhorn updates. It returns `VERIFY_OK 173 arithmetic and nonlinear finite-difference test cases` with the tested script. These tests are corroboration of the complete analytic proof above, not a replacement for its universal quantifiers.

A reproducible parameter example is \(s=1/2\): then \(a_*=1\), \(\mu_*=1/2\), and both optimal Acc-Sinkhorn and ordinary Sinkhorn have factor \(1/4\). At \(s=1/10\), optimal Acc-Sinkhorn has factor \(2/35\), which exceeds ordinary Sinkhorn's \(1/100\). At \(s=9/10\), optimal Acc-Sinkhorn has factor approximately \(0.5613433511\), below ordinary Sinkhorn's \(0.81\).

## Relationship to prior work

Xu and Chen [1] introduce exactly the two-sequence update studied here and establish a global \(O(1/k^2)\) bound for their homotopy strategy subject to a stability condition. Their Algorithm 1 and appendices give the iteration and reduced-dual differential structure, but do not state the sharp fixed-parameter two-atom spectral optimizer or its one-quarter comparison with ordinary Sinkhorn. The result here is not a rephrasing of their global theorem.

Gao, Qu, Ye, and Udell [2] prove a tight nonasymptotic local rate for **ordinary** Sinkhorn and develop distinct accelerated algorithms, notably online scaling and preconditioned accelerated gradient descent. Their local spectral-gap discussion supports the ordinary-Sinkhorn benchmark but neither establishes nor directly implies the Acc-Sinkhorn recurrence's fixed-parameter spectral minimax formula.

Thibault, Chizat, Dossal, and Papadakis [3] analyze an **overrelaxed alternating-projection/SOR** variant and derive its optimal local relaxation rate from the same Sinkhorn singular-value data. That method's scalar tuning parameter acts on a different iteration matrix; its known optimization is not the minimization proved here, and this result makes no claim to beat overrelaxed Sinkhorn.

## Limitations

The result applies only to strictly positive symmetric balanced \(2\times2\) kernels and constant \(\mu\); it does not analyze a changing-homotopy schedule, arbitrary marginals, multiple independent singular modes, numerical rounding, or global attraction. The spectral radius is an asymptotic **linearized dual-state** factor; objective gaps generally scale quadratically in small errors. The minimizing Jacobian has a repeated eigenvalue and is not diagonalizable, so generic linearized errors can contain a polynomial prefactor. No direct numerical iteration bound with optimal prefactor is asserted. Exact equivalence to an unindexed momentum or matrix-scaling analysis in earlier literature is a residual originality risk.

## References

[1] Zeyi Xu and Long Chen, *Accelerating Sinkhorn for Entropy-Regularized Optimal Transport*, arXiv:2605.30267v1 (first public version 2026-05-28); expanded arXiv:2605.30267v2 (2026-06-01), Sections 3–4, Algorithm 1, Appendix A.3. https://arxiv.org/html/2605.30267v2

[2] Wenzhi Gao, Zhaonan Qu, Yinyu Ye, and Madeleine Udell, *Tight Nonasymptotic Local Convergence of Sinkhorn-Knopp*, arXiv:2608.11760v1 (2026-08-12), Sections 3, 4.4–4.5, Algorithm 3. https://arxiv.org/html/2608.11760v3

[3] Alexis Thibault, Lénaïc Chizat, Charles Dossal, and Nicolas Papadakis, *Overrelaxed Sinkhorn–Knopp Algorithm for Regularized Optimal Transport*, arXiv:1711.01851 (first posted 2017); *Algorithms* **14** (2021), 143, Section 4.4, Proposition 2. https://arxiv.org/html/1711.01851v2
