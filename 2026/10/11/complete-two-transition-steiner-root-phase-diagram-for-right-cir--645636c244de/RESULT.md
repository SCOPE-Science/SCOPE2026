# Complete two-transition Steiner-root phase diagram for right circular cones
## Finding
Let \(K_{r,h}\subset\mathbb R^3\) be a right circular cone with base radius \(r>0\) and height \(h>0\). Put
\[
t=\frac hr.
\]
Similarity shows that the algebraic type of the roots of the Steiner polynomial depends only on \(t\).

Define
\[
m(t)=\pi+t-\arctan t,
\qquad
s(t)=1+\sqrt{1+t^2},
\]
and
\[
q(t)=\sqrt{m(t)^2-4s(t)}.
\]
For \(t>0\), one has \(q(t)>0\). Set
\[
\Psi_\pm(t)
=
m(t)^3-6m(t)s(t)+8t\pm q(t)^3.
\]

There are exactly two transition aspect ratios. Let \(t_2\) be the unique positive zero of \(\Psi_+\), and let \(t_1\) be the unique positive zero of \(\Psi_-\). They satisfy
\[
1<t_2<\sqrt3
<
\tan\!\left(\frac{2\pi}{5}\right)
<t_1<
\tan\!\left(\frac{5\pi}{12}\right),
\]
and numerically
\[
t_2=1.15239395234821\ldots,
\qquad
t_1=3.37108436208809\ldots.
\]

The complete root-type phase diagram is:
\[
\begin{array}{c|c}
\text{aspect ratio }t & \text{Steiner-root type}\\ \hline
0<t<t_2 & \text{complex roots of Type 2}\\
t=t_2 & \text{double real root of Type 2}\\
t_2<t<t_1 & \text{three distinct real roots}\\
t=t_1 & \text{double real root of Type 1}\\
t>t_1 & \text{complex roots of Type 1}.
\end{array}
\]

Thus a right circular cone passes through every non-ball root regime exactly once as its height-to-radius ratio increases.

## Assumptions and scope
The Steiner polynomial of a three-dimensional convex body \(K\) is
\[
f_K(\lambda)
=
V(K)+S(K)\lambda+M(K)\lambda^2+\frac{4\pi}{3}\lambda^3,
\]
where \(V\), \(S\), and \(M\) denote volume, surface area, and integral mean curvature.

The terminology Type 1 and Type 2 is the standard one used in the cited three-dimensional Steiner-root classification. If
\[
\phi_\pm(K)
=
M(K)^3-6\pi\bigl(M(K)S(K)-4\pi V(K)\bigr)
\pm
\bigl(M(K)^2-4\pi S(K)\bigr)^{3/2},
\]
then the classification states:
\[
\begin{aligned}
\phi_-(K)>0&\iff \text{complex roots of Type 1},\\
\phi_+(K)<0&\iff \text{complex roots of Type 2},\\
\phi_+(K)>0>\phi_-(K)&\iff \text{three distinct real roots},
\end{aligned}
\]
with \(\phi_-=0\) and \(\phi_+=0\) giving the Type 1 and Type 2 double-root boundaries, respectively.

The result concerns nondegenerate cones \(r>0\), \(h>0\). It classifies root type, not the exact locations of the three roots.

## Proof
By similarity, it is enough to set \(r=1\). The archive-era cone formulas are
\[
V(K_{1,t})=\frac\pi3t,
\qquad
S(K_{1,t})=\pi\bigl(1+\sqrt{1+t^2}\bigr),
\]
\[
M(K_{1,t})
=
\pi\bigl(\pi+t-\arctan t\bigr).
\]
Substitution into \(\phi_\pm\) gives
\[
\phi_\pm(K_{1,t})=\pi^3\Psi_\pm(t).
\]
The Minkowski inequality \(M^2\ge4\pi S\), with equality only for a ball, gives \(q(t)>0\) for every nondegenerate cone.

Put
\[
x(t)=\frac{t}{\sqrt{1+t^2}}.
\]
Then
\[
m'(t)=x(t)^2,
\qquad
s'(t)=x(t),
\]
and, since \(q^2=m^2-4s\),
\[
q'(t)=\frac{m(t)x(t)^2-2x(t)}{q(t)}.
\]
Writing
\[
A=m^3-6ms+8t,
\qquad
B=q^3,
\]
one finds
\[
A'
=
\frac32\bigl((mx)^2+(qx)^2\bigr)-6mx+8,
\]
and
\[
B'=3qx(mx-2).
\]
Therefore
\[
\boxed{
\Psi_\pm'(t)
=
2+rac32\bigl(x(t)(m(t)\pm q(t))-2\bigr)^2
}
\]
for every \(t>0\). In particular, both \(\Psi_+\) and \(\Psi_-\) are strictly increasing.

It remains only to certify one sign change for each function. Exact rational interval arithmetic using
\[
\frac{333}{106}<\pi<\frac{355}{113}
\]
and elementary rational enclosures of the required square roots gives
\[
-0.77780<\Psi_+(1)<-0.77139,
\]
\[
5.29383<\Psi_+(\sqrt3)<5.30290.
\]
Thus \(\Psi_+\) has exactly one zero \(t_2\) in \((1,\sqrt3)\).

For the other transition, use the exact special-angle identities
\[
\tan\!\left(\frac{2\pi}{5}\right)
=
\sqrt{5+2\sqrt5},
\qquad
\sec\!\left(\frac{2\pi}{5}\right)=1+\sqrt5,
\]
and
\[
\tan\!\left(\frac{5\pi}{12}\right)=2+\sqrt3,
\qquad
\sec\!\left(\frac{5\pi}{12}\right)=\sqrt6+\sqrt2.
\]
The same exact interval calculation gives
\[
-0.59867
<
\Psi_-\!\left(\tan\frac{2\pi}{5}\right)
<
-0.58213,
\]
\[
0.71591
<
\Psi_-\!\left(\tan\frac{5\pi}{12}\right)
<
0.73747.
\]
Hence \(\Psi_-\) has exactly one zero \(t_1\) in that interval. In particular,
\[
t_2<t_1.
\]

Finally,
\[
\Psi_+(t)-\Psi_-(t)=2q(t)^3>0.
\]
The three-dimensional root classification now gives the five regimes displayed in the finding. The decimal values of \(t_2\) and \(t_1\) are obtained by bisection and are not used to prove existence or uniqueness.

## Verification
The accompanying `verify.py` performs three independent checks from its packaged path.

First, symbolic exact arithmetic verifies the two identities
\[
\Psi_+'(t)
=
2+\frac32\bigl(x(m+q)-2\bigr)^2,
\]
\[
\Psi_-'(t)
=
2+\frac32\bigl(x(m-q)-2\bigr)^2.
\]

Second, a custom interval implementation based only on exact rational arithmetic certifies the four strict signs used in the proof. Square-root enclosures are produced by integer-square-root comparisons, so the sign test does not depend on floating-point evaluation.

Third, ordinary floating-point bisection reproduces the supplemental decimals
\[
t_2=1.152393952348211\ldots,
\qquad
t_1=3.371084362088092\ldots.
\]
Those decimals are not used as proof certificates.

## Relationship to prior work
Hernández Cifre and Saorín gave the general three-dimensional classification of Steiner polynomials by the signs of \(\phi_+\) and \(\phi_-\). Their 2007 paper materially treats several explicit families; its one-parameter circular example is the cylinder family, for which it states a single Type 2 transition. It does not contain a corresponding cone phase classification.

Saorín's 2008 thesis and the 2009 Banach Center paper then introduce the right circular cone family with
\[
V=\frac\pi3h,
\qquad
S=\pi(1+\sqrt{1+h^2}),
\qquad
M=\pi(\pi+h-\arctan h).
\]
They state that these cones can have real roots, complex roots of Type 1, or complex roots of Type 2. The thesis plots the family in the Blaschke diagram, and the 2009 paper records that cones with
\[
0\le h\lesssim3.37108
\]
are not in the Type 1 complex-root region. That upper transition is used there to exclude a range of cones from Hadwiger's class \(R_\beta\).

The present result supplies the missing all-parameter statement: both transition functionals are strictly increasing, the lower Type 2 boundary occurs uniquely at \(t_2=1.15239395234821\ldots\), the real-root window is exactly \((t_2,t_1)\), and the previously quoted \(3.37108\ldots\) value is the unique Type 1 boundary \(t_1\).

Targeted searches using the cone family, both transition decimals, the Type 1/Type 2 terminology, the functionals \(\phi_\pm\), and Steiner-root phase-diagram aliases did not locate a prior statement of this complete classification.

## Limitations
The theorem classifies only right circular cones under Euclidean Steiner parallelism. It does not classify oblique cones, truncated cones, or general tangential bodies.

The transition constants are characterized as unique zeros of explicit monotone transcendental functions; no elementary closed form is claimed.

The historical search was targeted. An equivalent phase classification under different notation may exist outside the indexed literature, although the most relevant primary full texts and the thesis cone example were materially inspected.

## References
1. E. Saorín Gómez, *On inner parallel bodies. From the Steiner polynomial to Poincaré inequality*, doctoral thesis, Universidad de Murcia, 2008; cone example in Chapter 2.
2. E. Saorín, *On Hadwiger's problem on inner parallel bodies*, Banach Center Publications 84 (2009), 121--129. DOI: 10.4064/bc84-0-8.
3. M. A. Hernández Cifre and E. Saorín, *On the roots of the Steiner polynomial of a 3-dimensional convex body*, Advances in Geometry 7 (2007), 275--294. DOI: 10.1515/ADVGEOM.2007.016.
