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

The proof is an exact Lie-derivative calculation. The bundled `verify.py` constructs the polynomial vector field and observable over exact rational coefficients in ten formal indeterminates, computes the Lie derivative term by term, and compares it with the claimed target polynomial. It also checks the exact rational specialization \(b=7/10\), \(c+f=99/50\), and \(g=23/20\), yielding coefficients \(35/99\) and \(115/198\).

Replay command from the directory containing the file:

`python3 verify.py`

Expected terminal line: `VERIFY_OK`.

The checker does not integrate trajectories and does not establish attractor existence, chaos, ergodicity, or convergence of arbitrary time averages. Those are outside the claim.
