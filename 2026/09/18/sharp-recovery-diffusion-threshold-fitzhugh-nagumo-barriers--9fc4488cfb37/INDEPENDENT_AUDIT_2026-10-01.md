# Independent audit — 2026-10-01

## Final claim

For a fixed positive activator profile in the stated heterogeneous FitzHugh-Nagumo barrier setting, a constant-proportional recovery profile exists exactly under the displayed \(c_*\) and positive-curvature budget conditions; for constant recovery diffusion this gives the exact profile threshold \(D_\sharp(V)=(\gamma-1/c_*)/\kappa_V\), with the stated source-tail saturation and conservatism example.

## Correctness — PASS

For the proportional ansatz \(W=cV\), the activator inequalities reduce exactly to \(c\le c_*\), while the recovery inequalities reduce on positive-curvature points to \(\kappa_\delta\le\gamma-1/c\). Since the right side is increasing in \(c\), existence is equivalent to the displayed two conditions and the optimal choice is \(c=c_*\). The exponential-tail saturation and constant-diffusion formula follow directly. The committed verifier and a fresh replay confirm the explicit threshold example and failure above it.

## Originality — PASS

Best-of-knowledge originality passes for the exact fixed-profile proportional criterion, saturation formula and unbounded-conservatism example. The source theorem gives a global sufficient small-diffusion condition; no checked source states the necessary-and-sufficient profile curvature budget.

### Equivalent formulations

Searches: Resultary: FitzHugh Nagumo proportional barrier recovery diffusion curvature threshold heterogeneous; arXiv:2609.14944; Kajiwara 2018 sub-supersolution FitzHugh-Nagumo

Evidence: Resultary returned the assigned exact criterion as the only exact-topic finding. Accessible source material describes propagation failure via coupled barriers and small recovery diffusion, not the optimized fixed-profile curvature threshold.

Reasoning: The proportional criterion is an optimization of the barrier inequalities, but the exact threshold and its saturation are stronger than a one-sided smallness condition.

### Broader coverage

Searches: heterogeneous FitzHugh-Nagumo sub/supersolution methods; stationary pulse literature

Evidence: Older work supplies general comparison/subsolution frameworks rather than the exact \([V'']_+/V\) budget for this source profile.

Reasoning: General existence machinery does not mechanically provide the stated profile-wise optimum without the additional reduction.

### Exact database or table

Searches: Resultary exact threshold search; targeted source-title search with curvature and proportional recovery

Evidence: No prior exact table/formula matching \(D_\sharp(V)\) was located.

Reasoning: Search absence is only best-of-knowledge evidence.

### Claim versus prior implication

Searches: Source sufficient bound versus optimized proportional inequalities

Evidence: The source theorem's accessible description is sufficient-only, whereas the audited argument proves necessity and sufficiency within a specified ansatz and exhibits unbounded conservatism of the uniform estimate.

Reasoning: A sufficient global bound does not imply the exact profile threshold.

### Source inspections

- **Propagation failure in heterogeneous FitzHugh-Nagumo systems via coupled upper and lower solutions** (https://arxiv.org/abs/2609.14944): Supports the small-diffusion persistence context but leaves residual overlap risk for detailed barrier algebra. Material read: Abstract and bibliographic metadata; full text retrieval failed after repeated access attempts. Method: Primary-source abstract inspection plus authorized-access attempt. Evidence: The accessible description gives propagation-failure barriers and small recovery diffusion rather than an exact profile threshold.
- **The sub-supersolution method for the FitzHugh-Nagumo type reaction-diffusion system with heterogeneity** (https://doi.org/10.3934/dcds.2018101): General adjacent method; no accessible exact proportional-curvature criterion. Material read: Accessible abstract and bibliographic material. Method: Primary-source abstract inspection. Evidence: The paper develops a sub-supersolution method and related stationary analysis.

Checked sources: Courdurier and Paduro, Propagation failure in heterogeneous FitzHugh-Nagumo systems via coupled upper and lower solutions, arXiv:2609.14944v1; Kajiwara, The sub-supersolution method for the FitzHugh-Nagumo type reaction-diffusion system with heterogeneity, DCDS 38 (2018); Assigned threshold verifier and fresh algebraic replay; Resultary semantic search for proportional recovery-diffusion thresholds

Residual risks: The 2026 source full text was not retrievable in this run; the audit relies on the explicitly quoted stationary-barrier inequalities plus accessible source metadata for the surrounding theorem. Kajiwara's older paper is adjacent; only its accessible abstract/metadata was inspected, so a more general theorem implying the exact proportional criterion remains a residual risk.

## Scientific value — PASS

Within a natural barrier ansatz, the result replaces a qualitative sufficiently-small hypothesis by an exact computable boundary, identifies positive normalized curvature as the bottleneck, and quantifies that the previous uniform sufficient estimate can be arbitrarily conservative. This is a motivated boundary result rather than an arbitrary parameter slice.

## Limitations

- Exact only for a fixed positive activator profile and constant-proportional recovery components; it is not a global propagation threshold and does not exclude nonproportional barriers.

## Conclusion

The final claim passes correctness, originality and scientific-value review.
