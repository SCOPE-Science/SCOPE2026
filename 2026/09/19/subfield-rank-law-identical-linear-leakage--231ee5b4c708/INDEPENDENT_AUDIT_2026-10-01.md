# Independent mathematical audit — 2026-10-01

## Final claim assessed

Subfield-rank law for identical leakage under linear computations

## Correctness — PASS

PASS. Finite-field trace duality identifies every nonzero \(B\)-linear functional \(F\to B\) with \(z\mapsto\operatorname{Tr}_{F/B}(\beta z)\), \(\beta\ne0\). Under the nondegenerate trace pairing on \(F^K\), the output leakage functionals correspond to the vectors \(\beta g_i\). Multiplication by \(\beta\) is a \(B\)-linear automorphism, so their exact functional rank is the \(B\)-dimension of the column span of \(G\). A \(B\)-basis of columns therefore generates the complete leakage transcript. If that rank is \(K\), the column span has a \(B\)-basis that is automatically \(F\)-independent, giving a change of input basis after which \(G\) is \(B\)-valued; conversely a \(B\)-valued full-rank generator has rank \(K\). Rank \(Km\) makes the local leakage map injective. For a systematic random generator, quotienting by \(B^K\) reduces full disclosure to full rank of \(L\) random vectors in a \(D=K(m-1)\)-dimensional \(B\)-space, yielding the stated product probability. The finite verifier agrees, but the theorem is proved algebraically rather than by enumeration.

## Originality — PASS

PASS to the best of current knowledge with explicit partial prior coverage. Aoutouf--Augot's complete primary preprint was inspected through its general computation framework and identical-leakage section. It proves only the simple-addition no-improvement statement and says that array summation appears to extend, while simulations suggest extension-field weighted relations and LFSRs can benefit. A published 18 September result already proves the stabilizer-field obstruction and therefore covers the base-field no-amplification corollary. A separate 19 September published result gives a minimum subfield-rank obstruction for computation-code words and a quotient-space criterion for one extra output. Neither inspected prior result states the exact local identity \(\operatorname{rank}_B L_{G,\lambda}=\rho_B(G)\), its generator-column descent equivalence, the maximal-rank full-disclosure theorem, or the random systematic saturation probability. Originality is therefore limited to that exact local rank law and its genuinely additional consequences; the base-field corollary is explicitly prior work.

### equivalent_formulations

Searches: Resultary: identical leakage linear computations subfield column rank trace leakage secret sharing; Subfield-rank obstruction for identical leakage under linear computations; Identical linear leakage cannot exploit computations over its stabilizer field

Evidence: The 18 September stabilizer result covers computations defined over the leakage subfield. The other 19 September record uses the minimum subfield rank of computation-code words to derive a necessary repair obstruction, not the column-span rank of the generator as the exact local leakage dimension.

Reasoning: Rank weight of computation words and column-span rank of a generator are different invariants serving different statements; neither inspected prior theorem is equivalent to the exact local-map rank identity.

### broader_coverage

Searches: arXiv:2609.19929 complete primary text; WCC 2026 subfield subcode LERS; rank-metric support finite fields trace duality

Evidence: The primary source supplies the product-code LERS framework and identical-addition obstruction but no general exact reused-leakage dimension theorem. Standard rank-metric and trace-duality theory supplies ingredients, not the source-specific leakage interpretation and corollaries.

Reasoning: No inspected broader theorem mechanically yields the full local rank/full-disclosure/random-threshold package.

### exact_database_or_table

Searches: Resultary semantic search for exact subfield column-rank leakage law and random systematic threshold

Evidence: Two nearby published records were found and inspected; neither contains the exact generator-column rank formula or random saturation theorem.

Reasoning: No numerical database is relevant; theorem-level published-record comparison was performed.

### claim_vs_prior_implication

Searches: Aoutouf--Augot Section 5 identical leakage full text; 2026/9/18 stabilizer obstruction full result; 2026/9/19 minimum subfield-rank obstruction full result

Evidence: The source proves simple addition only and reports simulations for more general relations. The 18 September result directly covers only the no-amplification subfield case. The minimum-rank obstruction gives a necessary compression theorem for attacks but does not determine the rank of the complete local reused-leakage map.

Reasoning: The exact local rank identity and maximal disclosure conclusion require a separate trace-dual identification of the output functionals with the computation columns.

## Scientific value — PASS

PASS. The exact local rank law replaces example-specific identical-leakage behavior by one natural invariant, distinguishes subfield-rational computations from genuine extension-field amplification, identifies the complete local-disclosure endpoint, and gives a sharp random saturation threshold. These facts are directly useful for deciding how much information repeated linear leakage creates before any global repair-code question is addressed.

## Source inspections

- **On the Leakage of Massey Secret Sharing Schemes under Linear Computations** — https://arxiv.org/abs/2609.19929. Material read: Complete 23-page primary preprint, including Sections 4 and 5 on general linear computations and identical leakage. Assessment: PRIMARY_SOURCE_PARTIAL_ONLY. Evidence: The paper proves identical leakage cannot exploit simple addition, suggests array summation, and reports simulations for weighted relations/LFSRs; it does not state the audited exact column-rank law.
- **Identical linear leakage cannot exploit computations over its stabilizer field** — https://github.com/Resultary/2026/blob/main/2026/9/18/SCOPE-identical-leakage-subfield-obstruction--7e9d9ede3eb3/RESULT.md. Material read: Complete published result. Assessment: DECISIVE_PARTIAL_COVERAGE. Evidence: It proves the stabilizer-field/base-field no-amplification corollary but not the exact local subfield-rank dimension or full-disclosure/random threshold.
- **Subfield-rank obstruction for identical leakage under linear computations** — https://github.com/Resultary/2026/blob/main/2026/9/19/SCOPE-subfield-rank-obstruction-identical-leakage--87665986b2bd/RESULT.md. Material read: Complete published result. Assessment: RELATED_DIFFERENT_RANK_STATEMENT. Evidence: It uses minimum subfield rank of computation-code words to compress a global attack and gives a one-output quotient criterion; it does not state the generator-column span as the exact local leakage rank.

## Limitations and residual risks

The result is restricted to identical nonzero one-symbol \(B\)-linear leakage on linear computations. It does not cover nonlinear leakage, independently chosen leakage maps, refreshed shares, or multiplicative computations.

- The exact rank identity is short linear algebra once the right invariant is named, so folklore or near-simultaneous priority remains plausible.
- One of the related rank-obstruction records is dated the same day; it is scientifically distinct but highlights contemporaneous discovery risk.
- The theorem does not decide global LERS existence in the intermediate-rank regime.

## Disposition

**passed**
