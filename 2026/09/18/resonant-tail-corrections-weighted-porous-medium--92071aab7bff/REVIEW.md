# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The source profile equation and leading tail were checked directly. With t=log xi and f=c_* exp(-qt)(1+epsilon), the radial Laplacian identity gives the exact relative-error equation stated in RESULT.md. The algebraic identities c_*^(p-1)=1/(p-1), alpha+beta q=1/(p-1), r=2+(m-1)q=D/(p-1), and h=1/beta=D/(m-p) were simplified symbolically.

The source's tail analysis places every bounded-profile orbit on the stable center manifold of the critical point corresponding to c_* xi^(-q). Its reduced linear dynamics contains the two rates -D/(p-1) and -1/beta. These are exactly -r and -h in logarithmic radius, agreeing with the direct profile-equation calculation. This provides the decay and derivative control needed to reduce the exact relative-error equation to beta epsilon_t + epsilon = A0 exp(-rt) + o(exp(-rt)) + O(epsilon^2).

Variation of constants then gives the three regimes. If r<h, the forced mode exp(-rt) dominates and its coefficient is A0/(1-beta r). If r=h, resonance produces (A0/beta)t exp(-rt). If h<r, the weighted equation for exp(ht)epsilon has an integrable right-hand side, so exp(ht)epsilon converges to a finite profile-dependent constant K_f. The identity 1-beta r=(2p-1-m)/(p-1) gives the displayed universal coefficient, and r=h is equivalent exactly to m=2p-1.

The curvature factor was checked independently from Delta_rad xi^(-s)=s(s-N+2)xi^(-s-2). Hence the additional cancellation A0=0 occurs exactly at s=N-2. The result deliberately does not claim a universal next coefficient after that cancellation or after K_f=0 in the homogeneous-mode regime.

The compact symbolic artifact reproduces the scaling identities and representative rates in all three regimes. For p=2, sigma=1, N=1 it gives (r,h)=(7/2,7) at m=5/2, (4,4) at m=3, and (5,5/2) at m=4. At the resonant point m=3, c_*=1 and A0/beta=48.

## Adversarial checks

The nonlinear term O(epsilon^2) does not alter the leading correction in the diffusion-forced or resonant regimes because it decays faster than the leading mode. In the homogeneous-mode regime it can create harmonics that precede the diffusion-forced term when K_f is nonzero, which is why no universal second correction beyond K_f xi^(-h) is asserted there.

If K_f=0, the leading homogeneous contribution cancels and a faster rate results; the next exponent can depend on nonlinear resonances. This exceptional case is left open rather than being identified automatically with the diffusion rate.

If s=N-2, the leading radial diffusion forcing vanishes. The stated theorem removes the corresponding coefficient but does not infer the next nonzero term without a higher-order calculation.

The result uses the bounded-profile tail manifold established by the source. It is not a theorem about arbitrary local solutions of the profile ODE that do not approach the source critical point.

## Originality

PASS, to the best of our knowledge.

The full source theorem and its tail dynamical-system analysis in arXiv:2609.20397v1 were inspected. The paper proves the universal leading tail c_* xi^(-sigma/(p-1)) for every bounded self-similar profile and classifies three distinct behaviors near the origin. It does not state a second-order tail expansion, the threshold m=2p-1, the logarithmic resonance there, the universal-versus-profile-dependent transition, or the separate curvature cancellation m sigma/(p-1)=N-2.

Searches covered the exact arXiv identifier and title together with `second-order asymptotic`, `tail correction`, `resonance`, `logarithmic correction`, `m=2p-1`, and synonymous weighted/spatially inhomogeneous porous-medium terminology. No source-specific correction or prior statement of this trichotomy was located. The current arXiv record inspected is v1, submitted 17 September 2026.

Earlier work by Iagar--Munteanu treats the complementary spatially inhomogeneous absorption range and supplies related dynamical-systems techniques, while Iagar--Laurençot studies second-order asymptotics for a different singular-diffusion equation with gradient absorption. These works are relevant methodological precedents and are not claimed as new here. No located result was found to imply the present m=2p-1 tail transition for the source equation.

The main residual originality risk is that older porous-medium or asymptotic-ODE literature may contain an equivalent second-order expansion under different variables or notation. The searches did not identify a specific inaccessible source with concrete evidence of such coverage. Because the source preprint is very recent, an unindexed author revision or discussion is also a residual risk.

## Value

PASS.

The source paper emphasizes that all bounded self-similar solutions share one leading far-field law despite having very different inner behavior. The present refinement identifies exactly when that universality persists one order further and when the first subleading term recovers profile-specific information. The transition is sharp, algebraic, and accompanied by a genuine logarithmic resonance at m=2p-1.

The additional condition m sigma/(p-1)=N-2 isolates a geometrically transparent cancellation of the radial diffusion curvature. Both thresholds are useful for higher-order matching, numerical tail fitting, and future large-time asymptotics based on the source profiles.

## Scope and limitations

The result is restricted to bounded radial self-similar profiles in the parameter range 1<p<m, sigma>0 and N>=1 considered in arXiv:2609.20397v1. It does not classify exceptional profiles with K_f=0, does not compute higher corrections after the curvature cancellation, and does not establish convergence rates for general PDE solutions. Originality is qualified to the best of our knowledge.
