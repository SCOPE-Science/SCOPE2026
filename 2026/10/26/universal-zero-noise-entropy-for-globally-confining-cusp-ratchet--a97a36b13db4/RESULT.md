# Universal zero-noise entropy for globally confining cusp ratchets

## Finding
Consider a run-and-tumble diffusion on a circle of circumference \(L\) with a two-valued orientation \(\sigma_t\in\{-1,+1\}\) reversing at rate \(\gamma>0\), self-propulsion speed \(v>0\), constant leftward load \(f\in\mathbb R\), and a periodic ratchet potential \(U\). For a globally inward-pointing cusp ratchet as specified below, its stationary entropy production rate \(\Pi_D\) has the **universal** zero-diffusivity limit
\[
\boxed{\lim_{D\downarrow0}\Pi_D=2\gamma v^2\left[\frac{1}{(H_++f)^2-v^2}+\frac{1}{(H_--f)^2-v^2}\right].}
\]
Here \(H_+\) and \(H_-\) are the positive one-sided slopes at the attracting cusp. In particular, the limit does not depend on the potential shape away from this cusp or the circle's circumference, provided the inward-pointing condition holds. This extends beyond exactly solvable linear sawtooth potentials to nonlinear cusp ratchets with variable slopes.

More precisely, choose the signed coordinate \(z(x)=x\) immediately to the right of the cusp and \(z(x)=x-L\) immediately to its left. Conditional on either orientation \(\sigma=s\), \(z(X_D)/D\) converges in distribution, with all fixed polynomial moments, to the asymmetric two-sided exponential probability law
\[
q_s(y)=\frac{A_sB_s}{A_s+B_s}\begin{cases}
 e^{-A_s y},&y\ge0,\\
 e^{B_s y},&y<0,
\end{cases}\quad
A_s=H_++f-sv,\quad B_s=H_--f+sv.
\]
The stationary probability of each orientation equals \(1/2\) at every \(D>0\).

## Assumptions and scope
Identify the circle with \([0,L)\), where \(L>0\). Let \(0<a<L\) and let the real periodic potential \(U\) be continuous, piecewise \(C^2\) with bounded one-sided derivatives on \((0,a)\) and \((a,L)\), having its sole attracting corner at \(0\) and the other corner at \(a\). Assume there exists \(c>0\) such that
\[
U'(x)+f\ge v+c\quad(0<x<a),\qquad
-U'(x)-f\ge v+c\quad(a<x<L).
\]
Assume \(U'(0+)=H_+>0\) and \(U'(L-)=-H_-<0\) exist. The stochastic dynamics at diffusion coefficient \(D>0\) are
\[
\mathrm dX_t=[\sigma_t v-f-U'(X_t)]\,\mathrm dt+\sqrt{2D}\,\mathrm dW_t\pmod L,
\]
with independent symmetric rate-\(\gamma\) orientation flips. Values of the drift at the two corners do not affect the diffusion law. All conclusions concern its unique stationary distribution and the standard full-state Fokker--Planck entropy production convention in which the orientation is observed and has even time-reversal parity. No assertion is made for a vanishing inward margin or for a smooth potential maximum with orientation-dependent attractors.

Write the stationary densities as \(p_s(x)\), spatial currents as \(j_s=(sv-f-U')p_s-Dp_s'\), and constant total spatial current as \(J=j_++j_-\). The entropy production, equivalently the stationary entropy flux, is
\[
\Pi_D=\sum_{s=\pm1}\int_0^L\frac{j_s(x)^2}{D p_s(x)}\,\mathrm dx+\gamma\int_0^L(p_+-p_-)\log(p_+/p_-)\,\mathrm dx
=\frac vD\int_0^L(j_+-j_-)\,\mathrm dx-\frac{fLJ}{D}.
\]
The formula specifies the physical observable: a differently coarse-grained or differently time-reversed entropy production need not coincide with it.

## Proof
**1. Exponential localization uniformly in the orientation.** Write \(b_s(x)=sv-f-U'(x)\). It is strictly negative on \((0,a)\) and strictly positive on \((a,L)\), uniformly in \(s\). Define \(r(x)=x/a\) for \(0\le x\le a\), and \(r(x)=(L-x)/(L-a)\) for \(a\le x\le L\). Then \(r\ge0\), it vanishes only at the attracting cusp, and \(b_s r'\le-c_0<0\) away from the corners, uniformly in orientation. For small fixed \(\eta>0\), the test function \(V_D(x)=\cosh(\eta r(x)/D)\) has generator
\[
\mathcal L_D V_D=\frac{\eta}{D}b_s r'\sinh(\eta r/D)+\frac{\eta^2}{D}(r')^2\cosh(\eta r/D)
\]
on either smooth arc. Taking \(\eta\) small shows this is at most \(-c_1V_D/D\) for \(r\ge K D\), and at most \(C/D\) otherwise. At \(r=0\) the derivative of \(V_D\) vanishes, so the cusp adds no positive local-time term; at \(r=1\) the derivative jump has the favorable (negative) sign. The stationary generator identity therefore yields \(\sup_{0<D\le D_0}\mathbb E[V_D(X_D)]<\infty\). Consequently \(r(X_D)/D\) has uniformly bounded exponential moments of some positive order, and the probability of any fixed neighborhood away from the attracting cusp is exponentially small in \(1/D\).

**2. Boundary-layer law.** In the local signed coordinate \(y=z(x)/D\), multiply the stationary generator equation for a compactly supported test function of \(y\) and the orientation by \(D\). The orientation-switching term becomes \(O(D)\), while the spatial generator tends on each half-line to
\[
\mathcal A_s\phi(y)=\phi''(y)-A_s\phi'(y)\quad(y>0),\qquad
\mathcal A_s\phi(y)=\phi''(y)+B_s\phi'(y)\quad(y<0).
\]
By step 1 the rescaled conditional laws are tight, and their moments are uniformly integrable. Every subsequential limit is an invariant measure for the one-dimensional frozen-orientation diffusion with the piecewise constant inward drift above. Its unique normalized invariant density, found by setting the current to zero and matching density at zero, is \(q_s\) in the Finding. Since the independent orientation process has stationary probabilities \(1/2\), there is only one possible joint limit. In particular,
\[
\lim_{D\downarrow0}\frac1D\mathbb E[\sigma z(X_D)]
=\frac12\left[\left(\frac1{A_+}-\frac1{B_+}\right)-\left(\frac1{A_-}-\frac1{B_-}\right)\right].
\]

**3. Entropy--moment identity.** Choose a smooth periodic function \(\psi\) equal to the signed coordinate \(z\) near zero. Exponential localization makes every expected term supported where \(\psi'\ne1\) or \(\psi''\ne0\) exponentially small. Stationarity applied to \(\psi(X_D)\) gives \(LJ=\mathbb E[b_{\sigma}(X_D)]=O(e^{-c_2/D})\). Applied to \(\sigma\psi(X_D)\), it gives
\[
\mathbb E[\sigma b_\sigma(X_D)]=2\gamma\mathbb E[\sigma\psi(X_D)]+O(e^{-c_2/D}).
\]
Integrating the diffusion terms in \(j_s\) over the circle and using \(\mathbb E[\sigma]=0\) gives \(\int(j_+-j_-)=\mathbb E[\sigma b_\sigma]\). The stationary entropy-flux identity in the assumptions thus implies
\[
\Pi_D=\frac{2\gamma v}{D}\mathbb E[\sigma\psi(X_D)]+o(1).
\]
Step 2 now gives \(\lim\Pi_D=\gamma v[(1/A_+-1/B_+)-(1/A_--1/B_-)]\), and elementary reciprocal differences give exactly the displayed universal formula. Its strict positivity follows from the inward margins. This proves both parts of the theorem.

## Verification
The standalone file `VERIFY.py` checks the reciprocal identities exactly and independently solves finite-volume stationary master equations with exponentially fitted drift rates. For a linear sawtooth with right/left slopes \(2,3\), \(v=1\), \(\gamma=1\), \(f=0\), the predicted entropy limit is \(11/12\). The computed values at \(D=0.05,0.025,0.0125,0.00625\) are approximately \(0.85010,0.88141,0.89854,0.90747\). Replacing each constant slope by an oscillating one with the **same local cusp slopes** gives approximate values \(0.75764,0.80421,0.84538,0.87568\), approaching the same limit. A nonzero load and a distinct switching rate give an independent parameter check. These finite calculations corroborate but do not replace the infinite-parameter proof in the preceding section.

## Relationship to prior work
Roberts and Zhen (2023) obtain a complete finite-diffusivity stationary solution for the **linear** periodic ratchet, derive the associated entropy flux, and observe a finite zero-diffusivity entropy in the confined regime. Their Section V presents only a partial leading contribution to that limit, explicitly leaving the contribution from the other slope unresolved. Those exact finite-diffusivity formulas are acknowledged as prior coverage for the linear case; the present theorem instead establishes an explicit complete coefficient together with its invariance under arbitrary allowed nonlinear changes of the two arcs.

Paoluzzi, Puglisi and Angelani (2024) present the general run-and-tumble entropy framework and discuss spatially heterogeneous forces. They explicitly refer to the linear-ratchet analysis but do not supply the nonlinear-cusp zero-noise asymptotic or the universal local-slope reduction. Razin (2020) considers reflecting hard walls, not an inward-pointing periodic two-cusp potential. The equations and entropy conventions used here are not proposed as novel.

## Limitations
The sharp inward margin is essential to the proof; boundary regimes, smooth extrema, spatially varying flip rates, and orientation-dependent trapping outside the cusp are not covered. Only the stationary entropy convention specified above is addressed. The limit is not a finite-\(D\) exact formula, and no rate of convergence beyond convergence itself is proved. Although the named primary sources were compared in full, unindexed equivalent cusp asymptotics remain a possible prior-art risk. Independent review has not been performed.

## References
1. C. Roberts and Z. Zhen, *Run-and-tumble motion in a linear ratchet potential: Analytic solution, power extraction, and first-passage properties*, Phys. Rev. E 108, 014139 (2023), arXiv:2303.07880, https://arxiv.org/abs/2303.07880.
2. M. Paoluzzi, A. Puglisi and L. Angelani, *Entropy production of run-and-tumble particles*, Entropy 26, 443 (2024), arXiv:2404.16955, https://arxiv.org/abs/2404.16955.
3. N. Razin, *The entropy production of an active particle in a box*, Phys. Rev. E 102, 030103(R) (2020), arXiv:2008.08088, https://arxiv.org/abs/2008.08088.
