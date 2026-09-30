# Independent Audit — 2026-09-29

**Record:** `2026/09/18/uniform-annular-density-no-four-on-a-circle--51e70afe33cd`  
**Title:** Uniform thick-annulus density for extensible no-four-on-a-circle sets  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `2697998987f5a2bb8955e3741985e23d4056687d`  
**Disposition:** **PASSED**

## Independent checks

- Recomputed the exact max-norm shell size 2r−1 and the resulting annulus expectation.
- Checked the uniform Chernoff/Borel–Cantelli argument over all admissible integer pairs (n,m).
- Checked the dyadic enclosure inequality 2^T<2(n+m)≤4n≤4m/η.
- Checked constants in the deletion estimate and the choice α^3≤η/(192C).

## Three-axis assessment

- **Correctness — PASS**: The annulus A_{n,m} contains exactly 2r−1 lattice points at max norm r, so the weighted sample has mean at least αm. Chernoff gives failure probability at most exp(−αm/8), and the double sum over all ηn≤m≤n is finite, hence Borel–Cantelli supplies eventual simultaneous occupancy for every admissible thick annulus. The source preprint’s dyadic good event holds simultaneously for all sufficiently large T with positive probability. Every deleted annular point can be injectively charged to a witnessing bad quadruple inside the enclosing dyadic box, giving D_{n,m}≤6Cα^4 2^T<24Cα^4m/η≤αm/8 when α^3≤η/(192C). Thus at least 3αm/8 points survive.
- **Originality — PASS**: The motivating Ghosal–Goenka preprint states only the prefix-density conclusion |S∩[n]^2|=Ω(n). Its dyadic shells are used to bound bad quadruples, not to assert simultaneous lower density in every constant-relative-thickness annulus. The earlier finite-box paper does not provide an extensible annular theorem. Targeted searches found no equivalent annular/local-in-scale strengthening.
- **Scientific Value — PASS**: The theorem upgrades a global prefix lower bound to uniform mesoscopic radial regularity at every sufficiently large scale. It also isolates a reusable concentration-plus-cumulative-deletion principle: shell occupancy is linear in thickness while deletions up to radius R are O(α^4R), so every Ω(R)-thick shell retains linear mass. This is a meaningful strengthening of the extensible construction.

## Findings

- The assigned tree exactly matches the current tree at the checked commit.
- The source PDF was inspected at the proof of Lemma 2.2: the collinear, symmetric, and asymmetric bad-quadruple estimates are combined into an event holding for every sufficiently large dyadic scale with positive probability.
- Independent summation confirms Σ_n Σ_{ηn≤m≤n} exp(−αm/8)<∞.
- The deletion charge is injective because the fixed tie-breaking deletion rule assigns each bad quadruple only one maximal-norm point; choosing one witness per deleted point therefore cannot reuse a quadruple for two deleted points.
- The source’s stated theorem remains a prefix Ω(n) result, so the annular conclusion is not a restatement of its final theorem.

## Sources compared

- Ghosal and Goenka, The extensible no-four-on-a-circle problem: https://arxiv.org/abs/2609.20447 — Primary 2026 source. It proves an extensible set with prefix density Ω(n) and supplies the weighted sampling and simultaneous dyadic bad-quadruple bounds used by the audited strengthening.
- Ghosal, Goenka, and Keevash, On Subsets of Lattice Cubes Avoiding Affine and Spherical Degeneracies: https://doi.org/10.1007/s00454-026-00853-7 — Finite-box precursor; it does not supply the all-large-scale annular extensible conclusion.

## Limitations

- The annuli are origin-centred square annuli in the inherited ℓ∞ geometry; no translation-uniform lower density is proved.
- The construction is for each fixed η>0, and both the set and c_η may depend on η; arbitrarily thin relative annuli are not controlled by one uniform statement.
- Constants are not optimized and inherit the implicit universal constant in the source bad-quadruple estimates.
- The motivating preprint is very recent, so contemporaneous unindexed work remains a residual originality risk.

This audit is independent of the repository’s pre-existing same-model review. No GitHub writes were performed during the audit.
