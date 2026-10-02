# Independent audit — 2026-09-30

**Record:** `SCOPE-20260910-022`

## Correctness — PASS

Fresh reconstruction of the five named Steiner systems gives 7,12,26,35,57 blocks and independently enumerates exactly 28,72,260,420,912 sails. The committed witnesses cover every block of the named systems through order 15 and the verifier checks zero monochromatic sails. For the named cyclic STS(19), the archived instance has 57 variables and 1824 clauses; a fresh replay of all 6632 trace events validated every decision, forced unit, conflict and backtrack and ended with the closed-tree identity 277 conflicts = 552/2 + 1. This certifies UNSAT for the exact NAE formulation and hence sail forcing in that named system.

## Originality — PASS

Granath et al. explicitly identify the sail as the sole unresolved unavoidable configuration with at most four blocks for 2-Ramsey status, and Sárközy's later paper still describes the Ramsey property of the sail as a main open problem while giving partial progress. The record does not claim to solve that global problem; it gives a finite named-system forcing certificate and lower-order witnesses. Searches for the exact cyclic STS(19) base blocks together with sail coloring/Ramsey terms found no prior certificate or table.

### Structured originality checks

- **equivalent_formulations:** Checked monochromatic-sail avoidance against the equivalent NAE-4-SAT encoding on the four block variables of each sail.
- **broader_coverage:** The primary literature addresses eventual Ramsey properties over all sufficiently large Steiner triple systems and asymmetric progress; it does not cover this exact named-system finite threshold.
- **exact_database_or_table:** Searches for the exact cyclic bases (0,1,4), (0,2,9), (0,5,11) combined with sail/C15/coloring terminology and the published-findings database found no prior matching finite certificate.
- **claim_vs_prior_implication:** The global open-problem literature neither implies that this specific STS(19) is sail-Ramsey nor supplies the four lower-order sail-free colorings; the finite results require the explicit census and SAT certificate.

## Scientific value — PASS

A certified forcing instance at order 19 paired with explicit sail-free witnesses through the canonical named order-15 system is a meaningful finite boundary datum for an acknowledged open Ramsey problem. It is carefully limited to one named STS(19), so its value is as an exact benchmark and structural test case rather than as a solution of the eventual 2-Ramsey question.

## Source inspections

- **Granath et al., Ramsey theory on Steiner triples** — Full accessible primary PDF; the introduction and page 3 explicitly isolate the sail as the remaining undecided small 2-Ramsey configuration. Establishes the motivation and open-problem boundary but contains no named cyclic STS(19) forcing certificate. https://real.mtak.hu/71057/1/jcdramseyrev2.pdf
- **Sárközy, Turan and Ramsey numbers in linear triple systems II** — Repository metadata and abstract; the direct PDF fetch timed out during this run. The abstract states that the Ramsey property of the sail remains one of the main open problems and that the paper provides partial progress. https://real.mtak.hu/162638/
- **Published-findings semantic search** — Top semantically related published findings. No earlier exact sail-coloring certificate for this named STS(19) was returned. https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE022

## Residual risks

- The 2023 Sárközy full PDF was not successfully fetched in this run; its repository abstract was read, while the earlier Granath paper was inspected in full. This access gap is disclosed and does not supply contrary coverage.
- The result says nothing about non-cyclic STS(19) or eventual 2-Ramsey behavior.
- The committed RESULT.md names output/artifacts paths, while the audited tree stores the verifier material under artifacts/. This is a reproducibility-path documentation defect, not a defect in the finite certificate.

## Disposition

**PASSED**. The final claim passes correctness, originality, and scientific value.
