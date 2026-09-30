# Independent Audit — 2026/09/21/four-existential-closure-super-geometric-dominance--424c9dd4cac4

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `2b8182a9a9f936dd351f613ed03bf31e32bd09a3`
- Disposition: **PASSED**

## Correctness

**PASS** — The transfer theorem is correct. In a diameter-two graph a third vertex lies on the metric line through u,v exactly when the induced triple has two edges. The 4-e.c. extension property supplies every witness used to separate two distinct lines, two closed neighborhoods, and a line from a closed neighborhood, including the shared-endpoint cases. It also forces diameter two. For the Paley corollary, expanding the four prescribed Legendre-symbol factors gives vanishing one-character sums, six exact two-character sums -1, cubic Weil errors at most 2 sqrt(p) each, a quartic error at most 3 sqrt(p), and root correction at most 32, hence 16N >= p-38-11 sqrt(p). This is positive at p=193 and thereafter. An independent exhaustive reconstruction of P(17) found 68 edges, 136 distinct generated lines with size distribution {6:68,10:68}, all required antichain properties, and no outside common nonneighbor of {0,1,2,3}, exactly as claimed.

## Originality

**PASS** — Chen-Huzhang-Miao-Yang introduced super geometric dominant graphs and explicitly stated that they knew no constructive family avoiding a random process. Paley existential-closure phenomena are classical, but those papers predate the metric-line notion. The checked source scopes do not contain the 4-e.c.-to-super-geometric-dominant transfer, and targeted searches found no direct Paley/super-geometric-dominant theorem. The claim is therefore original at the level asserted, with residual risk because the transfer is short once the two notions are juxtaposed.

## Scientific value

**PASS** — The result gives a deterministic infinite family addressing an explicit constructive gap in the source literature and cleanly connects an established adjacency-extension property to a metric-antichain property. The exact P(17) example additionally shows the sufficient 4-e.c. condition is not necessary. The result does not overclaim threshold sharpness or minimum order.

## Sources

- **Graph metric with no proper inclusion between lines** — X. Chen; G. Huzhang; P. Miao; K. Yang. https://doi.org/10.1016/j.dam.2014.12.022 — Introduces super geometric dominant graphs and states the lack of a known constructive nonrandom family.
- **Paley graphs satisfy all first-order adjacency axioms** — A. Blass; G. Exoo; F. Harary. https://doi.org/10.1002/jgt.3190050414 — Classical Paley adjacency-extension background; predates super geometric dominance.
- **A Prolific Construction of Strongly Regular Graphs with the n-e.c. Property** — P. J. Cameron; D. Stark. https://doi.org/10.37236/1647 — Modern n-existentially-closed terminology and Paley examples.

## Limitations

- The 4-e.c. condition is sufficient, not necessary.
- The prime-order Paley threshold p>=193 is only a convenient sufficient character-sum bound.
- No minimum-order or extremal-edge classification is proved.
- Because the transfer is elementary, an unindexed or near-simultaneous observation remains a residual originality risk.

## Independent checks

```json
{
  "proof_cases_reconstructed": true,
  "paley_character_count_rederived": true,
  "p193_lower_bound": 2.1831161160521617,
  "p17_edges": 68,
  "p17_distinct_lines": 136,
  "p17_line_size_distribution": {
    "6": 68,
    "10": 68
  },
  "p17_not_4ec_certificate_checked": true,
  "source_tree_unchanged": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged from the inventory snapshot through the checked commit. GitHub was used only as read-only evidence. Open-access and preprint sources were checked first, and no decisive comparison required institutional retrieval. No GitHub write or separate dispatcher report was performed.
