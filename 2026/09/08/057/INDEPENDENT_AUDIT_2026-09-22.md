# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/057`  
**Audit date (UTC):** 2026-09-24  
**Reviewer:** separate AI audit. This is not Lean verification or expert attestation.

## Source identity and claim

The audited source directory has tree SHA `d66a57b58e62455e487363668fc86104728c1fef`; the audited `RESULT.md` blob is `c7860a208916ffac68c31af696cb2794ea19f51f`.

The record claims a complete finite census of Diaconis–Sturmfels 2x2-move fiber-graph diameters for all ordered 3x3 margin pairs with entries 0..6 and all ordered 3x4 margin pairs with entries 0..4, including exact diameter histograms and extremal witnesses.

## Correctness — PASS

I reimplemented the computation independently from the committed scripts. The checker enumerated nonnegative integer tables from row/column margins, built the signed 2x2 rectangle moves directly from the definition, and ran BFS from every vertex of every fiber. It did not ingest the record's CSV diameter values.

The independent run obtained exactly 9,331 3x3 margin classes and 7,140 3x4 classes. For 3x3 the diameter histogram was
`0:445,1:969,2:1411,3:1668,4:1687,5:1383,6:889,7:489,8:241,9:102,10:37,11:9,12:1`.
The unique diameter-12 class was `r=c=(6,6,6)`, with fiber size 406. For 3x4 the histogram was
`0:296,1:840,2:1420,3:1714,4:1405,5:850,6:437,7:156,8:22`.
Exactly 22 classes had diameter 8; their size groups were 120 (4 classes), 255 (12), and 312 (6). The largest 3x4 fiber was `r=(4,4,4), c=(3,3,3,3)`, size 415, diameter 6. The stated witness `r=(4,4,4), c=(0,4,4,4)` had size 120 and diameter 8.

Boundary cases, including zero margins and singleton fibers, were included. No disconnected fiber was found. These results independently reproduce every headline numerical claim.

## Originality — PASS to the best of the checked literature

I searched the standard terminology rather than only the record title: `"contingency table fiber graph diameter Markov basis"`, `"3x3 contingency table Markov chain diameter"`, `"2x2 moves fiber diameter"`, and the exact extremal values. Diaconis–Sturmfels (1998, DOI 10.1214/aos/1030563990) supplies the foundational connectivity theorem for two-way fibers but not these diameter tables. Aoki's survey (arXiv:1607.07600) and Hara–Aoki–Takemura (arXiv:1109.0078) discuss Markov-basis MCMC and small models, not a complete diameter census. The Markov Bases Database records bases and related model metadata, not these per-margin graph diameters or shortest-path witnesses.

I did not find an earlier source containing the same complete bounded tables or the stated extrema. This is a qualified priority assessment, not a guarantee that no obscure table exists.

## Scientific value — PASS

After subtracting the classical connectivity theorem, the surviving contribution is an exact, reproducible benchmark for a natural graph invariant used in Markov-basis MCMC. The complete per-margin table, distributions, and extremal paths allow direct regression tests for fiber enumeration and MCMC implementations and give exact small-model distance scales; they are not implied by connectivity alone. The scope is finite, and the record correctly makes no general-diameter claim.

## Disposition

**PASSED.** Correctness, originality relative to the sources checked, and scientific value all pass. No repair was required.

## Access and reproducibility notes

All decisive literature used above was available through ordinary lawful web/arXiv access; no Oxford fallback was needed. The audit's independent recomputation used only the mathematical definitions in `RESULT.md`, not the prior `AUDIT.json` verdict. The historical audit was consulted only after the independent checks and does not serve as evidence for this disposition.
