# Condition nine is the sharp positivity frontier for optimally tuned heavy-ball
## Finding
Consider the heavy-ball iteration for the positive definite quadratic system
\[
Ax=b,
\qquad
A=A^{\mathsf T}>0,
\]
with initialization
\[
x^{(-1)}=x^{(0)}=0
\]
and update
\[
x^{(k+1)}
=
x^{(k)}
+
\beta\bigl(x^{(k)}-x^{(k-1)}\bigr)
+
\alpha\bigl(b-Ax^{(k)}\bigr),
\]
where
\[
\alpha>0,
\qquad
\beta\ge0.
\]

If \(A\) is Stieltjes, meaning that its off-diagonal entries are nonpositive, then
\[
x^{(1)}=\alpha b
\]
and
\[
x^{(2)}
=
\alpha\bigl[(2+\beta)I-\alpha A\bigr]b.
\]
Hence the following fixed-matrix criterion is exact:
\[
x^{(2)}\ge0
\quad\text{for every }b\ge0
\]
if and only if
\[
\alpha a_{ii}\le 2+\beta
\quad\text{for every }i.
\]

Consequently, over the whole class of Stieltjes matrices with spectrum contained in
\[
[\mu,L],
\qquad
0<\mu\le L,
\]
second-iterate positivity for every nonnegative right-hand side holds if and only if
\[
\alpha L\le2+\beta.
\]

For Polyak's optimal quadratic heavy-ball parameters
\[
\alpha_*=
\frac{4}{(\sqrt L+\sqrt\mu)^2},
\qquad
\beta_*=
\left(
\frac{\sqrt L-\sqrt\mu}
{\sqrt L+\sqrt\mu}
\right)^2,
\]
this criterion becomes
\[
\kappa:=\frac L\mu\le9.
\]
Thus condition number \(9\) is the sharp universal second-iterate positivity frontier on the Stieltjes class.

There is a stronger all-iterate statement for diagonal systems. Let
\[
A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),
\qquad
\mu\le\lambda_i\le L,
\]
and use the same optimal parameters. Then
\[
x^{(k)}\ge0
\quad\text{for every }k\ge0\text{ and every }b\ge0
\]
if and only if
\[
\kappa\le9.
\]
At the boundary \(\kappa=9\), the component corresponding to \(\lambda=L\) reaches zero exactly at the second iterate.

For every \(\kappa>9\), dimension two already gives a strict sign failure. Taking
\[
A=
\operatorname{diag}(\mu,L)
\]
and any strictly positive \(b\), the \(L\)-coordinate of \(x^{(2)}\) is negative. Hence dimension two and the second iterate are jointly minimal for failure in the optimally tuned spectral class.

For example, with
\[
A=
\operatorname{diag}(1,16),
\qquad
b=
\begin{pmatrix}
1\\
1
\end{pmatrix},
\]
one has
\[
\alpha_*=\frac4{25},
\qquad
\beta_*=\frac9{25},
\]
so
\[
x^{(1)}
=
\begin{pmatrix}
4/25\\
4/25
\end{pmatrix}>0,
\qquad
x^{(2)}
=
\begin{pmatrix}
44/125\\
-4/125
\end{pmatrix}.
\]
The exact solution is
\[
A^{-1}b=
\begin{pmatrix}
1\\
1/16
\end{pmatrix}>0.
\]

## Assumptions and scope
The theorem concerns the constant-parameter heavy-ball method on symmetric positive definite quadratics. The initialization is the standard zero-momentum initialization \(x^{(-1)}=x^{(0)}\).

The exact fixed-matrix and spectral-class second-iterate criteria use the Stieltjes sign pattern. The all-iterate theorem is asserted only for diagonal positive definite systems, where the coordinates decouple into scalar heavy-ball modes.

The result concerns coordinatewise positivity. It does not claim monotonic decrease of the objective, distance to the minimizer, or residual norm. It also does not classify later iterates for general non-diagonal Stieltjes matrices.

## Proof
The first update is
\[
x^{(1)}=\alpha b.
\]
Substituting this into the recurrence gives
\[
x^{(2)}
=
(1+\beta)\alpha b-\alpha^2Ab+\alpha b
=
\alpha\bigl[(2+\beta)I-\alpha A\bigr]b.
\]
For a Stieltjes matrix, every off-diagonal entry of
\[
(2+\beta)I-\alpha A
\]
is nonnegative. Therefore this matrix is entrywise nonnegative exactly when all of its diagonal entries are nonnegative:
\[
2+\beta-\alpha a_{ii}\ge0
\quad\text{for all }i.
\]
A matrix maps every nonnegative vector to a nonnegative vector if and only if it is entrywise nonnegative, which proves the fixed-matrix criterion.

If the spectrum lies in \([\mu,L]\), then
\[
a_{ii}\le L
\]
for every \(i\), so
\[
\alpha L\le2+\beta
\]
is sufficient uniformly over the class. It is also necessary uniformly because the diagonal matrix
\[
\operatorname{diag}(\mu,L)
\]
belongs to the class and has a diagonal entry equal to \(L\).

Now insert the optimal quadratic parameters. Put
\[
r=\sqrt{\kappa}.
\]
Then
\[
\alpha_*L
=
\frac{4r^2}{(r+1)^2},
\]
while
\[
2+\beta_*
=
2+
\frac{(r-1)^2}{(r+1)^2}
=
\frac{3r^2+2r+3}{(r+1)^2}.
\]
Thus
\[
\alpha_*L\le2+\beta_*
\]
is equivalent to
\[
r^2-2r-3\le0,
\]
hence to
\[
r\le3
\]
and therefore to
\[
\kappa\le9.
\]

It remains to prove the all-iterate diagonal statement. Fix one diagonal mode \(\lambda\in[\mu,L]\), and let
\[
z_k=\frac{\lambda x_k}{b}
\]
for a positive scalar right-hand side. The exact target is \(z=1\). Set
\[
e_k=1-z_k.
\]
For the optimal parameters define
\[
q=
\frac{\sqrt L-\sqrt\mu}
{\sqrt L+\sqrt\mu},
\]
and choose \(\theta\in[0,\pi]\) by
\[
\cos\theta
=
\frac{L+\mu-2\lambda}{L-\mu}.
\]
The scalar error satisfies
\[
e_{k+1}
=
2q\cos\theta\,e_k-q^2e_{k-1},
\]
with
\[
e_0=1,
\qquad
e_1=q(2\cos\theta-q).
\]
Writing \(U_k\) for the Chebyshev polynomial of the second kind and using \(U_{-1}=0\), the solution is
\[
e_k
=
q^k
\left[
U_k(\cos\theta)
-
qU_{k-1}(\cos\theta)
\right].
\]

If \(\kappa\le9\), then
\[
0\le q\le\frac12.
\]
For \(k=1\),
\[
e_1\le q(2-q)<1.
\]
For every \(k\ge2\), the standard bound
\[
|U_k(t)|\le k+1,
\qquad
-1\le t\le1,
\]
gives
\[
e_k
\le
q^k(k+1+qk)
\le
2^{-k}\left(k+1+\frac k2\right)
\le1.
\]
The last inequality is equality only at \(k=2\). Therefore
\[
z_k=1-e_k\ge0
\]
for every mode and every iteration.

Conversely, if \(\kappa>9\), then \(q>1/2\). At the high-curvature endpoint \(\lambda=L\), one has \(\cos\theta=-1\), so
\[
e_2
=
q^2(3+2q)>1.
\]
Hence
\[
z_2=1-e_2<0.
\]
This proves both necessity and the fact that the first failure occurs already at the second iterate.

## Verification
The accompanying `verify.py` uses exact rational arithmetic for the finite algebra.

It reconstructs the first two heavy-ball iterates for general rational \(\alpha,\beta\) and verifies
\[
x^{(2)}
=
\alpha[(2+\beta)I-\alpha A]b.
\]
It checks the optimal-parameter threshold at several square condition numbers on both sides of \(9\), and it verifies the explicit \(\kappa=16\) witness exactly.

For diagonal modes, the checker reconstructs the scalar error recurrence and the Chebyshev-\(U\) representation at many rational values of \(q\) and \(\cos\theta\). It also verifies the endpoint identity
\[
e_2=q^2(3+2q)
\]
at \(\lambda=L\), including equality \(e_2=1\) when \(q=1/2\).

The proof for all real spectral points and all iteration counts is analytic; the replay does not infer the infinite statement from finite samples.

## Relationship to prior work
Polyak's heavy-ball method and its optimal parameters on strongly convex quadratics are classical. Lessard, Recht, and Packard give the standard constant-parameter heavy-ball recurrence and record the optimal quadratic tuning
\[
\alpha_*=
\frac{4}{(\sqrt L+\sqrt\mu)^2},
\qquad
\beta_*=
\left(
\frac{\sqrt\kappa-1}
{\sqrt\kappa+1}
\right)^2.
\]
Those construction and convergence-rate facts are prior work.

Danilova, Kulakova, and Polyak analyze non-monotone heavy-ball transients on positive definite quadratics and show that even optimally tuned trajectories can exhibit peak effects. That qualitative non-monotonicity is also prior work.

The present result isolates a different structural property: coordinatewise positivity when the exact solution is positive. It gives an exact fixed-matrix second-iterate criterion for every Stieltjes system, a sharp spectral-class frontier, and an all-iterate characterization for diagonal systems. Neither objective non-monotonicity nor modal convergence-rate theory implies this orthant statement.

A nearby result on heavy-ball acceleration shows that uniformly requiring real characteristic roots prevents accelerated worst-case convergence. That root-geometry obstruction is distinct from the positivity frontier here: the threshold \(9\) is caused by the sign of the second solution polynomial and remains meaningful even though the optimally tuned method deliberately enters the complex-root regime on interior spectral modes.

## Limitations
The all-iterate theorem is diagonal. For a non-diagonal Stieltjes matrix, higher solution polynomials involve higher powers of \(A\), and their entrywise signs are not classified here.

The optimal parameters assume exact knowledge of \(\mu\) and \(L\). Misspecified spectral bounds change both the momentum and the positivity threshold.

Coordinatewise positivity is basis-dependent. The theorem is aimed at applications where the original coordinates carry a genuine nonnegativity interpretation.

The heavy-ball and monotone-iteration literatures are extensive. An older source may contain an equivalent low-order orthant criterion under different terminology; this remains the principal originality risk.

## References
1. Laurent Lessard, Benjamin Recht, and Andrew Packard, *Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints*, arXiv:1408.3595v1, August 15, 2014; SIAM Journal on Optimization 26 (2016), 57--95, DOI: 10.1137/15M1009597.
2. Marina Danilova, Anastasiya Kulakova, and Boris Polyak, *Non-monotone Behavior of the Heavy Ball Method*, arXiv:1811.00658v1, November 1, 2018.
3. Boris T. Polyak, *Some Methods of Speeding Up the Convergence of Iteration Methods*, USSR Computational Mathematics and Mathematical Physics 4 (1964), 1--17, DOI: 10.1016/0041-5553(64)90137-5.
