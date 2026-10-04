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
The analytic check starts from the exact half-flux band condition published for the magnetic square lattice with preferred-orientation coupling. With \(N_n=n\pi\) and \(k=N_n+x/N_n\), Taylor expansion gives
\[
R(k)=6-\frac8{x^2}+N_n^{-2}\left(-8x^2+\frac{88}{3}+\frac{16}{x}-\frac{16}{x^2}\right)+O(N_n^{-4}).
\]
The four limiting edge parameters are therefore \(-\sqrt2,-1,1,\sqrt2\), and the implicit-function calculation gives the stated edge corrections.

`artifacts/verify.py` replays the exact published \(R(k)\) numerically using only the Python standard library. It brackets and bisects the four equations \(R(k)=\pm2\) at \(n=10,20,40\), verifies the band-edge ordering, and checks that the difference between each exact translated energy and its two-term asymptotic remains bounded after multiplication by \(N_n^4\). The script returns `VERIFY_OK`.

The numerical replay is finite and is not a proof of the asymptotic statement. The proof uses Taylor expansion plus the implicit-function theorem at four simple limiting roots. No claim is made for flux values other than \(\Phi=\pi\), or for the wide high-energy band family.
