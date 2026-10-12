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

Use `python3 verify.py` with a standard Python 3 interpreter in this directory. No external packages or files are required. The verifier reconstructs the seeded local jump matrices and checks two exact nonzero determinants and one exact minor: \(\det B_{3,2}=-1\), \(\det B_{5,3}=-1\), and a four-by-four minor of \(B_{4,3}\) of determinant \(+1\). It independently builds the full and no-`111` four-excitation jump matrices for \(7\le n\le12\) and computes their ranks modulo the two primes 1000003 and 1000033.

The executed script returned `VERIFY_OK`; the full/no-triple dark dimensions were (5,4), (19,16), (47,41), (95,85), (170,155), and (280,259) for lengths seven through twelve, respectively. The differences are 1, 3, 6, 10, 15, 21, agreeing with the closed formula. Modular finite tests cannot establish an infinite theorem or prove absence of prior literature. The all-length claim relies on the explicit block induction and disjoint-image word count in `RESULT.md`. The three small determinant/minor computations use exact integer arithmetic.

No external or independent audit was performed.
