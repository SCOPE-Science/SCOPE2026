# Sharp catalyst-basin dichotomy for an irreversible reaction-diffusion system

## Result

Consider the catalytic irreversible reaction-diffusion system of Nguyen and Tang on a smooth bounded connected domain \(\Omega\subset\mathbb R^n\), normalized by \(|\Omega|=1\), with homogeneous Neumann boundary conditions:
\[
\begin{aligned}
a_t-d_1\Delta a&=b(c-a),\\
b_t-d_2\Delta b&=b(c-a),\\
c_t-d_3\Delta c&=-b(c-a),
\end{aligned}
\qquad d_1,d_2,d_3>0,
\]
for bounded nonnegative initial data. The conserved masses are
\[
M_1=\int_\Omega(a+c),\qquad M_2=\int_\Omega(b+c).
\]
Assume the coexistence regime
\[
M_2\le M_1<2M_2.
\]
Then the two nonnegative equilibria compatible with the masses are
\[
E_+=\left(\frac{M_1}{2},\ M_2-\frac{M_1}{2},\ \frac{M_1}{2}\right)
\]
and
\[
E_\partial=(M_1-M_2,0,M_2).
\]

### Theorem: exact basin dichotomy

Let \((a,b,c)\) be the global bounded classical solution in the setting above and let
\[
B_0:=\int_\Omega b_0(x)\,dx.
\]
Then exactly one of the following holds.

1. If \(B_0=0\), equivalently \(b_0\equiv0\) almost everywhere, then \(b\equiv0\) for all time and
   \[
   (a(t),b(t),c(t))\longrightarrow E_\partial
   \]
   in \(L^2(\Omega)^3\) (indeed the \(a\)- and \(c\)-components are independent Neumann heat flows).

2. If \(B_0>0\), then
   \[
   (a(t),b(t),c(t))\longrightarrow E_+
   \]
   in \(L^2(\Omega)^3\). Consequently, once the trajectory enters the local basin from Theorem 2.7 of Nguyen--Tang, the convergence is exponential.

Thus the basin of the boundary equilibrium inside this mass class is exactly the invariant catalyst-free face \(b_0\equiv0\). Every datum carrying any positive total catalyst mass converges to the positive equilibrium.

This also gives a sharp correction to the literal conjecture stated in the source paper: the phrase "any solution with non-negative initial data" cannot include \(b_0\equiv0\), since the boundary equilibrium itself, and in fact the entire face \(b_0\equiv0\), is invariant. After adding the necessary hypothesis \(\int b_0>0\), the intended global-attraction statement holds.

## Proof

Set
\[
\mathcal H(t):=\frac12\bigl(\|a(t)\|_2^2+\|c(t)\|_2^2\bigr).
\]
Multiplying the \(a\)- and \(c\)-equations by \(a\) and \(c\), integrating, and using the Neumann conditions gives the exact identity
\[
\mathcal H'(t)
=-d_1\|\nabla a\|_2^2-d_3\|\nabla c\|_2^2
-\int_\Omega b(c-a)^2\,dx\le0. \tag{1}
\]
Hence \(\mathcal H(t)\) has a finite limit and
\[
\int_0^\infty \bigl(\|\nabla a(t)\|_2^2+\|\nabla c(t)\|_2^2\bigr)\,dt<\infty. \tag{2}
\]
The uniform \(L^\infty\) bounds and heat regularization established for this system in Theorem 2.1 of the source give uniform positive-time \(H^2\) control for \(a,c\). As in Proposition 2.5 of the source, the time derivatives of the two gradient energies are therefore bounded. Combining this with (2) yields
\[
\|\nabla a(t)\|_2+\|\nabla c(t)\|_2\longrightarrow0. \tag{3}
\]

Write
\[
C(t):=\int_\Omega c(x,t)\,dx,
\qquad
B(t):=\int_\Omega b(x,t)\,dx=M_2-C(t).
\]
The first conservation law gives \(\int a=M_1-C(t)\). By Poincare--Wirtinger and (3),
\[
\|a-(M_1-C)\|_2+\|c-C\|_2\longrightarrow0. \tag{4}
\]
Let \(m=M_1/2\). Orthogonal decomposition around the spatial averages gives
\[
\mathcal H(t)
=\frac12\|a-(M_1-C)\|_2^2
 +\frac12\|c-C\|_2^2
 +(C-m)^2+m^2. \tag{5}
\]
Since the first two terms tend to zero and \(\mathcal H(t)\) converges, \(|C(t)-m|\) has a limit. If that limit is zero then \(C(t)\to m\). If it is positive, continuity of \(C\) prevents infinitely many crossings of \(m\) for large time, so \(C(t)\) again has a limit. Denote it by \(c_\infty\), and set
\[
a_\infty=M_1-c_\infty,
\qquad
B_\infty=M_2-c_\infty.
\]
Equation (4) then gives
\[
a(t)\to a_\infty,
\qquad
c(t)\to c_\infty
\quad\text{in }L^2. \tag{6}
\]

Integrating the \(b\)-equation gives
\[
B'(t)=\int_\Omega b(c-a)\,dx. \tag{7}
\]
Put \(\delta=c_\infty-a_\infty\). Since \(b\) is uniformly bounded in \(L^\infty\), it is uniformly bounded in \(L^2\), and (6) implies
\[
B'(t)-\delta B(t)
=\int_\Omega b\bigl[(c-a)-\delta\bigr]dx\longrightarrow0. \tag{8}
\]
Because \(B(t)\to B_\infty\), (8) shows that \(B'(t)\) has the limit \(\delta B_\infty\). A differentiable function with a finite limit cannot have a nonzero limiting derivative, hence
\[
\delta B_\infty=0. \tag{9}
\]
There are therefore only two possibilities:

- If \(\delta=0\), then \(a_\infty=c_\infty=m\) and
  \[
  B_\infty=M_2-m=:b_*>0,
  \]
  which is the positive equilibrium branch.
- If \(\delta\ne0\), then \(B_\infty=0\), so \(c_\infty=M_2\), \(a_\infty=M_1-M_2\): this is the boundary branch.

It remains to show convergence of \(b\). On the boundary branch, nonnegativity and the uniform \(L^\infty\) bound imply
\[
\|b(t)\|_2^2\le \|b(t)\|_\infty B(t)\longrightarrow0. \tag{10}
\]
On the positive branch, put \(q=b-B(t)\), so \(\int q=0\), and \(w=c-a\). Since \(B'=\int bw\), multiplication of the equation for \(q\) by \(q\) gives
\[
\frac12\frac d{dt}\|q\|_2^2
=-d_2\|\nabla q\|_2^2+\int_\Omega qbw\,dx.
\]
With the Neumann spectral gap \(\lambda_1>0\) and the uniform bound \(\|b\|_\infty\le\mathcal K\),
\[
\frac d{dt}\|q\|_2^2
\le-d_2\lambda_1\|q\|_2^2
 +\frac{\mathcal K^2}{d_2\lambda_1}\|w\|_2^2. \tag{11}
\]
By (6), \(\|w(t)\|_2\to0\), so (11) implies \(\|q(t)\|_2\to0\). Together with \(B(t)\to b_*\), this proves \(b(t)\to b_*\) in \(L^2\).

We now identify which branch is selected. If \(B_0=0\), nonnegativity gives \(b_0\equiv0\), and uniqueness for the linear equation
\[
b_t-d_2\Delta b=(c-a)b
\]
forces \(b\equiv0\). The remaining equations are uncoupled Neumann heat equations, hence the boundary branch is selected.

Suppose instead \(B_0>0\). Assume for contradiction that the boundary branch is selected. Then (10) and interpolation with the uniform \(L^\infty\) bound give \(b(t)\to0\) in every finite \(L^p\). Likewise (6) gives convergence of \(a,c\) in every finite \(L^p\). Applying the Neumann heat-semigroup estimate on a unit time interval to the \(a\)- and \(c\)-equations, with any \(p>n/2\), upgrades this to
\[
a(t)\to M_1-M_2,
\qquad
c(t)\to M_2
\quad\text{uniformly on }\Omega. \tag{12}
\]
Since
\[
2M_2-M_1=2b_*>0,
\]
(12) gives, for all sufficiently large \(t\),
\[
c(x,t)-a(x,t)\ge b_*>0
\qquad\text{for all }x\in\Omega. \tag{13}
\]
Therefore
\[
B'(t)=\int_\Omega b(c-a)\,dx\ge b_*B(t). \tag{14}
\]
Moreover \(B(t)>0\) for every finite \(t\): the global uniform bounds imply \(B'\ge-2\mathcal K B\), so Gronwall gives a positive lower bound at each fixed time from \(B_0>0\). Equation (14) would then force exponential growth of \(B\), contradicting the conservation-law bound \(0\le B(t)\le M_2\). Thus the boundary branch is impossible when \(B_0>0\), and the positive equilibrium is globally selected.

Finally, convergence in \(L^2\) implies that the trajectory eventually enters the small neighborhood required by Theorem 2.7 of Nguyen--Tang. Restarting the autonomous system at that time yields the stated eventual exponential convergence.

## Structural interpretation

The same quadratic energy used by Nguyen--Tang to prove global convergence in the boundary-only regime already contains a global selector in the coexistence regime. Its two possible asymptotic energy levels differ by
\[
\mathcal H(E_\partial)-\mathcal H(E_+)
=\left(M_2-\frac{M_1}{2}\right)^2=b_*^2.
\]
The catalyst equation then makes the boundary state repelling from every trajectory with positive total catalyst mass: near \(E_\partial\), the invasion rate \(c-a\) tends to \(2b_*>0\). The only way to converge to the boundary equilibrium is therefore to lie exactly on the invariant face \(b\equiv0\).

## Relation to the source paper

Nguyen and Tang prove global exponential convergence when \(M_1<M_2\), global convergence to the boundary equilibrium when \(M_1\ge2M_2\), local exponential stability of the positive equilibrium in the coexistence regime, and nonlinear Lyapunov instability of the boundary equilibrium there. They explicitly leave open whether a trajectory that leaves a neighborhood of the boundary equilibrium could later return and converge to it, and state a global-attraction conjecture for nonnegative initial data.

The theorem above closes that return-to-boundary question for system (1.1) and gives the exact basin decomposition. It also identifies a necessary exception to the literal conjecture: \(b_0\equiv0\) is an invariant face containing the boundary equilibrium, so no statement covering all nonnegative initial data can send that face to \(E_+\).

## Limitations

- The result concerns the catalytic system (1.1) with the homogeneous Neumann boundary conditions and bounded classical solutions in the setting of the source paper.
- The basin statement uses \(M_2\le M_1<2M_2\); at \(M_1=2M_2\) the positive equilibrium collides with the boundary equilibrium and \(b_*=0\).
- The proof gives a qualitative global selection theorem and then invokes the source paper's local theorem for the eventual exponential rate; it does not provide a new explicit global decay constant from time zero.
- The result does not address the different symmetric irreversible network (1.5) studied later in the source paper.

## References

1. T. L. Nguyen and B. Q. Tang, *Stability analysis of irreversible chemical reaction-diffusion systems with boundary equilibria*, Z. Angew. Math. Phys. **77**, 199 (2026). https://doi.org/10.1007/s00033-026-02847-0
2. T. L. Nguyen and B. Q. Tang, arXiv:2410.22928. https://arxiv.org/abs/2410.22928
