# Sharp reactive-coupling window for three coexisting Stuart–Landau rotating waves

## Finding

In the three-oscillator complex-coupled Stuart–Landau equation below, a positive dissipative coupling does not always select synchrony alone. When the reactive coupling is sufficiently strong, synchrony and both opposite-chirality equilateral splay states are **simultaneously locally orbitally exponentially attracting**. The sharp onset is the dimensionless ratio \(|q|/p>2\sqrt2\); for each fixed supercritical ratio the permitted growth rates form a single explicit bounded interval. There are three distinct attracting periodic orbits in the full labelled state space whenever both rotation frequencies are nonzero. This is an **at-least-three** local attractor statement, not an exhaustive census of all attractors.

## Assumptions and scope

Let \(j\in\{0,1,2\}\), \(\beta,p,k>0\), and \(q,\omega\in\mathbb R\). Consider the smooth autonomous system on \(\mathbb C^3\)
\[
\dot z_j=(\beta+i\omega-k|z_j|^2)z_j+(p+iq)\sum_{\ell\ne j}(z_\ell-z_j).
\]
Here \(p\) is the *positive* real dissipative coupling, \(q\) the imaginary reactive coupling, and the oscillators have identical natural frequencies and growth rates and no nonlinear frequency shift. Set \(a=\beta-3p\). The synchronous branch is
\[
z_j(t)=\sqrt{\beta/k}\,e^{i(\omega t+\phi)},\qquad j=0,1,2,
\]
and, whenever \(a>0\), the two labelled chiral splay branches are
\[
z_j^{\sigma}(t)=\sqrt{a/k}\,e^{i[(\omega-3q)t+\phi+\sigma 2\pi j/3]},\qquad \sigma=\pm1.
\]
The two chiral cycles are distinct as subsets of labelled \(\mathbb C^3\), although permutations relate them. When \(\omega\ne0\) and \(\omega\ne3q\), all three are genuine periodic orbits. Without these nonzero-frequency assumptions, the same spectral conclusions concern normally attracting phase circles of relative equilibria (which may consist of stationary points).

For \(a>0\), each splay orbit is locally orbitally exponentially attracting **if and only if**
\[
\beta>6p,\qquad q^2>\frac{p(2\beta-9p)^2}{3(\beta-6p)}.
\]
It is unstable whenever these strict conditions fail, except that equality in the displayed second inequality when \(\beta>6p\) is *nonhyperbolic* (an additional conjugate pair of purely imaginary exponents); no nonlinear stability is asserted at equality. When \(3p<\beta\le6p\), every finite \(q\) produces a linearly unstable splay orbit.

Equivalently, with \(s=(q/p)^2\), a nonempty interval of splay attraction exists exactly when \(s>8\). For \(s>8\), it is
\[
\frac{3p}{8}\bigl(12+s-\sqrt{s(s-8)}\bigr)
<\beta<
\frac{3p}{8}\bigl(12+s+\sqrt{s(s-8)}\bigr).
\]
The two endpoints collapse at \(s=8\) to the unique ratio \(\beta/p=15/2\). Throughout this entire strict stability window the synchronous orbit remains stable, so there are at least three coexisting local attractors.

## Proof

**Synchronous spectrum.** Rotate with frequency \(\omega\), so the synchronous state becomes constant with modulus \(\sqrt{\beta/k}\). In real coordinates \((\operatorname{Re}z_j,\operatorname{Im}z_j)\), the common spatial mode contributes eigenvalues \(0,-2\beta\). On each of the two independent mean-zero spatial modes, the Jacobian is
\[
-2\beta\begin{pmatrix}1&0\\0&0\end{pmatrix}-3\begin{pmatrix}p&-q\\q&p\end{pmatrix},
\]
with characteristic polynomial \((\lambda+3p)(\lambda+2\beta+3p)+9q^2\). Its trace is \(-2\beta-6p<0\) and determinant \(3p(2\beta+3p)+9q^2>0\). Thus all five nonzero exponents are strictly negative in real part.

**Splay spectrum.** Rotate with frequency \(\omega-3q\); the equations become \(\dot w_j=(a-k|w_j|^2)w_j+(p+iq)\sum_{\ell=0}^2w_\ell\). For either chiral branch, put \(e_j=(\cos(2\pi j/3),\sigma\sin(2\pi j/3))\) and \(C=\begin{psmallmatrix}p&-q\\q&p\end{psmallmatrix}\). The full real linearization at \(w_j=\sqrt{a/k}\,e_j\) is
\[
\dot v_j=-2a\,e_je_j^{\mathsf T}v_j+C\sum_{\ell=0}^2v_\ell.
\]
A direct six-by-six determinant expansion, symbolically checked for each chirality, gives
\[
\det(\lambda I-J)=\lambda(\lambda+2a)\left(\left[\lambda^2+(2a-3p)\lambda-3ap\right]^2+9q^2(\lambda+a)^2\right).
\]
The nontrivial four-dimensional spectrum is therefore governed by the complex quadratic and its conjugate
\[
Q(\lambda)=\lambda^2+(2a-3p-3iq)\lambda-3a(p+iq).
\]
At \(q=0\), its constant term is negative, giving a positive real root. A root crosses the imaginary axis only if \(\lambda=i\Omega\) and
\[
(2a-3p)\Omega=3aq,\qquad -\Omega^2+3q\Omega-3ap=0.
\]
Since \(p,a>0\), these equations require \(a>3p\) and are then equivalent to
\[
q^2=\frac{p(2a-3p)^2}{3(a-3p)},\qquad
\Omega=\frac{3aq}{2a-3p}.
\]
No zero eigenvalue occurs in \(Q\), since \(Q(0)=-3a(p+iq)\ne0\). The threshold is unique for fixed \(a>3p\). At the threshold the other root of \(Q\) has strictly negative real part \(-(2a-3p)\), and implicit differentiation gives, at positive critical \(q_c\) with \(B=2a-3p\),
\[
\left.\frac{d}{dq}\operatorname{Re}\lambda\right|_{q=q_c}=-\frac{18aq_c(a-3p)}{B\bigl[B^2+(2\Omega_c-3q_c)^2\bigr]}<0.
\]
The crossing is transverse. The complex-conjugation symmetry gives the identical classification for negative \(q\). For \(a\le3p\), no finite imaginary-axis crossing exists and the positive eigenvalue at \(q=0\) persists. Therefore the splay spectrum is strictly stable away from the rotational zero exponent precisely when \(a>3p\) and \(|q|\) exceeds the stated threshold.

**Sharp optimization and three attractors.** Write \(t=\beta/p>6\). Then the threshold for \(s=(q/p)^2\) is
\[
F(t)=\frac{(2t-9)^2}{3(t-6)}
=8+\frac{4(t-15/2)^2}{3(t-6)}.
\]
Hence \(F(t)\ge8\), with equality exactly at \(t=15/2\). Solving \(s>F(t)\) as a strict quadratic inequality in \(t\) yields the two stated endpoints, real and distinct if and only if \(s>8\). Both endpoints exceed \(6p\), since \(s-4>\sqrt{s(s-8)}\) for \(s>8\). The phase rotation zero exponent is simple throughout the strict region, so standard Floquet/normal-hyperbolicity theory makes all three periodic orbits locally orbitally exponentially attracting. Distinct chiral orderings are not obtainable from one another by a common complex phase; each has its own open attracting neighborhood.

## Verification

The accompanying standalone `check.py` constructs the complete real Jacobians directly, symbolically verifies the two six-dimensional splay characteristic polynomials and synchronous polynomial, substitutes the imaginary-axis condition, proves the sharp algebraic identity for \(F(t)\), checks the exact growth-window endpoints, and compares eight representative full-Jacobian numerical spectra with the predicted stable/unstable classification. Execute from a working directory containing the script using `python check.py`. The symbolic determinant identities and the proof above, rather than numerical enumeration alone, establish the all-parameter theorem.

For a concrete strict example, take \(p=k=1\), \(q=3\), \(\beta=8\), and \(\omega=2\). Then \(s=9\), the exact stable-growth window is \(27/4<\beta<9\), both splay amplitudes equal \(\sqrt5\), the common splay frequency is \(-7\), and the synchronous amplitude is \(\sqrt8\) with frequency \(2\). All three periodic orbits attract nearby full six-dimensional trajectories modulo their own phase.

## Relationship to prior work

Zhao and Uchida (2026, arXiv:2610.08239v1), whose model is used here, derive a finite-size zero-mean polygonal manifold and numerically sample its transverse spectra, chiefly for eight heterogeneously growing oscillators. They do not state the exact identical-three-site attraction criterion or the sharp reactive ratio \(2\sqrt2\). Zou and Zhan (2009) analytically classify splay stability for a ring with **real** diffusive coupling, and find that globally coupled nontrivial splay states require negative real coupling for stability in that model; no imaginary coupling is included. Schneider (2013) studies a triangle with positive real diffusion plus **delayed feedback control**, not a complex instantaneous edge coupling; its control-based wave stabilization does not imply this no-delay criterion. Kemeth et al. (2021) treat two-cluster center-manifold bifurcations near synchrony, not the regular three-distinct-phase splay spectrum here.

Special-case polygon stability at purely imaginary coupling, \(p=0\), cannot determine the strict \(p>0\) growth window; heterogeneous three-site stability examples likewise do not imply an identical-growth sharp criterion. The new assertion is the all-parameter, sharp simultaneous stability region for this specific instantaneous complex-diffusive triangle; it does not claim the discovery of splay solutions themselves.

## Limitations

Only local orbital exponential stability and the sharp linear stability boundary for these three explicit branches are established. At the marginal imaginary-pair boundary, nonlinear secondary bifurcations and nonlinear stability are not classified. Other periodic, quasiperiodic, stationary, or chaotic attractors and their basins may coexist. The conclusion concerns identical growth, common frequency, three labelled sites and no nonlinear frequency shift; it is not asserted for more sites or heterogeneous growth. Historical priority remains provisional against other specialized equivariant-oscillator literature; a separate independent scientific audit has not been performed.

## References

- L. Zhao and N. Uchida, *Heterogeneity-induced chaos in globally coupled Stuart–Landau oscillators* (first available 2026-10-06), arXiv:2610.08239v1, https://arxiv.org/abs/2610.08239.
- W. Zou and M. Zhan, *Splay States in a Ring of Coupled Oscillators: From Local to Global Coupling*, SIAM Journal on Applied Dynamical Systems 8 (2009), 1324–1340, https://doi.org/10.1137/09075398X.
- I. Schneider, *Delayed feedback control of three diffusively coupled Stuart–Landau oscillators: a case study in equivariant Hopf bifurcation*, Philosophical Transactions A 371 (2013), 20120472, https://doi.org/10.1098/rsta.2012.0472.
- F. P. Kemeth, B. Fiedler, S. W. Haugland and K. Krischer, *2-Cluster Fixed-Point Analysis of Mean-Coupled Stuart–Landau Oscillators in the Center Manifold*, Journal of Physics: Complexity 2 (2021), 025005, arXiv:2010.06221, https://arxiv.org/abs/2010.06221.
