# Independent audit — SCOPE-20260909-079

Audited at: 2026-09-30T23:18:42Z

Disposition: **repaired**

## Correctness

**PASS** — The original scientific claim survives, but the published proof had a real defect: one vector orthogonal to constants gives a Rayleigh quotient no larger than the second eigenvalue, not an upper bound. Fresh reconstruction of all 336 elements of SL(2,7), the explicit generator set and adjacency matrix verifies membership and connectedness. An independent exact characteristic polynomial computation factors the polynomial and isolates the largest nontrivial eigenvalue in the rational interval (183845/37617, 15913/3256), whose upper endpoint is below 4.89; the least eigenvalue is greater than -4.89. This independently proves the 7-regular bipartite double cover is Ramanujan. The repair removes the false Courant–Fischer direction and makes the exact Bareiss driver self-contained by embedding the witness set.

Sources/evidence:
- Actual package verify.py, exact_rayleigh.py, rayleigh_vec.json, bareiss_cert.py and bareiss_up.log at the audited source revision.
- Fresh exact SymPy characteristic-polynomial factorization and rational root isolation from the explicit generator set.

Residual risks:
- The repaired Bareiss certificate is computationally heavier than the spectral factorization; the historical saved Bareiss log is supporting evidence, not the sole proof.
## Originality

**PASS** — General Ramanujan covering theorems prove existence of degree-7 Ramanujan graphs but do not supply this specific Cayley graph of SL(2,7) in the central-unipotent generator class. published-record semantic search and literature searches found no earlier source with the explicit seven generators or the mixed-class dichotomy. The disconnected Borel family is elementary, but the explicit Ramanujan member inside the same constrained class is a distinct exact witness.

### Originality comparison details

**Equivalent formulations.** Bipartite double cover and base-spectrum formulations were compared through the identity that the nontrivial cover spectrum is the signed base spectrum.
- No exact generator-set match or equivalent class theorem was located.

**Broader coverage.** Existential graph results do not imply that the named central-unipotent Cayley class contains a Ramanujan member.
- Hall–Puder–Sawin prove existence of Ramanujan coverings for every degree/covering size but not this constrained Cayley construction.

**Exact database or table.** The witness is not merely a known catalog entry located under the searched descriptions.
- No prior exact table or generator tuple was found.

**Claim versus prior implication.** The exact class-membership claim is not implied by the broad existence results.
- Prior existence theorems allow arbitrary covering labels and do not force a Cayley realization in SL(2,7), let alone this generator class.

### Source inspections
- **Ramanujan Coverings of Graphs** — NOT_COVERING. Material read: Full HTML text and abstract/theorem context. Evidence: The result is existential over coverings and does not specify the audited Cayley witness.

Originality residual risks:
- A small-Cayley-graph catalogue could encode an isomorphic graph under different generators; no such covering source was found.
## Scientific value

**PASS** — The exact witness closes a proposed universal exclusion strategy for a natural constrained generator class: the same class contains an analytic disconnected family and a connected Ramanujan member. That is a motivated boundary/counterexample result with direct implications for how the constrained search space is treated.

Sources/evidence:
- General Ramanujan-covering literature establishes the relevance of degree-7 constructions.
- The audited exact witness settles the universal quantifier for the named class.

Residual risks:
- The result is not a classification of the whole class and makes no frequency claim.

## Limitations

- Single explicit Ramanujan witness, not a census of the generator class.
- No claim is made for primes q greater than 7.
- The repaired proof treats the Rayleigh vector only as a lower-bound cross-check, never as an upper certificate.
