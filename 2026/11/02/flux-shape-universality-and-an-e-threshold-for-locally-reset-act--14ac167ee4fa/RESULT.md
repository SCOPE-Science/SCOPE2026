# Flux-shape universality and an \(e\)-threshold for locally reset active-gas droplets

## Finding

For a class of density-dependent run-and-tumble transport laws with an arbitrary strictly concave gas current and a constant-speed dense phase, the stationary two-phase droplet has a **constitutive-law-independent width** and mass partition. In contrast, the availability of a competing continuous gas-only stationary profile depends on the maximum of the gas current. Their relative thresholds meet at the sharp dimensionless ratio \(F_{\max}/J=e\).

More precisely, define \(\Lambda=\sqrt{r(r+\alpha)}\), \(J=u\rho_m\), and let \(F_{\max}\) be the gas-current maximum defined below. Within the explicitly specified symmetric, monotone, single-interface stationary class:

1. A continuous gas-only profile exists exactly when \(M\Lambda/2\le F_{\max}\). A nondegenerate central dense droplet exists exactly when \(M\Lambda/2>J\). Consequently the two **distinct stationary branches** coexist precisely for \(J<M\Lambda/2\le F_{\max}\); this does **not** assert dynamical stability or uniqueness among arbitrary weak solutions.
2. Every such droplet has half-width
   \[
   b(r)=\frac{u}{\Lambda}\log\!\left(\frac{M\Lambda}{2J}\right),
   \]
   gas mass \(2J/\Lambda\), and liquid mass \(M-2J/\Lambda\), irrespective of the shape of the gas current.
3. The unique maximal droplet half-width is \(b_\star=M/(2e\rho_m)\), attained at \(\Lambda_\star=2eJ/M\). At this optimum exactly \(1/e\) of the mass is gas and \(1-1/e\) is dense, for **every** admissible gas current.
4. The width-maximizing reset rate lies inside the gas/droplet coexistence interval if \(F_{\max}/J>e\), at its upper fold if the ratio equals \(e\), and after the gas branch has disappeared if the ratio is less than \(e\). At the gas-only fold, the origin density exhibits the universal square-root law
   \[
   \rho_p-\rho_0\sim\sqrt{\frac{2(F_{\max}-M\Lambda/2)}{|f''(\rho_p)|}}.
   \]

This theorem separates a geometrically universal optimal droplet from a constitutive-law-dependent stationary coexistence window.

## Assumptions and scope

Fix \(M>0\) (total conserved mass), \(\alpha>0\) (uniform direction-reselection rate), \(r>0\) (independent local-resetting rate), a dense-phase threshold \(\rho_m>0\), and a dense-phase speed \(u>0\). In the gas, let \(f:[0,\rho_m)\to[0,\infty)\) be twice continuously differentiable, with \(f(0)=0\), \(f'(0)>0\), and \(f(\rho)>0\) for \(0<\rho<\rho_m\). Assume \(f\) is strictly concave in the strong sense \(f''(\rho)<0\), and has a unique interior maximum \(F_{\max}=f(\rho_p)\) at \(0<\rho_p<\rho_m\), where \(f'(\rho_p)=0\). Require \(F_{\max}>J:=u\rho_m\). The gas speed is \(v_g(\rho)=f(\rho)/\rho\) (extended continuously at zero); the dense speed is the constant \(u\). A density discontinuity across the phase interface is allowed, with continuity of both directional particle currents.

For \(x\ne0\), the stationary right/left mover densities \(q_\pm\) obey
\[
0=-\partial_x(vq_+)-\left(r+\frac{\alpha}{2}\right)q_++\frac{\alpha}{2}q_-,\qquad
0=\partial_x(vq_-)-\left(r+\frac{\alpha}{2}\right)q_-+\frac{\alpha}{2}q_+.
\]
Each reset injects at the origin, with its new direction selected uniformly. The full density is symmetric, \(q_+(x)=q_-(-x)\), has integral \(M\), and tends to zero at infinity. We examine continuous gas profiles with \(0<\rho(x)\le\rho_p\) on \(x>0\) and their symmetric extensions, or one dense interval \([-b,b]\) with \(\rho(b^-)=\rho_m\) and a monotone dilute gas outside. No additional atoms, interfaces, or shock solutions are admitted to this branch classification. The statement concerns stationary solutions of the kinetic mean-field equations, not an exact stochastic many-particle invariant law.

## Proof

**Flux identity.** Let \(\rho=q_++q_-\), \(\sigma=q_+-q_-\), \(R=v(\rho)\rho\), and \(S=v(\rho)\sigma\). The stationary equations on each phase give
\[
S'=-r\rho,\qquad R'=-(r+\alpha)\sigma.
\]
Hence \(S^2-\frac{r}{r+\alpha}R^2\) is constant. Both currents vanish at positive infinity, so the constant vanishes in the gas; current continuity transfers the same identity into the dense interval. The outward current is nonnegative, therefore, with \(c=\sqrt{r/(r+\alpha)}\),
\[
S=cR,\quad \sigma=c\rho,\quad R'=-\Lambda\rho.
\]
These identities are valid separately on every smooth phase and are compatible with the flux jumps and reset source at the origin.

**Gas-only branch.** On the increasing branch \(0<\rho\le\rho_p\), \(R=f(\rho)\), so
\[
f'(\rho)\rho'=-\Lambda\rho.
\]
If \(\rho(0^+)=\rho_0\), its unique decreasing profile is the inverse of
\[
\Lambda x=\int_{\rho(x)}^{\rho_0}\frac{f'(z)}{z}\,dz.
\]
The integral diverges as \(\rho(x)\downarrow0\), because \(f'(0)>0\), proving the profile extends to infinity and has no finite-support ambiguity. Integrating \(R'=-\Lambda\rho\) gives \(\Lambda M/2=f(\rho_0)\). The strict increase of \(f\) from \(0\) to \(F_{\max}\) on \([0,\rho_p]\) proves existence and uniqueness *within this gas branch* exactly for \(M\Lambda/2\le F_{\max}\). At equality the profile has an integrable endpoint cusp, interpreted in the stationary weak sense. Strict concavity and Taylor's theorem give the stated square-root fold for \(\rho_0\).

**Droplet branch.** At \(x=b>0\), the dense interface has density \(\rho_m\) and current \(J=u\rho_m\). Current continuity forces the gas interface density to be the **unique lower-branch root** \(\rho_b\in(0,\rho_p)\) of \(f(\rho_b)=J\); this root exists since \(F_{\max}>J\). Integrating the same flux identity from \(b\) to infinity yields
\[
\int_b^\infty\rho(x)\,dx=\frac{J}{\Lambda}.
\]
This identity requires no special function and no formula for the shape of \(f\). The gas density is determined uniquely by
\[
\Lambda(x-b)=\int_{\rho(x)}^{\rho_b}\frac{f'(z)}{z}\,dz.
\]
Inside the dense interval, \(R=u\rho\), so
\[
\rho(x)=\rho_m\exp\!\left(\frac{\Lambda(b-x)}{u}\right),\qquad 0\le x\le b,
\]
with half-droplet mass \(J\bigl(e^{\Lambda b/u}-1\bigr)/\Lambda\). Conservation of total mass now reads
\[
\frac M2=\frac J\Lambda e^{\Lambda b/u},
\]
forcing the claimed formula for \(b\) and proving \(b>0\) exactly when \(M\Lambda/2>J\). These expressions construct a positive, normalized profile with \(\rho(x)\ge\rho_m\) inside and \(0<\rho(x)\le\rho_b<\rho_m\) outside. The directional densities are \(q_\pm=(1\pm c)\rho/2\) for \(x>0\), interchanged for \(x<0\); their fluxes are continuous across \(b\). At the reset origin, \(S(0^+)=cM\Lambda/2=rM/2\), exactly the required symmetric injection jump. Thus the constructed profiles satisfy the distributional stationary system. The flux argument also proves their uniqueness within the stated branch class.

**Optimum and coexistence topology.** Since \(r\mapsto\Lambda\) is strictly increasing on \((0,\infty)\), maximize \(b(\Lambda)=u\Lambda^{-1}\log(M\Lambda/(2J))\) for \(\Lambda>2J/M\). Its derivative has the sign of \(1-\log(M\Lambda/(2J))\), and its unique maximum occurs at \(\Lambda_\star=2eJ/M\). Substitution gives \(b_\star=M/(2e\rho_m)\). The gas mass ratio at the optimum is \(2J/(M\Lambda_\star)=1/e\). The gas branch ends at \(\Lambda_s=2F_{\max}/M\), so comparing \(\Lambda_\star\) with \(\Lambda_s\) proves the sharp \(e\)-classification. All assertions follow without assuming anything about transient stability.

**Two explicitly different laws.** Set \(\rho_m=8\), \(u=1/8\), \(M=4\), \(\alpha=1\). For \(f_1(\rho)=\rho(1-\rho/8)\), the peak is \(F_{\max}^{(1)}=2\). For \(f_2(\rho)=\rho[1-(\rho/8)^2]\), it is \(F_{\max}^{(2)}=16/(3\sqrt3)>e\). The same optimal two-phase profile width is \(1/(4e)\) for both. Yet at that optimal reset rate the first law admits no pure gas branch, while the second admits one. This is a qualitative change induced solely by gas constitutive shape, despite invariant optimal droplet size.

## Verification

The package contains `verify.py`, a deterministic Python-standard-library test on \(f_p(\rho)=\rho[1-(\rho/8)^p]\) for \(p=1,2,3,4,7\). It independently checks the integrated gas and dense mass with numerical quadrature, reconstructs the gas profile by implicit inversion, compares its finite-difference derivative with the kinetic stationary ODE, and checks the exact branch disparity for \(p=1\) and \(p=2\), universal optimal half-width, and mass partition. Run `python3 verify.py`. These finite evaluations illustrate the theorem; the proof is the exact flux argument above.

## Relationship to prior work

Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting*, arXiv:2610.26149v2 (2026), establishes the kinetic first integral in its Section 2 and solves the **specific linear gas motility** \(v_g(\rho)=v_0(1-\rho/\rho_m)\) with saturated dense speed. Its Sections 3–4 calculate a droplet size, gas existence threshold, and coexistence regime for that particular law, while Section 5 investigates finite-speed return with a particular multiplicative form. These established statements and their algebraic consequences, including the optimal width for the linear law, are not claimed as new here.

The present result isolates a different axis: it treats an **arbitrary strictly concave gas current** with the same constant-speed dense phase, and proves simultaneously that (i) its droplet width and optimal condensed fraction are invariant under this deformation, (ii) its gas-only spinodal depends only on the gas peak current, and (iii) the exact ratio \(F_{\max}/J=e\) governs whether maximal condensation occurs with or without a competing gas stationary solution. The two explicit nonlinear laws show that the last distinction is not merely a reparameterization of one gas profile. The general flux identity in Grange's Section 2 is an important precursor to this extension.

Cates and Tailleur, *Motility-Induced Phase Separation*, arXiv:1406.3533 (2014; journal 2015), gives general active-matter motivation for density-dependent speeds, not the present local-resetting branch classification.

## Limitations

The result classifies **only** the symmetric piecewise-smooth branches with increasing-current dilute profiles and at most one centered dense interval; it does not exclude other weak/shock solutions. Neither branch's dynamical or stochastic stability is proved. Direction-reselection and resetting are Poisson, the dense speed is constant, and the dilute current is strictly concave with a single interior peak. Interactions and fluctuations beyond the deterministic kinetic description, higher dimensions, diffusion, or return times are not addressed. The \(e\)-classification concerns the existence of stationary gas and droplet branches, not an experimentally verified hysteresis loop. Prior literature may contain a more general flux-balance formulation, and independent external scientific validation has not been undertaken.

## References

1. P. Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting*, arXiv:2610.26149, first submitted 2026-10-19. https://arxiv.org/html/2610.26149v2
2. M. E. Cates and J. Tailleur, *Motility-Induced Phase Separation*, arXiv:1406.3533, first submitted 2014-06-13; Annual Review of Condensed Matter Physics **6** (2015), 219–244. https://arxiv.org/abs/1406.3533
3. M. E. Evans, S. N. Majumdar, and G. Schehr, *Stochastic resetting and applications*, Journal of Physics A: Mathematical and Theoretical **53** (2020), 193001. https://doi.org/10.1088/1751-8121/ab7cfe
