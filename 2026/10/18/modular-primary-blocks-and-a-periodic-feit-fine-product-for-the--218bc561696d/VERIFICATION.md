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

Run the included standalone Python 3 program using `python verify.py`. It implements finite-field linear elimination and computes each affine \(X\)-fiber without relying on the Euler-product calculation. It exhaustively enumerates \(Y\) in matrix sizes up to three for prime fields \(\mathbb F_2\) and \(\mathbb F_3\), and size two over the nonprime field \(\mathbb F_4\). It compares the counts with the independent partition expression derived in the theorem.

Expected `VERIFY_OK` output includes exactly \(N_1(2)=2\), \(N_2(2)=40\), \(N_2(3)=153\), \(N_3(2)=2192\), \(N_3(3)=95499\), and \(N_2(4)=1216\). The nonnilpotent contributions for \(n=p\) are \(12\) at \(q=2\) and \(33696\) at \(q=3\).

These finite computations corroborate the proof's count and characteristic boundary. They do not check infinitely many matrix sizes, do not prove algebraic-geometric scheme reducedness, and do not constitute an independent mathematical audit.
