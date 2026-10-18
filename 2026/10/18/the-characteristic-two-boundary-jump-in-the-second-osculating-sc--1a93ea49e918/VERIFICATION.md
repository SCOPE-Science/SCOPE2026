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

# Exact arithmetic verification

Execute `python3 verify.py` with a standard Python 3 interpreter. No external Python dependencies or network calls are used. The script independently constructs the six Hasse rows from the exponent vectors and integer binomial coefficients, then computes all 36 size-five determinants and the size-six determinant by Leibniz expansions. Eighteen size-five minors are nonzero and every nonzero minor is a single signed monomial with coefficient one or two.

The minors include \(-2u^2\), \(-uv\), and \(-2v^2\). Every other size-five minor is in \((2u^2,uv,2v^2)\), so the generated ideal is exactly that integral ideal. Modulo every odd prime or over characteristic zero, it becomes \((u,v)^2\). Modulo two, it becomes \((uv)\). The script also checks the characteristic-two ranks at the four support patterns \((0,0),(0,1),(1,0),(1,1)\), obtaining \((3,4,4,5)\). It reports `VERIFY_OK` on success; this run produced that output.

This computation is exhaustive for the displayed fixed-size integer matrix. The independent mathematical part of the global proof is the six-chart toric cover: each vertex chart is \(\operatorname{Spec}k[u,v]\), the permutation action identifies the charts, and coordinate axes glue into the hexagonal boundary. Thus no finite-field enumeration is treated as an infinite proof.

Limitations: The checker does not classify other toric embeddings or different jet orders, and it does not substitute for an independent mathematical audit. The identified complex-reference results and possible unpublished equivalent characteristic-two computations impose the stated originality qualifications.
