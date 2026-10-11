# An exact four-dimensional spectral bound for Khachiyan central cuts

## Finding

For a convex body \(K\subset\mathbb R^4\), let \(w(K)\) denote the volume of its maximum-volume inscribed ellipsoid. Let \(H\) be a closed halfspace whose boundary passes through the center of that ellipsoid, and define
\[
c_4=\sup_{K,H}\frac{w(K\cap H)}{w(K)}.
\]
Then
\[
\boxed{
\frac{4\sqrt3}{9}\le c_4\le C_4
}
\]
with
\[
\boxed{
C_4=0.8162394033204106\ldots
<
\frac{\sqrt e}{2}=0.8243606353500640\ldots .
}
\]

The upper constant is exact for the pair of finite-dimensional spectral certificates proved by Zhou--Zou--Liu. Put
\[
f_1(\alpha)=\sqrt{\alpha+\frac{\alpha^2}{4}},
\qquad
f_2(\alpha)=\sqrt{f_1(\alpha)+\frac{\alpha^2}{16}},
\]
and
\[
U_1(\alpha)
=
\alpha\left(\frac{4-f_1(\alpha)}{3}\right)^6,
\qquad
U_2(\alpha)
=
\alpha\left(\frac{4-f_2(\alpha)}{3}\right)^{12}.
\]
There is a unique
\[
\alpha_*\in(0,1)
\]
for which
\[
U_1(\alpha_*)=U_2(\alpha_*).
\]
It satisfies
\[
0.523194<\alpha_*<0.523195
\]
and is the unique root in \((0,1)\) of
\[
\begin{aligned}
P(\alpha)
={}&
\alpha^8-3840\alpha^6-8192\alpha^5+548864\alpha^4\\
&+3145728\alpha^3+1048576\alpha^2
-33554432\alpha+16777216.
\end{aligned}
\]
Moreover
\[
\max_{0<\alpha\le1}\min\{U_1(\alpha),U_2(\alpha)\}
=
U_1(\alpha_*)=U_2(\alpha_*)=C_4.
\]

The lower endpoint follows from the dimension-four circular cone in the source:
\[
\frac12\left(\frac43\right)^{3/2}
=
\frac{4\sqrt3}{9}
=
0.7698003589195010\ldots .
\]

## Assumptions and scope

The statement concerns the central-cut maximum-inscribed-ellipsoid problem in dimension four. It improves the dimension-free upper constant by optimizing the two finite-dimensional inequalities already proved in the source.

It does not determine the exact value of \(c_4\). The lower and upper endpoints need not coincide. The upper endpoint is the best constant obtained by taking the pointwise minimum of the two published finite-dimensional spectral bounds and then optimizing over the smallest semiaxis.

After affine normalization, the John ellipsoid of \(K\) is \(B_2^4\). A candidate ellipsoid in the retained half has the form
\[
E(a,A)=a+A B_2^4,
\]
with \(A\) positive definite. Write
\[
\alpha=\lambda_{\min}(A).
\]
Since \(B_2^4\) is already the maximum-volume ellipsoid in \(K\) and \(E(a,A)\subseteq K\),
\[
\det A\le1.
\]
Hence
\[
0<\alpha\le1.
\]

## Proof

Zhou--Zou--Liu prove, for every feasible nonsingular normalized candidate in dimension \(n\ge2\),
\[
\det A
\le
\alpha
\left(
\frac{n-f_j(\alpha)}{n-1}
\right)^{2^j(n-1)},
\qquad
j=1,2.
\]
At \(n=4\) these are exactly
\[
\det A\le U_1(\alpha),
\qquad
\det A\le U_2(\alpha).
\]
Thus
\[
\det A\le \min\{U_1(\alpha),U_2(\alpha)\}.
\]

It remains to optimize this one-variable envelope exactly.

First compare the two bounds. Since all bases are positive on the feasible range,
\[
\frac{U_1(\alpha)}{U_2(\alpha)}
=
\left(
\frac{3(4-f_1(\alpha))}
{(4-f_2(\alpha))^2}
\right)^6.
\]
Therefore equality holds precisely when
\[
(4-f_2(\alpha))^2
=
3(4-f_1(\alpha)).
\]
Eliminating the two nested square roots gives the polynomial equation
\[
P(\alpha)=0
\]
displayed above. A Sturm calculation gives exactly one root of \(P\) in \((0,1)\), and exact sign evaluation at the rational endpoints gives
\[
P(0.523194)>0,
\qquad
P(0.523195)<0.
\]
The crossing equation itself has opposite signs at \(\alpha=1/2\) and \(\alpha=1\), so its unique zero is this polynomial root. Denote it by \(\alpha_*\).

Next use logarithmic concavity. Set \(x=\log\alpha\). The source proves that
\[
x\longmapsto f_j(e^x)
\]
is convex for \(j=1,2\). Hence
\[
x\longmapsto
\log U_j(e^x)
=
x+2^j\cdot3\,
\log\left(
\frac{4-f_j(e^x)}{3}
\right)
\]
is concave wherever the base is positive: \(4-f_j(e^x)\) is positive and concave, and the logarithm is increasing and concave.

For \(U_1\), its logarithmic derivative is
\[
D_1(\alpha)
=
1-\frac{6\alpha f_1'(\alpha)}{4-f_1(\alpha)}.
\]
The inequality \(D_1(\alpha)>0\) is equivalent, after multiplying positive quantities and squaring, to
\[
49\alpha^3+224\alpha^2+192\alpha-256<0.
\]
That cubic is strictly increasing for \(\alpha>0\), and it is still negative at \(0.523195\). Therefore
\[
D_1(\alpha_*)>0.
\]
Concavity of \(\log U_1(e^x)\) then implies that \(U_1\) is strictly increasing throughout the interval to the left of \(\alpha_*\).

For \(U_2\), write
\[
D_2(\alpha)
=
1-\frac{12\alpha f_2'(\alpha)}{4-f_2(\alpha)}.
\]
Eliminating the radicals from the equation \(D_2(\alpha)=0\) gives, apart from the harmless factor \(\alpha^3\),
\[
\begin{aligned}
Q(\alpha)={}&
28561\alpha^9+228488\alpha^8-689520\alpha^7
-9777664\alpha^6\\
&-12046336\alpha^5+115867648\alpha^4
+471859200\alpha^3\\
&+603979776\alpha^2+67108864\alpha-268435456.
\end{aligned}
\]
Sturm's theorem gives exactly one root of \(Q\) in \((0,1)\), lying in
\[
(0.5165,0.5166).
\]
At \(\alpha=1/2\), using
\[
f_2(1/2)=\frac78,
\qquad
f_2'(1/2)=\frac{43}{84},
\]
one gets
\[
D_2(1/2)=\frac{3}{175}>0.
\]
At \(\alpha=1\), one has \(D_2(1)<0\). An elementary bound suffices: with \(s=f_1(1)=\sqrt5/2\) and \(t=f_2(1)\),
\[
\sqrt5<\frac94,
\qquad
t<\frac54,
\qquad
f_1'(1)>\frac23,
\]
so
\[
f_2'(1)
=
\frac{f_1'(1)+1/8}{2t}
>
\frac{19}{60}.
\]
Since \(t>1\),
\[
12f_2'(1)>\frac{19}{5}>3>4-t,
\]
which is exactly \(D_2(1)<0\). Hence \(D_2\) changes sign at its unique zero below \(0.5166\). Since
\[
\alpha_*>0.523194,
\]
we have
\[
D_2(\alpha_*)<0.
\]
Concavity now implies that \(U_2\) is strictly decreasing to the right of \(\alpha_*\).

Before the crossing,
\[
\min\{U_1,U_2\}\le U_1\le U_1(\alpha_*),
\]
while after the crossing,
\[
\min\{U_1,U_2\}\le U_2\le U_2(\alpha_*).
\]
At the crossing the two quantities are equal, so
\[
\max_{0<\alpha\le1}\min\{U_1,U_2\}
=
C_4.
\]

Finally, every normalized maximum ellipsoid in a four-dimensional central half satisfies
\[
\frac{w(K\cap H)}{w(K)}
=
\det A
\le C_4.
\]
For the lower bound, the source's circular cone \(K_4\) has John ellipsoid \(B_2^4\) and its retained central half contains an ellipsoid whose semiaxes are
\[
\frac12,\sqrt{\frac43},\sqrt{\frac43},\sqrt{\frac43}.
\]
Its relative volume is
\[
\frac12\left(\frac43\right)^{3/2}
=
\frac{4\sqrt3}{9}.
\]
This proves the bracket.

## Verification

The bundled checker uses exact rational Sturm sequences. It verifies:

- \(P\) has exactly one root in \((0,1)\);
- that root lies in \((0.523194,0.523195)\);
- the cubic controlling \(D_1\) is negative at the upper isolating endpoint;
- \(Q\) has exactly one root in \((0,1)\);
- that root lies in \((0.5165,0.5166)\);
- the algebraic resultant identities producing \(P\) and \(Q\) are matched by independent high-precision evaluations;
- bisection of the original unsquared crossing equation gives
  \[
  \alpha_*=0.5231942870027930993\ldots
  \]
  and
  \[
  C_4=0.8162394033204106090\ldots .
  \]

The Sturm counts and rational endpoint signs are the exact certificates. The decimal evaluations are for reproducibility and display only.

## Relationship to prior work

Zhou--Zou--Liu prove the uniform sharp constant
\[
\frac{\sqrt e}{2}
\]
and derive the two finite-dimensional inequalities used here. Their Section 5.1 explicitly presents those inequalities as useful dimension-dependent bounds without optimizing them to determine a fixed-dimensional constant. Their later discussion likewise leaves the best constant in a prescribed dimension undetermined.

A published follow-up on the same circular cone determines the exact maximum-volume ellipsoid of the retained half-cone and therefore confirms that the source's lower witness has exact ratio
\[
\frac12\left(\frac n{n-1}\right)^{(n-1)/2}
\]
within that family. It explicitly does not claim fixed-dimensional extremality among all convex bodies. At \(n=4\), this supplies the lower endpoint
\[
4\sqrt3/9,
\]
not the upper bound obtained here.

Targeted searches for the numerical fingerprint \(0.816239403\), the crossing parameter \(0.523194287\), dimension-four optimization of the two source bounds, and equivalent central-cut formulations found no statement giving this optimized four-dimensional certificate.

## Limitations

The theorem does not determine \(c_4\) exactly. The interval
\[
\frac{4\sqrt3}{9}
\le c_4
\le 0.8162394033204106\ldots
\]
still has a substantial gap.

The upper bound is optimal only for the pair of finite-dimensional spectral inequalities currently used; a stronger geometric or spectral argument may improve it. No assertion is made for the exact fixed-dimensional constants in dimensions other than four.

The originality assessment covers the focal full text, the closest published cone computation, targeted database searches, and direct web searches for the exact numerical and algebraic fingerprints. Very recent unindexed work remains a residual bibliographic risk.

## References

1. Zhou Longfei, Haijun Zou, Tianhao Liu, *A Spectral Proof of Khachiyan's Ellipsoid Conjecture*, arXiv:2609.28447v1, 23 September 2026.
2. S. P. Tarasov, L. G. Khachiyan, I. I. Erlikh, *The method of inscribed ellipsoids*, Doklady Akademii Nauk SSSR 298(5) (1988), 1081--1085; English translation Soviet Mathematics Doklady 37 (1988), 226--230.
