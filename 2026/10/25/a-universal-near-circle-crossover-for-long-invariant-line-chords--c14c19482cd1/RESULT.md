# A universal near-circle crossover for long invariant-line chords

## Finding
Let \(f\in C^3(\mathbb R/2\pi\mathbb Z)\) be a real-valued periodic function. Let \(K_\delta\) have support function \(h_\delta(\varphi)=1+\delta f(\varphi)\), where \(0\le\delta<\delta_0(f)\) ensures positive curvature and a strictly convex boundary. Choose an **unoriented affine line** with invariant measure \(d\varphi\,dt\), conditioned on its intersection with \(K_\delta\); \(\varphi\in[0,\pi)\) is the line's normal angle and \(t\) its signed normal offset. Write \(L_\delta\) for the resulting chord length and \(D_\delta\) for the diameter. Define
\[
H(\theta)=f(\theta)+f(\theta+\pi),\quad M=\max_{\theta}H(\theta),\quad \Delta(\theta)=M-H(\theta)\ge0.
\]
The exact diameter is \(D_\delta=2+\delta M\). For **every** finite \(x\ge0\), whenever \(\varepsilon\downarrow0\), \(\delta\ge0\), and \(\delta/\varepsilon\to x\),
\[
\boxed{\quad \frac{\Pr\{L_\delta>D_\delta-\varepsilon\}}{\sqrt\varepsilon}\ \longrightarrow\ G_f(x)=\frac1\pi\int_0^\pi\sqrt{\bigl(1-x\Delta(\theta)\bigr)_+}\,d\theta.\quad}
\]
Here \(y_+=\max(y,0)\). If \(H\) is constant, then \(G_f(x)=1\) for all \(x\). Otherwise \(G_f\) is strictly decreasing on \([0,\infty)\). When the maximizers of \(H\) modulo \(\pi\) are finite and nondegenerate, meaning \(H''(\theta_j)<0\), the sharp far end of the crossover is
\[
G_f(x)\sim\frac1{2\sqrt x}\sum_{H(\theta_j)=M}\sqrt{\frac2{-H''(\theta_j)}}\qquad(x\to\infty),
\]
where each maximum is counted once modulo \(\pi\). These statements concern a simultaneous near-circle/long-chord limit; they do not assert fixed-body endpoint-density novelty.

## Assumptions and scope
The starting disk has radius one. For sufficiently small positive \(\delta\), the inequality \(h_\delta+h_\delta''=1+\delta(f+f'')>0\) ensures the support function describes a regular, strictly convex body. For \(\delta=0\), it is the unit disk. The probability law is normalized by the total invariant measure of intersecting unoriented lines, which equals the perimeter \(P_\delta=\int_0^{2\pi}h_\delta(\theta)\,d\theta\). In particular, it is **not** the random-endpoints, random-midpoints, or uniform-direction-then-uniform-offset-unconditionally convention. The ratio \(\delta/\varepsilon\) is nonnegative and converges to a finite \(x\); the separately stated asymptotic \(x\to\infty\) concerns the limiting profile \(G_f\), not a claim of uniformity in a diverging ratio.

## Proof
**Exact diameter.** For any compact convex \(K\),
\[
\operatorname{diam}(K)=\max_{\|u\|=1}\{h_K(u)+h_K(-u)\}.
\]
Indeed, the right side is \(\max_{u}\max_{p,q\in K}(p-q)\cdot u=\max_{p,q\in K}\|p-q\|\). Substitution of the support function gives \(D_\delta=2+\delta M\), with no asymptotic error.

**Uniform local chord expansion.** Parameterize the support boundary by \(X_\delta(\varphi)=h_\delta(\varphi)n(\varphi)+h_\delta'(\varphi)Jn(\varphi)\). This is \(C^2\) in \(\varphi\), uniformly for small \(\delta\), and is a \(C^2\) perturbation of the unit circle. Fix an unoriented chord direction \(v_\theta=(\cos\theta,\sin\theta)\), normal \(Jv_\theta\), and signed offset \(t\). For \(|t|\le1/2\), its two transversal intersections with the boundary depend smoothly on \((\delta,\theta,t)\) by the implicit function theorem. For the disk their separation is \(2\sqrt{1-t^2}\). Differentiation at \(\delta=0,t=0\) gives \(\partial_\delta L_\delta(\theta,0)|_{\delta=0}=f(\theta)+f(\theta+\pi)=H(\theta)\): to first order the radius in direction \(v\) is \(1+\delta f(v)\). The derivative in \(t\) is uniformly bounded for \(|t|\le1/2\). Therefore, uniformly in \(\theta\) and small \(t,\delta\),
\[
L_\delta(\theta,t)=2-t^2+\delta H(\theta)+O_f(t^4+\delta|t|+\delta^2).
\]
This expansion uses the actual intersections, not only the body's widths.

**Localization of nearly longest chords.** For some \(B_f>0\), the inclusions \((1-B_f\delta)B_2\subseteq K_\delta\subseteq(1+B_f\delta)B_2\) hold, because the support functions are uniformly within \(B_f\delta\) of one. A chord of \(K_\delta\) at offset \(t\) is no longer than the concentric outer disk chord \(2\sqrt{(1+B_f\delta)^2-t^2}\). If it exceeds \(D_\delta-\varepsilon\) with \(\delta=O(\varepsilon)\), this comparison forces \(|t|\le C\sqrt\varepsilon\), uniformly in angle. For such offsets, the expansion yields
\[
D_\delta-L_\delta(\theta,t)=t^2+\delta\Delta(\theta)+o(\varepsilon)
\]
uniformly whenever \(\delta/\varepsilon\) stays bounded. Set \(t=\sqrt\varepsilon\,z\). The indicator of a long chord then converges almost everywhere on a bounded \((\theta,z)\)-domain to \(\mathbf1\{z^2+x\Delta(\theta)<1\}\). Exceptional boundary points are a measure-zero set in \(z\). Dominated convergence, together with \(P_\delta\to2\pi\), gives
\[
\lim\frac{\Pr\{L_\delta>D_\delta-\varepsilon\}}{\sqrt\varepsilon}
=\frac1{2\pi}\int_0^\pi\int_{\mathbb R}\mathbf1\{z^2+x\Delta(\theta)<1\}\,dz\,d\theta=G_f(x).
\]

**Shape dependence and large-argument coefficient.** Only the antipodally even sum \(H\) occurs in the limit. If it is nonconstant, \(\Delta>0\) on an open set, and for any \(x_2>x_1\ge0\) the integrand decreases strictly on a set of positive angular measure; hence \(G_f(x_2)<G_f(x_1)\). If \(H\) has isolated nondegenerate maxima \(\theta_j\), then \(\Delta(\theta_j+u)=c_ju^2/2+o(u^2)\) with \(c_j=-H''(\theta_j)>0\). Rescale \(u=x^{-1/2}v\). The local contribution is
\[
\frac1{\pi\sqrt x}\int_{-\sqrt{2/c_j}}^{\sqrt{2/c_j}}\sqrt{1-\tfrac12 c_jv^2}\,dv
=\frac1{2\sqrt x}\sqrt{\frac2{c_j}}.
\]
Compactness makes contributions away from the finitely many maxima zero for large enough \(x\), proving the displayed sum.

**Ellipse consistency check.** For \(E_\lambda=\{(u,v):u^2/(1+\lambda)+v^2\le1\}\), the support function is \(1+\frac\lambda2\cos^2\theta+O(\lambda^2)\) uniformly with derivatives. Its antipodal sum is \(\cos^2\theta\), so the profile is \(\pi^{-1}\int_0^\pi\sqrt{(1-x\sin^2\theta)_+}\,d\theta\). Alternatively, for \(a=\sqrt{1+\lambda}\), \(Z(\theta)=1+\lambda\sin^2\theta\), and perpendicular line offset \(t\), the exact ellipse chord is \(2a\sqrt{Z-t^2}/Z\). Consequently
\[
\Pr\{L>2a-\varepsilon\}=\frac2{P_\lambda}\int_0^\pi\sqrt{\big[Z-Z^2(1-\varepsilon/(2a))^2\big]_+}\,d\theta.
\]
When \(\lambda/\varepsilon\to x\), the bracket divided by \(\varepsilon\) tends uniformly to \(1-x\sin^2\theta\). This recovers the universal profile, including \(G(0)=1\), \(G(1)=2/\pi\), and \(G(x)\sim(2\sqrt x)^{-1}\). The two limiting orders (first near-circle, then extreme chord) do not commute at the level of exponent.

## Verification
A standalone Python 3 program, `verify_chord_tails.py`, independently reconstructs ellipse chords from quadratic-line intersections, compares invariant-line Monte Carlo frequencies with an exact orientation integral, checks fixed-ellipse endpoint coefficients as diagnostic benchmarks, and tests the crossover for several aspect ratios. It also intersects lines with a sampled support-parameterized **nonelliptic** strictly convex curve whose perturbation contains even and odd harmonics. Its terminal output is `ALL_GENERAL_SUPPORT_CROSSOVER_CHECKS_OK`. Every universal and double-limit statement above follows from the proof, not finite numerical experiments.

## Relationship to prior work
Gates (1987) studied the initial and terminal densities of random chord-length distributions and described a smooth-versus-polygon distinction; the inaccessible full article is a particularly important historical-priority risk. The present claim deliberately does **not** assert novelty of a fixed-body terminal density. Bäsel's preprint (first public 12 April 2012) and its predecessor literature give complete chord-length distributions for regular polygons, not the simultaneous \(\delta/\varepsilon\to x\) law for arbitrary smooth near-circular support perturbations. Martirosyan (2023) studies orientation-dependent chord characteristics of quadrilaterals. General fixed-shape results do not by themselves supply a uniform asymptotic for a shape perturbation of the same size as the long-chord deficit. No definitive historical-priority conclusion is claimed.

## Limitations
The perturbation shape \(f\) is fixed and \(C^3\), while \(\delta\ge0\) and \(\delta/\varepsilon\) tends to a finite nonnegative number. The formula is not asserted uniformly when the ratio diverges. The large-argument expansion of \(G_f\) requires finitely many nondegenerate maxima; flat maxima yield other behavior. The law concerns motion-invariant isotropic lines conditioned to hit the body, not point-pair sampling. Gates (1987) full text was not accessible for a conclusive historical comparison. Independent validation and definitive priority verification have not been performed.

## References
1. J. Gates, *Some properties of chord length distributions*, Journal of Applied Probability 24 (1987), 863–874, DOI: 10.2307/3214211. Abstract inspected; full text unavailable.
2. U. Bäsel, *Random chords and point distances in regular polygons*, arXiv:1204.2707v1 (12 April 2012); full open version arXiv:1204.2707v2 (5 September 2012), §§1–5 inspected.
3. D. M. Martirosyan, *Orientation-Dependent Chord Length Distribution in a Convex Quadrilateral*, Journal of Contemporary Mathematical Analysis 58 (2023), 416–430, DOI: 10.3103/S1068362323060055. Scope and abstract inspected.
