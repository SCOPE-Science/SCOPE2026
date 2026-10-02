# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260913-037`

## Correctness — PASS

An independent exact-rational reconstruction of all 96 Kunz subpieces reproduced 76 infeasible and 20 feasible pieces. The smallest nonexceptional real minimum is \(11/5\). The 14 exceptional minima are two \(4/5\), four \(6/5\), and eight \(8/5\). In the 12 cases above one, integrality forces \(W\ge2\). In the two \(4/5\) cases the parametrizations give even expressions \(4s-2t-2\) and \(-6s+8t\), so the positive lower bound forces \(W\ge2\) there as well. This supplies an infinite proof independent of the bounded exceptional scans. Direct recomputation gives \(W=2\) for \(\langle5,6,7angle\), so the bound is sharp.

Sources:
- artifacts/verify_piecewise_exact.py
- artifacts/verify_exceptional_closedforms.py
- independent exact-rational LP reconstruction

Risks:
- Specific to multiplicity five and embedding dimension three.

## Originality — PASS

Bruns et al. prove Wilf nonnegativity for all multiplicities at most 18, but the fresh searches did not find the stronger exact gap two for this canonical subfamily.

Sources:
- arXiv:1903.04342
- assigned Kunz artifacts
- Resultary search

Risks:
- Grey-literature overlap remains possible.

### equivalent_formulations

Searches:
- Resultary multiplicity-5/embedding-dimension-3 search
- web exact-gap search

Evidence:
- No external exact match.

Reasoning:
Kunz, conductor/genus, and Wilf-number formulations were searched.

### broader_coverage

Searches:
- Bruns et al., Wilf's conjecture in fixed multiplicity

Evidence:
- Their theorem proves \(W\ge0\), not \(W\ge2\) on this stratum.

Reasoning:
Broader nonnegativity does not imply the sharp gap.

### exact_database_or_table

Searches:
- finite semigroup census searches

Evidence:
- No infinite-stratum optimum table was located.

Reasoning:
A bounded census would not prove the claim.

### claim_vs_prior_implication

Searches:
- claim versus fixed-multiplicity theorem

Evidence:
- Known results leave values zero and one logically possible here.

Reasoning:
The new polyhedral/integrality analysis is required.

### source_inspections

- **Wilf's conjecture in fixed multiplicity** — https://arxiv.org/abs/1903.04342. Material read: abstract and theorem scope. Assessment: not covering. Evidence: proves Wilf's conjecture through multiplicity 18, not the gap two
- **Assigned exact piecewise verifier** — artifacts/verify_piecewise_exact.py. Material read: complete source. Assessment: reproduced. Evidence: 76 infeasible, 20 feasible, same exact minima

## Scientific value — PASS

A sharp positive Wilf gap with an exact equality witness on a natural infinite stratum is a motivated refinement of a central numerical-semigroup inequality, not an arbitrary finite slice.

Sources:
- Bruns et al. fixed-multiplicity theorem
- assigned exact proof

Risks:
- No higher-multiplicity generalization is claimed.

## Limitations

- The bounded exceptional scans are not used as an infinite proof; the audit closes the exceptional pieces by exact LP minima plus integrality/parity.
- RESULT and METADATA point to `output/artifacts/...` while the files are actually under `artifacts/...`; the unchanged passed package is not publication-ready.

## Disposition

**PASSED**
