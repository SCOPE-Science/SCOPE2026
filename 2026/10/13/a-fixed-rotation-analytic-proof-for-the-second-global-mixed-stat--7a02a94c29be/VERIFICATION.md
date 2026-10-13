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

# Verification

Run `python3 verify.py` in the same directory.  The checker reconstructs the two MEMS branches, the fixed local rotation, and the Cartan gate symbolically with \(c=\cos\chi\) and \(s=\sin\chi\).  It verifies that the characteristic-polynomial error is divisible by \(c^2+s^2-1\), so the displayed partial-transpose spectra hold for the entire continuous parameter interval rather than a sampled grid.

It also verifies the purity identities \(\mu=1/3+\gamma^2/2\) on the rank-three branch and \(\mu=\gamma^2+(1-\gamma)^2\) on the rank-two branch, with the common endpoint \(\mu=5/9\) at \(\gamma=2/3\).

The checker does not establish literature originality, does not classify all perfect entanglers, and does not extend the two-qubit PPT criterion to higher dimensions.  Those are outside the scientific claim.
