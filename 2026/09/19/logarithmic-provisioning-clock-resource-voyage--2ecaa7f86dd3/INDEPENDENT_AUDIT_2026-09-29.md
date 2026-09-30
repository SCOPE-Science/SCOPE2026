# Independent audit — Logarithmic provisioning clocks and finite consumption capacity in a resource-coupled mortality model

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/logarithmic-provisioning-clock-resource-voyage--2ecaa7f86dd3`  
**Audited tree:** `a7bc0563ca55b81337dfcca6f575432b19b66735`

## Disposition

**PASSED.** Correctness, originality on the stated narrow boundary, and scientific value all pass. The record may remain in the validated set.

## Correctness

**PASS.** The two large-buffer theorems follow from exact identities. S=h+i satisfies S'=-mu h-delta i <= -m S, hence q=c1 h+c2 i <= c_+ e^{-mt}. For rho>0, p(t)=p0 e^{-rho t}-R(t) exactly; strict decrease while p>0 gives a unique positive-threshold crossing, and p<=p0 e^{-rho t} bounds it above by rho^-1 log(p0/pc). The lower bound at each fixed time forces t_c to infinity with p0, while the convolution bound makes R(t_c) tend to zero, proving the sharp additive logarithmic clock. For rho=0, total consumption is at most c_+/m. When p0 tends to infinity, p remains uniformly large, lambda(p)=alpha+O(p0^-1), and dominated convergence reduces lifetime consumption to the constant-coefficient (h,i) system; inverting that 2x2 generator gives integrals (gamma+delta)/D and alpha/D and hence the stated J_alpha.

## Originality

**PASS, with the limitations below.** This is a source-specific asymptotic correction, not a claim that integrating factors or compartmental comparison are new. The source arXiv:2609.20430 explicitly reports an approximately linear critical provisioning time over its transient study; it does not state the rho>0 logarithmic large-buffer limit, the rho=0 finite-consumption obstruction, or the explicit limiting J_alpha. Those conclusions use the source's own equations and alter the interpretation of its scaling observation. No prior source tied to this newly introduced model was identified as containing the same asymptotics; the main novelty is therefore the correction/refinement of that specific 2026 model rather than a general ODE technique.

## Scientific value

**PASS.** The result changes the asymptotic interpretation of a headline numerical trend in a new resource-health model. It cleanly separates direct stock deterioration from mortality-limited consumption and gives both a sharp logarithmic clock and a finite-capacity obstruction. That is a useful diagnostic for model calibration and for avoiding extrapolation of finite-window linear fits.

## Independent checks

- Integrated the resource equation exactly with an exponential integrating factor.
- Proved exponential decay of h+i and used it to control the consumption convolution and total lifetime consumption.
- Computed the limiting baseline-system inverse giving J_alpha.
- Compared the asymptotic conclusion with the source abstract's explicitly finite/transient approximately linear finding.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.20430 — Crokidakis source introducing the resource-coupled voyage model and reporting an approximately linear critical provisioning time in the transient study.
- https://arxiv.org/abs/2504.01649 — Related historical resource-dynamics model by the same author; contextual rather than covering the audited theorem.

## Limitations

- The analysis is for the deterministic source ODE and a fixed positive threshold; it does not validate historical calibration or stochastic/resupply extensions.
- No closed form for the finite/intermediate-buffer crossover is claimed.
- The novelty is source-specific asymptotics rather than the standard ODE tools used to prove them.

## Repository identity

The assigned source-tree SHA `a7bc0563ca55b81337dfcca6f575432b19b66735` matched the current tree at the audited path after comparing the assignment inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` with the source-tree checked commit `253a0fe5d0217455660a277f9adb940030e567ad`; none of the intervening changed files touched this record. GitHub was read only during the audit.
