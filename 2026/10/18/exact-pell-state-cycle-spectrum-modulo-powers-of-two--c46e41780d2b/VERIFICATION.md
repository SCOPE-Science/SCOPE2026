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

# Reproduction and evidentiary scope

Run `python3 verify.py` using an ordinary Python 3 interpreter; no third-party package is needed. The program calculates the integer matrix powers and their two Smith invariant exponents, then exhaustively enumerates every state orbit modulo \(2^k\) for integers \(1\le k\le9\). It asserts exact cycle dictionaries, total state counts, and totals. An unmodified successful run prints `VERIFY_OK`.

The program's finite census certifies only the tested moduli. The all-\(k\) theorem follows instead from the explicit matrix recurrence and invertibility of \(I+2^{j-1}C_j\) modulo two. Those two proof steps are independently inspectable using the displayed integer matrices in `RESULT.md` and the usual Smith kernel-counting identity.

The literature comparison concerns exact all-seed state orbit multiplicities, not just a standard-seed Pell period or companion-matrix order. A self-review passed; independent audit has not been performed.
