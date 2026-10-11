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

The symbolic verification artifact `artifacts/verify_threshold.py` was executed on the packaged equations. It checks:

- \(\det M(a,\rho)=-F(a,\rho)/4\);
- \(\operatorname{disc}_a F=120P(\rho)\);
- \(\operatorname{disc}_x Q=12000P(\rho)\);
- exactly two positive real roots of \(P\), isolated respectively in \((2.188758,2.188759)\) and \((3.355161,3.355162)\);
- two roots of \(F(\cdot,1)\) in \((0,2)\), but none for \(\rho=5/2\) or \(\rho=4\);
- zero, two, and four real roots of the equilibrium quartic at \(\rho=1\), \(\rho=5/2\), and \(\rho=4\), respectively;
- the exact coefficient expansion that forces the centered quadratic weight family.

The saved output is `artifacts/verification_output.txt` and begins with `ALL_VERIFY_OK`.

The finite sample parameters in the root-count checks are not used as empirical evidence for an infinite parameter interval. The discriminant calculation proves that root topology can change only at the isolated positive roots of \(P\), while the endpoint identities \(F(0,\rho)=-10\) and \(F(2,\rho)=-4\rho^2\) exclude boundary crossings for \(\rho>0\). Thus exact algebra plus Sturm counts controls the whole interval.

No claim is made about translated quadratic or nonquadratic Lyapunov functions. At \(\rho=\rho_*\), the nonzero equilibrium born at the saddle-node prevents global attraction of the origin even though this does not imply loss of local stability there.
