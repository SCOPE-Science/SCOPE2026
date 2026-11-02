# Exact stable-fixed-point onset and a square-root cusp in the cosine-skewed interval map

## Finding

The cosine-skewed piecewise map of Moysis, Lawnik, Volos, Baptista, and Goudos (2023), with endpoint parameter \(c=0\), has an exact two-parameter boundary separating **one fixed point from three**, and separating **no attracting fixed point from exactly one**. The critical curve is strictly increasing and concave and develops a square-root cusp as the left endpoint parameter tends to zero. Its birth of a stable/unstable fixed-point pair has explicit square-root splitting and multipliers.

Put \(v=e^{-1}\), \(D=\cos(v)-\cos(1)>0\), and
\[
H(s)=\frac{\cos(v)-\cos(e^{s-1})}{D},\qquad 0\le s\le1.
\]
For \(0<\alpha<1\), the equation
\[
s_\alpha H'(s_\alpha)-H(s_\alpha)=\alpha
\]
has exactly one solution \(s_\alpha\in(0,1)\). Set
\[
b_*(\alpha)=H(s_\alpha)+(1-s_\alpha)H'(s_\alpha).
\]
For the map \(G_{\alpha,b}\) defined below, the number of *distinct* real fixed points in \([0,1]\) is exactly
\[
\#\operatorname{Fix}(G_{\alpha,b})=
\begin{cases}1,&0<b<b_*(\alpha),\\
2,&b=b_*(\alpha),\\
3,&b_*(\alpha)<b<1.
\end{cases}
\]
For \(b<b_*\), the sole fixed point is repelling. At equality an additional neutral fixed point of multiplier \(+1\) exists. For \(b>b_*\), **exactly one fixed point is attracting and the other two are repelling**. The attracting and an additional repelling fixed point belong to the left branch; the right-branch fixed point exists and repels for every parameter pair.

The curve obeys
\[
\frac{db_*}{d\alpha}=\frac{1-s_\alpha}{s_\alpha}>0,
\qquad
\frac{d^2b_*}{d\alpha^2}=-\frac{1}{s_\alpha^3H''(s_\alpha)}<0,
\]
and has the sharp singular endpoint expansion
\[
b_*(\alpha)=H'(0)+\sqrt{2H''(0)\alpha}+O(\alpha),\quad\alpha\downarrow0.
\]
In particular, \(H'(0)=0.3368297160059126\ldots\), \(\sqrt{2H''(0)}=1.1474541948122587\ldots\), and \(b_*(1/2)=0.9178276907017725\ldots\).

For fixed \(\alpha\in(0,1)\) and \(\delta=b-b_*(\alpha)\downarrow0\), the two left fixed points \(x_-<x_+\), expressed with \(x_\pm=b s_\pm\), have
\[
s_\pm=s_\alpha\pm\sqrt{\frac{2s_\alpha}{H''(s_\alpha)}}\sqrt\delta+O_\alpha(\delta),
\qquad
G'_{\alpha,b}(x_\pm)=1\pm
\frac{\sqrt{2s_\alpha H''(s_\alpha)}}{b_*(\alpha)}\sqrt\delta
+O_\alpha(\delta).
\]
Thus the lower-coordinate member of the pair is attracting and the upper-coordinate member repelling; the collision is an ordinary nondegenerate saddle-node.

## Assumptions and scope

Take arbitrary real parameters \(0<\alpha,b<1\). The map is the continuous self-map of \([0,1]\)
\[
G_{\alpha,b}(x)=
\begin{cases}
H(x/b)+\alpha(1-x/b),&0\le x\le b,\\
H((1-x)/(1-b)),&b<x\le1.
\end{cases}
\]
Here \(H(0)=0\), \(H(1)=1\), \(H'>0\), and \(H''>0\) on \([0,1]\). Convexity gives \(0\le H(s)\le s\), and hence both pieces map into \([0,1]\), meeting at value \(1\) at \(x=b\). At the open-interval parameter boundaries \(\alpha=0\) and \(b=1\), fixed points can sit at endpoints or the branch description degenerates; these boundaries are not included. No statement is made about higher-period orbits, invariant densities, global basins, or positive Lyapunov exponents.

## Proof

**Shape.** With \(w=e^{s-1}\in[e^{-1},1]\), direct differentiation gives
\[
H'(s)=\frac{w\sin w}{D}>0,
\qquad
H''(s)=\frac{w\sin w+w^2\cos w}{D}>0.
\]
This proves strict increase and strict convexity. We also use the elementary, rigorously bracketable inequalities \(H'(1)>2\), \(H'(1)<2+H'(0)\), \(H(3/5)+3/5<1\), and \(H'(3/5)>1\). For example, these follow from \(0.39278<D<0.39280\), \(0.3368<H'(0)<0.3369\), \(2.1422<H'(1)<2.1424\), \(H(3/5)+3/5<0.981\), and \(H'(3/5)>1.06\). Such strict rational-decimal enclosures are obtained from the alternating Taylor bounds for \(\sin\) and \(\cos\), with \(2.71828<e<2.71829\); only the weaker inequalities are used below.

**The right branch.** Writing \(s=(1-x)/(1-b)\), its fixed-point equation is \(H(s)+(1-b)s=1\), whose left-hand side strictly increases from \(0\) to \(2-b>1\). Thus exactly one right fixed point exists, with \(0<s<1\). Let \(q\) be the unique solution of \(H(q)+q=1\). The above bounds imply \(q>3/5\) and \(H'(q)>1\). Since \(b>0\), the right fixed point has \(s>q\), and its multiplier satisfies \(G'(x)=-H'(s)/(1-b)<-1\). It is always repelling.

**The left branch and the sharp curve.** Let \(s=x/b\), and subtract the fixed-point equation to obtain
\[
Q_{\alpha,b}(s)=H(s)+\alpha-(\alpha+b)s=0.
\]
The function is strictly convex, with \(Q(0)=\alpha>0\) and \(Q(1)=1-b>0\). Define \(A(s)=sH'(s)-H(s)\), \(B(s)=H(s)+(1-s)H'(s)\). Their derivatives are \(A'(s)=sH''(s)>0\) and \(B'(s)=(1-s)H''(s)>0\) in \((0,1)\), while \(A(0)=0\), \(A(1)=H'(1)-1>1\), \(B(0)=H'(0)\), and \(B(1)=1\). Every \(\alpha\in(0,1)\) therefore gives unique \(s_\alpha\in(0,1)\), and \(0<b_*(\alpha)<1\). The identities \(\alpha=A(s_\alpha)\) and \(b_*=B(s_\alpha)=H'(s_\alpha)-\alpha\) imply
\[
Q_{\alpha,b_*}(s_\alpha)=Q'_{\alpha,b_*}(s_\alpha)=0.
\]
Strict convexity makes \(Q_{\alpha,b_*}(s)\ge0\), with equality only at \(s_\alpha\). The exact comparison \(Q_{\alpha,b}(s)=Q_{\alpha,b_*}(s)+(b_*-b)s\) proves no left roots for \(b<b_*\); one double root for equality; and exactly two simple roots for \(b>b_*\), since the endpoint values remain positive and the value at \(s_\alpha\) becomes negative. The right-branch root is distinct from all left roots.

**Stability.** At a left fixed point, \(G'(bs)-1=Q'_{\alpha,b}(s)/b\). The upper root has \(Q'>0\), hence multiplier greater than \(1\). The lower root has multiplier less than \(1\). It is also greater than \(-1\): strict convexity yields \(H'(s)\ge H'(0)\), and
\[
b_*(\alpha)-\alpha+H'(0)
=\bigl[(1-2s)H'(s)+2H(s)+H'(0)\bigr]_{s=s_\alpha}>0.
\]
Indeed, the bracketed expression has derivative \((1-2s)H''(s)\), so its minimum on \([0,1]\) occurs at an endpoint; those values are \(2H'(0)>0\) and \(2-H'(1)+H'(0)>0\). Since \(b>b_*\), it follows that \(G'(bs)>[H'(0)-\alpha]/b>-1\). Thus the lower root is locally attracting for every \(b>b_*\). At the fold, the multiplier is \(1\).

**Geometry and onset.** Implicit differentiation of \(A(s_\alpha)=\alpha\) and \(B(s_\alpha)=b_*\) gives the stated first and second derivatives. At zero, Taylor's theorem gives \(A(s)=H''(0)s^2/2+O(s^3)\) and \(B(s)=H'(0)+H''(0)s+O(s^2)\), establishing the square-root cusp. Finally, put \(s=s_\alpha+u\) and \(b=b_*+\delta\). Then
\[
Q_{\alpha,b}(s)=\tfrac12 H''(s_\alpha)u^2-s_\alpha\delta+O(u^3+|u|\delta).
\]
Solving the two simple branches for \(\delta>0\) yields the stated root separation and, by expanding \(G'(bs)=\{H'(s)-\alpha\}/b\), the two multiplier expansions. The positive second derivative and nonzero parameter derivative \(\partial_b Q=-s_\alpha\) prove nondegeneracy.

## Verification

The standalone `certify_bounds.py` proves the five strict decimal enclosures used for the derivative signs by exact rational alternating Taylor bounds, without floating point. The accompanying standalone `verify.py` evaluates the defining transcendental functions with 60-digit arithmetic, checks the tangent and critical-curve equations, counts left roots above and below the curve, verifies right-branch repulsion, and tests the square-root onset for five values of \(\alpha\). It passes 1316 assertions. These finite calculations verify examples and numerical constants but **do not certify** the universal quantifiers; those follow from strict convexity, the exact branch comparison, and the derivative bounds in the proof. Run with `python certify_bounds.py` (standard library) and `python verify.py` (uses `mpmath`).

## Relationship to prior work

Moysis, Lawnik, Volos, Baptista, and Goudos, *Chaotic Maps with Tunable Mean Value—Application to a UAV Surveillance Mission* (2023), Equation (4), introduce exactly this cosine-skewed family before selecting \(c=0\) for numerical experiments. Their Sections 3.2 and 3.6 show numerical period-one and chaos regions versus the shape parameters but give no exact full two-parameter fixed-point census, global attracting-fixed-point boundary, critical-curve concavity, or endpoint cusp. Their earlier 2023 MOCAST conference account describes the broader piecewise-map concept; the accessible abstract does not establish the present cosine-family fixed-point theorem. General one-dimensional saddle-node calculus explains the *local* square-root exponent but not the specific all-parameter curve or the exhaustive count in this concrete piecewise family. A different published fixed-point classification concerns the distinct fractional-power discontinuous map of Lawnik–Moysis–Volos; it does not cover the present continuous cosine-skewed interpolation.

## Limitations

The result concerns only the \(c=0\) cosine-skewed map with \(0<\alpha,b<1\). It does not provide a classification of higher-period trajectories, ergodic averages, or global attracting basins. The paper's numerical bifurcation pictures are consistent with, but do not establish, these formulas. A complete text of the 2023 conference precursor was unavailable; a concealed equivalent derivation in that text or unindexed earlier literature remains a priority risk. No independent mathematical audit has been performed.

## References

1. L. Moysis, M. Lawnik, C. Volos, M. S. Baptista, and S. K. Goudos, *Chaotic Maps with Tunable Mean Value—Application to a UAV Surveillance Mission*, Symmetry **15** (2023), 2138. DOI: 10.3390/sym15122138. Published 2023-12-01. Equation (4) and Sections 3.2, 3.6.
2. L. Moysis, M. Lawnik, M. S. Baptista, S. K. Goudos, and C. Volos, *Construction of Piecewise Chaotic Maps With Tunable Statistical Mean*, MOCAST (2023), DOI: 10.1109/MOCAST57943.2023.10176612. Conference dates 2023-06-28 through 2023-06-30; only abstract and metadata accessible.
3. M. Lawnik, L. Moysis, and C. Volos, *A Family of 1D Chaotic Maps without Equilibria*, Symmetry **15** (2023), 1311, DOI: 10.3390/sym15071311. Its underlying piecewise construction is distinct.
