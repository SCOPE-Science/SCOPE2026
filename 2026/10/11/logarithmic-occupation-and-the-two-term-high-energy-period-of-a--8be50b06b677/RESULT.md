# Logarithmic occupation and the two-term high-energy period of a cubic global center

## Finding
For every fixed \(a\in\mathbb R\) and \(k>a^2\), the cubic system
\[
\dot x=(1+2ax+kx^2)y,\qquad
\dot y=-x+ax^2-kx^3-(a+kx)y^2
\]
is a global Hamiltonian center. On the periodic orbit of energy \(E>0\), let \(T(E)\) be the *minimal period in the displayed physical time*. Then
\[
\boxed{\lim_{E\to\infty}\left[\sqrt{\frac{kE}{2}}\,T(E)-\frac12\log\left(\frac{4E}{k}\right)\right]
=\log\left(\frac{8k^2}{k-a^2}\right).}
\]
Write \(s_E=(4E/k)^{1/4}\), and sample \(t\) uniformly in one period. The joint random variable
\[
\left(\frac{\log(1+|x(t)|)}{\log s_E},\operatorname{sgn}(x(t))\right)
\]
converges weakly to a uniform \([0,1]\) variable independent of a fair sign. In particular, for every fixed \(0<u<1\), the fraction of each period spent in either of the intervals \(0<x<s_E^u-1\) and \(1-s_E^u<x<0\) converges to \(u/2\). The two-term period constant depends nontrivially on the discriminant \(k-a^2\).

## Assumptions and scope
All variables and parameters are real. Fix \(a\in\mathbb R\) and \(k>a^2\), and put
\[
q(x)=1+2ax+kx^2,\qquad V(x)=\frac{x^2}{2}-\frac{ax^3}{3}+\frac{kx^4}{4},\qquad H(x,y)=\frac12q(x)y^2+V(x).
\]
The strict condition \(k>a^2\) implies \(q(x)>0\) and \(1-ax+kx^2>0\) for all real \(x\). Hence \(V'(x)=x(1-ax+kx^2)\) has the sign of \(x\), \(V(x)\to+\infty\) on both sides, and each \(E>0\) has exactly two turning points \(B(E)<0<A(E)\) satisfying \(V(B)=V(A)=E\). These imply a single smooth periodic oval. All asymptotic assertions take \(E\to\infty\) with \(a,k\) fixed. They do not cover the degenerate boundary \(k=a^2\) or parameter-dependent approaches to it.

## Proof
**1. First integral and physical-time quadrature.** Hamilton's equations \(\dot x=\partial_yH\), \(\dot y=-\partial_xH\) give exactly the displayed cubic vector field: \(q'(x)/2=a+kx\). Consequently \(dH/dt=0\), and the positive-energy ovals are periodic. Along either traversal, \(y=\pm\sqrt{2(E-V(x))/q(x)}\) and
\[
|\dot x|=\sqrt{2q(x)(E-V(x))}.
\]
The two passages over each interior position yield the *original-time* period
\[
T(E)=\sqrt2\int_{B(E)}^{A(E)}\frac{dx}{\sqrt{q(x)}\sqrt{E-V(x)}}.
\tag{1}
\]
The corresponding normalized physical-time position law is the integrand of (1) divided by its integral.

**2. Exact mass integral.** Set \(s=(4E/k)^{1/4}\) and
\[
J(E)=\int_{B(E)}^{A(E)}\frac{dx}{\sqrt{q(x)}\sqrt{1-V(x)/E}}.
\]
By (1), \(T(E)=\sqrt{2/E}\,J(E)\). Because \(V(x)/(kx^4/4)\to1\) as \(|x|\to\infty\), the turning points satisfy \(A(E)/s\to1\) and \(-B(E)/s\to1\). Decompose \(J=J_0+J_1\), where
\[
J_0=\int_B^A\frac{dx}{\sqrt q},\qquad
J_1=\int_B^A\frac{(1-V(x)/E)^{-1/2}-1}{\sqrt q}\,dx.
\]
Writing \(\Delta=k-a^2>0\), the exact antiderivative gives
\[
J_0=\frac1{\sqrt k}\left[\operatorname{arsinh}\left(\frac{kA+a}{\sqrt\Delta}\right)-\operatorname{arsinh}\left(\frac{kB+a}{\sqrt\Delta}\right)\right]
=\frac1{\sqrt k}\left(2\log s+\log\frac{4k^2}{\Delta}+o(1)\right).
\tag{2}
\]

**3. The endpoint correction.** We claim
\[
J_1\longrightarrow \frac{2}{\sqrt k}\int_0^1\frac{(1-u^4)^{-1/2}-1}{u}\,du=\frac{\log2}{\sqrt k}.
\tag{3}
\]
Here is the needed justification at both nonuniform endpoints. For every sufficiently small fixed \(\varepsilon>0\), on \(|x|\le\varepsilon s\) one has \(0\le V(x)/E\le1/2\) for all large \(E\). Since \(q(x)\ge c(1+x^2)\) for some fixed \(c>0\), the elementary bound \((1-z)^{-1/2}-1\le C z\) on \([0,1/2]\) and polynomial growth \(V(x)\le C(x^2+|x|^3+x^4)\) show that this central portion of \(J_1\) is bounded by \(C\varepsilon^4+o(1)\). On \(\varepsilon s\le|x|\le\max\{A,-B\}\), substitute \(x=\pm su\). Away from the two turning points, \(q(\pm su)/(ks^2u^2)\to1\) and \(V(\pm su)/E\to u^4\) uniformly. At either turning point, \(d(V(\pm su)/E)/du\to4\) in magnitude, so the integrands are bounded locally by a constant times the inverse square root of distance to the moving endpoint; this is uniformly integrable. Dominated convergence on both signs, followed by \(\varepsilon\downarrow0\), proves the first equality of (3). Substituting \(z=u^4\), then \(w=\sqrt{1-z}\), evaluates the one-sided integral to \((\log2)/2\). Combining (2) and (3),
\[
\sqrt k J(E)=2\log s+\log\frac{8k^2}{\Delta}+o(1)
=\frac12\log\frac{4E}{k}+\log\frac{8k^2}{k-a^2}+o(1).
\]
Together with \(T(E)=\sqrt{2/E}J(E)\), this is the asserted sharp period law.

**4. Occupation on logarithmic position scales.** For any \(0<u<1\), put \(M=s^u-1\). Uniformly for \(|x|\le M\), \(V(x)/E\to0\); indeed \(M^4/E\to0\). The normalized physical-time fraction of either signed interval, using the quadrature density from (1), is
\[
\frac{\displaystyle\int_0^M\frac{dx}{\sqrt{q(\pm x)}\sqrt{1-V(\pm x)/E}}}{J(E)}.
\]
For each sign, the numerator equals \((\log M)/\sqrt k+O(1)+o(\log s)=(u/\sqrt k)\log s+o(\log s)\). Step 3 gives \(J(E)\sim (2/\sqrt k)\log s\), so both ratios tend to \(u/2\). The same conclusion with \(u\uparrow1\) shows each sign has limiting probability \(1/2\). Their joint distribution functions at interior continuity points therefore converge to those of an independent fair sign and \(\operatorname{Unif}[0,1]\); tightness follows because \(A/s\to1\) and \(-B/s\to1\). This proves the weak law.

## Verification
The identity \(H_x\dot x+H_y\dot y=0\) is exact. A standalone standard-library numerical checker included with the result reconstructs both energy turning points, evaluates (1) by a smooth angular substitution, and checks convergence of the two-term constant for several admissible parameter pairs. The checker is a finite numerical cross-check, *not* the proof of either infinite-energy assertion; the proof is Steps 1–4 above. An additional consequence is that, for the trajectory starting at \((A,0)\), \(T(V(A))\sim 4\sqrt2\,(\log A)/(kA^2)\) as \(A\to\infty\).

## Relationship to prior work
Llibre and Rondón (2023, Theorem 2(c), equation (23)) classified this exact cubic family as a global center under \(k>a^2\), using the paper's parameters \(a=a_1\), \(k=-c_1\). Their qualitative existence result is fully credited. The present claim concerns the distinct quantitative high-energy, original-time period and occupation measure, including a nonleading constant. Ghose-Choudhury and Guha (2016, formula (2.1)) developed general position-dependent-mass period quadratures and monotonicity criteria; the quadrature is credited as a general framework. The two-term discriminant-dependent asymptotic and joint logarithmic-scale distribution require the separate endpoint analysis in Step 3 and are not stated there. García-Saldaña, Llibre and Valls (2019) classified the homogeneous-cubic subclass, which overlaps the special case \(a=0\), but their classification does not establish the high-energy constant or occupation law. The explicit quantitative statement is not claimed to be the first conceivable equivalent derivation; independent publication priority has not been certified.

## Limitations
All assertions use fixed \(a\) and \(k>a^2\) and concern only the high-energy limit. The analysis supplies neither a uniform bound as \(k\downarrow a^2\) nor a global monotonicity theorem for the full period function. It does not claim uniqueness of the phenomenon across all polynomial centers. Finite checker values do not certify asymptotic quantifiers. Possible unindexed or differently normalized earlier asymptotics remain a priority risk.

## References
1. J. Llibre and G. Rondón, *Global centers of a class of cubic polynomial differential systems*, arXiv:2310.07454v1 (first public 2023-10-11), Theorem 2(c), equation (23). https://arxiv.org/html/2310.07454v1
2. A. Ghose-Choudhury and P. Guha, *Monotonicity of the period function of the Liénard equation of second kind*, arXiv:1608.02910v1 (2016), Section 2, formula (2.1). https://arxiv.org/html/1608.02910v1
3. J. D. García-Saldaña, J. Llibre and C. Valls, *Linear type global centers of linear systems with cubic homogeneous nonlinearities*, Rend. Circ. Mat. Palermo (2019 publication), DOI:10.1007/s12215-019-00433-0, https://ddd.uab.cat/pub/artpub/2019/221314/GarLliVal2018_Preprint.pdf
