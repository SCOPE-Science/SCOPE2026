# Independent mathematical audit — SCOPE-20260920-46d335839ec5

Audited at: 2026-10-01T22:05:12.892464Z

Disposition: **passed**

## Correctness — PASS

The unweighted inclusion from the block \(\ell_p\)-sum to the block \(\ell_q\)-sum is strictly singular by a gliding-hump argument: successive almost-disjoint unit vectors have domain sums of order \(m^{1/p}\) but range sums of order \(m^{1/q}\). If a positive weight level contains blocks of unbounded dimension, those individual blocks give arbitrarily large subspaces on which the operator is bounded below, so finite strict singularity fails. Conversely, uniformly bounded block dimensions admit Auerbach coordinate factorization through the scalar formal inclusion, giving the displayed Bernstein bound and finite strict singularity. Finite block truncations prove compactness exactly when the weights tend to zero.

### Correctness sources

- assigned RESULT.md
- Lang and Nekvinda, Mathematische Nachrichten 298 (2025)
- Edmunds and Lang, arXiv:2503.19600

### Correctness risks

- The exact constant in the Bernstein upper envelope is not claimed optimal.
- The argument assumes every block is finite dimensional and nonzero, exactly as stated.

## Originality — PASS

The closest modern primary source treats scalar variable-exponent sequence embeddings and recalls Milman's scalar formal-inclusion examples. It does not state the arbitrary finite-dimensional Banach-block weight-threshold criterion or the weighted three-regime classification. Published-record semantic searches found no earlier same theorem. Milman's 1970 Russian paper and older operator-ideal monographs remain a specific historical risk because they were not inspected in full.

### Equivalent formulations

No equivalent older formulation was located after translating the claim into superstrict singularity, formal inclusions, block-diagonal maps, and Bernstein-number language.

Searches:
- Published-record semantic search: weighted block identity finitely strictly singular dimension threshold Bernstein numbers finite-dimensional Banach blocks
- Lang-Nekvinda 2025 full-text search for finite strict singularity and Bernstein numbers

Evidence:
- The closest published-record hit is the assigned theorem itself; nearby results concern scalar or different block-diagonal questions.
- Lang-Nekvinda work with scalar sequence coordinates and variable exponents, not arbitrary Banach blocks with thresholded dimensions.

### Broader coverage

Those results supply ingredients, but they do not imply the dimension-threshold classification for arbitrary finite-dimensional Banach blocks because the internal block geometry and unbounded block dimensions are absent from the scalar setting.

Searches:
- Lang-Nekvinda 2025
- Edmunds-Lang 2025 review
- Milman references recorded in those sources

Evidence:
- The modern sources cover scalar formal inclusions and variable-exponent embeddings and identify classical FSS/SS examples.

### Exact database or table

The claim is a structural operator-ideal theorem rather than a tabulated invariant; no exact database entry covers it.

Searches:
- Published-record semantic database query for the exact FSS threshold and Bernstein envelope

Evidence:
- No earlier record gives the criterion \(\sup\{\dim E_n:|\lambda_n|\ge t\}<\infty\) for every positive threshold.

### Claim versus prior implication

The final classification is not a mechanical restatement of the scalar formal inclusion.

Searches:
- Compared the assigned proof against the scalar Bernstein formula and modern variable-exponent criteria

Evidence:
- The scalar formula controls the factorized bounded-dimension high-weight part only; the audited theorem adds the necessity from large individual blocks and the threshold decomposition for arbitrary weights.

### Sources inspected

- **Embeddings between sequence variable Lebesgue spaces, strict and finitely strict singularity** — https://doi.org/10.1002/mana.12031
  - Trigger: Closest modern source on finite strict singularity and Bernstein numbers for sequence embeddings.
  - Material read: Full open HTML, including motivation, definitions, Section 4 strict-singularity criteria, Bernstein-number estimates, and references to Milman.
  - Method: Primary full text.
  - Assessment: NOT_COVERING
  - Evidence: The paper treats scalar variable-exponent sequence spaces; it does not formulate arbitrary Banach blocks or a high-weight block-dimension profile.
- **Notes on Non-Compact Maps and the Importance of Bernstein Numbers** — https://arxiv.org/abs/2503.19600
  - Trigger: Modern review cited by the record and plausible source of a more general block formulation.
  - Material read: Abstract and scope statement.
  - Method: Primary preprint metadata/abstract.
  - Assessment: BACKGROUND
  - Evidence: The review emphasizes Bernstein numbers and noncompact embeddings but no inspected statement covers the assigned block theorem.

### Checked sources

- https://doi.org/10.1002/mana.12031
- https://arxiv.org/abs/2503.19600
- https://doi.org/10.7153/oam-06-22
- published-record semantic search

### Residual risks

- Milman's 1970 Russian paper was not available in full during this run.
- Pietsch's older operator-ideal monographs were not exhaustively inspected for an equivalent block formulation.

## Value — PASS

The theorem gives a natural complete classification of compactness, finite strict singularity, and strict singularity for a broad block-diagonal class and quantitatively interpolates between classical scalar and large-block examples. The block-dimension threshold is a reusable invariant rather than an arbitrary special case.

### Value sources

- Lang-Nekvinda 2025
- Edmunds-Lang 2025 review

### Value risks

- The quantitative Bernstein upper bound is an envelope rather than a claimed sharp formula.

## Limitations

- All blocks are assumed nonzero and finite dimensional.
- The result concerns outer exponents \(p<q\); other exponent arrangements are not covered.
- Historical priority remains qualified because Milman's 1970 paper and older monographs were not fully inspected.
