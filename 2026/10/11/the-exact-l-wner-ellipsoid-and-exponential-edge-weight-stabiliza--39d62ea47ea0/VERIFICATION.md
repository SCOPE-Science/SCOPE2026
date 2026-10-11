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
# Reproducibility and scope

Run `python3 verify.py` using Python 3.10 or newer, standard library only. The program was executed from its own directory and printed `VERIFY_OK: 78 exact endpoint identities, three algebraic factors, 18 finite resistance contact pairs, and exponential asymptotic checks.` It uses exact integer polynomial arithmetic for the product and endpoint identities, and floating-point Gaussian elimination for independent effective-resistance calculations. It also evaluates representative high-dimensional asymptotics. The program is not an infinite-dimensional proof, an exhaustive literature search, or an independent audit. The universal result is supported by the analytic four-part proof in RESULT.md. No external services, private records, or pre-existing run logs are required to replay the code.
