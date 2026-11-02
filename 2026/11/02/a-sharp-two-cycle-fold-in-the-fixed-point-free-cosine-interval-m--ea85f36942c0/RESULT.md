# A sharp two-cycle fold in the fixed-point-free cosine interval map

## Finding
Consider the two-branch cosine map introduced in [1], with the switching point fixed at \(b=1/2\):
\[
F_{a,c}(x)=\begin{cases}
1-(1-a)\cos(\pi x),&0\le x\le 1/2,\\
-c\cos(\pi x),&1/2<x\le1.
\end{cases}
\]
For every \(1/4\le a<1/2\) and \(0<c<1/2\), this map has **no fixed point** and the following is an exact census of its geometrically distinct primitive period-two orbits.

Set \(k=\pi(1-a)\), \(\theta_a=\pi^{-1}\arccos(\pi/(2k))\), and on \((\theta_a,1/2]\) define
\[
C_a(x)=\cos(k\cos(\pi x)),\qquad Q_a(x)=\frac{x}{C_a(x)}.
\]
There is a unique minimizer \(x_*(a)\in(\theta_a,1/2)\), and the sharp threshold \(c_*(a)=Q_a(x_*(a))\) satisfies \(0<c_*(a)<1/2\). Equivalently \(x_*\) is the unique solution of \(C_a(x_*)=x_*C_a'(x_*)\) in that interval. The number \(N_2(a,c)\) of primitive two-cycles is
\[
N_2(a,c)=\begin{cases}
0,&0<c<c_*(a),\\
1,&c=c_*(a),\\
2,&c_*(a)<c<1/2.
\end{cases}
\]
At the threshold, the unique cycle has two-step multiplier \(1\). In the two-cycle region, the one with the smaller left-hand point is repelling (two-step multiplier strictly greater than \(1\)); the one with the larger left-hand point is attracting (two-step multiplier strictly between \(0\) and \(1\)). All cycle points avoid the switching boundary.

The collision is a nondegenerate fold. At fixed \(a\), put \(\delta=c-c_*(a)>0\), \(C_*=C_a(x_*)\), and \(C''_*=C_a''(x_*)<0\). Define
\[
D_a=\sqrt{-\frac{2C_*}{c_*(a)C''_*}}>0,
\qquad B_a=-c_*(a)C''_*D_a>0.
\]
For \(\delta\downarrow0\), the two left-hand cycle coordinates and their return multipliers obey
\[
x_\pm=x_*\pm D_a\sqrt\delta+O_a(\delta),\qquad
\lambda_\pm=1\mp B_a\sqrt\delta+O_a(\delta).
\]
In particular, the separation of the two left-hand coordinates is \(2D_a\sqrt\delta+O_a(\delta)\).

## Assumptions and scope
The state space is the closed real interval \([0,1]\), with the left formula at the switching point. Parameters satisfy \(1/4\le a<1/2\), \(0<c<1/2\), and \(b=1/2\) exactly. A primitive two-cycle is a two-element set \(\{x,y\}\subset[0,1]\) with \(F(x)=y\), \(F(y)=x\), and \(x\ne y\). The multiplier is the derivative of \(F^2\) at either point, taken where both orbit branches are smooth. No assertion is made about periodic orbits of other lengths or global basins.

## Proof
**Fixed-point exclusion and symbolic reduction.** On the left, \(1-\cos(\pi x)\ge2x^2\) for \(0\le x\le1/2\), so
\[
F(x)-x\ge a+2(1-a)x^2-x\ge a-\frac{1}{8(1-a)}\ge\frac1{12}>0.
\]
Here the last inequality holds throughout the stated range, with the minimum at \(a=1/4\). On the right, \(0\le F(x)\le c<1/2<x\). Thus there are no fixed points. Each branch is strictly increasing on its interior; a primitive two-cycle cannot have both points on one branch. Because the right branch maps into \([0,c]\subset[0,1/2)\), any such orbit has unique labels \(0<x<1/2<y<1\), with \(y=1-(1-a)\cos(\pi x)\) and \(x=-c\cos(\pi y)\). The condition \(y>1/2\) is equivalent to \(x>\theta_a\). Substitution reduces the cycle equation to
\[
x=c\cos(k\cos(\pi x))=cC_a(x),\qquad \theta_a<x<1/2,
\]
or \(c=Q_a(x)\). Conversely, every root in this interval yields a smooth primitive two-cycle; because \(c<1/2\), it automatically has \(x=cC_a(x)<1/2\).

**Unique turning point.** On \(\theta_a<x<1/2\), the function \(C_a\) is positive and has derivative
\[
C_a'(x)=k\pi\sin(\pi x)\sin(k\cos(\pi x))>0.
\]
Its second derivative is
\[
C_a''(x)=k\pi^2\left[\cos(\pi x)\sin(k\cos(\pi x))-k\sin^2(\pi x)\cos(k\cos(\pi x))\right].
\]
Set \(t=\cos(\pi x)\), decreasing from \(\pi/(2k)\) to \(0\). Since \(\cos(kt)>0\), the sign of \(C_a''\) is the sign of
\[
\Psi(t)=t\tan(kt)-k(1-t^2).
\]
The derivative \(\Psi'(t)=\tan(kt)+kt\sec^2(kt)+2kt\) is strictly positive, while \(\Psi(0)=-k<0\) and \(\Psi(t)\to+\infty\) as \(t\uparrow\pi/(2k)\). Thus \(C_a''\) changes exactly once, from positive to negative, as \(x\) increases.

Write \(H(x)=C_a(x)-xC_a'(x)\). Then \(Q_a'=H/C_a^2\) and \(H'=-xC_a''\). At the lower endpoint, \(H(\theta_a^+)=-\theta_a C_a'(\theta_a)<0\). At the upper endpoint, \(H(1/2)=1>0\). Because \(H\) first decreases and then strictly increases, it has exactly one zero \(x_*\), lying in the region \(C_a''<0\). Therefore \(Q_a\) strictly decreases and then strictly increases. Its boundary limits are \(Q_a(\theta_a^+)=+\infty\), \(Q_a(1/2)=1/2\); its unique minimum satisfies \(c_*<1/2\). A horizontal line \(c\in(0,1/2)\) consequently has zero, one or two intersections, exactly as claimed.

**Stability and fold coefficient.** On a two-cycle, its two-step multiplier is
\[
\lambda=F'(x)F'(y)=cC_a'(x)>0.
\]
Since \(c=Q_a(x)\), we have \(1-\lambda=H(x)/C_a(x)\). The lower root is on the decreasing side of \(Q_a\), hence \(\lambda>1\); the upper is on its increasing side, hence \(0<\lambda<1\). At \(x=x_*\), the multiplier is exactly one. Finally, Taylor expansion of \(cC_a(x)-x=0\) at \((x_*,c_*)\), using \(\partial_c(cC_a-x)=C_*>0\), \(\partial_x(cC_a-x)=0\), and \(\partial_x^2(cC_a-x)=c_*C''_*<0\), gives the two square-root branches with coefficient \(D_a\) above. Expanding \(cC_a'(x)\) on these branches gives \(\lambda_\pm=1\mp B_a\sqrt\delta+O_a(\delta)\).

## Verification
The standalone Python script `verify_cosine.py` implements the original two-branch map, independently reconstructs its return equation and roots, checks the complete period-two root count by dense sign scans at five parameter slices, compares direct full-map returns and derivatives with the reduction, and checks the square-root coefficients near each fold. It passed for \(a=0.25,0.30,0.37,0.45,0.49\). These finite computations are checks, not the proof of uniqueness or the all-parameter theorem. Example: at \(a=1/4\), \(x_*\approx0.461129385880\) and \(c_*\approx0.480797079833\).

## Relationship to prior work
The cosine example is Equation (20) of Lawnik, Moysis and Volos [1], which presents numerical phase diagrams, fixed-point regions and Lyapunov indicators, rather than an exact global primitive-two-cycle census or the analytic fold and multipliers proved here. The later paper [2] uses a transformation of logistic/tent-type functions to construct other no-fixed-point maps; its abstract and accessible publisher preview do not establish the present cosine-specific threshold. Generic saddle-node theory describes the local normal form once nondegeneracy is known, but does not imply the global uniqueness of the fold or the present explicit return function.

## Limitations
The parameter restrictions are substantive: the symmetric switching location, the stated fixed-point-free gain interval and the right-branch subcritical image bound enable exhaustive symbolic reduction. This is not a classification of all parameter values or of periods above two. At the threshold the multiplier is neutral, not attracting or repelling in the hyperbolic sense. The later related paper [2] was accessible only through its abstract and opening publisher preview: its openly listed accepted-manuscript PDF returned an access-denial response. Additional unindexed analyses may overlap with this exact threshold; publication priority has not been independently established.

## References
[1] M. Lawnik, L. Moysis, C. Volos, “A Family of 1D Chaotic Maps without Equilibria,” *Symmetry* **15** (2023), 1311, published 27 June 2023, doi:10.3390/sym15071311 (Equation (20), Section 4.2; accessible full text).

[2] M. Lawnik, L. Moysis, M. S. Baptista, C. Volos, “Discrete one-dimensional piecewise chaotic systems without fixed points,” *Nonlinear Dynamics* **112** (2024), 6679–6693, doi:10.1007/s11071-024-09349-6 (abstract and publisher preview inspected).
