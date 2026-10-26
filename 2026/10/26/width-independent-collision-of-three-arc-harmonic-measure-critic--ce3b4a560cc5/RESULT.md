# Width-independent collision of three-arc harmonic-measure critical points

## Finding
Let \(\mathbb D=\{z:|z|<1\}\), \(0<\beta<\pi/3\), and \(2\beta<\alpha<\pi-\beta\). On the unit circle, let \(E\) be the union of the three disjoint arcs of angular half-width \(\beta\) centered at angles \(0\), \(\alpha\), and \(-\alpha\). Let \(u(z)=\omega(z,E;\mathbb D)\), the harmonic solution of the Dirichlet problem with boundary values \(1_E\) (away from endpoints). A critical point is a zero of \(\nabla u\), counted by the multiplicity of the zero of its holomorphic complex derivative.

**Theorem.** There are exactly two critical points counted with multiplicity in \(\mathbb D\), with a unique collision parameter independent of \(\beta\):

1. When \(2\beta<\alpha<2\pi/3\), there are precisely two distinct simple critical points, forming a nonreal conjugate pair with positive real parts.
2. When \(\alpha=2\pi/3\), the origin is the unique critical point, of multiplicity exactly two.
3. When \(2\pi/3<\alpha<\pi-\beta\), there are precisely two distinct simple critical points, both real: one negative and one positive.

For fixed \(\beta\), put \(\delta=\alpha-2\pi/3\) and \(c_\beta=1/(3^{1/4}\sqrt{4\cos^2\beta-1})\). The two critical points satisfy, as \(\delta\to0\),
\[
 z_\pm=\begin{cases}\pm c_\beta\sqrt\delta+O_\beta(\delta),&\delta>0,\\
 \pm i c_\beta\sqrt{-\delta}+O_\beta(-\delta),&\delta<0.\end{cases}
\]
At the collision the harmonic function has a nonzero cubic leading term; away from it the critical points are ordinary quadratic saddles.

## Assumptions and scope
The three arcs are open; endpoint values of the boundary indicator do not affect the Poisson integral. The condition \(2\beta<\alpha<\pi-\beta\) ensures the arcs do not intersect. Since \(\beta<\pi/3\), the symmetric separation \(2\pi/3\) is strictly within this interval. A multiplicity-two critical point refers to a double zero of the analytic derivative, not two distinct points. The theorem concerns interior critical points, not extrema of the boundary function.

## Proof
Write \(b=\cos\beta\), \(x=\cos\alpha\), \(a=1+2x\), and \(B=12b^2+4x^2+4x-2\). The Fourier coefficients of the indicator of a centered arc are \(\sin(n\beta)/(\pi n)\); after forming the holomorphic completion \(g\) with \(\Re g=u\), differentiation and summation of the elementary trigonometric generating series give
\[
 g'(z)=\frac{2\sin\beta}{\pi}\sum_{\theta\in\{0,\alpha,-\alpha\}}
 \frac{e^{i\theta}}{1-2be^{i\theta}z+e^{2i\theta}z^2}.
\]
All denominator zeros lie on \(\partial\mathbb D\). Multiplying the three denominators and collecting terms yields the *exact* reciprocal polynomial numerator
\[
 N(z)=a(z^4+1)-4ba(z^3+z)+Bz^2.
\]
(The positive constant factor \(2\sin\beta/\pi\) has no effect on critical points.) Hence for \(z\ne0\), with \(t=z+z^{-1}\), the critical-point equation is \(Q(t)=0\), where
\[
 Q(t)=a t^2-4ba t+4(3b^2+x^2-1),\qquad
 \operatorname{disc}Q=16a(1-x)(1+x-2b^2).
\]
The strict separation \(\alpha>2\beta\) implies \(x<\cos(2\beta)=2b^2-1\); thus \(1+x-2b^2<0\). Moreover \(1-x>0\). Also
\[
 Q(2)=4(x-b)(x+2-3b)>0,\qquad
 Q(-2)=4(x+b)(x+2+3b)>0.
\]
To justify the first strict sign: \(x-b<0\) and \(x+2-3b<2b^2+1-3b=(2b-1)(b-1)<0\), since \(1/2<b<1\). For the second, \(\alpha<\pi-\beta\) gives \(x>-b\), and \(x+2+3b>0\).

If \(a>0\), equivalently \(\alpha<2\pi/3\), the discriminant is negative. Thus \(Q\) has two distinct nonreal conjugate zeros \(t,\overline t\). For every nonreal \(t\), the reciprocal quadratic \(z^2-tz+1=0\) has exactly one root in \(\mathbb D\) (neither root is on the unit circle and their product is \(1\)). The two interior roots are nonreal conjugates. Since \(\Re t=2b>0\) and \(\Re(z+z^{-1})=\Re z(1+|z|^{-2})\), both have positive real part and are simple.

If \(a<0\), equivalently \(\alpha>2\pi/3\), the discriminant is positive; the graph of \(Q\) is a downward parabola, and its strictly positive values at \(t=\pm2\) force its two real zeros to lie strictly in \(( -\infty,-2)\) and \((2,\infty)\). Each reciprocal quadratic therefore has one distinct simple root inside \((-1,0)\) or \((0,1)\), respectively. There are no other roots in \(\mathbb D\).

If \(a=0\), then \(x=-1/2\) and \(N(z)=3(4b^2-1)z^2\), with strictly positive coefficient, so the origin is precisely a double critical point. For the local expansion, \(a=-\sqrt3\,\delta+O(\delta^2)\), while the coefficient of \(z^2\) at \(\delta=0\) is \(3(4b^2-1)\). Substituting \(z=O(\sqrt{|\delta|})\) in \(N\) gives \(z^2=\delta/[\sqrt3(4b^2-1)]+O(|\delta|^{3/2})\), which proves the stated two-sided square-root splitting. Since \(g'\) has exactly a double zero at the collision, the first nonconstant term in \(u=\Re g\) is the real part of a nonzero multiple of \(z^3\). At simple zeros, the leading nonconstant term is quadratic, giving ordinary harmonic saddles.

## Verification
The accompanying `verify_three_arc.py` symbolically reconstructs all five numerator coefficients from the three rational summands. It computes the interior roots at parameter pairs on both sides of and at the collision and substitutes each root into the original rational derivative, testing residuals. These examples check algebraic normalization and selected parameter instances; the exhaustive classification for all admissible real \(\alpha,\beta\) follows from the above exact discriminant and sign argument, not from finite tests.

## Relationship to prior work
J. L. Walsh's 1947–1950 work explicitly studies the locations of critical points of harmonic measures and linear combinations of arc harmonic measures, providing the central classical context. The present result is a complete explicit zero count, localization and saddle-collision law for a three-equal-arc family, including the width-independent separation threshold; it does not claim priority for the complex-derivative representation or Walsh's general localization techniques. The abstract of Walsh's 1948 paper directly introduces arc harmonic-measure derivatives, so whether a theorem or worked example in the uninspected full text implies this classification is a material residual priority risk. Dubinin and Vuorinen's 2010 analysis treats harmonic-measure extremal decompositions rather than critical point bifurcations.

## Limitations
The conclusions require three equal-width disjoint arcs centered at a reflection-symmetric triple and do not cover unequal widths, more arcs or multiply connected domains. They concern planar interior critical points, not the global geometry of critical level sets. The 1948 Walsh article and the substantial relevant chapters of his 1950 monograph were not inspected in full; an equivalent earlier special case cannot be ruled out without those texts. Independent mathematical and historical validation has not been performed.

## References
- J. L. Walsh, *On the Location of the Critical Points of Harmonic Measure*, Proceedings of the National Academy of Sciences 33 (1947), 18–20, doi:10.1073/pnas.33.1.18.
- J. L. Walsh, *The Critical Points of Linear Combinations of Harmonic Functions*, Bulletin of the American Mathematical Society 54 (1948), 196–205, doi:10.1090/S0002-9904-1948-08984-4.
- J. L. Walsh, *The Location of Critical Points of Analytic and Harmonic Functions*, AMS Colloquium Publications 34 (1950), doi:10.1090/coll/034.
- V. N. Dubinin and M. Vuorinen, *An Extremal Decomposition Problem for Harmonic Measure*, arXiv:1011.4178, first version publicly submitted 2010-11-18.
- P. W. Jones and D. E. Marshall, *Critical Points of Green's Function, Harmonic Measure, and the Corona Problem*, Arkiv för Matematik 23 (1985), 281–314.
