# Schwarz-gap rigidity for real Poisson extremizers

## Finding

Fix
\[
1<p<\infty,
\qquad
0<r<1.
\]
Let
\[
f\in L^\infty_0(\mathbb T;\mathbb R),
\qquad
\|f\|_\infty=1,
\]
and let
\[
u=P[f].
\]
Choose the harmonic conjugate \(v\) so that the analytic completion
\[
F=u+iv
\]
satisfies
\[
F(0)=0.
\]

Set
\[
\Phi(z)=\frac4\pi\arctan z,
\qquad
U=\operatorname{Re}\Phi.
\]
The map \(\Phi\) conformally maps \(\mathbb D\) onto the vertical strip
\[
\{w:|\operatorname{Re}w|<1\}.
\]
Thus
\[
\omega=\Phi^{-1}\circ F
\]
is a holomorphic self-map of \(\mathbb D\) fixing the origin and
\[
u=U\circ\omega.
\]

Define
\[
q_r(f)
=
\max_{|z|\le r}
\left|
\frac{\omega(z)}{z}
\right|,
\]
where the value at zero is interpreted as
\[
\omega'(0).
\]
Then
\[
0\le q_r(f)\le1
\]
and
\[
\|P_r f\|_p^p
\le
M_p\!\left(q_r(f)r\right),
\]
where
\[
M_p(\rho)
=
\int_{\mathbb T}
|U(\rho\zeta)|^p\,dm(\zeta).
\]

The function \(M_p\) is strictly increasing on
\[
(0,1).
\]
Therefore every non-extremal Schwarz quotient produces a strict norm gap:
\[
q_r(f)<1
\quad\Longrightarrow\quad
\|P_r f\|_p
<
M_p(r)^{1/p}.
\]

The recent sharp-norm theorem identifies
\[
M_p(r)^{1/p}
=
\|P_r\|_{L^\infty_0(\mathbb T;\mathbb R)\to L^p}.
\]
Hence equality in that operator norm occurs if and only if
\[
q_r(f)=1.
\]
By the maximum-modulus principle this happens if and only if
\[
\omega(z)=e^{i\theta_0}z
\]
for some real \(\theta_0\). Taking radial boundary values then gives
\[
f(e^{i\theta})
=
\operatorname{sgn}\cos(\theta+\theta_0)
\]
almost everywhere.

Thus, at every finite radius and every
\[
1<p<\infty,
\]
the complete normalized extremizer set consists exactly of rotations of the square-wave trace
\[
\operatorname{sgn}\cos\theta.
\]

## Assumptions and scope

The boundary measure \(m\) is normalized Haar measure on \(\mathbb T\).

The Poisson operator is
\[
P_r f(\zeta)
=
\sum_{n\in\mathbb Z}
r^{|n|}
\widehat f(n)\zeta^n.
\]
The subscript zero means
\[
\widehat f(0)=0.
\]

The result concerns real-valued data and finite radii
\[
0<r<1.
\]
It is a rigidity and quantitative refinement of the exact real operator norm. It is not a statement about the unresolved complex endpoint problem.

The normalization
\[
\|f\|_\infty=1
\]
is only for convenience. By homogeneity, every nonzero extremizer without normalization is a real scalar multiple of a rotated
\[
\operatorname{sgn}\cos\theta.
\]

## Proof

The recent proof of the sharp real norm starts from the strip map
\[
\Phi(z)=\frac4\pi\arctan z.
\]
Since
\[
|u|<1
\]
in \(\mathbb D\), the normalized analytic completion \(F=u+iv\) maps \(\mathbb D\) into the strip
\[
|\operatorname{Re}w|<1.
\]
Therefore
\[
\omega=\Phi^{-1}\circ F
\]
is a disk self-map satisfying
\[
\omega(0)=0
\]
and
\[
u=U\circ\omega.
\]

By Schwarz's lemma,
\[
g(z)=
\begin{cases}
\omega(z)/z,&z\ne0,\\
\omega'(0),&z=0
\end{cases}
\]
is holomorphic in \(\mathbb D\) and satisfies
\[
|g(z)|\le1.
\]
For fixed \(r\), set
\[
q=q_r(f)=\max_{|z|\le r}|g(z)|.
\]

If
\[
q=0,
\]
then \(g\) vanishes on the disk of radius \(r\), hence identically, so \(u\equiv0\), and the claimed estimate is immediate.

Assume
\[
q>0.
\]
For
\[
|z|<1,
\]
define
\[
\psi(z)=\frac{\omega(rz)}{qr}.
\]
Since
\[
|\omega(rz)|
=
r|z||g(rz)|
\le
qr|z|,
\]
we have
\[
|\psi(z)|\le|z|,
\qquad
\psi(0)=0.
\]
Thus \(\psi\) is a holomorphic self-map of the disk fixing zero.

Now define
\[
V(z)=U(qrz).
\]
Then
\[
u(rz)
=
U(\omega(rz))
=
V(\psi(z)).
\]
Because
\[
p>1
\]
and \(V\) is harmonic,
\[
|V|^p
\]
is subharmonic. Littlewood's subordination principle therefore gives
\[
\int_{\mathbb T}
|u(r\zeta)|^p\,dm(\zeta)
\le
\int_{\mathbb T}
|U(qr\zeta)|^p\,dm(\zeta),
\]
which is
\[
\|P_r f\|_p^p
\le
M_p(qr).
\]

It remains to identify when this can reach the sharp value
\[
M_p(r).
\]

First, \(M_p\) is strictly increasing. Indeed,
\[
\Phi'(z)=\frac{4}{\pi(1+z^2)}
\]
does not vanish in \(\mathbb D\). Hence
\[
|\nabla U|>0.
\]
On the open set where
\[
U\ne0,
\]
one has
\[
\Delta|U|^p
=
p(p-1)|U|^{p-2}|\nabla U|^2
>
0.
\]
Every nonempty annulus in \(\mathbb D\) contains such an open set. The circular means of a subharmonic function increase according to its Riesz mass, so
\[
0<\rho_1<\rho_2<1
\quad\Longrightarrow\quad
M_p(\rho_1)<M_p(\rho_2).
\]

Consequently,
\[
q<1
\]
implies
\[
\|P_r f\|_p^p
\le
M_p(qr)
<
M_p(r).
\]

If instead
\[
q=1,
\]
then the bounded analytic function \(g\) attains modulus one at a point of the closed disk
\[
|z|\le r<1.
\]
The maximum-modulus principle forces
\[
g(z)=e^{i\theta_0}
\]
for some real \(\theta_0\). Hence
\[
\omega(z)=e^{i\theta_0}z
\]
and
\[
u(z)=U(e^{i\theta_0}z).
\]
Since \(U\) is the Poisson integral of
\[
\operatorname{sgn}\cos\theta,
\]
uniqueness of \(L^\infty\) radial boundary values yields
\[
f(e^{i\theta})
=
\operatorname{sgn}\cos(\theta+\theta_0)
\]
almost everywhere.

Conversely every such rotation gives equality by rotational invariance. This proves both the quantitative refinement and the complete extremizer classification.

## Verification

The recent primary source was inspected at the definition of Schwarz-contractivity, the strip conformal map, the representation
\[
u=U\circ\omega,
\]
the subharmonic Littlewood step, and the exact real operator norm. The paper states that the square-wave trace attains the norm but does not classify all equality cases.

The refinement was checked directly from the same analytic objects. The only additional ingredients are Schwarz's lemma, the maximum-modulus principle, Littlewood subordination after a finite-radius rescaling, and strict growth of the circular means of the non-harmonic subharmonic function
\[
|U|^p.
\]

The strictness step does not rely on finite sampling. It follows from the positive Riesz mass of
\[
|U|^p
\]
in every annulus.

No numerical experiment is used.

## Relationship to prior work

Kovalev's 2026 paper proves the exact real
\[
L^\infty_0\to L^p
\]
Poisson norm by subordinating every admissible harmonic function to the strip extremal \(U\). It records that
\[
\operatorname{sgn}\cos\theta
\]
attains the norm. It does not state that these rotations are the only extremizers, nor does it give the finite-radius refinement through \(q_r(f)\).

Classical Littlewood subordination supplies the non-strict integral-mean inequality used in the source. The 2024 refinement of Dmitrović and Karapetrović treats a different hypothesis in which the subordinating symbol is univalent. Here the symbol \(\omega\) arising from an arbitrary real bounded harmonic function need not be univalent; the present estimate instead uses the Schwarz quotient
\[
\omega(z)/z
\]
on the fixed disk of radius \(r\).

The classical harmonic Schwarz literature gives sharp pointwise bounds for real harmonic maps. Those bounds do not by themselves identify equality in the circular
\[
L^p
\]
operator norm.

Targeted searches under equality-case, strict-subordination, Schwarz-quotient, and rotated-square-wave formulations did not locate a statement implying this complete finite-radius classification.

## Limitations

The quantity
\[
q_r(f)
\]
is intrinsic to the analytic strip lift of \(f\), but this result does not convert
\[
1-q_r(f)
\]
into a boundary-space distance from the extremizer orbit. Thus it is a strict quantitative refinement, not yet an
\[
L^\infty
\]
stability theorem.

The argument is stated for
\[
1<p<\infty.
\]
The endpoint
\[
p=1
\]
would require a separate treatment of the Riesz measure of
\[
|U|.
\]

The result is restricted to real-valued data.

## References

1. L. V. Kovalev, *Schwarz-contractivity of the Poisson operator*, arXiv:2609.28938v1, 2026.
2. J. E. Littlewood, *On inequalities in the theory of functions*, Proceedings of the London Mathematical Society 23 (1925), 481–519.
3. P. L. Duren, *Theory of \(H^p\) Spaces*, Academic Press, 1970.
4. D. Dmitrović and B. Karapetrović, *Sharpening Littlewood subordination principle with univalent symbol*, Mathematika 70 (2024), e12254. DOI: 10.1112/mtk.12254.
5. D. Kalaj and M. Vuorinen, *On harmonic functions and the Schwarz lemma*, Proceedings of the American Mathematical Society 140 (2012), 161–165.
