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

# Reproduction and limits

Run `python verify_exhaustive.py` and `python verify_symbolic_families.py` using Python 3.10 or later, standard library only. Both should print `VERIFY_OK`; full expected output is in `verify_exhaustive.txt` and `verify_symbolic_families.txt`.

`verify_exhaustive.py` independently constructs all size-\(\lceil n/2\rceil-1\) Schur-free subsets for \(13\le n\le29\), all one-swap adjacencies, and their connected components. `verify_symbolic_families.py` separately constructs the proof's candidate families and verifies sum-freeness, cardinalities, all intersection-based edges and component formulas across odd sizes \(15\le n<100\) and even sizes \(20\le n\le100\). The second program is not a proof that the families exhaust all possible sets; that exhaustion is established mathematically using [1, Theorem 1.1]. Finite tests are corroborating checks only. All references in this document are to files included in the same research package.

The two first-failure examples \(n=13\) and \(n=18\) are exhaustively checked. No claim about smaller parameters or other exchange operations is made.
