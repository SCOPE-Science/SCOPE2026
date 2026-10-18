# Scientific review

## Correctness — PASS
The carry identity is derived from binary-column equations, so the event for a three-one shift is precisely at most three carries. A run of at least three zeros annihilates every still-relevant incoming carry, producing a rigorous universal sixteen-case reduction. The exact integer transfer is fully specified and the sixteen counts are independently checked by exhaustive residue enumeration in `verify.py`; this establishes the stated fractions for all admissible shifts, not merely tested shifts. The script was replayed and printed `VERIFY_OK`.

## Originality — PASS (qualified)
Drmota–Kauers–Spiegelhofer (arXiv:1509.08623) give a distributional recurrence and small-shift values; their inspected theorems do not give this all-gap classification. Spiegelhofer–Wallner (arXiv:2005.07167) prove an asymptotic many-block result. Cheng (arXiv:2606.23398) has already resolved the universal positivity question, and the later fixed-weight paper (arXiv:2608.25899) gives a large-weight asymptotic; neither accessible statement determines the five exact finite weight-three fractions and extremizers. The full text of the 2026 fixed-weight preprint was unavailable; a hidden finite-case corollary, or an unindexed earlier result, remains an originality risk. An independent literature audit may change this assessment.

## Value — PASS
The complete five-value spectrum and equality-classification answer a concrete, natural exact fixed-weight question. Weight three has two genuinely interacting gaps and is the first modest nontrivial phase diagram beyond single-gap elementary cases; the sharp minimum is substantially stronger than the existing uniform positivity bound. The gap-saturation lemma explains why arbitrarily distant set bits nevertheless produce only finitely many densities. This is a self-contained exact invariant, not an extrapolation of finite data.

## Evidence and limitations
All finite arithmetic is integer exact and reproducible with `python3 verify.py`. The proof needs the carry-truncation argument to cover unbounded gaps. No claim for weight four or higher, the full difference distribution, or new resolution of the general conjecture is made. The 2026 asymptotic fixed-weight paper could not be read in full; source coverage remains limited.

Self-review: passed. Independent audit: not yet performed.
