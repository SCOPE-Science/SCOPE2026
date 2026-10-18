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

The analytic proof reduces every exponent to a finite search using \(m\le\max\{k,\lfloor(2^k-2)/k\rfloor\}\). Execute `python3 CHECKER.py`; its two exact-integer algorithms agree for each of nineteen exponents and return five quadruples. The test uses modular inverse arithmetic and a separate congruence progression to detect all bounded solutions, and it replays the original power identity for each. Runtime observations are not the proof of the infinite cutoff; the binomial-congruence argument is.

The classification is only for \(2\le k\le20\). No independent audit has yet been performed.
