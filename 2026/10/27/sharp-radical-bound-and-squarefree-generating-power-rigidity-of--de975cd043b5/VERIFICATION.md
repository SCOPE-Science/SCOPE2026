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

# Reproducible checks
Run `python3 VERIFY.py` using Python 3 with no third-party packages. The checker constructs an order from CRT digits and compares entire finite left-right signature matrices for every cyclic modulus from \(2\) to \(80\). It independently iterates all \(5913\) oriented cyclic permutations at sizes \(2\) through \(8\) and verifies the universal upper bound and existence of equality at each size. The execution printed `PASS: 5992 exact finite checks; 5913 oriented cycles exhaustively classified (n=2..8)`.

The proof is symbolic and applies for every integer \(n\ge2\). Finite testing is neither an exhaustive check for unbounded sizes nor evidence of bibliographic novelty. No formal proof assistant, external expert review, or independent audit has been performed.
