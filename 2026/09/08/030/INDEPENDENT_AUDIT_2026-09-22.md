# Independent three-axis audit — 2026-09-23

Source: `2026/09/08/030`; audited source-tree SHA `507751a26aa19eae00ed4e9363e69bb426b48e64`; `RESULT.md` blob `33917fa3a5f8a7951547f38a3d68212c99dc6e5b`.

## Claim checked
For the one-pile normal-play subtraction game with `S={1,8,27,64,125}`, the record gives the exact cold-position and Sprague–Grundy census on `[0,200]`, proves eventual outcome period 7 beginning at 263 and SG period 7 beginning at 264, proves leastness, and gives exact maximum-nimber data.

## Correctness — passed
I independently recomputed the recurrence from the rules, without the record's verifier, through heap 8000. The cold list on `[0,200]` has 71 entries and matches exactly; the SG histogram is `{0:71,1:71,2:34,3:19,4:6}` and the SG-4 positions through 200 are `128,144,160,165,172,200`. The only later SG-4 is 263; the last SG-3 is 216. Exhaustive period search using the maximum-move certificate length 125 gives least outcome `(period,onset)=(7,263)` and least SG `(7,264)`. The stated cycles and last mismatches reproduce. The max-move induction is valid because one full predecessor-memory window propagates the recurrence.

## Originality — passed relative to checked literature
Searches used “subtract a cube”, “subtract cubes”, “cube subtraction game”, “Sprague-Grundy cubes”, the exact move set, and general periodicity terms. No prior cube-set SG period/census was found. The closest source, David Eppstein, *Faster Evaluation of Subtraction Games* (FUN 2018, arXiv:1804.06515), was inspected in full on arXiv: it develops general algorithms and experiments on subtract-a-square; perfect cubes occur only as plot sampling points, not as the subtraction set. This is an evidence-relative priority assessment, not a guarantee of absence.

## Scientific value — passed
The result is not merely a finite table: it gives a compact certificate of exact ultimate periodicity and least onset, together with a negative certificate that no 125-step period can be certified inside the original `[0,200]` window. The true onset beyond 200 is a useful benchmark for period-detection methods and guards against extrapolation from an insufficient cutoff.

No repair was needed. Eppstein's full text was OA; no Oxford fallback was needed. This is an independent AI audit, not a human/expert or Lean attestation.
