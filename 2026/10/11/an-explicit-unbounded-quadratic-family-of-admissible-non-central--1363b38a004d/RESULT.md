# An explicit unbounded quadratic family of admissible non-central section areas

## Finding

For every integer \(m\ge2\), define
\[
h_m=\frac{\pi}{2(2m+1+\sqrt2)},
\qquad
\gamma_m=\frac12-\frac{h_m}{\pi}.
\]
Then
\[
\gamma_m=[0;2,m,1,\overline{2}],
\]
where the bar denotes the infinite periodic tail \(2,2,\ldots\). Put
\[
R_m=\csc h_m,
\qquad
A_m=\frac{4\pi}{3}\cot^3 h_m.
\]

Let \(\mathbb A\) be the admissible area set of Haddad--Ryabogin. Then
\[
\boxed{A_m\in\mathbb A\quad\text{for every }m\ge2.}
\]
Consequently, if \(C\subset\mathbb R^4\) is a symmetric convex body of revolution containing the centered unit ball and every hyperplane tangent to that ball cuts \(C\) in the same three-dimensional area \(A_m\), then
\[
C=R_m B_2^4.
\]

The sequence is strictly increasing and unbounded:
\[
A_m\uparrow\infty.
\]
More precisely,
\[
R_m\sim\frac{4m}{\pi},
\qquad
A_m\sim\frac{256}{3\pi^2}m^3.
\]
Thus the admissible set \(\mathbb A\) reaches arbitrarily large section areas, through an explicit quadratic-irrational sequence whose rotation numbers approach the endpoint \(1/2\).

## Assumptions and scope

Haddad--Ryabogin associate to an area \(A>8\omega_3\), with \(\omega_3=4\pi/3\), the rotation number
\[
\gamma_A=\frac1\pi\arctan\!\left(\left(\frac{A}{\omega_3}\right)^{1/3}\right),
\]
the radius
\[
R_A=\sec(\pi\gamma_A),
\]
and the angular distances
\[
\delta_{A,k}
=
\pi\,\operatorname{dist}((2k-1)\gamma_A,\mathbb Z).
\]
For \(k\ge2\), let \(\alpha_{A,k}<\beta_{A,k}\) be the two smallest values among
\[
\delta_{A,1},\ldots,\delta_{A,k}.
\]
Their admissibility condition is
\[
F_{A,+}(\alpha_{A,k},\beta_{A,k})<\delta_{A,k+1},
\qquad
F_{A,-}(\alpha_{A,k})<\delta_{A,k+1}
\]
for every \(k\ge2\).

The result proves these inequalities for the displayed family. It does not solve the general Barker--Larman problem, remove the symmetry or body-of-revolution hypotheses, or characterize all of \(\mathbb A\).

## Proof

Write \(h=h_m\), \(\gamma=\gamma_m\), \(R=R_m\), and \(A=A_m\).

The periodic tail satisfies
\[
[2;2,2,\ldots]=1+\sqrt2,
\]
hence
\[
[1;2,2,\ldots]=\sqrt2.
\]
Therefore
\[
[0;2,m,1,\overline2]
=
\frac{m\sqrt2+1}{(2m+1)\sqrt2+2}
=
\frac12-\frac{1}{2(2m+1+\sqrt2)}
=
\gamma.
\]
Also
\[
\pi\gamma=\frac\pi2-h,
\]
so
\[
R=\sec(\pi\gamma)=\csc h
\]
and
\[
A=\frac{4\pi}{3}\tan^3(\pi\gamma)
=\frac{4\pi}{3}\cot^3 h.
\]
Since \(m\ge2\), one has \(h<\pi/8\), and therefore
\[
\cot h>\cot(\pi/8)=1+\sqrt2>2.
\]
Thus \(A>8\omega_3\), as required in the definition of \(\mathbb A\).

The continued-fraction coefficients are
\[
a_0=0,\quad a_1=2,\quad a_2=m,\quad a_3=1,\quad a_j=2\ \ (j\ge4).
\]
The first relevant convergent denominators are
\[
q_2=2m+1,\qquad q_3=2m+3,\qquad q_4=6m+7.
\]
They are odd, and all later denominators are odd as well.

We first verify the infinite tail of the admissibility conditions by Haddad--Ryabogin's Theorem 14. Their bounded-coefficient criterion at \(j_0=3\) is
\[
\frac{4\pi}
{\cos(\pi/q_3)\sqrt{R^2\cos^2(\pi/q_4)-1}}
\le q_3.
\]
For \(m\ge2\),
\[
h<\frac14,\qquad q_3\ge7,\qquad q_4\ge19.
\]
Using
\[
\cos x>1-\frac{x^2}{2},
\]
together with \(\pi/7<1/2\) and \(\pi/19<1/6\), gives
\[
\cos(\pi/q_3)>\frac78,
\qquad
\cos(\pi/q_4)>\frac{71}{72}.
\]
Since \(R=\csc h\),
\[
R^2\cos^2(\pi/q_4)-1
=
\frac{\cos^2(\pi/q_4)-\sin^2h}{\sin^2h}.
\]
Hence
\[
\frac{4\pi}
{\cos(\pi/q_3)\sqrt{R^2\cos^2(\pi/q_4)-1}}
=
\frac{4\pi\sin h}
{\cos(\pi/q_3)\sqrt{\cos^2(\pi/q_4)-\sin^2h}}.
\]
The bounds above imply
\[
\sqrt{\cos^2(\pi/q_4)-\sin^2h}>\frac{19}{20},
\]
and therefore
\[
\frac{4\pi}
{\cos(\pi/q_3)\sqrt{R^2\cos^2(\pi/q_4)-1}}
<
\frac{160\pi}{133}
<4<7\le q_3.
\]
Thus Theorem 14 gives \(C(A,k)\) for every
\[
k\ge\widetilde q_3=\frac{q_3+1}{2}=m+2.
\]

It remains to prove \(C(A,k)\) for
\[
2\le k\le m+1.
\]
Because
\[
\frac\pi2=(2m+1+\sqrt2)h,
\]
for \(1\le k\le m+1\) we have
\[
\delta_k=\frac\pi2-(2k-1)h.
\]
These values are strictly decreasing, so for \(2\le k\le m+1\),
\[
\alpha_k=\delta_k,
\qquad
\beta_k=\delta_{k-1}.
\]

For \(x>1\), the source function can be written
\[
G(x)=\arccos(1/x)-\left(\frac\pi2-h\right).
\]
Substitution of
\[
\alpha_k=\frac\pi2-(2k-1)h,
\qquad
\beta_k=\frac\pi2-(2k-3)h
\]
into the source definitions gives the exact identities
\[
F_-(\alpha_k)
=
\arcsin\!\left(
\frac{\sin h}{\sin((2k-1)h)}
\right)-h
\]
and
\[
F_+(\alpha_k,\beta_k)
=
h-\arcsin\!\left(
\tan h\,\sin(2(k-1)h)
\right).
\]

First take \(2\le k\le m\). Then
\[
\delta_{k+1}=\frac\pi2-(2k+1)h>h,
\]
so immediately
\[
F_+(\alpha_k,\beta_k)<h<\delta_{k+1}.
\]

For \(F_-\), the desired inequality is equivalent to
\[
3\sin h<\sin((4k-1)h).
\]
Indeed, after adding \(h\) and taking sine on the interval \((0,\pi/2)\), it becomes
\[
\frac{\sin h}{\sin((2k-1)h)}<\cos(2kh),
\]
and the product-to-sum identity gives the displayed condition.

Now
\[
7h\le(4k-1)h\le\pi-(3+2\sqrt2)h.
\]
Since sine has a single maximum on \([0,\pi]\),
\[
\sin((4k-1)h)
\ge
\min\{\sin(7h),\sin((3+2\sqrt2)h)\}.
\]
Because \(h<1/4\), the elementary estimate
\[
\sin x\ge x-\frac{x^3}{6}
\]
gives
\[
\sin(7h)
\ge
7h-\frac{343}{6}h^3
>
3h
>
3\sin h.
\]
Also \(3+2\sqrt2<6\) and \(3+2\sqrt2>21/4\), so
\[
\sin((3+2\sqrt2)h)
\ge
(3+2\sqrt2)h-\frac{(3+2\sqrt2)^3}{6}h^3
>
3h
>
3\sin h.
\]
Thus both inequalities in \(C(A,k)\) hold for every \(2\le k\le m\).

Finally take \(k=m+1\). Then
\[
\alpha_{m+1}=\sqrt2\,h,\qquad
\beta_{m+1}=(2+\sqrt2)h,
\qquad
\delta_{m+2}=(2-\sqrt2)h.
\]

For the minus branch,
\[
F_-(\alpha_{m+1})
=
\arcsin\!\left(\frac{\sin h}{\cos(\sqrt2 h)}\right)-h.
\]
The desired inequality is equivalent to
\[
2\sin h
<
\sin(3h)+\sin((3-2\sqrt2)h).
\]
The right side minus \(2\sin h\) equals
\[
\sin h\,(1-4\sin^2h)+\sin((3-2\sqrt2)h),
\]
which is strictly positive because \(h<1/4\).

For the plus branch,
\[
F_+(\alpha_{m+1},\beta_{m+1})
=
h-\arcsin\!\left(
\tan h\,\cos((1+\sqrt2)h)
\right).
\]
The desired inequality is equivalent to
\[
\sin(2h)>\tan(\sqrt2 h).
\]
Since \(h<1/4\),
\[
\sin(2h)
>
2h-\frac43h^3
>
\frac{23}{12}h,
\]
whereas
\[
\tan(\sqrt2 h)
<
\frac{\sqrt2\,h}{1-h^2}
<
\frac85h.
\]
Thus this inequality is also strict.

We have proved \(C(A,k)\) for \(2\le k\le m+1\), while Theorem 14 gives it for all \(k\ge m+2\). Hence
\[
A_m\in\mathbb A.
\]
Haddad--Ryabogin's rigidity theorem then yields
\[
C=R_mB_2^4.
\]

Finally, \(h_m\) decreases strictly to \(0\), so \(A_m\) increases strictly to infinity. Since
\[
h_m\sim\frac{\pi}{4m},
\]
the standard small-angle expansions give
\[
R_m=\csc h_m\sim\frac{4m}{\pi},
\qquad
A_m=\frac{4\pi}{3}\cot^3h_m
\sim
\frac{256}{3\pi^2}m^3.
\]

## Verification

The proof is analytic and covers every integer \(m\ge2\). The bundled checker independently verifies the continued-fraction formula, the first convergent denominators, the bounded-tail criterion, the exact formulas for \(F_+\) and \(F_-\), and the inequalities \(C(A_m,k)\) on a large finite stress-test range.

Those finite computations are diagnostic only. The infinite conclusion rests on the elementary inequalities above and on the cited Theorem 14 and rigidity theorem.

## Relationship to prior work

Haddad--Ryabogin prove that \(\mathbb A\) has positive Hausdorff dimension. Their explicit examples and all of their displayed large families remain in continued-fraction cylinders near fixed interior rotation numbers; in particular, the paper does not prove that \(\mathbb A\) is unbounded or exhibit admissible rotation numbers tending to \(1/2\).

A later published result proves that \(\mathbb A\) has positive Lebesgue measure by constructing a positive-measure restricted-digit cylinder near one interior admissible rotation number. Positive measure in a bounded cylinder does not imply that \(\mathbb A\) approaches the endpoint \(1/2\) or that the corresponding section areas are unbounded.

The present family supplies that missing boundary behavior explicitly:
\[
\gamma_m=[0;2,m,1,\overline2]\longrightarrow\frac12,
\qquad
A_m\longrightarrow\infty.
\]
Targeted searches for this continued-fraction family, unbounded admissible areas, arbitrarily large constant tangent-section areas, and equivalent endpoint formulations found no covering result.

A separate global Barker--Larman theorem for ellipsoids is not comparable in the needed direction: it removes the arithmetic restriction only after imposing the much narrower assumption that the unknown bodies themselves are ellipsoids.

## Limitations

The result proves unboundedness through one explicit countable sequence. It does not show that \(\mathbb A\) has positive measure arbitrarily far out, determine its asymptotic density, or characterize all admissible quadratic irrationals.

The geometric conclusion remains restricted to the four-dimensional symmetric bodies of revolution in the source theorem. The argument depends on the source's definitions of \(F_\pm\), its continued-fraction Theorem 14, and its rigidity theorem.

## References

1. J. Haddad and D. Ryabogin, *On convex bodies with constant non-central sections*, arXiv:2605.00299v1, first public 1 May 2026.
2. *Positive Lebesgue measure for admissible non-central section areas*, published mathematical result, 4 October 2026, record 9071214707a6.
3. *Global Barker--Larman rigidity for ellipsoids*, published mathematical result, 4 October 2026, record 75abc96cf1f6.
