# Review of the joint Crofton face-vector theorem

## Correctness

**PASS.** The sample space is invariant affine hyperplane measure conditioned on hitting the cross-polytope; it is not Haar orientation with a fixed central offset. The key normalization is exact because Gaussian radial and directional parts are independent: weighting a standard Gaussian by its largest absolute coordinate produces the required width-biased direction. Integrating a uniform positive offset from zero to that maximum gives a Gaussian integral with normalizing constant the expected maximum. The latent binomial integral follows from independent Gaussian exceedance events.

Every face of the regular cross-polytope is an admissible signed coordinate subset. The complete all-high/all-low enumeration proves the full finite-dimensional vector formula; integration of each original face's projection range yields its exact expected contribution. Gaussian maximum tail estimates give the uniform limit of the rescaled offset, binomial concentration then gives the random logarithmic exceedance count, and the positive mixed-face expansion gives the same random exponent at each fixed rank. These arguments handle all \(n\ge2\) and explicitly separate the fixed-rank asymptotic regime. `checker.py` verifies representative enumerations and numerical integral identities independently; its finite checks are not substituted for the proof.

## Originality

**PASS on presently accessible evidence, with residual bibliographic risk.** Birkemeyer et al. (arXiv:2609.16195, first posted 14 September 2026) study what combinatorial section information determines about a polytope, not an invariant random affine-section law in the accessible abstract. De Loera et al. (arXiv:2412.12419) establish maximum vertex counts, gaps and enumeration; those statements do not give a probability mass function or simultaneous distribution of all face ranks. Brazitikos–Pandis (arXiv:2606.07163, restricted-section volume theorems and section 5) concern extremal volumes under prescribed restrictions. Kabluchko (2020) calculates face expectations for a Poisson hyperplane tessellation's random cell, which is a different random body. The present Gaussian exceedance law and shared rankwise logarithmic exponent are not a relabeling or numerical specialization of those statements.

An earlier, unindexed special case of the exact distribution cannot be excluded. In addition, only the abstract and indexed metadata of the 2026 combinatorial slicing preprint were accessible, and no full-document absence claim is made for that source. The independently checked analytic claims are not contingent on the literature search proving uniqueness.

## Mathematical value

**PASS.** Integral geometry provides a natural invariant sampling model; the new statistic is the entire face vector of a section of a canonical regular polytope. The theorem determines its exact finite-dimensional joint law rather than a single table entry, all expected face numbers, and a strong high-dimensional phenomenon: perfectly correlated random exponents across fixed ranks, deterministic cross-rank ratios, and typical counts negligible compared with means. These conclusions directly illuminate why the expected complexity of such sections is not representative of a typical section. They are neither dimension-specific arithmetic nor a straightforward special case of the earlier extremal slice counts.

## Scope and remaining risks

The geometric model excludes central-only sampling. The logarithmic theorem fixes the face rank before increasing dimension; it does not treat ranks growing with dimension. Numerical quadrature truncation and finite random enumeration cannot independently certify the limiting theorem; the text supplies its Gaussian-tail proof. The inaccessible full preprint constitutes a finite bibliographic priority risk, not a mathematical proof defect.

Self-review: passed. Independent audit: not yet performed.
