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

The original proof is in `RESULT.md`. Run `python checker.py` using the Python 3 standard library; actual output from the package is reproduced in `checker_output.txt`. The checker creates the complete symbolic nine-letter superfamily by considering both possible bit values at every multiple of eight and checks 36 unique factors separated into eight disjoint start-residue classes. It also checks the eight dyadic endpoint classes and performs direct counts of lengths \(2^{n-4}\) and \(2^{n-4}+1\) in every prefix for \(6\le n\le12\), confirming exactly two singleton factors at starts \(11\cdot2^{n-4}\) and \(12\cdot2^{n-4}\). All indices used by the checker are positive and start positions are one-based.

The finite loops do not prove the infinite statement; the two-adic translation lemma, dyadic alignment induction, and endpoint classification in the written proof do. No external independent audit, external proof certification, or inaccessible source inspection is claimed.
