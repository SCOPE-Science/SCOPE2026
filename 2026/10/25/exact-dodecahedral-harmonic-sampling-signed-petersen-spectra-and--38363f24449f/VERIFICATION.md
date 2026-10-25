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

# Verification notes

The single self-contained command is `python3 code/verify.py`, which uses the Python standard library only. Its expected stdout is in `code/verification_output.txt`.

The checker builds the 20 normalized dodecahedral directions using exact pairs \((a,b)\) representing \(a+b\sqrt5\), selects 10 antipodal representatives, and checks all 100 entries of each matrix identity \(A^2=2I-A+J\), \(B^2=3I+C\), and \(B^3=5B\). It then evaluates all three rational Legendre spectral branches at each degree from \(0\) through \(186\), with all inequalities and equality checks exact. It confirms the complete low-degree rank table, absence of further zeros through \(186\), and the unique smallest positive quotient eigenvalue \(3094/1594323\) at degree \(13\).

For the remaining infinite set of degrees, the written proof establishes the bound \(1-\sqrt{186/\ell}\) on active quotient eigenvalues; the checker verifies the exact rational inequalities that make the bound strict enough for all \(\ell\ge187\). The checker is an exhaustive finite arithmetic certificate plus a stated analytic argument, not an exhaustive evaluation of infinitely many degrees.

External independent mathematical review has not been performed, and priority among older equivalent formulations is not independently certified.
