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

The proof is an exact boundary-equation reduction. For a one-loop-supported state, Eqs. (4.24) and (4.25) force both loop endpoint values to vanish. Positive energy therefore gives \(k=n\pi\). Equation (4.27) then reduces to \(e^{i(\alpha_2-\alpha_1)}=(-1)^n\). The explicit loop function \(\sin(n\pi x)\) proves sufficiency.

`verify.py` replays this reduction using exact integer parity data for \(1\le n\le20\). It checks both phase roots \(e^{i\alpha}=1\) and \(e^{i\alpha}=-1\), confirming that the derivative residual vanishes exactly for the root matching \((-1)^n\). The finite replay is only a consistency check; the proof covers every positive integer \(n\).

Limit: this verification concerns one-loop-supported states only. It does not enumerate or exclude compact states using more than one loop.
