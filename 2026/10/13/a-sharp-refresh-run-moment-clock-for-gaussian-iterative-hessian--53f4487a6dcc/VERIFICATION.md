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

# Verification and reproducibility

The proof's integrability mechanism is the gamma density \(h_\ell(w)\) near zero, with the exact condition \(\ell>2qr\) for a block of length \(r\) in moment order \(q\). No finite numerical experiment establishes infinite moments. The Bernoulli no-refresh event has strictly positive probability at every fixed horizon when \(0<p<1\). The ergodic theorem requires \(p>0\), and logarithmic integrability is independently checked analytically.

`verify.py` is a standalone exact-rational checker, with no external package dependency. Execute `python verify.py`. It checks 1,275 algebraic and boundary instances, including \(\ell=6\), \(\eta=1/3\), and the exactly finite or divergent two-step cases. The program does not claim to certify arbitrary real parameters or asymptotic probability limits. For full verification, compare the density asymptotics, conditional-block factorization, inverse gamma moments, and ergodic argument in RESULT.md.

The selected source was first publicly posted on arXiv on 2019-11-06; its later revisions do not change that date. This manuscript makes no claim of independent external audit.
