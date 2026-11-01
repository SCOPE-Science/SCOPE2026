# A sharp completeness boundary and two separatrix clocks in a quintic planar flow

## Finding
Consider the planar polynomial flow
\[
\dot x=y,\qquad \dot y=-x-\beta x^5+\alpha x^3y^2,\qquad \alpha>0,\quad\beta\geq0.
\]
Set
\[
V(x)=\int_0^x e^{-\alpha s^4/2}(s+\beta s^5)\,ds,\qquad
E_*=\frac{\sqrt\pi}{2\sqrt{2\alpha}}\left(1+\frac\beta\alpha\right),
\quad H(x,y)=\frac12e^{-\alpha x^4/2}y^2+V(x).
\]
There is an **exact global orbit/completeness trichotomy**. The equilibrium \((0,0)\) is the only energy-zero state. At each energy \(0<E<E_*\), the level is one simple closed periodic orbit, with positive turning amplitude \(A\) uniquely defined by \(V(A)=E\). At \(E=E_*\), the level comprises precisely two nonperiodic, globally defined trajectories; their position traverses all of \(\mathbb R\) monotonically, taking infinite physical time toward both infinite endpoints. At every \(E>E_*\), the level again has two monotone trajectories, but each reaches spatial infinity in **finite forward and backward physical time**. There are no other trajectories.

The periodic orbit of amplitude \(A\) has minimal physical period \(T(A)\). As \(A\to\infty\),
\[
\boxed{T(A)\sim 2\sqrt\alpha\,A^2\quad(\beta=0),\qquad
T(A)\sim4\sqrt{\alpha/\beta}\,\log A\quad(\beta>0).}
\]
Equivalently, writing \(\delta=E_*-E\downarrow0\),
\[
\boxed{T(E)\sim2\sqrt2\,\sqrt{\log(E_*/\delta)}\quad(\beta=0),\qquad
T(E)\sim\sqrt{\alpha/\beta}\,\log\log(E_*/\delta)\quad(\beta>0).}
\]
Thus adding any positive quintic restoring term changes the divergent-period law from a square root of a logarithm to a double logarithm, even though all systems retain a local center.

Along either critical trajectory, oriented so that \(x(t)\to+\infty\) as \(t\to+\infty\),
\[
\boxed{x(t)\sim\sqrt{2t/\sqrt\alpha}\quad(\beta=0),\qquad
\lim_{t\to+\infty}\frac{\log x(t)}t=\sqrt{\beta/\alpha}\quad(\beta>0).}
\]
For an \(E>E_*\) trajectory advancing toward \(+\infty\) at time \(t_+<\infty\),
\[
\boxed{t_+-t\sim\frac{e^{-\alpha x(t)^4/4}}{\alpha x(t)^3\sqrt{2(E-E_*)}}.}
\]
Finally, at small amplitude,
\[
T(A)=2\pi\left[1+\frac{\alpha-5\beta}{16}A^4+O_{\alpha,\beta}(A^8)\right].
\]
In particular, whenever \(\beta>\alpha/5\), the period function attains an interior minimum strictly below \(2\pi\); every prescribed period between that minimum and \(2\pi\) occurs for at least two distinct periodic orbits. No uniqueness of the minimum is asserted.

## Assumptions and scope
All assertions concern the **original, unrescaled physical time** of the specified polynomial vector field for arbitrary fixed \(\alpha>0\) and \(\beta\ge0\). Energy levels are taken in the full plane, with no compactification points counted as ordinary states. The asymptotic statements fix parameters before taking their limits; no uniformity in \(\beta\to0\) is claimed. The critical trajectory's time origin is arbitrary; the leading limits do not depend on it. This is a global dynamical description of flow completeness and recurrence, not a classification of all local centers in a general six-parameter family.

## Proof
**1. Conservation and topology of all energy levels.** Let \(w(x)=e^{-\alpha x^4/2}\) and \(f(x)=x+\beta x^5\). The identity \(w'(x)=-2\alpha x^3 w(x)\) gives
\[
\frac{dH}{dt}= w(x)y[-\alpha x^3y^2+(-f(x)+\alpha x^3y^2)+f(x)]=0.
\]
The potential \(V\) is even, \(V(0)=0\), strictly increasing for \(x>0\), and tends to \(E_*<\infty\) as \(x\to+\infty\). Substitution \(u=s^2\) and the Gaussian integrals for \(1\) and \(u^2\) yield the stated exact ceiling. Since \(H\ge0\) and the only equilibrium is the origin, every energy below the ceiling consists of one compact smooth oval without equilibria, hence a single periodic trajectory. For energies at or above the ceiling, the energy equation
\[
y=\pm v_E(x),\qquad v_E(x):=\sqrt{2e^{\alpha x^4/2}(E-V(x))}
\]
produces exactly two positive/negative monotone components, defined over all real positions. Their maximal physical-time lengths are determined by \(\int dx/v_E(x)\).

**2. Universal asymptotic velocity and completeness.** Write
\[
R(x)=E_*-V(x)=\int_x^\infty f(s)e^{-\alpha s^4/2}\,ds.
\]
A one-sided Laplace tail estimate, proved directly by one integration by parts or l'Hôpital's rule, gives
\[
R(x)\sim\frac{f(x)}{2\alpha x^3}e^{-\alpha x^4/2}
=\frac{1+\beta x^4}{2\alpha x^2}e^{-\alpha x^4/2}\quad(x\to+\infty).
\]
Thus \(v_{E_*}(x)^2\sim(1+\beta x^4)/(\alpha x^2)\). If \(\beta=0\), \(v_{E_*}(x)\sim1/(\sqrt\alpha\,x)\), implying \(t\sim\sqrt\alpha\,x^2/2\). If \(\beta>0\), \(v_{E_*}(x)\sim\sqrt{\beta/\alpha}\,x\), implying \(t/\log x\to\sqrt{\alpha/\beta}\). Both integrals diverge at both spatial ends, because \(V\) is even and \(v_E\) depends on \(x\) only through even functions. For \(E>E_*\), instead \(v_E(x)\sim\sqrt{2(E-E_*)}\,e^{\alpha x^4/4}\). Its reciprocal is integrable at infinity and its tail is asymptotic to the stated formula, by l'Hôpital's rule. This proves all temporal-completeness and escape claims.

**3. Period formula and the outer-boundary estimate.** For \(0<E<E_*\), evenness gives the exact quadrature
\[
T(A)=4\int_0^A\frac{dx}{v_{V(A)}(x)},\qquad
v_{V(A)}(x)^2=2e^{\alpha x^4/2}\int_x^A f(s)e^{-\alpha s^4/2}\,ds.
\]
For \(x<A\), the ratio of the periodic velocity to the critical one satisfies
\[
\frac{v_{V(A)}(x)^2}{v_{E_*}(x)^2}
=1-\frac{R(A)}{R(x)}.
\]
Choose a fixed \(K>1/\alpha\) and write \(h_A=K\log A/A^3\). The explicit asymptotic for \(R(x)\) and its strict decrease show uniformly on \(0\le x\le A-h_A\) that \(R(A)/R(x)\to0\); for \(x<A/2\) this follows directly from monotonicity, and on \([A/2,A-h_A]\) from the exponential factor \(e^{-\alpha (A^4-x^4)/2}\) with the polynomial prefactors bounded. Therefore
\[
\int_0^{A-h_A}\frac{dx}{v_{V(A)}(x)}
=(1+o(1))\int_0^{A-h_A}\frac{dx}{v_{E_*}(x)}.
\]
It remains to justify removal of the turning-point strip rather than assume it is negligible. For \(A-h_A\le x\le A\) and all large \(A\), \(f(s)\ge c f(A)\) on \([x,A]\), and \(s^4-x^4\le4A^3(s-x)\), with constant \(c>0\) independent of \(A\). Hence
\[
v_{V(A)}(x)^2\ge\frac{c f(A)}{\alpha A^3}\bigl(1-e^{-2\alpha A^3(A-x)}\bigr).
\]
Integrating the reciprocal square root gives the bound
\[
\int_{A-h_A}^A\frac{dx}{v_{V(A)}(x)}
\le C\sqrt{\frac{\alpha A^3}{f(A)}}\left(h_A+\sqrt{\frac{h_A}{\alpha A^3}}\right)=o(1).
\]
This exact control includes the integrable turning-point singularity. On the critical curve, the velocity asymptotic from step 2 gives
\[
\int_0^A\frac{dx}{v_{E_*}(x)}\sim
\begin{cases}\sqrt\alpha A^2/2,&\beta=0,\\ \sqrt{\alpha/\beta}\log A,&\beta>0.\end{cases}
\]
Multiplying by four proves both amplitude-period limits.

**4. Conversion from amplitude to energy.** At the turning point, \(\delta=R(A)\), so step 2 gives
\[
\delta\sim\frac{1+\beta A^4}{2\alpha A^2}e^{-\alpha A^4/2},
\qquad \log(E_*/\delta)\sim\alpha A^4/2.
\]
For \(\beta=0\), this implies \(A^2\sim\sqrt{2/\alpha}\sqrt{\log(E_*/\delta)}\). For \(\beta>0\), it gives \(\log A\sim\tfrac14\log\log(E_*/\delta)\). Substitution into step 3 proves both logarithmic laws with their coefficients.

**5. Local period and a nonmonotonicity consequence.** The time-preserving change of coordinate
\[
z=\int_0^x e^{-\alpha s^4/4}\,ds=x-\alpha x^5/20+O(x^9)
\]
reduces the dynamics near the origin to a conservative oscillator \(\ddot z+g(z)=0\), with
\[
g(z)=e^{-\alpha x^4/4}(x+\beta x^5)
=z+(\beta-\alpha/5)z^5+O(z^9).
\]
The standard energy integral for this oscillator, expanded to fourth order in turning amplitude, is
\(2\pi[1-5(\beta-\alpha/5)A^4/16+O(A^8)]\), since the turning amplitudes of \(z\) and \(x\) differ only by \(O(A^5)\). This yields the claimed expansion. If \(5\beta>\alpha\), the period immediately falls below \(2\pi\), whereas step 3 proves it diverges. By continuity the period attains an interior minimum below \(2\pi\), and each intermediate level has at least two preimages, one on each side of a minimizer.

## Verification
The accompanying `verify.py` symbolically verifies the conservation identity and the fifth-order transformed oscillator coefficient. It also evaluates the full period quadrature numerically from a stable integral representation at amplitudes up to five, comparing both divergent scales; these finite values are corroborative and are not substituted for the uniform boundary-layer proof. The equality of the potential ceiling with the Gaussian integral is checked symbolically. All calculations refer to the precise equations and parameters in this document.

## Relationship to prior work
Da Cruz and Llibre [1] classified the centers and global centers in a six-parameter quintic family; their Theorems 1 and 2 show that the positive coefficient of \(x^3y^2\) considered here is on a **local-center but non-global-center** locus. Their proof identifies orbit directions at infinity through compactification, but does not give the complete energy-level partition, distinguish critical infinite-time traversal from supercritical finite-time escape, or calculate the two sharply different physical-time period laws. A previously published calculation [2] treats the **opposite sign** of the same velocity-squared coefficient: its global-center energy potential diverges at infinity and its periods decrease to zero. Its theorem therefore does not imply the finite-ceiling or diverging-period statements here. The Jacobi-multiplier/position-dependent-mass change of variables is classical [3] and is not claimed as new. The contribution is the combined exact completeness trichotomy, sharp critical time scales, and two-regime separatrix period asymptotic in the positive-coefficient local-center family. The 2013 period-function paper [4] concerns general criteria rather than the specific explicit boundary constants here; complete priority across differently formulated literature cannot be guaranteed.

## Limitations
The system has been reduced to a two-parameter quintic subfamily. No claim is made for general additional quintic terms or negative \(\beta\). The outer period asymptotic is not uniform as \(\beta\downarrow0\), and no assertion is made about the uniqueness or location of the period minimum. The proof does not classify invariant measures beyond the evident equilibrium and periodic measures. A comparable result may exist in unindexed or inaccessible literature. Independent mathematical audit has not been performed.

## References
1. L. P. C. da Cruz and J. Llibre, *Global Centers in a Class of Quintic Polynomial Differential System*, arXiv:2312.05709v1 (first public 2023-12-09), https://arxiv.org/html/2312.05709v1, Theorems 1–2 and Section 4; later published with DOI 10.1017/prm.2024.43.
2. *Strict period decrease and sharp large-amplitude laws for quintic global centers*, mathematical research record, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-strict-period-decrease-and-sharp-large-amplitude-laws-for-quinti--ffe383da977f/RESULT.md (published 2026-10-11).
3. S. Chanda, A. Ghose-Choudhury, and P. Guha, *Jacobi-Maupertuis metric of Liénard type equations and Jacobi Last Multiplier*, Electronic Journal of Differential Equations 2018, no. 120, https://ejde.math.txstate.edu/Volumes/2018/120/chanda.pdf.
4. L.-J. Yang and X.-W. Zeng, *The period function of Liénard systems*, Proceedings of the Royal Society of Edinburgh A 143 (2013), 205–221, DOI 10.1017/S0308210511000096.
