# Sharp non-Euclidean Finsler-Hadwiger profiles

## Result

Let \(T\) be a nondegenerate geodesic triangle of perimeter
\[
p=a+b+c,\qquad s=\frac p2,
\]
and define the Finsler-Hadwiger side deficit
\[
D=(a-b)^2+(b-c)^2+(c-a)^2,\qquad
X=\frac{D}{p^2},\qquad
t=\sqrt{2X}.
\]
For every nondegenerate triangle, \(0\le X<1/2\), hence \(0\le t<1\). Put
\[
m=\frac p6.
\]

For the unit hyperbolic plane \(\mathbb H^2\), write \(A\) for area and set
\[
\phi_H(u)=\tanh\frac u2,\qquad
J_H(T)=\frac{\tan^2(A/4)}{\tanh(p/4)}.
\]
Then, for fixed \(p\) and \(D\),
\[
\boxed{
J_H(T)\le
\phi_H\!\bigl(m(1+2t)\bigr)
\phi_H\!\bigl(m(1-t)\bigr)^2
}
\tag{H+}
\]
and equality holds exactly, up to permutation, for the isosceles side triple
\[
\boxed{
(a,b,c)=
\left(\frac p3(1-t),\frac p6(2+t),\frac p6(2+t)\right).
}
\tag{E+}
\]

If \(0\le X<1/8\), there is also the sharp lower profile
\[
\boxed{
J_H(T)\ge
\phi_H\!\bigl(m(1-2t)\bigr)
\phi_H\!\bigl(m(1+t)\bigr)^2
}
\tag{H-}
\]
with equality exactly, up to permutation, for
\[
\boxed{
(a,b,c)=
\left(\frac p3(1+t),\frac p6(2-t),\frac p6(2-t)\right).
}
\tag{E-}
\]
For \(1/8\le X<1/2\), the infimum of \(J_H\) is \(0\); it is approached by nondegenerate triangles tending to a flat triangle and is not attained in \(\mathbb H^2\).

For the unit sphere \(S^2\), restrict to the usual geodesically convex minor-arc triangles, so \(0<p<2\pi\). Write \(A\in(0,2\pi)\) for spherical area and set
\[
\phi_S(u)=\tan\frac u2,\qquad
J_S(T)=\frac{\tan^2(A/4)}{\tan(p/4)}.
\]
The identical sharp profiles hold after replacing \(\phi_H\) by \(\phi_S\):
\[
\boxed{
J_S(T)\le
\phi_S\!\bigl(m(1+2t)\bigr)
\phi_S\!\bigl(m(1-t)\bigr)^2
}
\tag{S+}
\]
with equality exactly at (E+), and, for \(0\le X<1/8\),
\[
\boxed{
J_S(T)\ge
\phi_S\!\bigl(m(1-2t)\bigr)
\phi_S\!\bigl(m(1+t)\bigr)^2
}
\tag{S-}
\]
with equality exactly at (E-). Again, for \(1/8\le X<1/2\), the infimum is \(0\), approached at the degenerate boundary.

Equivalently, the exact maximal area is
\[
A_{\max}^{(\kappa)}(p,D)
=
4\arctan\sqrt{
\phi_\kappa(s)
\phi_\kappa\!\bigl(m(1+2t)\bigr)
\phi_\kappa\!\bigl(m(1-t)\bigr)^2
},
\]
where \(\kappa=H,S\), \(\phi_H(u)=\tanh(u/2)\), and \(\phi_S(u)=\tan(u/2)\). The analogous formula with \(1+2t,1-t\) replaced by \(1-2t,1+t\) gives the exact minimum when \(X<1/8\).

Thus the full vertical slice of the \((p,D,A)\) feasibility region is explicit: below the threshold \(X=1/8\), area lies between two isosceles branches; at and above that threshold, the lower branch is replaced by the degenerate boundary \(A=0\). Every intermediate admissible area is attained.

The formulas scale immediately to curvature \(-1/R^2\) or \(+1/R^2\) by replacing all lengths by length divided by \(R\) and area by area divided by \(R^2\).

## Proof

Set
\[
x=s-a,\qquad y=s-b,\qquad z=s-c.
\]
The strict triangle inequalities are exactly \(x,y,z>0\), and
\[
x+y+z=s=3m.
\]
Since
\[
a-b=y-x,\qquad b-c=z-y,\qquad c-a=x-z,
\]
the deficit satisfies
\[
D=(x-y)^2+(y-z)^2+(z-x)^2
   =3\sum_{\rm cyc}(x-m)^2.
\]
Hence, writing
\[
r=\sqrt{\frac D{18}}=mt,
\]
the constraints become
\[
x+y+z=3m,\qquad
(x-m)^2+(y-m)^2+(z-m)^2=6r^2.
\tag{1}
\]

### A three-variable moment lemma

Let \(f\in C^3(I)\) on an interval \(I\) and suppose \(f'''(u)>0\) throughout \(I\). Among triples \(x,y,z\in I\) with fixed
\[
e_1=x+y+z,\qquad e_2=xy+yz+zx,
\]
the symmetric quantity
\[
F(x,y,z)=f(x)+f(y)+f(z)
\]
is a strictly increasing function of
\[
e_3=xyz.
\]

For distinct \(x,y,z\), regard them as the roots of
\[
P(u)=u^3-e_1u^2+e_2u-e_3.
\]
Differentiating \(P(x_i)=0\) with respect to \(e_3\) gives
\[
\frac{dx_i}{de_3}=\frac1{P'(x_i)}.
\]
Consequently,
\[
\frac{dF}{de_3}
=
\sum_{i=1}^3\frac{f'(x_i)}{P'(x_i)}
=
f'[x,y,z],
\]
the second divided difference of \(f'\). Since \(f'''=(f')''>0\), \(f'\) is strictly convex and this divided difference is positive. Repeated-root cases follow by continuity.

Under (1), both \(e_1\) and \(e_2\) are fixed, because
\[
x^2+y^2+z^2=3m^2+6r^2
\]
is fixed.

### Extremizing the third elementary symmetric function

Every real triple satisfying (1) can be parametrized as
\[
x-m=2r\cos\theta,\quad
y-m=2r\cos(\theta+2\pi/3),\quad
z-m=2r\cos(\theta+4\pi/3).
\]
Therefore
\[
(x-m)(y-m)(z-m)=2r^3\cos3\theta.
\]
Since \(e_1,e_2\) are already fixed, maximizing or minimizing \(xyz=e_3\) is equivalent to maximizing or minimizing this product.

The maximum occurs exactly at permutations of
\[
(x,y,z)=(m+2r,m-r,m-r)
       =m(1+2t,1-t,1-t).
\tag{2}
\]
For \(t<1/2\), the minimum occurs exactly at permutations of
\[
(x,y,z)=(m-2r,m+r,m+r)
       =m(1-2t,1+t,1+t).
\tag{3}
\]
When \(t\ge1/2\), the closed constraint circle meets the boundary of the positive octant, where one of \(x,y,z\) is zero. Thus the infimum of any positive product that vanishes at that boundary is zero. The intersection begins exactly at \(t=1/2\), i.e. \(X=1/8\).

Converting (2) and (3) back through \(a=s-x\), \(b=s-y\), \(c=s-z\) gives (E+) and (E-).

### Hyperbolic and spherical area

The hyperbolic and spherical Heron-L'Huilier formulas are
\[
\tan^2\frac A4
=
\phi_\kappa(s)\phi_\kappa(x)\phi_\kappa(y)\phi_\kappa(z),
\tag{4}
\]
with
\[
\phi_H(u)=\tanh\frac u2,\qquad
\phi_S(u)=\tan\frac u2.
\]
For spherical minor-arc triangles \(s<\pi\), so all arguments lie in the positive domain of \(\tan(u/2)\).

Now define \(f_\kappa=\log\phi_\kappa\). Direct differentiation gives
\[
f_H'(u)=\frac1{\sinh u},\qquad
f_H'''(u)=\frac{1+\cosh^2u}{\sinh^3u}>0,
\]
and
\[
f_S'(u)=\frac1{\sin u},\qquad
f_S'''(u)=\frac{1+\cos^2u}{\sin^3u}>0.
\]
The moment lemma therefore shows that
\[
\phi_\kappa(x)\phi_\kappa(y)\phi_\kappa(z)
\]
is strictly increasing in \(xyz\) along every fixed-\((p,D)\) slice. Combining this with (2)-(4) proves all upper and lower bounds and their equality cases. The phase transition follows from the first contact of the fixed-moment circle with \(xyz=0\).

For \(t<1/2\), the feasible fixed-moment set is a circle inside the positive octant, so continuity gives every value between the two extrema. For \(t\ge1/2\), each positive component has boundary value \(0\) and contains the unique upper isosceles extremizer up to permutation, so every positive value below the maximum is likewise attained.

## Relation to prior literature

Svrtan and Veljan developed spherical and hyperbolic counterparts of classical triangle inequalities, including non-Euclidean Finsler-Hadwiger inequalities and isoperimetric inequalities. Their discussion explicitly notes the difficulty of finding the right non-Euclidean analogue needed to sharpen their two-dimensional isoperimetric chain.

For Euclidean triangles, Beniamin Bogosel subsequently determined the complete sharp relationship among area, perimeter squared, and
\[
D=(a-b)^2+(b-c)^2+(c-a)^2.
\]
With
\[
X=D/p^2,\qquad t=\sqrt{2X},
\]
the Euclidean specialization of the argument above reproduces the two boundary functions in that work:
\[
1-6X\pm4\sqrt2\,X^{3/2}.
\]
Accordingly, no originality is claimed here for the Euclidean fixed-\((p,D)\) profile. The contribution claimed here is the exact spherical and hyperbolic analogue: the complete sharp area interval for every admissible \((p,D)\), the two explicit isosceles boundary families, and the same \(X=1/8\) lower-bound phase transition transported through the non-Euclidean Heron-L'Huilier formulas.

Searches using Finsler-Hadwiger, non-Euclidean Finsler-Hadwiger, spherical/hyperbolic triangle area, fixed perimeter, side deficit, side variance, sum of squared side differences, and equivalent formulations did not locate these exact non-Euclidean profiles. This originality assessment is to the best of our knowledge.

## Limitations

- The spherical statement is restricted to geodesically convex minor-arc triangles with perimeter \(p<2\pi\). Other conventions for large spherical triangles are not treated.
- The stated formulas use unit curvature. Other constant curvatures follow by scaling.
- The result is a complete profile for the specific side deficit \(D=(a-b)^2+(b-c)^2+(c-a)^2\); it does not optimize other measures of triangle asymmetry.
- Originality is to the best of our knowledge. The main residual risk is an equivalent formulation in older non-Euclidean triangle-inequality literature under different transformed side variables.
- The Euclidean specialization is known and is included only as a consistency check and limiting case.

## References

1. D. Svrtan and D. Veljan, *Non-Euclidean versions of some classical triangle inequalities*, Forum Geometricorum **12** (2012), 197-209. http://forumgeom.fau.edu/FG2012volume12/FG201217.pdf
2. B. Bogosel, *Optimal Finsler-Hadwiger Inequalities*, Results in Mathematics **80** (2025), Article 88. https://doi.org/10.1007/s00025-025-02405-6
3. D. V. Alekseevskij, E. B. Vinberg and A. S. Solodovnikov, *Geometry II: Spaces of Constant Curvature*, Encyclopaedia of Mathematical Sciences 29, Springer, 1993. The standard spherical and hyperbolic Heron-L'Huilier formulas are used in (4).
