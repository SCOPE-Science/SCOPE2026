# Independent audit — 2026-09-30

**Record:** `SCOPE-20260910-017`

## Correctness — PASS

The headline claim is proved by the first cover equation alone. Exact recomputation confirmed the factorization, the rational witnesses on D_1 and D_2, and the mod-8 obstruction for D_7: among all 512 residue triples, the 32 solutions of X^2+Z^2=7U^2 modulo 8 have all three coordinates even. Clearing denominators from a hypothetical Q_2 point produces a primitive integral triple, contradicting that wall; therefore D_7(Q_2) and hence D_7(Q) are empty. Balakrishnan–Dogra's full text independently confirms that E_31 has rank 2. The final claim does not require a full census of X(Q).

## Originality — PASS

The full Balakrishnan–Dogra source treats the a=31 curve by quadratic Chabauty and states the rank-2 elliptic quotient, but it does not give this D_7 cover obstruction. Searches for the exact curve together with D_7, the cover equation, and a 2-adic obstruction returned no prior source beyond this record. General covering-collection literature supplies the method, not this exact local certificate.

### Structured originality checks

- **equivalent_formulations:** Checked the equivalent conic/Hilbert-symbol formulation of the first D_7 cover equation and searches using the exact curve equation and D_7 parameter.
- **broader_coverage:** Balakrishnan–Dogra gives broader rational-point machinery for the same curve family; Flynn–Wetherell gives broader covering-collection machinery. Neither inspected material states or logically supplies the exact D_7-at-2 certificate as a recorded result.
- **exact_database_or_table:** A semantic search of published findings and exact web searches for the curve plus D_7/2-adic obstruction found this record but no prior exact table or certificate.
- **claim_vs_prior_implication:** The prior papers motivate the curve and the descent method, but the precise local obstruction still requires the specific factorization and local calculation; it is not a stated corollary or parameter row in the inspected sources.

## Scientific value — PASS

Although the local obstruction itself is elementary, it is not an arbitrary negative check: D_7 is the first unresolved twist after explicit D_1 and D_2 rational witnesses in a standard rank-excess genus-2 benchmark. Pruning that canonical cover is a reusable, exact step toward a classical covering-collection resolution and a useful cross-check against height-theoretic methods.

## Source inspections

- **Balakrishnan–Dogra, Quadratic Chabauty and Rational Points II** — Full HTML, especially the family definition and the a=31 example. The paper studies X_a and states that E_31 has rank 2; it does not present the D_7 local obstruction. https://arxiv.org/html/1705.00401v2
- **Published-findings semantic search** — Top exact-match result and nearby arithmetic-geometry hits. No distinct prior finding covering the exact D_7 certificate was returned. https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE017

## Residual risks

- The general Flynn–Wetherell papers were used as method context rather than as the decisive originality source; no claim is made that every historical covering-collection computation has been exhaustively indexed.
- The committed RESULT.md names output/artifacts paths, while the audited tree stores the verifier files under artifacts/. This is a reproducibility-path documentation defect, not a defect in the mathematical proof.

## Disposition

**PASSED**. The final claim passes correctness, originality, and scientific value.
