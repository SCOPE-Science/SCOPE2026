# Reverse-order averaging cancels first-order underrelaxation bias in cyclic block Kaczmarz

## Result

Let \(P_1,\ldots,P_m\) be orthogonal projectors on \(\mathbb R^n\), and let
\(q_i\in\operatorname{range}(P_i)\). For \(0<\lambda<2\), define the relaxed affine
projection

\[
T_i^\lambda x=(I-\lambda P_i)x+\lambda q_i.
\]

Assume

\[
S:=\sum_{i=1}^m P_i \succ 0.
\]

Then the quadratic objective

\[
F(x)=\frac12\sum_{i=1}^m \|P_i x-q_i\|_2^2
\]

has the unique minimizer

\[
x_* = S^{-1}\sum_{i=1}^m q_i.
\]

For a permutation \(\pi=(\pi_1,\ldots,\pi_m)\), let one cyclic sweep be

\[
K_{\pi,\lambda}
=
T_{\pi_m}^\lambda\circ\cdots\circ T_{\pi_1}^\lambda,
\]

and let \(z_\pi(\lambda)\) be its fixed point. Let
\(\pi^R=(\pi_m,\ldots,\pi_1)\) be the reversed order.

### Theorem

For every \(0<\lambda<2\), each sweep \(K_{\pi,\lambda}\) has a unique fixed point,
and complete sweeps converge linearly to it. As \(\lambda\downarrow0\),

\[
z_\pi(\lambda)
=
x_*+\lambda h_\pi+O(\lambda^2),
\]

where

\[
h_\pi
=
S^{-1}
\sum_{1\le p<q\le m}
P_{\pi_q}r_{\pi_p},
\qquad
r_i:=P_i x_*-q_i.
\]

The reverse order has exactly the opposite first-order bias,

\[
h_{\pi^R}=-h_\pi.
\]

Consequently,

\[
\boxed{
\frac{z_\pi(\lambda)+z_{\pi^R}(\lambda)}{2}
=
x_*+O(\lambda^2)
}
\qquad(\lambda\downarrow0).
\]

Thus the two individual cyclic limits are generally only first-order accurate in
the underrelaxation parameter, while their forward/reverse midpoint is
second-order accurate.

This applies directly to ordinary and block Kaczmarz. For normalized row
Kaczmarz, \(P_i=u_i u_i^\top\) and \(q_i=\beta_i u_i\), where
\(u_i=a_i/\|a_i\|_2\) and \(\beta_i=b_i/\|a_i\|_2\). Then \(x_*\) minimizes

\[
\sum_i \frac{(a_i^\top x-b_i)^2}{\|a_i\|_2^2},
\]

the weighted least-squares objective that appears in the classical strong
underrelaxation theorem. For a block \(A_i x=b_i\), one may take
\(P_i=A_i^\dagger A_i\) and \(q_i=A_i^\dagger b_i\).

## Proof

### 1. Existence and uniqueness of each cyclic limit

Write \(M_i=I-\lambda P_i\). Since \(P_i=P_i^\top=P_i^2\),

\[
\|M_i v\|_2^2
=
\|v\|_2^2-\lambda(2-\lambda)\|P_i v\|_2^2.
\]

Hence \(M_i\) is nonexpansive for \(0<\lambda<2\), with equality in norm exactly
when \(P_i v=0\).

The linear part of a full sweep is

\[
Q_{\pi}(\lambda)
=
M_{\pi_m}\cdots M_{\pi_1}.
\]

If a nonzero vector \(v\) satisfied
\(\|Q_\pi(\lambda)v\|_2=\|v\|_2\), equality would have to hold at every factor in
the nonexpansive chain. The first equality gives
\(P_{\pi_1}v=0\), so the first factor leaves \(v\) unchanged; then the next gives
\(P_{\pi_2}v=0\), and so on. Thus \(P_i v=0\) for every \(i\). But

\[
v^\top S v=\sum_i\|P_i v\|_2^2,
\]

and \(S\succ0\), so \(v=0\), a contradiction. Compactness of the unit sphere
therefore gives

\[
\|Q_\pi(\lambda)\|_2<1.
\]

The affine sweep has a unique fixed point
\((I-Q_\pi(\lambda))^{-1}c_\pi(\lambda)\), and complete sweeps converge to it
linearly.

### 2. First-order expansion of the fixed point

Let

\[
d=\sum_i q_i.
\]

Expanding the ordered product gives

\[
Q_\pi(\lambda)
=
I-\lambda S+\lambda^2 B_\pi+O(\lambda^3),
\]

with

\[
B_\pi
=
\sum_{1\le p<q\le m}
P_{\pi_q}P_{\pi_p}.
\]

The affine term in one sweep is

\[
c_\pi(\lambda)
=
\lambda d-\lambda^2 e_\pi+O(\lambda^3),
\]

where

\[
e_\pi
=
\sum_{1\le p<q\le m}
P_{\pi_q}q_{\pi_p}.
\]

Because \(S\) is invertible,

\[
I-Q_\pi(\lambda)
=
\lambda\bigl(S-\lambda B_\pi+O(\lambda^2)\bigr)
\]

has, after division by \(\lambda\), an invertible analytic continuation at
\(\lambda=0\). Therefore \(z_\pi(\lambda)\) is analytic near zero. Write

\[
z_\pi(\lambda)=x_*+\lambda h_\pi+O(\lambda^2).
\]

Substituting into
\((I-Q_\pi(\lambda))z_\pi(\lambda)=c_\pi(\lambda)\), the order-\(\lambda\)
equation is \(Sx_*=d\). The order-\(\lambda^2\) equation is

\[
S h_\pi-B_\pi x_*=-e_\pi,
\]

hence

\[
S h_\pi
=
\sum_{p<q}
P_{\pi_q}\bigl(P_{\pi_p}x_*-q_{\pi_p}\bigr)
=
\sum_{p<q}P_{\pi_q}r_{\pi_p}.
\]

This proves the stated first-order coefficient.

### 3. Reversing the order flips the first-order coefficient

Since \(x_*\) minimizes \(F\),

\[
\sum_i r_i
=
\sum_i(P_i x_*-q_i)
=
Sx_*-d
=
0.
\]

Also \(r_i\in\operatorname{range}(P_i)\), so \(P_i r_i=r_i\).

For the reverse permutation,

\[
S h_{\pi^R}
=
\sum_{p<q}P_{\pi_p}r_{\pi_q}.
\]

Adding the two coefficients,

\[
\begin{aligned}
S(h_\pi+h_{\pi^R})
&=
\sum_{p<q}
\left(
P_{\pi_q}r_{\pi_p}+P_{\pi_p}r_{\pi_q}
\right)\\
&=
\sum_{j=1}^m P_j\sum_{i\ne j}r_i\\
&=
-\sum_{j=1}^m P_j r_j\\
&=
-\sum_{j=1}^m r_j\\
&=0.
\end{aligned}
\]

Since \(S\) is invertible, \(h_{\pi^R}=-h_\pi\). Averaging the two analytic
expansions cancels the entire first-order term and yields the \(O(\lambda^2)\)
midpoint estimate.

## Sharpness

The quadratic order cannot in general be improved.

Take \(n=1\), \(m=3\), \(P_1=P_2=P_3=1\), and
\((q_1,q_2,q_3)=(0,0,1)\). Then \(x_*=1/3\).
For the order \((1,2,3)\),

\[
z_{\rm f}(\lambda)
=
\frac{1}{3-3\lambda+\lambda^2},
\]

while for the reverse order,

\[
z_{\rm r}(\lambda)
=
\frac{(1-\lambda)^2}{3-3\lambda+\lambda^2}.
\]

Their midpoint satisfies the exact identity

\[
\frac{z_{\rm f}(\lambda)+z_{\rm r}(\lambda)}2-\frac13
=
\frac{\lambda^2}
{6(3-3\lambda+\lambda^2)}
=
\frac{\lambda^2}{18}+O(\lambda^3).
\]

Thus the midpoint error is generically capable of having a nonzero second-order
coefficient.

## Relation to known results

Censor, Eggermont and Gordon (1983) proved the strong-underrelaxation limit for
inconsistent Kaczmarz and block-Kaczmarz: as the relaxation parameter tends to
zero, cyclic limit points approach the weighted least-squares solution. The
statement above refines that limit locally by giving the first-order
order-dependent bias and showing that reversing the order negates it.

Later Kaczmarz literature contains exact least-squares extensions, randomized
variants, block variants, and symmetric forward/backward sweeps. In particular,
symmetric Kaczmarz/SOR performs a forward sweep followed by a backward sweep as
one composite iteration. That construction is different from taking the
arithmetic mean of the two separate cyclic fixed points considered here.

Forward/reverse averaging is also a standard second-order symmetrization device
in operator-splitting time integrators. That generic observation motivates a
useful comparison, but it does not itself identify the fixed-point expansion
above, the residual formula for \(h_\pi\), or the cancellation of the
strong-underrelaxation bias for inconsistent cyclic projections.

Searches through the current Kaczmarz survey and targeted literature queries did
not locate this fixed-point bias formula or the reverse-order midpoint theorem.
The originality claim is therefore only to the best of our knowledge; see the
limitations below.

## Computational interpretation

The theorem is for deterministic exact-arithmetic projection operators. A
forward sweep uses the blocks in one fixed order and a reverse sweep uses the
opposite order. To obtain the midpoint numerically, one may converge the two
cyclic processes separately at the same relaxation parameter and average their
corresponding phase-fixed points.

The result is an asymptotic accuracy statement in \(\lambda\), not a complexity
claim. Strong underrelaxation can make convergence to a cyclic limit slow.
Running two cyclic solves can therefore require more computational work than using a dedicated
least-squares solver such as CGLS, LSQR, or an extended Kaczmarz method. The
theorem instead identifies a simple bias-cancellation mechanism and a diagnostic
for order effects.

## Limitations

- The stated theorem is finite-dimensional and assumes orthogonal projectors.
- \(S=\sum_i P_i\) must be positive definite; rank-deficient problems require a
  separate treatment on the identifiable subspace or with a minimum-norm
  convention.
- The \(O(\lambda^2)\) statement is asymptotic as \(\lambda\downarrow0\); no
  uniform finite-\(\lambda\) constant is claimed.
- The two opposite cyclic fixed points must be obtained accurately enough that
  iteration error does not dominate the \(O(\lambda^2)\) bias.
- No floating-point stability or solver-speed advantage over modern least-squares
  solvers is claimed.
- The full text of Censor--Eggermont--Gordon (1983) was not inspected
  end-to-end; its abstract and later descriptions of its theorem were checked.
  A hidden rate expansion or order-symmetrization result in that paper would
  reduce originality.
- The full text of Popa (1995) was not inspected; its abstract describes two
  Kaczmarz-based algorithms converging to a least-squares solution. A
  specialized forward/reverse construction there remains a residual
  originality risk.
- Generic symmetrically weighted sequential splitting is established in the
  time-integration literature, so the broad idea of averaging opposite orders
  is not new. The claimed contribution is specifically the cyclic-projection
  fixed-point expansion and its least-squares bias cancellation.

## References

1. Y. Censor, P. P. B. Eggermont, D. Gordon, “Strong underrelaxation in
   Kaczmarz's method for inconsistent systems,” *Numerische Mathematik* 41
   (1983), 83–92. https://doi.org/10.1007/BF01396307
2. C. Popa, “Least-squares solution of overdetermined inconsistent linear
   systems using Kaczmarz's relaxation,” *International Journal of Computer
   Mathematics* 55 (1995), 79–89.
   https://doi.org/10.1080/00207169508804364
3. C. Popa, “Extensions of block-projections methods with relaxation parameters
   to inconsistent and rank-deficient least-squares problems,” *BIT Numerical
   Mathematics* 38 (1998), 151–176. https://doi.org/10.1007/BF02510922
4. D. Dax, “The Rate of Convergence of the SOR Method in the Positive
   Semidefinite Case,” *Computational and Mathematical Methods* (2022).
   https://doi.org/10.1155/2022/6143444
5. “Survey of a class of iterative row-action methods: The Kaczmarz method,”
   *Numerical Algorithms* (2024/2025).
   https://doi.org/10.1007/s11075-024-01945-2
6. “Application of operator splitting to the Maxwell equations including a
   source term,” *Applied Numerical Mathematics* 59 (2009), 522–541.
   https://doi.org/10.1016/j.apnum.2008.03.031
