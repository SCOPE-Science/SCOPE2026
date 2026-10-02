# Independent scientific audit — SCOPE-20260930-cc926907acdb

Audited at: 2026-10-02T00:16:07.579488Z

Disposition: **passed**

## Correctness — PASS

For \(\mathrm{CB}\le_{\mathrm{sW}}\mathrm{isInfinite}^{*}\), indicator sequences decide exactly which palette colors recur infinitely often. Conversely, a persistent marker color \(3m\) and disjoint residue classes encode a finite tuple of binary sequences so that \(\mathrm{CB}\) recovers \(m\) and every \(\mathrm{isInfinite}\) answer without access to the original input. For \(\mathrm{ECT}\times\mathrm{CB}\le_{\mathrm{sW}}\mathrm{PECT}\), the three-position block code separates a persistent marker, the ECT channel, and the color-basis channel; from a PECT output \((b,S)\), \(B=\lfloor(b+1)/3\rfloor\) is a valid ECT bound and \(S\) decodes the exact basis. The reverse strong reduction is immediate by duplicating the input. Combining this with the cited ordinary Weihrauch decompositions of ECT and minECT yields \(\mathrm{PECT}\equiv_{\mathrm W}\mathrm{minECT}\) and strictness over ECT.

### Correctness sources

- assigned RESULT.md
- assigned verify.py
- Davis–Hirschfeldt–Hirst–Pardo–Pauly–Yokoyama, arXiv:1812.09943
- Davis–Hirst–Keohulian–Miller–Ross, DOI:10.1177/22113568241304637

### Correctness risks

- The small ultimately-periodic verifier is only a replay of representative codes; the strong reductions are justified symbolically for arbitrary represented inputs.

## Originality — PASS

The 2018 primary paper gives the ECT and minECT degree decompositions, while the later color-basis paper studies the exact set of infinitely recurring colors. Exact product/factorization searches located no prior statement that attaching this basis to an arbitrary ECT witness is strongly equivalent to \(\mathrm{ECT}\times\mathrm{CB}\) and ordinarily equivalent to minECT. The color-basis paper's full text was not obtainable through the available lawful routes, so it remains a named residual risk rather than evidence of noncoverage.

### Equivalent formulations

No earlier combined-output equivalence was located.

Searches:
- published-corpus query: palette certified ECT color basis minECT Weihrauch product exact infinitely recurring colors
- literature query: ECT color basis minECT Weihrauch exact infinite colors product

Evidence:
- The exact corpus query returned the assigned theorem and no earlier equivalent combined principle.
- The accessible 2018 full text gives ECT/minECT decompositions; the later paper's accessible abstract/metadata concerns the exact color basis itself.

### Broader coverage

These are the two prior ingredients. The audited result identifies the exact strong product for the simultaneous PECT output and supplies explicit uniform codings between the independent product input and one coloring.

Searches:
- arXiv:1812.09943
- DOI:10.1177/22113568241304637

Evidence:
- The 2018 source proves \(\mathrm{ECT}\equiv_{\mathrm W}\mathrm{TC}_{\mathbb N}^{*}\), \(\mathrm{minECT}\equiv_{\mathrm W}\mathrm{TC}_{\mathbb N}^{*}\times\mathrm{isInfinite}^{*}\), and \(\mathrm{ECT}<_{\mathrm W}\mathrm{minECT}\).
- The later source studies the exact persistent-color basis and its reverse-mathematical/computability strength.

### Exact database or table

This is a reducibility theorem, not a finite numerical database result.

Searches:
- published-corpus exact query on \(\mathrm{PECT}\), \(\mathrm{ECT}\times\mathrm{CB}\), and \(\mathrm{minECT}\)

Evidence:
- No earlier degree table or theorem with the combined palette-certified principle was located.

### Claim versus prior implication

The ordinary degree equality follows after the strong product theorem; the strong theorem itself is not a formal restatement of the cited minECT identity.

Searches:
- full-text comparison with the ECT/minECT decomposition in arXiv:1812.09943; abstract/metadata and lawful-access attempts for DOI:10.1177/22113568241304637

Evidence:
- The known minECT decomposition does not automatically give a strong factorization for an output that must simultaneously return an arbitrary ECT bound and the exact persistent palette from the same coloring.
- The audited marker/residue block construction converts independent ECT and CB instances into one PECT instance and therefore supplies the missing uniform implication.

### Sources inspected

- **Combinatorial principles equivalent to weak induction** — https://arxiv.org/abs/1812.09943. Trigger: Primary source for ECT and minECT Weihrauch degrees. Material read: Full accessible PDF around the ECT equivalence, minECT product theorem, and strict separation. Method: Lawful open full text with page-level inspection. Assessment: COVERING_INGREDIENT. Evidence: It supplies the ECT/minECT degree identities but does not state the palette-certified strong product factorization.
- **Reverse mathematics of a color basis theorem** — https://doi.org/10.1177/22113568241304637. Trigger: Most plausible same-output source because it studies the exact set of colors occurring infinitely often. Material read: Accessible abstract/metadata and public first-page material; direct open-copy retrieval failed, and authorized institutional retrieval returned no verified PDF. Method: Lawful open-access attempts followed by authorized institutional retrieval. Assessment: INACCESSIBLE_PLAUSIBLE_SOURCE. Evidence: The accessible material confirms that the paper studies color bases, but the full theorem text could not be inspected. It is therefore retained as an originality risk rather than treated as noncovering evidence.

### Checked sources

- https://arxiv.org/abs/1812.09943
- https://doi.org/10.1177/22113568241304637
- published-result corpus search

### Residual risks

- The complete color-basis paper was inaccessible through the available lawful routes; it could contain a combined formulation not visible in the accessible material.
- No inaccessible-source uncertainty overrides a known covering theorem here; no such decisive coverage was found.

## Value — PASS

The theorem isolates exactly the computational content contributed by the persistent palette and explains why it raises an arbitrary ECT witness to the minECT degree. The strong product factorization is a natural information decomposition in Weihrauch analysis, not a merely cosmetic repackaging.

### Value sources

- arXiv:1812.09943
- DOI:10.1177/22113568241304637

### Value risks

- The identification with minECT is ordinary Weihrauch equivalence; no strong equivalence with minECT is claimed.

## Limitations

- The strong equivalence is \(\mathrm{PECT}\equiv_{\mathrm{sW}}\mathrm{ECT}\times\mathrm{CB}\); the minECT identification is only ordinary Weihrauch equivalence.
- Inputs are finite colorings of \(\mathbb N\) with the standard finite-palette representation.
- The full color-basis paper remained inaccessible and is an explicit originality risk.
