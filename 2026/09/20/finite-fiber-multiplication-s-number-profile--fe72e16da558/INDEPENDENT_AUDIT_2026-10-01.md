# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-fe72e16da558`

## Final claim

For finite-dimensional Euclidean fibers on a sigma-finite measure space, approximation, Bernstein, Gelfand and Kolmogorov numbers of the matrix-valued \(L^p\) multiplication operator are all \(\max\{\gamma,\beta_n\}\), and the limiting floor is exactly the distance to compact, finitely strictly singular and strictly singular operators.

## Correctness — PASS

The proof reconstructs. On atoms the space is an \(\ell^p\)-sum of finite Euclidean blocks, so truncating the globally largest singular directions gives a finite-rank approximation with error \(\max\{\gamma,\beta_n\}\). Conversely, each atomic singular direction above a threshold gives a finite-dimensional subspace on which the multiplier is bounded below, and on the nonatomic part a countable dense-sphere argument produces one fixed fiber vector on a positive-measure set, hence an infinite-dimensional scalar \(L^p\) copy with the same lower bound. Those witnesses give the matching approximation, Bernstein and Gelfand bounds. Reflexive Bochner duality transfers Gelfand numbers of the adjoint to Kolmogorov numbers. The same infinite bounded-below witnesses give the lower distance to compact/FSS/SS, while atomic truncation gives the matching upper bound.

### Correctness sources

- assigned RESULT.md
- Plichko–Shevchik 1999 full text
- Duru–Kitover–Orhon arXiv:1104.2806
- classical diagonal s-number literature

### Correctness risks

- The argument uses \(1<p<\infty\) for the clean reflexive duality step.
- The fibers are fixed finite-dimensional Euclidean spaces; arbitrary Banach fibers are not covered.

## Originality — PASS

The scalar atomless bounded-below phenomenon and scalar diagonal approximation theory are prior art. Searches did not locate the simultaneous four-s-number formula for mixed atomic/nonatomic, finite matrix-valued Bochner \(L^p\) multiplication together with all three exact operator-ideal distances. The most plausible older diagonal paper could not be fully inspected because publisher access required human verification; that is recorded as residual risk rather than treated as novelty evidence.

### equivalent_formulations

Searches:
- Resultary semantic query for finite-fiber multiplication exact approximation/Bernstein/Gelfand/Kolmogorov profile
- web search for Hutton–Morrell–Retherford diagonal approximation numbers and multiplication-operator s-numbers

Evidence:
- Current published hits did not produce a theorem matching the mixed matrix-valued formula.
- Plichko–Shevchik gives infinite-dimensional bounded-below/compact restriction structure for scalar multipliers, not the all-\(n\) matrix-valued profile.

Reasoning:
Equivalent formulations as direct-integral block singular-value order statistics and as four classical strict s-number profiles were compared.

### broader_coverage

Searches:
- Plichko–Shevchik 1999
- Duru–Kitover–Orhon 2013
- classical diagonal-operator sources

Evidence:
- The inspected papers establish scalar/restriction or structural characterizations, not the full mixed finite-fiber theorem.

Reasoning:
The audited theorem combines atomic singular-mode order statistics with a nonatomic norm floor and exact ideal distances; no inspected broader theorem subsumes all of these.

### exact_database_or_table

Searches:
- current Resultary multiplication/s-number records

Evidence:
- No exact published table/database result was located.

Reasoning:
The profile is a theorem derived from the multiplier structure, not a finite table.

### claim_vs_prior_implication

Searches:
- claim-versus-scalar-diagonal implication comparison

Evidence:
- Scalar diagonal formulas do not by themselves imply simultaneous matrix singular-mode rearrangement plus a nonatomic floor, nor the FSS/SS distance equality on mixed measure spaces.

Reasoning:
Additional finite-fiber geometry and the nonatomic witness are required.

### source_inspections

- **On Restriction Properties of Multiplication Operators** — https://doi.org/10.4171/ZAA/867. Trigger: Primary scalar multiplication source for infinite-dimensional bounded-below witnesses. Material read: Open full text and theorem context. Method: Primary full-text comparison. Assessment: Partial prior art, not covering. Evidence: It studies infinite-dimensional subspaces on which a scalar multiplier is an isomorphism or compact, rather than the audited finite-fiber all-s-number formula.
- **Multiplication operators on vector-valued function spaces** — https://arxiv.org/abs/1104.2806. Trigger: Vector-valued multiplication operator literature. Material read: Primary abstract and available full-text source identification. Method: Scope comparison. Assessment: Not covering. Evidence: Its main result characterizes multiplication operators by invariance/commutation, not their classical s-number profiles.
- **Diagonal operators, approximation numbers, and Kolmogoroff diameters** — https://doi.org/10.1016/0021-9045(76)90095-2. Trigger: Principal historical diagonal-s-number risk. Material read: Bibliographic/abstract-level material only; full text could not be inspected because access required human verification. Method: Access-limited prior-art comparison. Assessment: Unresolved historical overlap risk, not decisive coverage. Evidence: The title and citation context make it relevant to scalar diagonal pieces, but available material did not establish the audited mixed matrix-valued theorem.

### checked_sources

- Plichko–Shevchik 1999 full text
- Duru–Kitover–Orhon arXiv:1104.2806
- Hutton–Morrell–Retherford 1976 metadata
- current Resultary s-number search
- assigned RESULT.md

### residual_risks

- The 1976 diagonal paper could not be fully read because human verification was required at the publisher; no bypass was attempted.
- Older direct-integral/operator-ideal literature may package part of the result under different terminology.

## Scientific value — PASS

A single explicit order statistic simultaneously determines four classical approximation scales and three ideal distances for a natural mixed matrix-valued multiplier class. The theorem unifies atomic and nonatomic behavior and makes the compact/FSS/SS boundary completely explicit; this is a reusable structural result rather than a benchmark calculation.

### Value sources

- assigned exact profile theorem
- classical scalar multiplier/diagonal context

### Value risks

- No endpoint \(p=1,\infty\) or infinite-dimensional-fiber extension is claimed.

## Limitations

- The theorem assumes \(1<p<\infty\) and finite-dimensional Euclidean fibers.
- Historical overlap with older diagonal theory remains a documented access risk.
- The access restriction on the 1976 source was not bypassed or retried after human verification was required.

## Disposition

**PASSED**
