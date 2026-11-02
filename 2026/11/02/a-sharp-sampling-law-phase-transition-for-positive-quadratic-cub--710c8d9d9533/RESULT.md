# A sharp sampling-law phase transition for positive quadratic cubature with Chebyshev nodes

## Finding
Let \(0<q<1\), let \(m\ge2\), and sample \(X_1,\ldots,X_m\) independently from the Chebyshev (arcsine) density
\[
 f(x)=\frac{1}{\pi\sqrt{1-x^2}},\qquad -1<x<1.
\]
Define \(P_m(q)\) as the probability that **strictly positive weights on all \(m\) sampled nodes** integrate the three functions \(1,x,x^2\) to the target moments \(1,0,q\). The sampling law is **not** the target law. Put
\[
 G(t)=\frac{\arcsin t}{\pi},\quad
 r_{\rm out}(q)=\frac12+G(q),\quad
 r_{\rm in}(q)=1-2G(\sqrt q),\quad
 C(q)=\sqrt{\frac{\sqrt{q(1-q)}}{r_{\rm in}(q)}}.
\]
Then the sharp failure asymptotics, including leading constants and polynomial factors, are
\[
 1-P_m(q)\sim
 \begin{cases}
 C(q)\sqrt m\,r_{\rm in}(q)^m,&0<q\le1/3,\\
 2r_{\rm out}(q)^m,&1/3<q<1.
 \end{cases}\qquad(m\to\infty).
\]
The two exponential mechanisms exchange dominance **exactly at** \(q=1/3\). At equality their exponential bases coincide but the interior-hole mechanism wins by the factor \(\sqrt m\). In particular, for the *uniform probability target* on \([-1,1]\), whose quadratic moment is \(q=1/3\),
\[
 1-P_m(1/3)\sim C_*\sqrt m\,r_*^m,
 \qquad r_*=\frac12+\frac{\arcsin(1/3)}{\pi}=0.6081734479693928\ldots,
 \quad C_*=\sqrt{\frac{\sqrt2}{3r_*}}=0.8804063044373697\ldots.
\]
For arbitrary finite \(m\), there is also an exact two-variable quadrature for the success probability. With \(f_+(t)=(\pi\sqrt{1-t^2})^{-1}\) for \(0<t<1\),
\[
 P_m(q)=m(m-1)\int_q^1\int_{q/a}^1 f_+(a)f_+(b)
 \left[(G(a)+G(b))^{m-2}-(1-G(a)-G(b))^{m-2}\right] \,\mathrm db\,\mathrm da.
\]
These claims are exact mathematical statements for real-arithmetic, unrestricted strictly positive weights, not claims about weights produced by a particular randomized least-squares algorithm.

## Assumptions and scope
The random variables are independent and absolutely continuous, with the stated arcsine sampling law and the same fixed target moment vector \((1,0,q)\). The integer \(m\ge2\) is arbitrary for the finite formula; the sharp limits fix \(q\in(0,1)\) and let \(m\to\infty\). Weights may depend on the nodes, must all be positive, and must satisfy the three moments exactly. The target can be any centered probability measure supported in \([-1,1]\) with second moment \(q\); in particular, \(q=1/3\) gives normalized Lebesgue integration. The source-paper notion of weights approximately equal to importance weights is not imposed.

## Proof
**1. Moment-polytope geometry.** For an arbitrary sample with no zero or repeated coordinates, the node moments are points \((X_i,X_i^2)\) on a strictly convex parabola. A convex combination with first coordinate zero exists only when both signs occur. Let \(a,b\) be the nearest-to-zero magnitudes on the negative and positive sides, and let \(A,B\) be their farthest magnitudes. The chord joining \((-u,u^2)\) and \((v,v^2)\) meets the vertical line at zero at height \(uv\). The intersection of the sample convex hull with the vertical line through zero is therefore exactly the interval \([ab,AB]\). Thus strict positivity at every node is possible if and only if both signs occur and \(ab<q<AB\): if the target is an interior point, mix a positive-weight interior barycenter into any convex representation and choose a sufficiently small mixture coefficient. Equality boundaries have probability zero. The deterministic chord criterion is a reusable prior geometric observation, not the novel assertion.

**2. Disjoint failure mechanisms and exact integrals.** Denote by \(U_m(q)\) the event of no opposite signs or \(AB\le q\) ('insufficient outer spread'), and by \(L_m(q)\) the event of both signs but \(ab\ge q\) ('empty central cross interval'). These events are disjoint since \(ab\le AB\), and \(1-P_m(q)=U_m(q)+L_m(q)\). Conditioning on the largest positive node, and on the smallest positive node respectively, gives
\[
\begin{aligned}
 U_m(q)&=r_{\rm out}(q)^m+m\int_q^1 f_+(a)\left(G(a)+G(q/a)\right)^{m-1}\mathrm da,\\
 L_m(q)&=m\int_q^1 f_+(a)\left[\left(1-G(a)-G(q/a)\right)^{m-1}
 -\left(\tfrac12-G(a)\right)^{m-1}\right]\mathrm da.
\end{aligned}
\]
The first formula counts all configurations with no positive node above \(q\), then the configurations whose largest positive point exceeds \(q\) but whose negative extreme has magnitude at most \(q/a\). The second formula counts the configurations whose nearest positive point is \(a\) and whose nearest negative magnitude is at least \(q/a\), subtracting configurations without a negative point. Alternatively, distinguish the largest positive/negative pair for \(AB>q\), or the nearest opposite-sign pair for \(ab>q\), to obtain the stated double integral for their difference. In all integrations, the factor \(m\) or \(m(m-1)\) counts which labelled observations supply the specified extremes.

**3. Interior-hole Laplace asymptotics.** Substitute \(a=\sin\alpha\). The relevant base becomes
\[
 S_q(\alpha)=1-\frac{\alpha+\arcsin(q/\sin\alpha)}{\pi},
 \qquad \arcsin q\le\alpha\le\pi/2.
\]
A direct derivative calculation shows that \(G(a)+G(q/a)\) decreases strictly from \(a=q\) to \(a=\sqrt q\), then increases strictly to \(a=1\); indeed the sign of its derivative is that of \(a^4-q^2\). Thus \(S_q\) has a unique strict interior maximum at \(\alpha_0=\arcsin\sqrt q\), of height \(r_{\rm in}(q)\). Differentiation gives
\[
 S_q''(\alpha_0)=-\frac{2}{\pi\sqrt{q(1-q)}}.
\]
The subtracted power in \(L_m\) has base bounded above by \(1/2-G(q)<r_{\rm in}(q)\) and is exponentially negligible. The ordinary nondegenerate interior Laplace expansion now yields
\[
 L_m(q)\sim\frac{m}{\pi}\,r_{\rm in}(q)^{m-1}
 \sqrt{\frac{2\pi r_{\rm in}(q)}{m\,2/(\pi\sqrt{q(1-q)})}}
 =C(q)\sqrt m\,r_{\rm in}(q)^m.
\]
This is a theorem for all fixed \(q\in(0,1)\), not a finite-m extrapolation.

**4. Outer-spread asymptotics.** The base \(H_q(a)=G(a)+G(q/a)\) has a unique minimum at \(a=\sqrt q\), and its equal endpoint maxima are \(r_{\rm out}(q)\), at \(a=q\) and \(a=1\). Use \(a=\sin\alpha\). The upper endpoint contribution from \(\alpha\uparrow\pi/2\) to the integral in \(U_m\) is \(r_{\rm out}(q)^m(1+o(1))\), because
\[
 H_q(\sin\alpha)=r_{\rm out}(q)-\frac{\pi/2-\alpha}{\pi}+O((\pi/2-\alpha)^2).
\]
The lower endpoint at \(\alpha\downarrow\arcsin q\) satisfies \(r_{\rm out}(q)-H_q(\sin\alpha)\asymp\sqrt{\alpha-\arcsin q}\), so its integral contributes only \(O(r_{\rm out}(q)^m/m)\). The remaining compact interval is exponentially smaller. Including the initial \(r_{\rm out}^m\) term yields
\[
 U_m(q)\sim2r_{\rm out}(q)^m.
\]

**5. Exact crossover and target rate.** The function \(r_{\rm in}(q)\) is strictly decreasing and \(r_{\rm out}(q)\) is strictly increasing. Using \(\cos(2\arcsin(1/\sqrt3))=1/3\) gives \(r_{\rm in}(1/3)=r_{\rm out}(1/3)\). Monotonicity proves the crossover is unique. Summing the disjoint failure probabilities proves the piecewise asymptotic. For the uniform target, \(r_*=0.608173\ldots<2/3\), whereas the known uniform-*node* sharp failure rate is \(3(2/3)^m(1+o(1))\). Thus arcsine nodes strictly improve the leading exponential sample-complexity constant: at small failure tolerance \(\delta\), the ratio of necessary Chebyshev-node and uniform-node sample counts tends to
\[
 \frac{\log(3/2)}{-\log r_*}=0.8153409474946793\ldots.
\]
This compares support feasibility only, not accuracy beyond degree two or computational cost.

## Verification
A standalone `verify.py` checks the one-dimensional exact disjoint-failure integrals for five values of \(q\), tests both sharp asymptotic constants numerically at large \(m\), and independently checks the moment-polytope criterion by solving linear programs on 1,200 seeded random sample sets with \(3,4,6,9\) nodes. The verifier completed 1,257 checks. Additional separate double-integration replays for \(q\in\{1/5,1/3,7/10\}\) and \(m\in\{2,3,4,5\}\) agreed with the disjoint-failure formula to within \(3\times10^{-14}\). These tests are corroborating computations; the full-range proof is the geometric and Laplace argument above.

## Relationship to prior work
Neumayer, Schäfer and Ullrich (2026), arXiv:2610.32699v1, prove general high-probability existence of positive rules with Lewis-density sampling, bounded reweighting and sufficient oversampling, notably their Theorem 2.4. They do not state the Chebyshev-node, degree-two, target-variance-resolved exact failure law or its boundary polynomial prefactor. Bělík, Narayan and Turnage (2026), arXiv:2609.09506v1, study probabilistic positive quadrature through randomized least squares; only its abstract and publicly accessible secondary technical account could be inspected, leaving a priority risk. Van den Bos, Sanderse, Bierbooms and van Bussel (2018/2019), arXiv:1809.09842v2, develop positive nested rules for sample sets, but their examined introduction, exactness definitions and construction address positive extraction rather than this sampling-probability law. The classical Wendel origin-containment formula assumes central symmetry of the lifted sampling distribution, which the parabolic image \((X,X^2-q)\) does not have.

Earlier exact results for uniform sampling nodes already establish the opposite-sign chord criterion and the uniform-node asymptotic \(3(2/3)^m\) at \(q=1/3\). Neither the criterion itself nor that prior uniform-node result is claimed new. The contribution is the distinct arcsine-law phase transition, exact arcsine finite probability and nontrivial \(\sqrt m\) boundary mechanism, including the direct comparison of exponential sampling rates.

## Limitations
The asymptotics fix \(q\in(0,1)\); no assertion is made uniformly as \(q\) approaches the endpoints or varies with \(m\). The event is existence of **some** strictly positive exact weights, not positivity of ordinary interpolatory or least-squares weights. No lower bound on the smallest permissible weight, finite-precision stability, broader polynomial degree or computational work claim follows. The benchmark compared against uniform sampling arises from earlier work. A specialized equivalent historical probability formula may exist outside the primary sources inspected; scholarly priority has not been independently audited.

## References
- S. Neumayer, M. Schäfer and T. Ullrich, *Random nodes with positive weights: Richter–Tchakaloff rules and optimal positive quadrature*, arXiv:2610.32699v1 (first posted 2026-10-23), https://arxiv.org/html/2610.32699v1.
- F. Bělík, A. Narayan and J. Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares*, arXiv:2609.09506v1 (2026-09-08), https://arxiv.org/abs/2609.09506.
- L. M. M. van den Bos, B. Sanderse, W. A. A. M. Bierbooms and G. J. W. van Bussel, *Generating nested quadrature rules with positive weights based on arbitrary sample sets*, arXiv:1809.09842v2 (2019 revision; 2018 first public version), https://arxiv.org/html/1809.09842v2.
- J. G. Wendel, *A Problem in Geometric Probability*, Mathematica Scandinavica **11** (1962), 109–111, https://doi.org/10.7146/math.scand.a-10655.
