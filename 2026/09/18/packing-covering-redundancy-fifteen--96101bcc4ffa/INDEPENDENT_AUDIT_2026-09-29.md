# Independent Audit — 2026/09/18/packing-covering-redundancy-fifteen--96101bcc4ffa

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `28186146f6cc00571d37125dc57c465c4ef9a6f9`
- Disposition: **PASSED**

## Correctness

**PASS** — The finite reduction and exceptional binary argument check. Re-evaluating the submitted dimension-cap/binomial sieve with exact integers gives 62 redundancy-15 tuples: 6 low-dimension exclusions, 55 covering-binomial exclusions, and the single survivor (q,t,r)=(2,3,6) with K=78 at h=6. For that survivor, d3(C)≥15 implies d4(C^perp)≥k+2: otherwise a 4-dimensional dual subcode supported on at most k+1 coordinates leaves at least 14 parity-check columns in an 11-dimensional kernel, producing a 14-coordinate set of nullity at least three. Shortening the dual on nine independent parity-check coordinates gives a binary [N,6] code with N=k+6 and d4≥N-4. Therefore every 2-space of F_2^6 contains at most four generator columns with multiplicity. The 31 two-spaces through a fixed nonzero point partition the other 62 nonzero vectors into pairs; summing their inequalities gives N≤64 whenever any zero/repeated multiplicity occurs, while the simple case gives N≤63. Thus n≤73. Finally V_8(73,6)=20,282,523,983,828 is strictly below 2^45=35,184,372,088,832, contradicting the necessary covering-ball inequality.

## Originality

**PASS** — Essayag-Zabokritskiy's 16 September 2026 preprint proves the generalized packing-covering conjecture universally only through redundancy 14 and identifies a first residual regime beyond that threshold. The audited result closes the redundancy-15 finite reduction, with the binary (15,3,6) case requiring the additional six-dimensional generalized-weight obstruction. Targeted searches found no earlier theorem closing all redundancy 15. The generalized Griesmer philosophy, covering-ball inequality and source reduction are prior ingredients and are not counted as new.

## Scientific value

**PASS** — The theorem advances the universal field-independent redundancy threshold by one at exactly the first range left open by the newest source. The exceptional-case argument is short, exact and reusable: it improves a coarse dimension cap using dual generalized-weight geometry until the covering-ball bound becomes decisive.

## Sources

- Auxiliary Codes and the Generalized Packing-Covering Conjecture (Isaac Barouch Essayag; Aryeh Lev Zabokritskiy): https://arxiv.org/abs/2609.19098 — Primary source proving the universal statement through redundancy 14 and supplying the reduction framework.
- Optimal Codes and Arcs for the Generalized Hamming Weights (Sascha Kurz; Ivan Landjev; Assia Rousseva): https://epub.uni-bayreuth.de/id/eprint/8792/ — Background for generalized-weight/Griesmer geometry; the audited proof includes its needed six-dimensional special case directly.

## Limitations

- The theorem advances the threshold only through redundancy 15 and makes no claim for redundancy 16 or larger.
- Originality is time-sensitive because the source preprint is only two days older than the record; a simultaneous unindexed follow-up remains possible.
- The finite reduction depends on the cited source framework; the exceptional binary case and arithmetic were independently checked.

## Independent exact check

```json
{
  "implementation": "fresh exact-integer reconstruction of the rho=15 parameter sieve and final covering volume",
  "reduced_tuples": 62,
  "low_dimension_exclusions": 6,
  "binomial_exclusions": 55,
  "remaining": [
    [
      2,
      3,
      6,
      78,
      6
    ]
  ],
  "binary_shortened_length_bound": 64,
  "original_length_bound": 73,
  "V8_73_6": 20282523983828,
  "required_2pow45": 35184372088832,
  "strict_contradiction": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked first. No decisive comparison required Oxford Download in this record.
