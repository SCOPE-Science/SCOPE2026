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

# Verification record

The proof of the universal cusp uses the nonzero exact coefficient constants \(C_2=-m/[2(m+1)]\) and \(C_3=-m(m-1)/[3(m+1)^2]\), valid for all integers \(m\ge2\). Coprime analytic cluster factorization, valid over \(\mathbb C\), establishes the two independent local models. At the two-root stratum, the fiber-product exact sequence computes the local depth and the failure of \(S_2\).

To reproduce finite spot checks, install the declared SymPy dependency and run `python checks/verify_multiple_root_germs.py`. The checker tests eleven centered coefficient systems, 28 ambient tangent-space cases, and 105 Hilbert-function cases; all passed in the included output. The checker and its recorded output are included to support reproducibility. These checks cannot certify all integers \(m,d\); the proof covers all parameter values.

Formal local-ring identifications require the *reduced* image and exact root partitions. Claims of analytic structure at deeper collisions are not established. The singular-support classification is prior work, and an earlier Hilbert-function paper remains a literature risk. Independent mathematical audit has not occurred.
