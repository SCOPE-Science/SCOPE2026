# Independent Audit — 2026/09/18/multinomial-mode-cesaro-universality--a66b1067c370

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `3c32275c58e6de5057fa6334c785305cef93f2bb`
- Disposition: **PASSED**

## Correctness

**PASS** — The transfer argument and coefficient formulas check. Rational linear independence together with sum p_i=1 makes the only integer relation v·p in Z a multiple of the all-ones relation, so Jefferson quotient ties are absent and the mode is unique. Janson's random-house-size Jefferson seat-excess limit, combined with the deterministic boundedness of modal displacements, upgrades weak convergence to Cesàro convergence for every polynomial. Conditioning the submitted joint representation on J gives the displayed product MGF. For one coordinate, multiplying Janson's centered-uniform marginal MGF by the Bernoulli-polynomial generating function cancels one centered-uniform factor and yields E B_m(T_i+1)=p_i^m b_{m,n}; substitution into Elezović's coefficient formula makes every logarithmic coefficient mean independent of p. I also independently reran a 100,000-seat highest-averages enumeration for the submitted irrational three-category example and reproduced the c1, c2 and Q2 predictions.

## Originality

**PASS** — The two main ingredients are prior art: Elezović gives the multinomial mode/local Bernoulli-polynomial expansion and also studies Cesàro averages for his chosen bounded reference, while Janson gives the Jefferson seat-excess limit law. The new content is their on-slice combination at the actual mode under generic arithmetic assumptions, especially the all-order p-independent logarithmic-coefficient law and the explicit Q2 calculation showing where universality first breaks. Older apportionment papers can contain seat-excess moments, but they predate Elezović's complete multinomial local expansion and do not by themselves state this coefficient-transfer theorem. No covering statement was located in the targeted searches, and the claim is appropriately limited to that synthesis rather than to Janson's limit law.

## Scientific value

**PASS** — The theorem converts a fixed-p apportionment limit into explicit asymptotics for the actual multinomial modal mass, identifies a dimension-only hierarchy for logarithmic corrections, and pinpoints the first heterogeneity-sensitive multiplicative term. This gives a reusable averaging principle for any polynomial of modal displacement and clarifies which local asymptotic coefficients are genuinely universal.

## Sources

- Multinomial probabilities near the mode: integer modes and the complete local expansion (Neven Elezović): https://arxiv.org/abs/2609.20229 — Provides the Jefferson characterization of the mode and the complete Bernoulli-polynomial local expansion; its abstract also notes Cesàro averages for oscillating coefficients.
- Asymptotic bias of some election methods (Svante Janson): https://arxiv.org/abs/1110.6369 — Provides random-house-size limiting seat-excess distributions for divisor methods, including Jefferson/D'Hondt.

## Limitations

- The result assumes the generic rational-independence condition and does not cover tied or periodic arithmetic probability vectors.
- Only Cesàro convergence is asserted, not pointwise convergence in N or a quantitative averaging rate.
- The explicit loss-of-universality calculation is carried through Q2; higher multiplicative coefficients are not classified.
- Older apportionment moment literature is extensive, but its existence does not cover the post-2026 linkage to Elezović's complete local coefficient expansion.

## Independent exact check

```json
{
  "implementation": "fresh Jefferson highest-averages enumeration",
  "N_max": 100000,
  "mean_c1": -1.0833333559442817,
  "predicted_c1": -1.0833333333333333,
  "mean_c2": 0.6249989115292276,
  "predicted_c2": 0.625,
  "mean_Q2": 1.2436397577370235,
  "predicted_Q2": 1.2436423559492251,
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first; no needed source remained inaccessible, so Oxford Download was not required.
