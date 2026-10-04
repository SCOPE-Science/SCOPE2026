# Exact GC2 threshold count for a commensurately dilated honeycomb quantum graph

## Finding

Consider the periodic honeycomb quantum graph with two equal edge lengths and one doubled length,
\[
a=2b,\qquad c=b,\qquad b>0,
\]
and a common vertex \(\delta\)-coupling of strength \(\eta\in\mathbb R\).  For positive energy \(E=k^2\), set
\[
x=bk,\qquad \beta=\eta b,\qquad d=\arcsin(1/4),\qquad x_m=\left(m+\frac12\right)\pi\quad(m\ge0).
\]
Exner and Turek's lower gap condition GC2 specializes to
\[
\frac1{|\sin 2x|}-\frac2{|\sin x|}
>
\left|\cot 2x+2\cot x+\frac{\beta}{x}\right|.
\]

If \(\beta=0\), this inequality has no solution.  If \(\beta\ne0\), write \(\varepsilon=\operatorname{sgn}\beta\).  Then for every \(m\ge0\) the GC2 solution set has either no point near \(x_m\), or exactly one connected open interval.  Such an interval exists precisely when
\[
|\beta|>\tau_{m,\varepsilon},\qquad
\tau_{m,\varepsilon}:=\sqrt{\frac53}\left(x_m-\varepsilon d\right).
\]
For positive coupling it lies on the left flank \(x\in(x_m-d,x_m)\); for negative coupling it lies on the right flank \(x\in(x_m,x_m+d)\).  Equality \(|\beta|=\tau_{m,\varepsilon}\) does not produce an interval because GC2 is strict.

Hence the exact number of connected positive-momentum intervals certified by GC2 is
\[
N(0)=0,
\]
and, for \(\beta\ne0\),
\[
N(\beta)=
\max\!\left\{0,
\left\lceil
\frac{\sqrt{3/5}\,|\beta|+\varepsilon d}{\pi}-\frac12
\right\rceil
\right\}.
\]
For example, the first threshold is approximately \(1.7016805313\) for positive \(\beta\), but approximately \(2.3540981447\) for negative \(\beta\); the asymmetry comes from the term \(\eta/k\), which selects opposite flanks around each zero of \(\cos x\).

This is an exact classification of the GC2-certifying set, not of the entire spectral complement.  In particular, since \(a/b=2\) is rational, the same source proves that GC1 generates infinitely many gaps whenever \(\eta\ne0\).

## Assumptions and scope

The graph, Hamiltonian, and GC2 inequality are those of Exner and Turek for a honeycomb metric graph with common \(\delta\)-coupling.  The result fixes the simplest nonequilateral commensurate one-direction dilation \(a:b:c=2:1:1\), considers positive energy only, and counts connected components of the set where GC2 holds.  It does not claim that the full spectrum has finitely many gaps, and it does not classify negative-energy gaps.

## Proof

For \(a=2b\) and \(c=b\), Exner and Turek's condition (19) becomes
\[
\frac1{|\sin 2x|}-\frac2{|\sin x|}
>
\left|\cot 2x+2\cot x+\frac{\beta}{x}\right|.
\]
The left side is positive exactly when \(|\cos x|<1/4\).  Thus every possible solution lies in one of the disjoint flanks
\[
x_m-d<x<x_m+d.
\]
On such a flank put
\[
t=|\cos x|\in(0,1/4),\qquad s=\sqrt{1-t^2},\qquad q=\operatorname{sgn}(\sin x\cos x).
\]
The identity
\[
\cot 2x+2\cot x=\frac{6t^2-1}{2\sin x\cos x}
\]
turns GC2, after multiplication by \(2ts\), into
\[
1-4t>
\left|-q(1-6t^2)+\frac{2\beta ts}{x}\right|.
\]
When \(\beta=0\), the right side is \(1-6t^2\), which is strictly larger than \(1-4t\) for \(0<t<1/4\), so there are no solutions.

Assume now \(\beta\ne0\) and let \(\varepsilon=\operatorname{sgn}\beta\).  If \(q\ne\varepsilon\), the two terms inside the absolute value have the same sign and its magnitude exceeds \(1-6t^2>1-4t\).  Therefore every solution has \(q=\varepsilon\).  Around every \(x_m\), the sign of \(\sin x\cos x\) is positive on the left and negative on the right, so the sign of the coupling selects exactly one flank.  On that flank
\[
x=x_m-\varepsilon\arcsin t.
\]
Writing \(\gamma=|\beta|\), the inequality is equivalent to the pair
\[
F_{m,\varepsilon}(t)<\gamma<G_{m,\varepsilon}(t),
\]
where
\[
F_{m,\varepsilon}(t)=
\frac{x(2-3t)}{\sqrt{1-t^2}},
\qquad
G_{m,\varepsilon}(t)=
\frac{x(1+t)(1-3t)}{t\sqrt{1-t^2}}.
\]
A direct subtraction gives \(G_{m,\varepsilon}(t)>F_{m,\varepsilon}(t)\) on \(0<t<1/4\).

Both functions are strictly decreasing.  For
\[
r(t)=\frac{2-3t}{\sqrt{1-t^2}},
\]
one has
\[
r'(t)=\frac{2t-3}{(1-t^2)^{3/2}}<0.
\]
If \(\varepsilon=+1\), the factor \(x=x_m-\arcsin t\) also decreases, so \(F'_{m,+}<0\).  If \(\varepsilon=-1\), then
\[
(1-t^2)^{3/2}F'_{m,-}
=(2-3t)\sqrt{1-t^2}-x(3-2t)<0,
\]
because \(x\ge\pi/2\), \(3-2t>5/2\), and the first term is below \(2\).

Similarly, for
\[
h(t)=\frac{(1+t)(1-3t)}{t\sqrt{1-t^2}},
\]
\[
h'(t)=-\frac{2t^2-t+1}{t^2(1-t)\sqrt{1-t^2}}<0.
\]
Again \(G'_{m,+}<0\).  For \(\varepsilon=-1\), multiplying \(G'_{m,-}\) by the positive quantity \(t^2(1-t)(1-t^2)\) leaves
\[
t(1-t)(1-2t-3t^2)-x(2t^2-t+1)\sqrt{1-t^2},
\]
which is negative because the first term is less than \(1/4\), whereas the second is larger than \((\pi/2)(7/8)(\sqrt{15}/4)>1\).

The endpoint limits are
\[
\lim_{t\downarrow0}F_{m,\varepsilon}(t)=2x_m,
\qquad
\lim_{t\downarrow0}G_{m,\varepsilon}(t)=+\infty,
\]
and
\[
\lim_{t\uparrow1/4}F_{m,\varepsilon}(t)
=
\lim_{t\uparrow1/4}G_{m,\varepsilon}(t)
=
\sqrt{\frac53}\left(x_m-\varepsilon d\right).
\]
Since \(F\) and \(G\) are continuous, strictly decreasing, and satisfy \(F<G\), the set \(\{t:F(t)<\gamma<G(t)\}\) is empty when \(\gamma\le\tau_{m,\varepsilon}\) and is exactly one open interval when \(\gamma>\tau_{m,\varepsilon}\).  Counting the nonnegative integers \(m\) with this strict inequality gives
\[
N(\beta)=
\max\!\left\{0,
\left\lceil
\frac{\sqrt{3/5}\,|\beta|+\varepsilon d}{\pi}-\frac12
\right\rceil
\right\}.
\]

## Verification

The proof is analytic and does not rely on numerical experiments.  The supplementary script `verify_honeycomb_gc2.py` checks the algebraic transformation of GC2 on dense deterministic grids, verifies the predicted sign-selected flank and the threshold component count for several positive and negative dimensionless couplings, and checks monotonicity numerically away from the singular endpoints.  The replay prints `VERIFY_OK`.

## Relationship to prior work

Exner and Turek derive the honeycomb spectral condition and, in the case \(b=c\), isolate the lower gap condition GC2 as their condition (19).  Their Theorem 4.1 proves that when \(a/b\) is rational, GC1 generates infinitely many gaps for every nonzero coupling.  Their Corollary 4.5 proves only that for rational \(a/b\), condition (19) can generate at most finitely many gaps; it does not enumerate them for the ratio \(a/b=2\).

A later paper by the same authors studies the Bethe--Sommerfeld property on periodic quantum graphs and constructs rectangular lattices with a prescribed finite number of total gaps using suitable irrational edge-length ratios.  That result concerns a different lattice and a different number-theoretic regime.  Targeted searches for the constants \(\arcsin(1/4)\) and \(\sqrt{5/3}\), for the ratio \(2:1:1\), and for an exact count attached to condition (19) did not locate the formula above.

## Limitations

The result is a sharp special-case refinement of a known sufficient gap condition, not a new general spectral theorem.  It counts connected components of the GC2-certifying region at the fixed commensurate ratio \(2:1:1\); GC1 still supplies infinitely many gaps for nonzero coupling, so the total spectrum does not have the Bethe--Sommerfeld property in this case.  The derivation does not address other rational ratios, unequal \(b,c\), or negative energies.  An equivalent simplification may exist in notes or literature not indexed by the searches.

## References

1. P. Exner and O. Turek, “Spectrum of a dilated honeycomb network,” arXiv:1405.0694; *Integral Equations and Operator Theory* 81 (2015), 535–557, DOI: 10.1007/s00020-014-2194-1.
2. P. Exner and O. Turek, “Periodic quantum graphs from the Bethe--Sommerfeld perspective,” arXiv:1705.07306; *Journal of Physics A: Mathematical and Theoretical* 50 (2017), 455201.
