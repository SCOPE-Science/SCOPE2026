# Sharp nonsymmetric first-order stability at the equilateral pentagon trapezoid

## Finding

There is a *sharp two-direction, nonsymmetric local law* for the total distance of equilateral convex pentagons divided by their minimum width, at the degenerate marked trapezoid predicted by Audet and Ninin. Put \(Q(P)=S(P)/w(P)\), where \(S(P)\) is the sum of distances over the ten unordered pairs of the five marked vertices, and \(w(P)\) is Euclidean minimum width. If the two local angular coordinates are \(\delta\ge0\) and \(\alpha\in\mathbb R\), let \(r=\delta+|\alpha|\), \(m=\max\{\delta,\alpha,\delta-\alpha\}\), and \(A=6+4\sqrt3/3\). Then

\[
Q(\delta,\alpha)=4+6\sqrt3-[A m-\delta]+O(r^2),\qquad r\downarrow0.
\tag{1}
\]

This is uniform over all admissible approach directions. The sharp bound

\[
A m-\delta\ge K r,\qquad K=\frac52+\frac{2\sqrt3}{3},
\tag{2}
\]

has equality for every ray \(\alpha=\delta\ge0\), and only on that ray for nonzero directions. Thus \(P(0,0)\) is a strict local maximizer **even without reflection symmetry**. For every \(\varepsilon>0\), all sufficiently small admissible nonzero perturbations satisfy \(Q(0,0)-Q(\delta,\alpha)\ge(K-\varepsilon)r\); no larger angular \(\ell^1\)-coefficient works.

## Assumptions and scope

Five labeled vertices are arranged cyclically around a nondegenerate Euclidean convex polygon, consecutive side lengths are one, and weakly convex configurations with straight turns are allowed. The limiting reference has vertices

\[
p_0=(0,0),\ p_1=(1,0),\ p_2=(2,0),\ p_3=(3/2,\sqrt3/2),\ p_4=(1/2,\sqrt3/2).
\]

Only the turn at \(p_1\) is straight. Rigid motion makes the first directed edge \(e_0\) point along the positive horizontal axis. The next two edge directions are \(\theta_1=\delta\) and \(\theta_2=2\pi/3+\alpha\). Near \((\delta,\alpha)=(0,0)\), the remaining two directions \(\theta_3,\theta_4\) are the *unique smooth branch* of unit-edge closure with initial values \(\pi,4\pi/3\); see the proof. Near the reference all turns except \(\delta\) are strictly positive, so the admissible coordinate region is exactly \(\delta\ge0\). This gives a genuine local chart of the whole two-dimensional equilateral-pentagon shape space, including asymmetric configurations, modulo rigid motions and fixed cyclic marking.

The angular \(\ell^1\) modulus in (2) is coordinate-dependent by definition; its exact value refers to these specified natural edge-angle coordinates. The full directional formula (1) is the intrinsic geometric content of the local calculation.

## Proof

**1. Smooth closure and the chart.** Set \(e(\theta)=(\cos\theta,\sin\theta)\), \(e_0=e(0)\), \(e_1=e(\delta)\), and \(e_2=e(2\pi/3+\alpha)\). Let \(R=-e_0-e_1-e_2\), \(\phi=\operatorname{atan2}(R_y,R_x)\), and \(\beta=\arccos(|R|/2)\). As \(|R(0,0)|=\sqrt3<2\), these are locally well-defined and smooth for the branch of \(\phi\) near the reference. Define

\[
e_3=e(\phi-\beta),\qquad e_4=e(\phi+\beta).
\]

Their sum is \(R\), and at the reference their directions are \(\pi,4\pi/3\). The two unknown closing directions are locally unique: the Jacobian determinant for their two closure equations equals \(\sin(\theta_4-\theta_3)=\sin(\pi/3)\ne0\). The five vertices \(p_0=0\), \(p_j=\sum_{k<j}e_k\) for \(1\le j\le4\) form the desired closed unit-edge chain. The strict angle gaps at other four vertices persist near the reference, proving the assertion that convexity is exactly \(\delta\ge0\) locally.

**2. Linearized vertices and distances.** Differentiating the closure equations gives

\[
\mathrm d\theta_3=\mathrm d\delta-\mathrm d\alpha,\qquad \mathrm d\theta_4=\mathrm d\alpha.
\]

Put \(h=\sqrt3/2\). The vertex linearizations are

\[
\begin{aligned}
\mathrm dp_0&=\mathrm dp_1=(0,0),&\mathrm dp_2&=(0,\delta),\\
\mathrm dp_3&=(-h\alpha,\delta-\alpha/2),&\mathrm dp_4&=(-h\alpha,\alpha/2).
\end{aligned}
\tag{3}
\]

All ten pairwise distances are positive at the reference, hence smooth nearby. Five adjacent pair distances are constant one, and among the remaining five the only nonzero linear variations are

\[
\begin{aligned}
\mathrm d|p_0-p_3|&=\delta/2-\alpha,\\
\mathrm d|p_1-p_3|&=h(\delta-\alpha),\\
\mathrm d|p_1-p_4|&=h\alpha,\\
\mathrm d|p_2-p_4|&=\alpha-\delta/2.
\end{aligned}
\]

(The fifth is \(|p_0-p_2|\), with zero variation.) The terms cancel to

\[
S(\delta,\alpha)=S_0+h\delta+O(r^2),\qquad S_0=9+2\sqrt3.
\tag{4}
\]

**3. Active supporting widths.** For any convex polygon, minimum width occurs perpendicular to at least one edge: between consecutive edge-normal directions, the maximizing and minimizing support vertices are fixed, and the positive width is a sinusoid with second derivative equal to minus itself, so it has no interior local minimum. Therefore it suffices to check the five normal directions of edges \(e_0,\ldots,e_4\). At the reference, the edge-normal widths for indices \(0,1,3\) equal \(h\); indices \(2,4\) have width \(\sqrt3=2h\) and remain inactive nearby.

For edge \(e_0\) the upper support is whichever of \(p_3,p_4\) has larger height, and the lower support is \(p_0\) or \(p_1\), giving

\[
w_0=h+\delta/2+|\delta-\alpha|/2+O(r^2).
\]

For \(e_1\), lower support occurs at \(p_1\) or \(p_2\) and upper support at \(p_3\) or \(p_4\), giving

\[
w_1=h+\delta/2+|\alpha|/2+O(r^2).
\]

For \(e_3\), the upper support is the largest projection among \(p_0,p_1,p_2\), and the lower occurs at \(p_3\) or \(p_4\). The linearization is

\[
w_3=h+\delta/2+\max\{0,-\alpha,\alpha-\delta\}+O(r^2).
\]

The errors are uniform in the admissible half-plane, since all supporting projections are maxima and minima of finitely many smooth functions. Taking their minimum and splitting into \(\alpha<0\), \(0\le\alpha\le\delta\), \(\alpha>\delta\) yields respectively the active widths \(w_1,w_3,w_0\), and exactly

\[
w(\delta,\alpha)=h+\frac12\max\{\delta,\alpha,\delta-\alpha\}+O(r^2).
\tag{5}
\]

This nonsmooth maximum is essential: discarding any of the three active support families gives the wrong angular stability law.

**4. Quotient and sharpness.** Using (4)–(5), \(S_0/h=4+6\sqrt3\), and \(S_0/(2h^2)=(2/3)S_0=A\), division proves (1). To prove (2), split the same three regions. If \(0\le\alpha\le\delta\), then \(m=\delta\) and \(A m-\delta=(A-1)\delta\ge(A-1)(\delta+\alpha)/2\). If \(\alpha\ge\delta\), then \(m=\alpha\) and

\[
(A\alpha-\delta)-\frac{A-1}{2}(\delta+\alpha)=\frac{A+1}{2}(\alpha-\delta)\ge0.
\]

If \(\alpha\le0\), then \(m=\delta-\alpha=r\), so \(A m-\delta\ge(A-1)r\). As \(A>1\), the loss is strictly positive except at the origin, and (1) yields a strict local maximum. Equality in (2), among nonzero admissible directions, holds only when \(\alpha=\delta>0\). Such perturbations have strictly positive turns at all five vertices and are genuinely convex, so taking \(\delta=\alpha\downarrow0\) proves the coefficient optimal. The quadratic remainder is uniform, completing all quantifiers.

## Verification

The standalone `verify.py` constructs the five sides using the exact smooth-closure formula, measures all ten pairwise distances directly from vertices, and computes the minimum of five independently evaluated edge-normal support widths. It checks the three expansions in (1), (4), (5) over 45 parameter-scale samples spanning every active-width chamber and boundary, as well as the linear sharp coefficient. Running `python verify.py` prints `VERIFY_OK`. The sampled calculations are diagnostic only; the proof for *every sufficiently close admissible pentagon* is the analytic four-step argument above.

## Relationship to prior work

Audet and Ninin's 2010 working paper gives sharp bounds for perimeter, diameter, and area of equilateral unit-width convex polygons. Its later journal text, Section 4, introduces the **total vertex-distance** question, reports numerical optimization for odd polygon sizes, and conjectures a trapezoidal extremizer (Conjecture 9). Their numerics do not supply a full asymmetric local derivative or a strict angular stability coefficient.

An existing theorem for **reflection-symmetric** equilateral pentagons gives the sharp global value \(4+6\sqrt3\) in that restricted one-dimensional family. It does not assert an inequality for nonsymmetric pentagons, nor determine which of three competing edge-support widths becomes active under nonsymmetric perturbations, nor imply (1)–(2). The current theorem genuinely uses both independent shape coordinates and thereby excludes asymmetric *local* improving perturbations; it does not establish the global conjecture.

Dumitrescu's 2013 metric inequalities for polygons concern vertex-distance sums subject to a **perimeter** condition. Their statements do not determine the present **minimum-width-normalized** local first variation. Existing geometric phase treatments of equilateral pentagons discuss their moduli and kinematics, not the width-normalized extremal loss derived here.

## Limitations

This is a **local** theorem near one weakly convex, five-marked-vertex configuration. It does not prove that arbitrary convex equilateral pentagons satisfy \(Q\le4+6\sqrt3\), nor does it address more than five vertices. The stability constant is sharp specifically for the declared angular \(\ell^1\) coordinate metric; no global Hausdorff stability estimate is claimed. The primary conclusion is at first order with a uniform second-order remainder, not an exact formula at finite perturbations. An unindexed prior equivalent local analysis remains a possible priority risk. No independent audit is claimed.

## References

1. C. Audet and J. Ninin, *Maximal Perimeter, Diameter and Area of Equilateral Unit-Width Convex Polygons*, working paper G-2010-37, dated 8 June 2010. https://www.gerad.ca/en/papers/G-2010-37 ; https://www.gerad.ca/Charles.Audet/PUB/largeur_GERAD.pdf .
2. C. Audet and J. Ninin, *Maximal perimeter, diameter and area of equilateral unit-width convex polygons*, *Journal of Global Optimization* **56** (2013), 1007–1016, Section 4 and Conjecture 9, DOI 10.1007/s10898-011-9780-4. Lawful full text: https://paperzz.com/doc/8868213/equilateral-unit-width-convex-polygons .
3. *Sharp vertex-distance bound for reflection-symmetric equilateral pentagons*, full published proof: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-vertex-distance-bound-for-reflection-symmetric-equilateral--0104867bb49f .
4. A. Dumitrescu, *Metric inequalities for polygons*, *Journal of Computational Geometry* **4** (2013), 79–93. https://jocg.org/index.php/jocg/article/download/2940/2634/7316 .
