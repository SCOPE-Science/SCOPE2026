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

The expected final number infected is reconstructed from the exact first-jump equation on states \((s_1,i_1,s_2,i_2)\); no mean-field or branching approximation enters the calculation. With two people per patch, every infection reduces the remaining susceptible count, and every recovery decreases the infected count, ensuring a terminating recurrence.

Run `python -m pip install -r requirements.txt` followed by `python verify.py`. Checks include the symbolic endpoint values and derivatives for all positive transmission ratios, the sign-changing quartic, the complete rational mean at ratio four, the degree-eight derivative, a Descartes sign certificate after mapping the physical interval to positive reals, and an exact positive outbreak-size difference at mixing \(99/100\). A separately coded labelled-person process reproduces mean outbreak sizes at four rational mixing levels.

The numerical optimizer and critical transmission ratio are only approximations to algebraically defined numbers. The proof of their existence, sign and uniqueness is exact. The conclusion is confined to the stated Markovian four-person two-community model, with recovery rate normalized to one.
