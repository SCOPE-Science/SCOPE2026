# Reentrant collision–separation transitions in equal-radius two-kernel Bergman approximation

## Finding
Let \(A^2(\mathbb D)\) be the analytic Bergman space for normalized area measure \(dA/\pi\), with kernels \(k_a(z)=(1-\overline a z)^{-2}\). Fix \(0<t<1\) and choose two sampling nodes \(a=\sqrt t\) and \(b=\sqrt t\,e^{i\theta}\), \(0\le\theta\le\pi\), up to a common rotation and permutation. For \(0<\theta\le\pi\), let \(V_{t,\theta}=\operatorname{span}\{k_a,k_b\}\); at \(\theta=0\) give it the canonical confluent meaning \(V_{t,0}=\operatorname{span}\{k_a,\partial_{\overline a}k_a\}\). Define \(c=\cos\theta\) and the captured squared projection \(P_t(c)=\|\Pi_{V_{t,\theta}}z^2\|_{A^2}^2\), which is independent of common rotation.

Define
\[
D_t(c)=1-t+t^2-tc=t(1-c)+(1-t)^2,
\]
\[
Q_t(c)=4t^2(1-t)^2c^2+4t(1-t)^2(2t-1)c+8t^4-16t^3+16t^2-8t+1.
\]
Then the exact identity is
\[
\boxed{P_t(c)=t(1-t)^2(8t^2-7t+2)-\frac{t(1-t)^2(1-c)Q_t(c)}{D_t(c)}.}
\]
The normalized energy captured from \(z^2\) is \(3P_t(c)\), because \(\|z^2\|^2=1/3\). The exact optimum over the fixed-radius confluent two-kernel designs has the following complete phase diagram. Write
\[
t_0=0.121278837988269\ldots,\qquad t_1=0.825314595719694\ldots,
\]
where \(t_0\) is the unique zero in \((0,1/4)\) of \(20t^4-44t^3+36t^2-12t+1\) and \(t_1\) is the unique zero in \((1/4,1)\) of \(4t^3-4t^2+3t-2\).

For \(0<t\le t_0\) and \(t_1<t<1\), the unique optimizer is \(c=1\), the confluent first-jet configuration. For \(t_0<t<t_1\), the unique optimizer is \(c=c_*(t)\in(-1,1)\) with \(Q_t(c_*)<0\). It is the unique root in \(\{c\in(-1,1):Q_t(c)<0\}\) of the cubic equation
\[
\boxed{\big[(1-c)Q_t'(c)-Q_t(c)\big]D_t(c)+t(1-c)Q_t(c)=0.}
\]
At \(t=t_1\), there are exactly two inequivalent maximizing configurations: \(c=1\) and \(c=(2t_1)^{-1}-1=-0.394170413811731\ldots\). The latter angle is \(1.97596133431329\ldots\) radians. The separated optimum tends to collision as \(t\downarrow t_0\), but it tends to this nonzero angle as \(t\uparrow t_1\); above \(t_1\) the preferred configuration jumps back to collision. For every \(0<t<1\), an antipodal configuration \(c=-1\) fails to maximize \(P_t\).

For designs using two **distinct** kernels only, the optimizer is attained precisely for \(t_0<t\le t_1\). At all other radii the same sharp value is only a supremum as the nodes coalesce; the derivative kernel is an explicit limiting two-dimensional span, not a single repeated evaluation kernel.

## Assumptions and scope
All norms are those of \(A^2(\mathbb D)\) with \(\int_{\mathbb D}|f|^2\,dA/\pi\). The kernel normalization is exactly \(k_a(z)=(1-\overline a z)^{-2}\). The target is \(f(z)=z^2\). Both samples lie on one circle \(|a|=|b|=\sqrt t\), and their common radius is fixed during angular optimization. The coefficients of the two kernel functions in the approximant are unrestricted complex numbers and are chosen optimally by Hilbert-space orthogonal projection. The theorem concerns this natural circular two-site design, not arbitrary unequal-radius nodes, general weights, or more than two nodes.

Collision is interpreted as \(\lim_{b\to a}\operatorname{span}\{k_a,k_b\}=\operatorname{span}\{k_a,\partial_{\overline a}k_a\}\), where \(\partial_{\overline a}k_a(z)=2z(1-\overline a z)^{-3}\), a linearly independent jet. For fixed radius the tangential derivative differs by a nonzero scalar from the complex derivative, so this is indeed the relevant limit.

## Proof
**1. Exact Gram identity.** For distinct nodes \(a,b\), the Hermitian Gram entries are \(\langle k_{a_j},k_{a_i}\rangle=(1-a_j\overline{a_i})^{-2}\), and the evaluation vector of \(f(z)=z^2\) is \((a^2,b^2)\). The squared projection is the corresponding positive Gram-inverse quadratic form. Put \(a=\sqrt t\), \(b=\sqrt t e^{i\theta}\) and \(c=\cos\theta\). An explicit inversion of the \(2\times2\) Gram matrix, using \(\cos(2\theta)=2c^2-1\), \(\cos(3\theta)=4c^3-3c\), and \(\cos(4\theta)=8c^4-8c^2+1\), yields
\[
P_t(c)=P_t(1)-\frac{t(1-t)^2(1-c)Q_t(c)}{D_t(c)},\quad P_t(1)=t(1-t)^2(8t^2-7t+2).
\]
The removable \(c=1\) value follows either by continuity of the two-plane in Hilbert space or by direct inversion of the value/derivative-kernel Gram matrix. The identity is exact for all \(0<t<1\) and \(-1\le c\le1\), not an asymptotic expansion.

**2. Signs and the two sharp critical radii.** Since \(D_t(c)=(1-t)^2+t(1-c)>0\), a separated design beats collision precisely when \(Q_t(c)<0\). This quadratic is strictly convex in \(c\), and its vertex is \(v_t=(2t)^{-1}-1\). When \(t\le1/4\), the vertex lies at or to the right of \(1\); the minimum of \(Q_t\) on \([-1,1]\) is
\[
Q_t(1)=20t^4-44t^3+36t^2-12t+1.
\]
Its second derivative equals \(24(5t-3)(2t-1)>0\) on \([0,1/4]\), and its first derivative remains negative there because its value at \(1/4\) is negative. As \(Q_0(1)=1\) and \(Q_{1/4}(1)=-23/64\), this minimum crosses zero exactly once, at \(t_0\). When \(t\ge1/4\), the vertex lies within \([-1,1]\), and the minimum becomes
\[
Q_t(v_t)=t(4t^3-4t^2+3t-2).
\]
The cubic in parentheses increases strictly, because its derivative is \(12(t-1/3)^2+5/3>0\); it is negative at \(1/4\) and positive at \(1\). It therefore crosses zero exactly once at \(t_1\). Hence \(Q_t\ge0\) everywhere exactly for \(t\le t_0\) or \(t\ge t_1\). At \(t=t_1\), \(Q_t\) is a positive multiple of \((c-v_t)^2\); its only two maximizers of \(P_t\) are \(c=1\) and \(c=v_t\). At \(t=t_0\), the minimum zero occurs only at \(c=1\).

**3. A unique separated optimizer between the thresholds.** For \(t_0<t<t_1\), the negative set \(\{c\in[-1,1]:Q_t(c)<0\}\) is a nonempty interval. If its two real quadratic zeros are \(r_-<r_+\), then within its intersection with \((-1,1)\) the positive gain is a constant multiple of
\[
G_t(c)=\frac{(1-c)(c-r_-)(r_+-c)}{D_t(c)}.
\]
The logarithm has strictly negative second derivative:
\[
(\log G_t)''=-\frac1{(1-c)^2}-\frac1{(c-r_-)^2}-\frac1{(r_+-c)^2}+\frac{t^2}{D_t(c)^2}<0,
\]
where the last strict inequality follows from \(D_t(c)>t(1-c)\). The gain has an interior maximizer: at its right endpoint it vanishes; at its left endpoint it either vanishes or, when that endpoint is \(-1\), has positive inward derivative because
\[
P_t'(-1)=\frac{t(1-t)^4(4t^4+4t^3+4t^2+4t+1)}{(1+t^2)^2}>0.
\]
Strict log-concavity forces the maximizing angle to be unique. Differentiation gives precisely the displayed cubic equation. Thus the separated angle is never \(\pi\) and its optimizer is global on the entire circular design class.

**4. Critical limits and attainment.** As \(t\downarrow t_0\), the negative set contracts toward \(c=1\) (the vertex is outside the interval), so \(c_*(t)\to1\). As \(t\uparrow t_1\), it contracts toward \(v_{t_1}\in(-1,1)\), so \(c_*(t)\to v_{t_1}\). This proves continuous emergence and discontinuous return. At collision only the confluent jet achieves the limiting two-dimensional subspace; at a separated root ordinary distinct kernel vectors achieve it. The above strict inequalities classify all equality cases modulo simultaneous rotation and node exchange.

## Verification
The standalone script `verify_phase.py` reconstructs the exact projection rational function by independent symbolic expressions, checks the crucial polynomial identities and derivative formula, and compares the formula against direct complex \(2\times2\) Gram inversion for 160 independently generated parameter pairs at 60-digit precision. It also checks confluent limits and all critical regimes, totaling 179 assertions in one execution. To reproduce, use `python verify_phase.py` with Python 3, SymPy and mpmath. The verification is corroborative for the all-real-parameter conclusions; the algebraic and inequality arguments above provide those proofs.

For illustration, at \(t=0.4\) the unique optimal cosine is \(c_*=-0.126950746617272\ldots\) (separation \(1.69809057059\ldots\) radians) and \(P_t(c_*)=0.157360292863794\ldots\), while the collision value is only \(0.06912\). At \(t=t_1\), the two values tie exactly by the quadratic double root of \(Q_t\).

## Relationship to prior work
Qu, Qian, Li and Zhu (available online 10 November 2021) established existence of best reproducing-kernel approximations in weighted Bergman spaces, not this fixed-radius angular optimization or its critical radii. Qian's 18 January 2022 preprint proves broader existence in analytic reproducing-kernel spaces, with a full explicit Bergman-kernel discussion in Section 4.2; its analytic statements do not determine the present two-node projection constants. Classical reproducing-kernel Gram projection formulas are used here as input, not claimed as discoveries. Related cyclic kernel orbit spectra and Hardy two-node quadratic approximation concern different constraints and, respectively, different kernel normalizations; neither yields the two sharp collision–separation thresholds by statement implication.

## Limitations
The result does not prove optimality among nodes of unequal radii, among other targets, or among more than two kernels. In the collision regions a two-distinct-kernel configuration has only a sharp supremum, not a literal maximum. The results are analytical, with numerical calculations used only for corroboration and decimal presentation. Historical novelty is subject to the possibility of an earlier unindexed special-purpose approximation formula or an equivalent result implicit in the broader nonlinear-kernel literature; the focal 2021 paper's indexed opening material was available, but full-paper inspection was blocked by source access restrictions.

## References
Qu, W., Qian, T., Li, H., and Zhu, K., *Best kernel approximation in Bergman spaces*, Applied Mathematics and Computation 416 (2022), article 126749; online 10 November 2021; DOI: 10.1016/j.amc.2021.126749.

Qian, T., *n-Best Kernel Approximation in Reproducing Kernel Hilbert Spaces*, arXiv:2201.07228v1, 18 January 2022; Section 4.2 and Theorem 4.2.
