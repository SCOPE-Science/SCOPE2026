# Independent audit — 2026/09/16/001

**Date:** 2026-09-29  
**Disposition:** **REPAIRED**  
**Audited tree:** `6def786d3426e317ce51dc5a88d16808b3f01e85` at repository commit `253a0fe5d0217455660a277f9adb940030e567ad`

## Correctness

**REPAIRED** — The two-step transfer-matrix conjugacy to an almost-Mathieu equation is exact for E!=0; an independent symbolic multiplication gives P(B_E A_{E,theta})P^{-1}=[[E^2-2-2 lambda E cos(2pi theta),-1],[1,0]]. The arithmetic bound beta(alpha)<=beta(2alpha)<=2 beta(alpha) is also correct. The all-phase no-eigenvalue conclusion in 1<|lambda E|<exp(beta(2alpha)) is therefore a direct application of the known almost-Mathieu frequency-resonance singular-continuous regime. Two claims needed repair: the package’s finite continued-fraction script replaced the irrational alpha by a rational convergent and then reported a spurious finite beta, and the filed text overstated the conclusion as a full all-phase spectral-type theorem / immediate localization refutation without proving that the window actually meets the mosaic spectrum. The repair keeps the rigorous all-phase no-point-spectrum statement, scopes the singular-continuous conclusion conservatively, and relabels numerics as finite-scale only.

## Originality

**PASS_WITH_CAUTION** — The exact kappa=2 reduction and mobility-edge Lyapunov formula are part of the established mosaic-model literature, while the sharp arithmetic transition for the effective almost-Mathieu operator is also known. The potentially useful contribution is the explicit transfer of that arithmetic no-point-spectrum window to the energy-dependent mosaic coupling. Search absence is not used as a priority proof.

## Value

**PASS** — The corrected statement exposes a genuine arithmetic obstruction to naively promoting the formal mobility-edge condition |lambda E|>1 to localization for Liouville frequencies. This is scientifically useful even though spectral nonemptiness of the proposed window must be checked separately in any concrete application.

## Literature/evidence checked

- [Avila–You–Zhou, Sharp phase transitions for the almost Mathieu operator](https://arxiv.org/abs/1512.03124): Established the sharp frequency-arithmetic transition used after the exact two-step reduction; later literature summarizes 1<|lambda|<e^{beta(alpha)} as purely singular continuous.
- [Liu, Distributions of Resonances of Supercritical Quasi-Periodic Operators](https://doi.org/10.1093/imrn/rnad006): Open-access review of the supercritical AMO literature; explicitly records purely singular continuous spectrum for 1<|lambda|<e^{beta(alpha)}.
- [Wang et al., One-Dimensional Quasiperiodic Mosaic Lattice with Exact Mobility Edges](https://doi.org/10.1103/PhysRevLett.125.196604): Original exact-mobility-edge mosaic model; shows that the reduction/LE mechanism is not itself new.
- [He–Shan–Wang, Cantor Spectrum via a Reducibility-Duality Bridge for the Mosaic Almost Mathieu Operator](https://arxiv.org/abs/2606.23422): Recent mosaic-AMO work establishing a duality/reducibility framework and Cantor spectrum; inspected for originality context.

## Limitations of this audit

Main-branch tree and blob guards were checked before staging and matched the assignment. Literature search is claim-specific and is not a proof of absolute priority. GitHub was read only; no repository writes were made. No inaccessible source is claimed as read.
