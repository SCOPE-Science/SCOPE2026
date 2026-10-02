---
{"schema_version":1,"audit_date_utc":"2026-10-01","status":"passed"}
---

# Independent mathematical audit

## Final claim

The stated signing of the Chvatal graph has the displayed exact characteristic polynomial and spectral radius below sqrt(33/5), hence is a two-sided Ramanujan signing.

## Correctness — PASS

The archived signing was reconstructed from the stated 12-vertex edge list and mask. Its exact characteristic polynomial matches the claim. For M=33I-5A^2, all exact leading principal minors are positive, so Sylvester’s criterion gives M positive definite and hence rho(A)^2<33/5. This independently certifies the two-sided Ramanujan inequality.

Checked sources: artifacts/certify.py (blob 250e528d599c67d934023da9be99099de8593b26); independent exact characteristic polynomial and positive-definiteness check

Residual risks: The identification with other labelings of the Chvatal graph is by the stated standard edge list and matching structural invariants; the spectral certificate itself is labeling-independent once the graph is fixed.

## Originality — PASS

The primary covering literature leaves the full two-sided Bilu-Linial signing problem open for general non-bipartite bases; no inspected source supplies this Chvatal signing or a theorem that forces it. Searches located only the current explicit datum for this base.

### Equivalent formulations

Signed adjacency and two-lift formulations were both checked. Evidence: No equivalent signing or signed-spectrum row was located outside the current finding.

### Broader coverage

Those theorems do not imply a two-sided Ramanujan signing for this non-bipartite base. Evidence: The inspected primary literature provides one-sided results in general and full two-sided results in bipartite settings, while noting the general two-sided problem remains open.

### Exact database or table

The certificate is not a known-table lookup on the evidence inspected. Evidence: No exact signed-spectrum table containing mask 6995 or the stated characteristic polynomial was found.

### Claim versus prior implication

The explicit exact signing supplies information not mechanically implied by the prior theorems. Evidence: Existing general results stop short of the two-sided conclusion required here.

### Source inspections

- **Ramanujan coverings of graphs** — https://arxiv.org/abs/1506.02335. Trigger: Primary result closest to general Ramanujan covering existence. Material read: Introduction and discussion distinguishing one-sided general coverings from full two-sided bipartite coverings. Method: Primary full-text inspection. Assessment: NOT_COVERING. Evidence: The source explicitly leaves the general full two-sided problem unresolved outside the bipartite setting.
- **Open problems in the spectral theory of signed graphs** — https://arxiv.org/abs/1907.04349. Trigger: Survey of the Bilu-Linial signing problem and known one-sided bounds. Material read: Section discussing signed spectral-radius conjectures and MSS consequences. Method: Full-text survey inspection. Assessment: NOT_COVERING. Evidence: It records the general two-sided signing problem rather than an explicit Chvatal solution.

Checked sources: https://arxiv.org/abs/1506.02335; https://arxiv.org/abs/1907.04349; standard Chvatal graph references

Residual risks: Priority language such as “first constructive” was not established and is not endorsed by this audit.

## Scientific value — PASS

The Chvatal graph is a canonical small non-bipartite 4-regular graph, and a fully exact two-sided Ramanujan signing gives a concrete witness inside a general open signing problem. The certificate has substantial margin and is directly reusable as a benchmark example.

Checked sources: Ramanujan covering literature; standard Chvatal graph literature

Residual risks: This is one explicit base and does not advance existence for arbitrary non-bipartite graphs.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and scientific value.
