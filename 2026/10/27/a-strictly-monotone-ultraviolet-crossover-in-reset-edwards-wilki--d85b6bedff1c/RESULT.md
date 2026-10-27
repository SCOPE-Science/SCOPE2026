# A strictly monotone ultraviolet crossover in reset Edwards–Wilkinson height kurtosis

## Finding
Consider a one-dimensional, infinite-line Edwards–Wilkinson height field starting flat after each global Poisson reset and driven by Gaussian white-in-time noise supported at Fourier frequencies \(|k|\leq\Lambda\). For every diffusivity \(\nu>0\), noise strength \(D>0\), reset rate \(r>0\), and finite spectral cutoff \(\Lambda>0\), the stationary one-point excess kurtosis depends **only** on \(x=r/(2\nu\Lambda^2)\). It is the explicit function
\[
\mathcal K(x)=\frac{3x}{\left[\int_0^1\frac{du}{x+u^2}\right]^2}
\int_0^1\int_0^1\frac{du\,dv}{(x+u^2)(x+v^2)(x+u^2+v^2)}.
\]
The function \(\mathcal K:(0,\infty)\to(12/\pi-3,3)\) is **strictly increasing and onto**, with sharp endpoint expansions
\[
\mathcal K(x)=\frac{12}{\pi}-3+\frac{12}{\pi}\left(\frac4\pi-1\right)\sqrt{x}+O(x),\quad x\downarrow0,
\]
\[
\mathcal K(x)=3-\frac2x+O(x^{-2}),\quad x\to\infty.
\]
Consequently one stationary fourth-moment measurement identifies the ultraviolet cutoff \(\Lambda\) uniquely, assuming \(r\) and \(\nu\) known and the ideal hard-bandlimited model. Its noise amplitude \(D\) cancels out. The continuum infinite-band regime has excess \(12/\pi-3\), whereas rapid resets relative to the finite-band relaxation limit yield the Laplace excess \(3\).

## Assumptions and scope
The field obeys \(\partial_t H=\nu\partial_z^2H+\eta_\Lambda\) on \(\mathbb R\), with \(H(\cdot,0)=0\). The centered Gaussian noise has covariance
\[
\mathbb E[\eta_\Lambda(z,t)\eta_\Lambda(z',t')]=2D\,\delta(t-t')\int_{-\Lambda}^{\Lambda}e^{ik(z-z')}\frac{dk}{2\pi}.
\]
Independent exponentially distributed reset waiting times of parameter \(r\) restore the *entire* field to its flat initial condition. The quantity is the one-point stationary standardized excess kurtosis \(\mathcal K=\mathbb E[H^4]/(\mathbb E[H^2])^2-3\), with expectations over both noise and resetting. The one-point mean is zero. The spatial domain is the whole line: this is not a finite-periodic-ring theorem, nor a statement about KPZ nonlinear dynamics or a soft spectral cutoff.

## Proof
**Gaussian age mixture.** Condition on the time \(t\) elapsed since the last reset. Fourier solution of the heat equation gives the one-point conditional variance
\[
V_\Lambda(t)=\frac{D}{\pi\nu}\int_0^\Lambda\frac{1-e^{-2\nu k^2t}}{k^2}\,dk
=\frac{D}{\pi\nu\Lambda}\,h(2\nu\Lambda^2t),
\]
with \(h(z)=\int_0^1(1-e^{-zu^2})u^{-2}du=\sqrt{\pi z}\operatorname{erf}(\sqrt z)+e^{-z}-1\). At a stationary observation time the reset age is exponential of rate \(r\); equivalently \(S=rt\) is unit exponential. Hence \(H\mid S\) is centered Gaussian with variance \(c h(S/x)\), where \(c=D/(\pi\nu\Lambda)\). Gaussian fourth moments yield
\[\mathcal K(x)=3\left(\frac{\mathbb E[h(S/x)^2]}{\mathbb E[h(S/x)]^2}-1\right).\]
Using Tonelli and \(\mathbb E[e^{-aS}]=(1+a)^{-1}\),
\[
\mathbb E[h(S/x)]=\int_0^1\frac{du}{x+u^2}=\frac{\arctan(x^{-1/2})}{\sqrt x}.
\]
The covariance of the integrands \((1-e^{-Su^2/x})/u^2\) and \((1-e^{-Sv^2/x})/v^2\) equals
\[
\frac{x}{(x+u^2)(x+v^2)(x+u^2+v^2)}.
\]
Integration proves the formula in the finding. The integrals are finite and strictly positive for \(x>0\).

**Strict monotonicity.** We give a structural proof rather than inferring an infinite-dimensional inequality from numerics. Write \(w(z)=\sqrt{\pi z}\operatorname{erf}\sqrt z=2zh'(z)\) and \(q(z)=1-e^{-z}\). Since \(h=w-q>0\), its logarithmic elasticity satisfies
\[
R(z)=\frac{zh'(z)}{h(z)}=\frac1{2(1-q(z)/w(z))}.
\]
Now \(q/w=A/(2B)\), where \(A(z)=\int_0^1e^{-zv}dv\) and \(B(z)=\int_0^1e^{-zv}(2\sqrt v)^{-1}dv\). For each \(z>0\), the exponentially tilted density proportional to \(e^{-zv}\) has strictly larger expectation of \(v\) than the tilted density proportional to \(e^{-zv}/\sqrt v\), because their density ratio is a strictly increasing function of \(v\). Thus \((\log(A/B))'<0\): \(q/w\) and therefore \(R\) are strictly decreasing.

For \(x_2>x_1>0\), set \(f(s)=h(s/x_1)\) and \(g(s)=h(s/x_2)\). The derivative of \(\log(g/f)\) with respect to \(\log s\) is \(R(s/x_2)-R(s/x_1)>0\), so \(a(s)=g(s)/f(s)\) increases strictly; \(f\) also increases strictly. Under the unit-exponential measure on \(s\), let \(P_1\) and \(P_2\) have densities proportional to \(f\) and \(f^2\), respectively. Because \(f\) increases, \(P_2\) stochastically dominates \(P_1\). Therefore
\[
\frac{\mathbb E[g^2]}{\mathbb E[f^2]}=\mathbb E_{P_2}[a^2]
>\mathbb E_{P_1}[a^2]\geq\bigl(\mathbb E_{P_1}[a]\bigr)^2
=\left(\frac{\mathbb E[g]}{\mathbb E[f]}\right)^2.
\]
All expectations are finite because \(h(z)\leq z\). This proves \(\mathcal K(x_2)>\mathcal K(x_1)\) for *every* pair \(x_2>x_1\).

**End points.** As \(x\downarrow0\), \(h(s/x)=\sqrt{\pi s/x}-1+o(1)\) except on an exponentially small-age region. Direct exponential integration (with the latter region contributing \(O(x)\) to the second moment) gives
\[
\mathbb E[h(S/x)]=\frac\pi{2\sqrt x}-1+O(x),\qquad
\mathbb E[h(S/x)^2]=\frac\pi x-\frac\pi{\sqrt x}+1+O(x),
\]
which yields the first claimed expansion. As \(x\to\infty\), expand \(h(z)=z-z^2/6+z^3/30+O(z^4)\) under the exponentially integrable age law to obtain \(\mathcal K(x)=3-2/x+O(x^{-2})\). Both limits together with strict continuity and monotonicity establish the exact open range and unique invertibility.

## Verification
The accompanying standard-library Python file `checker.py` evaluates the exact two-dimensional integral by deterministic composite Simpson quadrature at six cutoff ratios, checks the limiting constants and high-rate expansion, and supplies an exact-rational counterexample showing that generic two-mode Ornstein–Uhlenbeck spectra need **not** have monotone excess kurtosis. Its numerical computations illustrate but do not replace the preceding proof. Run `python3 checker.py` from the extracted package directory.

## Relationship to prior work
Gupta, Majumdar and Schehr (2013/2014) established the unbounded-band resetting stationary law for Edwards–Wilkinson and KPZ interfaces and the Edwards–Wilkinson width scaling. Our lower endpoint is a consequence of their continuum scaling law; it is **not** asserted new. Gupta and Nagar (2016) examined power-law rather than exponential reset intervals. The present result instead resolves the hard ultraviolet-cutoff dependence of one-point excess kurtosis, including a global monotonicity theorem and an inverse spectral-cutoff identification. General fourth-cumulant formulas for finite ensembles of simultaneously reset Ornstein–Uhlenbeck modes provide a compatible starting point, but do not by themselves imply monotonicity under an Edwards–Wilkinson spectral band: arbitrary two-mode spectra can violate it, as the exact-rational control in `checker.py` demonstrates.

## Limitations
The theorem assumes an ideal sharp Fourier band, global whole-field resetting, Gaussian additive forcing, and infinite spatial extent. For a smooth cutoff or non-exponential resets, strict monotonicity is not established. A measured kurtosis outside the stated interval falsifies at least one assumption of this ideal model, not all Edwards–Wilkinson descriptions. Inverse cutoff estimation can be poorly conditioned near the endpoints. Full comprehensive publication-priority certainty, particularly for specialized microscopic interface regularizations, is not claimed.

## References
1. S. Gupta, S. N. Majumdar and G. Schehr, *Fluctuating interfaces subject to stochastic resetting*, arXiv:1312.5954 (initial posting 2013-12-20); *Physical Review Letters* **112**, 220601 (2014), DOI: 10.1103/PhysRevLett.112.220601.
2. S. Gupta and A. Nagar, *Resetting of fluctuating interfaces at power-law times*, arXiv:1604.06627 (initial posting 2016-04-22).
3. S. F. Edwards and D. R. Wilkinson, *The surface statistics of a granular aggregate*, *Proceedings of the Royal Society A* **381**, 17–31 (1982).
