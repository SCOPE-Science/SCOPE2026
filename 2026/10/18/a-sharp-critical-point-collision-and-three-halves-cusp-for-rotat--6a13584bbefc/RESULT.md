# A sharp critical-point collision and three-halves cusp for rotationally lifted Blaschke products

## Finding
Fix a radius \(0<r<1\), an integer \(n\ge1\), and a real parameter \(-1<c<1\). Put \(c=\cos\theta\) with \(0<\theta<\pi\), and define the finite Blaschke product
\[
 B_{n,r,c}(z)=C_{r,c}(z^n),\qquad
 C_{r,c}(w)=\frac{w(w^2-2rcw+r^2)}{1-2rcw+r^2w^2}.
\]
Its zeros are the origin with multiplicity \(n\), and the two rotated regular \(n\)-gons obtained by solving \(z^n=re^{i\theta}\) and \(z^n=re^{-i\theta}\). Define the sharp angular threshold
\[
 c_*(r)=\frac{\sqrt{3+r^2}}{2},\qquad 0<r<1.
\]
Besides the origin, which is a critical point of multiplicity \(n-1\) when \(n>1\), the following is a complete critical-point classification in the open unit disk:

* For \(|c|>c_*(r)\), there are \(2n\) simple nonzero critical points. They are the inverse images under \(z\mapsto z^n\) of two distinct real points having the sign of \(c\).
* For \(|c|<c_*(r)\), there are \(2n\) simple nonzero critical points. Their two base points are a nonreal conjugate pair.
* For \(|c|=c_*(r)\), there are precisely \(n\) nonzero critical points, each of multiplicity two (local mapping degree three). Their base critical point is \(\operatorname{sgn}(c)t(r)\), where
\[
 t(r)=\frac{\sqrt{3+r^2}-\sqrt{3(1-r^2)}}{2r}\in(0,1).
\]

Away from the collision, the nonzero critical points give exactly two distinct nonzero critical values, each repeated at \(n\) points. On the collision locus these merge into one nonzero critical value, repeated at the \(n\) doubly critical points. The critical-value collision has a sharp three-halves law. More precisely, set \(c_0=c_*(r)\), \(t=t(r)\), \(D_0=1-2rc_0t+r^2t^2>0\), and
\[
 K(r)=\frac{32c_0(1-r^2)t^3}{3D_0^2}\sqrt{\frac{8c_0}{3}}>0.
\]
If \(v_+(c)\) and \(v_-(c)\) are the two nonzero critical values for \(c\ne c_0\), then, as \(c\to c_0\) on either side,
\[
 |v_+(c)-v_-(c)|=K(r)|c-c_0|^{3/2}+O_r(|c-c_0|^2).
\]
The corresponding law near \(c=-c_0\) has the same coefficient after changing \(c\) to \(-c\). In particular, the limiting ratio to \(|c-c_0|^{3/2}\) is positive and finite.

## Assumptions and scope
All critical points and multiplicities are over \(\mathbb C\) in the open disk; zeros are counted with analytic multiplicity. The parameters satisfy \(n\in\mathbb Z_{\ge1}\), \(0<r<1\), and \(-1<c<1\); the endpoints \(c=\pm1\), where two prescribed zeros coincide, are excluded. A local mapping degree of three means a zero of multiplicity two of \(B'\). The theorem treats this particular two-orbit zero configuration, not all finite Blaschke products or their iteration dynamics.

## Proof
**1. Reduction to a reciprocal quartic.** Write \(q=r^2\), \(U(w)=w^3-2rcw^2+qw\), and \(V(w)=1-2rcw+qw^2\). Direct differentiation gives
\[
 C_{r,c}'(w)=\frac{N(w)}{V(w)^2},\quad
 N(w)=q(w^4+1)-4rc(w^3+w)+(3+4qc^2-q^2)w^2.
\]
The denominator never vanishes in the closed unit disk because it factors as \((1-re^{i\theta}w)(1-re^{-i\theta}w)\). Since \(N(0)=q>0\), all critical points of \(C\) are nonzero. For \(w\ne0\), put \(u=w+w^{-1}\); then
\[
 w^{-2}N(w)=Q(u),\qquad
 Q(u)=q u^2-4rcu+3+4qc^2-q^2-2q.
\]
The discriminant of \(Q\) is
\[
 \operatorname{disc}Q=4q(1-q)\bigl(4c^2-3-q\bigr).
\]
Its two roots, with the usual complex square-root convention, are
\[
 u_\pm=\frac{2c\pm\sqrt{(1-q)(4c^2-3-q)}}{r}.
\]
Each \(u\notin[-2,2]\) yields precisely one solution \(w\) of \(w+w^{-1}=u\) inside the disk, the other lying outside. A finite Blaschke product has no boundary critical point: at each \(|\zeta|=1\), its angular derivative is a sum of strictly positive Poisson terms. Consequently neither \(u_+\) nor \(u_-\) can enter \([-2,2]\). The resulting two disk roots, counted with multiplicity, exhaust the critical points because \(C\) has degree three and hence exactly two critical points in the disk. For \(|c|<c_*\), the \(u\)-roots are nonreal conjugates, yielding conjugate nonreal disk roots. For \(|c|>c_*\), they are real, and continuity from \(|c|=c_*\) shows the disk roots are real and have the sign of \(c\).

**2. Sharp collision and multiplicities.** At \(c=c_0>0\), define \(u_0=2c_0/r>2\). The discriminant vanishes and
\[
 N(w)=q(w^2-u_0w+1)^2.
\]
The inner zero of \(w^2-u_0w+1\) is exactly \(t(r)\), so it is a double zero of \(C'\). At \(c=-c_0\), symmetry \(C_{r,-c}(-w)=-C_{r,c}(w)\) places the double critical point at \(-t(r)\). The chain rule
\[
 B_{n,r,c}'(z)=n z^{n-1} C_{r,c}'(z^n)
\]
then gives the stated \(n-1\) zero at the origin and lifts every nonzero simple (respectively double) base critical point to \(n\) simple (respectively double) critical points. Total ramification multiplicity is \(3n-1\), as required for degree \(3n\).

**3. Distinctness of the two critical values.** The three zeros of \(C\), namely \(0\) and \(re^{\pm i\theta}\), are distinct, so no critical value is zero: the derivative cannot vanish at a simple zero. If two distinct simple critical points of the cubic map had the same image, that fiber would have degree at least \(2+2=4\), contradicting the mapping degree three. Hence the two nonzero critical values are distinct off the threshold and coalesce only at the double point. The lift introduces no new nonzero critical values.

**4. The sharp three-halves cusp.** For \(c=c_0+\delta\), the quadratic formula for \(u_\pm\) and the inverse branch of \(w+w^{-1}\) yield the two disk critical points
\[
 w_\pm=t\pm k\sqrt\delta+O_r(\delta),\qquad
 k=t\sqrt{\frac{8c_0}{3}}>0.
\]
Here the square root is real for \(\delta>0\) and imaginary for \(\delta<0\); the labels may be interchanged. Let \(F(c,w)=C_{r,c}(w)\). At \((c_0,t)\), the derivatives satisfy
\[
 F_w=F_{ww}=0,\quad
 F_{wc}=-\frac{8c_0(1-q)t^2}{D_0^2},\quad
 F_{www}=\frac{6(1-q)}{D_0^2},\quad
 k^2=-\frac{2F_{wc}}{F_{www}}.
\]
A Taylor expansion at the double critical point gives, with a consistent labeling,
\[
 F(c,w_+)-F(c,w_-)
 =\frac43 F_{wc}k\,\delta^{3/2}+O_r(|\delta|^2).
\]
Taking absolute values yields the displayed positive coefficient \(K(r)=\frac43|F_{wc}|k\). The negative-threshold statement follows from the symmetry in step 2.

## Verification
The standalone file `checker.py` symbolically checks the exact derivative numerator, the reciprocal-quadratic reduction, the double-root derivative identities, and the chain rule for several lifts. It also compares numerically evaluated critical-value splittings with the claimed leading coefficient at several radii and both sides of the threshold. All checks completed successfully in the recorded execution. The symbolic identities corroborate the calculation; the theorem for every admissible radius, angle, and integer lift rests on the algebraic argument above, not on finite numerical sampling. To reproduce: `python checker.py` with Python 3 and SymPy installed.

## Relationship to prior work
Garcia–Mashreghi–Ross's finite-Blaschke survey [1] gives the boundary noncriticality, reciprocal critical-point pairing, and exact degree-minus-one count for interior critical points, but not the explicit two-orbit zero-angle collision curve or the critical-value cusp constant. Favorov–Golinskii [2] address critical-point restrictions for infinite Blaschke products via function-space estimates, not this finite-degree phase diagram. The cubic classification of Fletcher–Hill [3] gives a disk-automorphism normal form and a hyperbolic-midpoint theorem for arbitrary cubic products, but its studied invariants and displayed classification do not give the specific prescribed-zero angular threshold and the critical-value three-halves splitting law; the present computation is in the original zero coordinates and extends to every rotational lift. The distinction is a claim-level comparison, not a claim of exhaustive publication priority.

## Limitations
This result is a same-source algebraic classification in a structured parameter family, not a theorem about generic zero triples or dynamical elliptic/parabolic regimes. The cusp expansion is local at fixed \(r\in(0,1)\); no uniform remainder as \(r\to0\) or \(r\to1\) is asserted. Independent literature priority and independent verification are not established. The specified excluded zero-collision endpoints \(c=\pm1\) are not classified. No assertion is made about critical values under iteration.

## References
[1] S. R. Garcia, J. Mashreghi, W. T. Ross, *Finite Blaschke products: a survey*, arXiv:1512.05444 (first public preprint 2015-12-17), especially Sections 3, 7, 8 and 10. https://arxiv.org/pdf/1512.05444

[2] S. Favorov, L. Golinskii, *On critical points of Blaschke products*, arXiv:1009.1755 (first public preprint 2010-09-09). https://arxiv.org/html/1009.1755v2

[3] A. N. Fletcher, A. Hill, *On cubic Blaschke products*, arXiv:2511.13484 (first public preprint 2025-11-17), especially Proposition 1.1 and Theorem 1.2. https://arxiv.org/abs/2511.13484
