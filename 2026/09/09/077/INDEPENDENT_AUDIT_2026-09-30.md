# Independent audit — SCOPE-20260909-077

Audited at: 2026-09-30T23:18:42Z

Disposition: **passed**

## Correctness

**PASS** — Fresh reconstruction of the polar as the Minkowski sum of the cross-polytope and a scaled cube gives the stated positive-orthant formula; exact Fraction arithmetic independently reproduces the primal and polar volume formulas, A prime at zero equal to -15, B prime at zero equal to 25, the slope 10, and all four rational Mahler ratios. The support-pattern vertex count is 3 to the fifth minus 1, namely 242, which is outside the independently recomputed five-dimensional Hanner vertex census. The Banach–Mazur upper sandwich follows directly from the norm inequalities.

Sources/evidence:
- Actual package RESULT.md and artifacts/verify_envelope_correction.py and artifacts/verify_jt.py at the audited source revision.
- Fresh exact-arithmetic reconstruction of the four ratio values and the vertex-count/Hanner recursion.

Residual risks:
- The record proves only one named unconditional ray; it does not establish a uniform neighborhood constant.
## Originality

**PASS** — Kim–Zvavitch prove qualitative stability for unconditional bodies but do not give this explicit ray, its exact volume-product formula, its one-sided derivative 10, or these four rational ratios. published-record semantic search searches for aliases, directional Mahler derivatives, exact ratios and Hanner-transverse rays found the same record and distinct later/nearby published records, not an earlier implication. The audited statement is therefore best-of-knowledge original as an explicit directional calculation, not as a new general Mahler theorem.

### Originality comparison details

**Equivalent formulations.** Equivalent normalization by scaling does not change the volume product, so fallback and target normalizations were treated as the same claim.
- No prior source located with the same norm family and slope-10/rational-ratio statement.

**Broader coverage.** The prior theorem motivates the computation but does not imply the explicit directional formula or exact ratios without the new calculation.
- Kim–Zvavitch Theorem 1 gives a dimensional stability conclusion for near-minimal unconditional bodies but leaves the dimension-dependent constant unspecified and does not evaluate this ray.

**Exact database or table.** The exact values are not a recomputation of a known numerical table.
- No pre-existing exact table with these fractions was located.

**Claim versus prior implication.** The final claim is narrower than the general subject but not a formal corollary of the inspected prior theorem.
- Prior stability/equality results do not determine the first directional derivative or four displayed ratios for this family.

### Source inspections
- **Stability of the reverse Blaschke–Santaló inequality for unconditional convex bodies** — NOT_COVERING. Material read: Full HTML text, especially introduction, Theorem 1 and Section 2 setup. Evidence: The paper gives qualitative dimensional stability toward a Hanner polytope, not this explicit ray or exact directional constants.

Originality residual risks:
- Older convex-geometry literature may use an equivalent gauge under different notation; no such source was found in the direct and alias searches.
## Scientific value

**PASS** — The ray is canonically tied to the cube by adding an l1 term to the l-infinity gauge, and it directly tests a proposed quadratic stability envelope. The exact linear slope and explicit envelope refutation identify a genuine boundary phenomenon rather than an arbitrary sample. This is a motivated structural counterexample/calibration datum despite not proving a global stability theorem.

Sources/evidence:
- The inspected Kim–Zvavitch stability theorem establishes the mathematical motivation of near-Hanner volume-product behavior.
- The exact family calculation directly falsifies the stated quadratic envelope.

Residual risks:
- Its value is directional and diagnostic; it should not be advertised as a uniform Mahler-stability constant.

## Limitations

- Single named unconditional ray only; no uniform neighborhood constant is established.
- No quantitative Banach–Mazur lower bound is claimed.
