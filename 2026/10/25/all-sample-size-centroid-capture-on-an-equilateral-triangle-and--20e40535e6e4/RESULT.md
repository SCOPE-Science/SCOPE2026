# All-sample-size centroid capture on an equilateral triangle and its sharp rare-failure tail

## Finding
Let \(T\) be any nondegenerate equilateral Euclidean triangle, \(G\) its centroid, and \(X_1,\ldots,X_m\) independent normalized-arclength-uniform points of \(\partial T\). For every integer \(m\ge1\), the probability \(p_m=\Pr(G\notin\operatorname{conv}\{X_1,\ldots,X_m\})\) is exactly
\[
p_m=m\int_0^{1/2}\left[Q(t)^{m-1}+(1-Q(t))^{m-1}\right]dt,
\qquad Q(t)=\frac{(1-t)^2}{2-3t}.
\]
Every \(p_m\) belongs to \(\mathbb Q+\mathbb Q\log2\), with the following explicit finite-sum evaluation. Put
\[
T_r=\begin{cases}\dfrac{2^{r+1}-2^{-(r+1)}}{r+1},&r\ne-1,\\ \log4,&r=-1,\end{cases}
\quad I_k=\frac1{3\,9^k}\sum_{j=0}^{2k}\binom{2k}{j}T_{j-k}.
\]
Then
\[
p_m=m\left(I_{m-1}+\sum_{k=0}^{m-1}(-1)^k\binom{m-1}{k}I_k\right).
\]
In particular, \(p_2=1\) and \(p_3=25/27-(20/81)\log2\). As \(m\to\infty\), the sharp equivalent is
\[
\boxed{\displaystyle p_m\sim3\sqrt{\frac{\pi m}{5}}\left(\frac59\right)^m.}
\]
The complete finite-sample law and the square-root prefactor, not the known geometric \(5/9\) halfplane-mass maximum, are the claimed contribution.

## Assumptions and scope
The triangular boundary includes all three straight sides with normalized arclength measure. Sampling is independent with replacement. The convex hull of one or two points is defined in the usual way. The centroid is strictly interior. Except for null antipodal configurations, the failure event is equivalent to all sample directions relative to \(G\) lying in one angular semicircle. No higher-dimensional, scalene, or other sampling measures are asserted.

## Proof
Normalize the side length to one and set \(A=(0,0)\), \(B=(1,0)\), \(C=(1/2,\sqrt3/2)\), \(G=(1/2,\sqrt3/6)\). The radial projection from \(G\) maps the boundary bijectively and in cyclic order to the circle of directions; its angular distribution is atomless. For \(m\ge2\), the event that all \(m\) directions lie in some semicircle holds exactly when there exists a unique sample direction whose ensuing counterclockwise semicircle contains every other direction. Uniqueness follows from the fact that two distinct gaps of size at least \(\pi\) cannot coexist when the gaps sum to \(2\pi\) (the exceptional antipodal configurations have probability zero). Conditioning on the unique first direction and summing over the \(m\) possible samples therefore gives \(p_m=m\mathbb E[q(X)^{m-1}]\), where \(q(X)\) is the normalized perimeter measure whose angular directions lie in the forward counterclockwise semicircle beginning at \(X\). The same formula yields \(p_1=1\).

By threefold symmetry it suffices to put \(X=(t,0)\), \(0\le t\le1\), with \(t\) uniform on \([0,1]\). The opposite ray through \(G\) meets the side \(BC\) at \(Y=(1-u)B+uC\) when \(0\le t\le1/2\). Comparing barycentric coordinates of the collinear triple \(X,G,Y\) yields \(u=(1-t)/(2-3t)\). The counterclockwise boundary arc from \(X\) to \(Y\) has normalized length
\[
q(t)=\frac{1-t+u}{3}=\frac{(1-t)^2}{2-3t}=Q(t)\quad (0\le t\le1/2).
\]
Reflection about the median through \(C\) reverses angular orientation, so \(q(t)=1-Q(1-t)\) on \([1/2,1]\). Consequently \(p_m=m\int_0^{1/2}[Q(t)^{m-1}+(1-Q(t))^{m-1}]dt\), as claimed.

For a finite expression, substitute \(z=2-3t\) in the integral of \(Q(t)^k\). This gives \(Q(t)=(z+1)^2/(9z)\), and thus \(I_k=\int_0^{1/2}Q(t)^k dt=\frac1{3\,9^k}\sum_{j=0}^{2k}\binom{2k}{j}\int_{1/2}^2z^{j-k}dz\). Evaluating the monomial integral gives \(T_{j-k}\); expanding \((1-Q)^{m-1}\) binomially gives the displayed exact sum. Every monomial integral is rational except its logarithmic case, \(\log4=2\log2\).

To obtain the tail, note that \(Q'(t)=-(t-1)(3t-1)/(3t-2)^2\); it has a unique minimum \(Q(1/3)=4/9\) on \([0,1/2]\), with \(Q''(1/3)=2\). Hence \(q(t)\) on \([0,1]\) has a unique global maximum at \(t=2/3\), with \(q(2/3)=5/9\), \(q''(2/3)=-2\). Its other values are strictly smaller, including the endpoints where \(q=1/2\). A second-order Taylor expansion \(q(t)=5/9-(t-2/3)^2+O(|t-2/3|^3)\) and the standard one-dimensional Laplace estimate yield
\[
\int_0^1 q(t)^{m-1}dt\sim\left(\frac59\right)^{m-1}\sqrt{\frac{5\pi}{9m}}.
\]
Multiplication by \(m\) gives the stated equivalent. The estimates are uniform outside a fixed neighborhood because \(q\) has a strict unique maximum, so endpoint or cusp contributions are exponentially smaller.

## Verification
The included standalone Python checker tests the equality between the integral and finite sums for every \(1\le m\le15\) at 65-digit working precision; checks the known three-sample specialization; compares direct geometric Monte Carlo for four sample sizes; and evaluates asymptotic ratios through \(m=500\). These tests corroborate, but do not replace, the exact derivations.

## Relationship to prior work
Wendel's classical convex-hull/halfspace framework concerns centrally symmetric direction distributions; arclength on a triangle is not centrally symmetric about its centroid, so the Wendel binomial formula does not give these probabilities. The earlier exact three-point centroid-containment law for a general triangle establishes the \(m=3\) value, which the present formula reproduces and does not claim anew. Berele and Catoiu identify the sharp halfplane perimeter fraction \(4/9\) at the centroid of an equilateral triangle (and analyze arbitrary triangles); this establishes the \(5/9\) exponential base geometrically but not the complete all-sample-size probability or its polynomial prefactor. General studies of inscribed random polytopes concern expected hull volumes, rather than this event probability.

## Limitations
No independent mathematical audit has been performed. The finite sum can exhibit cancellation at large \(m\), for which the positive integral is numerically preferable. Equivalent event-probability formulas in older specialized literature are a residual bibliographic possibility. The asymptotic is only as \(m\to\infty\), not a uniform statement over arbitrary triangles or sampling laws.

## References
1. J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica **11** (1962), 109–111, DOI: 10.7146/math.scand.a-10655.
2. I. Bárány, F. Fodor and V. Vígh, *Intrinsic volumes of inscribed random polytopes in smooth convex bodies*, arXiv:0906.0309, first posted 2009-06-01. Background on random hulls; interior sampling differs from the present model.
3. A. Berele and S. Catoiu, *The Perimeter Winternitz Theorem in a Triangle*, arXiv:2603.23653, first posted 2026-03-24. Known halfplane mass geometry; no random-sampling tail is claimed there.
