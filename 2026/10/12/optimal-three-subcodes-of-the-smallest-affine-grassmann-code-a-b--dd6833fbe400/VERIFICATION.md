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

For C^A(2,4), V=⟨1,a,b,c,d,det⟩ is 6-dimensional and evaluation on all q^4 matrices is injective, including q=2. A 3-dimensional subspace D of V has at most q² common zeros: if the determinant coefficient vanishes then three independent affine equations give at most q points, while otherwise two independent affine equations cut at most an affine two-plane and a determinant equation only reduces it. Equality means D is precisely the 3-dimensional kernel of evaluation on an affine plane where det restricts to an affine function. For q>2, vanishing of det on the 2-dimensional direction is equivalent to a fixed image line or fixed kernel line of rank-1 matrices, giving 2(q+1) directions and q² translates. For q=2 quadratic s²,t² reduce to linear functions and the only obstruction is the alternating nondegenerate symplectic polar pairing, giving 15 isotropic directions times 4 translates =60. Hence d3=q⁴−q², N_q=60 for q2 and 2q²(q+1) for q>2. Independent direct finite field direction enumeration confirmed 15 for q2, 8 for q3 and translation counts 60/72; this does not substitute for algebraic all-prime-power proof.

## originality

PASS

Best-of-knowledge originality of the narrow final statement, not a general absence certificate. Exact multiplicity and geometry of optimal 3-subcodes exceed known generalized weight values or codeword spectra.

## value

PASS

The third generalized-weight *value* is background. Exact multiplicities and a complete classification of optimal 3-subcodes are independently meaningful code-support invariants, and the exceptional field-two symplectic geometry is an instructive sharp boundary not visible in generic rank-one matrix rulings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
