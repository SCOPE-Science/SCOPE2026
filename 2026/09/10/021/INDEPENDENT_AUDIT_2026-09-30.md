# Independent audit — 2026-09-30

**Record:** `SCOPE-20260910-021`

## Correctness — PASS

A fresh computation from the divided-difference definitions reproduced S_2143 at y=1, the seven-term reflected polynomial, each of the five required Lascoux atoms, and exact zero residual for the stated graded combination. The lowest total degree is 14 and the coefficients 1,1,1,2,1 have the required alternating degree signs. This independently reproduces the committed checker without trusting its saved success output.

## Originality — PASS

Setiabrata–St. Dizier prove the reflected Lascoux-positivity statement for vexillary permutations and state it as Conjecture 1.4 for every permutation. Their full v2 text contains no occurrence of 2143, and exact searches did not locate the five-term expansion elsewhere. Since 2143 is the minimal non-vexillary permutation, the exact verified base case is outside the proved domain and is not implied by the cited theorem.

### Structured originality checks

- **equivalent_formulations:** Checked the reflected double-Schubert formulation and the graded Lascoux expansion formulation used in Conjecture 1.4; the record matches the conjecture's specialization to w=2143.
- **broader_coverage:** The primary paper proves the statement for all vexillary permutations and conjectures all permutations, but 2143 is itself the forbidden minimal pattern and lies just outside the theorem.
- **exact_database_or_table:** Semantic published-findings search and exact web searches for 2143 with Lascoux/reflected Schubert terms returned this record as the exact expansion and no prior table with these coefficients.
- **claim_vs_prior_implication:** A conjecture is not prior coverage. The proved vexillary theorem cannot be specialized to 2143 because 2143 is non-vexillary; no inspected result implies this base case.

## Scientific value — PASS

This is a natural minimal boundary case of an explicit current conjecture, not an arbitrary small example. The exact expansion gives a regression datum for future proofs or counterexample searches immediately beyond the established vexillary region, while making no claim about the full conjecture.

## Source inspections

- **Setiabrata–St. Dizier, Double orthodontia formulas and Lascoux positivity** — Full HTML, including Theorem 1.2, Corollary 1.3 and Conjecture 1.4; full-text search for 2143 returned no occurrence. The proved result covers vexillary permutations; Conjecture 1.4 asks for all permutations, leaving 2143 outside the proved domain. https://arxiv.org/html/2410.08038v2
- **Published-findings semantic search** — Top ten semantically related published findings. Only this record matched the exact reflected 2143 expansion. https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE021

## Residual risks

- The result is only one minimal finite case and does not establish any broader non-vexillary family.
- No exhaustive search of unpublished computational notebooks is possible; the originality conclusion concerns accessible published literature and indexed published findings.

## Disposition

**PASSED**. The final claim passes correctness, originality, and scientific value.
