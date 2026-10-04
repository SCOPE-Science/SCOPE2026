# Exact generalized rectangular constant of the real \(\ell_4^2\) plane
## Finding
For the real Banach plane \(X=\ell_4^2\), define the generalized rectangular constant by
\[
\mu_4(X)=\sup\left\{\frac{(1+\lambda^4)^{1/4}}{\|x+\lambda y\|_4}:x,y\in S_X,\ x\perp_B y,\ \lambda\ge0\right\}.
\]
Then
\[
\mu_4(\ell_4^2)=\left(\frac{5+\sqrt{17}}{4}\right)^{1/4}.
\]
The supremum is attained.

## Assumptions and scope
The scalar field is real. Birkhoff--James orthogonality means that \(x\perp_B y\) when \(\|x\|_4\leq\|x+t y\|_4\) for every real \(t\). The result concerns the Gastinel--Joly generalized rectangular constant with exponent \(4\), not the classical rectangular constant \(\mu=\mu_1\), Serb's rectangular modulus, or later constants that reuse similar terminology.

## Proof
Write \(x=(x_1,x_2)\) and \(y=(y_1,y_2)\) with \(x,y\in S_{\ell_4^2}\). Smoothness of the \(\ell_4\)-norm gives
\[
x\perp_B y\quad\Longleftrightarrow\quad x_1^3y_1+x_2^3y_2=0.
\]
Consequently
\[
\|x+\lambda y\|_4^4=1+\lambda^4+6A\lambda^2+4B\lambda^3,
\]
where
\[
A=x_1^2y_1^2+x_2^2y_2^2,\qquad B=x_1y_1^3+x_2y_2^3.
\]
After coordinate sign changes and permutation, write \(x=(a,b)\) with \(a,b\ge0\), \(a^4+b^4=1\). Every unit vector orthogonal to \(x\) is, up to sign,
\[
y=\frac{(b^3,-a^3)}{(a^{12}+b^{12})^{1/4}}.
\]
Put \(u=a^2b^2\). Since \(a^{12}+b^{12}=1-3u^2\), direct simplification gives
\[
A=\frac{u}{\sqrt{1-3u^2}},\qquad B^2=\frac{u(1-4u^2)}{(1-3u^2)^{3/2}}.
\]
Eliminating \(u\) yields the exact relation
\[
B^2=A(1-A^2),\qquad 0\le A\le1.
\]
Conversely every \(A\in[0,1]\) is obtained from such an orthogonal unit pair. Since replacing \(y\) by \(-y\) changes the sign of \(B\), the supremum uses \(B=-C\) with
\[
C=\sqrt{A(1-A^2)}.
\]
Therefore
\[
\mu_4(\ell_4^2)^4=\frac1{\displaystyle\min_{A\in[0,1],\,\lambda\ge0}F(A,\lambda)},
\]
where
\[
F(A,\lambda)=1+\frac{6A\lambda^2-4C\lambda^3}{1+\lambda^4}.
\]
On \(A=0\), \(\lambda=0\), and in the limit \(\lambda\to\infty\), the value is \(1\); on \(A=1\) it is at least \(1\). An interior point gives a value below \(1\), so a global minimizer is interior. At an interior critical point, differentiation gives
\[
3C=\lambda(1-3A^2)
\]
and
\[
3A(1-\lambda^4)=C\lambda(3-\lambda^4).
\]
The first equation forces \(A^2<1/3\). Substitution into the second equation and clearing positive factors gives
\[
18A^4-15A^2+1=0.
\]
The only root compatible with \(A^2<1/3\) is
\[
A^2=\frac{5-\sqrt{17}}{12}.
\]
For this root the critical equations give
\[
\lambda^4=\frac{15+3\sqrt{17}}{2},
\]
and direct substitution gives
\[
F_{\min}=\frac{5-\sqrt{17}}{2}.
\]
The boundary values are not smaller, and this is the only feasible interior critical point, so it is the global minimum. Finally,
\[
\mu_4(\ell_4^2)^4=\frac1{F_{\min}}=\frac{5+\sqrt{17}}{4},
\]
which proves the claim.

## Verification
A standalone decimal-arithmetic checker, `verify_mu4.py`, evaluates the algebraic critical point at high precision and verifies the polynomial critical equation, both first-order equations, the value of \(F_{\min}\), and the reciprocal formula for \(\mu_4^4\). It prints `VERIFY_OK`. The checker is a consistency test; the global statement relies on the analytic reduction and boundary/critical-point argument above, not on numerical search.

An explicit extremizing pair can be recovered from
\[
u^2=\frac{7-\sqrt{17}}{48},\qquad a^4+b^4=1,\qquad a^4b^4=u^2,
\]
by taking
\[
x=(a,b),\qquad y=\frac{(b^3,-a^3)}{(a^{12}+b^{12})^{1/4}},
\]
with the sign of \(y\) chosen so that \(B<0\), and using the displayed extremal \(\lambda\).

## Relationship to prior work
Baronti, Casini and Papini define \(\mu_p(X)\), state that its exact value is generally unknown, and in their Section 5 derive upper estimates for \(\mu_p(\ell_p)\). In particular, their Theorem 5.6 gives \(\mu_p(\ell_p)\le(2^{p-1}-1)^{1/p}\) for \(p\ge2\), rather than an exact value. Their primary MSC classification is 46B20. The same paper distinguishes these generalized constants from the classical rectangular constant and cites the older two-dimensional and projection-method literature.

Targeted comparison with Paul--Ghosh--Sain's work shows that it studies the classical rectangular constant \(\mu\) and rectangular modulus, not the exponent-matched invariant \(\mu_4(\ell_4^2)\). Desbiens likewise studies the classical rectangular constant and asymmetry of Birkhoff--James orthogonality. A 2024 paper titled “Generalized rectangular constant in Banach spaces” introduces different parameterized constants \(\mu(X,a)\) and \(\mu'(X,a)\), so title similarity does not supply the present formula.

## Limitations
The theorem is only for the real two-dimensional space \(\ell_4^2\) and the exponent-matched constant \(\mu_4\). It does not determine \(\mu_p(\ell_p)\) for other \(p\), higher-dimensional variants, or the classical rectangular constant. The original 1970 Gastinel--Joly paper is a residual bibliographic risk: current metadata and the detailed 2021 treatment identify it as the source of the definition and of classical \(\ell_p\) reductions, but its full text was not available in the inspected public sources.

## References
M. Baronti, E. Casini and P. L. Papini, “Revisiting the Rectangular Constant in Banach Spaces”, *Bulletin of the Australian Mathematical Society* 105 (2022), 124–133, first published online 26 April 2021, DOI: 10.1017/S0004972721000253.

K. Paul, P. Ghosh and D. Sain, “On rectangular constant in normed linear spaces”, *Journal of Convex Analysis* 24 (2017), 917–925; arXiv:1407.1353.

J. Desbiens, “Constante rectangle et biais d'un espace de Banach”, *Bulletin of the Australian Mathematical Society* 42 (1990), 465–482, DOI: 10.1017/S000497270002863X.
