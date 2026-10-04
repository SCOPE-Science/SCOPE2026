# Review of “Exact covariance defect in the multigrade EAIE”

## Correctness
**PASS.** Definition 2.1 of DOI 10.3934/math.2025671 expresses the EAIE as a step-grade increment plus a common balance using the grand value and only the highest-grade increment of each factor. The paper's COTR transformation adds all lower and upper grade shifts to the grand value. Substitution therefore leaves the exact common residual
\[
\frac1{{|F|}}\sum_{{j\in F}}\sum_{{q=1}}^{{d_j-1}}\zeta_{{j,q}},
\]
which the printed proof omits. The explicit \(d=(2,1)\) witness gives EAIE shift \((3/2,1/2,1/2)\) instead of \((1,0,0)\). The proof is algebraic and the packaged checker uses exact rationals.

## Originality
**PASS.** The main publisher PDF was inspected at Definition 2.1, the COTR definition, Lemma 3.4, Theorem 3.9, and the worked Section 5 formula. The source states the opposite of the finding and its Lemma 3.4 proof drops the lower-grade terms. Exact-title, DOI, lemma-name, correction/corrigendum, and semantic searches found no public correction. published-finding corpus searches for the EAIE/COTR claim returned no matching game-theory finding, and the current ledger has no EAIE, multichoice, or source-DOI overlap.

The closest structural predecessor inspected was Chen–Huang–Liao (2021), DOI 10.3390/catal11030345. Its MLII balance subtracts individual-level distinctions across all activity grades, so additive grade shifts cancel in the balance; it does not state or imply the 2025 EAIE covariance defect. The 2008 maximal-EANSC paper was identified as background, but its full text was not needed to resolve the source-specific contradiction between the 2025 definition and its own axiom.

## Value
**PASS.** COTR is one of the paper's advertised fairness axioms, and Theorem 3.9 characterizes the EAIE using COTR. The defect occurs precisely in genuine multigrade models, the setting introduced to extend flat participation. The result supplies a complete boundary—universal covariance holds exactly when all positive-grade counts are one—and a minimal exact counterexample. This is a structural failure of a central characterization, not a numerical rounding issue or a merely cosmetic notation error.

## Closest literature and limitations
The 2021 MLII is the closest formula-level predecessor and helps localize why the 2025 balance fails: the earlier rule sums all grade-level distinctions, whereas the EAIE balance uses only top-step distinctions. No claim is made that other axioms or the dynamic theorem fail independently. A later unindexed correction could exist; no such correction appeared in the searched public sources.

Same-model review: passed. Independent audit: not yet performed.
