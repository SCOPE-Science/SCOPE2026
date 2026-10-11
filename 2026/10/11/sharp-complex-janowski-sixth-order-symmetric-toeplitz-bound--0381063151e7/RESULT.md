# Sharp complex Janowski sixth-order symmetric Toeplitz bound

## Finding

Fix real parameters \(-1\le B<A\le1\). Let \(\mathcal J_{A,B}^{\mathrm{odd}}\) be the class of all normalized odd analytic functions
\[
f(z)=z+a_3z^3+a_5z^5+\cdots\quad(z\in\mathbb D)
\]
with unrestricted complex coefficients and
\[
\frac{zf'(z)}{f(z)}\prec\frac{1+Az}{1+Bz}.
\]
For \(a_1=1\) and \(a_{2j}=0\), use the **symmetric (non-Hermitian)** Toeplitz determinant
\[
T_6(1;f)=\det\bigl(a_{1+|j-k|}\bigr)_{j,k=1}^{6}.
\]
Write \(d=A-B\), \(P_1=d(A-3B)\), and \(P_2=d(3A-B)\). The exact maximum is
\[
\boxed{\max_{f\in\mathcal J_{A,B}^{\mathrm{odd}}}|T_6(1;f)|
=\left(\frac{(8+P_1)(8+P_2)}{64}\right)^2.}
\]
There are exactly **two** maximizing functions. They are characterized by
\[
\frac{zf_\pm'(z)}{f_\pm(z)}=\frac{1\pm iAz^2}{1\pm iBz^2}
\]
and are given explicitly, with the analytic branch normalized to equal \(1\) at the origin, by
\[
f_\pm(z)=
\begin{cases}
z(1\pm iBz^2)^{d/(2B)},&B\ne0,\\
z\exp(\pm iAz^2/2),&B=0.
\end{cases}
\]
In particular the complex-coefficient maximum exceeds \(1\) for **every** \(B<A\), whereas the real-coefficient Janowski theorem has maximum \(1\). At \((A,B)=(1,-1)\) the complex maximum is \(16\).

## Assumptions and scope

All parameters \(A,B\) are real and satisfy \(-1\le B<A\le1\); coefficients of \(f\) need not be real. Subordination means composition with an analytic Schwarz function \(\omega:\mathbb D\to\mathbb D\) satisfying \(\omega(0)=0\). The Möbius Janowski map is injective on \(\mathbb D\) for \(A>B\), and maps \(\mathbb D\) into the right half-plane. The oddness of \(f\) makes \(zf'/f\) even. Injectivity therefore forces the subordinating function to be even: \(\omega(z)=v(z^2)\), where \(v:\mathbb D\to\mathbb D\) is Schwarz and \(v(0)=0\). In particular the class consists of starlike univalent functions and is nonempty.

The \(6\times6\) symmetric Toeplitz matrix is **not** the Hermitian matrix formed using conjugated lower diagonals. The object \(T_6\) is generally complex and its absolute value is optimized.

## Proof

**1. Reduction to two complex coefficients.** Sorting row and column indices by parity makes the matrix block diagonal with two identical blocks
\[
\widehat T_3=
\begin{pmatrix}1&a_3&a_5\\a_3&1&a_3\\a_5&a_3&1\end{pmatrix}.
\]
Consequently, writing \(D=\det\widehat T_3\),
\[
T_6(1;f)=D^2,\qquad
D=(1-a_5)(1+a_5-2a_3^2).
\]
This parity identity is algebraic and works for complex coefficients; no conjugations are taken.

**2. General complex Schwarz parameters.** Write \(v(\zeta)=u\zeta+v_2\zeta^2+\cdots\). Schwarz--Pick gives \(|u|\le1\) and
\[
v_2=(1-|u|^2)\eta,\qquad |\eta|\le1.
\]
Indeed \(v(\zeta)/\zeta\) is a disk self-map, and Schwarz--Pick at the origin bounds its derivative. Comparing coefficients in
\[
zf'(z)=f(z)\frac{1+Av(z^2)}{1+Bv(z^2)}
\]
gives
\[
a_3=\frac{d}{2}u,\qquad
a_5=\frac{d(A-3B)}8u^2+\frac d4(1-|u|^2)\eta.
\]
Set
\[
R=|u|^2,\quad t=u^2,\quad
k=\frac{d(A-3B)}8,\quad m=\frac{d(3A-B)}8,\quad\ell=\frac d4.
\]
Thus \(0\le R\le1\), \(|t|=R\), and
\[
D=(1-kt-\ell(1-R)\eta)(1-mt+\ell(1-R)\eta).
\]
Define \(S=k+m=d^2/2\) and \(K=km=d^2[4d^2-(A+B)^2]/64\). Expansion reads
\[
D=P(t)+\ell(m-k)t(1-R)\eta-\ell^2(1-R)^2\eta^2,
\qquad P(t)=1-St+Kt^2.
\]
The permissible parameter range entails the elementary estimates
\[
0<S\le2,\quad K\ge-\frac S8,\quad
\ell|m-k|=\frac{d^2|A+B|}{16}\le\frac{d^2}8,
\quad\ell^2=\frac{d^2}{16}.
\]
Here \(|A+B|\le2\), \(d\le2\), and the formula for \(K\) prove every displayed inequality.

**3. Angular maximum of the leading quadratic.** For each \(0\le R\le1\) and \(|t|=R\),
\[
\boxed{|P(t)|\le P(-R)=1+SR+KR^2.}
\]
When \(K\ge0\), this is the triangle inequality, with equality for \(R>0\) only at \(t=-R\) because \(S>0\). Suppose \(K<0\) and \(R>0\); write \(t=Re^{i\theta}\), \(c=\cos\theta\). Direct expansion yields
\[
|P(t)|^2
=1+S^2R^2+K^2R^4-2KR^2
-2SR(1+KR^2)c+4KR^2c^2.
\]
Its derivative with respect to \(c\) is \(-2SR(1+KR^2)+8KR^2c\), maximized for \(-1\le c\le1\) at \(c=-1\). The value there is
\[
-2R\bigl[S(1+KR^2)+4KR\bigr]
\le-2RS\bigl(1-SR^2/8-R/2\bigr)
\le-\frac12RS<0.
\]
The function \(|P(t)|^2\) therefore decreases strictly with \(c\). Its unique maximum occurs at \(c=-1\), or \(t=-R\). The positive sign \(P(-R)>0\) follows from
\[
P(-R)\ge1+SR-\frac S8R^2>0.
\]

**4. Radial optimization and equality.** Using the preceding angular estimate gives
\[
|D|\le P(-R)+\ell|m-k|R(1-R)+\ell^2(1-R)^2.
\]
Subtracting this upper bound from \(P(-1)=1+S+K\) yields
\[
\begin{aligned}
P(-1)-|D|\;&\ge(1-R)
\left[S+K(1+R)-\ell|m-k|R-\ell^2(1-R)\right]\\
&\ge(1-R)\frac{3d^2}{16}.
\end{aligned}
\]
For the last inequality use \(K\ge-S/8\), \(1+R\le2\), \(S=d^2/2\), \(\ell|m-k|\le d^2/8\), and \(\ell^2=d^2/16\). Since \(d>0\), equality \(|D|=P(-1)\) requires \(R=1\). Then Schwarz's equality case gives \(v(\zeta)=u\zeta\). The angular uniqueness in Step 3 forces \(t=u^2=-1\), so \(u=+i\) or \(u=-i\). Conversely these two choices give
\[
D=P(-1)=(1+k)(1+m)=\frac{(8+P_1)(8+P_2)}{64}>0.
\]
Squaring proves the sharp maximum and uniqueness. Integrating \(zf'/f=(1+Au z^2)/(1+Bu z^2)\) gives the two displayed extremal functions; their Janowski subordination is immediate from \(v(\zeta)=u\zeta\).

Finally,
\[
P(-1)=1+S+K\ge1+\frac{7d^2}{16}>1,
\]
so the sharp complex maximum is strictly greater than \(1\) for every nondegenerate Janowski pair. At \((A,B)=(1,-1)\), \(k=m=1\), hence \(P(-1)^2=16\).

## Verification

The attached standalone `verify_complex_janowski.py` checks the coefficient factorization and all symbolic identities with exact polynomial simplification; it also performs 9,020 rational parameter stress tests, 40,000 reproducible numerical samples in the complex Schwarz parameter body, and 1,640 exact rational endpoint formula checks. Its observed output concludes `VERIFY_OK`. These checks support the displayed algebra and detect parameter/sign mistakes; they are not a proof of global optimality. The global statement follows from Steps 3 and 4 for continuous, infinite parameter ranges.

## Relationship to prior work

Mahmood, Rasheed, Mihsin and Atshan (September 2026, DOI below), Theorem 6.3, prove the real-coefficient bound \(\Phi(A,B)^2\le T_6(1)\le1\) for the same Janowski parameters. Their Proposition 5.3 separately determines the *complex-coefficient exponential* class, not the complex Janowski class. Their Discussion explicitly leaves the complex Janowski sharp bound open. The present result answers that specific problem with a different sharp constant and unique purely imaginary Schwarz extremizers.

The parity reduction, real Janowski coefficient identities, and real Janowski extremizers are prior input, not novelty claims. The complex Schwarz--Pick parametrization and the global two-complex-variable sharp bound (with strict radial inequality) yield the new implication. The result concerns neither Hermitian--Toeplitz determinants nor arbitrary non-odd normalized functions. Earlier low-order Janowski/Hermitian and logarithmic-coefficient Toeplitz studies do not imply this particular symmetric sixth-order complex optimization.

## Limitations

Only the sixth-order symmetric determinant at index \(1\), odd functions, and real Janowski parameters in the stated closed triangular range are covered. No sharp lower modulus, complete range of determinant values, Hermitian analogue, or order-eight case is claimed. The evidence for originality is literature-limited and requires independent review; the argument itself is a self-contained analytic proof subject to independent mathematical checking.

## References

1. Z. H. Mahmood, R. O. Rasheed, B. K. Mihsin and W. G. Atshan, *A Janowski positivity threshold for the sixth-order symmetric Toeplitz determinant of odd starlike functions*, Journal of Inequalities and Applications (published 2026-09-02), DOI: 10.1186/s13660-026-03535-3; open access: https://doi.org/10.1186/s13660-026-03535-3. In particular, Lemma 3.1, Corollary 3.2, Lemma 4.2, Theorem 6.3, Proposition 5.3, Discussion, and Appendix A.
2. S. S. Kumar, N. Srivastava and N. E. Cho, *Sharp estimation of Hermitian-Toeplitz determinants for Janowski type starlike and convex functions* (2020), an earlier different Hermitian determinant problem.
