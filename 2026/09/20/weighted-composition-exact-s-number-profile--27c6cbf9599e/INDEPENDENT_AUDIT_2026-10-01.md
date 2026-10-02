# Independent mathematical audit — SCOPE-20260920-27c6cbf9599e

Audited at: 2026-10-01T22:05:12.892464Z

Disposition: **passed**

## Correctness — PASS

For a threshold above the \(n\)-th fiber-maximal weight, the high-weight image is finite; separating those image points and cutting off around their fibers produces a rank-below-\(n\) operator with arbitrarily small excess error. Conversely, \(n\) distinct high-weight image points support disjoint peak functions forming an isometric \(\ell_\infty^n\), which gives matching lower bounds for approximation, Bernstein, Gelfand, and Kolmogorov numbers. Below the limiting threshold, an infinite threshold image yields pairwise disjoint peak functions spanning an isometric \(c_0\) on which the operator is bounded below. That witness forces the exact distances to compact, weakly compact, finitely strictly singular, and strictly singular classes.

### Correctness sources

- assigned RESULT.md
- Albanese and Mele, Mathematische Nachrichten 296 (2023)
- Takagi-Miura-Takahasi 2003 bibliographic/statement-level material

### Correctness risks

- The countably disjoint peak-function step uses standard compact-Hausdorff separation; no metrizability is assumed or needed.

## Originality — PASS

The classical finite-threshold-image criterion for compactness and weak compactness is confirmed in a modern full-text source, and the 2003 literature is known to determine the essential norm. Those prior results are explicitly excluded from the novelty claim. Searches did not locate the simultaneous exact finite-index approximation/Bernstein/Gelfand/Kolmogorov profile, the exact FSS/SS/weakly-compact distances, or the quantitative isometric \(c_0\) witness.

### Equivalent formulations

No equivalent finite-index profile was located under weighted-composition, disjointness-preserving, or strict-s-number terminology.

Searches:
- Published-record semantic search: weighted composition C(K) exact approximation Bernstein Gelfand Kolmogorov threshold image strict singularity
- Web literature search for approximation numbers and s-numbers of weighted composition operators on C(K)

Evidence:
- The exact same theorem was not found; the closest published records concern other operator classes.
- General s-number literature gives definitions and inequalities, not this fiber-counting identity.

### Broader coverage

These broader qualitative/limit results do not determine every finite-index s-number or the exact distances to FSS and SS.

Searches:
- Albanese-Mele 2023 full text
- Takagi-Miura-Takahasi 2003 essential-norm literature
- Singh-Summers compactness criterion as quoted in Albanese-Mele

Evidence:
- Compactness and weak compactness are characterized by finiteness of threshold images.
- The essential norm is classical and uses the same limiting threshold.

### Exact database or table

There is no known database table whose entries mechanically give the theorem; the proof uses finite-fiber interpolation and peak-function witnesses.

Searches:
- Published-record semantic query for all four s-number sequences

Evidence:
- No prior exact table/profile for the four classical s-numbers of these C(K) weighted composition maps was found.

### Claim versus prior implication

The claimed finite-index equalities and singular-ideal distances are not corollaries of the inspected classical results without the new quantitative construction.

Searches:
- Compared the finite-index theorem with the classical compactness and essential-norm threshold results

Evidence:
- A limiting essential-norm formula does not determine finite approximation, Bernstein, Gelfand, or Kolmogorov numbers.
- Compactness/weak compactness equivalence alone does not imply an isometric \(c_0\) lower witness at every subthreshold level.

### Sources inspected

- **On composition operators between weighted (LF)- and (PLB)-spaces of continuous functions** — https://doi.org/10.1002/mana.202200171
  - Trigger: Modern full-text source restating the classical weighted-composition compactness/weak-compactness criterion.
  - Material read: Full open HTML, including the weighted C(K)-space setup and the Singh-Summers finite-threshold-image lemma.
  - Method: Primary full text.
  - Assessment: PRIOR_QUALITATIVE_COVERAGE
  - Evidence: It confirms that compactness and weak compactness are classical threshold-image results but contains no all-index s-number formula.
- **Essential norms and stability constants of weighted composition operators on C(X)** — https://doi.org/10.4134/BKMS.2003.40.4.583
  - Trigger: Most plausible source for the limiting threshold/essential norm.
  - Material read: Bibliographic and later-source descriptions; a verified complete primary text was not obtained in this run.
  - Method: Bibliographic/secondary inspection.
  - Assessment: INACCESSIBLE_PLAUSIBLE_SOURCE
  - Evidence: It is treated as prior for the essential norm, but no evidence inspected suggests the stronger finite-index four-s-number theorem.

### Checked sources

- https://doi.org/10.1002/mana.202200171
- https://doi.org/10.4134/BKMS.2003.40.4.583
- https://doi.org/10.1002/mana.200610786
- published-record semantic search

### Residual risks

- The full 2003 Takagi-Miura-Takahasi paper and older Singh-Manhas/Singh-Singh sources were not exhaustively inspected.
- Older Banach-lattice disjointness-preserver literature could contain an equivalent finite-index formulation under different terminology.

## Value — PASS

A single natural fiber-counting invariant exactly determines four standard finite-index s-number sequences and four limiting operator-ideal distances, with a concrete \(c_0\) obstruction explaining every noncompact case. This is a reusable operator-theoretic profile rather than a routine endpoint restatement.

### Value sources

- Albanese-Mele 2023
- general s-number literature

### Value risks

- Part of the limiting compactness/essential-norm statement is classical and is not counted as new value.

## Limitations

- Scalar C(K)-spaces only; vector-valued fibers can behave differently.
- Compactness, weak compactness, and the essential-norm threshold are prior art.
- Some older survey/monograph literature was not fully inspected.
