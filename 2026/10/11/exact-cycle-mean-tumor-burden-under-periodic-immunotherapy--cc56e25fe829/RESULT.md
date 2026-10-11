# Exact cycle-mean tumor burden under periodic immunotherapy
## Finding
Consider
\[
\dot x=ax-bxy,\qquad \dot y=dxy-fy-\kappa x+\vartheta(t),
\]
where \(a,b>0\), \(\vartheta\) is continuous and \(T\)-periodic, and \((x(t),y(t))\) is a strictly positive \(T\)-periodic solution. With \(\overline h=T^{-1}\int_0^T h(t)\,dt\), every such cycle obeys
\[
\overline y=\frac ab,\qquad (da-\kappa b)\overline x=fa-b\overline\vartheta.
\]
If \(da\ne\kappa b\), this fixes the cycle-mean tumor burden as
\[
\overline x=\frac{fa-b\overline\vartheta}{da-\kappa b}.
\]
For the periodic cytokine forcing \(\vartheta(t)=u+F\cos^2(\omega t)\), whose period is \(T=\pi/\omega\), one has \(\overline\vartheta=u+F/2\), hence
\[
\overline x=\frac{fa-bu-bF/2}{da-\kappa b},\qquad \overline y=\frac ab.
\]
Thus changing treatment frequency or waveform while preserving its cycle mean can change existence, stability and oscillation shape, but not the mean tumor burden of a positive forcing-locked cycle in this model. On \(da=\kappa b\), the compatibility condition \(fa=b\overline\vartheta\) is necessary; if it fails, no strictly positive forcing-locked periodic solution exists.

## Assumptions and scope
The statement concerns classical solutions with \(x(t)>0\), \(y(t)>0\) for all \(t\), and with the same period \(T\) as the forcing. The same proof applies when the orbit period is an integer multiple of the forcing period. No small-amplitude, averaging, or linearization assumption is used. The identity is necessary, not sufficient, for a positive periodic orbit.

The motivating periodic-immunotherapy paper studies periodic solutions by averaging and lists primary MSC 34C25. Its introductory six-parameter model is the Sotolongo-Costa tumor–immune system with a cosine-squared treatment term. The original model paper studies how treatment dose and frequency affect tumor dynamics.

## Proof
Because \(x(t)>0\),
\[
\frac{d}{dt}\log x=a-by.
\]
Integration over one period gives \(0=a-b\overline y\), hence \(\overline y=a/b\).

Periodicity of \(x\) also gives
\[
0=\overline{\dot x}=a\overline x-b\overline{xy},
\]
so \(\overline{xy}=(a/b)\overline x\). Integrating the second equation over one period yields
\[
0=d\overline{xy}-f\overline y-\kappa\overline x+\overline\vartheta.
\]
Substitution of the first two identities gives
\[
0=\left(\frac{da}{b}-\kappa\right)\overline x-\frac{fa}{b}+\overline\vartheta,
\]
which, after multiplication by \(b\), is exactly
\[
(da-\kappa b)\overline x=fa-b\overline\vartheta.
\]
The nonresonant formula and resonant compatibility condition follow immediately. For \(u+F\cos^2(\omega t)\), direct integration over \(\pi/\omega\) gives \(\overline\vartheta=u+F/2\).

## Verification
The proof is an exact period-integration argument. Each boundary term vanishes by periodicity, and the logarithmic step uses only strict positivity of \(x\). No numerical experiment, finite enumeration, or asymptotic truncation is used. The resonant case \(da=\kappa b\) was checked separately rather than dividing by a possibly zero coefficient.

## Relationship to prior work
Torres-Espino and Vidal prove sufficient conditions for existence and stability of periodic tumor–immune solutions using averaging. Their inspected equations and averaged equilibria encode the familiar leading-order lymphocyte level, but the inspected material does not state the finite-amplitude cycle-mean elimination above. The original Sotolongo-Costa et al. paper defines the cosine-squared forced system and analyzes dose-frequency thresholds numerically and dynamically; searches of its full text for “average” and “mean” did not locate the stated cycle-mean law. A later global-analysis paper by Torres-Espino and Zamora studies the same therapy setting with topological methods; its abstract and accessible metadata do not state this identity.

The classical Lotka–Volterra mean-value calculation is a conceptual ancestor of the first equality \(\overline y=a/b\). The new content here is the exact elimination through the forced immune equation, which fixes \(\overline x\) from the mean treatment and yields the sharp resonant compatibility obstruction for the immunotherapy model.

## Limitations
The result does not prove that a positive periodic solution exists, is unique, or is stable. It does not constrain transient trajectories or cycles that are not synchronized to a period over which the forcing average is \(\overline\vartheta\). Full text of the later 2021 global-analysis paper was not lawfully accessible in the inspected sources, so an unobserved equivalent statement there remains a residual literature risk.

## References
1. G. Torres-Espino and C. Vidal, “Periodic solutions of a tumor-immune system interaction under a periodic immunotherapy,” *Discrete and Continuous Dynamical Systems - B* 26 (2021), 4523–4547, DOI 10.3934/dcdsb.2020301. Early access 2020-10-15.
2. O. Sotolongo-Costa, L. Morales-Molina, D. Rodríguez-Pérez, J. C. Antoranz and M. Chacón-Reyes, “Behavior of tumors under nonstationary therapy,” *Physica D* 178 (2003), 242–253, DOI 10.1016/S0167-2789(03)00005-8.
3. G. Torres-Espino and M. Zamora, “Dynamic aspects of tumour–immune system interaction under a periodic immunotherapy,” *European Journal of Applied Mathematics* 33 (2022), 606–645, DOI 10.1017/S0956792521000152.
