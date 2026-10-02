# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-7d1eeacc3f5d`

## Correctness — PASS

The infinite construction is not inferred from the finite verification. Each listed operation is a boundary-ear insertion and therefore preserves maximal outerplanarity while changing exactly the two endpoint degrees and adding one degree-two vertex. Starting from the published \(18k+2\) ladder counts, substituting each fixed residue template yields the displayed degree-count deltas and hence the exact largest three-consecutive-degree window \(8k+b_r\) for every \(k\ge1\); the symbolic dependence on \(k\) is affine and the unused high-degree windows remain smaller. Explicit triangulations cover orders 14–19. For orders 5–13 the verifier's recursive decomposition by the triangle incident to one boundary edge is exhaustive, reproduces the Catalan counts, and gives exact minima. The verifier was read completely and confirms all finite support claims.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_mop_spread.py and verification.txt
- Caro–Škrekovski–Zarb arXiv:2609.19762
- Caro–Lauri–Zarb 2019 precursor

### Correctness risks

- The small-order part is computer-assisted but exhaustive.
- The proof is specific to spread width two.

## Originality — PASS

The primary 2026 paper proves the matching lower bound, equality in one residue class, and a bounded additive upper gap. Its publicly indexed text says the other seventeen caps were computer-checked over a finite range and describes the all-order formula as a presumption, rather than a theorem. The audited record supplies a uniform ear-template proof for every residue and the complete small-order table. Fresh Resultary searches found no later or stronger theorem covering that full classification.

### equivalent_formulations

Searches:
- Resultary search for maximal outerplanar degree spread two and the \(\lceil(4n+10)/9\rceil\) formula
- primary-paper search for the seventeen caps and all-order statement

Evidence:
- The exact current record was the only Resultary theorem-level match.
- The source describes finite cap verification and the all-order equality as presumed.

Reasoning:
Finite cap data do not imply a uniform proof for all \(k\), and the audited ear words are checked symbolically.

### broader_coverage

Searches:
- Caro–Škrekovski–Zarb 2026
- Caro–Lauri–Zarb 2019

Evidence:
- The former gives the sharp lower bound and additive-43 upper bound; the latter gives an older weaker-scale construction.

Reasoning:
Neither broader source proves the exact all-order classification.

### exact_database_or_table

Searches:
- source finite cap computations and the assigned exhaustive small-order table

Evidence:
- The source's finite verification is not an exhaustive database for all orders; the audited small-order enumeration is exhaustive only for 5 through 13.

Reasoning:
The infinite theorem is not a table lookup.

### claim_vs_prior_implication

Searches:
- claim-versus-source implication comparison

Evidence:
- The source's conjectural/presumed formula plus finite checks does not imply the uniform ear-template theorem.

Reasoning:
A saved finite success range cannot certify all parameters; the explicit residue templates provide the missing proof.

### source_inspections

- **Spreads of degrees in graphs** — https://arxiv.org/abs/2609.19762. Trigger: Primary source of the lower bound and periodic ladder. Material read: Publicly indexed primary abstract and source text describing the residue-cap computations, the finite checked range, the presumption for all orders, and the general additive bound. Method: Primary statement/scope comparison. Assessment: NOT COVERING the audited uniform proof. Evidence: The source proves one residue family and a constant additive gap, while only presuming the universal exact formula.
- **Assigned maximal-outerplanar verifier** — artifacts/verify_mop_spread.py. Trigger: Small-order exhaustive enumeration and construction checks. Material read: Complete source and saved output. Method: Line-by-line inspection of recursion, chord witnesses, ladder builder and ear updates. Assessment: Correct supporting computation; it does not substitute for the symbolic all-\(k\) proof. Evidence: It reproduces Catalan triangulation counts through order 13 and checks all 18 residue templates for \(1\le k\le50\).

### checked_sources

- https://arxiv.org/abs/2609.19762
- https://arxiv.org/abs/1806.08303
- assigned RESULT.md and verifier
- fresh Resultary search

### residual_risks

- The source's supplementary material was not separately obtained; its public description indicates finite cap data, but an unadvertised uniform proof there would be a residual originality risk.

## Scientific value — PASS

The theorem closes a stated constant-gap extremal problem, produces optimal constructions in every residue class, and determines the exact invariant at every order. The six small exceptions and the uniform ear mechanism are natural classification data with clear future reuse.

### Value sources

- sharp source lower bound
- periodic extremal ladder
- audited residue templates and exhaustive small orders

### Value risks

- No analogous claim for other spread widths is made.

## Limitations

- The source supplement was not separately inspected and remains the principal originality risk.
- Orders 5–13 use exhaustive computer-assisted enumeration.
- The theorem concerns maximal outerplanar graphs and spread width two only.

## Disposition

**PASSED**
