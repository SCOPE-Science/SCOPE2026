# Independent Audit — 2026/09/19/energy-obstruction-hopf-langford-torus-bifurcation--7b5b263635c6

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `c8f1b9ffa4fac9a78772db11bb7c4a3568ae9a38`
- Disposition: **PASSED**

## Correctness

**PASS** — The exact reduction and obstruction were independently reconstructed. From rdot=r(mu-alpha+z), zdot=mu z-gamma(r^2+z^2), setting w=r^gamma and eliminating z gives w''-T w'=gamma^2 R^2 w-gamma^2 w^(1+2/gamma), with T=(1+2gamma)mu-2gamma alpha and R^2=(alpha-mu)(mu/gamma-alpha+mu). Multiplying by w' yields E'=T(w')^2 for the stated potential (with the logarithmic gamma=-1 case). Thus every nonstationary recurrent amplitude orbit is impossible for T!=0. The first-order (w,w') system has constant divergence T, so its P-period map determinant is exp(TP); a Neimark-Sacker unit-modulus crossing therefore requires T=0. For gamma>0 and R^2>0, V''(R^gamma)=2gamma R^2>0, so T=0 is a Hamiltonian-center degeneracy with nearby closed amplitude levels rather than a generic one-sided torus birth. The mapping to Vassilev-Nikolov's prior integrability condition is exact. I also reproduced the record's printed Example 2 arithmetic: R^2=2.9812898735e-6, T=-1.9991761605e-3 and 2gamma R^2=-5.9685420883e-6; the two displayed Lyapunov-coefficient formulas evaluate to about -425.545 and +3.282 respectively.

## Originality

**PASS** — Vassilev and Nikolov already identify a first-integrable Hopf-Langford surface in a broader family, and that prior integrability is correctly excluded from the novelty claim. Domingues's September 2026 preprint nevertheless explicitly claims a smooth Neimark-Sacker curve and a unique unstable invariant torus surrounding the periodic solution. The audited record supplies a source-specific contradiction: for the exact four-parameter system, off the integrable surface the amplitude energy is strictly monotone, while on the surface the system has a center foliation. Targeted searches located the prior integrability literature but not this monotone-energy refutation of the 2026 torus theorem or the explicit diagnosis of its numerical Example 2.

## Scientific value

**PASS** — The result corrects a substantive bifurcation claim in a current preprint using an exact invariant/monotonicity structure rather than numerical counterevidence. It identifies the true unit-modulus surface, explains its nongeneric center dynamics, and exposes an example that violates the source theorem's standing sign hypothesis and has a transverse saddle. Such a structural correction is scientifically valuable even though the critical first-integrability condition itself was known.

## Sources

- Torus Bifurcation in the Hopf-Langford type system through Averaging Theory (Gustavo Domingues): https://arxiv.org/abs/2609.18010 — Primary September 2026 source; abstract claims a smooth bifurcation curve with a unique surrounding invariant torus.
- First and Second Integrals of Hopf–Langford-Type Systems (Vassil M. Vassilev; Svetoslav G. Nikolov): https://doi.org/10.3390/axioms14010008 — Open-access prior integrability paper; gives the broader cylindrical/Lienard reduction and parameter conditions for first integrals.
- Completely integrable dynamical systems of Hopf-Langford type (S. G. Nikolov; V. M. Vassilev): https://doi.org/10.1016/j.cnsns.2020.105464 — Earlier Hopf-Langford integrability background.

## Limitations

- The correction applies to the exact rotationally symmetric four-parameter system analyzed in the source; additional symmetry-breaking or nonlinear terms can support genuine invariant tori.
- The transformation w=r^gamma is local to r>0, which is the relevant neighborhood of the nonzero periodic circle.
- The audit establishes incompatibility of the claimed torus branch with the exact flow but does not identify the precise symbolic error in the source's averaging calculation.

## Independent checks

```json
{
  "symbolic_scalar_reduction": "exactly reconstructed",
  "energy_identity": "E'=T(w')^2",
  "example2": {
    "R2": 2.981289873507937e-06,
    "T": -0.001999176160543999,
    "two_gamma_R2": -5.968542088259699e-06,
    "lyapunov_formula_a": -425.5451925476594,
    "lyapunov_formula_b": 3.2820181642595734
  },
  "proof_reconstructed": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. The dated independent-audit pair was verified absent before staging this change set, and `VERIFICATION.md` was read at blob `31a3bb079c3be0cdcbee536377edadb1613bf629`. GitHub was used only as read-only evidence; no repository write was performed. Open-access/preprint sources were checked first. No decisive comparison required Oxford Download in this run.
