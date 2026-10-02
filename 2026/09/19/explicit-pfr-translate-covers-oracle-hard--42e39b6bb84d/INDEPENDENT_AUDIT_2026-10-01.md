# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-42e39b6bb84d`

## Correctness — PASS

For \(A_z=H\cup\{z\}\), the sumset is exactly \(H\cup(z+H)\), so the doubling constant is below two, and two \(H\)-cosets give an optimal cover under the size constraint. For any output subspace \(V\) of dimension at most \(m\), writing \(U=V\cap H\) with dimension \(h\), an \(L\)-coset cover of \(H\) forces \(2^{m-h}\le L\). The quotient image of each output coset has at most \(2^{m-h}\le L\) classes, so the fixed output can cover at most \(L^2\) possible hidden outliers. Samples reveal the exceptional point with probability at most \(s/(2^m+1)\); before a positive membership hit, each informative query tests at most one candidate outlier. Conditional on no hit, at least \(2^m-1-q\) candidates remain, giving the residual \(L^2\) ratio and the stated lower bound. The assigned subspace enumeration is correct corroboration, not the proof.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_cover_barrier.py
- Arunachalam--Dutt--Grewal--Gupte, arXiv:2609.20771

### Correctness risks

- The lower bound concerns explicit lists of translate representatives under sample plus point-membership access.
- It does not apply to compressed witnesses or stronger oracles.

## Originality — PASS

The primary 2026 algorithmic PFR theorem was inspected in full through its main-result section: it explicitly outputs a basis of a PFR subspace and guarantees that polynomially many translates exist, but it does not output the translate representatives. Fresh semantic searches found no prior lower bound showing that materializing those representatives is exponentially harder. The hidden-outlier family is elementary, so folklore risk is real, but no covering theorem or equivalent oracle lower bound was located.

### equivalent_formulations

Searches:
- Resultary semantic search for explicit PFR translate representatives and oracle lower bounds
- search of algorithmic PFR output conventions

Evidence:
- The audited record was the only exact match returned.
- The primary theorem outputs only a subspace basis with an existential cover-number guarantee.

Reasoning:
Equivalent formulations as witness recovery, occupied quotient-coset discovery, and explicit translate listing were checked.

### broader_coverage

Searches:
- Arunachalam--Dutt--Grewal--Gupte arXiv:2609.20771
- earlier algorithmic PFR and robust-PFR work cited there

Evidence:
- These works solve subspace recovery efficiently under sample/membership access.
- None of the inspected theorem statements requires outputting a list of covering cosets.

Reasoning:
The audited lower bound targets a strictly stronger output requirement and therefore is not implied by the positive algorithms.

### exact_database_or_table

Searches:
- current Resultary PFR findings
- algorithmic PFR theorem statements

Evidence:
- No table/database entry gives explicit witness query complexity; the result is an oracle lower bound.

Reasoning:
The exact \(L^2\) candidate bound is structural rather than a lookup.

### claim_vs_prior_implication

Searches:
- claim-versus-primary-output implication comparison

Evidence:
- Knowing a correct subspace and an existential \(K^{O(1)}\) cover does not reveal which rare quotient coset is occupied.
- The hard family gives the correct subspace for free yet still hides one necessary representative among exponentially many candidates.

Reasoning:
The positive PFR theorem therefore cannot imply an efficient explicit-cover witness algorithm in this oracle model.

### source_inspections

- **Marton's conjecture in polynomial time** — https://arxiv.org/abs/2609.20771. Trigger: Primary algorithmic PFR result whose output convention motivates the boundary. Material read: Primary full text through the abstract, main theorem, prior-work discussion, and technical overview pages 1--10, obtained through authorized access after open routes failed. Method: Full theorem/output-model comparison. Assessment: NOT COVERING the explicit-witness task. Evidence: Theorem 1.2 outputs a basis for a subspace and only guarantees that \(A\) can be covered by \(K^{O(1)}\) translates.
- **Assigned cover-barrier verifier** — artifacts/verify_cover_barrier.py. Trigger: Finite checks of doubling and quotient-dimension inequalities. Material read: Complete source and saved output. Method: Line-by-line inspection. Assessment: Correct finite corroboration. Evidence: It verifies the identities through \(m=8\) and enumerates 2165 subspaces for \(m\le3\).

### checked_sources

- https://arxiv.org/abs/2609.20771
- artifacts/verify_cover_barrier.py
- current Resultary PFR semantic search

### residual_risks

- Because the lower-bound family is simple, an unindexed folklore observation remains possible.

## Scientific value — PASS

The result isolates an information-theoretic boundary in a major new algorithmic structure theorem: learning the PFR subspace can be polynomial while materializing even a constant-size optimal cover witness requires exponentially many interactions. The separation persists below doubling two and even when the correct subspace is supplied, so it identifies a genuine output-model limitation rather than a computational artifact.

### Value sources

- algorithmic PFR Theorem 1.2
- audited hidden-outlier lower bound

### Value risks

- The obstruction is tied to explicit representative lists and a rare-outlier access model.

## Limitations

- The lower bound is for explicit translate lists under uniform-sample plus point-membership access.
- It does not rule out compressed cover descriptions or stronger occupied-coset oracles.
- Originality is best-of-knowledge with material folklore risk.

## Disposition

**PASSED**
