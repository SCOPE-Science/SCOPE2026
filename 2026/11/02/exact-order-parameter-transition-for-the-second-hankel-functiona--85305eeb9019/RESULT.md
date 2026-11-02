# Exact order–parameter transition for the second Hankel functional of starlike maps

## Finding

Let \(0\leq\alpha<1\), \(0\leq\mu\leq1\), and write \(c=1-\alpha\). For every normalized analytic starlike function \(f(z)=z+a_2z^2+a_3z^3+a_4z^4+\cdots\) of order \(\alpha\) on the unit disk, the **exact sharp bound** is

\[
\boxed{\sup_f\left|\mu a_2a_4-a_3^2\right|
=c^2\max\left\{1,(1+2c)\left((1+2c)-\frac{4\mu}{3}(1+c)\right)\right\}.}
\]

There is exactly one change in the canonical extremal type, at \(\mu_*=3c/(1+2c)\). For \(\mu<\mu_*\), the value is attained by the generalized Koebe function \(f(z)=z(1-z)^{-2c}\); for \(\mu>\mu_*\), it is attained by the odd starlike function \(f(z)=z(1-z^2)^{-c}\). Both attain the bound at equality \(\mu=\mu_*\). Rotations of either construction also attain the corresponding bound. No assertion is made that these are the complete equality classes.

The same constant is sharp for the **directional generalized Hankel functional** of every radial-type starlike map \(F(x)=x h(x)\) on the open unit ball of any nonzero complex Banach space, with the precise normalization in the next section. In particular, this is a sharp replacement, for the stated radial class, of the larger two-parameter estimate \(c^2(9-8\mu)\) appearing in the 2026 motivating work. The replacement is strictly smaller for \(0<\alpha<1\), \(0\leq\mu<1\); it agrees at \(\mu=1\) and at \(\alpha=0\).

## Assumptions and scope

In one variable, starlike of order \(\alpha\) means \(f(0)=0\), \(f'(0)=1\), and \(\operatorname{Re}(zf'(z)/f(z))>\alpha\) for all nonzero \(z\) in the unit disk. This condition implies univalence. All parameters and quantifiers in the displayed extremum are real: \(\alpha\in[0,1)\), \(\mu\in[0,1]\), and the supremum is over *all* functions satisfying that condition, not just functions with real coefficients.

For the Banach-space statement, let \(X\ne\{0\}\) be any complex Banach space, \(B_X=\{x:\|x\|<1\}\), and let \(h:B_X\to\mathbb C\) be holomorphic, nowhere zero, and normalized by \(h(0)=1\). Assume

\[
\operatorname{Re}\left(1+\frac{Dh(x)[x]}{h(x)}\right)>\alpha
\quad(x\in B_X).
\]

Set \(F(x)=x h(x)\). This gives a normalized biholomorphic radial starlike map. For \(0\ne x\in B_X\) choose any norming functional \(\ell_x\in X^*\) with \(\|\ell_x\|=1\) and \(\ell_x(x)=\|x\|\), and define, for \(k\in\{2,3,4\}\),

\[
 b_k(F;x)=\frac{\ell_x(D^kF(0)[x,\ldots,x])}{k!\,\|x\|^k}.
\]

Then, for every such \(F\) and \(x\),

\[
\left|\mu b_2(F;x)b_4(F;x)-b_3(F;x)^2\right|
\le c^2\max\left\{1,(1+2c)\left((1+2c)-\frac{4\mu}{3}(1+c)\right)\right\},
\]

and the constant is attained for some \(F,x\) in *every* nonzero \(X\). The coefficients \(b_k\), and hence the displayed expression, are independent of which norming \(\ell_x\) is chosen. This specific radial hypothesis is essential: no claim is made about arbitrary nonradial biholomorphic maps.

## Proof

**1. Scalar Schwarz parameters.** Let \(f\) be as in the first paragraph. Put \(c=1-\alpha>0\). The Carathéodory representation is

\[
\frac{zf'(z)}{f(z)}=\alpha+c\frac{1+\omega(z)}{1-\omega(z)},
\]

where \(\omega\) is analytic in the disk, \(\omega(0)=0\), and \(|\omega(z)|<1\). A rotation of the independent variable multiplies the functional \(\mu a_2a_4-a_3^2\) by a unit-modulus factor, so assume \(\omega'(0)=t\in[0,1]\). The first two steps of the Schur algorithm give \(x,y\in\overline{\mathbb D}\) for which

\[
\omega(z)=tz+vz^2+wz^3+O(z^4),\qquad
v=(1-t^2)x,\qquad
w=(1-t^2)\big((1-|x|^2)y-tx^2\big).
\]

The formulas also hold at \(t=1\) with \(v=w=0\). Expanding the logarithmic derivative and comparing coefficients gives

\[
 a_2=2ct,\qquad
 a_3=cv+c(1+2c)t^2,
\]

\[
 a_4=\frac{2c}{3}w+\left(\frac{4c}{3}+2c^2\right)tv
 +\left(\frac{2c}{3}+2c^2+\frac{4c^3}{3}\right)t^3.
\]

With \(B=1+2c\), \(K=B[\frac{4\mu}{3}(1+c)-B]\), and \(A=2[(\frac43+2c)\mu-B]\), direct substitution yields the exact identity

\[
\frac{\mu a_2a_4-a_3^2}{c^2}
=Kt^4+At^2v-v^2+\frac{4\mu}{3}tw.
\tag{1}
\]

**2. Exhaustive bound over all complex Schur parameters.** Write \(T=1-t^2\), \(\rho=|x|\), and \(C=4\mu/3\). From (1) and the displayed formula for \(w\),

\[
\frac{|\mu a_2a_4-a_3^2|}{c^2}
\le |K|t^4+|A|t^2T\rho+T(T+Ct^2)\rho^2+CtT(1-\rho^2).
\tag{2}
\]

As a polynomial in \(\rho\in[0,1]\), the right side has a nonnegative linear coefficient and a nonnegative quadratic coefficient, because

\[
T(T+Ct^2-Ct)=T(1-t)(1+t-Ct)\ge0
\]

for \(0\le t\le1\) and \(0\le C\le4/3\). Consequently (2) is maximized at \(\rho=1\), and, writing \(u=t^2\), gives

\[
\frac{|\mu a_2a_4-a_3^2|}{c^2}
\le |K|u^2+(1-u)^2+H u(1-u),
\qquad H=|A|+\frac{4\mu}{3}.
\tag{3}
\]

**3. The sharp two-parameter envelope.** Define \(\mu_*=3c/B\in(0,1]\). In terms of two affine expressions,

\[
H=\max\{H_+,H_-\},\quad
H_+=4(1+c)\mu-2B,\quad
H_-=2B-4(c+1/3)\mu.
\]

Always \(H_+\le2\). If \(0\le\mu\le\mu_*\), then \(K\le-1\), and

\[
(-2K)-H_-=4cB-\frac{4\mu}{3}(1+3c+4c^2)
\ge\frac{4c^2}{B}>0.
\]

Thus \(H\le-2K=2\max\{1,|K|\}\) in this regime. If \(\mu_*\le\mu\le1\), then \(K\) increases from \(-1\) to \((1-4c^2)/3\), hence \(|K|\le1\), while

\[
H_-\le H_-(\mu_*)=2-\frac{4c^2}{B}<2.
\]

Therefore \(H\le2=2\max\{1,|K|\}\) in the remaining regime. Put \(M=\max\{1,|K|\}\). Equation (3) and \(|K|\le M\) imply

\[
\frac{|\mu a_2a_4-a_3^2|}{c^2}
\le M\big(u^2+(1-u)^2+2u(1-u)\big)=M.
\]

Since \(K\le-1\) below \(\mu_*\) and \(|K|\le1\) above it, \(M=\max\{1,-K\}\), precisely the stated formula.

**4. Attainment and strict improvement.** For \(f_1(z)=z(1-z)^{-2c}\) the coefficients satisfy

\[
\mu a_2a_4-a_3^2=c^2 K.
\]

For \(f_2(z)=z(1-z^2)^{-c}\), the value is \(-c^2\). Both are starlike of order \(\alpha\) because their logarithmic derivatives are \(\alpha+c(1+z)/(1-z)\) and \(\alpha+c(1+z^2)/(1-z^2)\), respectively. Their values attain the two branches and the meeting point. If \(0<c<1\), the difference between \(9-8\mu\) and the nonconstant branch \(B^2-(4\mu/3)B(1+c)\) is affine in \(\mu\), with strictly positive endpoint values \(9-B^2\) and \(4(1-c^2)/3\). Also \(9-8\mu>1\) when \(\mu<1\). Therefore the sharp bound is strictly below \(c^2(9-8\mu)\) for \(0<\alpha<1\), \(0\le\mu<1\). At \(\mu=1\), both constants equal \(c^2\).

**5. Banach-space lifting without loss.** For every unit vector \(v\in X\), the scalar function \(g_v(\zeta)=\zeta h(\zeta v)\) is normalized starlike of order \(\alpha\), since

\[
\frac{\zeta g_v'(\zeta)}{g_v(\zeta)}
=1+\frac{Dh(\zeta v)[\zeta v]}{h(\zeta v)}.
\]

For \(x=rv\) with \(0<r<1\), the identity \(D^kF(0)[x^k]/k!=x\,D^{k-1}h(0)[x^{k-1}]/(k-1)!\) gives \(b_k(F;x)=[\zeta^k]g_v(\zeta)\), because \(\ell_x(x)=\|x\|\). The scalar result therefore proves the uniform bound and its independence from \(\ell_x\).

For sharpness on any nonzero \(X\), choose \(v\) of norm one and, by Hahn–Banach, \(\ell\in X^*\) of norm one with \(\ell(v)=1\). Use \(h_1(x)=(1-\ell(x))^{-2c}\) or \(h_2(x)=(1-\ell(x)^2)^{-c}\), as appropriate, evaluated at \(x=rv\). Both satisfy the required real-part condition and yield their scalar extremal coefficients along \(v\). They also produce normalized biholomorphic maps \(x\mapsto xh_j(x)\): on each complex line through the origin the scalar map is starlike and univalent, and distinct lines cannot have the same nonzero image under a radial scalar multiplier. Its derivative is invertible by the rank-one inversion formula because \(1+Dh_j(x)[x]/h_j(x)\) has positive real part. This proves sharpness for every \(X\).

## Verification

A standalone standard-library script `CHECK.py` reconstructs the first three coefficients from rational Schwarz functions by formal power-series division and the independent logarithmic-derivative recurrence. It compares the resulting functional with (1), verifies the scalar envelope on rational parameters, checks both exact extremal values and the phase boundary, and checks strict improvement in the interior. The checker passes 9,193 exact-rational assertions. The proof above, not the finite checks, establishes the theorem for every real parameter and every admissible holomorphic function.

## Relationship to prior work

Majumder, Banerjee, Panja and Pramanik (arXiv:2610.33031v1, first posted 2026-10-13) introduce the same parameterized functional and prove the dimension-independent upper bound \(c^2(9-8\mu)\) (Theorem 2.1 and its proof, pp. 5 and 8–11), with matching equality at \(\alpha=0\) and at \(\mu=1\). Their two-parameter expression is not the sharp constant for \(0<\alpha<1\), \(\mu<1\): the present formula proves the strict improvement, exact extremal transition, and sharpness in all Banach dimensions for the radial class.

Thomas (arXiv:1508.05839, 2015) and Sim–Thomas–Zaprawa (DOI:10.1080/17476933.2021.1931149) study the *unparameterized* second Hankel determinant \(a_2a_4-a_3^2\), corresponding to \(\mu=1\). The \(\mu=1\) slice is known and is included only to state the complete parameter transition; it is not claimed as new. Earlier work on Fekete–Szegő quantities or other Hankel indices does not automatically imply the joint \((\alpha,\mu)\) optimization here.

## Limitations

The parameter restriction \(0\le\mu\le1\) matters; no sharp bound is asserted for negative or complex \(\mu\). The Banach statement requires the scalar-multiplier form \(F(x)=xh(x)\) and the specified radial starlikeness condition. The theorem identifies sharp constants and canonical extremal constructions, not all equality cases. It does not classify general nonradial biholomorphic mappings. Earlier material not accessible in full or not indexed can remain an originality risk. This work has not undergone independent mathematical audit.

## References

1. S. Majumder, A. Banerjee, S. Panja and D. Pramanik, *Estimates for a Parameterized Hankel Functional of Starlike Mappings of Order \(\alpha\) and Quasi-Convex Mappings of Type \(B\) in Complex Banach Spaces*, arXiv:2610.33031v1 (first posted 2026-10-13), https://arxiv.org/abs/2610.33031.
2. D. K. Thomas, *The Second Hankel Determinant for Starlike Functions of Order Alpha*, arXiv:1508.05839 (2015), https://arxiv.org/abs/1508.05839.
3. Y. J. Sim, D. K. Thomas and P. Zaprawa, *The second Hankel determinant for starlike and convex functions of order alpha*, Complex Variables and Elliptic Equations 67 (2022), 2423–2443, DOI:10.1080/17476933.2021.1931149; publicly available abstract and accepted-manuscript listing at https://cronfa.swan.ac.uk/Record/cronfa57214.
