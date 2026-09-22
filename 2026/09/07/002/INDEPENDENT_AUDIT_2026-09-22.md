# Independent audit — 2026-09-22

## Scope and source identity

Separate AI audit of `2026/09/07/002`, reviewed 2026-09-22 UTC. The audit began from repository commit `b491a8d1d4b639eb085a4c66fe4951ac3f344663` (after the separately published audit of record 001).

Source blobs: `RESULT.md` 762198c5feaaef9dadfc2e1a3e7df6fcd2f85f32; `METADATA.json` 2f2c0ce0c2466660c1b0998a423fb9bbd970a16e; prior `AUDIT.json` a0f905d054b3aefe2f80c557ec2b33225da9802c; prior `VERIFICATION.md` 00d9cbc212cfed64c344acdf724800e03d5a6a2e. Critical artifact blob: e40d015364e6031ef1a630555fd984239aa0e7d1.

Reviewed claim: For lazy simple random walk on the balanced spider S(k,L), the stated two-stage coupling has mean at most 3L^2, yields the stated restart tail and mixing bounds (including T0=32kL^2), and gives the stated centered exponential tail.

## Correctness — PASS

PASS. I re-derived the radial hitting equation E_a H_0=2a(2L-a), the cycle-lift alternating coupling and its L^2 meeting bound, and the synchronous post-radius coupling. The full-walk marginals are faithful, including leg resampling only on 0→1 moves. The uniform Markov-restart argument gives the claimed geometric tail; the centered-tail reduction is also valid. As an independent finite sanity check I built transition matrices for k=3,4,5 and L=1,…,5, verified detailed balance to numerical precision, and checked convergence at the claimed scale. No omitted L=1 boundary defect was found.

## Originality — PASS relative to checked evidence

PASS relative to checked evidence, narrowly. General results relating mixing to hitting times already give the L^2-order behavior on finite trees (including Peres–Sousi and Peres–Sauerwald–Sousi–Stauffer). I found no checked source giving this specific faithful two-stage balanced-spider coupling with these explicit constants and restart/centered-tail formulation. The audit therefore does not treat the L^2 mixing order itself as new.

## Scientific value — PASS

PASS, narrowly. The durable contribution is an elementary, explicit coupling/certificate with concrete constants and a reproducible simulation check; it is not a new asymptotic mixing law.

## Prior-art checks

1. Mixing times are hitting times of large sets — https://arxiv.org/abs/1108.0133 — General reversible-chain mixing/hitting equivalence; covers order-level context, not this explicit spider coupling.
2. Mixing times are hitting times of large sets: tree-related consequences / finite-tree mixing-hitting work — https://arxiv.org/abs/1412.8458 — Finite-tree results make L^2-order mixing unsurprising; no identical constant-level coupling located.
3. Markov Chains and Mixing Times — https://pages.uoregon.edu/dlevin/MARKOV/ — Standard coupling inequality and hitting-time tools used by the record.

The originality verdict means no substantive covering result was found in the checked evidence; it does **not** establish or award scholarly priority.

## Residual risks / limitations

- Novelty is only at the explicit construction/constants level; stronger and more general tree-mixing theorems already exist.
- Constants are deliberately loose; no lower bound or cutoff statement is established.

## Final disposition

- Correctness: **PASS**
- Originality: **PASS relative to checked evidence**
- Scientific value: **PASS**
- Disposition: **passed**.
