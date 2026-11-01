# Exact random-node feasibility and a two-mechanism phase transition for positive quadratic quadrature

## Finding

For integers \(n\ge 2\), choose independent \(X_1,\ldots,X_n\) uniformly on \([-1,1]\), and fix \(0<q<1\). Let \(E_n(q)\) be the event that there are **nonnegative** numbers \(w_i\) with
\[
\sum_{i=1}^n w_i=1,\qquad \sum_{i=1}^n w_i X_i=0,\qquad \sum_{i=1}^n w_i X_i^2=q.
\]
Thus the rule is exact for \(\operatorname{span}\{1,x,x^2\}\) with target moments \((1,0,q)\). For \(q=1/3\), it integrates all quadratics under normalized uniform measure on \([-1,1]\). Define \(P_n(q)=\Pr(E_n(q))\). The following statements hold simultaneously for every integer \(n\ge2\) and every \(q\in(0,1)\):

1. Almost surely, \(E_n(q)\) holds precisely when the sample has nodes on both sides of zero and \(uv<q<ab\), where \(a\) and \(b\) are the largest absolute negative and positive nodes, while \(u\) and \(v\) are the smallest absolute negative and positive nodes. The strict inequalities may be replaced by weak ones without affecting probability. On the success event there are almost surely weights **strictly positive on every sampled node**.
2. The exact finite-sample success probability is
\[
P_n(q)=\frac{n(n-1)}{2^n}\int_q^1\int_{q/a}^1\left[(a+b)^{n-2}-(2-a-b)^{n-2}\right]\,db\,da.
\]
For \(n=2\) this is zero; for \(n=3,4\), respectively,
\[
P_3(q)=\frac{3q}{2}\left(\log\frac1q-1+q\right),\qquad P_4(q)=2P_3(q).
\]
In particular \(P_3(1/3)=\tfrac12\log3-\tfrac13\) and \(P_4(1/3)=\log3-\tfrac23\).
3. The exact large-sample exponential failure root is
\[
\lim_{n\to\infty}(1-P_n(q))^{1/n}
=\max\left\{\frac{1+q}{2},\;1-\sqrt q\right\}.
\]
The dominant failure mechanism switches at the unique \(q_0=3-2\sqrt2\): when \(q>q_0\), insufficient extreme-node spread dominates; when \(q<q_0\), an excessive empty gap around zero dominates. At equality the two exponential mechanisms tie. In particular at uniform integration \(q=1/3\), the root is \(2/3\).

## Assumptions and scope

The sampling law is continuously distributed and exactly uniform on \([-1,1]\). All assertions concern existence of weights, not feasibility under a prescribed upper/lower bound on their magnitudes, and use exact real arithmetic. Repeated nodes and equality with a boundary have probability zero. Here and below \(q\in(0,1)\) is fixed as \(n\to\infty\); \(n\) counts candidate nodes, not polynomial degree. The positive weights need not be equal.

## Proof

**1. Convex-geometric reduction.** Moment matching is equivalent to \((0,q)\in\operatorname{conv}\{(X_i,X_i^2):1\le i\le n\}\). If all sample nodes have the same sign, the convex hull cannot contain \((0,q)\). Otherwise order the negative and positive nodes as \(-a\le\cdots\le-u<0<v\le\cdots\le b\), with all four positive magnitudes between zero and one. A chord between \((-r,r^2)\) and \((s,s^2)\) with \(r,s>0\) crosses the vertical line at zero at ordinate \(rs\), by direct affine interpolation. The intersection of the convex hull with this line is an interval. Its lower endpoint uses the adjacent nodes \(-u,v\), since all points of the strictly convex parabola lie above the relevant chord at their abscissae. Its upper endpoint uses the two extremes \(-a,b\), because every sampled parabola point lies at or below the chord through these extremes. Equivalently, any intersection point at zero is a convex combination of sign-opposed two-node chords, whose heights lie in \([uv,ab]\), and both endpoint chords occur. Therefore the desired point lies in the hull exactly when \(uv\le q\le ab\). For three or more distinct samples, strict inequalities place the target in the interior of the two-dimensional hull; indeed there are points above and below on the vertical line and the target is not on any supporting face. Hence a representation with all node weights strictly positive exists: choose a sufficiently small equal positive mass \(\varepsilon\) on every sampled node, observe that the renormalized residual target remains inside the hull, then represent it with nonnegative weights and add the \(\varepsilon\)-mass back. The boundary configurations have zero probability for fixed \(q\).

**2. Two disjoint failure mechanisms.** Set \(a=b=u=v=0\) as needed on the one-sign configurations, so these fall under the insufficient-extremes failure. The event \(E_n(q)\) is \(\{ab\ge q\}\setminus\{uv>q\}\) almost surely: \(uv>q\) implies \(ab\ge uv>q\), so the upper and lower failure events \(\{ab<q\}\), \(\{uv>q\}\) are disjoint. For \(a,b\in(0,1)\), the joint (unconditional) density of the most extreme negative and positive magnitudes is
\[
f_{a,b}(a,b)=\frac{n(n-1)}{2^n}(a+b)^{n-2}.
\]
Indeed, select which two labeled observations realize the opposite extremes, multiply their two uniform densities \(1/2\), and require every remaining point to lie in \([-a,b]\), of mass \((a+b)/2\). Likewise the joint density of the nearest-to-zero negative and positive magnitudes is
\[
f_{u,v}(u,v)=\frac{n(n-1)}{2^n}(2-u-v)^{n-2},
\]
since all remaining samples avoid \((-u,v)\). Integrating each density over the common region \(ab\ge q\) (or \(uv>q\), equivalently up to null boundaries) and subtracting gives the displayed formula. At \(n=2\) the densities are identical and the success probability vanishes. At \(n=3\), the integrand becomes \(2(a+b-1)\), so elementary integration gives \(3q(\log(1/q)-1+q)/2\); at \(n=4\), the complete integrand including its prefactor is twice the \(n=3\) integrand, giving \(P_4(q)=2P_3(q)\). Every larger integer \(n\) admits an elementary finite expansion involving rational functions of \(q\) and \(\log q\).

**3. Sharp exponential rates.** Write \(F_n^+=\Pr(ab<q)\) and \(F_n^-=\Pr(uv>q)\); the failure probability is their sum. For \(0\le a,b\le1\) with \(ab\le q\), one has \(a+b\le1+q\). The joint-density bound on samples with both signs, plus the one-sign probability \(2^{1-n}\), yields \(F_n^+\le C n(n-1)((1+q)/2)^{n-2}\) for an absolute finite \(C\). Conversely, if all \(n\) samples lie in \([-q,1]\), whose sampling mass is \((1+q)/2\), then \(ab\le q\); the equality boundary has measure zero. Thus
\[
\lim_{n\to\infty}(F_n^+)^{1/n}=\frac{1+q}{2}.
\]
For the inner gap, \(uv\ge q\) forces \(u+v\ge2\sqrt q\), so \(F_n^-\le C n(n-1)(1-\sqrt q)^{n-2}\). For any fixed \(s\in(\sqrt q,1)\), if every sampled node lies in \([-1,-s]\cup[s,1]\) and at least one node has each sign, the central gap exceeds \(q\). This event has probability \((1-s)^n(1-2^{1-n})\). Letting \(s\downarrow\sqrt q\) after taking \(n\)-th roots proves
\[
\lim_{n\to\infty}(F_n^-)^{1/n}=1-\sqrt q.
\]
Since \(1-P_n=F_n^++F_n^-\), its \(n\)-th-root limit equals the larger of these two bases. The unique crossover solves \((1+q)/2=1-\sqrt q\), equivalently \(q=3-2\sqrt2\).

## Verification

`verify.py` is a standalone Python 3 standard-library checker. It constructs the integral's exact rational-plus-rational-times-log coefficients for each \(n\), checks \(4,800\) rational node sets against independent convex-combination enumeration (including exact boundary cases), verifies the \(n=3,4\) identities, and reports probabilities for \(n=2,\ldots,12\) at \(q=1/3\). All reported checks pass. These finite checks supplement, rather than establish, the all-\(n\) proof and the asymptotic limit.

## Relationship to prior work

Neumayer, Schäfer and Ullrich (2026, arXiv:2610.32699v1) establish high-probability sufficient sample-size bounds and bounded-weight random quadrature constructions for general finite-dimensional function spaces (Theorem 1.1 and subsequent sections). The present result instead classifies **unconstrained positive-weight feasibility** for every number of uniform random nodes in the fixed three-moment univariate polynomial model, with exact probability and sharp failure-rate phase transition. Its precise probability and rate formulas are not consequences of a numerical dimension-only sample-size bound. Bělík, Narayan and Turnage (2026, arXiv:2609.09506v1) study randomized least-squares constructions rather than this exact event. Van den Bos and Sanderse (2019, arXiv:1902.07477) study deterministic node addition to preserve positive quadrature weights. Hayakawa, Lyons and Oberhauser (2023, arXiv:2101.04250) establish broader random convex-hull bounds; their general inequalities do not evaluate the nonsymmetric parabola-point inclusion probability at \((0,q)\) or identify this model's two sharp exponential failure rates. The geometric convex-hull equivalence itself is standard and is not claimed as new.

## Limitations

The formula does not describe prescribed near-equal weight boxes, kernel interpolation, multivariate moment surfaces, or non-uniform sampling. The all-\(n\) law depends on uniformly distributed independent nodes. The positive weights' distribution, conditioning and numerical construction are not analyzed. No independent external mathematical audit or exhaustive historical priority proof is claimed.

## References

- S. Neumayer, M. Schäfer, T. Ullrich, *Random nodes with positive weights: Richter–Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699v1, first posted 2026-10-23. https://arxiv.org/html/2610.32699v1
- J. Bělík, A. Narayan, A. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506v1, 2026. https://arxiv.org/html/2609.09506v1
- L. M. M. van den Bos, B. Sanderse, *A geometric approach for the addition of nodes to an interpolatory quadrature rule with positive weights*, arXiv:1902.07477, 2019. https://arxiv.org/abs/1902.07477
- S. Hayakawa, T. Lyons, H. Oberhauser, *Estimating the probability that a given vector is in the convex hull of a random sample*, Probability Theory and Related Fields, 2023; arXiv:2101.04250. https://arxiv.org/abs/2101.04250
