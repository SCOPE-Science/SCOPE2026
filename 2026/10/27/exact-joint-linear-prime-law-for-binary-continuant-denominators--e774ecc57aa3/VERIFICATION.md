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

# Verification of the exact two-linear-prime continuant law

The accompanying `verify.py` requires Python 3 standard library only. Run `python3 verify.py` from the directory containing the packaged files. Its expected terminal report is:

`VERIFY_OK transfer_dimension=9 annihilator_degree=4 matrix_degrees=100 direct_words_through=14`

The program constructs the integer nine-state transfer matrix directly from the characteristic-two two-point continuant recursion, checks its state space and transition multiplicities, and checks the exact **vector** identity \(v_4=v_3+2v_1+4v_0\). That identity implies the claimed all-degree fourth-order recurrence by multiplication with powers of the same matrix; no induction hypothesis depends on enumerated large degrees. It also checks the closed formulas for both marginals and the joint count for every degree from zero through 99.

Independently of state propagation, the program enumerates every ordered word of lengths zero through 14, computes complete continuant polynomials using binary bitwise polynomial operations, evaluates each at zero and one, and compares all four joint classes with the formulas. The code's first calculation proves the matrix identity for the given nine-state transitions; the second provides bounded corroboration. Neither a sampled experiment nor a run with a time limit is used as a substitute for an infinite proof.

The analytical argument is in `RESULT.md`, including the degree conventions, initial states, vector values, recurrence, generating function, marginal derivation, covariance and normalization. The claim concerns the distribution induced by *uniform words*, equivalently orthogonal-multiplicity-weighted denominators. It does not concern uniform monic denominators, density of positive-multiplicity polynomials, or nonlinear prime-factor independence. Independent validation has not occurred.
