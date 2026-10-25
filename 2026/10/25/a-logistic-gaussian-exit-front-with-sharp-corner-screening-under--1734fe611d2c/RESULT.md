# A logistic–Gaussian exit front with sharp corner screening under Poisson resetting

## Finding
Consider planar Brownian motion in the positive quadrant, with generator \(D(\partial_{xx}+\partial_{yy})\), where \(D>0\). Both coordinate axes absorb. During an excursion from \((x,y)\in(0,\infty)^2\), an independent Poisson clock of rate \(\lambda=Dq^2\), \(q>0\), either interrupts the excursion and resets both coordinates to \((x,y)\), or the excursion succeeds by reaching an axis. The first successful excursion terminates the process. Let \(I=1\) mean it ends at the axis \(x=0\), and let \(H\) be **only the duration of that final successful excursion**.

**Exact finite-parameter corner bound.** Write \(R=\sqrt{x^2+y^2}\), let \(K_\nu\) denote the modified Bessel function of the second kind, and set
\[
 h_x=\mathbb E[e^{-Dq^2T_x};\,T_x<T_y],\qquad
 h_y=\mathbb E[e^{-Dq^2T_y};\,T_y<T_x],
\]
where \(T_x,T_y\) are independent one-dimensional Brownian hitting times from respective distances \(x,y\), both with diffusivity \(D\). Define the corner deficit \(\delta_x=e^{-qx}-h_x\). Then for **every** \(x,y,D,q>0\),
\[
\boxed{
0\leq\frac{2x}{\pi y}K_0(qR)-\delta_x
\leq\frac{2xR}{\pi y^3q}K_1(qR).
}
\]
The same bound with \(x,y\) exchanged holds for \(\delta_y=e^{-qy}-h_y\). In particular, the actual splitting probability is exactly
\[
\mathbb P(I=1)=\frac{e^{-qx}-\delta_x}{e^{-qx}+e^{-qy}-\delta_x-\delta_y}.
\]
For \(x,y\) in any fixed compact subset of \((0,\infty)^2\), uniformly as \(q\to\infty\),
\[
\delta_x=\frac{2x}{\pi y}K_0(qR)\bigl(1+O(q^{-1})\bigr).
\]

**A simultaneous exit-side and excursion-time limit.** Fix \(a,D>0\) and \(z\in\mathbb R\). For \(q\to\infty\), reset to
\[
 x_q=a-\frac{z}{2q},\qquad y_q=a+\frac{z}{2q},\qquad \lambda_q=Dq^2,
\]
and let \((I_q,H_q)\) denote the final successful side and duration. Define
\[
V_q=\frac{2Dq^{3/2}}{\sqrt a}
\left(H_q-\frac{a}{2Dq}\right),\qquad
\ell(z)=\frac1{1+e^{-z}}.
\]
Then
\[
\boxed{(I_q,V_q)\ \Longrightarrow\ (B_z,Z),\qquad
\mathbb P(B_z=1)=\ell(z),\quad Z\sim N(0,1),\quad B_z\perp Z.}
\]
Furthermore, the first exponentially small correction to the exit-side law is **sharp**:
\[
\boxed{
\lim_{q\to\infty}\sqrt q\,e^{(\sqrt2-1)aq}
\bigl(\mathbb P(I_q=1)-\ell(z)\bigr)
=\frac1\pi\sqrt{\frac\pi{2\sqrt2a}}
\frac{\sinh(z/2)}{\cosh^2(z/2)}.
}
\]
This limit is locally uniform in \(z\). At \(z=0\) the splitting probability is exactly \(1/2\) for every admissible \(q\), not merely asymptotically. Thus the nontrivial side-selection window has geometric width \(q^{-1}=\sqrt{D/\lambda}\), while successful-excursion times have mean scale \(q^{-1}\), fluctuation scale \(q^{-3/2}\), and an independent limiting Gaussian fluctuation. The corner contributes the explicitly quantified smaller scale \(q^{-1/2}e^{-aq(\sqrt2-1)}\) to the splitting probability.

## Assumptions and scope
The planar coordinates are independent Brownian motions between resets, each with variance \(2Dt\); resetting is instantaneous and complete, acts simultaneously on the two coordinates, and is independent of the Brownian motions. The boundary is the union of the two positive coordinate axes, with absorption at first contact. All resets return to the **same** strictly interior point. The side of the first successful excursion agrees with the side of eventual absorption. For the limit, \(a,D,z\) are fixed and \(q\) tends to infinity through values with \(x_q,y_q>0\). No statement concerns the **total** absorption time including unsuccessful excursions.

## Proof
**1. Renewal reduction and exact marked densities.** The excursion-level hitting times \(T_x,T_y\) are independent. The one-dimensional hitting-time density and survival function are
\[
f_x(t)=\frac{x}{\sqrt{4\pi D}}t^{-3/2}e^{-x^2/(4Dt)},\qquad
S_y(t)=\operatorname{erf}\!\left(\frac{y}{\sqrt{4Dt}}\right).
\]
The defective density of an excursion that beats both resetting and absorption at the other axis and ends at \(x=0\) is \(e^{-Dq^2t}f_x(t)S_y(t)\,dt\). Integrating gives \(h_x\). Since failed excursions independently regenerate the same initial configuration, the final successful excursion's joint marked law is the normalized sum of the two defective measures, normalized by \(h_x+h_y>0\). The standard one-dimensional Laplace identity
\[
\int_0^\infty e^{-Dq^2t}f_x(t)\,dt=e^{-qx}
\]
implies \(\delta_x=\int_0^\infty e^{-Dq^2t}f_x(t)\operatorname{erfc}(y/\sqrt{4Dt})\,dt\).

**2. Exact, all-rate Bessel enclosure.** Put \(u=y/(2\sqrt{Dt})\) and \(m(u)=\sqrt\pi u e^{u^2}\operatorname{erfc}(u)\). The change of variables in the complementary-error-function integral gives
\[
m(u)=\int_0^\infty e^{-w-w^2/(4u^2)}\,dw,
\qquad 0\leq1-m(u)\leq\frac1{2u^2}=\frac{2Dt}{y^2}.
\]
Consequently, exactly,
\[
\delta_x=\frac{x}{\pi y}\int_0^\infty t^{-1}
 e^{-Dq^2t-R^2/(4Dt)}m\!\left(\frac y{2\sqrt{Dt}}\right)dt.
\]
The two positive-kernel identities
\[
\int_0^\infty t^{-1}e^{-Dq^2t-R^2/(4Dt)}dt=2K_0(qR),
\]
\[
\int_0^\infty e^{-Dq^2t-R^2/(4Dt)}dt=\frac R{Dq}K_1(qR)
\]
yield both inequalities in the stated enclosure, without any asymptotic approximation. On interior compact sets the standard positive-real-argument expansion \(K_1(s)/K_0(s)=1+O(s^{-1})\) gives its uniform relative error \(O(q^{-1})\).

**3. Logistic boundary layer and its corner coefficient.** For the specified \(x_q,y_q\), write \(A=e^{-qx_q}=e^{-aq+z/2}\), \(B=e^{-qy_q}=e^{-aq-z/2}\), and \(R_q=\sqrt{x_q^2+y_q^2}=\sqrt2a+O(q^{-2})\). The Bessel enclosure and \(K_0(s)\sim\sqrt{\pi/(2s)}e^{-s}\) show, locally uniformly in \(z\),
\[
\delta_{x_q}=\frac2\pi K_0(\sqrt2aq)\bigl(1+O(q^{-1})\bigr),\qquad
\delta_{y_q}=\frac2\pi K_0(\sqrt2aq)\bigl(1+O(q^{-1})\bigr).
\]
Since both are exponentially smaller than \(A+B\), expand \((A-\delta_{x_q})/(A+B-\delta_{x_q}-\delta_{y_q})\). Its leading term is \(A/(A+B)=\ell(z)\). The first correction equals
\[
\frac{e^{aq}}\pi K_0(\sqrt2aq)
\frac{\sinh(z/2)}{\cosh^2(z/2)}
+o\!\left(q^{-1/2}e^{-(\sqrt2-1)aq}\right),
\]
which gives the displayed sharp limit. At \(z=0\), coordinate exchange is an exact symmetry and makes both splitting probabilities \(1/2\).

**4. Conditional Gaussian duration and independence.** Remove the opposite-axis survival factors temporarily. For either distance \(d\in\{x,y\}\), the resulting normalized tilted hitting-time law has Laplace transform
\[
\mathbb E_{\nu_{d,q}}e^{-sT}
=\exp\left[-d\left(\sqrt{q^2+s/D}-q\right)\right],
\]
where \(d\) is the starting distance from the corresponding absorbing axis. It has exactly
\[
\mathbb E_{\nu_{d,q}}T=\frac{d}{2Dq},\qquad
\operatorname{Var}_{\nu_{d,q}}(T)=\frac{d}{4D^2q^3}.
\]
Expanding its characteristic function at the \(q^{-3/2}\) scale proves that \(2Dq^{3/2}(T-a/(2Dq))/\sqrt a\Rightarrow N(0,1)\) for both \(d=x_q\) and \(d=y_q\). The unnormalized total variation discarded by omitting the competing boundary is exactly \(\delta_{x_q}+\delta_{y_q}\). Normalizing changes the joint side/time law by total variation at most \((\delta_{x_q}+\delta_{y_q})/(A+B-\delta_{x_q}-\delta_{y_q})\), which tends to zero exponentially. The approximating law is a mixture of the two tilted hitting-time laws with side weights \(A/(A+B)\) and \(B/(A+B)\); since each component has the same Gaussian limit, the joint limit is the independent Bernoulli–Gaussian pair claimed.

## Verification
The accompanying standalone `verify.py` numerically checks the exact independent hitting-time integrals against their Laplace identities, the global Bessel \(K_0/K_1\) enclosure, reflection symmetry, and finite-parameter approach to the sharp boundary-layer coefficient. With Python and SciPy, the program completed **816 deterministic checks**. These are finite consistency checks; steps 1–4 above supply the infinite-range mathematical proof. The script uses direct positive one-dimensional quadrature rather than unverified simulation claims.

## Relationship to prior work
Najeeb, Pal and Prasad, arXiv:2505.04208 (public May 7, 2025), subsequently *Physical Review E* 113, 024104 (2026), derive the underlying wedge-resetting renewal kernels, boundary currents, conditional exit-time quantities, and splitting probabilities. They explicitly report the high-reset preference for the nearer absorbing side and exact equality at the bisector. **None of these prior results is claimed as new here.** The present theorem resolves a coupled near-bisector scaling in which neither side is asymptotically certain, obtains an all-rate Bessel enclosure and its sharp exponentially small coefficient, and identifies the joint final-excursion time fluctuation law. The finite-rate splitting law of the earlier paper can in principle be specialized and asymptotically analyzed; deriving the sharp bound and coupled front is the claimed additional mathematical work, not a different model.

The earlier Brownian wedge survival study by Chupeau, Bénichou and Majumdar (2015) provides free-diffusion survival and short-time expansions; the conditional-resetting criterion of Pal and collaborators (2025) addresses mean selective outcomes rather than the present marked high-rate limit. A general Gaussian hitting-time tilt or Bessel-kernel asymptotic theorem may give ingredients, and independent originality assessment remains necessary.

## Limitations
The sharp Bessel enclosure and joint switching front are proved only for the right-angle wedge, where the two Brownian coordinates separate. Nothing here implies the same coefficient for arbitrary wedge angle, correlated coordinate noise, partial resetting, random reset locations, or non-Poisson resets. The normal limit is for the *final successful excursion*, not for the entire search duration. Its limiting independence is not finite-rate independence. The published finite-rate wedge analysis contains the building blocks, so novelty must be judged at the level of the new sharp quantified statement rather than the known renewal identities. Independent review has not been performed.

## References
1. F. Najeeb, A. Pal and V. V. Prasad, *Diffusion in a wedge geometry: First-Passage Statistics under Stochastic Resetting*, arXiv:2505.04208v1 (first public May 7, 2025); revised journal version, *Phys. Rev. E* **113**, 024104 (2026), DOI: 10.1103/3bc4-nlkt.
2. M. Chupeau, O. Bénichou and S. N. Majumdar, *Survival probability of a Brownian motion in a planar wedge of arbitrary angle*, *Phys. Rev. E* **91**, 032106 (2015), DOI: 10.1103/PhysRevE.91.032106.
3. S. Pal, L. Dagdug, D. Ghosh, D. Boyer and A. Pal, *Universal criterion for selective outcomes under stochastic resetting*, arXiv:2502.09127v1 (2025), *Phys. Rev. E* **112**, 034116 (2025).
