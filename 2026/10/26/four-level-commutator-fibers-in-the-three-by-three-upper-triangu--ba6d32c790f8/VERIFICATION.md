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

Run `python3 verify.py` from the directory containing this document. The script uses only the Python standard library.

The checks enumerate all 4096 ordered pairs of upper triangular matrices over \(\mathbb F_2\) and all 531441 pairs over \(\mathbb F_3\), construct every commutator by two literal matrix products, and check the full \(q^3\)-target histogram against the claimed fiber formula. It separately checks the complete alternating-pairing rank strata for every dual target over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), using \(\mathbb F_4=\mathbb F_2[t]/(t^2+t+1)\), and checks the total-count identity for \(q=2,3,4,5,7,9,11\). The expected success line is `VERIFY_OK_TRIANGULAR_COMMUTATOR_FIBERS`.

Finite enumeration and the implemented rank checks do not prove the statement for all finite extension fields. The separate alternating-rank and Fourier-inversion argument in RESULT.md supplies the general proof. Publication priority and independent mathematical validation have not been established.
