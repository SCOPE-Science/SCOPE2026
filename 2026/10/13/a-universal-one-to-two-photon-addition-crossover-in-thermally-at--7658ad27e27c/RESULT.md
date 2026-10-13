# A universal one-to-two photon-addition crossover in thermally attenuated Wigner negativity

## Finding

Let \(\rho_m\) be the state produced by adding exactly \(m\in\{1,2\}\) photons to the same single-mode thermal state of mean occupation \(\bar n\ge0\), followed by the same thermal attenuator of transmissivity \(\eta\in[0,1]\) and environment occupation \(\bar n_b\ge0\). The integrated Wigner-negative volume is
\[
\mathcal N_m=\int_{\mathbb C}[-W_m(\beta)]_+\,d^2\beta,
\qquad [z]_+=\max\{z,0\}.
\]
Set
\[
\eta_c=\frac{\bar n_b+1/2}{\bar n_b+1},\qquad
\theta=\frac{\eta(\bar n_b+1)-(\bar n_b+1/2)}{\eta(\bar n+1)}
\quad(\eta>\eta_c).
\]
For \(\eta\le\eta_c\), both negative volumes vanish. For \(\eta>\eta_c\), necessarily \(0<\theta\le1/2\), and
\[
\begin{aligned}
\mathcal N_1(\theta)&=\frac{\theta-1+e^{-\theta}}{1-\theta},\\
\mathcal N_2(\theta)&=\frac{2e^{-2\theta}}{(1-\theta)^2}
\left[\sqrt2\,\theta\cosh(\sqrt2\,\theta)-\sinh(\sqrt2\,\theta)\right].
\end{aligned}
\]
There is exactly one \(\theta_*\in(0,1/2)\) at which these two volumes agree; the ratio \(\mathcal N_2/\mathcal N_1\) is strictly increasing throughout \((0,1/2]\). Numerically,
\[
\theta_*=0.3013805517222017\ldots,\qquad
\mathcal N_1(\theta_*)=\mathcal N_2(\theta_*)=0.0589401573081\ldots.
\]
Thus **one addition retains more Wigner negativity near the noise threshold, but two additions retain more past a single universal crossover**. Define \(\bar n_*=1/(2\theta_*)-1=0.65903206807079\ldots\). If \(0\le\bar n<\bar n_*\), the unique transmissivity crossover is
\[
\eta_*=\frac{\bar n_b+1/2}{\bar n_b+1-\theta_*(\bar n+1)}\in(\eta_c,1),
\]
with \(\mathcal N_1>\mathcal N_2\) for \(\eta_c<\eta<\eta_*\) and the strict reverse for \(\eta_*<\eta\le1\). If \(\bar n=\bar n_*\), equality in the Wigner-negative regime occurs only at \(\eta=1\); if \(\bar n>\bar n_*\), the one-added state has strictly greater negative volume at every \(\eta>\eta_c\). In particular, for a vacuum seed and vacuum environment, \(\eta_*=0.7156972243366184\ldots\).

The same ordering and equality regimes hold for Wigner logarithmic negativity \(\log_2(1+2\mathcal N_m)\), a strictly increasing function of negative volume.

## Assumptions and scope

The input thermal state is
\[
\rho_{\rm th}(\bar n)=\frac1{1+\bar n}\sum_{k=0}^\infty
\left(\frac{\bar n}{1+\bar n}\right)^k|k\rangle\langle k|,
\qquad
\rho_m=\frac{(a^\dagger)^m\rho_{\rm th}(\bar n)a^m}{m!(1+\bar n)^m}.
\]
At \(\bar n=0\), the limiting thermal state is vacuum. The phase-insensitive thermal attenuator \(\mathcal L_{\eta,\bar n_b}\) acts on the symmetric Weyl characteristic function through
\[
\chi_{\rm out}(\xi)=\chi_{\rm in}(\sqrt\eta\,\xi)
\exp[-(1-\eta)(\bar n_b+1/2)|\xi|^2].
\]
It includes pure loss as \(\bar n_b=0\), ideal transmission as \(\eta=1\), and complete attenuation as \(\eta=0\). We normalize \(W\) by \(\int_{\mathbb C}W(\beta)d^2\beta=1\); hence the negative volume is half of the frequently used \(\int|W|-1\). The theorem concerns exactly one versus two photon additions before the channel, with identical seed and channel parameters, not energy-matched states.

## Proof

**1. Characteristic function of a photon-added thermal state.** Put \(q=\bar n/(1+\bar n)\). Its exact photon-number probabilities are
\[
\langle m+k|\rho_m|m+k\rangle=\binom{m+k}{m}(1-q)^{m+1}q^k,
\qquad k\ge0.
\]
The diagonal number-state Weyl characteristic is \(e^{-t/2}L_j(t)\), where \(t=|\xi|^2\). Differentiating the generating identity
\[
\sum_{j\ge0}L_j(t)z^j=(1-z)^{-1}\exp[-zt/(1-z)]
\]
exactly \(m\) times gives
\[
\chi_m(\xi)=e^{-(\bar n+1/2)t}L_m((\bar n+1)t).
\]
After thermal attenuation this becomes
\[
\chi_{m,\mathrm{out}}(\xi)=e^{-a t}L_m(vt),\qquad
a=\frac12+\eta\bar n+(1-\eta)\bar n_b,
\quad v=\eta(\bar n+1).
\]
Here \(a>0\) and \(v\ge0\). With \(\delta=v-a\), direct subtraction yields
\[
\delta=\eta(\bar n_b+1)-(\bar n_b+1/2).
\]

**2. A normalized Wigner profile.** Applying the complex Gaussian Fourier transform termwise to the Laguerre polynomial, or summing in \(m\) before inversion, gives when \(a\ne v\)
\[
W_m(\beta)=\frac{e^{-|\beta|^2/a}}{\pi a}
\left(\frac{a-v}{a}\right)^m
L_m\!\left(-\frac{v|\beta|^2}{a(a-v)}\right).
\]
The expression has a continuous limit at \(a=v\). If \(a\ge v\), the Laguerre argument is nonpositive and \(L_m(-x)=\sum_{j=0}^m\binom mj x^j/j!\ge0\) for \(x\ge0\); its limiting polynomial at equality is nonnegative too. Since \(a\ge v\) exactly when \(\eta\le\eta_c\), both negative volumes then vanish.

When \(\delta>0\), set \(\theta=\delta/v\). Now \(0<\theta\le1/[2(\bar n+1)]\le1/2\), because \(\theta(\eta)\) is increasing on \(\eta>\eta_c\) and has terminal value \(1/[2(\bar n+1)]\) at \(\eta=1\), as explicitly verified in step 5. Writing \(y=v|\beta|^2/(a\delta)\) and using radial area \(d^2\beta=\pi\,d(|\beta|^2)\), we obtain for every integer \(m\ge1\)
\[
\mathcal N_m(\theta)=\frac{\theta^{m+1}}{(1-\theta)^m}
F_m(\theta),\qquad
F_m(\theta)=\int_0^\infty e^{-\theta y}[-(-1)^mL_m(y)]_+\,dy.
\]
This is an exact one-parameter reduction: all dependence on seed occupation, bath occupation and transmissivity enters through \(\theta\).

**3. Evaluate the two negative domains.** With \(L_1(y)=1-y\),
\[
F_1(\theta)=\int_0^1e^{-\theta y}(1-y)\,dy
=\frac{\theta-1+e^{-\theta}}{\theta^2}.
\]
For \(L_2(y)=1-2y+y^2/2\), the negative domain is precisely \((2-\sqrt2,2+\sqrt2)\); integrating yields
\[
F_2(\theta)=\int_{2-\sqrt2}^{2+\sqrt2}e^{-\theta y}[-L_2(y)]\,dy
=\frac{2e^{-2\theta}}{\theta^3}
\left[\sqrt2\,\theta\cosh(\sqrt2\,\theta)-\sinh(\sqrt2\,\theta)\right].
\]
These identities give the two asserted closed negative-volume formulas. Both volumes are strictly positive when \(\theta>0\).

**4. Prove global uniqueness of the crossover.** Define \(R(\theta)=\mathcal N_2(\theta)/\mathcal N_1(\theta)=\theta F_2(\theta)/[(1-\theta)F_1(\theta)]\). For \(i=1,2\), define the exponentially tilted mean
\[
\mu_i(\theta)=\frac{\int y e^{-\theta y}[-(-1)^iL_i(y)]_+dy}{F_i(\theta)}.
\]
The integrands are strictly positive on their respective support intervals, so \(0<\mu_1<1\) and \(2-\sqrt2<\mu_2<2+\sqrt2\). Differentiating the positive Laplace integrals gives \(F_i'/F_i=-\mu_i\), whence
\[
\frac{d}{d\theta}\log R(\theta)
=\frac1{\theta(1-\theta)}+\mu_1(\theta)-\mu_2(\theta)
>4-(2+\sqrt2)=2-\sqrt2>0
\]
for all \(0<\theta\le1/2\). Moreover, \(F_1(0)=1/2\) and \(F_2(0)=4\sqrt2/3\), so \(R(\theta)\sim(8\sqrt2/3)\theta\to0\) at the left endpoint. At \(\theta=1/2\),
\[
\mathcal N_1(1/2)=2e^{-1/2}-1<1/4,
\qquad
\mathcal N_2(1/2)=8e^{-1}
\left[z\cosh z-\sinh z\right]_{z=1/\sqrt2}
>\frac4{3\sqrt2\,e}>\frac14.
\]
The first inequality follows from \(e^{1/2}>1+1/2+1/8\), and the second from \(z\cosh z-\sinh z>z^3/3\), \(e<3\) and \(\sqrt2<3/2\). Thus \(R(1/2)>1\), and continuity plus strict increase gives one and only one \(\theta_*\in(0,1/2)\).

**5. Translate back to physical parameters.** On the negative-Wigner regime,
\[
\theta(\eta)=\frac{\bar n_b+1}{\bar n+1}-
\frac{\bar n_b+1/2}{\eta(\bar n+1)}
\]
is strictly increasing with \(\eta\), starting at zero as \(\eta\downarrow\eta_c\) and attaining \(1/[2(\bar n+1)]\) at \(\eta=1\). The strict value of \(\bar n_*\) is therefore the exact boundary between an interior reachable crossover, an endpoint crossover, and no crossover. Solving \(\theta(\eta)=\theta_*\) gives the displayed \(\eta_*\). Because \(x\mapsto\log_2(1+2x)\) is strictly increasing on nonnegative \(x\), the same ordering holds for Wigner logarithmic negativity.

## Verification

Run `python verify.py` with the dependencies in `requirements.txt`. The independent checker compares the characteristic function with the normalized Fock-basis sum (36 parameter tests), radial Fourier/Hankel integral against the Wigner closed form including nonzero bath occupation (40 tests), and direct quadrature of both negative domains against the elementary formulas (12 tests). It also samples the increasing ratio, solves the crossover numerically, and tests physical reparameterizations. One execution produced:

`VERIFY_OK input_fock_characteristic=36 independent_hankel=40 integrated_volume=12 ratio_samples=200 thermal_phase_pairs=12 crossing=0.301380551722202`

The analytic proof, not the finite tests or printed digits, establishes the continuum of parameters, unique crossover and endpoint classifications. Numerical digits are approximate and not claimed as certified interval enclosures.

## Relationship to prior work

Kenfack and Życzkowski (2004) define the integrated Wigner-negative volume; their convention is twice \(\mathcal N\) used here. Usha Devi, Prabhu and Uma (2006) give early Wigner calculations for photon-added thermal light. Li (2008) **already evaluates the one-added thermal state under a thermal reservoir, including its negative-volume decay and reservoir-dependent Wigner-positivity threshold**; neither that one-added result nor this threshold is claimed to be new. Marian, Ghiu and Marian (2012/2013) derive the exact damped Wigner-Laguerre profile for arbitrary photon-addition number, notably their Eq. (4.4); the profile and universal positivity threshold are antecedents, not new contributions. Veitch and collaborators (2013) likewise analyze the single-added loss threshold. Xu and Yuan (2019) investigate Wigner logarithmic negativity in a thermal reservoir, but only a first-page publisher preview was available for comparison.

The contribution assessed here is the **evaluated two-addition versus one-addition negative-volume ordering**, a proof of exactly one universal crossover, and its sharp thermal-seed and bath-dependent accessibility phase diagram. It requires integrating distinct negative regions and proving global monotonicity of their ratio; the inspected antecedents give Wigner profiles, single-added volumes or thresholds, not that ordering theorem. This does not rule out equivalent results in uninspected full text.

## Limitations

The comparison uses ideal normalized photon addition, single-mode unsqueezed thermal input, a phase-insensitive Gaussian attenuator, equal seed and channel settings for the two states, and integrated Wigner negativity. It is not an energy-matched comparison, does not establish optimal heralding yield or finite-sample detectability, and does not compare all higher photon-addition numbers or other nonclassicality measures. The first-page-only availability of Xu and Yuan (2019) and the possibility of another source evaluating the same crossing remain publication-priority risks. All stated numerical constants are unvalidated approximations beyond the analytic uniqueness proof; no independent audit has been performed.

## References

1. A. Kenfack and K. Życzkowski, *Negativity of the Wigner function as an indicator of nonclassicality*, arXiv:quant-ph/0406015 (first public 2004-06-02).
2. A. R. Usha Devi, R. Prabhu and M. S. Uma, *Non-classicality of photon added coherent and thermal radiations*, arXiv:quant-ph/0602071 (first public 2006-02-07).
3. S.-B. Li, *Nonclassicality of single quantum excitation of a thermal field in thermal environments*, arXiv:0805.4252 (first public 2008-05-28), especially the evaluated single-addition negative volume and positivity threshold.
4. P. Marian, I. Ghiu and T. A. Marian, *Gaussification through decoherence*, arXiv:1211.1701 (first public 2012-11-07), especially Sec. IV A, Eq. (4.4).
5. V. Veitch, N. Wiebe, C. Ferrie and J. Emerson, *Efficient simulation scheme for a class of quantum optics experiments with non-negative Wigner representation*, New J. Phys. 15 (2013), 013037, Sec. 4.
6. X.-X. Xu and H.-C. Yuan, *Dynamical evolution of photon-added thermal state in thermal reservoir*, Chinese Physics B 28 (2019), 110301, DOI:10.1088/1674-1056/ab457d (first-page preview only).
