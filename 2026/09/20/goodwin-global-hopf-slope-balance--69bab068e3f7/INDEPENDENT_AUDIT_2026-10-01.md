# Fresh mathematical audit — Global Hopf-slope balance for third-order feedback cycles and the Goodwin oscillator

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** The periodic identities follow directly by multiplying the scalar third-order equation by \(z'\) and \(z''\), integrating over a period, and substituting the first identity into the second. The invariant-measure version follows from generator identities for \(v^2/2\), \(zv\), \(g(z)v\), \(vw\), and \(w^2/2\). The Goodwin elimination gives the claimed cubic coefficients, and \(a_1a_2-a_3=(\beta_1+\beta_2)(\beta_1+\beta_3)(\beta_2+\beta_3)\). The strict crossing statement correctly excludes the affine critical-slope case.

Sources checked: RESULT.md at the assigned source tree; artifacts/verify_identities.py; Chen–Shih 2026, DOI 10.1007/s00285-026-02419-w; Forger 2011, DOI 10.1073/pnas.1004720108.

Correctness risks: The numerical Goodwin orbit is corroborative only; the proof does not depend on it..

## Originality

**PASS.** Best-of-knowledge originality survives. Forger gives the exact Goodwin period/Sobolev relation, and Chen–Shih give the local Routh–Hurwitz Hopf threshold, but the inspected material does not state the derivative-energy-weighted feedback-slope identity, its invariant-measure extension, or the finite-amplitude slope-crossing consequence.

### Equivalent formulations

Searches/sources: Published-record semantic search: third-order feedback weighted slope identity Goodwin oscillator periodic orbit invariant measure Hopf threshold; Forger 2011 DOI 10.1073/pnas.1004720108; Chen–Shih 2026 DOI 10.1007/s00285-026-02419-w.

Evidence: Forger derives the period identity from an inner-product/integration-by-parts argument, not the weighted feedback-slope law. Chen–Shih equation (2.31) gives the local critical slope \(\alpha_1 f'(\bar x)=-(\beta_1+\beta_2)(\beta_2+\beta_3)(\beta_1+\beta_3)/(\alpha_2\alpha_3)\).

These are adjacent ingredients, not equivalent statements: neither implies the invariant-measure balance or strict finite-amplitude crossing without the additional multiplier identities.

### Broader coverage

Searches/sources: Published-record search for Goodwin recurrence balances and Hopf slope; Classical Goodwin/negative-feedback references cited in the record.

Evidence: No earlier searched record stated a broader theorem containing the exact weighted-slope identity for general scalar third-order feedback equations. Classical sources located concern oscillation existence/stability, period bounds, or sector/secant criteria.

The claimed theorem is broader than the Goodwin specialization but narrower than general cyclic-feedback stability theory; no inspected broader theorem dominates the exact identity.

### Exact database or table

Searches/sources: Resultary semantic search using the exact objects and weighted-slope consequence.

Evidence: The current record was the only exact matching published-record hit; nearby records concern different oscillators and different balances.

There is no external numerical table at issue; the applicable database check is exact/semantic theorem-record search.

### Claim versus prior implication

Searches/sources: Forger period formula versus second multiplier identity; Chen–Shih Hopf threshold versus global orbit average.

Evidence: Forger's identity supplies the \(b\)-weighted derivative-energy relation but not the second \(g'\)-weighted relation. Chen–Shih's local threshold identifies the constant after specialization but does not imply its finite-amplitude weighted average.

The final claim is not a corollary of either prior source alone; the new multiplier identity and invariant-measure argument are essential.

### Source inspections

- **Signal processing in cellular clocks** — SUPPORTING_NOT_COVERING.
  Identifier: https://pmc.ncbi.nlm.nih.gov/articles/PMC3060235/
  Trigger: Exact Goodwin period relation is the closest multiplier prior.
  Material read: Open full-text Goodwin example and exact period discussion.
  Method: lawful open-access full text
  Evidence: The paper derives the Goodwin period/Sobolev identity and minimum-period consequences, not the weighted feedback-slope theorem.
- **Stoichiometric balance and sustained rhythms** — SUPPORTING_NOT_COVERING.
  Identifier: https://doi.org/10.1007/s00285-026-02419-w
  Trigger: Same three-stage Goodwin model and exact local Hopf threshold.
  Material read: Full open-access HTML, including the general-repression Hopf section and equation (2.31).
  Method: lawful open-access full text
  Evidence: It gives the local Routh–Hurwitz critical slope and Hopf analysis, not the global weighted-slope or invariant-measure identities.

Originality risks:
- The 1977 Hastings–Tyson–Webster article and the 1978 Tyson–Othmer chapter were not inspected in complete full text; an older equivalent third-order multiplier identity could exist under different notation.

## Scientific value

**PASS.** The result identifies a natural exact finite-amplitude continuation of the local Hopf slope threshold, applies to all compact recurrent statistics of the scalar third-order feedback form, and forces a qualitative slope crossing on every genuinely nonlinear periodic orbit. This is a structural dynamical constraint rather than a routine numerical check.

Value risks: The theorem is necessary rather than an existence or stability theorem..

## Final assessment

The final claim survives unchanged on correctness, originality, and scientific value. No change to the scientific result or slogan is proposed.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
