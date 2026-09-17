# Same-model review

## Verdict

**PASS (same-model review only).** The contribution is assessed separately as correct, original to the best of our knowledge, and scientifically useful. This is not independent validation or peer review.

Same-model review: passed. Cross-model review: not yet performed.

## Correctness audit

The result was checked against the equations in arXiv:2607.18140v1.

1. **Fogging-surface jump.** For 0<k<1, both sides of I=kC use the below-capacity formulas for recovery and mosquito infection. Turning fogging on changes only the mosquito equations, by (-eta U,-eta V). The I-component of the jump is exactly zero.
2. **Normal velocity.** The switching normal is e_I. Therefore the two one-sided normal velocities at I=kC are exactly equal. Opposite-sign normal velocities, required for an ordinary Filippov sliding or escaping region, cannot occur. Common zero normal velocity is a tangency and is explicitly excluded from the transversal saltation statement.
3. **Capacity-surface continuity.** At I=C, the recovery pieces agree because gamma1 C = gamma1 C + gamma2(C-C), and the mosquito-infection pieces agree because beta_m2 U(C-C)=0. For k<1 fogging is already on from both sides. Thus the vector field is continuous at I=C even though its Jacobian generally is not.
4. **Coincident thresholds.** For k=1, the capacity and fogging thresholds coincide. The capacity-dependent terms remain continuous there, while the fogging jump remains tangent to the I-normal, so the no-sliding conclusion persists.
5. **Saltation algebra.** For a transversal identity-reset event, S=I+(Delta F n^T)/(n^T F^-). Since n^T Delta F=0, the rank-one correction squares to zero and the matrix determinant lemma gives det S=1. Hence the saltation is unipotent. At I=C with k<1, Delta F=0 and S=I exactly.
6. **Floquet determinant.** Multiplying smooth-flight state-transition matrices and event saltation matrices, Liouville's formula supplies the smooth determinant factors and every event contributes determinant one. The result concerns the product of Floquet multipliers, not each multiplier individually.
7. **Mosquito-fraction perturbation.** The fogging saltation changes delta U and delta V proportionally to U and V. Direct differentiation of q=V/(U+V) therefore gives no instantaneous jump in delta q.

### Correctness limitations

Degenerate points with zero common normal velocity can support higher-order grazing or tangency phenomena and are not classified as transversal crossings. The theorem excludes ordinary codimension-one Filippov sliding/escaping regions, not every possible higher-order nonsmooth phenomenon. It does not establish existence or stability of periodic orbits or determine Hopf criticality.

## Originality audit

### Existing SCOPE records

Searches of the current SCOPE archive by the source model, dengue/fogging terminology, Filippov sliding, switching manifolds, and saltation terminology located no prior SCOPE record covering this result.

### External literature checked

- **Aldila et al., arXiv:2607.18140v1 (2026).** The full accessible preprint was inspected. It formulates the two switching variables, reports boundary-equilibrium and Hopf bifurcations, and explicitly lists a Filippov-based sliding-mode analysis of I=kC and I=C as future work. No no-sliding theorem, saltation matrix, or Floquet determinant consequence is given.
- **di Bernardo et al., Piecewise-smooth Dynamical Systems (2008).** This is standard background for crossing/sliding geometry and discontinuity-induced bifurcations; it supplies general theory rather than the model-specific conclusion.
- **Kong et al., Proceedings of the IEEE (2024), DOI 10.1109/JPROC.2024.3440211.** This is a modern reference for the standard saltation formalism. The generic saltation formula is not claimed as new here; the contribution is its exact structural specialization to the 2026 dengue model.
- **You et al., Mathematical Methods in the Applied Sciences 47 (2024), DOI 10.1002/mma.10192.** The accessible abstract describes a different piecewise-smooth dengue model with a threshold policy and a genuine sliding mode analyzed by Utkin's method. This does not cover the present model; rather, it confirms that the absence of sliding is not automatic for threshold dengue systems and depends on how the switch changes the normal dynamics.
- Synonymous searches using the 2026 paper title/arXiv identifier together with Filippov, sliding, saltation, switching, and threshold-fogging terms did not locate a follow-up or independent source containing the present model-specific result.

The full text of You et al. (2024) was not inspected; only the publisher abstract and bibliographic material were available. That paper is a residual originality-risk source for generic threshold-dengue techniques, but its publication predates and concerns a different model, so it cannot itself contain the model-specific specialization to arXiv:2607.18140. The generic facts about tangential vector-field jumps and saltation matrices are standard and are not asserted to be original. Originality is claimed only for the application and consequences for the 2026 dengue model, to the best of our knowledge.

## Value audit

The source preprint explicitly identifies Filippov sliding analysis of both switching manifolds as an open analytical direction. The result resolves the ordinary sliding question in a stronger negative form: the model's switch geometry forbids sliding regions on both thresholds. It also distinguishes the two thresholds structurally—tangential vector-field discontinuity at fogging activation versus a continuous vector field with a derivative jump at hospital capacity—and turns this geometry into an exact saltation rule useful for stability calculations of the reported periodic outbreaks. The determinant-one and mosquito-fraction invariance consequences provide reusable simplifications for Floquet analysis.
