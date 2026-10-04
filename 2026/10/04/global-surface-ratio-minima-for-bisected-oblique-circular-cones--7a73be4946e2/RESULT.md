# Global surface-ratio minima for bisected oblique circular cones
## Finding
Let the base be the unit disk in \(z=0\), let the apex be \(p=(0,a,b)\) with \(a\ge 0\) and \(b>0\), and split the cone by Finch's canonical plane through the apex and the base diameter whose endpoints are equidistant from the apex. Put
\[
I_+(a,b)=\int_0^1 \frac{\sqrt{(1-au)^2+b^2}}{\sqrt{1-u^2}}\,du,
\qquad
I_-(a,b)=\int_0^1 \frac{\sqrt{(1+au)^2+b^2}}{\sqrt{1-u^2}}\,du.
\]
For \(a>0\), one has \(I_+<I_-\), so these are the curved-area contributions of the smaller and larger canonical half-cones. Consider the three surface-area ratios used in Finch's paper:
\[
L(a,b)=\frac{I_+}{I_-},\qquad
T(a,b)=\frac{\pi/2+I_+}{\pi/2+I_-},
\]
and, for the addendum's convention that counts the common triangular cut face in each half-cone,
\[
O(a,b)=\frac{\sqrt{a^2+b^2}+\pi/2+I_+}{\sqrt{a^2+b^2}+\pi/2+I_-}.
\]
For every fixed \(a>0\), all three functions are strictly increasing in \(b>0\). Hence each global infimum over \(a\ge0,b>0\) is a boundary infimum as \(b\to0^+\).

Let \(x_L\in(0,\pi/2)\) be the unique root of
\[
2x_L=\pi\cos x_L.
\]
Then the lateral and overlap-inclusive ratios have their unique boundary minimizer at
\[
a_L=\csc x_L=1.2437608987462040336\ldots,
\]
with exact infima
\[
\inf L=2\cos x_L-1=\frac{4x_L}{\pi}-1
=0.18922328811367116598\ldots,
\]
\[
\inf O=\cos x_L=\frac{2x_L}{\pi}
=0.59461164405683558299\ldots.
\]
Let \(x_T\in(0,\pi/2)\) be the unique root of
\[
2x_T+\pi=2\pi\cos x_T.
\]
Then the original total-area ratio has its unique boundary minimizer at
\[
a_T=\csc x_T=1.4782960807222794431\ldots,
\]
with exact infimum
\[
\inf T=2\cos x_T-1=\frac{2x_T}{\pi}
=0.47296889648303336826\ldots.
\]
The infima are not attained by a nondegenerate cone because \(b>0\); they are approached uniquely in horizontal parameter as \(b\to0^+\).

## Assumptions and scope
The normalization and canonical split are exactly those of Finch: unit circular base, apex \(p=(0,a,b)\), \(a\ge0\), \(b>0\). Reflection handles a negative horizontal offset. The finding concerns the lateral-area ratio, Finch's original total-area ratio with one base semicircle assigned to each half, and the addendum's overlap-inclusive total-area ratio. It does not address the mean-width ratio, a different splitting plane, or a different base shape.

## Proof
Write
\[
A(u)=\sqrt{(1-au)^2+b^2},\qquad
B(u)=\sqrt{(1+au)^2+b^2},\qquad
w(u)=\frac1{\sqrt{1-u^2}}.
\]
For \(a>0\) and \(0<u<1\),
\[
B(u)^2-A(u)^2=4au>0,
\]
so \(B>A>0\). Therefore
\[
I_- > I_+,
\qquad
J_+:=\int_0^1\frac{w(u)}{A(u)}\,du
>
J_-:=\int_0^1\frac{w(u)}{B(u)}\,du.
\]
Differentiation under the integral sign is legitimate for \(b>0\), and
\[
\partial_b I_+=bJ_+,\qquad \partial_b I_-=bJ_-.
\]
Hence
\[
\partial_b L
=\frac{b(J_+I_--J_-I_+)}{I_-^2}>0.
\]
More generally, if \(c>0\) is independent of \(b\),
\[
\partial_b\frac{c+I_+}{c+I_-}
=\frac{b[J_+(c+I_-)-J_-(c+I_+)]}{(c+I_-)^2}>0,
\]
which proves \(\partial_bT>0\). For the overlap convention put \(c(b)=\sqrt{a^2+b^2}+\pi/2\). Then
\[
\partial_b O
=\frac{c'(b)(I_--I_+)+b[J_+(c+I_-)-J_-(c+I_+)]}{(c+I_-)^2}>0.
\]
Thus for each fixed \(a>0\), the infimum occurs as \(b\to0^+\). This proves, rather than assumes, the boundary reduction that Finch conjectured to be relevant for surface area.

For \(0\le a\le1\), direct integration at \(b=0\) gives
\[
I_+(a,0)=\frac\pi2-a,\qquad I_-(a,0)=\frac\pi2+a.
\]
Therefore
\[
L_0(a)=\frac{\pi-2a}{\pi+2a},\qquad
T_0(a)=\frac{\pi-a}{\pi+a},\qquad
O_0(a)=\frac{\pi}{\pi+2a},
\]
and each is strictly decreasing on \([0,1]\).

For \(a>1\), Finch's exact boundary formulas are
\[
L_0(a)=\frac{\pi-2a+4\sqrt{a^2-1}-4\operatorname{arcsec}(a)}{\pi+2a},
\]
\[
T_0(a)=\frac{-a+2\sqrt{a^2-1}+2\operatorname{arccsc}(a)}{\pi+a},
\]
\[
O_0(a)=\frac{2\sqrt{a^2-1}+2\operatorname{arccsc}(a)}{\pi+2a}.
\]
Set \(x=\arcsin(1/a)\in(0,\pi/2)\). Then \(a=\csc x\), \(\sqrt{a^2-1}=\cot x\), \(\operatorname{arcsec}(a)=\pi/2-x\), and the three functions become
\[
L_0(x)=\frac{4\cos x+4x\sin x-\pi\sin x-2}{\pi\sin x+2},
\]
\[
T_0(x)=\frac{-1+2\cos x+2x\sin x}{1+\pi\sin x},
\]
\[
O_0(x)=\frac{2\cos x+2x\sin x}{\pi\sin x+2}.
\]
Direct differentiation factors completely:
\[
L_0'(x)=\frac{4(2x-\pi\cos x)\cos x}{(\pi\sin x+2)^2},
\qquad
O_0'(x)=\frac{2(2x-\pi\cos x)\cos x}{(\pi\sin x+2)^2},
\]
\[
T_0'(x)=\frac{(2x-2\pi\cos x+\pi)\cos x}{(1+\pi\sin x)^2}.
\]
The functions \(2x-\pi\cos x\) and \(2x-2\pi\cos x+\pi\) are strictly increasing on \((0,\pi/2)\), because their derivatives are respectively \(2+\pi\sin x\) and \(2+2\pi\sin x\). Each changes sign exactly once. Hence the three boundary profiles have the stated unique minima. Continuity at \(a=1\), together with the strict decrease on \([0,1]\), shows these are also the global minima over all \(a\ge0\).

At \(x_L\), the equation \(2x_L=\pi\cos x_L\) factors the minimum values as
\[
L_0(x_L)=2\cos x_L-1=\frac{4x_L}{\pi}-1,
\qquad
O_0(x_L)=\cos x_L=\frac{2x_L}{\pi}.
\]
At \(x_T\), the equation \(2x_T+\pi=2\pi\cos x_T\) gives
\[
T_0(x_T)=2\cos x_T-1=\frac{2x_T}{\pi}.
\]
This completes the global surface-area optimization.

## Verification
The proof is analytic; no finite experiment is used to infer a universal statement. The bundled `verify.py` independently bisects the two strictly monotone critical equations, reconstructs \(a_L,a_T\) and the three exact minimum formulas, and checks the reported decimal values. It also evaluates the boundary formulas from both the \(a\)- and \(x\)-representations at the roots. The checker is supplementary: the strict \(b\)-monotonicity and uniqueness arguments above are the proof.

## Relationship to prior work
Finch's 2012 paper derives the same one-parameter \(b\to0^+\) formulas and the same numerical critical parameters, but explicitly states that rigorous proofs of minimality are absent and that the relevance of the \(a>1,b\to0^+\) regime is conjectural. The present result proves the missing global reduction: for each fixed horizontal offset the surface-area ratios increase strictly with \(b\), and it then proves uniqueness of the boundary minimizers and simplifies the minimum values to exact expressions in the unique roots \(x_L,x_T\).

A later convex-body optimization paper by Yang and Zhang cites Finch but optimizes volume, surface area, and integral mean curvature under fixed width/radius or diameter/inradius constraints; it does not state a result about the two canonical half-cones. Ding and Fay's earlier paper concerns minimization of the total lateral surface area of a cone, not the smaller-to-larger area ratio of Finch's split. No checked source stated or implied the three global ratio minima proved here.

## Limitations
The mean-width part of Finch's question remains outside this result. The proof also keeps Finch's canonical isosceles-triangle splitting plane; optimization over arbitrary splitting planes is not addressed. The infima occur only as the cone height tends to zero, so they are not attained by a nondegenerate cone. Literature searches cannot exclude unindexed or differently phrased prior work; the full text of Ding and Fay (2001) was not available in the inspected sources, although its abstract describes a different fixed-parameter objective.

## References
1. S. R. Finch, *Oblique Circular Cones and Cylinders*, arXiv:1212.5946v1 (24 December 2012), revised as v2 (31 December 2012), primary MSC 53A05, https://arxiv.org/abs/1212.5946.
2. Y. Yang and D. Zhang, *Two optimisation problems for convex bodies*, Bulletin of the Australian Mathematical Society 93 (2016), 137–145, DOI: 10.1017/S0004972715000799.
3. J. Ding and T. H. Fay, *Minimizing the lateral surface area of a cone*, International Journal of Mathematical Education in Science and Technology 32 (2001), DOI: 10.1080/002073901750334727.
