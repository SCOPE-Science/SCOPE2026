# A supra-Hilbert \(A_{2,p}\) plateau on Banaś--Frączek planes
## Finding
For every real \(\lambda\ge\sqrt2\), let \(R_\lambda^2=(\mathbb R^2,N_\lambda)\) with
\[
N_\lambda(u,v)=\max\left\{\lambda|u|,\sqrt{u^2+v^2}\right\}.
\]
For every \(p\in[2,\infty]\), the generalized Baronti constant satisfies
\[
A_{2,p}(R_\lambda^2)=1+\sqrt{1-\lambda^{-2}}.
\]
More precisely, if
\[
G_\lambda(\tau)=
\sup_{N_\lambda(x)=N_\lambda(y)=1}
\frac{N_\lambda(x+\tau y)+N_\lambda(x-\tau y)}2,
\qquad 0\le\tau\le1,
\]
then
\[
G_\lambda(\tau)=
\frac{1+\tau+\sqrt{1+2(1-2\lambda^{-2})\tau+\tau^2}}2.
\]
For every finite \(p\ge2\), the normalized Baronti profile
\[
\frac{2^{1/p}G_\lambda(\tau)}{(1+\tau^p)^{1/p}}
\]
is nondecreasing on \([0,1]\), so the maximum occurs at \(\tau=1\); for \(p=\infty\) the same conclusion follows directly from the displayed formula.

Writing
\[
a=\lambda^{-1},
\qquad
b=\sqrt{1-\lambda^{-2}},
\qquad
\kappa=b^2-a^2=1-2\lambda^{-2},
\]
one extremizing unit pair for every \(\tau\in[0,1]\) is
\[
x=(a,b),
\qquad
y=(-a,b).
\]
At \(\tau=1\), this pair gives
\[
A_{2,p}(R_\lambda^2)=1+b
\]
simultaneously for every \(p\in[2,\infty]\).

## Assumptions and scope
The scalar field is real, the dimension is exactly two, and \(\lambda\ge\sqrt2\). The generalized Baronti constant is
\[
A_{2,p}(X)=
\sup\left\{
\frac{\|u+v\|+\|u-v\|}{2}:
u,v\in X,\ 
\left(\|u\|^p+\|v\|^p\right)^{1/p}\le2^{1/p}
\right\}
\]
for finite \(p\), with the usual maximum-norm interpretation when \(p=\infty\).

The result concerns the classical Banaś--Frączek plane
\[
N_\lambda(u,v)=
\max\left\{\lambda|u|,\sqrt{u^2+v^2}\right\}.
\]
No assertion is made here for \(1<\lambda<\sqrt2\) or for the generalized \(\ell_r\)-based Banaś--Frączek family.

## Proof
Let
\[
E(u,v)=\sqrt{u^2+v^2},
\qquad
F(u,v)=\lambda|u|.
\]
Then \(N_\lambda=\max\{E,F\}\), and the closed unit ball is
\[
B_\lambda=
\left\{
(u,v):u^2+v^2\le1,\ |u|\le a
\right\}.
\]
Fix \(0\le\tau\le1\). We estimate
\[
N_\lambda(x+\tau y)+N_\lambda(x-\tau y)
\]
for \(x,y\in B_\lambda\), separating the four possible active-branch combinations.

If both terms use \(E\), then the Euclidean parallelogram identity and Cauchy inequality give
\[
E(x+\tau y)+E(x-\tau y)
\le
2\sqrt{1+\tau^2}.
\]
If both terms use \(F\), then
\[
F(x+\tau y)+F(x-\tau y)
=
2\lambda\max\{|x_1|,\tau|y_1|\}
\le2.
\]

It remains to treat a mixed branch. Consider
\[
E(x+\tau y)+F(x-\tau y).
\]
For a Euclidean unit vector \(w=(w_1,w_2)\) and a sign \(\sigma\in\{-1,1\}\),
\[
E(x+\tau y)+F(x-\tau y)
=
\sup_{w,\sigma}
\left[
(w+\sigma\lambda e_1)\cdot x+
\tau(w-\sigma\lambda e_1)\cdot y
\right].
\]
Thus its maximum over \(B_\lambda\times B_\lambda\) is
\[
\sup_{w,\sigma}
\left[
h_{B_\lambda}(w+\sigma\lambda e_1)
+
\tau h_{B_\lambda}(w-\sigma\lambda e_1)
\right],
\]
where \(h_{B_\lambda}\) is the support function.

For \(\lambda\ge\sqrt2\), both vectors \(w\pm\lambda e_1\) expose the vertical circular-cut vertices of \(B_\lambda\). Indeed, with \(t=w_1\),
\[
(\lambda^2-1)(\lambda-t)^2-(1-t^2)
=
\lambda^2-2+
(-\lambda^2+\lambda t+1)^2
\ge0,
\]
and the same identity with \(t\) replaced by \(-t\) handles the other sign. Consequently,
\[
h_{B_\lambda}(c,d)=a|c|+b|d|
\]
for these two supporting directions.

Taking \(\sigma=1\) without loss of generality and maximizing over \(w\) now gives
\[
\begin{aligned}
&h_{B_\lambda}(w+\lambda e_1)
+
\tau h_{B_\lambda}(w-\lambda e_1)\\
&=
1+\tau
+
a(1-\tau)w_1+
b(1+\tau)|w_2|\\
&\le
1+\tau+
\sqrt{a^2(1-\tau)^2+b^2(1+\tau)^2}\\
&=
1+\tau+
\sqrt{1+2\kappa\tau+\tau^2}.
\end{aligned}
\]
Equality is obtained by
\[
x=(a,b),
\qquad
y=(-a,b).
\]
For this pair,
\[
x+\tau y=(a(1-\tau),b(1+\tau))
\]
lies on the Euclidean-active side, while
\[
x-\tau y=(a(1+\tau),b(1-\tau))
\]
lies on the \(F\)-active side. Hence the mixed upper bound is attained.

Because \(\kappa\ge0\),
\[
\sqrt{1+2\kappa\tau+\tau^2}
\ge
\sqrt{1+\tau^2},
\]
and
\[
1+\tau\ge\sqrt{1+\tau^2}.
\]
Therefore the mixed value dominates both same-branch bounds. This proves
\[
G_\lambda(\tau)=
\frac{1+\tau+\sqrt{1+2\kappa\tau+\tau^2}}2.
\]

Baronti and Papini's unit-sphere reduction gives, for finite \(p\),
\[
A_{2,p}(R_\lambda^2)
=
\sup_{0\le\tau\le1}
\frac{2^{1/p}G_\lambda(\tau)}
{(1+\tau^p)^{1/p}}.
\]
Put
\[
s(\tau)=\sqrt{1+2\kappa\tau+\tau^2}.
\]
For \(p=2\), direct differentiation gives
\[
\left(
\frac{G_\lambda'(\tau)}{G_\lambda(\tau)}
-
\frac{\tau}{1+\tau^2}
\right)
G_\lambda(\tau)s(\tau)(1+\tau^2)
=
\frac{(1-\tau)\bigl(\kappa(1+\tau)+s(\tau)\bigr)}2
\ge0.
\]
For every finite \(p\ge2\),
\[
\frac{\tau^{p-1}}{1+\tau^p}
\le
\frac{\tau}{1+\tau^2}
\qquad(0\le\tau\le1),
\]
because \(\tau^{p-2}\le1\). Hence
\[
\frac{d}{d\tau}
\log
\left(
\frac{G_\lambda(\tau)}
{(1+\tau^p)^{1/p}}
\right)
\ge0.
\]
Thus the normalized profile is nondecreasing and its maximum occurs at \(\tau=1\). When \(p=\infty\), the same conclusion follows directly because \(G_\lambda\) itself is increasing.

Finally,
\[
G_\lambda(1)
=
\frac{2+\sqrt{4-4\lambda^{-2}}}{2}
=
1+\sqrt{1-\lambda^{-2}}.
\]
This proves the stated formula for every \(p\in[2,\infty]\).

## Verification
The active-branch decomposition is exhaustive because each of the two numerator norms is the maximum of exactly two functions, \(E\) and \(F\). The support-function step optimizes over the entire unit ball, not over sampled boundary points.

The key strip-support condition is certified algebraically by
\[
(\lambda^2-1)(\lambda-t)^2-(1-t^2)
=
\lambda^2-2+
(-\lambda^2+\lambda t+1)^2,
\]
so it is valid for every \(t\in[-1,1]\) exactly throughout the claimed regime \(\lambda\ge\sqrt2\).

The maximizing pair
\[
x=(\lambda^{-1},\sqrt{1-\lambda^{-2}}),
\qquad
y=(-\lambda^{-1},\sqrt{1-\lambda^{-2}})
\]
has \(N_\lambda(x)=N_\lambda(y)=1\), and the two active branches at the mixed optimum can be checked directly. No numerical optimization or finite enumeration is used in the proof.

## Relationship to prior work
Banaś and Frączek introduced the plane \(R_\lambda^2\) with the exact max norm above while studying deformation, convexity, and smoothness. Their work does not define the later generalized Baronti constants.

Baronti and Papini introduced the family \(A_{2,p}\), proved its unit-sphere reduction, and computed it for several concrete spaces, including the regular hexagon, regular octagon, the \(\ell_2-\ell_\infty\) Day--James plane, and \(L_s\) spaces. The inspected article contains no Banaś--Frączek example. Their Proposition 4.2 gives a closed formula under the hypothesis that the Day modulus is linear in \(\tau\). The present profile is not in that class for finite \(\lambda\ge\sqrt2\): its excess \(G_\lambda(\tau)-1\) has derivative \(1-\lambda^{-2}\) at \(0\), while its value at \(1\) is \(\sqrt{1-\lambda^{-2}}\), and these are unequal.

Yang and Yang later studied the generalized Banaś--Frączek family
\[
\max\{\lambda|x_1|,\|x\|_r\}
\]
and obtained James-type and von Neumann--Jordan constants. Their \(r=2\) member is the present space, but those are different invariants and do not imply the \(A_{2,p}\) profile.

## Limitations
The theorem covers the regime \(\lambda\ge\sqrt2\) and parameters \(p\ge2\). The proof uses the fact that both shifted Euclidean support directions are forced onto the vertical-strip boundary; this fails uniformly below \(\sqrt2\), so no lower-\(\lambda\) formula is claimed.

The literature search cannot rule out an older equivalent computation under different terminology. In particular, later work on generalized von Neumann--Jordan or other two-parameter constants for Banaś--Frączek spaces is not logically equivalent to the Baronti family treated here.

## References
1. J. Banaś and K. Frączek, “Deformation of Banach spaces,” *Commentationes Mathematicae Universitatis Carolinae* 34 (1993), 47--53. Public digital record: DML-CZ 118554.
2. M. Baronti and P. L. Papini, “Triangles, parameters, modulus of smoothness in normed spaces,” *Mathematical Inequalities & Applications* 19 (2016), 197--207, DOI 10.7153/mia-19-15; published online 2016-03-11.
3. C. Yang and X. Yang, “On the James type constant and von Neumann-Jordan constant for a class of Banaś-Frączek type spaces,” *Journal of Mathematical Inequalities* 10 (2016), 551--558, DOI 10.7153/jmi-10-43.
