# Exact two-stage loss of invertibility in a quadratic sine-circle map

## Finding

For the degree-one circle lift
\[
F_{a,b,\Omega}(x)=x+a\bigl[1-(\Omega-b\sin(2\pi x))^2\bigr],
\qquad a>0,\quad b\in\mathbb R\setminus\{0\},\quad \Omega\in\mathbb R,
\]
put \(B=|b|\), \(\rho=|\Omega|/B\), and
\[
\Delta=\sqrt{\rho^2+8},\qquad
\nu_\pm=\frac{\rho\pm\Delta}{4},\qquad
H_-(\rho)=\sqrt{1-\nu_-^2}\,(\rho-\nu_-).
\]
The sharp loss-of-invertibility threshold is
\[
\boxed{a_-(B,\rho)=\frac{1}{4\pi B^2 H_-(\rho)}.}
\]
For \(a<a_-\), the circle map is a real-analytic orientation-preserving diffeomorphism; at \(a=a_-\) it is a strictly increasing homeomorphism with isolated cubic stationary inflections; for \(a>a_-\) it is noninjective. In particular, its topological entropy is zero whenever \(a\le a_-\), because it is then a circle homeomorphism. Noninjectivity alone does **not** assert positive entropy or chaos.

If \(0\le\rho<1\), also put
\[
H_+(\rho)=\sqrt{1-\nu_+^2}\,(\nu_+-\rho),\qquad
\boxed{a_+(B,\rho)=\frac1{4\pi B^2H_+(\rho)}.}
\]
For \(0<\rho<1\) one has \(0<a_-<a_+\). The exact number of **distinct critical points** (zeros of \(F'\)) in one circle period is
\[
\begin{array}{c|ccccc}
\text{range of }a&(0,a_-)&a_-&(a_-,a_+)&a_+&(a_+,\infty)\\\hline
\#\{F'=0\}&0&1&2&3&4.
\end{array}
\]
At \(a=a_-\) the single derivative zero is double; at \(a=a_+\) two derivative zeros are simple and a third is double; all four zeros above \(a_+\) are simple. When \(\rho=0\), both thresholds coincide at \(a_-=a_+=1/(2\pi B^2)\); below it are no derivative zeros, at it exactly two double zeros, and above it exactly four simple zeros. When \(\rho\ge1\), the second threshold is absent; the zero counts are respectively \(0,1,2\) as \(a<a_-\), \(a=a_-\), or \(a>a_-\), with a double zero only at equality.

The second threshold has the sharp singular law
\[
\boxed{
 a_+(B,\rho)\sim\frac{3\sqrt3}{8\sqrt2\,\pi B^2}
 (1-\rho)^{-3/2}\quad(\rho\uparrow1).
}
\]
The two thresholds split linearly away from exact symmetry:
\[
\boxed{
 a_+(B,\rho)-a_-(B,\rho)
 =\frac{\sqrt2}{\pi B^2}\rho+O_B(\rho^2)
 \quad(\rho\downarrow0).
}
\]
Each newly born pair of ordinary turning points separates at square-root order in \(a-a_\pm\), with the explicit coefficient in the proof.

## Assumptions and scope

The map is the reduction introduced by Mugnaine, Sales, Szezech and Viana (2022), with \(a\in[0,1]\), \(b\in\mathbb R\), and \(\Omega\in[-1,1]\) in the motivating physical parameter domain. The theorem is a valid analytic extension to all \(a>0\), \(b\ne0\), and real \(\Omega\); its conclusions in the physical domain are obtained by intersection with those parameter bounds. The circle is \(\mathbb R/\mathbb Z\). A critical point means \(F'_{a,b,\Omega}(x)=0\) for the degree-one lift; a double derivative zero corresponds to an order-three stationary inflection of the lift, not an ordinary fold. Zeros are counted as distinct points modulo one, not with algebraic multiplicity.

## Proof

**1. Parameter reduction and derivative.** Translation of the angular variable by a half turn allows either sign of \(b\) and \(\Omega\) to be replaced by their absolute values when counting derivative zeros. Indeed, changing the sign of \(b\) is conjugate to a half-turn of the phase, and changing the sign of \(\Omega\) is likewise conjugate to a half-turn. Thus assume \(b=B>0\) and \(\Omega=B\rho\ge0\). Writing \(\theta=2\pi x\), one has
\[
F'(x)=1+4\pi aB^2 g_\rho(\theta),\qquad
 g_\rho(\theta)=\cos\theta\,(\rho-\sin\theta).
\]
The exact reflection identity \(g_\rho(\pi-\theta)=-g_\rho(\theta)\) makes its positive and negative extremes equal in magnitude.

**2. Exhaustive stationary-point analysis.** With \(s=\sin\theta\), differentiation gives
\[
g_\rho'(\theta)=2s^2-\rho s-1.
\]
Its two algebraic roots are \(\nu_-= (\rho-\Delta)/4\in(-1,0)\) and \(\nu_+=(\rho+\Delta)/4\). The latter belongs to \((0,1)\) precisely for \(\rho<1\), equals one when \(\rho=1\), and is outside the physical range for \(\rho>1\). The negative set of \(g_\rho\) consists of one lobe of depth \(H_-(\rho)\) for every \(\rho\ge0\), and a second lobe of depth \(H_+(\rho)\) when \(0\le\rho<1\). Each lobe has exactly one strict interior minimum. Explicitly, the deep minimum has sine \(\nu_-\), negative cosine, and value \(-H_-\); the shallow one has sine \(\nu_+\), positive cosine, and value \(-H_+\). For \(\rho>0\) with \(\rho<1\), the deep depth is strictly larger: evaluating the deep-lobe objective \(\sqrt{1-s^2}(\rho+s)\) at the positive sine which maximizes the shallow objective \(\sqrt{1-s^2}(s-\rho)\) gives a strict gain. For \(\rho=0\) the two lobes are symmetric and both depths equal \(1/2\).

It follows that
\[
\min_{x\bmod1}F'(x)=1-4\pi aB^2H_-(\rho)=1-a/a_-.
\]
The nonnegative, strictly positive, and negative-derivative cases now give precisely the asserted diffeomorphism, critical homeomorphism, and noninjective phases. At equality \(F'\ge0\) has only finitely many zeros, hence \(F\) is strictly increasing on the real line. For \(a>a_-\), the lift has both negative and positive derivative, so cannot be a degree-one circle homeomorphism.

**3. Exact zero counts.** On each negative lobe, \(F'\) equals one at its endpoints and has one strict interior minimum \(1-a/a_{\mathrm{lobe}}\). Therefore it contributes zero zeros below its threshold, one double zero at its threshold, and two simple zeros above its threshold. There are no zeros on nonnegative lobes. This establishes all cases, including the two simultaneous equal-depth lobes at \(\rho=0\), and the single lobe for \(\rho\ge1\).

**4. Nature and separation of critical points.** At either threshold let \(\nu\in\{\nu_-,\nu_+\}\) correspond to its lobe and \(c=\sqrt{1-\nu^2}>0\). At its minimum \(\theta_c\) one has \(g_\rho''(\theta_c)=\Delta c>0\). Thus \(F'(x_c)=F''(x_c)=0\) and \(F'''(x_c)=(2\pi)^2\,4\pi aB^2\Delta c>0\): the stationary inflection is cubic. For \(a=a_c+\varepsilon\) with \(\varepsilon\downarrow0\), the two nearby critical phases satisfy
\[
\boxed{
 \theta_\pm=\theta_c\pm
 \frac{\sqrt\varepsilon}{\sqrt{2\pi a_c^2 B^2\Delta c}}
 +O(\varepsilon).
}
\]
The expansion follows by Taylor expanding \(F'\) in \(a\) and \(\theta\); the linear term in \(a-a_c\) equals \(-\varepsilon/a_c\), while the quadratic angular term is \(2\pi a_cB^2\Delta c(\theta-\theta_c)^2\). The simple derivative zeros above threshold satisfy \(F''\ne0\), so they are ordinary folds.

**5. Singular and symmetry limits.** Put \(\eta=1-\rho\downarrow0\). Direct expansion of \(\nu_+\) gives \(\nu_+=1-\eta/3+O(\eta^2)\), hence
\[
H_+(\rho)=\frac23\sqrt{\frac23}\,\eta^{3/2}(1+O(\eta)).
\]
Inverting the definition of \(a_+\) gives the \(3/2\)-power divergence. At \(\rho\downarrow0\), the envelope theorem applied to the two nondegenerate lobe maxima yields
\[
H_-(\rho)=\tfrac12+\rho/\sqrt2+O(\rho^2),\qquad
H_+(\rho)=\tfrac12-\rho/\sqrt2+O(\rho^2),
\]
which gives the linear threshold splitting after inversion. Finally, every orientation-preserving circle homeomorphism has zero topological entropy, proving the stated entropy consequence without any claim about entropy in the noninjective phases.

## Verification

The standalone standard-library program `check_turning.py` evaluates the closed thresholds and derivative for 118 deterministic cases: generic derivative-zero counts across the three regimes, the exact derivative minimum, the singular \(3/2\)-power asymptotic, and square-root critical-point splitting. Executing `python3 check_turning.py` produces `PASS: 118 deterministic parameter and asymptotic tests`. These finite checks are supplementary; the full-domain proof above is analytic.

## Relationship to prior work

Mugnaine, Sales, Szezech and Viana (2022) derive the map and its derivative, analyze period-one saddle-node curves and numerical multistability, and explicitly observe that the loss-of-invertibility criticality does not have an obvious simple curve in the three-parameter domain (their Sec. II). Their fixed-point bifurcation curves \(b\pm\Omega=1\) concern \(F'=1\) at a fixed point, whereas the result here concerns \(F'=0\) anywhere on the circle; neither implication goes in the other direction. A 2025 follow-up by Baroni and collaborators considers a related strongly dissipative two-parameter quadratic-sinusoidal circle map, but its accessible abstract does not resolve the present full three-parameter fold stratification. Its complete text was not available for comparison; it remains a substantive priority risk, especially for the symmetric subfamily.

## Limitations

No classification of periodic attractors, basins, positive entropy after noninjectivity, or exact chaotic-onset boundary is claimed. The asymptotic threshold formula near \(\rho=1\) concerns analytic parameter continuation even when the second threshold lies beyond the original physical bound \(a\le1\). The literature comparison is not an exhaustive proof of publication priority; the uninspected 2025 follow-up and any unindexed multiharmonic-circle-map analysis remain risks.

## References

1. M. Mugnaine, M. R. Sales, J. D. Szezech Jr., and R. L. Viana, *Dynamics, multistability, and crisis analysis of a sine-circle nontwist map*, Physical Review E **106**, 034203 (2022), DOI: 10.1103/PhysRevE.106.034203, full author manuscript: https://fisica.ufpr.br/viana/artigos/2022/PhysRevE.106.034203.pdf (published 2022-09-06).
2. R. Simile Baroni, R. Egydio de Carvalho, C. E. P. Abreu, and R. O. Medrano-T, *Global dynamics and asymmetric fractal dimension in a nontwist circle map*, Chaos **35**, 023122 (2025), DOI: 10.1063/5.0238699 (abstract inspected; complete text not inspected).
3. Classical circle-homeomorphism entropy theorem: a circle homeomorphism has zero topological entropy; used only for the elementary dynamical consequence.
