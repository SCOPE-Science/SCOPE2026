# Independent Audit — Stability-targeted physical nonpairwise design for three Stuart–Landau oscillators

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `e2b184a6a2dc176f78b1f9ccf5def487f73eb625`  
**Audited current source tree:** `e2b184a6a2dc176f78b1f9ccf5def487f73eb625`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence; this file is a guarded publication-plan payload and is not claimed to be already present in the repository.

## Correctness — PASSED

PASS. Differentiating the submitted second-order phase vector field at synchrony and at the splay state reproduces the stated transverse eigenvalues. With eta=kappa*epsilon^2/a, expansion about rho=pi/2 yields the two boundary shifts (3/2-2kappa)epsilon/a and (4kappa-3/4)epsilon/a, hence leading overlap 9/4-6kappa and the balanced value kappa=3/8. Eliminating eta between the two exact marginality equations gives 4a x-2epsilon x^2+3epsilon=0, equivalent to the submitted weak root x*=(a-sqrt(a^2+3epsilon^2/2))/epsilon, and back-substitution gives eta*. The algebra is internally exact for the truncated phase model.

## Originality — PASSED

PASS, narrowly scoped. Muolo–Nakao–Bick derive the same mixed-order Stuart–Landau phase model and choose eta=epsilon^2/(4a) to cancel the asymmetric emergent harmonic and half of the symmetric one. Their open full text then assesses the two stability boundaries numerically and says the engineered interaction shifts both toward the first-order transition; it does not derive the submitted analytic synchrony/splay stability curves, the 3/8 stability-balanced coefficient, or the exact simultaneous-marginality point. The new claim is therefore a model-specific stability-targeted design calculation, not a new phase-reduction method.

## Scientific value — PASSED

PASS. The result turns the source's harmonic-cancellation design into an explicit alternative optimization criterion: minimize the leading bistable-window width rather than cancel one Fourier motif. The 3/8 coefficient and exact marginality point give a concrete, testable design rule and clarify why the source's 1/4 choice only partially aligns the stability boundaries. Value is limited to the second-order truncated model and does not extend automatically to the full nonlinear oscillator system.

## Independent checks

- Read the lawful open arXiv full text of Muolo–Nakao–Bick around Eqs. 16–22 and the phase-diagram discussion.
- Verified the source explicitly chooses eta=epsilon^2/(4a), explains that exact cancellation of both EN harmonics is impossible with one strength, and reports boundary shifts numerically rather than the submitted closed stability formulas.
- Independently eliminated eta from the submitted sync/splay marginality equations; the result factors as 9 epsilon(4ax-2epsilon x^2+3epsilon)/(8a).
- Checked the weak-coupling expansions of x*, rho*, eta*, and the 3/8 coefficient.
- Inspected the repository symbolic verification artifact as corroboration rather than as the proof.
- Verified the assigned record path is unchanged from the dispatcher source-check commit to current main and that both dated independent-audit marker files are absent.

## Limitations

- The stability statements concern the second-order/mixed-order phase truncation, not a proof of nonlinear stability boundaries for the unreduced Stuart–Landau system.
- The balanced coefficient is derived for three identical oscillators with straight isochrones, no self-coupling, and unweighted all-to-all coupling.
- The source preprint is extremely recent, so simultaneous unindexed follow-up work remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.20632
- https://arxiv.org/html/2609.20632v1
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/stability-targeted-nonpairwise-stuart-landau-design--209d4d8aa9d9

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
