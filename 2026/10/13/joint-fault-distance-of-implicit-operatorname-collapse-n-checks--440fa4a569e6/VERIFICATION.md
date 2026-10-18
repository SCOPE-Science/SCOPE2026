---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The root observable L=∏X_i commutes with each modeled X_i while LS_j with S_j=Z_j Z_(j+1) changes sign on domain walls x_j⊕x_(j+1). Cancelling ideal common signs proves e_j⊕e0=x_j⊕x_(j+1). Pure faults require constant e or constant x; mixed weight-two witness is X_1 plus first-check flip, and no weight-one pair is accepted. For e0=1, total weight k+n−t with t transitions and k ones, t<=min(2k,n−1), yielding minimum floor(n/2)+1 attained alternating. Transition generating function G=(1−q,q)[[1−q,qr],[(1−q)r,q]]^(n−1)(1,1)^T produces A0=(1−p)^n G(p/(1−p);q), A1=p^n G((1−p)/p;q). At equal small rates, positivity gives the exact exponent. Exhaustive independent x,e enumeration through n=9 corroborated these distances; no circuit-level claim.

## originality

PASS

Best-of-knowledge PASS for simultaneous effective patch-X/classical-readout acceptance kernel and sharp mixed sign distance and stochastic profile; SOURCE Smith et al already explicitly claim pure readout detection to order n−1, which is credited. Generic quantum data-syndrome literature motivates mixed errors but supplies no implication giving this particular collapse(n) measurement kernel.

## value

PASS

The exact mixed-fault distance exposes a materially smaller hidden postselection failure threshold than either isolated fault channel, directly useful for interpreting the ideal check gadget and extrapolating effective phenomenological noise. The transfer law supplies a precise conditional sign-error rate, not just a low-n counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
