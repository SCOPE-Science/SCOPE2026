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

This result consists of a complete case classification of factors with zero, one, and two marked symbols; its maximization reduces to the integer optimization \(\max q(p+1)\) subject to \(0\le p\le q\) and \(p+2q\le n-2\). The proof in `RESULT.md` is the justification for every length.

Run `python3 verify.py` in this directory. It independently enumerates all factors and tests borders with occurrence counts; it checks the full factor sets and all maximizers for lengths \(2\)–\(16\), the arithmetic maximizers for lengths \(17\)–\(100\), and the zero/one-marker boundary through length \(34\).

The enumerations are finite cross-checks, not substitutes for the proof or evidence of unpublished priority. The available 2013 primary text was compared at its definitions, extremal theorem, and table. One relevant 2016 article was available only through its abstract, leaving a bounded literature-priority risk.
