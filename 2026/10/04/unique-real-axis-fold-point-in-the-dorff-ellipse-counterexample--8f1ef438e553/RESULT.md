# Unique real-axis fold point in the Dorff ellipse counterexample

## Finding

Let
\[
f=h+\overline g
\]
be the normalized convex harmonic ellipse mapping constructed by Wang and Zhong, and let
\[
F=f\widetilde *f=p+\overline q
\]
be its harmonic self-convolution.

The source proves that the Jacobian changes sign between
\[
-\frac{99}{100}
\]
and \(0\). The exact rational formulas in the same construction determine the entire real-diameter sign pattern.

Define
\[
\begin{aligned}
P_4(x)=\;&24297200x^4-94137557624x^3+96137381658603x^2\\
&-231722242336904x-360263217096475
\end{aligned}
\]
and
\[
\begin{aligned}
P_6(x)=\;&20269382049144670000x^6
-76570023016489888285400x^5\\
&+64433804996566834468116815x^4
+6563513204097494574954697684x^3\\
&+196525575821143049386765307327x^2\\
&-546666175276725488438747500196x\\
&-701902078885331749352905757780.
\end{aligned}
\]

Then \(P_4\) has no root in \((-1,1)\) and is negative there, while \(P_6\) has exactly one root
\[
x_*\in(-1,1).
\]
It is enclosed by
\[
-0.961916078016036<x_*<-0.961916078016035.
\]

Consequently,
\[
J_F(x)<0
\quad
(-1<x<x_*),
\]
\[
J_F(x_*)=0,
\]
and
\[
J_F(x)>0
\quad
(x_*<x<1).
\]

Hence the real diameter contains exactly one fold point, and the self-convolution is orientation-reversing on precisely the interval
\[
(-1,x_*).
\]

## Assumptions and scope

The notation and normalization are those of the source. Its normalized mapping has
\[
h(z)=z+\sum_{n\ge2}M_nz^n,
\qquad
g(z)=\sum_{n\ge2}N_nz^n,
\]
with the two geometric tails
\[
M_n=Aa^{n-2}+Bb^{n-2},
\qquad
N_n=Da^{n-2}+Cb^{n-2},
\]
where
\[
a=-\frac{10}{11},
\qquad
b=\frac1{44},
\]
and
\[
A=-\frac{9890884608}{9139543205},
\qquad
B=-\frac{251761689}{562995861428},
\]
\[
C=\frac{41190732}{12795360487},
\qquad
D=\frac{1373955264}{9139543205}.
\]

For the self-convolution,
\[
p'(z)
=
1+A^2S_{a^2}(z)+2ABS_{ab}(z)+B^2S_{b^2}(z),
\]
\[
q'(z)
=
D^2S_{a^2}(z)+2DCS_{ab}(z)+C^2S_{b^2}(z),
\]
where
\[
S_r(z)=\frac{z(2-rz)}{(1-rz)^2}.
\]

The result classifies only zeros and signs of the Jacobian on the real diameter. It does not classify nonreal critical points.

## Proof

On the real interval \((-1,1)\), the source formulas give
\[
J_F(x)
=
p'(x)^2-q'(x)^2
=
\bigl(p'(x)-q'(x)\bigr)
\bigl(p'(x)+q'(x)\bigr).
\]

Exact rational simplification yields
\[
p'(x)-q'(x)
=
-\frac{
3748096\,P_4(x)
}{
24606462475\,(x-1936)^2(100x-121)^2
}
\]
and
\[
p'(x)+q'(x)
=
-\frac{
3748096\,P_6(x)
}{
818606249961404385845\,
(x-1936)^2(5x+242)^2(100x-121)^2
}.
\]

Every denominator factor is nonzero on
\[
-1<x<1.
\]
Thus the sign of the Jacobian is determined entirely by the two polynomial factors.

An exact Sturm count gives
\[
\#\{x\in(-1,1):P_4(x)=0\}=0.
\]
Since
\[
P_4(0)<0,
\]
it follows that
\[
P_4(x)<0
\]
throughout the real diameter.

The same exact root count gives
\[
\#\{x\in(-1,1):P_6(x)=0\}=1.
\]
Call that root \(x_*\). Direct exact-sign evaluation at the rational decimal endpoints gives
\[
P_6(-0.961916078016036)>0
\]
and
\[
P_6(-0.961916078016035)<0.
\]
Therefore
\[
-0.961916078016036<x_*<-0.961916078016035.
\]

Because \(P_4<0\), the first factor
\[
p'-q'
\]
is positive throughout \((-1,1)\). The sign of \(J_F\) is therefore the sign of
\[
p'+q',
\]
which is the opposite of the sign of \(P_6\).

Since
\[
P_6(0)<0,
\]
the sextic is negative on \((x_*,1)\) and positive on \((-1,x_*)\). This proves
\[
J_F(x)>0
\quad
(x_*<x<1)
\]
and
\[
J_F(x)<0
\quad
(-1<x<x_*).
\]

At \(x_*\),
\[
p'(x_*)+q'(x_*)=0,
\]
so
\[
p'(x_*)=-q'(x_*),
\]
and the harmonic Jacobian vanishes there.

## Verification

The exact coefficients \(a,b,A,B,C,D\) and the rational derivative formulas were taken from the primary source and reconstructed symbolically.

The packaged checker uses exact rational arithmetic to form \(p'\), \(q'\), and \(J_F\). It verifies the displayed factorization, counts roots of \(P_4\) and \(P_6\) in \((-1,1)\) by an exact Sturm procedure, and checks the two rational signs bracketing \(x_*\).

It also reproduces the source mechanism:
\[
J_F(0)=1
\]
and
\[
J_F(-99/100)<0.
\]
The numerical decimal for \(x_*\) is not used to prove uniqueness.

## Relationship to prior work

Wang and Zhong construct the first bounded convex harmonic self-convolution counterexample answering Dorff's problem. Their proof needs only one negative Jacobian value at
\[
-99/100
\]
and the positive value at the origin, so it concludes existence of at least one real critical point by continuity.

The present finding uses their exact two-tail formulas to determine the complete real-axis picture. It proves there is exactly one critical point on the real diameter and identifies the full orientation-reversing interval.

Earlier harmonic convolution papers establish positive univalence or directional-convexity results under special dilatation hypotheses, especially for half-plane and strip mappings. Those theorems do not analyze the new ellipse counterexample or its exact Jacobian zero.

Targeted searches for the new source together with real critical points, Jacobian roots, fold location, and orientation reversal did not locate a published statement equivalent to this classification.

## Limitations

The finding is one-dimensional in the sense that it classifies the Jacobian only on the real diameter.

There may be nonreal zeros of the Jacobian in the disk; none are ruled out or counted here.

The result does not provide a universal dilatation criterion for harmonic self-convolution.

## References

1. Z.-G. Wang and D. Zhong, *A counterexample to an open problem of Dorff*, arXiv:2609.11556v1, 2026.
2. M. Dorff, *Convolutions of planar harmonic convex mappings*, Complex Variables 45 (2001), 263–271. DOI: 10.1080/17476930108815381.
3. Z. Boyd, M. Dorff, M. Nowak, M. Romney, and M. Wołoszkiewicz, *Univalency of convolutions of harmonic mappings*, Applied Mathematics and Computation 234 (2014), 326–332. DOI: 10.1016/j.amc.2014.01.162.
4. O. P. Ahuja and J. M. Jahangiri, *Convolutions of Harmonic Functions with Certain Dilatations*, International Journal of Mathematics and Mathematical Sciences 2017, Article 4015268. DOI: 10.1155/2017/4015268.
