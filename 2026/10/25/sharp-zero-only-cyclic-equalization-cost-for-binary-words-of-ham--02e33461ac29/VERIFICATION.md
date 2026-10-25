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

Run `python3 verify.py` using standard Python 3 (standard library only). It prints a histogram for each tested length and finishes with `VERIFY_OK`.

The check uses (a) the interval formula and (b) for all ordered pairs of length-\(n\) words of Hamming weight two with \(3\le n\le8\), direct enumeration of every common zero-gap vector of total length from zero through the formula optimum, literal construction of the resulting words, and an explicit cyclic-string containment test. It confirms that no smaller padding works and that the asserted optimum does.

For \(3\le n\le12\) the code also counts all ordered pairs by the proved closed formula. The last-bin count for every \(4\le n\le12\) is \(4n\). For \(4\le n\le100\) the canonical strictly nested witness has formula cost \(n-3\).

At length \(8\), the complete cost histogram for costs \(0,1,2,3,4,5\) is \(208,256,144,96,48,32\), summing to the \(\binom82^2=784\) ordered pairs. The general mathematical proof is in `RESULT.md`; no finite test establishes the all-length theorem independently. No external or human validation has been performed.
