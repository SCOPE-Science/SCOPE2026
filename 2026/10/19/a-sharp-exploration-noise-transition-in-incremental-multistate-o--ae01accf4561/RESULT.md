# A sharp exploration-noise transition in incremental multistate opinion dynamics

## Finding
For every integer \(k\geq1\), the nearest-neighbor incremental opinion mean-field model with an additional independent symmetric one-step exploration rate \(\varepsilon>0\) has a **single, explicit noise threshold**
\[
\varepsilon_c(k)=\frac{2k-1}{3}.
\]
At or above this threshold, the uniform distribution on the \(2k+1\) ordered opinion levels is the only equilibrium and attracts every initial probability vector. Below it there are exactly three equilibria: uniform (a saddle with one unstable direction), and exactly two exponentially tilted, oppositely polarized distributions (both locally asymptotically stable). Every trajectory converges to one of these three states; the uniform equilibrium attracts at most a measure-zero set of interior initial conditions below threshold. The polarized mean vanishes at the transition with an explicit square-root coefficient, and **every polarized equilibrium obeys the exact second-moment identity**
\[
\sum_{j=-k}^{k}j^2p_j=k(k-\varepsilon).
\]

## Assumptions and scope
Fix \(k\in\mathbb N\), \(k\ge1\), and \(\varepsilon>0\). An agent has opinion \(j\in J_k=\{-k,-k+1,\ldots,k\}\). Put \(p_j(t)\ge0\), \(\sum_jp_j(t)=1\), and \(m(t)=\sum_j j p_j(t)\). In the mean-field incremental persuasion model, an opinion increases by one at rate \((1+m/k)/2\) when below \(k\), or decreases by one at rate \((1-m/k)/2\) when above \(-k\). Add **independent symmetric spontaneous exploration** at rate \(\varepsilon/2\) for each permitted direction, with attempted outward steps suppressed at the endpoints. Thus the total directed rates are
\[
 a(m)=\frac{1+\varepsilon+m/k}{2},\qquad
 b(m)=\frac{1+\varepsilon-m/k}{2}.
\]
Write \(F_j=a(m)p_j-b(m)p_{j+1}\) for \(-k\le j<k\), and impose \(F_{-k-1}=F_k=0\). The equations are exactly \(\dot p_j=F_{j-1}-F_j\). The theorem concerns this deterministic mean-field ODE, not a finite-population stationary distribution; its exploration mechanism is an additional modeling assumption, not an equation asserted by the motivating paper.

Define \(Z_k(s)=\sum_{j=-k}^{k}e^{sj}\), \(\mu_s(j)=e^{sj}/Z_k(s)\), \(V_k=k(k+1)/3\), and
\[
W_k=\operatorname{Var}_{\mu_0}(J^2)
=\frac{k(k+1)[4k(k+1)-3]}{45}>0.
\]
For \(0<\varepsilon<\varepsilon_c(k)\), let \(s_\varepsilon>0\) be the unique solution of
\[
\mathbb E_{\mu_s}[J^2]=k(k-\varepsilon).
\]
The polarized equilibrium laws are \(\mu_{s_\varepsilon}\) and \(\mu_{-s_\varepsilon}\). Their positive mean \(m_\varepsilon\) satisfies
\[
 m_\varepsilon\sim V_k\sqrt{\frac{2k}{W_k}}
\sqrt{\varepsilon_c(k)-\varepsilon}
\qquad(\varepsilon\uparrow\varepsilon_c(k)).
\]

## Proof
**1. A character identity and its monotonicity.** The partition function has the exact representation
\[
Z_k(s)=\frac{\sinh((k+1/2)s)}{\sinh(s/2)}
\quad(s\ne0),
\]
with continuous extension at zero. Direct differentiation gives
\[
Z_k''(s)+\coth(s/2)Z_k'(s)=k(k+1)Z_k(s).
\]
Consequently, for \(s>0\),
\[
\frac{\mathbb E_{\mu_s}J}{\tanh(s/2)}
=k(k+1)-\mathbb E_{\mu_s}J^2=:H_k(s).
\]
The distribution of \(D=|J|\) under \(\mu_s\) has weights proportional to \(1\) for \(D=0\) and \(2\cosh(sd)\) for \(1\le d\le k\). For \(s_2>s_1\ge0\), the ratio \(\cosh(s_2d)/\cosh(s_1d)\) is strictly increasing in \(d\), since its logarithmic derivative is \(s_2\tanh(s_2d)-s_1\tanh(s_1d)>0\). Thus \(\mathbb E_{\mu_s}J^2\) strictly increases for \(s>0\) (strict covariance with \(d^2\)), from \(V_k\) to \(k^2\). Equivalently, \(H_k(s)\) strictly decreases from \(2k(k+1)/3\) to \(k\).

**2. Exact equilibrium classification.** Since \(a,b\ge\varepsilon/2>0\), every equilibrium has all components positive and every edge flux zero. Hence \(p=\mu_s\), with \(e^s=a(m)/b(m)\), equivalently
\[
m=k(1+\varepsilon)\tanh(s/2).
\]
At \(s=0\), the uniform law is always an equilibrium. At \(s\ne0\), the identity of Step 1 reduces the self-consistency condition exactly to \(H_k(|s|)=k(1+\varepsilon)\), or \(\mathbb E_{\mu_s}J^2=k(k-\varepsilon)\). Strict monotonicity gives precisely one positive solution (and its negative) for \(0<\varepsilon<(2k-1)/3\), and none at or above threshold. This proves both completeness and the sharp moment identity.

**3. A strict Lyapunov function and global convergence.** For \(|m|\le k\), define a smooth potential by \(\Phi_\varepsilon(0)=0\) and
\[
\Phi_\varepsilon'(m)=\log\frac{a(m)}{b(m)}
=2\operatorname{arctanh}\left(\frac{m}{k(1+\varepsilon)}\right).
\]
On the probability simplex use
\[
\mathcal E(p)=\sum_jp_j\log p_j-\Phi_\varepsilon\left(\sum_jjp_j\right),
\]
with \(0\log0=0\). Every trajectory enters the simplex interior immediately, and positive lower/upper bounds on both jump rates imply a uniform positive lower bound on components at all sufficiently late times (consider one fixed time-unit interval of the inhomogeneous birth-death propagator). In the interior, summation by parts gives exactly
\[
\frac{d\mathcal E}{dt}
=-\sum_{j=-k}^{k-1}(a p_j-bp_{j+1})
\log\frac{a p_j}{b p_{j+1}}\le0.
\]
Each summand is nonnegative before the minus sign, with equality precisely when all fluxes vanish. LaSalle's invariance principle on the eventual compact interior, followed by connectedness of the omega-limit set and finiteness of the equilibrium set, implies that every trajectory converges to a single equilibrium. When \(\varepsilon\ge\varepsilon_c(k)\), the uniform state is the only one, proving global attraction.

**4. Stability and critical scaling.** On the tangent space \(\sum_jv_j=0\), the Hessian of \(\mathcal E\) at a stationary probability \(p\) is
\[
D^2\mathcal E_p[v,v]=\sum_j\frac{v_j^2}{p_j}
-\Phi_\varepsilon''(m)\left(\sum_jjv_j\right)^2.
\]
It is positive definite exactly when \(\Phi_\varepsilon''(m)\operatorname{Var}_p(J)<1\), and has exactly one negative direction when this product exceeds one. At uniformity the product is \(\varepsilon_c(k)\)-critical: it equals \(2(k+1)/(3(1+\varepsilon))\). At each nonzero branch, the strict decrease of \(H_k\) makes the derivative of \(\mathbb E_{\mu_s}J-k(1+\varepsilon)\tanh(s/2)\) negative at its zero, which is equivalent to strict positivity of this Hessian. The vector field is a gradient flow with strictly positive edge logarithmic-mean mobilities in the simplex interior. Its linearization therefore has the negative of the Hessian's inertia: below threshold uniformity has one unstable eigenvalue and all remaining eigenvalues stable, whereas each polarized branch is locally asymptotically stable. The smooth stable-manifold theorem makes the interior basin of the uniform saddle a set of Lebesgue measure zero.

Finally, Taylor expansion under \(\mu_s\) yields \(\mathbb E_{\mu_s}J^2=V_k+\tfrac12W_ks^2+O(s^4)\) and \(\mathbb E_{\mu_s}J=V_ks+O(s^3)\). Combining these with the exact moment identity yields the displayed positive square-root law. This completes the theorem.

## Verification
The accompanying standalone `checker_published.py` performs finite numerical and algebraic consistency tests of the partition-function identity, equilibrium equations for \(1\le k\le9\), entropy decrease, the elementary \(k=1\) closed-form branch, and numerical ODE convergence. It reports 444 successful checks. In particular, at \(k=2\) and \(\varepsilon=1/2\), the polarized tilt and mean are approximately \(s=1.14103333363535\) and \(m=1.54721585869541\). These tests do not certify the claims for every integer \(k\); the proofs above are analytic.

## Relationship to prior work
Cao and Gong introduce the incremental persuasion mean-field law without spontaneous exploration, and prove convergence/basin results for that *zero-noise model* (arXiv:2605.28984v1, 27 May 2026, especially Section 2 and Section 3). Their paper neither incorporates the independent symmetric exploration mechanism defined here nor classifies its noise-dependent equilibria. Multistate noisy-voter literature, such as Khalil and Galla (Phys. Rev. E 103, 012311, 2021), studies imitation among categorical states together with mutation, rather than the ordered nearest-neighbor incremental persuasion mechanism analyzed here; its known finite-population modal transitions must not be equated with this deterministic infinite-population pitchfork. Doniec, Lipiecki and Sznajd-Weron (Entropy 24, 983, 2022) analyze bounded-confidence unanimous-group updates and a different independence mechanism, also not the present generator. The general concept of noise-driven opinion transitions is not claimed as new. The specific sharp \(k\)-dependent threshold, exact polarized second-moment identity, and the accompanying global flow classification for these precisely stated nearest-neighbor rates constitute the claim.

## Limitations
The statement is restricted to mean-field dynamics on a complete-mixing population, linearly persuasive probabilities, symmetric independent adjacent-step exploration, reflecting endpoint suppression, and \(\varepsilon>0\). No finite-population stationary law, metastable switching time, empirical inference, or precise global separatrix below threshold is asserted. Independent scientific audit has not been performed. A full-text comparison with Khalil–Galla (2021) could not be completed from the accessible sources; the difference in microscopic transition rules was verified from available descriptions, but an unindexed coincidentally equivalent theorem remains a residual literature risk.

## References
1. Fei Cao and Xiaoqian Gong, *The incremental voter model: mean-field analysis and convergence to equilibrium*, arXiv:2605.28984v1, first submitted 27 May 2026. https://arxiv.org/html/2605.28984v1
2. Nagi Khalil and Tobias Galla, *Zealots in multistate noisy voter models*, Physical Review E **103**, 012311 (2021), arXiv:2007.07535. https://doi.org/10.1103/PhysRevE.103.012311
3. Maciej Doniec, Arkadiusz Lipiecki, and Katarzyna Sznajd-Weron, *Consensus, Polarization and Hysteresis in the Three-State Noisy q-Voter Model with Bounded Confidence*, Entropy **24**, 983 (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9319784/
4. American Mathematical Society, *MSC2020*, entry 91D30, “Social networks; opinion dynamics.” https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=91D10
