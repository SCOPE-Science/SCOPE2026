# Independent Audit — 2026/09/19/spectral-radius-parity-obstruction-ordered-product-growth--89c304423416

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `b8c4feff79d2330d7a1a44c6a2f1d5fc30fc303c`
- Disposition: **PASSED**

## Correctness

**PASS** — The explicit counterexample is exact. Differentiating the displayed polynomial map at the two orbit points gives A=s[[0,-1],[1,0]] and B=[[0,e^(2a)/s],[-e^(2b)/s,0]], so BA=diag(e^(2a),e^(2b)) and the per-iterate Lyapunov exponents are a>b. Even blocks have spectral radius e^(2ak). Each odd phase product is off-diagonal and has spectral radius respectively s e^(k(a+b)) and e^((k+1)(a+b))/s; phase-averaging cancels log s and gives h_(2k+1)=(a+b)/2. For a=0.2,b=-0.8,s=0.8, an independent numerical multiplication gives rho(A)=0.8, rho(B)=0.6860145451, h_L=-0.3 for odd L, h_L=0.2 for even L, and the singular-value analogue g_L=0.2 for every L tested. The general periodic checkpoint identity h_(mp)=lambda_1 follows from conjugacy of invertible phase monodromies. The standard subadditive/norm formulation, unlike spectral radius, has the claimed Lyapunov limit.

## Originality

**PASS** — General cocycle theory already distinguishes norm growth from spectral-radius growth: Martinez Ramos summarizes that a limsup formula is available broadly while full spectral-radius convergence can fail, and proves convergence only under extra hypotheses. The audited record does not claim that general distinction as new. Its contribution is source-specific: an elementary smooth period-two map in the same non-normal dynamical setting with an exact parity law, permanent sign reversal despite positive lambda_1, failure of the finite-product eigenvector argument, and the observation that period-multiple checkpoints can exactly mask the defect. Targeted searches did not locate this explicit correction to the September 2026 h_L proposal.

## Scientific value

**PASS** — The counterexample directly corrects an unconditional convergence interpretation attached to a newly introduced diagnostic and supplies the standard singular-value replacement with the right Lyapunov behavior. The exact parity mechanism is transparent enough to serve as a regression test for future uses of h_L, and the period-multiple identity explains why a numerical checkpoint can appear validating even when unrestricted-horizon convergence is false.

## Sources

- **A New Route to Chaos through the Geometric Composition of Non-Normal Amplification** — D. Sornette; V. R. Saiprasad; V. Troude. https://arxiv.org/abs/2609.18017 — Primary 2026 source introducing the ordered-product spectral-radius statistic h_L in the non-normal chaos setting.
- **Asymptotic behavior of the spectral radius of locally constant strongly irreducible cocycles** — Nicolas Martinez Ramos. https://arxiv.org/abs/2507.19624 — Prior cocycle theory establishing spectral-radius convergence only under additional structural hypotheses and discussing failure of the unrestricted full limit.
- **Law of large numbers for the spectral radius of random matrix products** — Richard Aoun; Çağrı Sert. https://arxiv.org/abs/1908.07469 — Prior random-product spectral-radius convergence theory under hypotheses; background for why spectral radius is subtler than norm growth.

## Limitations

- The counterexample refutes an unconditional spectral-radius convergence claim but does not analyze every trajectory or finite-L empirical use in the motivating systems.
- The general failure of spectral-radius limits is prior cocycle theory; novelty is restricted to the explicit smooth-map parity obstruction and source-specific correction.
- The exact period-multiple identity assumes invertible tangent maps along the periodic orbit.
- The singular-value replacement is standard subadditive-ergodic theory, not a new Lyapunov theorem.

## Independent checks

```json
{
  "jacobians_rederived": true,
  "two_step_monodromy_checked": true,
  "odd_even_spectral_radius_law_checked": true,
  "representative_parameters": {
    "a": 0.2,
    "b": -0.8,
    "s": 0.8
  },
  "representative_h_odd": -0.3,
  "representative_h_even": 0.2,
  "representative_g_all": 0.2,
  "periodic_checkpoint_identity_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence; no repository mutation or separate dispatcher report was performed. Preprints and lawful open-access sources were checked first. No decisive originality comparison remained inaccessible, so Oxford Download was not required.
