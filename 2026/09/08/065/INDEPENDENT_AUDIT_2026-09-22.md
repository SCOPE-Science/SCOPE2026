# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/065`  
**Audit date (UTC):** 2026-09-24  
**Reviewer:** separate AI audit; not Lean verification or expert attestation.

## Source identity and claim

Audited source tree: `e0264015cfba3236cbb84a5f8cebd568d2c24c64`.  
Audited `RESULT.md` blob: `762c4a24dc4e881293f13e3860db2abfa5a6055e`.

The record extends Sprague–Grundy tables for octal games `.13337` and `.13137` from the published 10,000-value frontier to n=12,000, certifies a finite non-periodicity box `q<=8000, p<=2000`, and records cold/extremal values.

## Correctness — PASS

I independently implemented the octal recursion directly from the digit bits and mex definition, without reading the committed generated tables. Computing both games through n=12,000 reproduced the record's new samples exactly:
- `.13337`, n=10001..10010: `65,46,40,132,64,42,128,68,11,102`;
- `.13137`: `28,64,142,16,86,34,67,145,25,83`.

The independently computed cold positions exactly matched both published lists. The `.13337` maximum through 12,000 is 187 (attained at n=10736 and also later at 11721); the record only claims a new record at n=10736, not uniqueness. `.13137` has global maximum 229 at n=7310 (also later at 7773), and the maximum in the new interval is 222 at n=11579, as stated.

I also independently scanned every `q=0..8000` and `p=1..2000` against the computed sequences. No candidate closes within the table. The latest first failure for `.13337` is n=8002 at `(q,p)=(7999,348)`, with `G(8002)=131 != G(8350)=128`; for `.13137` it is n=8001 at `(8000,125)`, with `94 != 174`. These reproduce the headline finite certificate.

## Originality — PASS to the best of the checked literature

OEIS A071448 identifies `.13137` and links a table only through n=10,000; the adjacent A071449 is the corresponding `.13337` sequence and the record's OEIS gate is consistent with that published frontier. The OEIS comments also identify the dependent shifted games. Achim Flammenkamp's octal-game hub states that its systematic tabulation covers at-most-three-place `0.???`/`4.???` games plus specified special families; these five-digit games are outside that census.

Searches for the exact game codes, new extrema, and candidate-period box found no prior 12,000-value table or equivalent non-closure certificate. The novelty conclusion is limited to the evidence checked.

## Scientific value — PASS

This is finite computation, but it is tied to a recognized unresolved octal-game classification program rather than an arbitrary parameter sweep. It advances the public exact-value frontier by 20% for two named five-digit games, supplies explicit falsifying witnesses for every period/preperiod candidate in a 16,002,000-pair box per game, finds a new cold position for `.13137`, and raises the known `.13337` nimber record. These facts directly constrain future periodicity/sparse-space investigations and provide reproducible test data.

## Disposition

**PASSED.** All three axes pass relative to the checked literature. No repair was needed.

## Access notes

The decisive prior-data comparison used ordinary lawful public sources (OEIS and Flammenkamp). No inaccessible paper was needed for the novelty decision, so Oxford fallback was not required.
