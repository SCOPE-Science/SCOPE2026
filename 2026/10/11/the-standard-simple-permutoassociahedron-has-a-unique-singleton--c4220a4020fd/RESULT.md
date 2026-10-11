# The standard simple permutoassociahedron has a unique singleton-facet inball
## Finding
For every integer
\[
n\ge2,
\]
let
\[
PA_n\subset\mathbb R^{n+1}
\]
be the standard simple permutoassociahedron of Baralić, Ivanović, and Petrić.

The source realizes \(PA_n\) in the affine hyperplane
\[
x_0+\cdots+x_n=3^{n+1}.
\tag{1}
\]
Its unique Euclidean incenter is
\[
\boxed{
c_n=\frac{3^{n+1}}{n+1}\mathbf1
}
\tag{2}
\]
and its exact intrinsic inradius is
\[
\boxed{
r_{\mathrm{in}}(PA_n)
=
\frac{3^{n+1}-3(n+1)}{\sqrt{n(n+1)}}.
}
\tag{3}
\]

The centered maximal ball is tangent exactly to the
\[
\boxed{n+1}
\]
singleton facets
\[
x_i=3,
\qquad
0\le i\le n.
\tag{4}
\]
Every other facet lies strictly farther from \(c_n\).

## Assumptions and scope
The realization is exactly the halfspace realization introduced in *A simple permutoassociahedron*. It is not an arbitrary realization of the same face lattice.

Distances are intrinsic to the affine hyperplane (1), with the metric inherited from the standard orthonormal coordinates of \(\mathbb R^{n+1}\).

The theorem is stated for \(n\ge2\), the range in which the non-singleton facet comparison is nontrivial.

## Proof
Put
\[
N=n+1,
\qquad
\mu=\frac{3^N}{N}.
\tag{5}
\]
The source facets are indexed by integers
\[
1\le k\le k+l\le n.
\]
Writing
\[
t=k+l,
\]
the corresponding facet normal has positive coefficients
\[
1,2,\ldots,k-1,
\underbrace{k,\ldots,k}_{l+1\text{ times}}
\tag{6}
\]
on \(t\) distinct coordinates and zero elsewhere. Its facet equation is
\[
\langle a,x\rangle=\kappa(k,l),
\tag{7}
\]
where
\[
\kappa(k,l)
=
\frac{3^{t+1}-3^{l+1}}2
+
\frac{3^k-3k}{3^n-n-1}.
\tag{8}
\]
The halfspace containing \(PA_n\) is
\[
\langle a,x\rangle\ge\kappa(k,l).
\]

Let
\[
W=\sum_i a_i,
\qquad
Q=\sum_i a_i^2.
\tag{9}
\]
Explicitly,
\[
W=\frac{k(k+2l+1)}2
\tag{10}
\]
and
\[
Q=
\frac{(k-1)k(2k-1)}6
+
(l+1)k^2.
\tag{11}
\]

Inside the tangent space \(\mathbf1^\perp\) of (1), the projected facet normal has squared norm
\[
P=Q-\frac{W^2}{N}.
\tag{12}
\]
At the uniform point \(c_n=\mu\mathbf1\), the facet distance is therefore
\[
d_{k,l}
=
\frac{\mu W-\kappa(k,l)}{\sqrt P}.
\tag{13}
\]

For the singleton case
\[
(k,l)=(1,0),
\]
we have
\[
W=Q=1,
\qquad
P=\frac nN,
\qquad
\kappa(1,0)=3.
\]
Hence
\[
d_{1,0}
=
(\mu-3)\sqrt{\frac Nn}
=
\frac{3^N-3N}{\sqrt{N(N-1)}},
\tag{14}
\]
which is exactly (3).

We prove that every facet with
\[
t\ge2
\]
has strictly larger distance.

Define
\[
H=\sqrt{\frac{NP}{n}}.
\tag{15}
\]
Comparing (13) with (14), it is enough to show
\[
\kappa(k,l)
<
\mu(W-H)+3H.
\tag{16}
\]

First,
\[
H^2
=
\frac{NQ-W^2}{n}
=
Q-\frac{W^2-Q}{n}
\le Q,
\]
so
\[
H\le\sqrt Q.
\tag{17}
\]
The \(t\) positive entries of \(a\) are all at least \(1\). Writing
\[
a=\mathbf1+b
\]
on its support, with \(b_i\ge0\), the triangle inequality gives
\[
\sqrt Q
=
\|\mathbf1+b\|_2
\le
\sqrt t+\|b\|_2
\le
\sqrt t+\|b\|_1
=
\sqrt t+W-t.
\]
Thus
\[
W-H\ge t-\sqrt t.
\tag{18}
\]

The source also records
\[
\kappa(k,l)
=
3^t+3^{t-1}+\cdots+3^{l+1}+\varepsilon(k),
\qquad
0\le\varepsilon(k)<1.
\]
Therefore
\[
\kappa(k,l)
<
\frac{3^{t+1}}2+1.
\tag{19}
\]

Since
\[
N\ge t+1
\]
and \(3^N/N\) increases with \(N\ge3\),
\[
\mu\ge\frac{3^{t+1}}{t+1}.
\tag{20}
\]
For \(t\ge6\), the function
\[
\frac{t-\sqrt t}{t+1}-\frac12
\]
is increasing. At \(t=6\),
\[
\frac{6-\sqrt6}{7}-\frac12
=
\frac{5-2\sqrt6}{14}
>
\frac1{140}
>
\frac1{3^7},
\]
where \(\sqrt6<49/20\). Consequently, for every \(t\ge6\),
\[
\frac{t-\sqrt t}{t+1}
>
\frac12+\frac1{3^{t+1}}.
\tag{21}
\]
Equations (18)--(21) imply
\[
\mu(W-H)
>
\frac{3^{t+1}}2+1
>
\kappa(k,l),
\]
so (16) holds strictly.

For \(2\le t\le5\), the same coarse bounds already prove (16) except for the following finite parameter pairs:
\[
(N,t)\in
\{(3,2),(4,2),(4,3),(5,4),(6,5)\}.
\tag{22}
\]
Indeed:
\[
t=2,\ N\ge5;
\qquad
t=3,\ N\ge5;
\qquad
t=4,\ N\ge6;
\qquad
t=5,\ N\ge7
\]
follow respectively from
\[
\sqrt2<\frac32,\quad
\sqrt3<2,\quad
\sqrt4=2,\quad
\sqrt5<\frac52
\]
together with (18)--(20) and (19).

For the five pairs in (22), use the exact rational comparison
\[
\Delta
=
(\mu W-\kappa)^2
-
(\mu-3)^2H^2.
\tag{23}
\]
All quantities in (23) are rational. Exhausting
\[
1\le k\le t,\qquad l=t-k,
\]
the minimum exact values are
\[
\begin{array}{c|c}
(N,t)&\min_k\Delta\\
\hline
(3,2)&45\\
(4,2)&1191/2\\
(4,3)&1683/2\\
(5,4)&53901/5\\
(6,5)&118818
\end{array}
\tag{24}
\]
and are all positive. The accompanying exact-arithmetic verifier reproduces every entry of (24). This finishes the proof that all non-singleton facets are strictly farther from \(c_n\) than the singleton facets.

It remains to prove global optimality and uniqueness of the incenter. Every singleton set is a source facet, so
\[
x_i\ge3
\tag{25}
\]
for every \(i\). The intrinsic normal length of \(x_i=3\) inside (1) is
\[
\sqrt{\frac nN}.
\]
If a radius-\(\rho\) ball centered at \(q\) lies in \(PA_n\), then every singleton facet gives
\[
q_i-3
\ge
\rho\sqrt{\frac nN}.
\tag{26}
\]
Summing (26) over all \(N\) coordinates and using (1),
\[
3^N-3N
\ge
N\rho\sqrt{\frac nN}.
\]
Hence
\[
\rho
\le
\frac{3^N-3N}{\sqrt{Nn}},
\]
which is (3). The ball centered at \(c_n\) attains this value by the preceding facet-distance comparison.

If equality holds, then every inequality in (26) must be equality, forcing all coordinates of \(q\) to be equal. Equation (1) then forces
\[
q=c_n.
\]
Thus the incenter is unique.

## Verification
The proof is symbolic for all \(n\ge2\), apart from the explicitly isolated five finite pairs in (22), which are checked exactly rather than numerically.

The source-dependent premises were checked directly in the primary full text and page image: the affine equation, the complete facet family, the exact \(\kappa(k,l)\) formula, the singleton facets \(x_i=3\), and facet-defining status.

The accompanying `verify.py` performs two independent checks. It reproduces the exact rational finite table (24), and it exhaustively checks every facet parameter
\[
1\le k\le k+l\le n
\]
for
\[
2\le n\le60
\]
using exact rational squared-distance comparisons. The finite all-\(n\) replay is corroborative only; the inequalities above prove the arbitrary-dimensional result.

## Relationship to prior work
Baralić, Ivanović, and Petrić introduced this simple permutoassociahedron and gave the explicit halfspace realization used here. Their construction makes the singleton inequalities visible and proves every indexed halfspace is facet-defining. The paper studies combinatorics, coherence, and geometric realization, not Euclidean inradii.

Ivanović later gave Minkowski-sum realizations normally equivalent to the same simple permutoassociahedron and restated the defining halfspaces. That work concerns normal equivalence and Minkowski decomposition rather than Euclidean largest-inscribed balls.

The exact inradius is not a formal consequence of the fact that \(PA_n\) lies inside the simplex cut out by
\[
x_i\ge3.
\]
One must still prove that every additional permutoassociahedral facet stays outside that simplex's insphere. Inequality (16), including the exact small-parameter certificate, supplies this missing comparison.

Targeted searches under “simple permutoassociahedron”, “permutoassociahedron”, “inradius”, “Chebyshev center”, “Euclidean facet distance”, and “inball” did not locate a theorem implying (2)--(4).

## Limitations
The theorem is realization-specific. Normally equivalent or combinatorially equivalent permutoassociahedra obtained by moving facets can have different Euclidean inradii.

The proof uses the source's exponentially scaled constants \(3^j\); it does not claim the same singleton-only tangency for arbitrary deformations of those constants.

The result determines the inball and its contact facets, not the circumradius, John ellipsoid, or complete metric geometry.

A residual originality risk remains for an equivalent observation in unpublished notes about this explicit realization. Search nonappearance is not treated as a formal global novelty certificate.

## References
1. Djordje Baralić, Jelena Ivanović, and Zoran Petrić, *A simple permutoassociahedron*, arXiv:1708.02482, first public version 2017-08-08; Discrete Mathematics 342 (2019), 111591, DOI 10.1016/j.disc.2019.07.007.
2. Jelena Ivanović, *Geometrical Realisations of the Simple Permutoassociahedron by Minkowski Sums*, arXiv:1904.06700, first public version 2019-04-15.
