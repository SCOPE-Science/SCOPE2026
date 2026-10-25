# A sharp three-wall caustic phase diagram for the first two constant-width harmonics

## Finding

Consider the real-analytic plane oval with support function
\[
h(\theta)=R+a\cos(3\theta)+b\cos(5\theta),\qquad R>8|a|+24|b|,\quad (a,b)\ne(0,0).
\]
The condition makes the oval strictly convex and its width constantly \(2R\). The Fourier orders \(3\) and \(5\) are the first two nontranslation odd modes compatible with constant width.

Let \(W\) be the Wigner caustic (midpoints of antipodally normal boundary contacts) and \(S\) their centre symmetry set (envelope of the joining chords). Count ordinary cusps by their distinct normal-angle parameters modulo \(\pi\). Whenever \(a\ne0\), write \(t=b/a\). Away from the three exceptional ratios \(-1/3,-3/25,1/5\), **the exact simultaneous cusp counts** are

| Ratio | Wigner cusps | Centre-symmetry cusps |
|---|---:|---:|
| \(t<-1/3\) | 5 | 5 |
| \(-1/3<t<-3/25\) | 3 | 5 |
| \(-3/25<t<1/5\) | 3 | 3 |
| \(t>1/5\) | 5 | 5 |

When \(a=0\) and \(b\ne0\), both counts are five. When \(b=0\) and \(a\ne0\), both counts are three. The three walls are sharp and attainable within the strictly convex family.

At \(t=-1/3\), a Wigner stationary parameter at \(\theta=0\) has zero velocity of exact order two (a \(4/3\)-type cusp); the remaining Wigner singularities are ordinary and all five centre-symmetry cusps are ordinary. At \(t=-3/25\), the centre symmetry set has a zero of velocity of exact order three at \(\theta=0\) (a \(5/4\)-type cusp); all Wigner cusps are ordinary. At \(t=1/5\), the parameter \(\theta=\pi/2\) has Wigner velocity zero of exact order three and centre-symmetry velocity zero of exact order two, corresponding respectively to \(5/4\)- and \(4/3\)-type cusps. These types refer to parametric germs, not a claim of distinct spatial images at self-intersections.

A concrete invariant-matching consequence is that the two ovals
\[
h_{\pm}(\theta)=1+\frac{\cos(3\theta)}{100}\pm\frac{\cos(5\theta)}{400}
\]
have the same constant width \(2\), perimeter \(2\pi\), area \(39981\pi/40000\), oriented Wigner area \(-19\pi/80000\), and oriented centre-symmetry area \(-219\pi/80000\), yet their Wigner caustics have respectively five and three ordinary cusps. Their centre-symmetry sets both have five ordinary cusps. Thus these four scalar measures do not determine Wigner cusp topology even among strictly convex analytic constant-width ovals with the two lowest nontrivial odd Fourier modes.

## Assumptions and scope

The support function is taken with outward normal \(n(\theta)=(\cos\theta,\sin\theta)\), counterclockwise tangent \(\tau(\theta)=(-\sin\theta,\cos\theta)\), and contact point \(x(\theta)=h(\theta)n(\theta)+h'(\theta)\tau(\theta)\). All angles are real modulo \(2\pi\); caustics have period \(\pi\). Count cusps as singular *parameter occurrences* of the natural antipodal-pair parametrizations. Oriented areas are counted once over a half-turn and may be negative because the caustics need not be embedded. The sufficient strict-convexity hypothesis is not claimed necessary.

## Proof

Write \(p(\theta)=a\cos(3\theta)+b\cos(5\theta)\), and put
\[
D(\theta)=p(\theta)+p''(\theta)=-8a\cos(3\theta)-24b\cos(5\theta).
\]
Because \(p(\theta+\pi)=-p(\theta)\) and likewise for its derivative, the two antipodally normal points are \(x(\theta)=w(\theta)+Rn(\theta)\) and \(x(\theta+\pi)=w(\theta)-Rn(\theta)\), where
\[
w(\theta)=p(\theta)n(\theta)+p'(\theta)\tau(\theta),\qquad w'(\theta)=D(\theta)\tau(\theta).
\]
Thus \(w\) parameterizes the Wigner caustic. The parallel-pair chord line is \(w(\theta)+s n(\theta)\). An envelope point must have derivative in the direction of \(n\), so \(D+s=0\). Hence
\[
S(\theta)=w(\theta)-D(\theta)n(\theta),\qquad S'(\theta)=-D'(\theta)n(\theta).
\]
The normal and tangent both rotate with nonzero unit angular speed. If the scalar velocity has a zero of order \(k=1,2,3\), direct integration of its Taylor series gives a plane germ with initial independent components of orders \(k+1\) and \(k+2\), respectively. For \(k=1\) this is the ordinary \(3/2\)-cusp, and \(k=2,3\) give the named higher types.

Assume \(a\ne0\) and set \(t=b/a\), \(y=\cos^2\theta\). Elementary multiple-angle identities give
\[
D(\theta)=-8a\cos\theta\,Q_W(y),\quad D'(\theta)=24a\sin\theta\,Q_S(y),
\]
where
\[
Q_W(y)=4y-3+3t(16y^2-20y+5),\qquad
Q_S(y)=4y-1+5t(16y^2-12y+1).
\]
Their discriminants, as quadratic polynomials in \(y\), are
\[
16(45t^2+6t+1)>0,\qquad16(125t^2-10t+1)>0.
\]
The endpoint values are
\[
\begin{aligned}
Q_W(0)&=15t-3,&Q_W(1)&=3t+1,\\
Q_S(0)&=5t-1,&Q_S(1)&=25t+3.
\end{aligned}
\]
A zero \(y\in(0,1)\) gives two distinct normal parameters modulo \(\pi\). The factor \(\cos\theta\) contributes one Wigner singular parameter at \(\theta=\pi/2\), and \(\sin\theta\) contributes one centre-symmetry singular parameter at \(\theta=0\). Distinct interior roots cannot collide because the discriminants are positive. They can enter or exit \((0,1)\) only at the displayed endpoint walls; the leading quadratic coefficient may vanish at \(t=0\), but its finite interior root persists and no root arrives from infinity. At \(t=-1,0,1\), direct evaluation gives, respectively, two, one and two interior roots for each quadratic, with the centre-symmetry wall at \(-3/25\) dividing the negative and central regions. This proves the table and all generic simplicity assertions. The case \(a=0\) reduces directly to \(\cos(5\theta)\) and \(\sin(5\theta)\).

At the three endpoint ratios, Taylor expansions (or derivatives of the displayed factors) give exact orders: at \(t=-1/3\), \(\cos(3\theta)+3t\cos(5\theta)\) has a quadratic zero at \(\theta=0\); at \(t=-3/25\), \(\sin(3\theta)+5t\sin(5\theta)\) has a cubic zero at \(\theta=0\); at \(t=1/5\), the former has a cubic and the latter a quadratic zero at \(\theta=\pi/2\). Other roots are simple by the discriminant and endpoint analysis.

For any closed smooth oval, \(A=\tfrac12\int_0^{2\pi}(h^2-(h')^2)\,d\theta\). Fourier orthogonality yields
\[
A=\pi R^2-4\pi a^2-12\pi b^2.
\]
Applying the signed area integral \(\tfrac12\int_0^\pi\det(z,z')\,d\theta\) to \(z=w\) and \(z=S\), again separating Fourier frequencies, gives
\[
A_W^*=-2\pi a^2-6\pi b^2,\qquad A_S^*=-18\pi a^2-150\pi b^2.
\]
The values are unchanged by reversing the sign of \(b\). For \(R=1,a=1/100,b=\pm1/400\), the curvature radius is bounded below by \(1-8/100-24/400>0\), hence both curves are strictly convex; substitution yields the displayed exact invariant values and cusp-count contrast. This completes the proof.

## Verification

Run `python verify.py` with SymPy installed. It checks both caustic derivative identities, exact polynomial discriminants and endpoint values, signed-area coefficients, sample cusp counts on both sides of every wall, and the zero orders at the exceptional ratios. Its finite list of sample parameters is not offered as proof of the continuum phase diagram; that step follows from the discriminant and endpoint argument above.

## Relationship to prior work

The fundamental local Wigner and centre-symmetry cusp criteria and their order-lowering relation occur in M. Zwierzyński, *Singularities of the Wigner Caustic and the Centre Symmetry Set of Frontal Curves in the Euclidean Plane*, arXiv:2609.14653 (2026), Theorems 3.3, 3.9 and 4.1. These do not state the joint \(3\)/\(5\) harmonic global phase diagram or the matched-invariants counterpair. The oriented Wigner-area and constant-width isoperimetric framework is developed in M. Zwierzyński, *Mixed Volumes, the Wigner Caustic, and Isoperimetric Inequalities*, arXiv:2608.11068 (2026), especially §7. Its Fourier area formulas imply the relevant scalar area expression but not the cusp-count separation. The general inequality that the number of ordinary centre-symmetry cusps is at least that of Wigner cusps is from W. Domitrz and P. de M. Rios (2014), Theorem 7.2; the present table makes both equality and a strict two-cusp gap explicit within the lowest two odd support modes.

## Limitations

The assertions apply only to the aligned real cosine modes and the stated strict-convexity domain; arbitrary phases, higher Fourier modes, or nonconvex frontals are not classified. The area formulas are specializations of standard support-function identities, not independent new general inequalities. Counts refer to naturally parametrized branches and are not a classification of all spatial self-intersections. The literature comparisons cannot exclude every unpublished or unindexed prior specialization. No independent audit has been performed.

## References

1. M. Zwierzyński, *Singularities of the Wigner Caustic and the Centre Symmetry Set of Frontal Curves in the Euclidean Plane*, arXiv:2609.14653, first posted 2026-09-13, https://arxiv.org/abs/2609.14653.
2. M. Zwierzyński, *Mixed Volumes, the Wigner Caustic, and Isoperimetric Inequalities*, arXiv:2608.11068, first posted 2026-08-11, https://arxiv.org/abs/2608.11068.
3. W. Domitrz and P. de M. Rios, *Singularities of equidistants and global centre symmetry sets of Lagrangian submanifolds*, Geom. Dedicata 169 (2014), 361–382, https://doi.org/10.1007/s10711-013-9861-2.
