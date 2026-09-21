# Quantitative area stability for reduced polygons

Let \(R\) be a reduced Euclidean \(n\)-gon, where \(n\ge 5\) is odd, and let
\(\Delta=\Delta(R)\) be its thickness. Use Lassak's canonical angles
\(\psi_1,\ldots,\psi_n\in(0,\pi/2)\), which satisfy
\[
\psi_1+\cdots+\psi_n=\pi.
\]
Put
\[
\mu=\frac{\pi}{n},\qquad
f(x)=\bigl(1-\tan^2(x/2)\bigr)\tan(x/2).
\]
Lassak's butterfly decomposition gives
\[
\operatorname{area}(R)\le \frac{\Delta^2}{2}\sum_{i=1}^n f(\psi_i),
\]
while the regular reduced \(n\)-gon of thickness \(\Delta\) has area
\[
A_{\rm reg}(n,\Delta)=\frac{n\Delta^2}{2}f(\mu).
\]

Define
\[
q(x)=-f''(x)
=\tan(x/2)+4\tan^3(x/2)+3\tan^5(x/2),
\]
\[
c_n=\frac{f(\mu)-\mu f'(\mu)}{\mu^2},
\qquad
h_n=\frac{q(\mu)}2,
\]
and
\[
C_n=c_n+\frac{h_n-c_n}{n}.
\]

## Theorem

For every reduced Euclidean odd \(n\)-gon \(R\) with \(n\ge5\),
\[
\boxed{
A_{\rm reg}(n,\Delta)-\operatorname{area}(R)
\ge
\frac{\Delta^2}{2}\,C_n
\sum_{i=1}^n\left(\psi_i-\frac{\pi}{n}\right)^2.
}
\]
Moreover \(C_n>0\), and
\[
C_n
=
\frac{\pi}{6n}
+\frac{\pi}{12n^2}
+\frac{13\pi^3}{120n^3}
+O(n^{-4}).
\]

Thus a reduced \(n\)-gon whose area is within \(\varepsilon\Delta^2\) of the
regular \(n\)-gon satisfies the inverse stability estimate
\[
\sum_{i=1}^n\left(\psi_i-\frac{\pi}{n}\right)^2
\le \frac{2\varepsilon}{C_n}.
\]

## Proof

The function \(q=-f''\) is strictly increasing on \((0,\pi/2)\), since it is
a polynomial with positive coefficients in the increasing variable
\(\tan(x/2)\).

Consider the tangent deficit at the mean:
\[
D_\mu(x)=f(\mu)+f'(\mu)(x-\mu)-f(x).
\]
For \(0\le x\le\mu\), two integrations of \(q=-f''\) give
\[
D_\mu(x)=\int_x^\mu (t-x)q(t)\,dt.
\]
After writing \(t=x+s(\mu-x)\),
\[
\frac{D_\mu(x)}{(\mu-x)^2}
=
\int_0^1 s\,q\!\left(x+s(\mu-x)\right)\,ds
\ge
\int_0^1 s\,q(s\mu)\,ds
=c_n.
\]
The last identity follows from
\[
D_\mu(0)=f(\mu)-\mu f'(\mu).
\]

For \(x\ge\mu\),
\[
D_\mu(x)=\int_\mu^x (x-t)q(t)\,dt,
\]
so
\[
\frac{D_\mu(x)}{(x-\mu)^2}
=
\int_0^1(1-s)\,q\!\left(\mu+s(x-\mu)\right)\,ds
\ge \frac{q(\mu)}2=h_n.
\]
Also
\[
c_n=\int_0^1 s\,q(s\mu)\,ds\le \frac{q(\mu)}2=h_n.
\]

Let
\[
u_i=\mu-\psi_i\quad(\psi_i<\mu),\qquad
v_j=\psi_j-\mu\quad(\psi_j>\mu),
\]
and write
\[
U_2=\sum u_i^2,\qquad V_2=\sum v_j^2.
\]
Because \(\sum_i(\psi_i-\mu)=0\),
\[
\sum u_i=\sum v_j=:S.
\]
If there are \(m\) positive deviations, then \(m\le n-1\), and Cauchy's
inequality gives
\[
V_2\ge \frac{S^2}{m}\ge \frac{S^2}{n-1}\ge\frac{U_2}{n-1}.
\]
Hence
\[
V_2\ge \frac{U_2+V_2}{n}.
\]
Summing the one-sided tangent-deficit estimates therefore yields
\[
\begin{aligned}
n f(\mu)-\sum_i f(\psi_i)
&=\sum_iD_\mu(\psi_i)\\
&\ge c_nU_2+h_nV_2\\
&\ge
\left(c_n+\frac{h_n-c_n}{n}\right)(U_2+V_2)\\
&=C_n\sum_i(\psi_i-\mu)^2.
\end{aligned}
\]
Combining this with Lassak's area inequality proves the theorem.

Finally, Taylor expansion at zero gives
\[
c_n=\frac{\pi}{6n}+\frac{13\pi^3}{120n^3}+O(n^{-5}),
\qquad
h_n=\frac{\pi}{4n}+\frac{13\pi^3}{48n^3}+O(n^{-5}),
\]
which gives the displayed expansion of \(C_n\).

## Two-term sharpness for the underlying angle inequality

Let \(K_n\) be the largest constant for which
\[
n f(\mu)-\sum_{i=1}^n f(x_i)
\ge K_n\sum_{i=1}^n(x_i-\mu)^2
\]
holds for every \(x_i\in(0,\pi/2)\) with \(\sum_i x_i=\pi\).
The proof above gives \(K_n\ge C_n\).

For the opposite direction, let one coordinate tend to \(0\) and let the
remaining \(n-1\) coordinates tend to \(\pi/(n-1)\). This gives
\[
K_n\le R_n,
\]
where
\[
R_n=
\frac{n(n-1)}{\pi^2}
\left[
n f\!\left(\frac{\pi}{n}\right)
-(n-1)f\!\left(\frac{\pi}{n-1}\right)
\right].
\]
Its expansion is
\[
R_n
=
\frac{\pi}{6n}
+\frac{\pi}{12n^2}
+\frac{\pi(10+13\pi^2)}{120n^3}
+O(n^{-4}).
\]
Consequently,
\[
\boxed{
K_n=
\frac{\pi}{6n}
+\frac{\pi}{12n^2}
+O(n^{-3}).
}
\]
So the first two asymptotic terms in the explicit stability coefficient are
optimal for the scalar angle-sum problem underlying Lassak's Jensen step.

## Context

Lassak proved in 2005 that, among reduced Euclidean \(n\)-gons of fixed
thickness, the regular \(n\)-gon has maximal area. His proof introduces the
angles \(\psi_i\), proves \(\sum_i\psi_i=\pi\), establishes the butterfly-area
bound above, and then applies strict concavity of \(f\) and Jensen's
inequality. The present result quantifies that strictness by an explicit
variance deficit.

The usual uniform strong-concavity estimate based on
\(\inf_{[0,\pi/2]}(-f'')\) is vacuous here because \(f''(0)=0\). The
mean-dependent argument above instead exploits the monotonicity of
\(-f''\), together with the zero-sum constraint on the deviations.

## Scientific limitations

- The theorem controls Lassak's canonical angle variance. It does not by
  itself give Hausdorff-distance or vertex-coordinate stability.
- The coefficient \(C_n\) is explicit and has the two-term optimal scale for
  the underlying angle inequality, but no claim is made that it is the best
  possible coefficient for actual reduced polygons. Geometric realizability
  constraints and overlap among the butterflies can only strengthen the area
  deficit.
- Originality is asserted only to the best of our knowledge. Searches of the
  2005 source, later surveys on reduced bodies, and recent work on reduced
  polygons located the qualitative extremal theorem but no quantitative
  angle-variance refinement of this form.

## References

1. M. Lassak, *Area of reduced polygons*, Publicationes Mathematicae
   Debrecen 67 (2005), 349–354.
   https://doi.org/10.5486/PMD.2005.3159
2. M. Lassak and H. Martini, *Reduced convex bodies in Euclidean space—a
   survey*, Expositiones Mathematicae 29 (2011), 204–219.
   https://doi.org/10.1016/j.exmath.2011.01.006
3. M. Lassak and H. Martini, *Reduced Convex Bodies in Finite Dimensional
   Normed Spaces: A Survey*, Results in Mathematics 66 (2014), 405–426.
   https://doi.org/10.1007/s00025-014-0384-4
4. Á. Sagmeister, *On the perimeter, diameter and circumradius of ordinary
   hyperbolic reduced polygons*, Canadian Mathematical Bulletin (2025).
   https://doi.org/10.4153/S0008439525000189
