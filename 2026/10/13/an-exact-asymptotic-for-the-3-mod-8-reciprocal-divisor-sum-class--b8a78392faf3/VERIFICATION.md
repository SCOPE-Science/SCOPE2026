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

The proof of the asymptotic is analytic and does not depend on finite experimentation.

The attached `verify.py` checks the finite interface to the published structural theorem. It directly constructs the reciprocal of the parity generating function for \(\sigma(n)\) over \(\mathbb F_2\) through \(30000\). For every integer in that range congruent to \(3\pmod8\), it compares the reciprocal coefficient with the exact prime-square criterion
\[
n=p^{4j+1}k^2,
\qquad
p\equiv3\pmod8,
\qquad
k\text{ odd},
\qquad
p\nmid k.
\]
It also computes the exact number of structural members through \(10^6\).

The infinite proof uses two standard analytic inputs: the prime number theorem in the fixed residue class \(3\pmod8\) and the Chebyshev bound \(\pi(y)\ll y/\log y\). The higher exponent layers and the coprimality correction are each \(O(\sqrt X)\), so neither changes the \(X/\log X\) main term.
