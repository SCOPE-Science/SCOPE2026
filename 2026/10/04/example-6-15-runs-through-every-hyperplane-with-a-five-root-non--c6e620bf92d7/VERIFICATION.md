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
`artifacts/verify.py` uses only the Python standard library.

It realizes
\[
\mathbb F_{64}=\mathbb F_2[a]/(a^6+a+1)
\]
and first verifies that \(a\) has multiplicative order \(63\). The subfield \(\mathbb F_4\) is recovered as the fixed set of \(x\mapsto x^4\), and the relative trace is computed as
\[
\operatorname{Tr}_{64/4}(x)=x+x^4+x^{16}.
\]

For every \(\rho\in\mathbb F_{64}\), the verifier constructs
\[
\phi_\rho(x)=\rho x+x^4,
\qquad
\phi_\rho^\dagger(y)=\rho y+y^{16}.
\]
It checks that exactly \(21\) nonzero parameters satisfy \(\rho^{21}=1\), and for each such parameter it exhausts all \(64\) inputs to obtain the exact image and adjoint kernel.

It verifies that every singular image has \(16\) elements, that the \(21\) singular images are pairwise distinct, and that each image equals \(y^\perp\) for any nonzero \(y\) in its adjoint kernel. It separately enumerates all projective normal lines and confirms that these give exactly the same \(21\) hyperplanes.

Finally, it computes each hull directly by intersection, confirms that exactly five singular images have one-dimensional hull, and checks that their parameter set is exactly the root set of
\[
\rho^5+\rho^4+1.
\]
It also confirms the full \(60\)-LCD/\(5\)-non-LCD projective distribution. Successful replay prints `VERIFY_OK`.
