---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The provided `verify_square_word.py` performs exact, reproducible enumeration of the square map in \(UT_5(\mathbb F_q)\) and the complete iff predicate at \(q=2,4\), using bitwise polynomial multiplication for \(\mathbb F_4\) modulo the irreducible polynomial \(X^2+X+1\). It enumerates \(q^{10}\) roots and all \(q^6\) targets, checks the predicted image size, additionally checks the previously known two-square width and small-size surjectivity.

Reproduction command: `python verify_square_word.py`. Expected terminal marker: `VERIFY_OK`.

For \(q=2\), there are \(52\) distinct squares among \(64\) derived elements, and all \(64\) are products of two squares. For \(q=4\), there are \(3376\) distinct squares among \(4096\) derived elements, and all \(4096\) are products of two squares. Both fields satisfy the complete target-by-target criterion.

The universal finite-field membership and image-size statement relies on the displayed proof: explicit quadratic-coordinate equations, constructive sufficiency, and disjoint target strata. The already-known verbal width and threshold are not newly claimed. Finite computation is not a certificate for infinitely many finite fields; no independent audit was performed.

The particular image sizes at \(q=2\) and \(q=4\) also appear in Dolfi–Singh–Yadav (2019), Section 3 table, so they are not counted as new discoveries.
