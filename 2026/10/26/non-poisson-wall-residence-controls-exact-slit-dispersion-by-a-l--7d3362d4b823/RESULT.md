# Non-Poisson wall residence controls exact slit dispersion by a Laplace transform

## Finding

For the four-direction confined run-and-tumble particle defined below, arbitrary independent wall-residence times with finite positive mean retain the original mean bulk occupancy but change the **exact longitudinal effective diffusivity** through one Laplace-transform value. Put \(b=2W/v\), \(m=\mathbb E S\), \(\phi=b/(b+m)\), and \(L(\beta)=\mathbb E[e^{-\beta S}]\). Then

\[
D(F;\beta)=\phi\frac{v^2}{2\lambda}+(1-\phi)\frac{\bar v^2}{\beta}\left[1-\frac{1-L(\beta)}{\beta m}\right].
\]

At fixed \(m\), any nontrivial increase in wall-residence variability in the **convex order** strictly increases \(D\) if \(\bar v>0\). Its sharp distribution-free bounds are

\[
\phi\frac{v^2}{2\lambda}+(1-\phi)\frac{\bar v^2}{\beta}\left[1-\frac{1-e^{-\beta m}}{\beta m}\right]
\ \le\ D(F;\beta)\ <\
\phi\frac{v^2}{2\lambda}+(1-\phi)\frac{\bar v^2}{\beta}.
\]

The lower bound is attained precisely by deterministic positive dwell time; the upper bound is a nonattained supremum over finite-second-moment dwell laws. Moreover, varying the **surface orientation-decorrelation rate** \(\beta\) determines the full dwell-time law because

\[
L(\beta)=1-\beta m+\frac{\beta^2m}{(1-\phi)\bar v^2}\left[D(F;\beta)-\phi\frac{v^2}{2\lambda}\right].
\]

Thus bulk occupancy cannot distinguish wall-time distributions with the same mean, whereas the longitudinal diffusion-versus-decorrelation curve can.

## Assumptions and scope

Fix width \(W>0\), bulk speed \(v>0\), bulk tumble rate \(\lambda>0\), wall speed \(\bar v>0\), and wall decorrelation rate \(\beta>0\). The transverse coordinate lies in \([-W/2,W/2]\). In the interior the velocity has four cardinal possibilities \((\pm v,0),(0,\pm v)\). At events of an independent rate-\(\lambda\) Poisson process, its direction is chosen uniformly among the four possibilities; a redraw may repeat the old direction.

Upon reaching either wall in an outward-pointing direction, the particle immediately starts a wall sojourn with independent initial longitudinal velocity sign \(\pm\bar v\), each with probability one-half. During the sojourn this sign flips at Poisson rate \(\beta/2\). Its duration \(S\ge0\) is sampled independently of these flips and all previous dynamics, with \(0<m=\mathbb E S<\infty\) and \(\mathbb E S^2<\infty\); every visit draws a new independent copy. At the end of the sojourn the particle moves from that wall into the interior in the unique inward cardinal direction; its previous longitudinal sign is forgotten. There is no translational Brownian noise. Wall-to-wall excursions are independent after reflection of the transverse coordinate and reinitialization of all random mechanisms.

The asymptotic diffusivity is \(D=\lim_{t\to\infty}\operatorname{Var}(X_t-X_0)/(2t)\), and the corresponding diffusive central-limit theorem also holds. Statements about convex-order strictness, sharp extrema, and inverse recovery require \(\bar v>0\). The comparison class for extrema consists of all laws on \([0,\infty)\) with prescribed mean \(m>0\) and finite second moment (and the same extrema hold as infimum/supremum when strictly positive sojourns are required).

## Proof

**1. Regenerative bulk excursions.** Let \(B\) be the duration of one interior excursion, entered at the lower wall with upward velocity; reflection gives the same law for entrance at the upper wall. Write \(h=W/2\) and let \(u_U(y),u_D(y),u_H(y)\) denote expected exit times for upward, downward, and either horizontal direction. The four-state generator, with uniform rate-\(\lambda\) redraws, satisfies \(-\mathcal G u=1\) and absorbing conditions \(u_U(h)=u_D(-h)=0\). Direct substitution gives

\[
\begin{aligned}
u_U(y)&=\frac{\lambda(h^2-y^2)}{v^2}+\frac{2(h-y)}v,\\
u_D(y)&=\frac{\lambda(h^2-y^2)}{v^2}+\frac{2(h+y)}v,\\
u_H(y)&=\frac{\lambda(h^2-y^2)}{v^2}+\frac{2h}v+\frac2\lambda.
\end{aligned}
\]

A uniform positive probability of reaching a wall within any fixed sufficiently long interval gives an exponential tail for \(B\), which justifies the stopped-generator equations. Hence

\[
\mathbb EB=u_U(-h)=\frac{4h}{v}=\frac{2W}{v}=b.
\]

Let \(H\) be the longitudinal displacement of the bulk excursion, and let \(V_x\in\{-v,0,v\}\) be its longitudinal instantaneous velocity. Uniform redraws give \(\mathcal G V_x=-\lambda V_x\) and \(\mathcal G(V_x^2)=\lambda(v^2/2-V_x^2)\). Therefore \(H_t+V_x(t)/\lambda\) is a martingale, and both the initial and terminal \(V_x\) are zero. Optional stopping of \(V_x^2\) yields \(\mathbb E\int_0^B V_x(t)^2dt=(v^2/2)b\). The predictable quadratic variation of the martingale has rate \((v^2/2+V_x^2)/\lambda\), so its stopped second moment is

\[
\mathbb EH=0,\qquad \mathbb EH^2=\frac{v^2}{\lambda}b.
\]

**2. Arbitrary wall-time law.** During a wall sojourn the symmetric telegraph sign \(\xi_t\) has \(\mathbb E[\xi_s\xi_t]=e^{-\beta|t-s|}\). Given \(S=s\), the longitudinal wall displacement \(J=\bar v\int_0^s\xi_tdt\) has mean zero and

\[
\mathbb E[J^2\mid S=s]=\frac{2\bar v^2}{\beta}\left[s-\frac{1-e^{-\beta s}}\beta\right].
\]

Thus \(\mathbb EJ^2=(2\bar v^2/\beta)[m-(1-L(\beta))/\beta]\). Wall and interior displacements are independent, with no directional memory crossing a boundary, and the cycles \((B+S,H+J)\) are identically distributed and independent by reflection symmetry. The mean cycle duration is \(b+m\) and the centered cycle displacement has variance \((v^2/\lambda)b+\mathbb EJ^2\). The regenerative central-limit theorem and renewal-reward second-moment limit apply: cycle times have finite second moments, and motion has bounded speed. Dividing the cycle variance by twice the mean cycle duration gives the displayed \(D\). The renewal-reward occupation fraction is exactly \(\phi=b/(b+m)\), which depends on the wall law only through its mean.

**3. Strict convex ordering and sharp limits.** If \(S_1\preceq_{cx}S_2\) and both have mean \(m\), strict convexity of \(s\mapsto e^{-\beta s}\) gives \(L_1(\beta)\le L_2(\beta)\), strictly when the two laws differ. The formula is strictly increasing in \(L(\beta)\) for \(\bar v>0\). Jensen gives \(L(\beta)\ge e^{-\beta m}\), with equality only for \(S=m\) almost surely. As \(m>0\), \(L(\beta)<1\); two-point laws concentrating probability near zero while allocating rare, increasingly long positive sojourns to preserve mean \(m\) have \(L(\beta)\uparrow1\). Each such law has finite second moment, proving both extrema sharp.

**4. Identifiability and useful limits.** Rearranging the explicit diffusivity yields the displayed recovery formula for \(L(\beta)\). Uniqueness of the Laplace transform on \([0,\infty)\) means that knowledge of \(D(F;\beta)\) at every \(\beta>0\), together with \(m,W,v,\lambda,\bar v\), determines \(F\). At a single fixed \(\beta\), only one Laplace-transform value is identified. For exponential \(S\) with rate \(\mu=1/m\), \(L(\beta)=\mu/(\mu+\beta)\), and the formula reduces exactly to the published Poisson-escape result

\[
D=\phi\frac{v^2}{2\lambda}+(1-\phi)\frac{\bar v^2}{\beta+\mu}.
\]

With finite \(\mathbb ES^2\), the long-persistence wall limit also follows by expanding the Laplace transform:

\[
\lim_{\beta\downarrow0}D(F;\beta)
=\phi\frac{v^2}{2\lambda}+(1-\phi)\frac{\bar v^2\mathbb ES^2}{2m}.
\]

## Verification

The standalone script `verification/check_surface_diffusion.py` uses only the Python standard library. Execute `python verification/check_surface_diffusion.py`. It tests the bulk backward generator at 31 transverse positions, the exponential-wall reduction, Laplace recovery, convex-order examples, and the slow-orientation limit. It also simulates independent physical direction-changing trajectories for 65,000 wall/bulk cycles under each of four residence laws: deterministic, Gamma shape two, exponential, and two-point. The simulated diffusion coefficients were respectively \(0.3966633\), \(0.4228015\), \(0.4416129\), and \(0.5401593\), compared with exact values \(0.3990211\), \(0.4266957\), \(0.4463560\), and \(0.5393513\) at the specified numerical parameters. All programmed checks passed. These finite tests corroborate but do not prove the all-law theorem; the analytic regenerative proof does.

## Relationship to prior work

Pietrangeli, Ybert, Cottin-Bizonne, and Detcheverry established the Poisson-escape four-direction slit diffusion formula and its optimization (their Eq. (1) and Sec. II.3); they explicitly identify non-Poissonian escape as a missing extension in their Conclusion. That result is recovered here exactly, and neither the original model nor its Poisson formula is claimed as new. Datta, Beta, and Großmann derive arbitrary waiting-time diffusion formulas for a *spatially homogeneous* alternating active/immobile state model, not this bounded four-direction bulk plus **moving** wall with resetting at each contact. Salgado-García analyzes adsorption on spatially disordered obstacles with displacement during adhesion tied to obstacle geometry, not a persistent, freely translating wall state. Both are relevant general antecedents, and the general renewal-reward method is classical. The evaluated combination of a wall Laplace-transform law, a strict convex-order transport effect at fixed occupancy, and inverse dwell-law recovery was not identified in the inspected sources; priority beyond those sources remains unproved.

## Limitations

The result concerns an idealized discrete-direction slit, independently renewed wall sojourns, exponentially decorrelating velocity *within* each wall sojourn, and finite second moment of the surface dwell time. It does not prove comparable formulas for continuous orientation, correlated wall dwell times, wall sliding coupled to the escape clock, heavy-tailed dwell distributions without a second moment, reflecting boundary dynamics without directional reinitialization, or interacting swimmers. Laplace-curve recovery is an exact mathematical identifiability statement, not a statistical stability guarantee for noisy finite observations. Full publication-priority exclusion against all possible general renewal transport theorems is not established.

## References

1. T. Pietrangeli, C. Ybert, C. Cottin-Bizonne, F. Detcheverry, *Optimal run-and-tumble in slit-like confinement*, Phys. Rev. Research **6**, 023028 (published 5 April 2024), DOI: https://doi.org/10.1103/PhysRevResearch.6.023028 ; author-preprint https://arxiv.org/abs/2404.07680 (first arXiv version 11 April 2024).
2. A. Datta, C. Beta, R. Großmann, *The random walk of intermittently self-propelled particles*, https://arxiv.org/abs/2406.15277 (2024).
3. R. Salgado-García, *Active particles in reactive disordered media: how does adsorption affect diffusion?*, https://arxiv.org/abs/2105.10840 (2021).
4. G. Junot et al., *Run-to-Tumble Variability Controls the Surface Residence Times of E. coli Bacteria*, https://arxiv.org/abs/2107.11123 (2021).
