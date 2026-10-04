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
The universal statement is proved analytically. The key checks are:

1. Normalize the four coefficient moduli to one and rewrite the Fourier zero equation as \(1+Z+W+\eta ZW=0\).
2. For \(\eta=1\), verify the exact factorization \((1+Z)(1+W)\).
3. For \(\eta\ne1\), solve for \(W\), impose \(|W|=1\), and derive \(Z^2=\eta^{-1}\), giving exactly the two unit-torus zeros \((s,-s)\) and \((-s,s)\).
4. Check grid membership: once one zero is present, its antipode is present exactly when both cyclic orders are even.
5. Verify the explicit witnesses for the four factorable counts and for the parity-dependent isolated count.

The standalone script `artifacts/verify.py` directly evaluates the discrete Fourier transform for every \(2\le m,n\le40\) on the explicit witnesses. It is a finite corroboration only; no conclusion for larger moduli is inferred from the computation.
