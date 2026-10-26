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

# Reproducibility and limits

Run `python3 verify.py` with the Python standard library. It confirms the fourteen Koszul identities and exact rational ranks for all fifteen coordinate four-planes. The counts are three nonisotropic examples with dimensions (0,6) and twelve isotropic examples with dimensions (1,6) for the spaces of sections H0(E|C(-3)), H0(E|C(-2)). These coordinate tests do not imply the universal theorem; the exterior-square Euler-sequence proof, symplectic isotropy argument, and global generation bound in RESULT.md establish it for every smooth twisted cubic.

An additional direct linear syzygy check of the source's displayed matrix finds a fourteen-dimensional degree-one syzygy space whose evaluation at a coordinate point has rank nine; the symplectic action is transitive on P5 and preserves the construction. This supports the globally generated premise stated in the cited primary source.

The published comparison inspected the source papers arXiv:2610.20208v1 (full six-page construction), arXiv:2212.04228v1 (relevant symplectic Section 6.2), and arXiv:2306.04317v1 (general syzygy moduli framework). The existence of earlier structural descriptions is acknowledged. No computational experiment substitutes for the universal proof, and no independent audit has been performed.
