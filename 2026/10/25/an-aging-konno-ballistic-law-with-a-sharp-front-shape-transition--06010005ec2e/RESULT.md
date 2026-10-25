# An aging--Konno ballistic law with a sharp front-shape transition under power-law quantum-walk restart

## Finding
Fix a self-loop weight \(\ell>0\) and a restart exponent \(1<s<2\). Write \(\alpha=s-1\in(0,1)\),
\[
a=\sqrt{\frac{\ell}{\ell+2}},\qquad b=\sqrt{\frac{2}{\ell+2}}=\sqrt{1-a^2}.
\]
At each integer observation time \(t\), let \(X_t\) be the measured position of the weighted three-state Grover walk after iid whole-state resets to the origin and the flat-band-dark coin described below. Then
\[
\frac{X_t}{t}\ \Rightarrow\ Y=UV,
\]
where the independent factors satisfy
\[
U\sim\operatorname{Beta}(1-\alpha,\alpha),\qquad
\Pr(V\in dv)=\rho_\ell(v)\,dv,\qquad
\rho_\ell(v)=\frac{b}{\pi(1-v^2)\sqrt{a^2-v^2}}\mathbf1_{\{|v|<a\}}.
\]
There are no atoms in the limiting law. The even density on \((-a,a)\setminus\{0\}\) is
\[
f_{\alpha,\ell}(x)=\frac{\sin(\pi\alpha)}{\pi}\int_{|x|/a}^1
 \frac{\rho_\ell(x/u)}{u^{1+\alpha}(1-u)^{1-\alpha}}\,du.
\]
Its central and positive-front asymptotics, for \(x\downarrow0\) and \(\delta\downarrow0\), are
\[
f_{\alpha,\ell}(x)\sim C_0(\alpha,\ell)x^{-\alpha},\qquad
f_{\alpha,\ell}(a-\delta)\sim C_{\rm e}(\alpha,\ell)\delta^{\alpha-1/2},
\]
with strictly positive finite constants
\[
\begin{aligned}
C_0(\alpha,\ell)&=\frac{\sin(\pi\alpha)b a^{\alpha-1}}{2\pi^2}
 B\!\left(\frac\alpha2,\frac12\right)
 {}_2F_1\!\left(1,\frac\alpha2;\frac{\alpha+1}{2};a^2\right),\\
C_{\rm e}(\alpha,\ell)&=\frac{\sin(\pi\alpha)}{\pi^2 b\sqrt{2a}\,a^\alpha}
 B\!\left(\alpha,\frac12\right).
\end{aligned}
\]
Consequently, the limiting density diverges at either ballistic front for \(1<s<3/2\), has a finite positive one-sided front limit for \(s=3/2\), and vanishes at the front for \(3/2<s<2\). In all cases it has the integrable cusp \(|x|^{1-s}\) at the restart origin. Moreover,
\[
\mathbb E(Y^2)=\frac{(2-s)(3-s)}2\left(1-\sqrt{\frac{2}{\ell+2}}\right).
\]
This is a weak scaling limit and a statement about its density; it does not assert pointwise convergence of finite-lattice mass functions after rescaling.

## Assumptions and scope
The coin space has the ordered basis \(|L\rangle,|S\rangle,|R\rangle\). Define
\[
|s_\ell\rangle=\frac{(1,\sqrt\ell,1)^T}{\sqrt{\ell+2}},\qquad
C_\ell=2|s_\ell\rangle\langle s_\ell|-I_3.
\]
One restart-free step first applies \(C_\ell\) and then shifts the \(L\), \(S\), \(R\) components by \(-1,0,+1\), respectively. Initially, and upon every restart, the walker is localized at zero with normalized coin
\[
\chi_\perp=\frac{(\sqrt\ell,-2,\sqrt\ell)^T}{\sqrt{2(\ell+2)}}.
\]
Restart waiting times \(T_1,T_2,\dots\) are independent, positive integer valued, with \(\Pr(T_i=m)=m^{-(1+\alpha)}/\zeta(1+\alpha)\) for every integer \(m\ge1\). At each renewal epoch the complete walker-coin state resets, independently of earlier walks. \(X_t\) means the position sampled at integer time \(t\) from the corresponding mixed state, starting with a renewal at \(t=0\). Here \(\ell>0\) and \(0<\alpha<1\) are held fixed as \(t\to\infty\); the endpoint cases \(s=1,2\) and \(\ell=0\) are excluded.

## Proof
**1. Renewal-age limit.** Let \(p_m=m^{-(1+\alpha)}/\zeta(1+\alpha)\), \(\Phi_j=\Pr(T>j)\), and let \(u_n\) be the probability of a renewal at integer time \(n\), with \(u_0=1\). For the elapsed age \(A_t\) since the latest renewal,
\[
\Pr(A_t=j)=u_{t-j}\Phi_j,\quad 0\le j\le t.
\]
The sequence is aperiodic and \(\Phi_j\sim j^{-\alpha}/[\alpha\zeta(1+\alpha)]\). Its renewal generating function is \(\sum_{n\ge0}u_nz^n=[1-\operatorname{Li}_{1+\alpha}(z)/\zeta(1+\alpha)]^{-1}\). The singular expansion, followed by coefficient transfer for this positive regularly varying lattice distribution, gives
\[
u_n\sim\frac{\alpha\zeta(1+\alpha)\sin(\pi\alpha)}{\pi}\,n^{\alpha-1}.
\]
For \(j/t\to v\in(0,1)\), multiplication yields
\[
t\Pr(A_t=j)\longrightarrow
\frac{\sin(\pi\alpha)}\pi v^{-\alpha}(1-v)^{\alpha-1}.
\]
A standard endpoint-tightness estimate from the displayed renewal and survival asymptotics (bounding the sums over \(j\le\varepsilon t\) and \(t-j\le\varepsilon t\) by constants times \(\varepsilon^{1-\alpha}\) and \(\varepsilon^\alpha\)) upgrades the local limit to
\[
A_t/t\Rightarrow U\sim\operatorname{Beta}(1-\alpha,\alpha).
\]
The beta density is normalized by \(B(1-\alpha,\alpha)=\pi/\sin(\pi\alpha)\). In particular \(A_t\to\infty\) in probability.

**2. Unreset quantum ballistic limit.** Let \(X_m^{(0)}\) denote the position after \(m\) uninterrupted steps from \(\chi_\perp\). The Fourier-space walk has one flat band and two dispersive bands with quasienergies \(\pm\omega(k)\) and
\[
\cos\omega(k)=-\frac{2+\ell\cos k}{2+\ell},\qquad
|\omega'(k)|=\sqrt{\frac{\ell(1+\cos k)}{\ell+4+\ell\cos k}}.
\]
The flat-band spectral projection annihilates \(\chi_\perp\) at every \(k\). By the Fourier spectral weak-limit theorem, \(X_m^{(0)}/m\Rightarrow V\) where the dispersive-band group velocities are weighted by their band projections. Reflection symmetry of the coin and initial state makes the law even; the sum of the two dispersive projection weights equals one at each momentum. Pushing normalized Lebesgue momentum through \(|\omega'(k)|\) gives
\[
\rho_\ell(v)=\frac{b}{\pi(1-v^2)\sqrt{a^2-v^2}},\quad |v|<a.
\]
Indeed, for uniform momentum \(k\), the variable \(z=\cos^2(k/2)\) has density \(1/[\pi\sqrt{z(1-z)}]\), and \(v^2=\ell z/(2+\ell z)\). Substitution gives the displayed symmetric density, whose integral is one. Thus this purely dispersive preparation has no atomic zero-velocity part.

**3. Mixing the ages.** Conditioned on \(A_t=j\), the position distribution is that of \(X_j^{(0)}\). For bounded continuous \(g\), the characteristic functions or a bounded convergence argument apply to \((A_t/t)(X_{A_t}^{(0)}/A_t)\). Since \(A_t\to\infty\) in probability and \(A_t/t\Rightarrow U\), while the conditional uninterrupted law converges to the fixed law of \(V\), the joint limit has independent factors \(U\) and \(V\). The convention for \(A_t=0\) has no effect in the limit. Thus \(X_t/t\Rightarrow UV\).

**4. Density and two singularities.** The product-density change of variables gives
\[
f(x)=\int_{|x|/a}^1\frac1u\,\frac{\sin(\pi\alpha)}\pi u^{-\alpha}(1-u)^{\alpha-1}\rho_\ell(x/u)\,du.
\]
For \(x>0\), substitute \(v=x/u\). Then
\[
x^\alpha f(x)=\frac{\sin(\pi\alpha)}\pi
\int_x^a v^{\alpha-1}\left(1-\frac{x}{v}\right)^{\alpha-1}\rho_\ell(v)\,dv.
\]
To justify the limit, split the integral at \(v=2x\). On \(x\le v\le2x\) the substitution \(v=x(1+t)\) bounds its contribution by \(O(x^\alpha)\). On \(2x\le v\le a\), the factor \((1-x/v)^{\alpha-1}\) is bounded by \(2^{1-\alpha}\), and the remaining integrand \(v^{\alpha-1}\rho_\ell(v)\) is integrable at both endpoints. Dominated convergence therefore gives \(C_0=(\sin(\pi\alpha)/\pi)\int_0^a v^{\alpha-1}\rho_\ell(v)\,dv\). Substituting \(v=a\sqrt z\) evaluates this Euler integral to the stated beta-hypergeometric expression.

For the front, put \(x=a-\delta\) and \(u=1-e\), with \(0\le e\le\delta/a\). Uniformly on compact relative subintervals and with an integrable domination after scaling, the only singular factors are \(e^{\alpha-1}\) and \((\delta-ae)^{-1/2}\), and
\[
\rho_\ell\left(\frac{a-\delta}{1-e}\right)
\sim\frac1{\pi b\sqrt{2a(\delta-ae)}}.
\]
The beta integral
\[
\int_0^{\delta/a}e^{\alpha-1}(\delta-ae)^{-1/2}\,de
=a^{-\alpha}\delta^{\alpha-1/2}B(\alpha,1/2)
\]
proves the constant \(C_{\rm e}\) and the sign-changing front exponent \(\alpha-1/2\). All constants are positive for the claimed parameter ranges.

**5. Moment consistency.** Since \(|X_t/t|\le1\), weak convergence also gives convergence of all positive moments. Independence and beta integration show \(\mathbb E(U^2)=(1-\alpha)(2-\alpha)/2\). The Konno integral yields \(\mathbb E(V^2)=1-b\). Multiplying gives the reported second moment, agreeing with the known leading mean-squared displacement for this preparation.

## Verification
The standalone `verification.py` implements the original three-coin unitary step on the integer lattice, the discrete renewal convolution, direct numerical finite-size position probabilities, and independent quadrature of the limiting density. Running `python verification.py` with NumPy and SciPy gives 18 PASS diagnostics for the normalization, finite-time second moment, four cumulative distribution values, and the central/front amplitudes for three exponents. The finite-size test uses 650 steps at \(\ell=2\) and \(\alpha=0.3\): the computed scaled second moment is approximately \(0.174897\) versus the exact limit \(0.174271\). These are checks, not substitutes for the proof of weak convergence or the endpoint asymptotics.

## Relationship to prior work
Das, *Restart and first detection in a lackadaisical quantum walk with flat-band localization* (2026), establishes the walk, the renewal representation, the flat-band-dark preparation, the restart-free velocity formulation, pointwise fixed-site decay under infinite-mean power-law restart, and the leading scaled mean-squared displacement. These results are antecedents, not claimed as new. Štefaňák, Bezděková and Jex (2014) establish three-state walk Konno-type weak limits and coin-eigenstate structure. The generalized arcsine (Dynkin–Lamperti) age law is classical. Wang, Höll and Barkai (2020) study the ballistic regime of a classical Lévy walk, which has a different displacement rule: flights contribute cumulatively rather than returning to the origin at every renewal. The contribution here is the explicit full spatial scaling law for the specified power-law restarted quantum walk and its exact cusp/front coefficient pair and front transition at \(s=3/2\); neither the ingredients individually nor the known second-moment formula assert these conclusions.

## Limitations
This theorem fixes \(\ell>0\) and \(1<s<2\), assumes complete origin resets to the symmetric flat-band-dark state and iid power-law restart intervals, and addresses one-time position statistics. It does not cover the marginal exponent \(s=2\), active initial coins with localized atomic weight, joint path laws, finite-time pointwise density limits, or first detection. The phase transition concerns singularity of the limiting density, not a finite-time thermodynamic phase transition. The proof and numerical diagnostics are same-source reproducible scientific evidence; no independent verification or universal priority certification is claimed.

## References
1. D. Das, *Restart and first detection in a lackadaisical quantum walk with flat-band localization*, arXiv:2609.08973v1 (public 2026-09-08), https://arxiv.org/html/2609.08973v1. Read Sections II.2, II.4, III, V and Appendices C and E.
2. M. Štefaňák, I. Bezděková and I. Jex, *Limit distributions of three-state quantum walks: the role of coin eigenstates*, arXiv:1405.7146 (2014), https://arxiv.org/abs/1405.7146. Read Sections I–II, especially its velocity-density representation.
3. W. Wang, M. Höll and E. Barkai, *Large deviations of the ballistic Lévy walk model*, Physical Review E 102, 052115 (2020), https://doi.org/10.1103/PhysRevE.102.052115. Compared ballistic-front processes with cumulative rather than resetting displacement.
