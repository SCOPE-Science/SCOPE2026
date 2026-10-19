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
# Exact reproducibility and limits

Run `python3 verify.py` with Python 3 and no nonstandard dependencies. The checker reconstructs the six excluded five-bit words from the local commutation equation, generates the sixteen-state transfer matrix, and computes its characteristic polynomial with the integer Faddeev–LeVerrier algorithm (checking exact divisions). It compares traces against direct application of the two staggered layers to all \(2^L\) initial states for even \(4\le L\le16\); it also computes \(L=18\) by exact matrix multiplication and verifies the Lucas fixed-point correction.

All-size correctness rests on the proof in `RESULT.md`: the equivalence \(F^2(x)=x\iff OE(x)=EO(x)\), a fully specified five-bit truth table, and a closed-walk/cyclic-word bijection. Finite checks validate implementation and small boundary cases but do not independently establish infinitely many ring sizes. The asymptotic uses an algebraic cubic root separation, not a floating-point claim of root ordering. The checked prior articles establish model context, not originality by themselves. No independent external scientific audit has been performed.
