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

The proof is unbounded. Its four critical ingredients are: the inductive least-height threshold \(E_j\); the exact binary factorial valuations \(\nu_2((E_{k-1}+1)!)=E_{k-1}-1\) and \(\nu_2((E_{k-1}+2)!)=E_{k-1}\); the lcm valuation identity \(\nu_p(L(N))=\lfloor\log_p N\rfloor\); and Bertrand's prime in \((N^{1/(a+1)},N^{1/a})\) when \(a\ge16\), with direct primes at levels \(3,4\).

`verify.py` runs exact integer computations using only the Python standard library. The accompanying `verification_output.txt` is its actual output. The program tests two consecutive factorial indices around each of the first five hitting thresholds, two consecutive lcm indices around each of the first four hitting thresholds, the lcm plateau endpoint and immediate next index for levels \(3,4\), and the first 511 lcm indices for unexpected earlier records. Those finite checks are not a substitute for the unrestricted symbolic argument. The existence of the prime in each higher-level interval is mathematical (Bertrand's postulate), not inferred by trial enumeration.
