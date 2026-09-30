# Independent Audit — 2026/09/19/anisotropic-lorentz-wasserstein-curvature-tomography--262c3143b703

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `1def39814a6249e8170fbe4b4c8d59617ec5a894`
- Disposition: **PASSED**

## Correctness

**PASS** — Braun-Li's Fermi-coordinate estimates contain the unaveraged quadratic term a_ij w^i w^j and are uniform over endpoint pairs in the required scale regime. For the matched anisotropic laws, the identity transverse coupling gives the lower bound and arbitrary causal couplings give the upper bound after dropping the nonpositive transverse-displacement term. Since the curvature term depends only on the first marginal, both bounds integrate to the same contraction tr(A_v M_mu), with uniform remainders for probability laws supported in the unit ball. Atomic rank-one laws are therefore legitimate and recover a(u,u). The n(n+1)/2 tidal-operator reconstruction is ordinary polarization. For the full tensor, vanishing on all orthogonal timelike-spacelike planes implies S(z,v,v,z)=0 for every timelike v and all z; homogeneity plus polynomial continuation from the open timelike cone and standard curvature polarization force S=0. Finite-dimensional separation then permits exactly D_m=m^2(m^2-1)/12 scalar probes, which is also the linear lower bound.

## Originality

**PASS** — Braun-Li average the same Fermi quadratic form over isotropic spacelike balls and report the Ricci trace. Their available full description explicitly shows that the trace appears through the ball second moment. The audited theorem keeps arbitrary matched second moments, permits rank-one atomic laws, and derives finite sectional/tidal/full-curvature tomography. Barton-Borza-Roehrig likewise recover timelike Ricci using symmetric causal-diamond measures. Ketterer-Mondino recover sectional/intermediate Ricci information through a different Riemannian entropy-convexity framework. Targeted searches found no prior Lorentz-Wasserstein matched-law second-moment tomography theorem. The underlying second-variation fact is classical; the originality is the transport observable and finite reconstruction package.

## Scientific value

**PASS** — The result shows that the source observable is not intrinsically Ricci-only: anisotropic probe design can resolve individual timelike sectional curvatures and, with finitely many measurements, the entire algebraic Riemann tensor. That materially changes the interpretation of the new Lorentzian Ollivier framework and supplies an explicit minimal measurement count for local curvature tomography, even though conditioning and noisy-data questions remain open.

## Sources

- Timelike Ollivier-Ricci curvature (Mathias Braun; Xue-Mei Li): https://arxiv.org/abs/2609.18664 — Primary source; proves the isotropic codimension-one Lorentz-Wasserstein Ricci reconstruction and displays the Fermi quadratic form before averaging.
- Ollivier-Ricci curvature for causal sets (J. Barton; S. Borza; J. Roehrig): https://arxiv.org/abs/2606.04910 — Independent Lorentzian/casual-set transport construction recovering timelike Ricci from symmetric measures.
- Sectional and intermediate Ricci curvature lower bounds via optimal transport (Christian Ketterer; Andrea Mondino): https://arxiv.org/abs/1610.03339 — Riemannian optimal-transport characterization of sectional/intermediate Ricci bounds, distinct from the local Lorentz-Wasserstein endpoint observable.

## Limitations

- The expansion inherits epsilon=o(delta^(5/2)) and smooth local hypotheses from Braun-Li's pointwise upper estimate.
- The full-tensor claim is algebraic identifiability, not a statistically stable or optimally conditioned reconstruction theorem.
- No discrete causal-set estimator or finite-sample convergence result is supplied.
- The anisotropic extension is technically close to the source estimates; scientific value comes from the interpretation and finite tomography consequences.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "source_femi_quadratic_and_isotropic_average_checked": true,
  "tensor_separation_argument_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked before considering institutional retrieval.
