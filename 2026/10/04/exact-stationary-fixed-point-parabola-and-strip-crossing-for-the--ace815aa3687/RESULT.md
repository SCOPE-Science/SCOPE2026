# Exact stationary fixed-point parabola and strip crossing for the Hénon map
## Finding
Consider the dissipative Hénon map
\[
H_{a,b}(x,y)
=
(1-a x^2+y,bx),
\qquad
 a>0,
\qquad
0<b<1.
\]
Let \(\mu\) be any compactly supported invariant Borel probability measure.

The two fixed points have \(x\)-coordinates \(r_-<r_+\), where
\[
a r^2+(1-b)r-1=0.
\]
Write
\[
m=\mathbb E_\mu[x].
\]
Then the entire first-two-moment geometry of the first coordinate lies on the exact parabola
\[
\operatorname{Var}_\mu(x)
=
(r_+-m)(m-r_-).
\]
In particular,
\[
r_-\le m\le r_+.
\]
The left endpoint is attained only by the fixed-point atom at \((r_-,br_-)\), and the right endpoint only by the fixed-point atom at \((r_+,br_+)\).

The second-coordinate marginal is exactly a scaled copy of the first-coordinate marginal:
\[
(y)_\#\mu
=
(bx)_\#\mu.
\]
Consequently, for every continuous one-variable observable \(\phi\),
\[
\mathbb E_\mu[\phi(y)]
=
\mathbb E_\mu[\phi(bx)],
\]
and in particular
\[
\mathbb E_\mu[y]=bm,
\qquad
\operatorname{Var}_\mu(y)=b^2\operatorname{Var}_\mu(x).
\]

There is also an exact fixed-point polynomial balance
\[
\mathbb E_\mu\!
\left[
a(x-r_-)(x-r_+)\right]
=0.
\]
Since this polynomial is negative exactly for
\[
r_-<x<r_+
\]
and positive exactly for
\[
x<r_-
\quad\text{or}\quad
x>r_+,
\]
every invariant measure that is not supported on the two fixed points must place positive mass on both sign regions. Equivalently, every genuinely non-fixed recurrent statistical state crosses the fixed-point vertical strip in the measure-theoretic sense:
\[
\mu\{r_-<x<r_+\}>0
\]
and
\[
\mu\{x<r_-\text{ or }x>r_+\}>0.
\]

For the classical parameters
\[
a=\frac75,
\qquad
b=\frac3{10},
\]
the fixed-point coordinates are
\[
r_\pm
=
\frac{-7\pm\sqrt{609}}{28},
\]
so numerically
\[
r_-\approx-1.1313544771,
\qquad
r_+\approx0.6313544771.
\]
Thus every non-equilibrium-mixture invariant measure for the classical Hénon map must spend positive stationary mass both between these two vertical lines and outside their interval.

## Assumptions and scope
The theorem assumes \(a>0\), \(0<b<1\), and compact support of the invariant probability measure. The positivity and strict upper bound on \(b\) are the classical dissipative orientation-reversing regime used in Hénon's construction and are also used in the equality classification for the strip balance.

Compact support is more than enough to guarantee the first and second moments used in the proof. The same moment identity remains valid for any invariant probability measure for which the required moments are finite, but that broader integrability formulation is not claimed here.

The result concerns all compact invariant probability measures: fixed-point atoms, their convex mixtures, periodic-orbit measures, and chaotic invariant measures are all included.

The earliest verified public-source date used for the model is 1 February 1976. A Crossref-derived bibliographic record gives the issue month as February 1976, while a separate bibliographic record explicitly gives 1 February 1976.

## Proof
Invariance means
\[
\int f\circ H_{a,b}\,d\mu
=
\int f\,d\mu
\]
for every continuous \(f\) on the compact support.

Apply this first to the coordinate function \(y\). Since
\[
y\circ H_{a,b}=bx,
\]
we obtain the stronger marginal identity
\[
(y)_\#\mu=(bx)_\#\mu.
\]
Hence
\[
\mathbb E[y]=b\mathbb E[x]=bm.
\]

Now apply invariance to the coordinate function \(x\). Since
\[
x\circ H_{a,b}=1-a x^2+y,
\]
we get
\[
m
=
1-a\mathbb E[x^2]+bm.
\]
Therefore
\[
a\mathbb E[x^2]+(1-b)m-1=0.
\]
Let \(r_-<r_+\) be the two roots of
\[
a r^2+(1-b)r-1=0.
\]
By Vieta's formulas,
\[
r_-+r_+
=-\frac{1-b}{a},
\qquad
r_-r_+
=-\frac1a.
\]
Consequently,
\[
\begin{aligned}
(r_+-m)(m-r_-)
&=-m^2+(r_-+r_+)m-r_-r_+\\
&=-m^2-\frac{1-b}{a}m+\frac1a\\
&=\mathbb E[x^2]-m^2\\
&=\operatorname{Var}(x).
\end{aligned}
\]
This proves the variance parabola. Nonnegativity of variance gives
\[
r_-\le m\le r_+.
\]
If \(m=r_-\) or \(m=r_+\), the variance vanishes, so \(x\) is constant almost surely. Invariance of the first coordinate then forces \(y\) to be constant, and invariance of the second coordinate forces \(y=bx\). Hence the measure is the corresponding fixed-point atom.

The same stationary equation can be written as
\[
\mathbb E\!
\left[
a x^2+(1-b)x-1\right]
=0,
\]
which factors as
\[
\mathbb E\!
\left[
a(x-r_-)(x-r_+)\right]
=0.
\]

It remains to classify the pointwise-zero case. Suppose
\[
a(x-r_-)(x-r_+)=0
\]
throughout the support. Then every support point has \(x\in\{r_-,r_+\}\). Since \(b>0\), the inverse map exists and the previous \(x\)-coordinate of a support point is \(y/b\); support invariance therefore gives a previous coordinate \(x_-\in\{r_-,r_+\}\). For a root \(x\), the fixed-point polynomial gives
\[
1-a x^2=(1-b)x.
\]
Thus the next first coordinate is
\[
x_+=(1-b)x+b x_-.
\]
Because \(0<b<1\), if \(x_-\ne x\) this is a strict convex combination of \(r_-\) and \(r_+\), hence lies strictly between them, contradicting the support assumption. Therefore \(x_-=x\), so \(y=bx\), and the point is one of the two fixed points. Hence pointwise vanishing of the fixed-point polynomial is equivalent to support on the two fixed points.

For any invariant measure not supported on those fixed points, the continuous polynomial
\[
q(x)=a(x-r_-)(x-r_+)
\]
is therefore nonzero on a set of positive measure. Since
\[
\mathbb E[q(x)]=0,
\]
it must assume both signs on sets of positive measure. Its negative set is exactly the open fixed-point strip and its positive set is exactly the exterior, proving the strip-crossing claim.

Finally, the marginal identity gives
\[
\operatorname{Var}(y)=b^2\operatorname{Var}(x).
\]

## Verification
The accompanying checker uses only exact rational arithmetic and a small exact quadratic-extension class for the classical radical \(\sqrt{609}\).

It verifies the general cleared stationary identity
\[
a\bigl(\mathbb E[x^2]-m^2\bigr)
=
1-(1-b)m-a m^2
\]
modulo
\[
a\mathbb E[x^2]+(1-b)m-1=0.
\]
It also verifies exactly, for
\[
a=\frac75,
\qquad
b=\frac3{10},
\]
that
\[
r_\pm=\frac{-7\pm\sqrt{609}}{28}
\]
are the two roots of the fixed-point polynomial, have the correct Vieta sum and product, and give fixed points \((r_\pm,br_\pm)\).

The stored checker output is `VERIFY_OK`.

The sign-crossing and support-rigidity steps are analytic arguments using invariance and the strict convex-combination property for \(0<b<1\); they are not inferred from finite orbit sampling.

## Relationship to prior work
Hénon's original paper defines exactly
\[
x_{n+1}=1-a x_n^2+y_n,
\qquad
y_{n+1}=b x_n,
\]
identifies the constant Jacobian \(-b\), gives the inverse map, computes the two invariant points, and constructs a trapping region for the classical parameter pair. Its focus is the existence and geometry of a simple strange attractor, supported by extensive numerical iteration. The complete article was inspected; it does not formulate invariant probability measures or the mean-variance parabola above.

Benedicks and Carleson's 1991 work gives the foundational rigorous analysis of Hénon dynamics, while Benedicks and Young's 1993 paper constructs Sinai–Bowen–Ruelle invariant measures for certain Hénon maps. These works make invariant measures central to the subject but do not, in the inspected bibliographic material, expose the elementary fixed-point moment identity assessed here.

A full open preprint by Senti and Takahasi studies the entire space of invariant Borel probability measures for strongly dissipative Hénon maps at the first bifurcation and develops thermodynamic formalism for geometric potentials. Its model definition, invariant-measure setup, main theorem, introduction, and paper structure were inspected, together with document-wide searches for moment and average terminology. No first-coordinate moment parabola, fixed-point polynomial balance, or strip-crossing theorem was located.

Targeted searches for equivalent formulations included invariant-measure moments, time averages of \(x^2\), fixed-point variance formulas, periodic-orbit averages, and polynomial-observable identities. No same-object source was found that implies the complete statement above. The closest indexed published comparison found during the search was an analogous variance-gap law for the continuous-time Rössler system, which is a different vector field and does not imply the Hénon result.

## Limitations
The theorem is deliberately restricted to \(0<b<1\). The first-moment identity itself is more general, but the proof that pointwise vanishing of the fixed-point polynomial forces equilibrium support uses the strict convex-combination property of this parameter range.

The result does not identify a physical or Sinai–Bowen–Ruelle measure, prove uniqueness of an attractor, estimate entropy, or determine Lyapunov exponents. It is a universal constraint on whatever compact invariant probability measures exist.

The straddling conclusion is measure-theoretic. It asserts positive stationary mass on both sides of the fixed-point polynomial's sign partition; it does not assert continuous-time crossing between the corresponding vertical lines.

The basic expectation calculation is short. The novelty and value claim is therefore restricted to the exact fixed-point variance parabola together with its equality classification and the resulting all-invariant-measures strip-crossing consequence. A differently phrased observation in older numerical or periodic-orbit literature could remain unlocated.

## References
1. M. Hénon, “A Two-dimensional Mapping with a Strange Attractor,” Communications in Mathematical Physics 50, 69–77 (1976), DOI 10.1007/BF01608556.
2. M. Benedicks and L. Carleson, “The Dynamics of the Hénon Map,” Annals of Mathematics 133, 73–169 (1991), DOI 10.2307/2944326.
3. M. Benedicks and L.-S. Young, “Sinai–Bowen–Ruelle Measures for Certain Hénon Maps,” Inventiones Mathematicae 112, 541–576 (1993), DOI 10.1007/BF01232446.
4. S. Senti and H. Takahasi, “Equilibrium Measures for the Hénon Map at the First Bifurcation,” Nonlinearity 26, 1719–1741 (2013), arXiv:1110.0601.
5. S. Senti and H. Takahasi, “Equilibrium Measures for the Hénon Map at the First Bifurcation: Uniqueness and Geometric/Statistical Properties,” Ergodic Theory and Dynamical Systems 36, 215–255 (2016), DOI 10.1017/etds.2014.61.
