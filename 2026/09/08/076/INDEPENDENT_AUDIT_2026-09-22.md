# Independent Audit — 2026-09-22

Record: `2026/09/08/076`

## Scope and method

This independent audit checks correctness, originality, and scientific value for the record “Certified Rouché-disk zero table for exponential sections (s_n), (n \le 16), with Szegő-curve gap logs and extremal witnesses.”

The audit uses the committed record, its replayable verifier and exact-arithmetic evidence, together with literature comparison against the cited exponential-section literature. No inaccessible paper is represented here as having been read in full.

## Correctness — PASS

The central claims are supported by replayable and independently checked finite computations.

- The committed verifier reports 136 disks and verifies the Rouché inequalities at both radii (r=3/10) and (r=1/100), pairwise disjointness by degree, the maximal-real-part separation, and the Szegő-gap separation.
- The audit evidence records an independent exact-`Fraction` reconstruction of the inequalities (m=|a_1|r-|a_0|>M) and (|a_0|<|a_1|r) for all 136 disks at both radii.
- Exact disjointness plus one Rouché-counted zero per disk and exactly (n) disks for degree (n) accounts for all zeros of each (s_n), (1\le n\le16).
- The reported extremal separation is wide: the witness real-part lower bound is (7.716102197), while every competing disk has upper bound at most (6.984780933).
- The reported Szegő-gap witness interval has upper endpoint (0.161927324), while every competing disk has lower endpoint at least (0.170167940).

Residual risks are limited to non-headline implementation details noted in the existing audit: float ranking is used before an exact separation check, a side remark about real zeros is not separately certified, and the exponential remainder bound is terse. None overturns the finite headline claims.

**Correctness verdict: PASS.**

## Originality — PASS, finite-scope claim

The checked prior literature concerns the asymptotic location and limiting behavior of zeros of exponential partial sums, including the classical Szegő/Newman–Rivlin line of work and later expository/asymptotic treatments. The committed audit search found no prior source providing this same finite package: 136 per-zero disjoint rational Rouché disks for (1\le n\le16), replayable one-zero counts, whole-disk Szegő-gap enclosures, and the two stated finite-scope extremal witnesses.

The originality claim is therefore intentionally narrow: the record does **not** claim a new limit theorem or new asymptotic theory; it contributes a certified, replayable small-(n) table and associated finite extremals.

**Originality verdict: PASS within the stated finite scope.**

## Scientific value — PASS

The record turns commonly presented floating-point zero approximations into exact, replayable finite certificates. The isolation disks, count proofs, and extremal witnesses are useful as validation benchmarks for numerical root-finding, stability-region work, and experiments concerning the Szegő curve. The scope (n\le16) is modest, but the result is concrete, reproducible, and attached to a canonical object rather than an arbitrary parameter sweep.

**Scientific-value verdict: PASS.**

## Overall verdict

**PASS.** The record is correct within its stated finite scope, presents a narrowly defined certified-data contribution not identified in the checked prior literature, and has reproducibility/benchmark value.

## Evidence used

- `RESULT.md`
- `AUDIT.json`
- `artifacts/verify.py` and the committed disk/gap data described by the record
- Literature references and searches documented in the existing audit, including Newman–Rivlin (1972), Walker (2003), DLMF search results, and the internal SCOPE005 comparison

This file is one component of the repository’s independent-audit completion convention. The companion JSON audit file and the corresponding `VERIFICATION.md` evidence update are separate required changes.
