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

The accompanying `verify.py` uses only the Python standard library. Execute `python3 verify.py`. It checks the direct Lie-endomorphism and idempotence equations over three small prime fields in dimension three, all \(2^{16}\) binary \(4\times4\) candidate projection matrices and their admissible functional counts in dimension five, and the dimension maximization finite-difference relation for \(1\leq n<30\). It prints `HEISENBERG_RETRACTIONS_OK` on success.

Observed profiles: dimension three over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\): ranks \(0,1,3\) occur \((1,12,1)\), \((1,36,1)\), \((1,150,1)\) times. Dimension five over \(\mathbb F_2\): proper ranks \(0,1,2\) occur \((1,240,960)\) times, with one additional identity. The rank-two test enumerates candidate quotient matrices exhaustively and counts all allowed central functionals via the proved \(2^r\) factor; it does not separately enumerate every full endomorphism matrix.

These computations are finite consistency tests. Scheme smoothness, irreducibility in arbitrary characteristic, and the infinite family of counting formulas rely on the human-readable proof in `RESULT.md`; they are not independently certified here.
