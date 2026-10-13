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

The proof reduces the problem by the exact affine change of variables \(\phi(X)=aX+b/2\) to the three critical orbits of \(X^2\), \(X^2-1\), and \(X^2-2\). Those orbits are respectively constant at \(0\), alternating \(-1,0\), and equal to \(-2,2,2,\ldots\). Applying \(\phi^{-1}(z)=(2z-b)/(2a)\) gives every formula in the claim.

`verify_boundary.py` is a secondary exact-arithmetic replay. It enumerates many integral coefficient triples satisfying each boundary equation, directly iterates the original quadratic at its rational critical point, checks the closed formula at every tested index, and compares the actual rational-square predicate with the classified index set. It uses `fractions.Fraction` and `math.isqrt`; no floating-point arithmetic is used.

The replay is finite and is not presented as proof of the universal statement. The universal proof is the symbolic conjugacy and exhaustive three-orbit analysis above.
