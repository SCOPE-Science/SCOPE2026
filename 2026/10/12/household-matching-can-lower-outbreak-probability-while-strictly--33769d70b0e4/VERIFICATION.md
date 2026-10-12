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

# Verification of the household-matching theorem

Run `python3 verify.py` from this directory. The script checks with exact `Fraction` arithmetic each conditional partner-infection mixture, the displayed \(F_0\) and \(F_1\), the mean difference \(101/200\), both rational upper bounds at \(u=1/2\), and the polynomial difference lower bound \(3839/512\), together with the elementary rational bound on \(e^{4/5}\). The expected final line is `VERIFY_OK`.

An illustrative numerical bisection in the script reports approximate extinction roots \(q_0pprox0.092789\), \(q_{1/2}pprox0.113724\), and \(q_1pprox0.133811\); numerical roots are **not** the proof of the all-parameter result. The proof instead uses the strict polynomial inequality and uniqueness of the Galton–Watson extinction root. The passage from branching-process survival to probability of a major epidemic relies on Ball–Critcher (2026), electronic supplementary Theorem 9.1, for a single uniformly selected index case. The script does not check that published theorem or make any claim of independent certification.
