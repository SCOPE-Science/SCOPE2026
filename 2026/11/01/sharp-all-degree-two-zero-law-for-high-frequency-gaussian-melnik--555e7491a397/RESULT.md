# Sharp all-degree two-zero law for high-frequency Gaussian Melnikov splitting

## Finding

Consider the randomly forced Duffing oscillator
\[
\ddot y+\varepsilon\delta\dot y-y+y^3=\varepsilon\sum_{k=1}^{N}\left(a_k\cos(k\omega t)+b_k\sin(k\omega t)\right),
\]
where \(N\ge1\) is any integer, \(\omega>0\), and \(\delta,a_1,b_1,\ldots,a_N,b_N\) are independent standard real Gaussian variables. Let \(Z_{N,\omega}\) be the number of zeros, in one forcing period, of the first-order right-homoclinic Melnikov function (counting distinct zeros; almost surely all are simple). Define
\[
q=\exp(-\pi\omega/2),\qquad t=\frac{3\sqrt2\pi\omega}{4}\operatorname{sech}(\pi\omega/2).
\]
For every \(\omega>0\) and every \(N\ge1\),
\[
\left|\mathbb P(Z_{N,\omega}\ge1)-\frac{t}{\sqrt{1+t^2}}\right|
\le \frac{3\sqrt2\pi\omega}{2}\frac{q^2(2-q)}{(1-q)^2}.
\tag{1}
\]
Furthermore, for every \(N\ge1\),
\[
\mathbb P(Z_{N,\omega}\ge4)
\le 8\left(\frac{1+q^2}{q}\sum_{k=2}^{\infty}(k^2+k^3)q^k\right)^2.
\tag{2}
\]
The bounds are independent of \(N\), including when \(N\) depends arbitrarily on \(\omega\). Consequently, uniformly in \(N\ge1\) as \(\omega\to\infty\),
\[
\boxed{\mathbb P(Z_{N,\omega}=2)
=\frac{3\pi}{\sqrt2}\,\omega\exp(-\pi\omega/2)
+O\!\left(\omega\exp(-\pi\omega)\right),}
\tag{3}
\]
whereas \(\mathbb P(Z_{N,\omega}\ge4)=O(\exp(-\pi\omega))\). Thus the rare high-frequency first-order separatrix-crossing events are asymptotically exhausted by exactly two transverse Melnikov zeros, with a sharp explicit prefactor. The formula concerns Melnikov zeros, not a uniform-in-\(\omega\) finite-\(\varepsilon\) horseshoe probability.

## Assumptions and scope

The random coefficients are independent, identically distributed \(N(0,1)\) real random variables; \(N\) is a finite positive integer (possibly selected as a function of \(\omega\)). A zero is counted once per distinct phase \(\theta\in[0,2\pi)\), with endpoints identified. The perturbation parameter \(\varepsilon\) does not enter the first-order Melnikov function; for each fixed realization and fixed \(\omega,N\), a simple zero gives a transverse perturbed separatrix intersection for sufficiently small \(\varepsilon>0\). The theorem does not assert a uniform choice of \(\varepsilon\) over frequencies or random draws. The classification is primarily \(37\mathrm{C}29\).

## Proof

**1. Normalization and Gaussian offset.** The right-loop Melnikov integral, as evaluated in the motivating work, is
\[
M_{N,\omega}(\theta/\omega)=-\frac43\delta+U_N(\theta),\quad
U_N(\theta)=\sum_{k=1}^N s_k\bigl(a_k\sin(k\theta)-b_k\cos(k\theta)\bigr),
\]
\[
s_k=\sqrt2\pi\omega k\operatorname{sech}(\pi k\omega/2)>0.
\]
Writing \(m_N=\min U_N\), \(M_N=\max U_N\), and letting \(\Phi\) be the standard-normal distribution function, independence of \(\delta\) gives the exact identity
\[
\mathbb P(Z_{N,\omega}\ge1)=
\mathbb E\left[\Phi\left(\tfrac34 M_N\right)-\Phi\left(\tfrac34m_N\right)\right].
\tag{4}
\]
The trigonometric polynomial is nonconstant almost surely. Conditional on its coefficients, critical values form a finite set, so the Gaussian offset hits any of them with probability zero. All zeros are consequently simple almost surely, and periodicity makes their number even.

**2. Exact one-harmonic probability.** When \(N=1\), the forcing harmonic is a sinusoid of amplitude \(s_1R\), with \(R=\sqrt{a_1^2+b_1^2}\) Rayleigh-distributed independently of \(\delta\). The zero event is \(|\delta|\le tR\), where \(t=3s_1/4\). Its probability equals
\[
\int_0^\infty r e^{-r^2/2}\bigl(2\Phi(tr)-1\bigr)\,dr
=\frac{t}{\sqrt{1+t^2}}.
\tag{5}
\]
The final equality follows by differentiating in \(t\), obtaining \((1+t^2)^{-3/2}\), and using value zero at \(t=0\).

**3. Uniform control of all remaining harmonics.** Write \(H=U_N-U_1\), and \(R_k=\sqrt{a_k^2+b_k^2}\). The extrema of \(U_N\) differ from those of \(U_1\) by at most \(\|H\|_\infty\). Since \(\Phi\) has Lipschitz constant \((2\pi)^{-1/2}\), equation (4) implies
\[
|p_N-p_1|\le \frac{3}{2\sqrt{2\pi}}\mathbb E\|H\|_\infty
\le\frac34\sum_{k=2}^N s_k.
\]
Here \(\mathbb ER_k=\sqrt{\pi/2}\). Since \(\operatorname{sech}(\pi k\omega/2)\le2q^k\),
\[
\sum_{k=2}^N s_k\le2\sqrt2\pi\omega\sum_{k=2}^\infty kq^k
=2\sqrt2\pi\omega\frac{q^2(2-q)}{(1-q)^2}.
\]
This proves (1), with constants uniform over all degrees.

**4. Two critical points with overwhelming conditional probability.** Rotate the angular origin so that \(U_1=s_1R\cos\theta\), where \(R=R_1>0\) almost surely. Put
\[
T=\sum_{k=2}^N s_k(k+k^2)R_k,
\qquad c=\frac1{2\sqrt2}.
\]
Because \(\|H'\|_\infty,\|H''\|_\infty\le T\), on the event \(T<c s_1R\) the derivative of \(U_N\) has precisely two zeros. Indeed, on the arcs \(|\sin\theta|\ge1/\sqrt2\), the sign of \(U'_N\) is the sign of \(-\sin\theta\); on each complementary quarter-circle around \(0\) or \(\pi\), the sign of \(U_N''\) is the sign of \(-\cos\theta\), with derivative signs opposite at its endpoints. This produces one maximum and one minimum and no other critical points. Any horizontal level then has either zero or two transverse intersections, apart from zero-probability tangencies.

Conditionally on \(T\), the first-harmonic radius \(R\) is an independent Rayleigh variable. Thus
\[
\begin{aligned}
\mathbb P(Z_{N,\omega}\ge4)
&\le \mathbb P(T\ge cs_1R)\\
&=\mathbb E\left[1-\exp\left(-\frac{T^2}{2c^2s_1^2}\right)\right]\\
&\le\frac{\mathbb ET^2}{2c^2s_1^2}
\le 8\left(\frac{\sum_{k=2}^N s_k(k+k^2)}{s_1}\right)^2.
\end{aligned}
\]
The last inequality is Minkowski's inequality in \(L^2\) and \(\mathbb ER_k^2=2\). Using \(s_1=2\sqrt2\pi\omega q/(1+q^2)\) and \(s_k\le2\sqrt2\pi\omega kq^k\) gives (2). The infinite sum is absolutely convergent for \(0<q<1\) and starts at order \(q^2\).

**5. Sharp asymptotics and exactly two zeros.** From (5),
\[
t=\frac{3\sqrt2\pi}{2}\frac{\omega q}{1+q^2},\qquad
p_1=\frac{3\sqrt2\pi}{2}\omega q+O(\omega q^3+\omega^3q^3).
\]
The error \(\omega^3q^3\) is \(O(\omega q^2)\) as \(\omega\to\infty\). Equation (1) yields
\(p_N=(3\pi/\sqrt2)\omega q+O(\omega q^2)\), uniformly in \(N\). Equation (2) says \(\mathbb P(Z\ge4)=O(q^2)\). Since the simple-zero count is even, \(\mathbb P(Z=2)=p_N-\mathbb P(Z\ge4)\), proving (3). All asymptotic constants can be chosen independently of \(N\).

## Verification

The standalone `verification.py` rederives and numerically checks the Rayleigh integral, the exact geometric-series majorant, and the exponential scaling of the bounds. It runs with the Python standard library and is supplementary to the complete analytic proof above.

## Relationship to prior work

Ittayem and Lundberg (2026, arXiv:2610.33620v1) derive the exact Gaussian Melnikov trigonometric polynomial and give a sharp *expected-zero formula* alongside a high-frequency upper bound \(O(\omega\exp(-\pi\omega/2))\) for the probability of any zeros (Theorems 3.1 and 4.1, including the proof of the latter). The upper bound is not a sharp probability asymptotic: expected zeros can count four or more crossings. In fact, their one-harmonic specialization already implies the exact formula (5). The new conclusions here are the **degree-uniform probability prefactor**, the uniform control of higher-harmonic effects, and the **two-simple-zero dominance**. They are not claimed as a new Melnikov integral, a new first-harmonic formula, or a new exponential rate.

Earlier deterministic periodic-forcing calculations of the Duffing separatrix also yield exponentially suppressed Fourier harmonic contributions; they do not compare random Gaussian crossing probabilities uniformly over all Fourier degrees. General upper bounds for numbers of Melnikov zeros in polynomial Hamiltonian perturbations address a distinct counting problem. The possibility of a broader, unidentified Gaussian-process small-noise theorem implying this result remains a historical-priority risk.

## Limitations

This is a statement about the first-order Melnikov function on the right homoclinic loop, conditional on independent standard Gaussian coefficients and the stated damping distribution. For each fixed parameter realization, a simple Melnikov zero yields a transverse homoclinic intersection for sufficiently small perturbation, but the proof does not supply a uniform perturbation radius over \(N\), \(\omega\), or random coefficients. Probabilities are over sampled deterministic coefficients, not noisy trajectories. The bounds are not asserted sharp at moderate frequencies. Exactly-two refers to Melnikov phase zeros, not to a census of all intersections of invariant manifolds in the full perturbed flow. Novelty has been assessed against inspected sources, not independently certified.

## References

1. A. Ittayem and E. Lundberg, *Zeros of Melnikov functions for periodically perturbed Hamiltonian systems with random coefficients*, arXiv:2610.33620v1 (public October 24, 2026). https://arxiv.org/html/2610.33620v1
2. S. Benditkis and D. Novikov, *On the number of zeros of Melnikov functions*, Ann. Fac. Sci. Toulouse Math. **20** (2011), 465–491. https://archive.numdam.org/articles/10.5802/afst.1314/
3. *Effect of the shape of periodic forces and second periodic forces on horseshoe chaos in Duffing oscillator* (deterministic harmonic forcing, prior literature). https://www.researchgate.net/publication/1745240_Effect_of_the_shape_of_periodic_forces_and_second_periodic_forces_on_horseshoe_chaos_in_Duffing_oscillator
