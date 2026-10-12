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

The exact local computation uses the coordinate presentation \(t=x^3+y^2-uw\) on the blow-up chart containing the critical set. The differential ideal is \((x^2,y,u,w)\); the second blow-up chart has base derivative \(-1\). The public checker \(\texttt{verify.py}\) reproduces the local Gröbner basis over \(\mathbb Q\) and the relevant cyclic weight relations. The checker printed \(\texttt{ELLIPTIC_CRITICAL_RIBBON_LOCAL_OK}\) in the recorded run.

The global assertions are verified by proof, not by finite enumeration. The center's critical locus occurs only over the six simple roots of the sextic; the finite cyclic action on the chosen elliptic curve is free. Descending the weight-two nilpotent coordinate along the connected degree-six isogeny produces a nontrivial order-three line bundle. Degree-zero cohomology and Serre duality on the elliptic quotient give the asserted vanishing for this torsion line bundle. These global arguments are not tested computationally.

The available source establishes the fivefold construction, its equivariant coordinates and its local singularity type; it does not directly state the complete descended critical scheme. Bibliographic priority beyond the sources identified remains subject to independent evaluation.
