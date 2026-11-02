# Stationary speed-slope balance and quantitative outer-branch activity in Chua's piecewise-linear flow

## Finding
Consider the globally Lipschitz Chua system
\[
\dot x=\alpha(y-h(x)),\quad \dot y=x-y+z,\quad \dot z=-\beta y,
\qquad \alpha,\beta>0,
\]
with the continuous odd three-segment function
\[
h(x)=\begin{cases}
 m_1x+(m_0-m_1),&x\ge1,\\
 m_0x,&-1\le x\le1,\\
 m_1x-(m_0-m_1),&x\le-1,
\end{cases}\qquad m_0<0<m_1.
\]
Let \(\mu\) be any compactly supported invariant Borel probability measure of the flow. All expectations below are with respect to \(\mu\). Then
\[
\boxed{\mathbb E[y\mid x]=h(x)},\qquad
\boxed{\operatorname{Var}(y)-\operatorname{Var}(h(x))
=\alpha^{-2}\mathbb E[\dot x^2]}.
\]
The exact **speed-slope balance** is
\[
\boxed{\mathbb E[\dot y^2]=\mathbb E[h'(x)\dot x^2]}. \tag{1}
\]
The value chosen for \(h'\) at \(x=\pm1\) is immaterial. In particular, with
\[
K_{\mathrm{in}}=\mathbb E[\dot x^2\mathbf1_{\{|x|<1\}}],\qquad
K_{\mathrm{out}}=\mathbb E[\dot x^2\mathbf1_{\{|x|>1\}}],
\]
every measure not supported on equilibria obeys
\[
\boxed{\frac{K_{\mathrm{out}}}{K_{\mathrm{in}}+K_{\mathrm{out}}}
>\frac{-m_0}{m_1-m_0}}. \tag{2}
\]
For the classical slopes \(m_0=-1/7\) and \(m_1=2/7\), the right-hand side is exactly \(1/3\). Thus more than one third of the stationary **squared \(x\)-speed energy**, not necessarily one third of residence time, occurs at \(|x|>1\). There is no assertion here that a chaotic attractor exists for every allowed parameter pair.

The following additional identities are useful in the derivation:
\[
\mathbb E[x+z\mid y]=y,\quad \mathbb E[y\mid z]=0,\quad
\operatorname{Var}(x+z)-\operatorname{Var}(y)=\mathbb E[\dot y^2],\quad
\mathbb E[xh(x)]=\mathbb E[y^2]=\beta^{-2}\mathbb E[\dot z^2]. \tag{3}
\]
The last identity and the conditional laws in \(y,z\), as well as the equilibrium-amplitude excursion they imply, had already been established for this same Chua model in the earlier published finding *Equilibrium-amplitude excursion law for the Chua double-scroll system* (2026-10-04); see References. They are included here as **previously known inputs and contextual consequences**, not independent new results. In particular, that prior result shows that a non-equilibrium compact stationary state puts positive mass on \(|x|>r=(m_1-m_0)/m_1\) (equal to \(3/2\) for the classical slopes). The additional result of the present theorem is the **quantitative outer-branch squared-speed requirement (2)**, arising from (1), together with the \(x\)-fiber calibration and its variance defect.

## Proof
Write \(L\) for the generator. Compact support and invariance imply \(\int L\Phi\,d\mu=0\) for each \(C^1\) test function \(\Phi\). Given a continuous \(\phi\) on the compact \(x\)-projection of the support, select a \(C^1\) primitive \(H\) with \(H'=\phi\). Then
\[
0=\mathbb E[LH(x)]=\alpha\mathbb E[\phi(x)(y-h(x))].
\]
As continuous test functions determine conditional expectation on a compact real range,
\(\mathbb E[y\mid x]=h(x)\). Orthogonality of conditional expectation gives
\[
\mathbb E[(y-h(x))^2]
=\operatorname{Var}(y)-\operatorname{Var}(h(x)),
\]
and the equation \(\dot x=\alpha(y-h(x))\) yields the claimed defect. The analogous primitive tests in \(y\) and \(z\) prove the first two identities in (3), which are also present in the earlier cited work. The conditional \(y\)-identity yields the \(\dot y\)-variance defect.

For (1), define \(g=y-h(x)=\dot x/\alpha\) and \(q=x-y+z=\dot y\). The composition of a Lipschitz function with each solution is absolutely continuous, and its classical derivative is \(h'(x)\dot x\) at every time away from the breakpoints. Since the vector field is Lipschitz, at a breakpoint where \(\dot x=0\) the chain-rule product relevant below is zero. More explicitly, the stationary measure carries no \(\dot x^2\)-weighted mass on \(x=1\) or \(x=-1\): on a flow-box neighborhood where the vector field crosses such a plane transversally, distinct sufficiently close time translates of the intersection with that plane are disjoint; a finite invariant measure assigns that transversal set mass zero. Exhausting the transversal subsets and observing \(\dot x=0\) on the remainder proves the claim.

The bounded absolutely continuous function \(g(t)^2/2\) has stationary mean derivative zero. Consequently,
\[
0=\mathbb E[g(q-h'(x)\dot x)]
=\alpha^{-1}\bigl(\mathbb E[\dot x\dot y]-\mathbb E[h'(x)\dot x^2]\bigr),
\]
so
\[
\mathbb E[\dot x\dot y]=\mathbb E[h'(x)\dot x^2]. \tag{4}
\]
Here \(h'\) is assigned arbitrarily at the breakplanes. Independently,
\[
\dot q=\dot x-q-\beta y.
\]
Stationarity of \(q^2/2\) yields
\[
0=\mathbb E[q\dot q]
=\mathbb E[\dot x\dot y]-\mathbb E[\dot y^2]
-\beta\mathbb E[y\dot y].
\]
Stationarity of \(y^2/2\) gives \(\mathbb E[y\dot y]=0\), hence
\[
\mathbb E[\dot x\dot y]=\mathbb E[\dot y^2]. \tag{5}
\]
Combining (4) and (5) proves (1). Because \(h'\) equals \(m_0\) on the inner branch and \(m_1\) on the outer branches, (1) becomes
\[
\mathbb E[\dot y^2]=m_0K_{\rm in}+m_1K_{\rm out}. \tag{6}
\]

We now justify strictness in (2), including measures which are not ergodic. If \(\mathbb E[\dot y^2]=0\), the continuous function \(\dot y\) vanishes throughout the invariant support. Along every trajectory in that support, \(y\) is constant. The equation \(\dot z=-\beta y\) and boundedness of each complete support trajectory force \(y=0\). Then \(q=0\) implies \(x+z=0\), and \(\dot z=0\) forces \(x\) constant and \(h(x)=0\). Thus the support consists only of equilibria. Conversely, at equilibria all coordinate speeds vanish. Any measure not supported on equilibria therefore has \(\mathbb E[\dot y^2]>0\), and likewise \(\mathbb E[\dot x^2]>0\). Equation (6) with \(m_0<0<m_1\) now implies
\[
m_1K_{\rm out}>-m_0K_{\rm in},
\]
which rearranges to (2). The numerical rational specialization follows by substitution.

For clarity about (3), conditional testing in \(z\) gives \(\mathbb E[y\mid z]=0\), so \(\mathbb E[yz]=0\). Stationarity of \(y^2/2\) yields \(\mathbb E[xy]=\mathbb E[y^2]\); conditioning \(y\) on \(x\) gives \(\mathbb E[xy]=\mathbb E[xh(x)]\); and \(\dot z=-\beta y\) gives the last expression. This is an alternative derivation of a previously established identity, not a priority claim for it.

## Verification and boundaries
The proof of (1) is an exact stationary differentiation argument, valid for every compact invariant probability measure. It does not rely on a simulated attractor, a finite sample, or the output of a checker. The boundary values \(x=\pm1\) have no \(\dot x^2\)-weighted mass, so the piecewise derivative presents no ambiguous term. At equilibrium mixtures both sides of (1) vanish, and the strict ratio in (2) is correctly restricted to the complement of those mixtures. The assumptions \(m_0<0<m_1\) are essential to the positive threshold; the conditional identities and equation (1) require only the stated continuous Lipschitz characteristic and normalization.

The packaged standard-library exact-rational checker verifies some algebraic moment steps and the classical \(3/2\) and \(1/3\) constants. Those tests do not constitute a proof of the measure-theoretic identities. No claim is made for residence-time proportions, entropy, Lyapunov exponents, arbitrary nonstationary trajectories, or the existence of an attractor.

## Relationship to literature
The 1985/1986 Chua–Komuro–Matsumoto work defines this normalized piecewise-linear system and proves rigorous double-scroll chaos through piecewise-linear geometry, return maps, homoclinic orbits, and bifurcations. An explicit counterpart of the stationary speed-slope identity (1) was not located in the inspected primary-text passages and targeted document-wide terminology searches; an exhaustive negative-coverage claim is not made. The 2016 Gribov–Kanatnikov–Krishchenko paper studies localization of compact invariant sets, but the accessible introduction specializes to a **cubic Chua nonlinearity** and its full text was not obtained; the possibility of an equivalent stationary estimate elsewhere remains a literature risk. The earlier published equilibrium-amplitude finding already establishes the sector identity and amplitude excursion in (3). The distinguishable mathematical contribution here is (1) and the new weighted-energy inequality (2), together with the \(x\)-fiber calibration.

## References
1. L. O. Chua, M. Komuro, T. Matsumoto, *The Double Scroll Family*, Berkeley report UCB/ERL M85/102 (1985), and IEEE Transactions on Circuits and Systems 33 (1986), 1072–1118, DOI 10.1109/TCS.1986.1085869.
2. *Equilibrium-amplitude excursion law for the Chua double-scroll system* (published 2026-10-04), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-equilibrium-amplitude-excursion-law-for-the-chua-double-scroll-s--fef28a2bc259 .
3. A. F. Gribov, A. N. Kanatnikov, A. P. Krishchenko, *Localization Method of Compact Invariant Sets with Application to the Chua System*, International Journal of Bifurcation and Chaos 26 (2016), 1650073, DOI 10.1142/S0218127416500735.
