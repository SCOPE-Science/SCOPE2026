# Exact Turán constant at \(\lambda=5/2\)
## Finding
Let
\[
\Omega_{5/2}=(-1,1)\cup(3/2,7/2)\cup(-7/2,-3/2)
\]
and let
\[
F(a)=256a^7+256a^6-96a^5-80a^4+40a^3+30a^2-15a-5.
\]
There is a unique zero \(a_\ast\in(0.53305,0.53306)\) of \(F\). The exact Turán constant is
\[
\mathcal T_{\mathbb R}(\Omega_{5/2})
=
\frac{(2a_\ast+1)^2(4a_\ast^2-6a_\ast+1)^2}
{128a_\ast^6-20a_\ast^2+5}
=
2.1353071788763974322\ldots .
\]
Equivalently,
\[
\mathcal T_{\mathbb Z}(\{0,\pm1,\pm4,\pm5,\pm6\})
=
\frac{2(2a_\ast+1)^2(4a_\ast^2-6a_\ast+1)^2}
{128a_\ast^6-20a_\ast^2+5}
=
4.2706143577527948645\ldots .
\]
The recent three-interval paper proves only an explicit strict lower bound for this same finite model and states that no optimality is claimed. The equality above closes that finite optimization exactly.

## Assumptions and scope
For a finite symmetric set \(A\subset\mathbb Z\) containing \(0\), write \(\mathcal T_{\mathbb Z}(A)\) for the supremum of \(P(0)\) over nonnegative trigonometric polynomials
\[
P(t)=\sum_{n\in A}c_ne^{int},\qquad c_0=1.
\]
Averaging with \(P(-t)\) permits real even coefficients. For
\[
A=\{0,\pm1,\pm4,\pm5,\pm6\},
\]
putting \(x=\cos t\) gives the equivalent problem of maximizing \(H(1)\) among
\[
H(x)=1+\beta_1T_1(x)+\beta_4T_4(x)+\beta_5T_5(x)+\beta_6T_6(x)
\]
that satisfy \(H(x)\ge0\) for every \(x\in[-1,1]\), where \(T_k(\cos t)=\cos(kt)\).

The rational-endpoint reduction in arXiv:2608.15643v1 gives
\[
\mathcal T_{\mathbb R}(\Omega_{5/2})=\frac12\mathcal T_{\mathbb Z}(A).
\]
No assertion is made here for other rational parameters.

## Proof
First, \(F(0.53305)<0<F(0.53306)\), while exact interval arithmetic gives
\[
71.07<F'(a)<71.09\qquad(0.53305\le a\le0.53306).
\]
Hence \(F\) has exactly one zero \(a_\ast\) in this interval.

For a parameter \(a\), define
\[
r_a(x)=x^3+ax^2+\left(2a^2-\frac54\right)x-2a^3
\]
and
\[
d_0(a)=\frac{128a^6-20a^2+5}{32}.
\]
A direct Chebyshev expansion gives the polynomial identity
\[
32r_a(x)^2
=
(128a^6-20a^2+5)T_0(x)
-4a(64a^4-40a^2+5)T_1(x)
+4(5a^2-1)T_4(x)
+4aT_5(x)+T_6(x).
\]
In particular the \(T_2\)- and \(T_3\)-coefficients vanish identically. Since \(d_0(a_\ast)>0\),
\[
H_\ast(x)=\frac{r_{a_\ast}(x)^2}{d_0(a_\ast)}
\]
is feasible for the discrete problem. Its objective is
\[
H_\ast(1)
=
\frac{2(2a_\ast+1)^2(4a_\ast^2-6a_\ast+1)^2}
{128a_\ast^6-20a_\ast^2+5}.
\]
This proves the lower bound.

For the matching upper bound, \(r_{a_\ast}\) has three simple roots \(x_1<x_2<x_3\) satisfying the certified disjoint brackets
\[
-0.9163<x_1<-0.9161,\qquad
-0.4146<x_2<-0.4143,\qquad
0.7975<x_3<0.7978.
\]
Thus all three roots lie in \((-1,1)\).

Set
\[
D=a(96a^4-5),\qquad
S=-160a^4+60a^2+5a-2,\qquad
E=4(2a-1)D,
\]
and define \(Q_a(x)=Q_0(a)+Q_1(a)x+Q_2(a)x^2\), where
\[
\begin{aligned}
Q_0(a)&=-3840a^7+1920a^6+2432a^5-1120a^4-640a^3+250a^2+53a-14,\\
Q_1(a)&=-4a(2a-1)(256a^4-60a^2-5a-3),\\
Q_2(a)&=-4(2a-1)(160a^4-60a^2-5a+2).
\end{aligned}
\]
Let
\[
q_a(x)=\frac{Q_a(x)}{E(a)},\qquad
w_j=\frac{q_{a_\ast}(x_j)}{r'_{a_\ast}(x_j)}.
\]
The same exact interval calculation gives \(E(a_\ast)>0\), and on the three root brackets respectively,
\[
r'_{a_\ast}>0,\quad r'_{a_\ast}<0,\quad r'_{a_\ast}>0,
\]
while
\[
Q_{a_\ast}>0,\quad Q_{a_\ast}<0,\quad Q_{a_\ast}>0.
\]
Consequently \(w_1,w_2,w_3>0\).

For any polynomial \(h\), Lagrange interpolation for the monic cubic \(r_{a_\ast}\) says that
\[
\sum_{j=1}^3\frac{q_{a_\ast}(x_j)h(x_j)}{r'_{a_\ast}(x_j)}
\]
is the coefficient of \(x^2\) in the remainder of \(q_{a_\ast}(x)h(x)\) modulo \(r_{a_\ast}(x)\). Exact polynomial division gives
\[
\sum_{j=1}^3 w_jT_k(x_j)=-1
\qquad(k=1,4,5),
\]
and
\[
\sum_{j=1}^3 w_jT_6(x_j)+1
=
-\frac{2(2a_\ast+1)(4a_\ast^2-6a_\ast+1)F(a_\ast)}
{a_\ast(96a_\ast^4-5)}
=0.
\]
Also
\[
\sum_{j=1}^3w_j=\frac{S(a_\ast)}{D(a_\ast)}=:s_\ast>0.
\]

Now let
\[
H(x)=1+\beta_1T_1(x)+\beta_4T_4(x)+\beta_5T_5(x)+\beta_6T_6(x)
\]
be any feasible polynomial. Since \(H(x_j)\ge0\), multiplying these three inequalities by the positive weights and summing gives
\[
s_\ast-\beta_1-\beta_4-\beta_5-\beta_6\ge0.
\]
Therefore
\[
H(1)\le1+s_\ast.
\]
Finally, direct algebra yields
\[
s_\ast-\left(H_\ast(1)-1\right)
=
\frac{2(2a_\ast+1)(4a_\ast^2-6a_\ast+1)F(a_\ast)}
{a_\ast(96a_\ast^4-5)(128a_\ast^6-20a_\ast^2+5)}
=0.
\]
Hence \(H(1)\le H_\ast(1)\) for every feasible \(H\), while \(H_\ast\) itself is feasible. This proves the exact discrete optimum and, by the rational-endpoint reduction, the stated continuous Turán constant.

## Verification
The accompanying `verify_turan_5_2.py` uses only the Python standard library and exact rational arithmetic for the algebraic identities and interval certificates. It verifies the Chebyshev cancellation, the four dual moment identities after clearing denominators, the unique-root bracket for \(a_\ast\), the three disjoint root brackets for \(r_{a_\ast}\), the signs needed for \(w_j>0\), and a high-precision decimal evaluation of the final constant.

The finite checker does not replace the proof: the exact upper bound is the positive three-node dual certificate above, valid for every feasible nonnegative trigonometric polynomial.

## Relationship to prior work
Fu, Li, Wang and Wang reduce the rational three-interval problem to the finite set \(A_{p,q}\). For \(p=5\), \(q=2\), their Section 4.3 identifies exactly
\[
A=\{0,\pm1,\pm4,\pm5,\pm6\}
\]
and supplies the feasible square-cubic certificate
\[
q(x)=x^3+\frac{\sqrt{42}}{12}x^2-\frac23x-\frac{7\sqrt{42}}{144}.
\]
They obtain
\[
\mathcal T_{\mathbb R}(\Omega_{5/2})\ge\frac{559+80\sqrt{42}}{506}
=2.1293661183\ldots
\]
and explicitly state that no optimality of the finite problem is claimed. Their certificate belongs to the same one-parameter square-cubic family above, at \(a=\sqrt{42}/12\); the present result identifies the optimizing parameter \(a_\ast\) and adds the dual certificate needed for equality.

Targeted searches for the exact frequency set, its Carathéodory–Fejér formulation, the algebraic parameter polynomial, and the decimal constant did not locate an earlier statement of this exact value. General Turán and Carathéodory–Fejér theory supplies the framework but does not, by itself, imply this set-specific algebraic optimum.

## Limitations
The result concerns only \(\lambda=5/2\). It does not classify all half-integer or rational parameters, and it does not claim a new general duality theorem. The novelty claim is the exact evaluation of this specific finite arithmetic model and hence of the corresponding continuous three-interval Turán constant.

A residual literature risk remains that the same finite Carathéodory–Fejér constant may have been tabulated under a different normalization or notation in older extremal-trigonometric-polynomial literature. No such match was found in the targeted searches performed here.

## References
1. X.-Y. Fu, Y.-K. Li, W.-J. Wang, X. Wang, “Turán problem on the union of three intervals of equal length,” arXiv:2608.15643v1, first publicly posted 16 August 2026. In particular Theorem 1.2 and Section 4.3.
2. M. N. Kolountzakis and Sz. Gy. Révész, “Turán’s extremal problem for positive definite functions on groups,” J. London Math. Soc. 74 (2006), 475–496.
3. L. Fejér, “Über trigonometrische Polynome,” J. Reine Angew. Math. 146 (1916), 53–82.
4. F. Riesz, “Über ein Problem des Herrn Carathéodory,” J. Reine Angew. Math. 146 (1916), 83–87.
