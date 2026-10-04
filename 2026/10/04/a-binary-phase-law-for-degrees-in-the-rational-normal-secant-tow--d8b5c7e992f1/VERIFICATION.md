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
The geometric degree formula used is
\[
D_{d,k}=\binom{d-k}{k+1}
\]
for
\[
0\le k\le\left\lfloor\frac{d-2}{2}\right\rfloor.
\]

Kummer's theorem gives the exact base-\(p\) carry count, and Legendre's formula gives the equivalent digit-sum expression. Lucas's theorem modulo two is used for the whole-tower classification.

The bundled checker verifies the valuation formula against direct factorial valuations for several primes through \(d=500\), checks the all-even dimensions, and confirms the exact first odd index whenever one exists. These computations are finite regression checks only.

Unproved by the checker and instead proved symbolically: the assertions for all \(d\), all admissible \(k\), and every prime \(p\).
