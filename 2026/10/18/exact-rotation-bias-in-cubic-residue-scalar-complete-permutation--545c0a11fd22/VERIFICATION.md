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

The standalone `verify.py` executes with Python 3 standard library only. Command: `python3 verify.py`. The observed terminal marker is `VERIFY_OK`.

Eight exact finite-field tests: \(q\in\{19,37,64,73,109,127,163,199\}\). For each, checks include (1) primality-order properties of a multiplicative generator, (2) subgroup \(K\) and its characters, (3) the norm-\(q\) cubic Jacobi sum in the Eisenstein integer basis, (4) independent classification of the three local counts \(N_j\), (5) the exact global rotation and transposition totals, and (6) the strict Jacobi-norm difference. For the four smallest fields, **every** admissible ordered coefficient triple is tested by constructing both field maps on **all** field elements, independently of the character-class test. The characteristic-two example uses arithmetic modulo the irreducible polynomial \(X^6+X+1\) over \(\mathbb F_2\), and checks the multiplicative generator has order \(63\).

Sample exact totals \((q,N_0,N_1,N_2,R_q,T_q)\): \((19,2,1,2,17,12)\), \((37,2,5,4,197,120)\), \((64,8,6,6,944,864)\), and \((73,8,6,9,1457,1296)\).

This code only tests finitely many fields. The proof in `RESULT.md` covers all allowed prime powers and all positive exponents \(k\) via the fiber-bijection and Jacobi arguments. The asymptotic remainder is analytic and not verified by finite sampling. The bibliographically plausible 2013 earlier paper's full contents have not been read.
