# Exact two-cycle cusp, bistability, and global convergence in a fixed-point-free quadratic map

## Finding

The quadratic specialization of the fixed-point-free piecewise family introduced in [1] has an exact two-parameter census of primitive period-two orbits, a region of two coexisting attracting cycles, and a codimension-two parabolic cusp with a sharp algebraic relaxation law. No other periods occur, and every forward orbit approaches a period-two cycle.

For parameters \(1/2<a<1\) and \(0<c<1/2\), set \(k=1-a\). Define
\[
F_{a,c}(x)=\begin{cases}
1-k(1-2x)^2,&0\le x\le1/2,\\
c(2x-1)^2,&1/2<x\le1.
\end{cases}
\]
For \(3/8<k<1/2\), put
\[
u_{\pm}(k)=\frac{2\pm\sqrt{4-3/(2k)}}{3},\qquad
c_{\pm}(k)=\frac{(4-3u_{\pm}(k))^2}{32(1-u_{\pm}(k))}.
\]
Here \(0<c_-(k)<c_+(k)\); compare these thresholds with the allowed \(0<c<1/2\).

The number \(N_2\) of geometrically distinct primitive two-cycles is exactly
\[
N_2(k,c)=\begin{cases}
3,&3/8<k<1/2\text{ and }c_-(k)<c<c_+(k),\\
2,&3/8<k<1/2\text{ and }c\in\{c_-(k),c_+(k)\},\\
1,&\text{otherwise}.
\end{cases}
\]
Whenever three cycles occur, the two outer cycles are hyperbolic attractors separated by a hyperbolic repelling cycle. At a two-cycle fold, the double cycle is parabolic and semistable; the remaining cycle is a hyperbolic attractor. The limits of every orbit are described below, including fold and cusp parameters.

At the cusp \((a,c)=(5/8,3/8)\), the only primitive two-cycle is
\[\frac16\longleftrightarrow\frac56.\]
If \(u_n\) denotes the normalized left-coordinate of the \(n\)-th two-step return and \(u_0\ne2/3\), then
\[
\lim_{n\to\infty}\sqrt n\left(u_n-\frac23\right)
=\operatorname{sgn}\left(u_0-\frac23\right)\frac23.
\]
In particular the physical left-point deviation satisfies \(\lvert x_{2n}-1/6\rvert\sim1/(3\sqrt n)\), whenever the original initial point is in the left half and is not on the cycle.

A rational bistability witness is \((a,c)=(9/16,7/16)\). Its three two-cycles correspond to left-coordinate roots
\[
\frac{4-2\sqrt2}{7},\quad\frac{-4+6\sqrt2}{7},\quad\frac{4+2\sqrt2}{7};
\]
the outer two have exact two-step multiplier \(1/2\), while the middle one is repelling.

## Assumptions and scope

The state space is the closed real interval \([0,1]\). The left branch includes \(1/2\), while the right branch excludes it. The parameters obey the strict inequalities \(1/2<a<1\) and \(0<c<1/2\), so that left points map strictly to the right half and right points strictly to the left half. A primitive two-cycle means an unordered pair of two distinct points interchanged by \(F_{a,c}\). Stability refers to the multiplier of the two-step return restricted to its interval, rather than to any numerical Lyapunov estimate. All statements concern the exact real map, not finite-precision arithmetic or stochastic perturbations.

## Proof

**1. Alternation and the scalar return.** Since \(F_{a,c}([0,1/2])\subset(1/2,1]\) and \(F_{a,c}((1/2,1])\subset[0,c]\subset[0,1/2)\), every trajectory alternates strictly between the two halves. On each left visit define \(u=1-2x\in[0,1]\). One left-to-right-to-left return becomes
\[
G_{k,c}(u)=1-2c(1-2ku^2)^2.
\]
The function \(G_{k,c}\) continuously maps \([0,1]\) into itself and is strictly increasing: \(G'_{k,c}(u)=16cku(1-2ku^2)\ge0\), with strict positivity for \(u>0\). Every orbit of a continuous increasing interval map is monotone from its first iterate onward: the sign of \(G(u)-u\) cannot reverse along an orbit. Thus it converges to a fixed point of \(G\). The same monotonicity prohibits periodic points of \(G\) of period greater than one, so \(F\) has no periodic orbit other than a primitive two-cycle. A right-half initial point enters the left half in one step. The fixed-point-free property of \(F\) follows immediately from strict alternation.

**2. Exact count by a fold curve.** Solving \(G_{k,c}(u)=u\) for \(c\) yields
\[
c=C_k(u):=\frac{1-u}{2(1-2ku^2)^2},\quad
C_k(0)=\frac12,\quad C_k(1)=0.
\]
The denominator is positive on \([0,1]\) because \(0<k<1/2\). Direct differentiation gives
\[
C'_k(u)=\frac{-1+8ku-6ku^2}{2(1-2ku^2)^3}.
\]
The quadratic numerator is nonpositive everywhere if \(k\le3/8\), vanishing only at \((k,u)=(3/8,2/3)\). Hence every horizontal level \(c\in(0,1/2)\) is attained exactly once for \(k\le3/8\).

If \(3/8<k<1/2\), the derivative vanishes exactly at \(u_-(k)\) and \(u_+(k)\), both in \((0,1)\). The signs of \(C'_k\) on the three complementary intervals are negative, positive, and negative. Substituting the critical identity \(k=1/[2u(4-3u)]\) into \(C_k(u)\) gives \(c_\pm(k)=(4-3u_\pm)^2/[32(1-u_\pm)]\). Since the curve has one strict minimum and one strict maximum, intersection with a horizontal line in \((0,1/2)\) has exactly three roots between those heights, two at either height (one tangency plus one transverse intersection), and one otherwise. This proves the census. The upper fold lies above the permissible \(c\)-strip when \(k>27/64\), and touches its boundary at \(k=27/64\); the stated min/max test already handles that case.

**3. Stability and basins.** At a fixed point \(u\), differentiating \(G_{k,c}(u)-u=2(1-2ku^2)^2(C_k(u)-c)\) gives
\[
G'_{k,c}(u)-1=2(1-2ku^2)^2 C'_k(u).
\]
Therefore roots on the decreasing segments satisfy \(0\le G'<1\) and are hyperbolically attracting, while roots on the increasing segment satisfy \(G'>1\) and are hyperbolically repelling. The fold fixed points have \(G'=1\), with quadratic tangency and one-sided attraction. Because \(G\) is increasing, each initial point in an interval between consecutive fixed points moves monotonically to the appropriate endpoint. In the three-cycle region the repelling middle root is the exact separator of the two basins, while the repelling orbit itself remains stationary under the return. At either fold, this monotone-iteration rule also gives convergence for every orbit (the neutral fold attracts from precisely one side).

**4. Cusp and critical clock.** Both fold branches merge at \(k=c=3/8\), \(u=2/3\). Exact polynomial division gives
\[
G_{3/8,3/8}(u)-u=-\frac{(u+2)(3u-2)^3}{64}.
\]
Thus the fixed point is unique, it attracts from both sides, and \(u=2/3\) corresponds to \(x=(1-u)/2=1/6\), whose image is \(5/6\). Writing \(v_n=u_n-2/3\), one obtains the exact, not truncated, recurrence
\[
v_{n+1}=v_n-\frac98v_n^3-\frac{27}{64}v_n^4.
\]
By monotone convergence \(v_n\to0\), and \(v_n\) keeps the sign of \(v_0\). For nonzero \(v_n\), the reciprocal-square difference obeys
\[
\frac1{v_{n+1}^2}-\frac1{v_n^2}=\frac94+O(v_n).
\]
Cesàro averaging gives \(1/(n v_n^2)\to9/4\), hence the signed limit \(\sqrt n\,v_n\to\pm2/3\). The statement for \(x_{2n}\) follows from \(x=(1-u)/2\).

**5. An exact two-attractor witness.** At \(k=c=7/16\), the return fixed-point polynomial factors as
\[
G_{7/16,7/16}(u)-u
=-\frac{(7u^2+8u-8)(49u^2-56u+8)}{512}.
\]
The three listed roots lie strictly inside \((0,1)\) and exhaust the roots there. Direct differentiation gives multiplier \(1/2\) at both outer roots. The intermediate root is on the increasing segment of \(C_k\), hence its multiplier exceeds one. Two disjoint open attracting basins therefore coexist in a map having no fixed points.

## Verification

A standalone Python/SymPy script `verify_quadratic_cycles.py` checks the exact return conjugacy, derivative, fold parameterization, cusp factorization, critical quartic recurrence, rational two-attractor witness and multipliers. It also uses exact Sturm root counts on 800 rational parameter samples, with two numerical iterates of 250,000 returns as diagnostics of the cusp asymptotic. The script executed successfully with the output `PASS: return conjugacy, fold, cusp, exact three two-cycle witness, 800 rational parameter samples, critical-rate diagnostics`. The interval-wide result is proved by the monotonicity and calculus arguments above; finite tests alone cannot certify it.

## Relationship to prior work

Lawnik, Moysis and Volos [1] defined this piecewise-polynomial family in their equation (15), established the absence of fixed points for powers at least one, and displayed phase, Lyapunov and parameter diagrams for its quadratic specialization. Their inspected derivations and figures do not present the exact three/one/two primitive-cycle census, the two distinct sinks at the rational witness, or the cubic parabolic return law. The fractional-power fixed-point phase diagram of the same family treats a different exponent regime and a different invariant, and does not imply this theorem. Classical bifurcation studies of piecewise-smooth unimodal maps, including [2], discuss coexistence and border collisions in other map families; they do not supply the explicit global return or the present cusp and critical-rate formulas. A related 2024 fixed-point-free mapping paper [3] describes different constructions in its abstract; its full text could not be inspected, which is a residual priority risk.

## Limitations

The theorem applies only to the quadratic exponent, equal midpoint partition and the stated strict parameter rectangle. It does not characterize the larger family with general power or partition, does not establish noise or rounding robustness, and does not assert cryptographic security. The exceptional neutral cusp and fold are not uniformly exponentially attracting. Some potentially related later full texts were inaccessible, so the priority assessment is limited to the material actually examined; independent mathematical audit has not been performed.

## References

[1] M. Lawnik, L. Moysis, and C. Volos, *A Family of 1D Chaotic Maps without Equilibria*, Symmetry **15** (2023), article 1311, first published 27 June 2023, DOI: 10.3390/sym15071311. https://doi.org/10.3390/sym15071311

[2] I. Sushko, A. Agliari, and L. Gardini, *Bistability and border-collision bifurcations for a family of unimodal piecewise smooth maps*, Discrete Contin. Dyn. Syst. B **5** (2005), 881–897, DOI: 10.3934/dcdsb.2005.5.881. https://doi.org/10.3934/dcdsb.2005.5.881

[3] M. Lawnik, L. Moysis, M. S. Baptista, and C. Volos, *Discrete one-dimensional piecewise chaotic systems without fixed points*, Nonlinear Dynamics **112** (2024), 6679–6693, DOI: 10.1007/s11071-024-09349-6. https://doi.org/10.1007/s11071-024-09349-6
