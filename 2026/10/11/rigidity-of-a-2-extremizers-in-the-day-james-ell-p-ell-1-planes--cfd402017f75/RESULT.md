# Rigidity of \(A_2\)-extremizers in the Day--James \(\ell_p-\ell_1\) planes
## Finding
Let \(1<p<\infty\), and let \(X_p=(\mathbb R^2,N_p)\) be the real Day--James plane
\[
N_p(u,v)=
\begin{cases}
\bigl(|u|^p+|v|^p\bigr)^{1/p},&uv\ge0,\\
|u|+|v|,&uv\le0.
\end{cases}
\]
For the Baronti--Casini--Papini constant
\[
A_2(X_p)=\sup_{x,y\in S_{X_p}}\frac{N_p(x+y)+N_p(x-y)}2,
\]
the known value is
\[
A_2(X_p)=1+2^{1/p-1}.
\]
Moreover, the complete equality set is rigid:
\[
\frac{N_p(x+y)+N_p(x-y)}2=1+2^{1/p-1}
\]
holds if and only if
\[
\{x,y\}=\{\varepsilon e_1,\delta e_2\}
\qquad
\text{for some }\varepsilon,\delta\in\{-1,1\}.
\]
Thus, for every \(1<p<\infty\), the only \(A_2\)-maximizing pairs are the two coordinate-axis unit vectors, up to order and independent sign changes of the two vectors.

## Assumptions and scope
The scalar field is real and \(1<p<\infty\). The norm is the classical sign-dependent Day--James norm displayed above. The endpoint \(p=1\) is excluded because the strict-convexity step used in the equality analysis degenerates there.

The quantity \(A_2(X)\) is the arithmetic-mean triangle constant
\[
A_2(X)=\sup_{x,y\in S_X}\frac{\|x+y\|+\|x-y\|}{2}.
\]

## Proof
Write
\[
H(x,y)=N_p(x+y)+N_p(x-y).
\]
Yang and Li prove
\[
H(x,y)\le 2+2^{1/p}
\qquad
(x,y\in S_{X_p})
\]
and equality of the supremum is obtained from \(e_1,e_2\). We retain the equality information in their estimates.

First classify maximizing pairs of extreme points. The extreme points of the unit ball are exactly
\[
\left\{(u,v): |u|^p+|v|^p=1,\ uv\ge0\right\}.
\]
Changing the sign of either whole vector leaves \(H\) unchanged, so an extreme pair may be written
\[
x=(a,b),\qquad y=(c,d),
\qquad a,b,c,d\ge0,
\]
with
\[
a^p+b^p=c^p+d^p=1.
\]

If
\[
(a-c)(b-d)\ge0,
\]
the two unit vectors are coordinatewise comparable. Equality of their \(\ell_p\)-norms forces \(x=y\), and then
\[
H(x,y)=2<2+2^{1/p}.
\]
Hence an extreme maximizing pair must cross. After interchanging the two vectors and, if needed, the two coordinates, assume
\[
a\ge c,\qquad b\le d.
\]
Then
\[
H(x,y)
=
\bigl((a+c)^p+(b+d)^p\bigr)^{1/p}
+a-c+d-b.
\]
Put
\[
s=a-c+d-b.
\]

If
\[
s\le2^{1/p},
\]
Minkowski's inequality gives
\[
\bigl((a+c)^p+(b+d)^p\bigr)^{1/p}\le2,
\]
so \(H(x,y)\le2+2^{1/p}\). Equality in this branch would require equality in Minkowski and \(s=2^{1/p}\). Because \(p>1\), equality in Minkowski for the two positive unit vectors forces \(x=y\), which gives \(s=0\), a contradiction. Thus this branch is strict.

If
\[
s\ge2^{1/p},
\]
the second branch of the Yang--Li estimate gives
\[
\begin{aligned}
H(x,y)
&\le
\bigl(a^p+d^p\bigr)^{1/p}
+\bigl(c^p+b^p\bigr)^{1/p}
+a-c+d-b\\
&\le
\bigl(a^p+d^p\bigr)^{1/p}+a+d\\
&\le
2^{1/p}+2.
\end{aligned}
\]
For equality in the final line, both independently bounded terms must be maximal:
\[
a+d=2,
\qquad
\bigl(a^p+d^p\bigr)^{1/p}=2^{1/p}.
\]
Since \(0\le a,d\le1\), this forces
\[
a=d=1.
\]
The unit equations then give \(b=c=0\). Hence every maximizing extreme pair is, up to order and vector signs,
\[
(e_1,e_2).
\]

It remains to exclude nonextreme maximizers. Every nonextreme point of \(S_{X_p}\) lies in the relative interior of one of the two \(\ell_1\)-edges in the opposite-sign quadrants. Such a point is a strict convex combination of the two coordinate-axis vertices bounding that edge. If, for example,
\[
x=\lambda u+(1-\lambda)v,
\qquad 0<\lambda<1,
\]
and \(H(x,y)=2+2^{1/p}\), joint convexity of \(H\) implies
\[
H(u,y)=H(v,y)=2+2^{1/p}.
\]
Decomposing \(y\), if necessary, into extreme points and applying the same equality argument produces an extreme point \(y_0\) such that both
\[
H(u,y_0)=H(v,y_0)=2+2^{1/p}.
\]
But the extreme-point classification says that an extreme maximizer must use the other coordinate axis. The two endpoints \(u,v\) lie on different coordinate axes, so no single \(y_0\) can maximize with both. This contradiction shows that no nonextreme point can occur in a maximizing pair.

Conversely, for
\[
x=\varepsilon e_1,\qquad y=\delta e_2,
\]
one of \(x+y,x-y\) lies in a same-sign quadrant and the other in an opposite-sign quadrant. Therefore their norms are \(2^{1/p}\) and \(2\), in some order, so every displayed pair attains the stated value.

## Verification
The proof is exact and covers the whole unit sphere, not a finite sample. The critical equality steps are:

1. strict equality in Minkowski for \(p>1\), which forces positive unit vectors to coincide;
2. the second Yang--Li branch, where equality at the global bound forces \(a=d=1\);
3. convexity on the two nonextreme \(\ell_1\)-edges, which would force one extreme point to maximize simultaneously with both coordinate-axis endpoints.

As a private stress test, dense/randomized sampling of the whole radial unit sphere was performed for several values of \(p\), including values close to \(1\) and large \(p\). The sampled maxima occurred only at coordinate-axis pairs. This computation is not used as proof.

## Relationship to prior work
Yang and Li compute the exact James-type constant
\[
J_{X,t}(\tau)
=
\left(
\frac{(1+\tau^p)^{t/p}+(1+\tau)^t}{2}
\right)^{1/t}
\]
for the same \(X=\ell_p-\ell_1\) family. At \(t=1\) and \(\tau=1\), this gives the known scalar value of \(A_2(X_p)\). Their proof explicitly uses \(x=e_1,y=e_2\) as a sharp witness and reduces the upper bound to extreme points, but it does not state a complete classification of all equality pairs.

Dinarvand later studies Hölder-mean constants, including \(A_2\), for absolute normalized norms on \(\mathbb R^2\) and several concrete spaces. The inspected full text does not treat the sign-dependent \(\ell_p-\ell_1\) family and contains no equality classification for it.

Targeted searches for \(A_2\)-extremizers, maximizing pairs, equality cases, and James-type equality in the \(\ell_p-\ell_1\) family found no statement equivalent to the classification above.

## Limitations
The result concerns only \(1<p<\infty\). It does not classify the degenerate endpoint \(p=1\), and it does not classify maximizers for the full three-parameter James-type functional \(J_{X,t}(\tau)\).

A 2007 paper on the Baronti constant of absolute normalized norms was located only at metadata level. Since the present Day--James norm is sign-dependent rather than absolute, it is not an evident covering source, but lack of inspectable full text remains a bibliographic residual risk.

## References
1. C. Yang and H. Li, “On the James type constant of \(\ell_p-\ell_1\),” *Journal of Inequalities and Applications* 2015, Article 79, DOI 10.1186/s13660-015-0598-3; published 2015-03-04.
2. M. Dinarvand, “Hölder's Means and Absolute Normalized Norms on \(\mathbb R^2\),” *Filomat* 31 (2017), 1583--1593, DOI 10.2298/FIL1706583D.
