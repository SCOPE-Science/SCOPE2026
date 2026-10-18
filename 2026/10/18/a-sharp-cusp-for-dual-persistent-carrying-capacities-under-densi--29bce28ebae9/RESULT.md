# A sharp cusp for dual persistent carrying capacities under density-dependent dispersal

## Finding
Consider two habitat patches with Beverton–Holt recruitment and dispersal survival that increases according to a Hill response. **Even when isolated patches have a unique globally attracting positive density, the coupled populations can have two distinct locally attracting positive equilibria separated by a hyperbolic saddle.** A cubic discriminant gives the sharp parameter region for three positive *synchronous* equilibria. A rational two-patch example has exactly three positive equilibria, globally contracts the difference between patch densities, and has no asymmetric equilibria.

Precisely, let \(a>0\), \(h>0\), \(u,v>0\), \(u+v<1\), \(0<p<1\), and define
\[
f(x)=\frac{a x}{1+x},\qquad s(x)=u+\frac{v x^2}{h^2+x^2},\qquad T(x)=s(x)f(x).
\]
For \((x_1,x_2)\in[0,\infty)^2\), define the synchronous-time patch map
\[
F_1(x_1,x_2)=pT(x_1)+(1-p)T(x_2),\quad
F_2(x_1,x_2)=(1-p)T(x_1)+pT(x_2).
\]
These are density-dependent dispersal coefficients \(d_{11}=d_{22}=p s\), \(d_{21}=d_{12}=(1-p)s\), with column sum \(s(x)<1\), so the model includes dispersal-related loss. Every coefficient is strictly positive and strictly increasing for positive source densities. Assume \(K=au-1>0\) and put \(L=a(u+v)-1>K\), \(H=h^2>0\), \(Q=L^2+18LK-27K^2\). There are **three distinct positive synchronous fixed points** if and only if
\[
L>9K,\qquad H_-<H<H_+,\qquad
H_\pm=\frac{Q\pm\sqrt{(L-9K)^3(L-K)}}8.
\]
Outside this strict region there is only one distinct positive synchronous equilibrium, except on the two fold boundaries, where there are two (one double), and at the cusp \(L=9K,\ H=27K^2\), where all three coalesce into one triple root. In the three-root regime the smallest and largest synchronous fixed points are **locally asymptotically stable in the full planar map for every** \(0<p<1\); the middle is unstable along the diagonal (and is a saddle when its transverse multiplier has modulus less than one).

For the exact choice
\[
a=10,\quad u=\frac{17}{110},\quad v=\frac6{11},\quad h^2=11,\quad p=\frac35,
\]
**all nonnegative fixed points of the full planar system** are
\[
(0,0),\qquad (1,1),\qquad (2,2),\qquad (3,3).
\]
The positive equilibria \((1,1)\) and \((3,3)\) are hyperbolic sinks and \((2,2)\) is a hyperbolic saddle. All trajectories synchronize exponentially:
\[
|x_1(t)-x_2(t)|\le \left(\frac35\right)^t |x_1(0)-x_2(0)|.
\]
Along the diagonal, nonzero starting populations below \(2\) converge to \(1\), populations above \(2\) converge to \(3\), and the threshold \(2\) is fixed. The three hyperbolic positive equilibria survive all sufficiently small admissible smooth perturbations of growth and dispersal parameters, including perturbations breaking patch-exchange symmetry (with the two sinks and saddle retaining their types).

## Assumptions and scope
Time is discrete, densities are nonnegative, and there are exactly two patches. Each recruited population is Beverton–Holt \(f(x)=a x/(1+x)\). A fraction \(s(x)\) of post-recruitment individuals survives and is split between the destination patches; the remaining fraction is lost. The Hill exponent is exactly \(2\). The cusp criterion classifies synchronous equilibria and their local planar stability for any \(0<p<1\), not arbitrary nonsynchronous equilibria at every mixing value. The complete full-system equilibrium classification and synchronization bound are asserted for the displayed rational parameter point. The parameter open-neighborhood conclusion is local and does not claim global convergence after perturbation.

## Proof
**Cubic reduction and cusp.** On the diagonal \(x_1=x_2=x\), the update is \(x\mapsto T(x)\). A nonzero equilibrium satisfies
\[
(1+x)(H+x^2)=a\,[uH+(u+v)x^2],
\]
which is equivalent to \(P(x)=0\), where
\[
P(x)=x^3-Lx^2+Hx-HK.
\]
Under \(K>0\), \(L>K\), one has \(P(-y)=-y^3-Ly^2-Hy-HK<0\) for \(y\ge0\). Thus every real root is positive. Its cubic discriminant is
\[
\Delta=H\big[-4H^2+QH-4L^3K\big],\qquad Q=L^2+18LK-27K^2.
\]
The quadratic factor is positive precisely between its distinct positive roots. Its discriminant has the *exact factorization*
\[
Q^2-64L^3K=(L-9K)^3(L-K).
\]
Because \(L>K>0\), positivity of the quadratic somewhere with \(H>0\) is equivalent to \(L>9K\), in which case \(Q>0\) and the roots are \(H_-<H_+\) as displayed. Hence \(\Delta>0\) precisely in the stated cusp region, giving three distinct positive roots; \(\Delta<0\) gives exactly one real, positive root. On its fold boundary \(\Delta=0\) gives one simple and one double positive root; at \(L=9K\), \(H=27K^2\), \(P(x)=(x-3K)^3\). This handles all equality cases.

The map \(T(x)=a[x/(1+x)]s(x)\) is strictly increasing for \(x\ge0\), because \(x/(1+x)\) strictly increases and \(s(x)>0\) is nondecreasing. Moreover,
\[
T(x)-x=-\frac{xP(x)}{(1+x)(H+x^2)}.
\]
When the positive roots are \(r_1<r_2<r_3\), this sign rule together with monotonicity proves \(T^t(x)\to r_1\) for \(0<x<r_2\) and \(T^t(x)\to r_3\) for \(x>r_2\). At a simple fixed root,
\[
T'(r)=1-\frac{rP'(r)}{(1+r)(H+r^2)}.
\]
Since \(P'(r_1),P'(r_3)>0\) and \(P'(r_2)<0\), the outer roots have \(0<T'(r_i)<1\), while the middle has \(T'(r_2)>1\). For general \(p\), the planar eigenvalues at a synchronous fixed point are \(T'(r)\) and \((2p-1)T'(r)\). Because \(|2p-1|<1\), the two outer synchronous equilibria are full-planar hyperbolic sinks throughout the three-root regime. The middle equilibrium is always unstable in its diagonal direction, but is not necessarily transversely stable without a mixing bound.

**Nondegenerate rational example and all full-system fixed points.** The proposed parameters satisfy \(0<u<u+v=7/10<1\), \(K=6/11\), \(L=6\), and \(H=11\). Direct simplification gives
\[
T(x)=\frac{x(17+7x^2)}{(1+x)(11+x^2)},\quad
T(x)-x=-\frac{x(x-1)(x-2)(x-3)}{(1+x)(11+x^2)}.
\]
Consequently, the synchronous equilibria are \(0,1,2,3\). Their exact longitudinal multipliers are
\[
T'(0)=\frac{17}{11},\qquad T'(1)=\frac{11}{12},\qquad
T'(2)=\frac{47}{45},\qquad T'(3)=\frac{37}{40}.
\]
A direct differentiation yields
\[
T'(x)=\frac{7x^4+120x^3+214x^2+187}{(1+x)^2(11+x^2)^2}>0.
\]
The numerator of \(3-T'(x)\) after multiplication by the positive denominator has strictly positive coefficients (in ascending powers): \(176,726,215,12,62,6,3\). Thus \(0<T'(x)<3\) for all \(x\ge0\). Since \(2p-1=1/5\), the mean-value theorem gives, for every trajectory,
\[
|F_1(x_1,x_2)-F_2(x_1,x_2)|=\frac15|T(x_1)-T(x_2)|
\le\frac35|x_1-x_2|.
\]
Any fixed point must therefore satisfy \(x_1=x_2\), giving exactly the four listed fixed points. At each synchronous fixed point the Jacobian is \(T'(r)\begin{pmatrix}3/5&2/5\\2/5&3/5\end{pmatrix}\), with eigenvalues \(T'(r)\), \(T'(r)/5\). This proves the stated sink/saddle classification. The origin has one multiplier above one and one below one, so it is unstable; it is not one of the two positive attractors. Because the three positive fixed points are hyperbolic, the implicit-function theorem and continuity of the eigenvalues preserve their existence and local stability types under small admissible \(C^1\) perturbations. The isolated Beverton–Holt map \(f(x)=10x/(1+x)\) has only the positive equilibrium \(9\), globally attracting every initial \(x>0\), illustrating that dual positive carrying capacities arise through dispersal survival rather than local recruitment multistability.

## Verification
The accompanying standard-library Python 3 program `verify.py` reconstructs the exact rational fixed-point polynomial, diagonal multipliers, derivative coefficients and cusp factorization on integer substitutions. It also tests finite rational sample states for the exact map identities and synchronization contraction. Its finite checks supplement, but cannot replace, the analytical global proofs; the coefficient positivity and discriminant factorization in the proof are the decisive certificates.

## Relationship to prior work
McGrane-Corrigan, Mason and de Andrade Moral (2024) introduced the general bounded Kolmogorov, density-dependent, lossy-dispersal patch map used here, proved persistence and extinction conditions, and numerically observed multiple types of outcomes. Their Example 5 exhibits an extinction-versus-persistence bistability with a Ricker/Hassell pair, rather than a sharp **two-positive-sink** cusp with identical monotone Beverton–Holt recruitment. Vortkamp et al. (2020) study multiple attractors under constant dispersal and *intrinsic* Allee reproduction; Knipl and Röst (2016) prove multiplicity in a continuous-time heterogeneous model with intrinsic Allee patches and linear migration. Bilgin and Kulenović (2017) give general scalar monotone-system tools and standard sigmoid Beverton–Holt results, but their stated family has at most two positive equilibria and does not furnish the present Hill-survival two-patch cusp or nontrivial synchronization certificate. These comparisons do not imply unconditional novelty; additional specialist models could contain an equivalent parameterization.

## Limitations
The cusp criterion governs synchronous equilibria. Exact exclusion of asynchronous equilibria, global synchronization and hyperbolic classifications are demonstrated at the rational example, not claimed for all allowed mixing coefficients. The example's global synchronization does not by itself supply an explicit full-plane separatrix or a global convergence theorem for every asymmetric initial state. The perturbation assertion ensures only local hyperbolic continuations. The Hill survival profile is phenomenological and need not describe a particular species. No independent mathematical audit is asserted.

## References
1. B. McGrane-Corrigan, O. Mason and R. de Andrade Moral, *A density-dependent metapopulation model: Extinction, persistence and source-sink dynamics*, arXiv:2405.04505v1 (first public 2024-05-07), https://arxiv.org/abs/2405.04505.
2. I. Vortkamp, S. J. Schreiber, A. Hastings and F. M. Hilker, *Multiple attractors and long transients in spatially structured populations with an Allee effect*, arXiv:2004.11219v1 (2020), https://arxiv.org/abs/2004.11219.
3. D. Knipl and G. Röst, *Spatially heterogeneous populations with mixed negative and positive local density dependence*, Theoretical Population Biology 109 (2016), 6–15, https://doi.org/10.1016/j.tpb.2016.01.001.
4. A. Bilgin and M. R. S. Kulenović, *Global asymptotic stability for discrete single species population models*, Discrete Dynamics in Nature and Society (2017), https://doi.org/10.1155/2017/5963594.
