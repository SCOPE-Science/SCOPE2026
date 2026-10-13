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

Run `python3 verify.py` with Python 3 and the standard library. Execution of the source included here returned `VERIFY_OK`. The program computes exact determinants in the quotient ring \(\mathbb Z[t]/(t^4+1)\) and compares the full 1,128-pair incidence matrix with a separately calculated rank matrix over \(\mathbb F_{17}\), using the specialization \(t=2\). It exhausts all 13,824 candidate triples of four-line systems and checks their compatibility without sampling. It constructs the complete monomial projective group from six generators and its action, and checks the complete four-element Galois action. It also verifies line-degree and pairwise-system intersection consistency counts.

Verified assertions: 48 lines; 128 twelve-skew systems; projective orbit sizes 32 and 96; stabilizers 48 and 16; Galois fixed counts 128,16,128,16; 16 rational systems and 112 systems minimally over \(\mathbb Q(i)\). All statements are restricted to the standard all-plus quartic over characteristic zero. These computations constitute finite exact verification, not an external independent audit.
