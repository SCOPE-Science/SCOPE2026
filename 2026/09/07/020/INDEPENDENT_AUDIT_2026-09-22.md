# Independent audit — 2026-09-22 campaign

Record: SCOPE-20260907-020
Source: 2026/09/07/020
RESULT.md blob: e88dea1f8c3a9fc67dcf3d62e4b13a7b4bdf6e60
Review date: 2026-09-23 UTC
Reviewer: separate AI independent audit.

## Correctness — PASS

A fresh reconstruction of AG(3,3) and PG(3,3) produced 27/117 and 40/130 point/line counts. An independently written recursive cap enumerator reproduced the complete-cap census containing point 0 exactly: AG has 13,104 complete 8-caps and 702 complete 9-caps; PG has 113,724 complete 8-caps and 2,106 complete 10-caps, with no complete 9-cap. The computational claims reproduce.

## Originality — FAIL

Faina, Marcugini, Milani and Pambianco, Ars Combinatoria 50 (1998), 235-243, already give the full catalog of complete-cap sizes in PG(3,q) for q<=5; publisher archive: https://combinatorialpress.com/ars-articles/volume-050-ars-articles/ . The q=3 projective spectrum and maximum 10 are therefore prior art. The AG(3,3) maximum 9 is classical, and complete nonmaximum 8-caps are longstanding. The remaining point-0 labeled counts are a routine exhaustive census, not a new structural classification.

## Scientific value — FAIL

After subtracting the known maxima and spectra, the surviving labeled counts do not provide orbit classification, stabilizer data, a new theorem, or an algorithmic advance. They are useful regression data but do not meet the campaign's scientific-value threshold.

## Final disposition

FAILED: correctness passed; originality and scientific value failed.
