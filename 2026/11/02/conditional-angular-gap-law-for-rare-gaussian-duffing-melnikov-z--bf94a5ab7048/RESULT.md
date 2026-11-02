# Conditional angular-gap law for rare Gaussian Duffing Melnikov zeros

## Finding

For the Gaussian Duffing Melnikov family defined below, let \(Z_{N,\omega}\) denote its number of zeros in one phase period. Whenever \(Z_{N,\omega}=2\), let \(\Delta_{N,\omega}\in(0,\pi)\) be the length of the shorter circular arc joining its two zero phases.

**Exact one-harmonic conditional law.** Put \(c=2\sqrt2/(3\pi)\), \(w_k=\omega k\operatorname{sech}(\pi\omega k/2)\), and \(t_\omega=w_1/c\). For every \(\omega>0\), and \(0\le d\le\pi\),
\[
\mathbb P(\Delta_{1,\omega}\le d\mid Z_{1,\omega}=2)
=1-\frac{\cos(d/2)\sqrt{1+t_\omega^2}}{\sqrt{1+t_\omega^2\cos^2(d/2)}}.
\]

**Universal high-frequency gap law.** Uniformly over every choice of integer \(N=N(\omega)\ge1\),
\[
\mathbb P(Z_{N,\omega}=2\mid Z_{N,\omega}\ge1)\longrightarrow1,
\qquad
\sup_{0\le d\le\pi}\left|\mathbb P(\Delta_{N,\omega}\le d\mid Z_{N,\omega}=2)-(1-\cos(d/2))\right|\longrightarrow0
\]
as \(\omega\to\infty\). The limiting gap density is \(\tfrac12\sin(d/2)\) for \(0<d<\pi\). On the two-zero event, the midpoint of the shorter arc is **exactly uniform in phase** and independent of the gap, at every finite \(N,\omega\).

**Rare-event amplitude selection.** Writing \(R=\sqrt{a_1^2+b_1^2}\), its conditional distribution given \(Z_{N,\omega}\ge1\) converges, uniformly over \(N\ge1\), in total variation to the Maxwell density \(\sqrt{2/\pi}\,r^2e^{-r^2/2}\,dr\) on \(r>0\). More precisely, jointly with \(R\), the normalized offset \(V=\delta/(t_\omega R)\) and first-harmonic phase converge in total variation to independent variables: this Maxwell amplitude, a uniform variable on \([-1,1]\), and a uniform angle on \([0,2\pi)\). The total-variation error is \(O(q+t_\omega^2)\), where \(q=e^{-\pi\omega/2}\), uniformly in \(N\). This joint statement implies the above limiting gap CDF by continuity of simple roots.

## Assumptions and scope

Let \(\omega>0\), \(N\in\{1,2,\ldots\}\), and let \(\delta,a_1,b_1,\ldots,a_N,b_N\) be mutually independent standard real Gaussian random variables. The normalized Melnikov function on \(\theta\in\mathbb R/(2\pi\mathbb Z)\) is
\[
G_{N,\omega}(\theta)=c\delta+\sum_{k=1}^N w_k(a_k\sin(k\theta)+b_k\cos(k\theta)),\qquad c=\frac{2\sqrt2}{3\pi},\quad w_k=\omega k\operatorname{sech}(\pi\omega k/2).
\]
This is exactly the distribution of the normalized function in Ittayem–Lundberg, equation (3.1), after \(\theta=\omega t_0\). Almost surely all zeros are simple: conditional on the nonconstant trigonometric part, its finite critical-value set is avoided by the independent continuous random offset \(c\delta\). The null event with two antipodal zeros is also excluded, so the shorter arc and its midpoint are well defined almost surely on \(Z=2\). All results concern **Melnikov zeros and phase geometry**, not exact nonlinear homoclinic intersection locations at fixed perturbation size.

## Proof

**1. Exact single-frequency law.** For \(N=1\), the random oscillatory part has amplitude \(w_1R\), with \(R=\sqrt{a_1^2+b_1^2}>0\) a Rayleigh variable. Define \(t=t_\omega=w_1/c\) and \(U=|\delta|/(tR)\). There are exactly two simple zeros if and only if \(0\le U<1\). Their shorter angular separation is \(\Delta=2\arccos U\). Rotational invariance of the standard Gaussian vector \((\delta,a_1,b_1)\in\mathbb R^3\) gives, for every \(s\ge0\),
\[
\mathbb P(|\delta|\le sR)=\frac{s}{\sqrt{1+s^2}}.
\]
To verify: polar direction on the unit sphere is uniform, so its absolute first coordinate is uniform on \([0,1]\); the displayed event is equivalent to that coordinate being at most \(s/\sqrt{1+s^2}\). Thus, for \(0\le u\le1\),
\[
\mathbb P(U\le u\mid U\le1)
=\frac{u\sqrt{1+t^2}}{\sqrt{1+t^2u^2}}.
\]
Substituting \(u=\cos(d/2)\), and taking the complementary tail, proves the finite-frequency CDF.

**2. Uniform control of all higher harmonics.** Let \(q=e^{-\pi\omega/2}\). Divide \(G_{N,\omega}\) by \(w_1\) and set
\[
B(\theta)=a_1\sin\theta+b_1\cos\theta,\qquad
H(\theta)=\sum_{k=2}^N\frac{w_k}{w_1}(a_k\sin(k\theta)+b_k\cos(k\theta)).
\]
For \(R_k=\sqrt{a_k^2+b_k^2}\), define \(S=\sum_{k=2}^N(w_k/w_1)R_k\), \(D=\sum_{k=2}^N k(w_k/w_1)R_k\). Then \(\|H\|_\infty\le S\), \(\|H'\|_\infty\le D\). Since \(w_k\le2\omega kq^k\), \(w_1=2\omega q/(1+q^2)\),
\[
\frac{w_k}{w_1}\le(1+q^2)kq^{k-1}\quad (k\ge2).
\]
The Rayleigh moments are finite, and therefore \(\mathbb ES+\mathbb ED=O(q)\), with all moments of \(S+D\) bounded independently of \(N\) for sufficiently small \(q\). All these bounds remain valid for arbitrary \(N=N(\omega)\).

**3. Total-variation limit under the rare zero event.** Let \(v=\delta/t\), \(t=w_1/c\), and write \(B(\theta)=R\sin(\theta+\phi)\). Conditional on every harmonic coefficient, \(G\) has at least one zero exactly when
\[
v\in I_H:=[-\max(B+H),-\min(B+H)].
\]
The endpoints of \(I_H\) differ by at most \(S\) from the endpoints of \(I_0=[-R,R]\). The unconditional density of \(v\) is \(t\varphi(tv)\), where \(\varphi\) is the standard normal density. For every bounded measurable test function \(F(R,v/R,\phi)\), the difference between
\[
\frac1t\mathbb E\big[F(R,v/R,\phi)\mathbf1_{\{v\in I_H\}}\big]
\quad\text{and}\quad
\varphi(0)\,\mathbb E\int_{-R}^{R}F(R,v/R,\phi)\,dv
\]
is bounded by \(2\varphi(0)\|F\|_\infty\mathbb ES+O(t^2)\|F\|_\infty\), because \(|\varphi(tv)-\varphi(0)|\le\tfrac12\varphi(0)t^2v^2\), while \(\mathbb E(R+S)^3\) is uniformly finite. Since \(2\varphi(0)\mathbb ER=1\), the zero-event probability divided by \(t\) tends uniformly to 1. Dividing the test-function identity by that probability gives **total variation** convergence, with error \(O(q+t^2)\), to the probability measure
\[
\frac{R\,d\mathbb P_R}{\mathbb ER}\ \otimes\ \operatorname{Unif}[-1,1]\ \otimes\ \operatorname{Unif}[0,2\pi).
\]
The first factor has the density \(\sqrt{2/\pi}\,r^2e^{-r^2/2}\), and the three factors are independent. This is a genuine rare-event size bias of the first-harmonic amplitude.

**4. From coefficient limits to actual zero locations.** The same conditional-integral bound and independence of \((R,\phi)\) from the higher harmonics yield
\[
\mathbb E[S+D\mid Z_{N,\omega}\ge1]=O(q)
\]
uniformly in \(N\): bound the conditional zero probability by \(2t\varphi(0)(R+S)\) and use the uniformly bounded second moments of \(S+D\). Hence \(\|H\|_{C^1}\to0\) in conditional probability. By Step 3, the random normalized offset \(v\), amplitude \(R\) and phase \(\phi\) converge jointly to a limit supported where \(R>0\) and \(|v|<R\) almost surely. Every such limiting function \(v+R\sin(\theta+\phi)\) has precisely two simple zeros. On a compact circle, a sufficiently small \(C^1\) perturbation of a function with precisely two simple zeros preserves their number and moves them continuously. The continuous-mapping theorem, or an elementary restriction to \(R\ge\eta\) and \(|v|\le(1-\eta)R\), now proves that the probability of exactly two roots conditioned on at least one tends to 1, and the short gap converges in distribution to \(2\arccos|V|\), with \(V\sim\operatorname{Unif}[-1,1]\). Its CDF is \(1-\cos(d/2)\); continuity of this CDF upgrades weak convergence to uniform CDF convergence. Every error estimate preceding root continuity is uniform in \(N\); compact truncation makes the root-continuity argument uniform as well.

**5. Exact uniform midpoint.** Shifting the phase by any angle \(\alpha\) rotates each independent isotropic Gaussian coefficient pair by \(k\alpha\). This preserves the law, as well as the event \(Z=2\) and the gap length, but translates the shorter-arc midpoint by \(\alpha\). Thus its conditional joint law with the gap is invariant under arbitrary rotations of the midpoint. Uniqueness of Haar probability on the circle proves the midpoint is uniform and independent of the gap, for every finite \(N,\omega\). The event of exactly antipodal zeros has probability zero: it would force the nonzero odd-harmonic part \(B(\theta)+\sum_{k\ge3,\ k\text{ odd}}(w_k/w_1)(a_k\sin k\theta+b_k\cos k\theta)\) to vanish at one of finitely many phases (almost surely), and would simultaneously require the independent continuous \(\delta\) to take one of finitely many prescribed values.

## Verification

The standalone Python 3 file `verify.py` checks the weight identity, a uniform deterministic higher-harmonic tail bound, and the exact one-harmonic gap CDF. It also runs fixed-seed independent Gaussian samples at three amplitudes and three gap thresholds, verifying the spherical conditional-law formula within sampling tolerances. It is supplementary finite evidence: the infinite-\(N\) and high-frequency uniform statements are proved above by geometric tail estimates and conditional convergence, **not** by simulations.

## Relationship to prior work

Ittayem and Lundberg (2026), arXiv:2610.33620v1, equation (3.1), establish the normalized random Melnikov function, expected zero counts, and high-/low-frequency zero-event bounds. Their Theorems 3.1 and 4.1 do not specify conditional zero **locations** or the law of the **shorter angular gap**. Counts cannot imply locations. Qualls (1970) studies counts in stationary Gaussian trigonometric polynomials; the complete text was not available for a full comparison. Existing Gaussian zero-count and spectral-statistics literature uses different large-degree or stationary regimes, rather than the rare first-harmonic-dominated high-frequency conditioning used here. The exact one-frequency CDF, Maxwell size bias, and uniform-in-degree high-frequency gap law are the distinct assertions examined here; historical priority remains provisional.

## Limitations

This is a conditional rare-event statement for an idealized independent Gaussian ensemble of **Melnikov functions**, not a theorem about the exact perturbed Duffing separatrices at a fixed perturbation size. The limit assumes \(\omega\to\infty\) and permits arbitrary finite \(N=N(\omega)\), but does not give a sharp uniform convergence rate for the observable zero gap. Higher-order splitting corrections, non-Gaussian coefficients, and noisy physical observations are not treated. Complete texts of some older specialized Gaussian-trigonometric papers were unavailable for exclusion of every historical antecedent.

## References

- A. Ittayem and E. Lundberg, *Zeros of Melnikov functions for periodically perturbed Hamiltonian systems with random coefficients*, arXiv:2610.33620v1, first submitted October 24, 2026. https://arxiv.org/html/2610.33620v1
- C. Qualls, *On the Number of Zeros of a Stationary Gaussian Random Trigonometric Polynomial*, J. London Math. Soc. (1970), DOI:10.1112/jlms/s2-2.2.216 (bibliographic record and article landing page inspected; not full text).
- J. Antezana, J. Buckley, J. Marzo, J.-F. Olsen, *Gap probabilities for the cardinal sine*, J. Math. Anal. Appl. 396 (2012), 466–472; arXiv:1108.2983 (abstract inspected; distinct zero-free interval model).
