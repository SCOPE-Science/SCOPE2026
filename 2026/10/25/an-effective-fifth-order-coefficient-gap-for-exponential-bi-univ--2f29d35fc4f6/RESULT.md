# An effective fifth-order coefficient gap for exponential bi-univalent subordination

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). Suppose that \(f(z)=z+a_2z^2+\cdots\) is analytic in \(\mathbb D\), its inverse germ at the origin extends holomorphically to \(\mathbb D\) as \(g\), and there exist Schwarz maps \(\omega,\eta:\mathbb D\to\mathbb D\), both vanishing at the origin, for which
\[
\frac{f(z)}z=e^{\omega(z)},\qquad \frac{g(z)}z=e^{\eta(z)}.
\]
Then
\[
\boxed{|a_2|^2<\frac{191}{288}},
\]
and hence the supremum of \(|a_2|\) over this class is at most \(\sqrt{191/288}=0.814\ldots\). This gives an explicit positive gap of \(1/288\) below the standard joint-second-order coefficient-square ceiling \(2/3\). No sharpness assertion is made.

## Assumptions and scope
The extension \(g\) must have the Taylor series of the genuine local inverse of \(f\); two unrelated functions with the displayed subordinations do not suffice. Global univalence of \(f\) and \(g\), as ordinarily required in a bi-univalent class, is allowed but not needed for the bound. The Schwarz functions are analytic maps of the unit disk into itself, vanish at the origin, and need not be univalent. The exponential is the ordinary entire exponential. The theorem is for the identity-operator two-sided exponential-subordination class, not for arbitrary multiplier operators.

## Proof
Rotation allows us to assume \(u=a_2\in[0,1)\). Put \(r=u^2\), \(R=1-r\), and write
\[
\omega(z)=uz+vz^2+wz^3+xz^4+O(z^5),\quad
\eta(z)=-uz+sz^2+tz^3+yz^4+O(z^5).
\]
Since \(f(z)/z=e^{\omega(z)}\) and \(g(z)/z=e^{\eta(z)}\), the formal inverse-series identities give
\[
s=r-v,\qquad t=3uv-w-\tfrac32u^3,
\]
and the coefficient of order four in the logarithm of the inverse gives the **exact fifth-order compatibility identity**
\[
0=\Delta:=\frac83u^4-8u^2v+4uw+2v^2-x-y.\tag{1}
\]
For transparency, coefficient extraction begins with
\[
\begin{aligned}
a_3&=v+u^2/2,\\
a_4&=w+uv+u^3/6,\\
a_5&=x+uw+v^2/2+u^2v/2+u^4/24,
\end{aligned}
\]
while the inverse coefficients through degree five are
\[
-a_2,\quad 2a_2^2-a_3,\quad -5a_2^3+5a_2a_3-a_4,\quad
14a_2^4-21a_2^2a_3+3a_3^2+6a_2a_4-a_5.
\]
Expanding the logarithm of the inverse quotient yields the coefficient \(\frac83u^4-8u^2v+4uw+2v^2-x\); it must equal \(y\), proving (1).

Schwarz–Pick applied to \(\omega(z)/z\) and \(\eta(z)/z\) gives \(|v|\le R\), \(|s|\le R\), so \(r=|v+s|\le2R\), equivalently \(r\le2/3\). To establish a quantitative improvement, suppose for contradiction \(191/288\le r\le2/3\) and put
\[
\delta=\frac23-r,\quad D=\frac1{288},\quad u_0=\sqrt{\frac23},\quad R_0=\frac13.
\]
Thus \(0\le\delta\le D\). Because \(s=r-v\), the parallelogram identity yields
\[
\left|v-\frac r2\right|^2
=\frac{|v|^2+|s|^2}{2}-\frac{r^2}{4}
\le R^2-\frac{r^2}{4}
=\delta+\frac34\delta^2
\le \left(\frac3{50}\right)^2.
\]
Write \(\rho=3/50\), \(V=\rho+D/2\), so \(|v-1/3|\le V\) and \(|s-1/3|\le V\).

Schwarz–Pick supplies analytic disk maps \(H,K\) with
\[
\omega(z)=uz+\frac{Rz^2H(z)}{1+uzH(z)},\qquad
\eta(z)=-uz+\frac{Rz^2K(z)}{1-uzK(z)}.
\]
Write \(H(z)=p+h_1z+h_2z^2+\cdots\), \(K(z)=q+k_1z+k_2z^2+\cdots\). Then
\[
p=\frac vR,\quad q=\frac sR,\quad
w=R(h_1-up^2),\quad t=R(k_1+uq^2),
\]
and
\[
x=R(h_2-2uph_1+u^2p^3),\qquad
y=R(k_2+2uqk_1+u^2q^3).\tag{2}
\]
A disk map \(H\) with constant coefficient \(p\) satisfies \(|h_j|\le1-|p|^2\) for every \(j\ge1\): average \(H\) over the \(j\)-th roots of unity, subtract the constant term through the disk automorphism taking \(p\) to zero, and apply the Schwarz lemma of order \(j\). The same holds for \(K\). Since \(|v|,|s|\ge r-R=2r-1\),
\[
1-|p|^2,\;1-|q|^2\le\frac{R^2-(2r-1)^2}{R^2}
=\frac{3\delta r}{R^2}\le18D=:E.
\]
Also \(R\ge1/3\), \(r/2-R=-3\delta/2\), so
\[
|p-1|,|q-1|\le3(\rho+3D/2)=:P.
\]
Set \(R_*=1/3+D\). We have \(R\le R_*\), \(|u-u_0|=\delta/(u+u_0)\le5D/4\), since \(u_0>4/5\). At the formal limiting extremal data \(\delta=0\), the coefficients forced by Schwarz–Pick are
\[
v_0=s_0=1/3,\quad w_0=-u_0/3,\quad x_0=y_0=2/9,
\]
so substitution into (1) yields \(\Delta_0=-46/27\). Equations (2), \(|p^2-1|\le2P\), and \(|p^3-1|\le3P\) imply
\[
|w-w_0|\le R_*(E+2P)+\frac{17D}{12}=:W,
\]
and
\[
|x-2/9|,\;|y-2/9|\le R_*(3E+3P)+\frac{4D}{3}=:X.
\]
Here \(|Rr-R_0(2/3)|\le4D/3\), and \(|R u-R_0u_0|\le17D/12\). We can now bound each term in (1) by its discrepancy from the limiting value:
\[
\begin{aligned}
|\Delta-\Delta_0|&\le
\frac{32D}{9}
+8\left(\frac{2V}{3}+\frac D3\right)
+4\left(W+\frac{5D}{12}\right)
+2V\left(R_*+\frac13\right)+2X\\
&=:S.
\end{aligned}
\]
With \(D=1/288\) and \(\rho=3/50\), **exact rational arithmetic** gives
\[
S=\frac{830093}{518400}<\frac{46}{27}=|\Delta_0|.
\]
Thus \(\Delta\neq0\), contradicting the necessary inverse coefficient identity (1). Therefore \(|a_2|^2<191/288\) for every member of the class.

## Verification
The accompanying `verify_gap.py` uses only the Python standard library to reproduce the strict rational comparison, the enclosing square-root inequality, and the positive margin. The formal inverse-coefficient identities in (1) can be reproduced by polynomial composition or symbolic power-series expansion; the proof above displays the exact coefficients so no numerical experiment is used as a substitute for the infinite-dimensional assertion.

## Relationship to prior work
Mahmood, Rasheed, Mihsin, and Atshan (2026) prove strict separation below \(\sqrt{2/3}\) for the exponential bi-univalent example by a fifth-order obstruction and explicitly state that their gap is unquantified. The present theorem supplies an elementary **effective numerical gap** for the identity-operator exponential two-sided subordination, based on quantitative near-extremal Schwarz coefficient rigidity. Unlike an abstract normal-family argument, it proves a reproducible rational estimate. The source's accessible abstract provides this stated distinction; its complete primary text was not obtained for a complete implication audit.

## Limitations
The constant \(191/288\) is not claimed sharp, and the exact second-coefficient extremal value remains open. The theorem does not cover nonidentity multiplier operators, different generators, or arbitrary unrelated inverse pairs. The comparison with the main 2026 paper is limited by incomplete access to its complete text; an unindexed stronger inequality may subsume the numerical bound.

## References
1. Z. H. Mahmood, R. O. Rasheed, B. K. Mihsin, W. G. Atshan, “Sharp joint Carathéodory compatibility and fifth-order lifting obstructions in bi-univalent function theory,” *AIMS Mathematics* **11** (2026), 32751–32781, DOI: 10.3934/math.20261285, first published 2026-10-10; abstract consulted at https://www.aimspress.com/article/doi/10.3934/math.20261285.
2. Classical Schwarz lemma and Schwarz–Pick inequality; only their elementary coefficient consequences are used.
