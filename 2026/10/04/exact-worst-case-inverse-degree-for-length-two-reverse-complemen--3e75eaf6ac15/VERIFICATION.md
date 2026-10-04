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
# Verification

The universal theorem is established by the symbolic proof in `RESULT.md`. The executable check is supplementary.

`verify.py` uses two independently written descriptions of the one-error channel: a forward map that enumerates every source and every duplication start, and an inverse parser that recognizes received-word blocks satisfying the reverse-complement condition and deletes the inserted pair. It asserts equality of the resulting parent sets for every received word in twelve exhaustive parameter cases: \(q=2\) with \(2\le n\le8\), \(q=4\) with \(2\le n\le4\), and \(q=6\) with \(2\le n\le3\).

For every exhaustive case it also computes the maximum inverse degree, checks that it equals \(\lfloor n/2\rfloor\), verifies that adjacent valid starts yield the same parent, and checks the proposed period-four extremal construction. The construction is additionally checked for \(q\in\{2,4,6,8,10\}\) and every \(2\le n\le100\).

A successful replay is:

`python3 verify.py`

with terminal line:

`VERIFY_OK exhaustive_cases=12 construction_q<=10_n<=100`

Finite exhaustive checks do not prove the theorem for unbounded \(q\) and \(n\); they test the model, boundary cases, and algebraic conclusion. No independent audit or external validation has been performed.
