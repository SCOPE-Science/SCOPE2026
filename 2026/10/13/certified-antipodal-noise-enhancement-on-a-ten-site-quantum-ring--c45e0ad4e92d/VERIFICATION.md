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

The proof uses a finite rational witness for the integrated density matrices at two exact dephasing rates. Run `python3 verify.py` with `certificate.json` in the same directory; only Python's standard library is required.

The executable performs exact integer reconstruction of both \(10\)-by-\(10\) complex residual matrices and checks \(S_0=244156\), \(S_{1/5}=187408\), their selected matrix entries, and the positive rational lower bound \(1385039389500/10^{14}\) for the transport-efficiency gain. No floating-point matrix inversion is used in certificate verification.

The global error bound follows from the proved dissipativity inequality \(\operatorname{Re}\langle X,\mathcal M_\gamma X\rangle\ge2\mu\|X\|_2^2\). This certifies a finite counterexample, not a general ring-size classification, an optimal-noise calculation, or a finite-time improvement. A separate independent scientific audit has not been performed.
