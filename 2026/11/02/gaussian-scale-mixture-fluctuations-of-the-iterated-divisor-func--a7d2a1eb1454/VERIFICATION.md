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
# Reproducibility and verification

The exact prime-factor decomposition in the proof was verified by a standalone Python 3 program against direct divisor enumeration for every integer from \(1\) to \(200000\). The program independently computes the powerful part, squarefree prime-factor count, odd part of the divisor count, and directly counts divisors of \(\tau(n)\). Every identity agreed; 886 powerful-fiber values were observed and eight fixed-fiber frequency predictions were compared with exact analytic densities. Its prime-truncated smallest-scale probability was approximately \(0.687827\), consistent with empirical \(0.687870\) at this finite cutoff.

Run from this package directory with `python3 verify.py --bound 200000`. No nonstandard packages or network resources are required for that finite check.

The independent mathematical input is the classical Selberg–Delange/Erdős–Kac result on the number of distinct prime factors among squarefree integers with finitely many excluded primes. The proof writes the corresponding Euler product explicitly and shows how the characteristic-function limit follows. The code is not a certificate of this infinite analytic theorem; no finite enumeration establishes a distributional limit. No independent mathematical audit has been performed.
