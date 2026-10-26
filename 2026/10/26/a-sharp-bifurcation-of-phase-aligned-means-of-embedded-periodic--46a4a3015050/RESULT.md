# A sharp bifurcation of phase-aligned means of embedded periodic orbits

## Finding
Let \(H=L^2(\mathbb R/2\pi\mathbb Z;\mathbb C)\), with normalized norm \(\|u\|_2^2=(2\pi)^{-1}\int_0^{2\pi}|u(t)|^2\,dt\). Circular time shifts act by \((S_\theta u)(t)=u(t+\theta)\); on the quotient \(\mathcal Q=H/S^1\) use \(d([u],[v])=\min_\theta\|u-S_\theta v\|_2\). For \(k\ge2\) and \(0<\varepsilon<1\), consider the two smoothly embedded, regularly parametrized loops
\[
\gamma_{\pm,k}(t)=(1\pm\varepsilon\cos kt)e^{it}.
\]
For their equally weighted two-sample Fréchet functional \(\mathcal F([z])=\tfrac12 d([z],[\gamma_{+,k}])^2+\tfrac12d([z],[\gamma_{-,k}])^2\), the following hold.

**Sharp two-lobe classification.** When \(k=2\), put \(a=\varepsilon^2\) and \(a_c=2/5\). If \(0<a\le a_c\), there is exactly one Fréchet mean class, represented by the unit circle \(m_0(t)=e^{it}\). If \(a_c<a<1\), there are exactly two distinct mean classes represented by
\[
 m_{\pm\theta_a}(t)=\tfrac12[\gamma_{+,2}(t)+\gamma_{-,2}(t\pm\theta_a)],\qquad
 \theta_a=\arccos\sqrt{\frac{2+a}{6a}}\in(0,\pi/4).
\]
Writing \(M(a)=1-a/2\) for \(a\le a_c\) and \(M(a)=(2+a)^{3/2}/(3\sqrt{6a})\) for \(a>a_c\), the exact minimal Fréchet variance is \(\mathcal V(a)=(2+a-2M(a))/4\). The angular branches emerge with \(\theta_a\sim(5/\sqrt{12})\sqrt{a-a_c}\) as \(a\downarrow a_c\) from above. At the boundary, the optimal alignment has a strictly negative quartic departure, rather than a quadratic one. The gain in minimal variance over the unshifted circle is \(a/2-\mathcal V(a)\sim(125/192)(a-a_c)^2\).

**Instability of uniqueness arbitrarily close to a circle.** For any integer \(k\ge2\), if \(\varepsilon^2>2/(k^2+1)\), the two-sample functional has at least two distinct Fréchet mean classes. Consequently, for every \(\eta>0\), two real-analytic embedded loops can lie within uniform distance \(\eta\) of the unit-circle parametrization, while their two-sample phase-shift Fréchet mean is nonunique. Each input loop is realizable as an exponentially attracting periodic orbit of a smooth autonomous planar vector field (the two fields may differ).

## Assumptions and scope
Only circular **time shifts** are quotiented out; ambient-plane rotations, general reparametrizations, and arc-length reparametrization are not. The loops are sampled in the uniform-angle time coordinate \(t\), of fundamental period \(2\pi\). The Fréchet means are sought in the full Hilbert quotient \(\mathcal Q\), not restricted to embedded loops. In all assertions \(k\) is an integer, \(k\ge2\), and \(0<\varepsilon<1\), so \(1\pm\varepsilon\cos kt>0\) and both input loops are regular analytic embeddings. Distinct means are distinct classes under parameter shifts alone.

## Proof
**1. Exact reduction to pairwise alignment.** Write \(A=[\gamma_{+,k}]\), \(B=[\gamma_{-,k}]\), and \(D=d(A,B)\). For any \(Z\in\mathcal Q\), the triangle inequality and the scalar quadratic inequality give
\[
\mathcal F(Z)=\tfrac12[d(Z,A)^2+d(Z,B)^2]\ge\tfrac14[d(Z,A)+d(Z,B)]^2\ge D^2/4.
\]
Choose an optimal phase \(\theta\) between representatives and form \(m_\theta=(\gamma_{+,k}+S_\theta\gamma_{-,k})/2\). Its two distances to \(A,B\) are at most \(D/2\), so \([m_\theta]\) attains the bound. Conversely, if \([z]\) is a minimizer, compactness of the shift circle permits representatives \(u\in A\), \(v\in B\) at the respective nearest distances to a chosen representative of \(z\). The Hilbert parallelogram identity implies
\[
\|z-u\|_2^2+\|z-v\|_2^2\ge\tfrac12\|u-v\|_2^2\ge D^2/2.
\]
Equality is forced throughout, hence \(z=(u+v)/2\) and \(\|u-v\|_2=D\). Thus **all** global Fréchet means, not merely some, are precisely midpoint classes of optimal phase alignments.

**2. Fourier alignment identity.** Orthogonality of the three modes \(1,1+k,1-k\) yields \(\|\gamma_{\pm,k}\|_2^2=1+\varepsilon^2/2\) and the real cross-correlation
\[
C_k(\theta)=\operatorname{Re}\langle\gamma_{+,k},S_\theta\gamma_{-,k}\rangle
=\cos\theta\left(1-\frac{\varepsilon^2}{2}\cos k\theta\right).
\]
Consequently \(D^2=2+\varepsilon^2-2\max_\theta C_k(\theta)\) and \(\inf\mathcal F=D^2/4\).

**3. Global two-lobe maximizers.** For \(k=2\), set \(a=\varepsilon^2\) and \(x=\cos\theta\in[-1,1]\). Then
\[
C_2(\theta)=P_a(x),\quad P_a(x)=(1+a/2)x-ax^3=x(1+a/2-ax^2).
\]
Since \(0<a<1\), the last factor is strictly positive, so a maximizing \(x\) is nonnegative. On \([0,1]\), \(P_a'(x)=1+a/2-3ax^2\) strictly decreases. It stays nonnegative exactly for \(a\le2/5\), giving only \(x=1\), i.e. only zero phase. Above \(2/5\), its unique positive zero is \(x_a=\sqrt{(2+a)/(6a)}\in(0,1)\); the two and only two maximizing phases are \(\pm\theta_a\). Substitution gives the piecewise \(M(a)\) and \(\mathcal V(a)\) claimed. Taylor expansion of \(x_a\), or of \(P_a\) at \(x=1\), gives \(\theta_a^2\sim25(a-2/5)/12\) and \(M(a)-(1-a/2)\sim125(a-2/5)^2/96\). At \(a=2/5\), the correlation satisfies \(C_2(\theta)=C_2(0)-(3/10)\theta^4+O(\theta^6)\).

**4. Distinctness of the midpoint classes.** For any \(k\), the Fourier coefficient of \(m_\theta\) at mode \(1\) is \((1+e^{i\theta})/2\), while those at modes \(1\pm k\) are \((\varepsilon/4)(1-e^{i(1\pm k)\theta})\). Suppose \(0<\theta<\pi\) and \([m_\theta]=[m_{-\theta}]\). The nonzero mode-\(1\) coefficient forces the identifying shift to be \(-\theta\pmod{2\pi}\). At every nonzero additional coefficient, however, the ratio of negative-phase to positive-phase coefficients equals \(-e^{-i(1\pm k)\theta}\), contradicting the factor \(e^{-i(1\pm k)\theta}\) required by that shift. At least one additional coefficient is nonzero: simultaneous vanishing would imply both \((k+1)\theta\) and \((k-1)\theta\) are multiples of \(2\pi\); since their greatest common divisor is at most two, this is impossible for \(0<\theta<\pi\). Hence the two mean classes in the two-lobe regime are genuinely distinct.

**5. High-frequency near-circle obstruction.** Differentiating the exact correlation gives
\[
C_k''(0)=-1+\frac{\varepsilon^2(k^2+1)}{2}.
\]
When this is positive, zero phase is a strict local minimum, not an optimum. The correlation is even, and \(C_k(\pi)<C_k(0)\) for \(0<\varepsilon<1\). Therefore at least one global maximum occurs at some \(0<\theta<\pi\), and its negative is also a maximum. Step 4 proves their midpoint classes are different. Given \(\eta>0\), choose \(k\) large enough that \(\sqrt{2/(k^2+1)}<\min\{\eta,1\}\), and choose \(\varepsilon\) strictly between these two numbers. Then \(\|\gamma_{\pm,k}-e^{it}\|_\infty=\varepsilon<\eta\), yet the means are not unique.

**6. Dynamical realizability.** In a positive-radius annulus, put \(R_\pm(\vartheta)=1\pm\varepsilon\cos(k\vartheta)\) and define \(\dot\vartheta=1\), \(\dot r=R_\pm'(\vartheta)-\lambda(r-R_\pm(\vartheta))\), for any fixed \(\lambda>0\). The radial error \(r-R_\pm(\vartheta)\) obeys \(\dot e=-\lambda e\). Thus \(r=R_\pm(\vartheta)\) is an exact regular attracting limit cycle with transverse Floquet multiplier \(e^{-2\pi\lambda}\). A radial cutoff extends each annular field smoothly to the plane without changing this local orbit. The two cycles are not asserted to coexist in one planar flow.

## Verification
The standalone \(\texttt{verify_phase_means.py}\) reconstructs the Fourier correlation by periodic quadrature for several harmonics and phases, checks polynomial stationary-point identities, compares complete numerical phase scans against the exact two-lobe maximum, checks the near-circle high-frequency sign test, and verifies phase-shift inequivalence numerically for a representative supercritical case. The proof above, not finite sampling or those tests, establishes the unbounded claims and exact equality cases. Run \(\texttt{python3 verify_phase_means.py}\) with Python's standard library.

## Relationship to prior work
Hering and Kuehn (2026) define the phase-shift quotient metric on periodic-trajectory curves, prove existence of empirical Fréchet means, and explain that quotient means need not generally be unique. The quotient definition, existence facts, and generic possibility of nonuniqueness are prior work, not claims of novelty here. The contribution is the exact two-lobe **global** uniqueness-to-two-means transition for regular embedded periodic orbits, its variance law and critical scaling, and nonuniqueness for pairs arbitrarily close to a common circle in the time-parametrized uniform norm. Doğan, Bernal, and Hagwood (2015; arXiv version 2025) develop phase/rotation alignment algorithms for closed planar shapes; their setting additionally quotients ambient rotations and uses arc-length sampling, so its optimization is not equivalent to the fixed-frame phase-only quotient studied here.

## Limitations
This is an exact deterministic two-sample construction; it does not classify arbitrary ensembles or establish statistical estimation performance. The high-frequency result is a sufficient condition for nonuniqueness, not a converse for every harmonic \(k\). Near-circle means uniform convergence of the input *parametrizations*; it does not claim \(C^1\)-small perturbations or uniqueness failure under an arc-length or ambient-rotation quotient. The dynamical realizations concern two potentially different planar flows. Independent historical-priority verification has not been performed.

## References
1. P. S. Hering and C. Kuehn, *Fréchet Means of Periodic Orbits in Dynamical Systems: Geometry, Dynamics, and Diagnostics*, arXiv:2606.10748v1, first public 2026-06-09. https://arxiv.org/abs/2606.10748 . Specifically quotient definitions in Section 3, nonuniqueness discussion in Section 3.1, computational method in Section 4, and geometric diagnostics in Section 6.
2. G. Doğan, J. Bernal and C. R. Hagwood, *FFT-based Alignment of 2d Closed Curves with Application to Elastic Shape Analysis*, DIFF-CV 2015; open arXiv record arXiv:2501.17779. https://arxiv.org/abs/2501.17779 . Its rigid rotation and starting-point alignment are differentiated from time-phase-only quotient means.
