# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-eb153aa9e688`

## Correctness — PASS

The rank-one shell computation is exact for every prime power. Writing \(N=q^n\), a rank-\(s\) matrix character has shell coefficient \((q^{2n-s}-2N+1)/(N-1)^2\). These real coefficients strictly decrease with \(s\); therefore the maximum absolute nontrivial coefficient occurs at an endpoint. For \(n\ge3\), the rank-one endpoint dominates \(1/(N-1)\), including the binary square case. Fourier diagonalization of the additive channel gives the claimed maximal correlation. The lower bound is exactly Theorem 5 of Cohen--D'Oliveira--Sprintson at rank one, so the shell attains the universal converse. Independent product channels preserve the largest nontrivial singular value, and the product upload is a deterministic function of the two uploads. The assigned finite verifier correctly corroborates prime-field shells and the symbolic endpoint algebra but is not used as the infinite proof.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_rank_one_masking.py
- Cohen--D'Oliveira--Sprintson, arXiv:2609.18876, Theorems 4 and 5
- earlier exact-minimax shell theorem for nonbinary/nonsquare cases

### Correctness risks

- The theorem is specific to rank budget one and \(n\ge3\).
- Uniform inputs and input-independent rank-constrained masks are essential.

## Originality — PASS

A 2026-09-18 published theorem already proves exact-rank-shell minimaxity for all nonbinary fields and binary nonsquare rectangles, so those portions of the present statement are prior-covered. Crucially, that theorem explicitly excludes binary square spaces and notes a genuine spectral exception at higher rank. The present direct rank-one spectrum closes the binary square case at the first nontrivial rank budget. Fresh semantic searches found no earlier theorem covering that surviving \(q=2\), square, rank-one region. Thus the final all-prime-power theorem is not implied by the broader-looking predecessor even though most of its parameter range is covered.

### equivalent_formulations

Searches:
- Resultary semantic search for exact rank-one masking maximal correlation and binary-square rank-one shell
- statement comparison with 2026/09/18 exact-minimax nonbinary low-rank masking

Evidence:
- The earlier theorem covers \(q\ge3\) and binary nonsquare rectangles, but explicitly leaves binary square minimaxity undetermined.
- The audited direct formula proves binary square rank-one minimaxity for every \(n\ge3\).

Reasoning:
The equivalent formulation is exact minimaxity of the uniform rank-one relation in the bilinear-forms scheme; the only surviving new parameter region is the binary square relation at rank one.

### broader_coverage

Searches:
- 2026/09/18/SCOPE-exact-minimax-nonbinary-low-rank-masking--518b6bf1d437
- Cohen--D'Oliveira--Sprintson arXiv:2609.18876

Evidence:
- The earlier SCOPE theorem is stronger in rank and rectangularity where its spectral monotonicity hypotheses apply, but deliberately excludes \(q=2,d=e\).
- The primary masking paper supplies only the universal lower bound and \(q^{-r}\) achievability for its two samplers.

Reasoning:
Neither broader source dominates the binary-square rank-one statement.

### exact_database_or_table

Searches:
- Delsarte bilinear-forms association scheme spectrum
- current published SCOPE masking records

Evidence:
- Classical rank-relation eigenvalues are prior mathematical ingredients, not a database entry stating the privacy minimax theorem.
- No exact published table/result found that identifies the binary square rank-one shell as the minimax masking distribution.

Reasoning:
The raw spectrum can be tabulated, but converting it to the universal privacy optimum requires matching the masking converse; the new binary-square match is not a mere table lookup.

### claim_vs_prior_implication

Searches:
- implication comparison with exact-minimax theorem and Cohen--D'Oliveira--Sprintson converse

Evidence:
- The source converse gives the same lower-bound number but no attaining distribution.
- The earlier shell theorem supplies attainment only outside binary square spaces.

Reasoning:
Together they do not imply binary-square rank-one attainment; the audited direct Fourier calculation supplies that missing implication.

### source_inspections

- **Low-Rank Masking for Single-Server Matrix Multiplication** — https://arxiv.org/abs/2609.18876. Trigger: Primary source of the universal converse and existing samplers. Material read: Complete five-page primary paper obtained through authorized access after open routes failed. Method: Full theorem and proof-scope comparison. Assessment: Theorem 5 gives the exact rank-one lower bound; no exact-rank-shell attainment theorem is stated. Evidence: Theorems 4 and 5 leave a finite-length factor-two gap for the paper's samplers.
- **Exact minimax maximal correlation for low-rank matrix masking** — 2026/09/18/exact-minimax-nonbinary-low-rank-masking--518b6bf1d437. Trigger: Closest broader published SCOPE theorem. Material read: Complete RESULT.md at the audited repository snapshot. Method: Full statement and parameter-range comparison. Assessment: Covers nonbinary and binary nonsquare exact-rank shells, but explicitly excludes binary square spaces. Evidence: Its Binary-square exception section states the exact binary-square optimum is not determined.
- **Assigned rank-one verifier** — artifacts/verify_rank_one_masking.py. Trigger: Package computation supporting the shell spectrum. Material read: Complete source and saved output. Method: Line-by-line inspection. Assessment: Correct finite corroboration only. Evidence: It enumerates \(q=2,3,5,n=3\) and checks 72 symbolic endpoint cases.

### checked_sources

- https://arxiv.org/abs/2609.18876
- 2026/09/18/exact-minimax-nonbinary-low-rank-masking--518b6bf1d437
- Delsarte 1978 bilinear-forms scheme
- artifacts/verify_rank_one_masking.py
- Resultary semantic searches

### residual_risks

- The nonbinary part is not new and is explicitly credited as covered.
- Classical association-scheme literature contains the raw rank-one spectrum, so originality is only in the masking minimax connection for the surviving binary-square region.

## Scientific value — PASS

Resolving the first nontrivial binary-square rank budget is a natural boundary left open by the exact-rank minimax theorem, not an arbitrary parameter slice. It gives an exact finite-length optimum for the original square masking problem and identifies a simple sampler strictly improving the source samplers at finite length.

### Value sources

- binary-square exception in the 2026-09-18 exact-minimax theorem
- Cohen--D'Oliveira--Sprintson rank-constrained masking problem

### Value risks

- The gain over \(q^{-1}\) is exponentially small in \(n\); the value is the exact boundary characterization rather than a new asymptotic exponent.

## Limitations

- Most nonbinary parameters are prior-covered by the 2026-09-18 exact-minimax theorem; the surviving novelty is binary square rank one.
- The theorem does not settle binary square exact minimaxity for rank budgets at least two.
- The finite verifier is corroborative only.

## Disposition

**PASSED**
