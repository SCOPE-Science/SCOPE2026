# Exact Haar-qutrit near-orthogonality law for harmonic unitary evolution

## Finding

For a uniformly random *complex* pure qutrit with a three-level harmonic Hamiltonian, the probability that its free orbit comes within squared fidelity \(\varepsilon\) of an orthogonal state has the exact one-dimensional expression
\[
\boxed{\displaystyle
P_3(\varepsilon)=h+\int_h^1
\left[\frac{w+h^2-\sqrt{(1-h^2)(w^2-h^2)}}2\right]^{1/2}dw,\quad h=\sqrt\varepsilon,\quad0\le\varepsilon\le1.}
\]
The small-tolerance constant is \(\lim_{\varepsilon\downarrow0}P_3(\varepsilon)/\sqrt\varepsilon=7/3\). For a complex Haar qubit with any nondegenerate two-level Hamiltonian, \(P_2(\varepsilon)=\sqrt\varepsilon\). Consequently the sharp relative enhancement in the qutrit is \(7/3\). The two contributions \(1\) and \(4/3\) in that constant correspond to distinct geometric portions of the near-orthogonality region.

## Assumptions and scope

The Hilbert space is \(\mathbb C^3\), the Hamiltonian is \(H=\hbar\omega\operatorname{diag}(0,1,2)\) with \(\omega>0\), and the initial ray \(|\psi\rangle\) has the unitarily invariant Fubini–Study (complex Haar) law. Set
\[
F_*(\psi)=\min_{t\in\mathbb R}\left|\langle\psi|e^{-itH/\hbar}|\psi\rangle\right|^2,
\qquad P_3(\varepsilon)=\Pr\{F_*\le\varepsilon\}.
\]
The minimum is attained because the orbit is periodic. If \(p_j=|\langle j|\psi\rangle|^2\), then \((p_0,p_1,p_2)\) is uniform on the probability simplex, with density \(2\) in the coordinates \((p_0,p_1)\). The phases of the initial amplitudes do not enter \(F_*\). This is not the real-Gaussian-amplitude sampling law used for the two-level calculation in the motivating work [1].

## Proof

**1. Reduction to a real quadratic.** Put \(\theta=\omega t\), \(y=p_1\), \(s=1-y\), \(d=p_0-p_2\), and \(c=\cos\theta\). Multiplying the overlap by \(e^{-i\theta}\) leaves its modulus unchanged, so
\[
\left|p_0+p_1e^{i\theta}+p_2e^{2i\theta}\right|^2
=(y+sc)^2+d^2(1-c^2)
=y^2+d^2+2ysc+(s^2-d^2)c^2.
\]
Here \(0\le y\le1\) and \(|d|\le s\). Set \(w=1-2y=s-y\), \(z=d^2\). The quadratic is convex because \(s^2-z\ge0\). Its vertex lies in \([-1,1]\) precisely when \(y\le1/2\) and \(z\le sw\), apart from harmless equalities and degenerate boundaries. In that region
\[
F_*=y^2+z-\frac{y^2s^2}{s^2-z}
=\frac{z(w-z)}{s^2-z};
\]
outside it the minimum occurs at \(c=-1\) and equals \(w^2\). Boundary cases follow by continuity. On \(0\le z\le sw\), the derivative of the interior formula has numerator \((z-sw)(z-s)\ge0\), so \(F_*\) increases from \(0\) to \(w^2\). This establishes all relevant monotonicity without assuming a numerical global optimizer.

**2. Haar measure and threshold geometry.** The map \((p_0,p_1)\mapsto(y,d)\), with \(p_0=(1-y+d)/2\), has Jacobian magnitude \(1/2\). The Haar probability density in \((y,d)\) is therefore exactly \(1\) on \(0\le y\le1\), \(|d|\le1-y\).

Fix \(0<h<1\). If \(|w|\le h\), the test phase \(\theta=\pi\) gives \(F_*\le w^2\le h^2\), and the whole \(d\)-interval qualifies. Its measure is
\[
\int_{(1-h)/2}^{(1+h)/2}2(1-y)\,dy=h.
\]
If \(w<-h\), the vertex is unavailable and the minimum \(w^2\) exceeds \(h^2\); no point qualifies. If \(w>h\), the endpoint minimum exceeds \(h^2\), and the interior monotonicity shows that \(F_*\le h^2\) exactly when \(0\le z\le z_-(w,h)\), where \(z_-\) is the smaller root of
\[
z^2-(w+h^2)z+h^2s^2=0.
\]
Because \(4s^2=(1+w)^2\), the discriminant is \((1-h^2)(w^2-h^2)\), and
\[
z_-(w,h)=\frac{w+h^2-\sqrt{(1-h^2)(w^2-h^2)}}2,
\qquad h<w\le1.
\]
The allowed \(d\)-interval has length \(2\sqrt{z_-}\); the coordinate change \(y=(1-w)/2\) gives its mass \(\int_h^1\sqrt{z_-}\,dw\). Adding the strip establishes the displayed exact formula. At \(h=0\) and \(h=1\) it extends continuously to \(0\) and \(1\), respectively.

**3. Sharp small-tolerance constant.** Rationalizing the smaller quadratic root yields, with \(s=(1+w)/2\),
\[
\frac{\sqrt{z_-(w,h)}}h=
\frac{\sqrt2\,s}{\sqrt{w+h^2+\sqrt{(1-h^2)(w^2-h^2)}}}.
\]
At every fixed \(0<w\le1\), the right-hand side tends to \(s/\sqrt w\) as \(h\downarrow0\). It is at most \(\sqrt2\,s/\sqrt w\) on \(h\le w\le1\), an integrable dominating function. Extend the integrand by zero on \(0<w<h\) and apply dominated convergence. Then
\[
\lim_{h\downarrow0}\frac{P_3(h^2)}h
=1+\int_0^1\frac{1+w}{2\sqrt w}\,dw
=1+\frac43=\frac73.
\]

**4. Two-level comparison and exact zeros.** For a complex Haar qubit the excitation population \(p\) is uniform on \([0,1]\), and the minimum return fidelity is \((2p-1)^2\), giving \(P_2(h^2)=h\) exactly. The qutrit return amplitude vanishes precisely on the union \(p_1=1/2\) and \(p_0=p_2\), \(p_1\le1/2\), up to intersections and zero-measure boundaries. These two branches explain why the three-level small-tolerance constant has two positive contributions.

## Verification

The self-contained program `verify.py` checks exact optimizer formulas against direct phase-grid minimization, independently integrates the CDF, tests the boundary cases, and compares finite Haar-simplex simulations against the analytic values. For example, \(P_3(0.01)=0.2020638949345\ldots\), \(P_3(0.04)=0.3742906235963\ldots\), and \(P_3(0.25)=0.7584183762028\ldots\). A finite check cannot establish the exact distribution or the asymptotic constant; those follow from the proof above.

## Relationship to prior work

Morley-Short, Rosenfeld and Kok [1] define maximum distinguishability over free-evolution orbits and study the *same harmonic energy spectrum* in low dimensions. Their higher-dimensional results are numerical; their analytic two-level distribution uses a real-Gaussian-amplitude ensemble, which is not the complex Haar measure used here. This finding supplies the exact complex-Haar three-level probability and its sharp near-orthogonality constant.

Dunkl and collaborators [2] describe the numerical shadow of a **fixed** operator under complex Haar sampling, including its simplex interpretation for normal operators and projected qutrit dynamics. Puchała and collaborators [3] study restricted numerical shadows and trajectories of entangled systems. A time-minimized return fidelity is a nonlinear infimum over the family of operators \(e^{-itH/\hbar}\), not a fixed-operator shadow. These works supply background geometry but do not, in their examined treatments, state the probability above. No claim of exhaustive priority verification is made.

## Limitations

The result requires the unitarily invariant **complex** pure-state measure and exactly equally spaced nondegenerate energies. It does not describe random real-amplitude states, mixed states, different gaps, finite observation windows, or larger Hilbert-space dimensions. The formula is a convergent one-dimensional integral, not an elementary closed form. A hidden equivalent formula in the wider literature remains possible; the literature comparison is not independent certification.

## References

[1] S. Morley-Short, L. Rosenfeld and P. Kok, *Unitary evolution and the distinguishability of quantum states*, arXiv:1409.2244v1 (public 2014-09-08); Phys. Rev. A 90, 062116 (2014). https://arxiv.org/abs/1409.2244

[2] C. F. Dunkl, P. Gawron, J. A. Holbrook, J. A. Miszczak, Z. Puchała and K. Życzkowski, *Numerical shadow and geometry of quantum states*, arXiv:1104.2760v1 (public 2011-04-14). https://arxiv.org/abs/1104.2760

[3] Z. Puchała, J. A. Miszczak, P. Gawron, C. F. Dunkl, J. A. Holbrook and K. Życzkowski, *Restricted numerical shadow and geometry of quantum entanglement*, arXiv:1201.2524v2 (2012). https://arxiv.org/abs/1201.2524
