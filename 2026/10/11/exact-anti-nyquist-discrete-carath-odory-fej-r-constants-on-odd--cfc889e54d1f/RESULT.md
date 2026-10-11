# Exact anti-Nyquist discrete Carathéodory–Fejér constants on odd cycles
## Finding
For every integer \(m\ge 4\), let \(N=2m+1\) and set
\[
D_m=\sup\left\{a\in\mathbb R:\exists b\in\mathbb R,\ 1+a\cos\!\left(rac{2\pi j}{N}ight)+b\cos\!\left(rac{2\pi m j}{N}ight)\ge0\ 	ext{for all }j\in\mathbb Z}ight\}.
\]
If \(lpha=\pi/N\), then
\[
D_m=rac{\cos(lpha/2)}{\coslpha\,\cos(3lpha/2)}.
\]
The coefficient \(b\) is uniquely determined at equality:
\[
b_m=(-1)^mrac{2\sinlpha}{\cos(3lpha/2)}.
\]
Thus the highest nonredundant frequency on every odd cyclic grid has a closed-form discrete Carathéodory–Fejér constant. In positive-definite-sequence normalization, the sharp value at \(1\) is \(D_m/2\).

## Assumptions and scope
The result concerns real sampled trigonometric polynomials on the cyclic grid of odd order \(N=2m+1\), with \(m\ge4\). The frequency \(m\) is the anti-Nyquist frequency: it is the largest nonredundant positive frequency on \(\mathbb Z_N\). No assertion is made here about arbitrary pairs \((N,m)\), continuous nonnegativity between grid points, or complex nonsymmetric coefficient objectives.

## Proof
Write \(s=(-1)^m\), \(u=\sin(lpha/2)\), and \(v=\sin(3lpha/2)\). At the two grid indices \(j=m\) and \(j=m-1\),
\[
\cos\!\left(rac{2\pi m}{N}ight)=-\coslpha,
\qquad
\cos\!\left(rac{2\pi(m-1)}{N}ight)=-\cos(3lpha),
\]
and
\[
\cos\!\left(rac{2\pi m^2}{N}ight)=s u,
\qquad
\cos\!\left(rac{2\pi m(m-1)}{N}ight)=-s v.
\]
Hence every feasible pair \((a,b)\) satisfies
\[
1-a\coslpha+bsu\ge0,
\qquad
1-a\cos(3lpha)-bsv\ge0.
\]
Multiplying the first inequality by \(v\), the second by \(u\), and adding eliminates \(b\). Since \(u,v>0\),
\[
a\lerac{u+v}{\coslpha\,v+\cos(3lpha)u}.
\]
The identities
\[
u+v=2\sinlpha\cos(lpha/2)
\]
and
\[
\coslpha\,v+\cos(3lpha)u=\sin(2lpha)\cos(3lpha/2)
\]
give
\[
a\le A:=rac{\cos(lpha/2)}{\coslpha\,\cos(3lpha/2)}.
\]

Set
\[
B:=rac{2\sinlpha}{\cos(3lpha/2)}
\qquad	ext{and}\qquad
b=sB.
\]
We now verify every grid inequality. By symmetry it suffices to take \(0\le j\le m\), and write \(r=m-j\) and \(x_r=(2r+1)lpha/2\). Then
\[
\cos\!\left(rac{2\pi j}{N}ight)=-\cos(2x_r),
\qquad
b\cos\!\left(rac{2\pi mj}{N}ight)=(-1)^r B\sin x_r.
\]
Thus the sampled value is
\[
Q_r=1-A\cos(2x_r)+(-1)^rB\sin x_r.
\]
With \(y=\sin x_r\), this becomes one of two quadratics,
\[
q_+(y)=2Ay^2+By+1-A
\]
for even \(r\), and
\[
q_-(y)=2Ay^2-By+1-A
\]
for odd \(r\). Direct substitution gives
\[
q_+\!\left(\sin(lpha/2)ight)=0,
\qquad
q_-\!\left(\sin(3lpha/2)ight)=0.
\]
The polynomial \(q_+\) is strictly increasing for \(y\ge0\), so every even \(r\) gives \(Q_r\ge0\). Also \(A>1\), hence the product of the two roots of \(q_-\) is \((1-A)/(2A)<0\); therefore \(q_-\) has exactly one positive root, namely \(\sin(3lpha/2)\). Every odd \(r\ge1\) has \(\sin x_r\ge\sin(3lpha/2)\), so again \(Q_r\ge0\). Symmetry covers the remaining grid indices. Therefore \((A,sB)\) is feasible and the upper bound is sharp.

If \(a=A\), the positive weighted sum of the two nonnegative contact inequalities used for the upper bound is zero. Both contact inequalities must therefore vanish separately, which forces \(b=sB\). This proves uniqueness of the extremizing higher-harmonic coefficient.

## Verification
The accompanying `verify.py` re-evaluates every sample for \(4\le m\le200\), checks the two exact contact locations numerically, and verifies that the closed form agrees with the solution obtained from those contacts. This finite replay is corroborative only; the universal result is the analytic proof above.

The asymptotic expansion is
\[
D_m=1+rac{3\pi^2}{2(2m+1)^2}+O(m^{-4}),
\]
so the anti-Nyquist sampling gain is explicitly second order in the odd grid size.

## Relationship to prior work
Kolountzakis and Révész formulate both continuous and discretized Carathéodory–Fejér-type extremal problems for prescribed spectral support, providing the framework in which the present odd-cycle problem lives. Krenedits and Révész later develop the corresponding positive-definite formulation on locally compact Abelian groups and recall the Herglotz and Fejér–Riesz equivalences. Those sources do not give the anti-Nyquist closed form above.

The closest indexed results checked here are an exact formula for a fixed third harmonic on arbitrary grids, an exact formula for the degree-two sampled problem, and a general sampling-rigidity theorem for singleton higher harmonics. The first two cover only the low cases corresponding to \(m=3\) and \(m=2\), which are excluded from the stated theorem. The rigidity theorem determines when sampling has no gain over the continuous singleton problem, but it does not determine the exact value or extremizer on the diagonal family \(N=2m+1\).

## Limitations
The theorem is restricted to the anti-Nyquist family \(N=2m+1\) and to real even data. It does not give a formula for general \(N\) and higher harmonic \(k\), nor for continuous positivity on the whole circle. A residual originality risk is that the same diagonal formula may occur in older finite positive-definite or cyclic trigonometric-polynomial literature under different notation; the primary sources and indexed searches inspected for this review did not reveal such a statement.

## References
1. M. N. Kolountzakis and S. Gy. Révész, *On pointwise estimates of positive definite functions with given support*, arXiv:math/0302193v1 (first public version 2003-02-17).
2. S. Krenedits and S. Gy. Révész, *The Carathéodory–Fejér type extremal problem on locally compact Abelian groups*, arXiv:1304.0071v1 (first public version 2013-03-30); Journal of Approximation Theory 194 (2015), 108–131.
