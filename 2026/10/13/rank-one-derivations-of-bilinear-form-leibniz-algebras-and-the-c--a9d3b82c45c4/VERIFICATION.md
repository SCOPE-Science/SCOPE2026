---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The derived ideal is Kz, so D(z)=az. If a is nonzero a rank-one image is Kz, which makes the right-hand side of the derivation law zero and contradicts aB≠0. Write the remaining noncentral case as D(v)=ψ(v)(u+cz). Applying the law with one argument in ker ψ forces both B(u,−) and B(−,u) to be multiples of ψ, and with both arguments outside that kernel their coefficients sum to zero. Nondegeneracy makes the first coefficient nonzero. This yields precisely the stated normal form on W_B, including the converse and the uniqueness for fixed projective representatives. Squaring gives D²=tB(u,u)D. The central type contributes qⁿ−1, each line in W_B contributes q(q−1), and in characteristic two the square root of B(u,u) on W_B is a linear functional over the finite field. If it is nonzero exactly q^(r−1) lines lie outside its kernel, each giving q maps per prescribed nonzero scalar. In odd characteristic 2B(u,u)=0 on W_B, so that exceptional case cannot occur. Independent direct basis-pair tests using normalized rank-one factors corroborated, for example, totals 75 and idempotent counts 16 versus 0 for I₂ and the alternating plane over F₄. Over F₄ with B=diag(1, [[1,1],[0,1]]), r=1, the observed counts by scalar were 63,4,4,4, testing a proper symmetrization radical. These are bounded reproductions; the tensor-factor argument supplies the universal proof. The frozen verification file and checker were inspected, not executed.

## originality

PASS

Prior structural and derivation-matrix results explain overlap in the classical examples. No inspected result covers the arbitrary nondegenerate bilinear form with central lift and the characteristic-two rank-one counts. Credit is for the uniform rank stratum and the precise exceptional count, not for the isometry-algebra reduction or the alternating transvection formula in isolation.

## value

PASS

This natural smallest nonzero stratum of a derivation algebra is useful even without a higher-rank classification. The rank-one idempotent obstruction changes in characteristic two and is not determined by the dimension of the symmetrization radical. The criterion and exact multiplicities distinguish algebras with identical rank-one totals but different possible projection derivations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
