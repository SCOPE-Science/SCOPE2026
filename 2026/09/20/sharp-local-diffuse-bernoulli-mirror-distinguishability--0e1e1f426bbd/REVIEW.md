# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** The mirror total variation is exactly the `L1` norm of the odd Walsh polynomial

\[
H_a(\varepsilon)=\frac12\left[\prod_i(1+a_i\varepsilon_i)-\prod_i(1-a_i\varepsilon_i)\right].
\]

Orthogonality makes the squared `L2` norm of all degrees at least three an explicit sum of squared monomial coefficients, uniformly bounded by `e^v-1-v-v^2/2=O(v^3)`. Together with `1-e^{-v} <= Delta^2 <= v`, this proves the dimension-free local expansion. The sharp local interval follows from the classical optimal `p=1` Khintchine constants, with exact one- and two-coordinate witnesses.

For the diffuse finite-signal theorem, half the log-likelihood ratio is `S=sum atanh(a_i) epsilon_i`. Under the plus law its mean and variance are both `v+o(1)`, while the maximal summand vanishes; Lindeberg therefore gives `S => N(v,v)`. Reflection interchanges the plus and minus laws, so the threshold-zero likelihood-ratio test gives the stated total-variation limit. The product overlap converges to `e^{-v/2}`, yielding the stated `Delta` limit. The monotonicity calculation for the limiting ratio reduces to `2 sinh(t^2/2) > t integral_0^t exp(-u^2/2) du`, which follows strictly from `2 sinh(t^2/2)>t^2` and the integral being less than `t`.

The verification artifact independently checks exact low-dimensional formulas and homogeneous-binomial convergence. No numerical check is used in place of a proof.

## Originality

**PASS, to the best of our knowledge.** Smirnov's 2026 preprint is the direct source: it introduces the mirror-product family in the Bernoulli-product reduction, identifies `Delta`, and proves only an unspecified absolute-constant lower comparison for the computational-basis measurement. The sharp Khintchine constants are due to Haagerup, and local asymptotic normality is classical; neither is claimed as new. Recent Bernoulli-product TV papers by Avital--Kontorovich--Salafatinos and Kontorovich address small-parameter structure, tensorization, or homogenization rather than this mirror-measurement efficiency.

Searches for equivalent formulations using mirror Bernoulli products, Rademacher products, Hellinger/total-variation efficiency, local alternatives, and computational-basis distinguishability did not locate the displayed uniform local identity, the complete local interval, or the explicit finite-signal curve. The strongest residual risk is older binary-experiment or Riesz-product literature: the finite-signal normal limit is a classical LAN phenomenon, so an equivalent asymptotic formula could exist under different notation. The novelty claim is therefore restricted to the explicit mirror-product sharpening and its source-specific efficiency geometry, not to LAN or Khintchine theory themselves.

The global optimal constant in Smirnov's Theorem 4.1 is not resolved. Numerical evidence is not used to assert the plausible stronger inequality `tau >= Delta/sqrt(2)`.

## Value

**PASS.** The result turns a qualitative constant-factor measurement theorem into a sharp weak-signal description. It identifies the exact first-order loss as a Rademacher `L1/L2` geometry, proves that local efficiencies fill precisely `[1/sqrt(2),1]`, and shows that diffuse alternatives obey a one-parameter efficiency curve increasing from `sqrt(2/pi)` to one. This distinguishes sparse/concentrated and diffuse signal geometries that are invisible to `Delta` alone and gives explicit calibration for the new Bernoulli-product reduction.

## Limitations

- The sharp interval is a weak-signal statement.
- The finite-signal theorem assumes the largest coordinate tends to zero.
- No quantitative triangular-array convergence rate is claimed.
- The globally optimal mirror-product comparison constant remains open here.
- Classical LAN, Gaussian test power, and sharp Khintchine constants are prior art.
- Older binary-experiment and Riesz-product literature was not exhaustively inspected.
- Cross-model review has not been performed.
