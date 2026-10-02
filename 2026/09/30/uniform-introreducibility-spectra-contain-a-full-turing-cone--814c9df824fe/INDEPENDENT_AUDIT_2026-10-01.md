# Independent mathematical audit — SCOPE-20260930-814c9df824fe
Audit date: 2026-10-01 (UTC) UTC.
Disposition: **passed**.

## Final claim
Every infinite introenumerable set contains an infinite uniformly introreducible core \(R\) such that the Turing degrees of uniformly introreducible infinite subsets of \(R\) are exactly the cone above \(\deg_T(R)\); moreover a single decoder can witness uniform introreducibility for a constructed family realizing every degree in that cone.

## Correctness
Status: **PASS**.

Cintioli supplies a core \(R\) with one functional recovering \(R\) from every infinite subset. For any \(X\geq_T R\), pull the finite-initial-segment code \(S_X\) back along the increasing enumeration of \(R\). From an infinite subset of the pullback, the fixed core decoder first recovers \(R\); its indices form an infinite subset of \(S_X\), from which the universal initial-segment decoder recovers \(X\), and hence the full pullback. This composition is independent of \(X\). Conversely, every infinite subset of \(R\) computes \(R\), giving the exact lower cone bound. Both Turing inequalities are explicit, so the constructed subset has degree exactly \(\deg_T(X)\).

## Originality
Status: **PASS**.

Cintioli’s recent theorem supplies the uniformly introreducible core and fixed decoder but does not state the cone spectrum. Kumar–Shelah Lemma 2.2 gives a closely related full-cone theorem for introreducible subsets using a Dekker code, but it does not assert uniform introreducibility or one decoder for the full family. Combining the two still requires the functional-level observation that the core decoder can be composed with a universal initial-segment decoder uniformly in \(X\). Published-record search located no earlier common-decoder cone theorem. The full 1968 Jockusch article was not available in the inspected lawful route, so older implicit coverage remains a named residual risk rather than novelty evidence.

### Equivalent formulations
- Search/source: Patrizio Cintioli, Every introenumerable set contains a uniformly introreducible subset, arXiv:2609.17605v1
- Search/source: Ashutosh Kumar and Saharon Shelah, Ultrafilters and Turing Independence, Lemma 2.2
- Search/source: Published-record semantic query: uniformly introreducible subsets cone common decoder Cintioli Kumar Shelah
- Evidence: Cintioli states the uniform-core existence theorem; Kumar–Shelah state the nonuniform introreducible cone theorem; neither inspected source states the common-decoder uniform cone theorem.
- Reasoning: No equivalent formulation was located in the inspected material.

### Broader coverage
- Search/source: arXiv:2609.17605v1
- Search/source: Kumar–Shelah, Lemma 2.2
- Evidence: The closest results cover the two principal ingredients separately but not the uniform family conclusion.
- Reasoning: Neither prior statement mechanically contains the claim; the composed functional is an additional theorem.

### Exact database or table
- Search/source: Published-record semantic corpus
- Evidence: No exact table/database is relevant to this infinite degree-spectrum statement.
- Reasoning: The named check is inapplicable as a tabulation question; the exact published theorem corpus was searched instead.

### Claim versus prior implication
- Search/source: Cintioli 2026
- Search/source: Kumar–Shelah 2026, Lemma 2.2
- Evidence: Cintioli gives a fixed decoder for the ambient core; Kumar–Shelah’s pullback construction gives cone degrees only at the introreducible level.
- Reasoning: The uniform common-decoder conclusion requires composing the two decoding mechanisms and checking that the functional is independent of the coded real; that step is not stated in the inspected priors.

### Source inspections
- **Every introenumerable set contains a uniformly introreducible subset** (arXiv:2609.17605v1): trigger — ownership source for the uniformly introreducible core; material read — accessible primary abstract and theorem-level material describing a single procedure for recovery from infinite subsets; method — lawful primary-source inspection; assessment — CORE_EXISTENCE_ONLY; evidence — The source supplies a uniformly introreducible subset with a common recovery procedure but does not state the full cone spectrum inside that core.
- **Ultrafilters and Turing Independence** (Kumar–Shelah 2026, Lemma 2.2): trigger — closest known cone-spectrum result; material read — full accessible PDF around Lemma 2.2 and its Dekker-code pullback proof; method — lawful full-text inspection; assessment — NONUNIFORM_CONE_PRECEDENT; evidence — Lemma 2.2 gives the full cone of degrees for introreducible subsets of an introreducible set, not a uniformly introreducible family sharing one decoder.
- **Uniformly Introreducible Sets** (JSL 33 (1968), 521-536): trigger — foundational paper most likely to contain older implicit coverage; material read — bibliographic record and accessible extract only; full article text was not available in the inspected route; method — lawful accessible-material inspection; assessment — INACCESSIBLE_PLAUSIBLE_SOURCE; evidence — No affirmative overlap was visible in the accessible material; full-text noncoverage is not claimed.

## Value
Status: **PASS**.

The theorem upgrades a recent existence result to exact hereditary degree control: inside one selected uniform core, every and only degrees above the core occur, and one reconstruction functional works across the constructed cone family. That is a natural and reusable structural strengthening of uniform introreducibility, not an arbitrary coding exercise.

## Checked sources
- Patrizio Cintioli, Every introenumerable set contains a uniformly introreducible subset, arXiv:2609.17605v1.
- Ashutosh Kumar and Saharon Shelah, Ultrafilters and Turing Independence, 2026, Lemma 2.2.
- Carl G. Jockusch Jr., Uniformly Introreducible Sets, Journal of Symbolic Logic 33 (1968), 521-536.

## Residual risks
- The complete 1968 Jockusch paper was not available in the inspected lawful path; older implicit coverage remains possible.
- The cone base is \(\deg_T(R)\), not necessarily \(\deg_T(A)\), and no effective bound for obtaining the decoder from an arbitrary presentation of \(A\) is claimed.

The audit distinguishes finite reproducibility checks from proofs of infinite statements and makes no claim beyond the final claim above.
