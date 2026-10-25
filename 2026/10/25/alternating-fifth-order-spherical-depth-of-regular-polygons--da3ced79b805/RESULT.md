# Alternating fifth-order spherical depth of regular polygons

## Finding

For each integer \(n\geq 3\), let \(P_n\) be a regular Euclidean \(n\)-gon of positive area, let \(O\) be its center, and let \(X,Y\) be independent points uniformly distributed with respect to area on \(P_n\). Define
\[
D_n=\Pr\bigl((X-O)\cdot(Y-O)\leq0\bigr).
\]
Equivalently, \(D_n\) is the probability that the disk with diameter \(XY\) contains \(O\) (the spherical depth of \(O\)).

For every even \(n\), \(D_n=1/2\). For odd \(n\), write \(\alpha=\pi/n\), \(h=\tan\alpha\), and define independent \(\Phi,\Psi\) with density
\[
f_\alpha(t)=\frac{\sec^2t}{2\tan\alpha}\,\mathbf 1_{[-\alpha,\alpha]}(t),\qquad
J(\alpha)=\Pr\!\left(\frac\alpha2<\Phi-\Psi<\frac{3\alpha}2\right).
\]
Then the **exact law** is
\[
\boxed{D_n=\frac12+\frac{(-1)^{(n-3)/2}}{2n}\bigl(1-4J(\pi/n)\bigr).}
\]
The essential strict estimate is \(0<J(\alpha)<1/4\) for \(0<\alpha\leq\pi/3\). Thus, for every odd \(n\),
\[
\boxed{\operatorname{sgn}(D_n-1/2)=(-1)^{(n-3)/2}.}
\]
In particular, the center has spherical depth **above** one half for \(n\equiv3\pmod4\), and **below** one half for \(n\equiv1\pmod4\). Both signs occur infinitely often. Moreover, along odd integers,
\[
\boxed{D_n=\frac12+(-1)^{(n-3)/2}\left(\frac{5\pi^4}{192n^5}+O(n^{-7})\right).}
\]
The fifth-order coefficient is sharp and positive. These assertions include an exact elementary evaluation: for \(n\geq5\) odd, set \(b=\tan(\alpha/2)\), \(c=\tan(3\alpha/2)\), and
\[
H_k(z)=\frac zk-\frac{1+k^2}{k^2}\log(1+kz).
\]
Then
\[
\boxed{J(\alpha)=\frac{H_b(h)-H_b(-b)-H_c(h)+H_c(b)+2hb}{4h^2}.}
\]
At \(n=3\), \(J(\pi/3)=(2-\log3)/4\), hence \(D_3=1/3+(\log3)/6\), agreeing with the published equilateral-triangle result [1]. For example, \(D_5=0.499054315984404\ldots\) and \(D_7=0.500162939594708\ldots\).

## Assumptions and scope

The randomness is the **independent uniform area measure**, not independently chosen vertices, edges, chord orientations, or boundary arclength in an arbitrary polygon. The regular polygon may have any scale or rotation, since the probability is similarity-invariant. For a regular polygon its center is also its incenter, and its sides are tangent to a common circle. The dot-product equality boundary has probability zero. All formulas and inequalities are for integers \(n\geq3\); the asymptotic is restricted to odd \(n\to\infty\). The conditional angular density above, and its elementary antiderivative, are obtained below rather than assumed.

## Proof

**1. Angular transfer.** Scale so that the polygon's inradius is one. The \(n\) sectors subtended by its sides have equal area. Relative to the outward normal of any chosen side, a ray through the center has angle \(t\in[-\alpha,\alpha]\) and exits the polygon at radius \(\rho(t)=\sec t\). Integrating area in polar coordinates shows that, conditional on the sector index, \(t\) has density
\[
\frac{\rho(t)^2}{\int_{-\alpha}^\alpha\rho(s)^2\,ds}=\frac{\sec^2t}{2\tan\alpha}.
\]
Thus a uniform-area direction has the same distribution as \(2\pi K/n+\Phi\), with \(K\) uniform on \(\{0,\ldots,n-1\}\) and independent \(\Phi\sim f_\alpha\). This is also an instance of the directional cone-measure transfer proved in [1].

**2. Exact cyclic count.** For even \(n\), the polygon is centrally symmetric. Conditional on \(X\neq O\), exactly half the area lies in either open half-plane through \(O\) perpendicular to \(X-O\), so \(D_n=1/2\).

Now suppose \(n\) odd and let \(z=\Phi-\Psi\in(-2\alpha,2\alpha)\). Write \(\varepsilon=(-1)^{(n-3)/2}\). Among the \(n\) cyclic differences \(2\pi j/n+z\), \(0\leq j<n\), the number with negative cosine is exactly
\[
N_n(z)=\frac{n+\varepsilon}{2}-\varepsilon\,\mathbf1_{\{\alpha/2<|z|<3\alpha/2\}},
\qquad |z|<2\alpha,
\]
except at the finitely many threshold values, which are null events. To check this count, locate the cyclic grid points adjacent to each of the two boundaries of the open negative-cosine semicircle. As \(z\) travels across one complete spacing interval on either side of zero, a grid point crosses a boundary only when \(|z|=\alpha/2\) or \(|z|=3\alpha/2\); the count at \(z=0\) is \((n+\varepsilon)/2\). The formula works also for \(n=3\), when two directions selected from the same sector can form an obtuse angle.

Since the sector-index difference is uniform on \(\{0,\ldots,n-1\}\), averaging \(N_n(\Phi-\Psi)/n\) gives
\[
D_n=\frac12+\frac\varepsilon{2n}
-\frac\varepsilon n\Pr\!\left(\frac\alpha2<|\Phi-\Psi|<\frac{3\alpha}2\right).
\]
The difference is symmetrically distributed and the probability on the right equals \(2J(\alpha)\), proving the exact law.

**3. Strict anti-concentration lemma.** We prove the following more general fact. If \(U,V\) are independent with the *same* even continuously differentiable probability density on \([-1,1]\), strictly increasing in \(|u|\), then
\[
\Pr\bigl(1/2<U-V<3/2\bigr)<1/4.
\]
Indeed, any such density \(p\) is a probability mixture of uniform measure on \([-1,1]\) and uniform measures on the two outer intervals \([-1,-s]\cup[s,1]\), \(0<s<1\). Explicitly, for \(p\) differentiable on \((0,1)\), the mixture places mass \(2p(0)\) at \(s=0\) and mass \(2(1-s)p'(s)\,ds\) at \(s\in(0,1)\). This identity follows by integrating the density \(\mathbf1_{\{|u|\geq s\}}/[2(1-s)]\) against those masses. The weights sum to one because \(2\int_0^1p(u)du=1\). Our application \(p(u)=\alpha\sec^2(\alpha u)/(2\tan\alpha)\) is smooth and strictly increasing for positive \(u\).

It suffices to handle independent outer-uniform variables at arbitrary \(s,t\in[0,1)\). Let \(\mathcal B=\{(u,v)\in[-1,1]^2:1/2<u-v<3/2\}\), which has area one, and set
\[
K(s,t)=\operatorname{area}\bigl(\mathcal B\cap[-s,s]\times[-t,t]\bigr).
\]
For every fixed \(0\leq s\leq1\), the area of \(\mathcal B\) restricted to \(|u|<s\) equals \(s\): the allowed vertical length \(\ell(u)\) obeys \(\ell(u)+\ell(-u)=1\). The analogous identity holds for \(|v|<t\). Inclusion-exclusion therefore gives the exact outer-uniform probability
\[
\frac14+\frac{K(s,t)-st}{4(1-s)(1-t)}.
\]
Put \(a=s+t\), \(b=|s-t|\), and \((x)_+=\max(x,0)\). Direct integration of a strip across the central rectangle gives
\[
K(s,t)=\frac12\left[(a-1/2)_+^2-(b-1/2)_+^2-(a-3/2)_+^2\right].
\]
We now verify \(K(s,t)\leq st\), strictly for \(0<s,t<1\). If \(a\leq1/2\), then \(K=0\). If \(1/2<a\leq3/2\) and \(b\leq1/2\), then \(K=(a-1/2)^2/2\); the desired inequality is equivalent to \(b^2\leq1/2-(a-1)^2\), true because the left side is at most \(1/4\) and the right side is at least \(1/4\). Equality in this subcase with both parameters positive requires one of \(s,t\) to equal one. If \(1/2<a\leq3/2\) and \(b>1/2\), assume \(s\geq t\); then \(K=t(2s-1)\leq st\), again strictly unless \(s=1\). Finally, if \(a>3/2\), then \(b<1/2\) since \(a+b=2\max(s,t)\leq2\). Here \(K=a-1\leq st\), because \(st-(s+t-1)=(1-s)(1-t)\geq0\), strictly for interior parameters.

Every pair of nonzero mixture parameters consequently contributes strictly less than \(1/4\), while pairs with a zero parameter contribute exactly \(1/4\). The density \(p_\alpha\) has strictly positive mixture mass on \((0,1)\), hence
\[
0<J(\alpha)<\frac14\qquad (0<\alpha\leq\pi/3).
\]
This proves the claimed strict alternating signs.

**4. Elementary evaluation.** The event defining \(J\) may be integrated by conditioning on \(\Phi=t\). The admissible interval for \(\Psi\) yields the identity
\[
4h^2J(\alpha)
=\int_{-\alpha/2}^{\alpha}\!\sec^2t\tan(t-\alpha/2)\,dt
-\int_{\alpha/2}^{\alpha}\!\sec^2t\tan(t-3\alpha/2)\,dt
+2h\tan(\alpha/2).
\]
For \(0<\alpha<\pi/3\), substitution \(z=\tan t\) yields
\[
\int \sec^2t\tan(t-c)\,dt
=H_{\tan c}(\tan t)+\text{constant}.
\]
The displayed elementary formula follows on substituting endpoints. At \(\alpha=\pi/3\), the second integrand becomes \(-\sec^2t\cot t\), with primitive \(-\log\tan t\); simplification gives \(J(\pi/3)=(2-\log3)/4\).

**5. Fifth-order asymptotic.** Put \(U=\Phi/\alpha\), \(V=\Psi/\alpha\), each supported on \([-1,1]\). Their common density has the uniform expansion
\[
p_\alpha(u)=\frac{\alpha\sec^2(\alpha u)}{2\tan\alpha}
=\frac12+\frac{\alpha^2}{2}\left(u^2-\frac13\right)+O(\alpha^4).
\]
Let \(g_\alpha=p_\alpha-1/2\), an even zero-integral function. Because \(\ell(u)+\ell(-u)=1\), the terms linear in \(g_\alpha\) vanish *exactly* when expanding \(J(\alpha)=\iint_{\mathcal B}p_\alpha(u)p_\alpha(v)\,du\,dv\). Hence
\[
J(\alpha)=\frac14+\frac{\alpha^4}{4}I+O(\alpha^6),
\qquad
I=\iint_{\mathcal B}\left(u^2-\frac13\right)\left(v^2-\frac13\right)\,du\,dv.
\]
The strip decomposes into the two integration domains
\[
-\frac12<u<\frac12,\ -1<v<u-\frac12;
\qquad
\frac12<u<1,\ u-\frac32<v<u-\frac12.
\]
Polynomial integration gives \(I=-5/96\), and therefore
\[
J(\alpha)=\frac14-\frac{5\alpha^4}{384}+O(\alpha^6).
\]
Substitute \(\alpha=\pi/n\) into the exact odd-order law to obtain the asserted \(n^{-5}\) expansion, with \(O(n^{-7})\) remainder.

## Verification

The accompanying standalone `verify.py` calculates \(I=-5/96\) exactly using rational symbolic integration, checks the cyclic phase count for every odd order from three through forty-three on nonthreshold sample points, and compares the elementary logarithmic expression with independent adaptive angular integrations for several polygon orders. It also checks the strict sign pattern and fifth-order asymptotic numerically. Running `python verify.py` with the packages in `requirements.txt` produced the final line `PASS: exact convolution coefficient, phase counts, independent quadrature and limits`. The infinite-dimensional and all-order assertions rely on the proof above, not on these finite tests.

## Relationship to prior work

Rabinowitz [1], first posted on 2026-08-26, established the planar directional cone-measure transfer and computed the incenter's spherical depth for arbitrary triangles, including the equilateral value recovered here at \(n=3\). Its explicit probability formula and sharp extremal assertion are about triangles, not the full family of regular polygons. This work uses that transfer as motivation but proves a different, all-order alternation theorem and the fifth-order asymptotic. Bremner and Shahsavarifar [2] introduced efficient planar spherical-depth computation for empirical point sets; their abstract does not give the analytic regular-polygon law. A literature and indexed-claims search located related central-chord, regular-polygon and depth results but no statement implying the alternating sign and sharp coefficient proved here. Absence from those searches is not a proof of global publication priority.

## Limitations

The strict sign theorem uses the radial geometry of a *regular* polygon and does not extend to arbitrary tangential polygons without additional hypotheses. The general outward-angular-density lemma provides a sufficient mechanism, not a characterization of all possible distributions. The case \(n=3\), the even-order half-depth observation, and the directional-transfer principle are prior or elementary facts; the new mathematical content is the exact odd-order profile, strict alternating directions of deviation, and fifth-order cancellation. No claim is made about the spherical-depth maximum over points other than the center, nor about arbitrary nonregular polygons. Historical priority outside searchable and inspected primary literature remains an uncertainty.

## References

[1] Stanley Rabinowitz, *The Probability That the Incenter of a Triangle Lies in a Random Diameter Disk*, arXiv:2608.27491v1, first submitted August 26, 2026. https://arxiv.org/abs/2608.27491 .

[2] David Bremner and Rasoul Shahsavarifar, *An Optimal Algorithm for Computing the Spherical Depth of Points in the Plane*, arXiv:1702.07399, first submitted February 23, 2017. https://arxiv.org/abs/1702.07399 .
