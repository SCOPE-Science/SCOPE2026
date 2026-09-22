# Independent audit — 2026-09-22

## Scope and source identity

Separate AI audit of `2026/09/07/009`, reviewed 2026-09-22 UTC. The audit began from repository commit `b491a8d1d4b639eb085a4c66fe4951ac3f344663` (after the separately published audit of record 001).

Source blobs: `RESULT.md` 86234c5e50103209a349b6efb77d8ba3d8ebde30; `METADATA.json` c0ab08af8926cca377446cce4bada84b0fe52433; prior `AUDIT.json` a2a5e9d95501cd34efdaf7c6e700ed8f08fe5a1d; prior `VERIFICATION.md` 83b03a7f246da30fad50fa39962dbb6d7f0519f0.

Reviewed claim: Among the 8-state quarter-grid birth–death chains in the stated stratum, the endpoint hitting time H=E_0 T_7 has unique rows-0–6 maximizer (modulo free row 7) with H=6544; the stated top-five values and periodic maximum are exact.

## Correctness — PASS

PASS for the exact census claim. I independently enumerated all 4·6^6=186,624 rows-0–6 patterns using exact rational recurrence d0=1/p0, di=(1+qi d_{i-1})/pi. This reproduced exactly 10,046 distinct H values, unique maximum 6544, top five 6544,5088,4608,4464,4358, and periodic maximum 3265. The analytic monotonicity argument also independently proves the left-drift maximizer. The record’s mixing bracket is explicitly numerical/empirical and is not promoted by this audit to theorem-grade evidence.

## Originality — PASS relative to checked evidence

PASS relative to checked evidence, very narrowly. The recurrence, monotonicity principle and extremizer shape are textbook birth–death material. Searches did not locate the exact denominator-restricted 8-state census/table or the number 6544 in this context. The audit therefore credits only the finite benchmark table, not a new method.

## Scientific value — PASS

PASS, very narrowly. The result is a small exact regression benchmark with a complete rational census; it is scientifically modest and unsurprising, but still independently reusable. The numerical mixing discussion is ancillary.

## Prior-art checks

1. Markov Chains and Mixing Times — https://pages.uoregon.edu/dlevin/MARKOV/ — Standard birth–death/hitting/mixing background.
2. Markov Chains, Cambridge notes — https://www.statslab.cam.ac.uk/~james/Markov/ — Standard hitting-time methods; no matching quarter-grid table located.
3. Reversible Markov Chains and Random Walks on Graphs — https://www.stat.berkeley.edu/~aldous/RWG/ChapURL.html — General reference, not a source of the finite census.

The originality verdict means no substantive covering result was found in the checked evidence; it does **not** establish or award scholarly priority.

## Residual risks / limitations

- Novelty and value are limited to the compiled finite table.
- The reported mixing upper near 21 is Monte Carlo, and the spectral numbers are numerical; neither is part of the exact theorem certified here.

## Final disposition

- Correctness: **PASS**
- Originality: **PASS relative to checked evidence**
- Scientific value: **PASS**
- Disposition: **passed**.
