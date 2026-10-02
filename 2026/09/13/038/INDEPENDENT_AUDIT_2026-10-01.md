# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260913-038`

## Correctness — PASS

The lower certificate is a valid trial-measure energy bound; an independent numerical recomputation gives capacity \(0.2215367734\ldots\), safely above 0.221. The upper certificate's cell potential formula is correct, and splitting at the singular endpoints and unique critical point suffices to bound each contribution. A separate dense recomputation gives an upper value near 0.22911, consistent with the exact certified 0.2292253 bound. The scripts use rational arithmetic and certified logarithm enclosures in place of those floating checks, so the claimed \(0.221\le\operatorname{cap}(E_3)\le0.230\) is supported.

Sources:
- artifacts/lower_cert.py
- artifacts/upper_cert.py
- artifacts/upper_weights.json
- independent energy/potential recomputation

Risks:
- Certification relies on the inspected atanh-series logarithm enclosure implementation.

## Originality — PASS

General rigorous capacity algorithms and multiple-interval inequalities predate the record, but no inspected source gives this finite \(E_3\) enclosure. Direct evaluation of Dubinin-Karp's simple general upper theorem gives only about 0.2341 after rescaling, so it does not imply 0.230.

Sources:
- Ransford-Rostand 2007
- Dubinin-Karp 2009
- assigned exact certificates
- Resultary search

Risks:
- A specialized unindexed finite-prefractal table could overlap.

### equivalent_formulations

Searches:
- Resultary finite-Cantor-prefractal capacity search
- web search for \(E_3\) capacity

Evidence:
- No external exact certificate found.

Reasoning:
The finite stage was distinguished from the limiting Cantor set.

### broader_coverage

Searches:
- Ransford-Rostand 2007
- Dubinin-Karp 2009

Evidence:
- General methods/bounds only; the limiting Cantor-set value is a different object.

Reasoning:
Their directly inspected bounds do not mechanically yield this interval.

### exact_database_or_table

Searches:
- prefractal capacity table searches

Evidence:
- No certified \(E_3\) row located.

Reasoning:
Not covered by a known table found in search.

### claim_vs_prior_implication

Searches:
- claim versus multiple-interval theorem

Evidence:
- Dubinin-Karp's simple upper theorem is weaker on this instance.

Reasoning:
The explicit trial measures and exact enclosures are decisive.

### source_inspections

- **Computation of capacity** — https://doi.org/10.1090/S0025-5718-07-01941-2. Material read: abstract and scope. Assessment: not covering. Evidence: the approximately 0.220949 value is for the limiting Cantor set
- **Two-sided bounds for logarithmic capacity of multiple intervals** — https://arxiv.org/abs/0905.3283. Material read: full theorem statements. Assessment: not covering. Evidence: the direct upper bound is about 0.2341

## Scientific value — PASS

A certified capacity enclosure for the canonical third stage of the middle-third Cantor construction is a natural benchmark for potential-theory algorithms and convergence studies.

Sources:
- rigorous capacity-computation literature
- assigned certificates

Risks:
- The interval is not claimed optimal.

## Limitations

- Trial measures are not optimal.
- The midpoint estimate is not certified.
- RESULT and METADATA use `output/artifacts/...` while the files are under `artifacts/...`; the unchanged passed package is not publication-ready.

## Disposition

**PASSED**
