# Independent mathematical audit — The affine groups AGL(1,q) are BI-groups

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** For a connected inverse-closed Cayley graph, every eigenvalue from the unique nonlinear representation appears in the regular spectrum with multiplicity divisible by \(d\), whereas each of the \(d\) linear characters contributes once. Thus total spectral multiplicity modulo \(d\) recovers the number of linear-character sums at each eigenvalue. Connectedness excludes the only ambiguous residue \(d\), because if all linear sums equalled the principal sum \(|S|\), the top eigenvalue would not be simple. The zero adjacency trace then recovers the unique nonlinear character sum. Abdollahi--Zallaghi's connected-complement reduction extends this to all Cayley graphs. The affine groups \(\operatorname{AGL}(1,q)\) have exactly \(q-1\) linear characters and one nonlinear character of degree \(q-1\), so the criterion applies. The broader Frobenius-branch statement uses Seitz's classical one-nonlinear-character classification.

Checked sources: Assigned RESULT.md; Abdollahi--Zallaghi 2019 full arXiv text; Abdollahi--Zallaghi 2015 accessible author copy; Seitz 1968 classification as cited in later character-theory literature.

Residual correctness risks: A verified full PDF of Seitz 1968 could not be obtained after lawful access attempts; the classification statement was cross-checked through its citation chain, and the explicit \(\operatorname{AGL}(1,q)\) corollary can be checked directly..

## Originality

**PASS.** The complete 2019 primary source proves the order-20 and order-42 affine cases separately and lists BI-groups only through order 30. Its introduction still frames classification of BI-groups as open. No inspected source states the general spectral-residue criterion or the all-\(q\) \(\operatorname{AGL}(1,q)\) theorem.

### Equivalent formulations

Searches/sources: Resultary semantic search: AGL(1,q) BI-group spectral multiplicity residues one nonlinear character; arXiv:1710.04446; 2015 Character Sums for Cayley Graphs.

Evidence: The exact published-result hit was the audited theorem. The 2019 paper explicitly gives non-CI BI examples only of orders \(20\) and \(42\), namely the first affine instances. The 2015 paper supplies counterexamples and the BI classification question, not the all-affine theorem.

No equivalent general BI criterion for one-nonlinear-character groups was found.

### Broader coverage

Searches/sources: Seitz classification of groups with one nonlinear irreducible character; Abdollahi--Zallaghi BI-group classification work; 2026 ratio-one Frobenius Cayley-spectrum search.

Evidence: Seitz classifies the group structures but is not a BI theorem. The 2019 BI paper treats isolated affine cases and finite small-order census. The recent ratio-one Frobenius spectral paper concerns Ramanujan normal Cayley graphs, a different invariant.

No broader inspected theorem combines the character classification with BI invariance so as to dominate the audited result.

### Exact database or table

Searches/sources: Resultary exact theorem search; 2019 list of BI-groups of order at most 30.

Evidence: The small-order table contains \(\operatorname{AGL}(1,5)\) but cannot imply the infinite family. No earlier exact all-\(q\) record was found.

The infinite affine theorem is not a table recomputation.

### Claim versus prior implication

Searches/sources: Can the order-20/order-42 computations imply all \(q\)?; Does Seitz's classification alone imply the BI property?.

Evidence: The two finite examples do not imply a uniform spectral mechanism. Seitz gives group structure but no character-sum invariance under Cayley graph isomorphism. The multiplicity-modulo-\(d\) argument is the new implication step.

The final theorem is not a mechanical corollary of either prior source separately.

### Source inspections

- **Non-Abelian finite groups whose character sums are invariant but are not Cayley isomorphism** — PARTIAL_PRIOR.
  Identifier: https://arxiv.org/abs/1710.04446
  Trigger: Direct predecessor containing the two affine examples and BI classification question.
  Material read: Complete arXiv paper, including introduction, Proposition 2.5, the order-20 and order-42 proofs, and the small-order BI list.
  Method: lawful open-access full text
  Evidence: It proves \(\operatorname{AGL}(1,5)\) and \(\operatorname{AGL}(1,7)\) separately but no all-\(q\) theorem.
- **Character Sums for Cayley Graphs** — BACKGROUND_NOT_COVERING.
  Identifier: https://doi.org/10.1080/00927872.2014.967398
  Trigger: Foundational BI counterexample paper and source of the classification problem.
  Material read: Public author-copy material and full abstract/problem context.
  Method: lawful public author material
  Evidence: It shows BI failure in other groups and formulates the problem; it does not supply the audited criterion.
- **Finite groups having only one irreducible representation of degree greater than one** — ACCESS_RISK.
  Identifier: https://doi.org/10.1090/S0002-9939-1968-0222160-X
  Trigger: Critical structural classification used for the broad Frobenius corollary.
  Material read: Bibliographic theorem citation chain; open-web full text was unavailable and an authorized lawful retrieval found no verified PDF.
  Method: lawful access attempts
  Evidence: The classical classification statement is consistently cited in later character-theory literature, but this audit did not obtain a verified primary full text.

Residual originality risks:
- The inaccessible Seitz primary text creates source-version risk for the broad classification wording, though not for the direct \(\operatorname{AGL}(1,q)\) application.
- An unindexed general BI observation could exist in character-theory literature.

## Scientific value

**PASS.** The result replaces two isolated affine examples with a simple general spectral mechanism covering every \(\operatorname{AGL}(1,q)\), and standard CI restrictions then yield an infinite nonabelian BI-but-not-CI family. It directly advances the published BI-group classification problem.

Residual value risks: The extraspecial two-group branch of the one-nonlinear-character classification remains outside the theorem..

## Final assessment

The final claim survives unchanged on correctness, originality and scientific value. No change to `RESULT.md` or `SLOGAN.txt` is proposed.

Earlier same-model scientific evidence remains separately identified in `AUDIT.json`; it is not relabeled as this independent assessment.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
