# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260920-6bbca663bfa1`

## Correctness — PASS

The symbolic argument closes. For the boundary join, the total positive imbalance sum is \(S=J+mA\). Every positive imbalance is at most the deviation sum \(A\), and the maximum positive imbalance \(D\) is at most \(m\). If \(D\le m-1\), then \(S\ge mD\ge D(D+1)\); if \(D=m\), either an internal edge contributes at least \(m\) to \(J\), or the only remaining cross-edge case reduces to \(m=D=1\) and parity supplies \(S\ge2\). The total imbalance sum is always even. The stated Erdős–Gallai lemma therefore makes the positive multiset graphic, and zeros may be reattached as isolated vertices. The complete atlas verifier agrees for all graphs through order seven and finds the unique known order-four obstruction; this finite check is corroborative only.

### Correctness sources

- assigned RESULT.md
- Kozerenko–Serdiuk 2023 full paper
- artifacts/verify.py and verification.txt
- Erdős–Gallai criterion

### Correctness risks

- The theorem fixes only the one-step boundary and not each graph's optimal smaller join threshold.

## Originality — PASS

The 2023 primary paper was inspected in full around Theorem 3.7 and the paragraph immediately following it. It proves the older threshold, gives the order-four one-step-lower counterexample, and explicitly asks whether analogous counterexamples exist for arbitrary order. The audited theorem answers that question negatively for every order at least five. Current semantic search returned no later theorem resolving this exact boundary; the recent positive-imbalance results do not apply to joins containing zero-imbalance edges.

### equivalent_formulations

Searches:
- Resultary query: imbalance graphic empty join one-step threshold n max delta Kozerenko Serdiuk
- Kozerenko–Serdiuk 2023 Theorem 3.7 and following question
- exact boundary searches

Evidence:
- The source threshold is one larger.
- The source explicitly raises the arbitrary-order existence question at the one-step-lower boundary.

Reasoning:
Equivalent formulations via empty joins, the exact threshold, and graphicality of the edge-imbalance multiset were compared.

### broader_coverage

Searches:
- 2026 positive-imbalance conjecture papers
- 2026 regular-block imbalance work

Evidence:
- Those broader-looking results use hypotheses that do not cover arbitrary joined graphs with zero-imbalance edges.
- No exact one-step-boundary theorem was located.

Reasoning:
The inspected broader coverage does not imply this theorem.

### exact_database_or_table

Searches:
- current Resultary imbalance records
- graph-atlas verification

Evidence:
- The atlas is finite supporting evidence, not a database proof of the infinite theorem.
- No exact known-threshold table covering every order was located.

Reasoning:
The theorem rests on Erdős–Gallai, not enumeration.

### claim_vs_prior_implication

Searches:
- Kozerenko–Serdiuk Theorem 3.7 versus audited threshold

Evidence:
- The prior theorem assumes one more independent-set vertex; the order-four example shows that simply dropping one is not a formal consequence for all orders.
- The new sum-versus-maximum argument uses the order-at-least-five boundary to exclude the exceptional cross-edge case.

Reasoning:
The claim is a strict strengthening rather than a restatement.

### source_inspections

- **New results on imbalance graphic graphs** — https://doi.org/10.7494/OpMath.2023.43.1.81. Trigger: Primary source of the bound and open question. Material read: Complete published PDF, especially Theorem 3.7 and the following counterexample/question. Method: Primary full-text theorem and question comparison. Assessment: The source poses the exact boundary question resolved here. Evidence: It proves the threshold with one more empty-join vertex and exhibits the four-vertex failure one step lower.
- **A Proof of the Imbalance Conjecture** — https://arxiv.org/abs/2608.09191. Trigger: Recent broad imbalance-graphicness result. Material read: Accessible theorem scope and hypotheses. Method: Hypothesis comparison. Assessment: Not covering the arbitrary join theorem. Evidence: Its positive-imbalance hypothesis need not hold for the audited joins.
- **Assigned graph-atlas verifier** — artifacts/verify.py. Trigger: Finite sanity check. Material read: Complete source and deterministic output. Method: Line-by-line inspection. Assessment: Correct corroboration only. Evidence: It reports zero failures at orders five through seven and the unique known order-four failure.

### checked_sources

- Kozerenko–Serdiuk 2023 full PDF
- current Resultary exact-boundary search
- arXiv:2608.09191
- assigned exact verifier

### residual_risks

- Unindexed or inaccessible later work could contain the same boundary theorem, but no specific plausible covering source was identified.

## Scientific value — PASS

The result resolves a concrete published question and strictly improves a universal sufficient bound for every graph from order five onward. The proof also packages a useful even-sum/max-entry graphicality lemma that explains why the four-vertex example is exceptional at this boundary.

### Value sources

- Kozerenko–Serdiuk 2023 open question
- audited Erdős–Gallai proof

### Value risks

- The optimal threshold below this boundary remains graph-dependent and open.

## Limitations

- The theorem improves the universal bound by exactly one.
- It does not determine graph-specific optimal thresholds.
- Finite atlas verification is supporting evidence only.
- Originality is best-of-knowledge.

## Disposition

**PASSED**
