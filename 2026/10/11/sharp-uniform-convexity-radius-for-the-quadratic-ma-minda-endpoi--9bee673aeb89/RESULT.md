# Sharp uniform-convexity radius for the quadratic Ma–Minda endpoint

## Finding

Let
\[
\phi(z)=1+z+\frac{z^2}{2}
\]
and
\[
\mathcal C(\phi)
=
\left\{
f\in\mathcal A:
1+\frac{zf''(z)}{f'(z)}\prec\phi(z)
\right\}.
\]
This is the endpoint member of the quadratic Ma–Minda family
\[
1+z+t z^2,
\qquad
0\le t\le\frac12,
\]
introduced in the primary source.

The sharp radius of uniform convexity of this endpoint class is
\[
\rho
=
0.646983632244827384202155177576\ldots,
\]
where \(\rho\) is the unique root in \((0,1)\) of
\[
\rho^6-4\rho^4+23\rho^2-9=0.
\]
Thus every dilation
\[
f_r(z)=\frac{f(rz)}{r}
\]
of every \(f\in\mathcal C(\phi)\) is uniformly convex for
\[
0<r<\rho,
\]
and this statement fails for every larger universal radius.

The first contact with the uniform-convexity parabola is nonreal. Define
\[
x_\rho
=
-\frac{\rho^4-11\rho^2+3}
{\rho(\rho^4-4\rho^2-3)}
=
-0.4910049966330048\ldots
\]
and
\[
\theta_\rho=\arccos x_\rho.
\]
Then
\[
w_\rho=\rho e^{i\theta_\rho}
\]
satisfies
\[
\operatorname{Re}\phi(w_\rho)
=
|\phi(w_\rho)-1|.
\]

## Assumptions and scope

The normalized analytic class is
\[
\mathcal A
=
\left\{
f\in\mathcal H(\mathbb D):
f(0)=0,
\ f'(0)=1
\right\}.
\]
A function is uniformly convex exactly when
\[
\operatorname{Re}
\left(
1+\frac{zf''(z)}{f'(z)}
\right)
>
\left|
\frac{zf''(z)}{f'(z)}
\right|
\]
throughout the disk.

Equivalently, the quantity
\[
1+\frac{zf''(z)}{f'(z)}
\]
must lie in the parabolic domain
\[
\Omega_{\mathrm{ucv}}
=
\left\{
q\in\mathbb C:
\operatorname{Re}q>|q-1|
\right\}.
\]

The theorem concerns the endpoint coefficient \(t=1/2\), which is the largest parameter allowed by the source's univalence condition for the quadratic target. It does not claim a formula for the whole parameter interval \(0\le t<1/2\).

## Proof

For
\[
f\in\mathcal C(\phi),
\]
there is a Schwarz function \(w\), with
\[
w(0)=0,
\qquad
|w(z)|<1,
\]
such that
\[
1+\frac{zf''(z)}{f'(z)}
=
\phi(w(z)).
\]
By Schwarz's lemma,
\[
|w(z)|\le|z|.
\]
Therefore it is enough to determine the largest \(r\) for which
\[
\phi(\mathbb D_r)
\subset
\Omega_{\mathrm{ucv}}.
\]

Write
\[
w=s e^{i\theta},
\qquad
x=\cos\theta.
\]
Put
\[
u=w+\frac{w^2}{2},
\qquad
\phi(w)=1+u.
\]
The parabolic condition
\[
\operatorname{Re}(1+u)>|u|
\]
is equivalent to
\[
1+2\operatorname{Re}u-(\operatorname{Im}u)^2>0.
\]
On the circle \(|w|=s\), the left-hand side is the quartic
\[
\begin{aligned}
F(s,x)=\;&s^4x^4-s^4x^2+2s^3x^3-2s^3x\\
&+3s^2x^2-2s^2+2sx+1.
\end{aligned}
\]
At the two real endpoints,
\[
F(s,-1)=(1-s)^2,
\qquad
F(s,1)=(1+s)^2,
\]
so no first contact can occur there while \(0<s<1\).

An interior first contact must satisfy simultaneously
\[
F(s,x)=0
\]
and
\[
\frac{\partial F}{\partial x}(s,x)=0.
\]
Exact elimination of \(x\) gives
\[
\operatorname{Res}_x
\left(
F,
\frac{1}{2s}\frac{\partial F}{\partial x}
\right)
=
-s^{16}
\left(
s^6-4s^4+23s^2-9
\right).
\]
Hence every interior first-contact radius in \((0,1)\) must be a zero of
\[
Q(s)=s^6-4s^4+23s^2-9.
\]

Now
\[
Q'(s)
=
2s
\left(
3s^4-8s^2+23
\right).
\]
The quadratic
\[
3y^2-8y+23
\]
has negative discriminant and positive leading coefficient, so
\[
Q'(s)>0
\qquad
(0<s<1).
\]
Also
\[
Q(0)=-9,
\qquad
Q(1)=11.
\]
Thus \(Q\) has exactly one zero \(\rho\) in \((0,1)\).

Since
\[
F(0,x)=1,
\]
continuity and the absence of any endpoint or interior contact before \(\rho\) imply
\[
F(s,x)>0
\]
for every
\[
0\le s<\rho,
\qquad
-1\le x\le1.
\]

The linear subresultant at a common zero yields
\[
x_\rho
=
-\frac{\rho^4-11\rho^2+3}
{\rho(\rho^4-4\rho^2-3)}.
\]
Writing
\[
y=\rho^2,
\]
one has
\[
\frac25<y<\frac12.
\]
Modulo
\[
y^3-4y^2+23y-9=0,
\]
the inequality \(|x_\rho|<1\) reduces to positivity of
\[
-23y^2+283y-108,
\]
which is already positive at \(y=2/5\) and increasing on \([2/5,1/2]\). Hence
\[
-1<x_\rho<0,
\]
so the contact is a genuine nonreal point of the boundary circle.

The target \(\phi\) is univalent on \(\mathbb D\), as proved in the source. Therefore \(\phi(\mathbb D_s)\) is bounded by the Jordan curve \(\phi(se^{i\theta})\). The parabolic domain \(\Omega_{\mathrm{ucv}}\) is convex because, for \(q=X+iY\), it is
\[
X>
\frac{1+Y^2}{2}.
\]
Consequently, positivity of \(F(s,x)\) on the boundary circle implies
\[
\phi(\mathbb D_s)
\subset
\Omega_{\mathrm{ucv}}
\]
for every \(s<\rho\).

For sharpness, choose the canonical function determined by the identity
\[
1+\frac{zf_0''(z)}{f_0'(z)}
=
\phi(z).
\]
It is
\[
f_0(z)
=
\int_0^z
\exp\!\left(
\xi+\frac{\xi^2}{4}
\right)d\xi.
\]
At
\[
z=w_\rho,
\]
the parabolic inequality becomes equality. Thus, for every \(R>\rho\), the point \(w_\rho\) lies inside \(\mathbb D_R\) and the dilation criterion fails for this extremal. Hence \(\rho\) is sharp.

## Verification

The packaged exact-arithmetic checker reconstructs \(F\), differentiates it, and verifies the resultant
\[
-s^{16}(s^6-4s^4+23s^2-9).
\]
It verifies the endpoint identities
\[
F(s,-1)=(1-s)^2,
\qquad
F(s,1)=(1+s)^2,
\]
the subresultant formula for \(x_\rho\), the unique-root bracket
\[
0.646983632244827
<
\rho
<
0.646983632244828,
\]
and the exact contact identity.

The proof of positivity below \(\rho\) is not a finite sampling argument. It follows from continuity plus the exact classification of every possible first contact by the resultant.

## Relationship to prior work

Allu and Kumar introduced the quadratic target
\[
1+z+t z^2,
\qquad
0\le t\le\frac12,
\]
verified its Ma–Minda properties, and obtained sharp second and third Hankel determinant estimates. Their paper identifies \(t=1/2\) as the endpoint of the univalent quadratic-target range, but it does not study uniform convexity or its radius.

Uniformly convex functions are classically characterized by the parabolic condition
\[
\operatorname{Re}
\left(
1+\frac{zf''}{f'}
\right)
>
\left|
\frac{zf''}{f'}
\right|.
\]
A large radius literature applies this criterion to special functions and to other analytic classes. Those general works do not state the radius for the 2026 quadratic Ma–Minda endpoint above.

Related recent results for other Ma–Minda targets determine convexity, starlikeness, or uniform-convexity thresholds for different image domains. They do not imply the cubic equation
\[
y^3-4y^2+23y-9=0
\]
or the nonreal tangency mechanism for \(\phi(z)=1+z+z^2/2\).

Targeted searches using the exact source identifier, the quadratic target, uniform-convexity radius terminology, the parabolic-region formulation, and the resultant polynomial did not locate a published statement equivalent to this finding.

## Limitations

The result treats the structurally distinguished endpoint
\[
t=\frac12
\]
rather than giving a complete radius formula for all
\[
0\le t<\frac12.
\]

No quantitative stability estimate is claimed for functions whose parabolic defect is small near the sharp contact.

The theorem concerns uniform convexity, not stronger conic-domain variants such as \(k\)-uniform convexity or uniformly convex spirallikeness.

## References

1. V. Allu and S. Kumar, *Sharp Estimates of Hankel Determinants for certain classes of convex univalent functions*, arXiv:2604.16833v1, 2026.
2. A. W. Goodman, *On uniformly convex functions*, Annales Polonici Mathematici 56 (1991), 87–92.
3. F. Rønning, *Uniformly convex functions and a corresponding class of starlike functions*, Proceedings of the American Mathematical Society 118 (1993), 189–196.
4. R. M. Ali, *On the Largest Disc Mapped by Sum of Convex and Starlike Functions*, Abstract and Applied Analysis 2013, Article 682413.
