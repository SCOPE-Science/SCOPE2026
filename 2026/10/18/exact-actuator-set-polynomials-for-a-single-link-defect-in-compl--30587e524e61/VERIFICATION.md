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

# Verification of the actuator-set theorem

The independent finite-instance checker is `verify.py` and uses only the Python 3 standard library. Run from the same directory with `python3 verify.py`. It performs exact modular Gaussian elimination on a Kalman matrix for every input subset, for each of two distinct large primes. It does not merely diagonalize the quotient matrix used in the proof.

Tested part sizes: \((p,q)=(3,3),(3,4),(4,4),(4,5),(5,5)\). Tested exceptional conductances: \(c=0,1/2,1,2,5/2\). Both primes are used independently; the complete rank truth table is checked against the proposed if-and-only-if criteria. The completed execution printed `VERIFY_OK 19840 individual truth-table entries over two primes`, and the recorded minimum actuator counts and minimum-placement counts agreed with the closed forms in all instances. A full-rank modular witness proves full rank over the rationals for these inputs; failure of modular rank alone would not prove rational noncontrollability, so the finite checker is corroboration rather than the infinite proof.

The analytical proof in `RESULT.md` supplies the noncomputational argument for all integers \(p,q\ge3\) and every real \(c\ge0\). In particular, the exceptional eigenvalue collisions are treated separately at \(p=q\) and \(c=1\). The checker does not quantify controllability Gramian conditioning or control energy near \(c=1\).
