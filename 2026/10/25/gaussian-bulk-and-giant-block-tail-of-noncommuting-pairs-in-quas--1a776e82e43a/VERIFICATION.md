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

# Reproducibility and boundaries

Run `python checks/check_quasitrivial.py` using the Python 3 standard library. The script independently enumerates \(4^{\binom n2}\) quasitrivial multiplication tables for each \(1\le n\le4\), evaluates associativity directly on triples, counts unordered noncommuting pairs, and compares the resulting polynomial with the block-composition recurrence. These four cases involve 1, 4, 64, and 4,096 candidate tables, respectively, and total 4,165.

The observed numbers of associative quasitrivial laws are 1, 4, 20, and 138. At \(n=4\), direct enumeration and recurrence both give \(24+72w+24w^2+16w^3+2w^6\). The script also compares unmarked totals through \(n=8\) to published enumeration and reports moments from exact recurrence arithmetic through \(n=60\). The numerical coefficients \(\rho\), \(\alpha\), and \(\beta\) agree with the equations in RESULT.md.

The general central limit theorem is proved by the uniform complex-pole coefficient expansion of the real-parameter characteristic function. The superexponential tail law is proved by a direct large-block factorial upper bound and a one-large-block construction. Finite tests do not establish either infinite limit or historical novelty. Independent audit remains unperformed.
