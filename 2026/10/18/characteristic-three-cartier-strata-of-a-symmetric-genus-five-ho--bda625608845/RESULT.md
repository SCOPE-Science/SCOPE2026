# Characteristic-three Cartier strata of a symmetric genus-five Howe family

## Finding
Let \(k=\overline{\mathbf F}_3\). For \(s,t\in k\setminus\{0,1\}\) with \(s\ne t\), let \(C_{s,t}\) be the smooth projective normalization of the fiber product over \(\mathbf P^1_x\) of
\[
E_1:\ y^2=x(x^2-1),\qquad E_2:\ z^2=(x^2-s)(x^2-t).
\]
Set \(u=s+t\), \(v=st\), and
\[
T(u,v)=v(1+u)^3+(u+v)^3=u^3(v+1)+v^3+v.
\]
Every \(C_{s,t}\) is geometrically smooth of genus \(5\) and nonhyperelliptic. The \(3\)-rank \(f_3\) and \(a\)-number of its Jacobian are **exactly**
\[
(f_3,a)=\begin{cases}
(0,3),&u=0,\ T=0,\\
(2,3),&u=0,\ T\ne0,\\
(1,2),&u\ne0,\ T=0,\\
(3,2),&u\ne0,\ T\ne0.
\end{cases}
\]
In particular, the entire \(3\)-rank-zero stratum on this ordered two-parameter surface is
\[
\boxed{t=-s,\quad s^4=-1.}
\]
It consists of four reduced parameter points, all defined over \(\mathbf F_9\), and all four present **one geometric isomorphism class** of genus-five curves. None of the members is ordinary or superspecial. No assertion is made that any rank-zero Jacobian is supersingular, or that this family exhausts genus-five curves with the same invariants.

## Assumptions and scope
Work over the algebraically closed field \(k\) of characteristic \(3\). The conditions \(st(s-1)(t-1)(s-t)\ne0\) ensure that the two elliptic double covers have disjoint reduced branch sets: \(\{0,1,-1,\infty\}\) and \(\{\pm\sqrt{s},\pm\sqrt{t}\}\). Hence the fiber product is integral and its smooth normalization is a generalized Howe curve of type \((g_1,g_2,r)=(1,1,0)\). The Riemann–Hurwitz formula gives genus \(2(1+1)+1=5\). The standard generalized-Howe hyperellipticity criterion, or its degree-two quotient argument, shows nonhyperellipticity because \(r=0\ne3\).

Here \(f_3\) is the dimension over \(\mathbf F_3\) of the geometric \(3\)-torsion étale part of the Jacobian; \(a=\dim_k\operatorname{Hom}(\alpha_3,\operatorname{Jac}(C))\). Thus \(a=g-\operatorname{rank}\mathcal C\), where \(\mathcal C\) is the Cartier operator on holomorphic differentials. A finite number of parameter values over \(\mathbf F_9\) is not used as a proof of statements for all \(s,t\in k\).

## Proof
The Klein four group acts by separately changing the signs of \(y,z\). Its three nontrivial quotient curves are \(E_1\), \(E_2\), and
\[
H:\ w^2=x(x^2-1)(x^2-s)(x^2-t).
\]
The third has genus \(3\). The quotient pullback/norm correspondences give a decomposed Richelot isogeny
\[
\operatorname{Jac}(C_{s,t})\ \longrightarrow\ \operatorname{Jac}(E_1)\times\operatorname{Jac}(E_2)\times\operatorname{Jac}(H)
\]
whose kernel has \(2\)-power order. Since \(2\) is invertible in characteristic \(3\), the induced \(3\)-divisible groups are isomorphic. Consequently, **both** \(3\)-rank and \(a\)-number add across these three factors.

For the first elliptic curve, \(x^3-x\) has zero coefficient of \(x^2\), so its Cartier operator vanishes and \((f_3,a)=(0,1)\). The polynomial of the second elliptic curve is \(x^4-u x^2+v\), whose Cartier scalar is \(-u\). Thus its invariants are \((0,1)\) when \(u=0\), otherwise \((1,0)\).

For the genus-three quotient, expand
\[
F(x)=x(x^2-1)(x^2-s)(x^2-t)=x^7-(1+u)x^5+(u+v)x^3-vx.
\]
In characteristic \(3\) one has \((p-1)/2=1\). Relative to the standard basis \(\{dx/w,x\,dx/w,x^2\,dx/w\}\), put \(M=(c_{3i-j})_{1\le i,j\le3}\) for the coefficients \(c_m=[x^m]F(x)\). This yields
\[
M=\begin{pmatrix}0&-v&0\\-(1+u)&0&u+v\\0&1&0\end{pmatrix}.
\]
The Cartier matrix is the entrywise cube-root of \(M\), while the corresponding Frobenius/Hasse–Witt matrix is \(M^{\mathsf T}\). As \(v\ne0\), the first and third rows are dependent and nonzero. The middle row is nonzero: its vanishing would imply \(u=-1\), \(v=1\), whence the quadratic with roots \(s,t\) is \((X-1)^2\), forbidden. Thus \(\operatorname{rank}M=2\), and \(a(H)=1\) for **every** admissible parameter.

For stable rank, write \(A=-v\), \(B=-(1+u)\), \(D=u+v\). In the Frobenius-twisted composition, the essential scalar is
\[
B^3A+D^3=v(1+u)^3+(u+v)^3=T.
\]
Direct multiplication gives
\[
M^{[9]}M^{[3]}M=\begin{pmatrix}
0&A^9T&0\\ B T^3&0&D T^3\\0&T&0
\end{pmatrix},
\]
where \(M^{[3^j]}\) means raising every matrix entry to \(3^j\). If \(T=0\), this product is zero, so \(f_3(H)=0\). If \(T\ne0\), its rank is \(2\), and its two-block semilinear action retains stable rank \(2\) under all later Frobenius iterations, so \(f_3(H)=2\). Adding the three quotient invariants proves the four cases.

Finally, \(f_3(C_{s,t})=0\) requires \(u=0\) and \(T=0\). Then \(t=-s\), \(v=-s^2\), and \(T=v^3+v=v(v^2+1)\). Since \(v\ne0\), this is equivalent to \(s^4=-1\). The polynomial \(S^4+1\) has four simple roots in \(\mathbf F_9\) (they are the elements of multiplicative order \(8\)). The change of coordinates \((s,t)\mapsto(u,v)=(s+t,st)\) has nonzero Jacobian determinant \(s-t\) on the admissible locus. Moreover, \(\partial T/\partial v=1+u^3\), which equals \(1\) when \(u=0\). Thus the rank-zero subscheme cut out by \((u,T)\) consists of **four reduced points**.

Swapping \(s,t\) does not change \(C_{s,t}\). Inversion \(x\mapsto1/x\), together with appropriate nonzero scalar rescalings of \(y/x^2\) and \(z/x^2\), identifies \(C_{s,t}\) with \(C_{1/s,1/t}\) over \(k\). For \(s^4=-1\), the four roots \(\{s,-s,1/s,-1/s\}\) are distinct and exhaust the exceptional parameters. Swapping and inversion act transitively; hence the four exceptional presentations give one geometric isomorphism class.

## Verification
Run \(\texttt{python3 verify_howe5.py}\). The standalone standard-library checker uses sparse polynomial arithmetic modulo \(3\) to verify the expansion of \(F\) and the Cartier coefficient positions, then enumerates the complete \(42\) admissible **ordered** pairs over \(\mathbf F_9\) (represented as \(\mathbf F_3[i]\), \(i^2=-1\)). It independently computes ranks of the Frobenius-twisted matrices and matches the formula in all \(42\) cases. The resulting counts by \((f_3,a)\) are \((0,3):4\), \((1,2):8\), \((2,3):2\), \((3,2):28\). The program also checks the exceptional orbit under swap/inversion. These finite checks corroborate, but are **not** substituted for, the proof over \(k\).

## Relationship to prior work
Katsura and Takashima establish the generalized-Howe genus, quotient, and decomposed-Richelot framework, and present a different explicit genus-five example with elliptic equations \(y^2=x^4\pm1\). Moriya and Kudo's 2023 genus-five paper treats the branch pattern \((2,2,4)\), rather than the \((1,1,0)\) pattern here. Kudo's 2024 sequel treats \((1,1,0)\) but assumes characteristic \(0\) or at least \(5\) and classifies plane-sextic models and singularities, not this characteristic-three Cartier stratification. Kawakita's later paper concerns Serre-bound point counts in different parameter settings and does not derive this complete rank-zero locus. The quotient isogeny and general Cartier formulas are **previously known**; the asserted contribution is the explicit all-parameter rank/\(a\)-number stratification and its reduced four-point deepest locus with one geometric isomorphism class.

## Limitations
This is a two-parameter symmetric subfamily, not the full moduli space of genus-five Howe curves. The four count is for ordered presentations, not four distinct abstract curves. The result does not determine Newton polygons or prove supersingularity of the \(3\)-rank-zero Jacobians. The literature comparison cannot rule out an unindexed equivalent formula; independent mathematical review has not been performed.

## References
- T. Katsura and K. Takashima, *Decomposed Richelot isogenies of Jacobian varieties of hyperelliptic curves and generalized Howe curves*, arXiv:2108.06936 (first available 2021); Theorems 2–3 and Example 4.
- T. Moriya and M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, I*, arXiv:2310.15993 (first public 2023-10-24), introduction and Section 2.
- M. Kudo, *Explicit construction of a plane sextic model for genus-five Howe curves, II*, arXiv:2401.00760 (first public 2024-01-01), introduction and conclusion.
- M. Q. Kawakita, *Generalised Howe curves of genus five attaining the Serre bound*, arXiv:2412.03071 (first public 2024-12-04), Sections 2 and 4.
