---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the stated zero-indexed substitution fixed point, p_2j=0 and p_(2j+1)=1−p_j imply p_i=v₂(i+1) mod 2. For every m=2^r, positions within each aligned m-sector have valuation parity independent of the sector except at its last position. An arbitrary consecutive length-m window shifted by a fixed residue has exactly one sector-end symbol; all other letters depend only on that residue. Thus at most two distinct length-m blocks occur in the triple at every starting index, including r=0. An independent valuation-sector reconstruction (/workspace/review-evidence/antipower.py) exhausts the length-15 windows of all three legal consecutive aligned 16-sector pairs, 00,01,10; all pairs are realized and two sectors suffice for any window. It matches the 23 frozen CSV rows, 115 tests and minimum column, yields 14 length-9 prefixes and only the three stated failures, and confirms all four exceptional length-15 extensions pass the length-five test. Hence the least lengths are 3 and 5 (only 1,2,4 could compete); start zero requires 5. Inverting the source-derived parity entries gives precisely the stated even and odd exceptions. Ones have density 1/3 by summing the dyadic residue classes (the neglected tail is bounded by a dyadic-multiple density); no 11 makes 00,01,10 each frequency 1/3. The parity identities give 0100 and 0010 each frequency 1/6 and 00100 frequency 1/12, whence 5/24 and complement 19/24. This establishes natural densities, not estimates from sampled prefixes. Frozen proof, certificate and script were read; the uploaded script was not executed.

## originality

PASS

General existence and linear radius bounds are prior. The supported distinction is the exact local least-length classification and natural densities, together with the all-index dyadic exclusion for this particular word. The strongest matching available claims address different words, different block predicates, or much coarser conclusions.

## value

PASS

This is a sharp uniform-start result for a standard automatic word, not a chosen prefix cutoff. It resolves the local obstruction at exactly identified positions with positive density and shows that an infinite family of natural scales can never work, even though each position has a short witness. The finding is limited to order three and does not classify nondyadic lengths past the minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
