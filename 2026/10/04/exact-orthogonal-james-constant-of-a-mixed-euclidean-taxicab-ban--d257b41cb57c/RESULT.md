# Exact orthogonal James constant of a mixed Euclidean–taxicab Banach plane
## Finding
Let \(X=(\mathbb R^2,\|\cdot\|)\) be the real Banach plane with
\[
\|(s,t)\|=\begin{cases}
\sqrt{s^2+t^2},&st\ge0,\\
|s|+|t|,&st<0.
\end{cases}
\]
For Birkhoff--James orthogonality \(x\perp_B y\), define
\[
J_\perp(X)=\sup\left\{\min\{\|x+y\|,\|x-y\|\}:x,y\in S_X,\ x\perp_B y\right\}.
\]
Then
\[
J_\perp(X)=\frac{2}{\sqrt{1+\tau^2}}=1.6256295733131909\ldots,
\]
where \(\tau\) is the unique root in \((\sqrt2-1,1)\) of
\[
\tau^4+2\tau^3-1=0.
\]
Equivalently, if \(s=J_\perp(X)^2\), then \(s=2.642671509630427\ldots\) is the relevant root of
\[
s^4-12s^3+64s^2-128s+64=0.
\]
A maximizing pair is
\[
x=(1,0),\qquad y=(a_0,b_0),\qquad
a_0=\frac{1-\tau^2}{1+\tau^2},\quad b_0=\frac{2\tau}{1+\tau^2}.
\]
Numerically, \(a_0=0.3213357548152136\ldots\) and \(b_0=0.9469653281284046\ldots\). Coordinate swap, central sign changes, and replacing \(y\) by \(-y\) give the corresponding symmetric maximizers.

## Assumptions and scope
The space is real and two-dimensional. Birkhoff--James orthogonality means \(x\perp_B y\) when \(\|x\|\le\|x+ry\|\) for every real \(r\). The unit circle consists of Euclidean quarter-circles in the regions where the coordinate product is nonnegative and line segments of the \(\ell_1\) diamond where the coordinate product is negative.

The proof uses the standard support-functional characterization: \(x\perp_B y\) exactly when a norm-one supporting functional at \(x\) annihilates \(y\). No smoothness assumption is imposed at the coordinate axes; their full supporting-functional intervals are used.

## Proof
By central symmetry and coordinate interchange, it is enough to classify the location of \(x\) on three types of unit-sphere pieces.

**1. Interior of a Euclidean arc.** Write \(x=(c,s)\) with \(c,s>0\) and \(c^2+s^2=1\). The unique norming functional is \((c,s)\), so an orthogonal unit vector can be taken as
\[
y=\frac{(-s,c)}{c+s}.
\]
Indeed, \(y\) lies in an opposite-sign quadrant and therefore has norm one. Put \(q=c+s\ge1\). The Euclidean scalar product of \(x\) and \(y\) is zero and the Euclidean length of \(y\) is \(q^{-1}\), hence both \(x+y\) and \(x-y\) have Euclidean length \(\sqrt{1+q^{-2}}\).

At least one of \(x+y\) and \(x-y\) has coordinate product nonnegative. Otherwise one would have simultaneously \(cq<s\) and \(sq<c\); multiplying gives \(q^2<1\), a contradiction. The norm of that vector is therefore its Euclidean length. Consequently
\[
\min\{\|x+y\|,\|x-y\|\}\le\sqrt{1+q^{-2}}\le\sqrt2.
\]

**2. Interior of an \(\ell_1\) segment.** Write \(x=(u,-v)\) with \(u,v>0\) and \(u+v=1\). Its norming functional is \((1,-1)\), so an orthogonal unit vector can be taken as \(y=(r,r)\), where \(r=1/\sqrt2\). If \(u>r\), then \(x-y\) is in an opposite-sign quadrant and \(\|x-y\|=1\); if \(v>r\), then \(\|x+y\|=1\). In the remaining case \(u,v\le r\), both relevant vectors lie in Euclidean quadrants. Their squared Euclidean lengths have average \(u^2+v^2+1\le2\), so their smaller norm is at most \(\sqrt2\). Thus every orthogonal pair with \(x\) in the interior of a line segment contributes at most \(\sqrt2\).

**3. Coordinate axis.** By symmetry take \(x=(1,0)\). The supporting functionals at this corner are
\[
f_\sigma(z_1,z_2)=z_1+\sigma z_2,\qquad -1\le\sigma\le0.
\]
After replacing \(y\) by \(-y\) if needed, the equation \(f_\sigma(y)=0\) forces
\[
y=(a,b),\qquad 0\le a\le b,\qquad a^2+b^2=1.
\]
Hence \(0\le a\le1/\sqrt2\) and \(b=\sqrt{1-a^2}\). The two norms are
\[
F(a)=\|x+y\|=\sqrt{2(1+a)},\qquad
G(a)=\|x-y\|=1-a+\sqrt{1-a^2}.
\]
Here \(F\) is strictly increasing and \(G\) is strictly decreasing. Moreover \(F(0)=\sqrt2<G(0)=2\), while \(F(1/\sqrt2)>G(1/\sqrt2)=1\). Therefore \(\min\{F(a),G(a)\}\) has a unique maximum at the crossing \(F(a_0)=G(a_0)\).

Introduce
\[
t=\sqrt{\frac{1-a}{1+a}},\qquad
\sqrt2-1\le t\le1.
\]
Then
\[
a=\frac{1-t^2}{1+t^2},\qquad
b=\frac{2t}{1+t^2},\qquad
F=\frac{2}{\sqrt{1+t^2}},\qquad
G=\frac{2t(t+1)}{1+t^2}.
\]
The crossing condition is
\[
\sqrt{1+t^2}=t(t+1),
\]
and because both sides are positive this is equivalent to
\[
t^4+2t^3-1=0.
\]
The polynomial has derivative \(4t^3+6t^2>0\) for \(t>0\), and its values at \(\sqrt2-1\) and \(1\) have opposite signs. It therefore has exactly one root \(\tau\) in the required interval. At that root,
\[
\max_a\min\{F(a),G(a)\}=\frac{2}{\sqrt{1+\tau^2}}.
\]
Since \(\tau<1\), this value is strictly larger than \(\sqrt2\), so the axis case dominates the two interior cases. This proves the formula and attainment.

Eliminating \(\tau\) from \(s=4/(1+\tau^2)\) and \(\tau^4+2\tau^3-1=0\) gives \(s^4-12s^3+64s^2-128s+64=0\), which yields the stated equivalent algebraic description.

## Verification
The argument is exhaustive because every point of the unit sphere is either in the interior of a Euclidean arc, in the interior of an \(\ell_1\) segment, or on a coordinate axis; the latter are exactly the nonsmooth junctions handled by the full supporting-functional interval.

The accompanying `verify.py` independently reconstructs the unique positive root in the relevant interval by bisection, checks the defining quartic and the equivalent polynomial for \(J_\perp(X)^2\), evaluates the stated extremizer in the original piecewise norm, and samples each analytic branch as a diagnostic. The sampling is not used as proof; the global inequalities above are analytic.

## Relationship to prior work
Baronti and Papini introduced \(J_\perp\) and, in Example 5.4 of their 2022 paper, studied exactly this norm. They reported that the calculation is nontrivial and gave only the numerical information \(J_\perp(X)\approx1.626\), attained near a vector with first coordinate \(0.321\). The formula above identifies that number algebraically and proves the global maximum by an exhaustive support-functional classification.

A 2024 paper by Martín and Papini revisits extreme norms of sums of Birkhoff-orthogonal unit vectors and explicitly recalls \(J_\perp\) and several exact examples from the 2022 paper, but its inspected text does not supply an exactification of Example 5.4. Later 2026 work introduces weighted and approximate-Birkhoff variants of the orthogonal James constant; the searched descriptions establish broader parameter families but do not imply the algebraic value for this specific mixed norm.

## Limitations
The result concerns one natural two-dimensional mixed Euclidean--taxicab norm and the unweighted orthogonal James constant. It does not compute the weighted or approximate-Birkhoff profiles, does not claim a formula for higher-dimensional analogues, and does not classify every symmetry representative beyond the maximizing orbit described above. The originality check cannot exclude an obscure unindexed independent derivation.

## References
1. M. Baronti and P. L. Papini, *Parameters in Banach spaces and orthogonality*, Constructive Mathematical Analysis 5 (2022), 37--45, DOI:10.33205/cma.1067323. Published online 2022-03-09.
2. P. Martín and P. L. Papini, *Moving around the sums of orthogonal unit vectors*, Mathematical Inequalities & Applications 27 (2024), 401--415, DOI:10.7153/mia-2024-27-28.
3. J. Qi, Z. Yin, Q. Liu, and Y. Li, *A weighted Birkhoff orthogonal James-type constant*, arXiv:2606.01068 (2026).
4. Z. Fang, Y. Xu, Q. Liu, Z. Gu, and Y. Li, *James-type constants for Birkhoff--James orthogonality and approximate isosceles*, arXiv:2609.37502 (2026).
